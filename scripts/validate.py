#!/usr/bin/env python3
"""Validate the chat-handoff skill folder.

Usage: python3 scripts/validate.py [path-to-skill-folder]
Exit code 0 = no errors (warnings allowed), 1 = errors found.

Limits come from the official Agent Skills docs:
  name: <=64 chars, lowercase letters/digits/hyphens, no leading/trailing/double
        hyphen, no "anthropic"/"claude", must equal the folder name.
  description: 1..1024 chars, no XML tags.
  SKILL.md body: under 500 lines (this project sets a stricter 150-line cap).
"""
import os
import re
import sys

REQUIRED_FILES = [
    "SKILL.md", "README.md", "CHANGELOG.md", "LICENSE", "CONTRIBUTING.md",
    "references/templates/general.md", "references/templates/coding.md",
    "references/templates/writing.md", "references/templates/research.md",
    "references/templates/business.md", "references/templates/study.md",
    "references/privacy-redaction.md", "references/fidelity-rules.md",
    "references/lean-mode.md", "references/edge-cases.md",
    "examples/example-general.md", "examples/example-coding.md",
    "examples/example-writing.md",
    "tests/test-cases.md", "tests/checklist.md",
    "scripts/validate.py", "scripts/package.sh",
]
TEMPLATES = ["general", "coding", "writing", "research", "business", "study"]
SECTIONS = [
    "Goal", "Decisions made", "Key facts", "Current state",
    "Open items / next step", "Style and preferences",
    "Files and artifacts", "Do not redo",
]
MINI_REQUIRED = ["Goal", "Decisions made", "Current state",
                 "Open items / next step", "Do not redo"]
