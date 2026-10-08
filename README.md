# chat-handoff

An open-source [Agent Skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) that compresses a long conversation into one compact brief you paste into a fresh chat. You keep your context, and the new chat starts small.

**Quick install:** download [chat-handoff.zip](https://github.com/kaktech/chat-handoff/releases/latest/download/chat-handoff.zip) and upload it in claude.ai under Customize > Skills. Claude Code users: see [Install](#install).

Say "this chat is getting long" or "hand off". You get one code block to copy, plus one line telling you where to paste it.

## Why it saves usage

Every reply in a chat is generated with the whole conversation so far as input. A long chat therefore makes each new message heavier than the last, and the chat approaches the context limit. Usage limits on most plans are tied to how much text is processed, so long chats tend to use up your allowance faster than the same questions asked in short chats. A brief that carries only decisions, facts and state lets a new chat start from a small base instead of the full history.

## How much does this save?

No exact number, because it depends on your plan, your model, how long the chat is, and whether caching applies. What holds in general:

- The later a message is in a long chat, the more earlier text rides along with it.
- A brief is typically a small fraction of the chat it replaces. Each brief reports its own rough size comparison, labelled as an estimate.
- You save most when you hand off before the chat gets very long, then continue in the new one.
- Savings are lost if the brief is padded or if the new chat has to re-ask what the old one knew. That is why the skill keeps decisions, exact values and rejected options.

Measure it yourself: compare the length of a brief with the chat it came from (the skill prints the estimate), and watch your usage meter over a few days.

## What the brief contains

1. Goal
2. Decisions made
3. Key facts
4. Current state
5. Open items / next step
6. Style and preferences
7. Files and artifacts
8. Do not redo (with reasons)

It ends with a Resume line: "Continue from Open items. Do not re-ask answered questions."

## Features

- **Three lengths**: Mini (cap 150 words), Standard (cap 400, default), Full (cap 900). Say "mini handoff" or "full handoff".
- **Six modes**: general, coding, writing, research, business, study. Auto-detected, overridable ("coding handoff").
- **Privacy pass**: API keys, passwords, tokens, personal IDs and card numbers become `[REDACTED]`, and you get a warning.
- **Fidelity rules**: nothing invented, uncertain items marked `unconfirmed`, exact numbers, names and code identifiers, your own wording for requirements.
- **Self-check** before output: nothing decided is missing, nothing is fabricated, word cap respected.
- **Your language**: the brief is written in the language of the chat.
- **Lean Mode** (optional, off by default): cuts preambles, restated questions and closing recaps.
- **Edge cases**: very short chats (no handoff needed), attachments (listed, not pasted), unrelated topics (one brief per topic).

## Install

The skill follows the official format: a folder named `chat-handoff` with `SKILL.md` (frontmatter `name` and `description`) and optional supporting files.

### claude.ai (Pro, Max, Team, Enterprise; code execution must be enabled)

1. Run `bash scripts/package.sh`. It validates the skill and writes `dist/chat-handoff.zip`. The zip has the `chat-handoff/` folder at its root, as claude.ai requires.
2. In claude.ai open Customize > Skills (older UIs: Settings > Features), upload `chat-handoff.zip`, and enable the skill.
3. Custom skills are per user on claude.ai. Each team member uploads their own copy.

### Claude Code

Copy the folder (not the zip) to `~/.claude/skills/chat-handoff/` for all projects, or `.claude/skills/chat-handoff/` for one project.

### Claude API

Upload the zip through the Skills API (`/v1/skills`) and reference its `skill_id` with the code execution tool. See the official [Skills guide](https://platform.claude.com/docs/en/build-with-claude/skills-guide).

Skills do not sync between surfaces. Install on each one you use.

## Usage

| You say | You get |
|---|---|
| "this chat is getting long" | Standard brief (about 400 words max) |
| "mini handoff" | Brief of 150 words max |
| "full handoff" | Brief of 900 words max |
| "coding handoff, full" | Coding template, Full length |
| "lean mode on" | Shorter replies for the rest of the chat |

Then open a new chat and paste the brief as your first message. Re-attach any files the brief lists.

See `examples/` for finished briefs.

## FAQ

**Does the new chat remember everything?** No. It knows what is in the brief. The brief keeps decisions, exact facts and rejected options, and drops chatter.

**Can the skill read my other chats?** No. It only sees the current conversation.

**Is anything sent anywhere?** The skill runs inside your chat. It makes no network calls. The scripts in `scripts/` are for maintainers and are not included in the upload zip.

**What if a secret slipped through?** The privacy pass is pattern-based and cannot catch everything. Read the brief before pasting it anywhere.

**Why not just paste the whole chat?** That keeps the cost you wanted to avoid.

## Limitations

- It summarizes from the conversation text the model can see. In very long chats the model's own recall of early messages may be imperfect, so skim the brief for gaps.
- Word counts and the "N times shorter" note are estimates.
- Redaction is best effort, not a guarantee.
- It cannot carry attachments, images or tool state into the new chat.
- Auto mode detection can be wrong on mixed chats. Override it.

## Decisions and assumptions

- **Description length**: the API docs and the Agent Skills specification allow 1,024 characters, and this skill's description uses about 580. One help-center page describes a shorter limit for claude.ai. If an upload is rejected for length, shorten the `description` in `SKILL.md` and keep the trigger phrases first.
- **SKILL.md size**: capped at 150 lines by this project (official guidance is under 500).
- **Zip contents**: only `SKILL.md`, `references/`, `examples/` and `LICENSE`. Docs, tests and scripts stay out to keep the skill small.
- **Mini** omits sections that have no content; Standard and Full keep all eight.
- **Word caps** are hard maximums, counted over the whole brief including headings.
- Lean Mode is a ruleset the chat applies while on; there is no persistent setting between chats.

## Development

```bash
python3 scripts/validate.py   # checks frontmatter, structure, templates, examples, word caps
bash scripts/package.sh       # validates, then builds dist/chat-handoff.zip
```

Requires Python 3.8+ and `zip`. No third-party packages. See `CONTRIBUTING.md` and `tests/`.

## License

MIT. See `LICENSE`.