CAPS = {"Mini": 150, "Standard": 400, "Full": 900}
RESUME_PREFIX = "Resume: Continue from Open items."
MAX_SKILL_LINES = 150
SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9]{20,}", r"ghp_[A-Za-z0-9]{20,}", r"AKIA[0-9A-Z]{16}",
    r"xox[abp]-[A-Za-z0-9-]{10,}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    r"\b(?:\d[ -]?){15}\d\b",
]

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def read(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as f:
        return f.read()


def parse_frontmatter(text):
    """Minimal YAML subset parser: top-level `key: value` and one-level maps."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    data, current = {}, None
    for line in m.group(1).split("\n"):
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            if current is not None and isinstance(data.get(current), dict):
                k, _, v = line.strip().partition(":")
                data[current][k.strip()] = v.strip().strip('"')
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if v == "":
            data[k] = {}
            current = k
        else:
            data[k] = v.strip('"')
            current = None
    return data, text[m.end():]


def check_structure(root):
    for rel in REQUIRED_FILES:
        if not os.path.isfile(os.path.join(root, rel)):
            err("missing required file: " + rel)
    if os.path.isfile(os.path.join(root, "skill.md")) and not os.path.isfile(
            os.path.join(root, "SKILL.md")):
        err("file must be named SKILL.md (uppercase)")


def check_skill_md(root):
    if not os.path.isfile(os.path.join(root, "SKILL.md")):
        return
    text = read(root, "SKILL.md")
    fm, body = parse_frontmatter(text)
    if fm is None:
        err("SKILL.md: frontmatter missing or not closed with ---")
        return
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not name:
        err("frontmatter: name is required")
    else:
        if len(name) > 64:
            err("name longer than 64 characters")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
            err("name must be lowercase letters, digits, single hyphens, "
                "no leading/trailing hyphen")
        if re.search(r"anthropic|claude", name):
            err('name must not contain "anthropic" or "claude"')
        if name != os.path.basename(os.path.abspath(root)):
            err("name '%s' must match folder name '%s'"
                % (name, os.path.basename(os.path.abspath(root))))
    if not desc:
        err("frontmatter: description is required and non-empty")
    else:
        if len(desc) > 1024:
            err("description is %d chars; max 1024" % len(desc))
        if re.search(r"</?[A-Za-z][^>]*>", desc):
            err("description must not contain XML/HTML tags")
        if re.search(r"\b(I can|you can|I will|I'll)\b", re.sub(r"\"[^\"]*\"", "", desc), re.I):
            warn("description should be third person")
        for phrase in ["new chat", "this chat is getting long", "hand off",
                       "handoff", "summarize so I can continue",
                       "wrap up this conversation",
                       "continue in a fresh chat", "save my progress",
                       "context is getting full"]:
            if phrase.lower() not in desc.lower():
                err("description missing trigger phrase: '%s'" % phrase)
        print("  description length: %d / 1024 chars" % len(desc))
    for key in fm:
        if key not in ("name", "description", "license", "compatibility",
                       "metadata", "allowed-tools"):
            warn("unknown frontmatter field: " + key)
    n_lines = len(text.rstrip("\n").split("\n"))
    print("  SKILL.md lines: %d / %d" % (n_lines, MAX_SKILL_LINES))
    if n_lines > MAX_SKILL_LINES:
        err("SKILL.md has %d lines; project cap is %d"
            % (n_lines, MAX_SKILL_LINES))
    if "\\" in re.sub(r"```.*?```", "", body, flags=re.S) and re.search(
            r"\w\\\w+\.\w+", body):
        warn("possible Windows-style path in SKILL.md")
    # Every file referenced from SKILL.md must exist; none nested deeper than
    # one hop is enforced by only linking from SKILL.md.
    refs = set(re.findall(
        r"`((?:references|examples|tests|scripts)/[A-Za-z0-9_./-]+)`", body))
    for ref in sorted(refs):
        if not os.path.exists(os.path.join(root, ref)):
            err("SKILL.md references missing file: " + ref)
    for t in TEMPLATES:
        if "references/templates/%s.md" % t not in body:
            err("SKILL.md does not tell Claude when to read template: " + t)
    for r in ["privacy-redaction", "fidelity-rules", "lean-mode", "edge-cases"]:
        if "references/%s.md" % r not in body:
            err("SKILL.md does not reference references/%s.md" % r)
    for cap in CAPS.values():
        if str(cap) not in body:
            err("SKILL.md does not state word cap %d" % cap)


def check_templates(root):
    for t in TEMPLATES:
        rel = "references/templates/%s.md" % t
        if not os.path.isfile(os.path.join(root, rel)):
            continue
        text = read(root, rel)
        for s in SECTIONS:
            if not re.search(r"^## " + re.escape(s) + r"\s*$", text, re.M):
                err("%s: skeleton missing section '## %s'" % (rel, s))
        if RESUME_PREFIX not in text:
            err("%s: skeleton missing Resume line" % rel)
        if "| %s |" % t not in text:
            err("%s: header line should contain '| %s |'" % (rel, t))


def extract_brief(text):
    m = re.search(r"^## Brief\s*\n+```\n(.*?)\n```", text, re.S | re.M)
    return m.group(1) if m else None


def word_count(s):
    return len(s.split())


def check_examples(root):
    for ex in ["general", "coding", "writing"]:
        rel = "examples/example-%s.md" % ex
        if not os.path.isfile(os.path.join(root, rel)):
            continue
        text = read(root, rel)
        tier = re.search(r"^Tier:\s*(\w+)", text, re.M)
        cap = re.search(r"^Cap:\s*(\d+)", text, re.M)
        if not tier or tier.group(1) not in CAPS:
            err("%s: needs 'Tier: Mini|Standard|Full'" % rel)
            continue
        tier = tier.group(1)
        if not cap or int(cap.group(1)) != CAPS[tier]:
            err("%s: Cap must be %d for %s" % (rel, CAPS[tier], tier))
        brief = extract_brief(text)
        if brief is None:
            err("%s: no '## Brief' section with a code block" % rel)
            continue
        wc = word_count(brief)
        print("  %s: %d words (%s cap %d)" % (rel, wc, tier, CAPS[tier]))
        if wc > CAPS[tier]:
            err("%s: brief has %d words, cap %d" % (rel, wc, CAPS[tier]))
        if wc < CAPS[tier] * 0.25:
            warn("%s: brief far below cap (%d words)" % (rel, wc))
        needed = MINI_REQUIRED if tier == "Mini" else SECTIONS
        for s in needed:
            if not re.search(r"^## " + re.escape(s) + r"\s*$", brief, re.M):
                err("%s: brief missing section '%s'" % (rel, s))
        if not brief.rstrip().split("\n")[-1].startswith(RESUME_PREFIX):
            err("%s: brief must end with the Resume line" % rel)
        for pat in SECRET_PATTERNS:
            if re.search(pat, brief):
                err("%s: brief contains secret-like text (%s)" % (rel, pat))
        if "[REDACTED]" in text and "Heads up" not in text:
            err("%s: uses [REDACTED] but has no warning line" % rel)


def check_tests(root):
    rel = "tests/test-cases.md"
    if not os.path.isfile(os.path.join(root, rel)):
        return
    text = read(root, rel)
    n = len(re.findall(r"^## \d+\. ", text, re.M))
    print("  test scenarios: %d" % n)
    if n < 10:
        err("tests/test-cases.md has %d scenarios; need 10+" % n)
    if text.count("Must:") < n:
        err("each scenario needs a 'Must:' line")


def check_misc(root):
    lic = os.path.join(root, "LICENSE")
    if os.path.isfile(lic) and "MIT License" not in read(root, "LICENSE"):
        err("LICENSE should be the MIT License")
    pk = os.path.join(root, "scripts/package.sh")
    if os.path.isfile(pk) and not os.access(pk, os.X_OK):
        warn("scripts/package.sh is not executable (chmod +x)")
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.endswith(".md"):
                p = os.path.join(dirpath, f)
                if "\\" in os.path.relpath(p, root):
                    err("backslash in path: " + p)
                if os.path.getsize(p) == 0:
                    err("empty file: " + os.path.relpath(p, root))


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..")
    root = os.path.abspath(root)
    print("Validating " + root)
    check_structure(root)
    check_skill_md(root)
    check_templates(root)
    check_examples(root)
    check_tests(root)
    check_misc(root)
    for w in warnings:
        print("WARN  " + w)
    for e in errors:
        print("ERROR " + e)
    if errors:
        print("\nFAILED: %d error(s), %d warning(s)" % (len(errors), len(warnings)))
        return 1
    print("\nOK: 0 errors, %d warning(s)" % len(warnings))
    return 0


if __name__ == "__main__":
    sys.exit(main())
