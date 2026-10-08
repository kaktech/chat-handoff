---
name: chat-handoff
description: Compresses a long conversation into one compact handoff brief the user can paste into a fresh chat, so they keep full context and save usage limits. Use when the user says "new chat", "this chat is getting long", "hand off", "handoff", "summarize so I can continue", "wrap up this conversation", "continue in a fresh chat", "save my progress", or "context is getting full". Offers Mini, Standard and Full lengths, templates for general, coding, writing, research, business and study chats, automatic redaction of secrets, and an optional Lean Mode that trims preambles and recaps.
license: MIT
metadata:
  version: "1.0.0"
  repository: chat-handoff
---

# Chat Handoff

Turn the current conversation into one pasteable brief. Work from the conversation only. Never invent.

## Workflow

1. **Check the chat is worth handing off.** If it is very short, has a single topic with no decisions, or covers several unrelated topics, read `references/edge-cases.md` first and follow it.
2. **Pick the length tier.** Default Standard. "mini handoff" = Mini. "full handoff" = Full.

   | Tier | Hard cap | Keep |
   |---|---|---|
   | Mini | 150 words | Goal, Decisions, Current state, Next step, Do not redo (one line each) |
   | Standard | 400 words | All 8 sections, short |
   | Full | 900 words | All 8 sections, with detail and exact values |

3. **Pick the mode.** Detect it from the conversation. The user can override ("coding handoff"). Read only the matching template:
   - `references/templates/general.md` (default, or mixed content)
   - `references/templates/coding.md` (code, repos, errors, commands)
   - `references/templates/writing.md` (drafts, edits, voice, audience)
   - `references/templates/research.md` (sources, claims, verification)
   - `references/templates/business.md` (plans, stakeholders, deadlines, numbers)
   - `references/templates/study.md` (learning, exam prep, practice)
4. **Extract.** Scan the whole conversation, not just the last messages. Collect goal, settled decisions, facts, state, open items, preferences, files, rejected approaches.
5. **Privacy pass.** Read `references/privacy-redaction.md`. Replace secrets and personal IDs with `[REDACTED]`. Remember what was removed.
6. **Fidelity pass.** Read `references/fidelity-rules.md`. Verbatim names, numbers and identifiers. Mark guesses `unconfirmed`. Quote the user's own wording for requirements.
7. **Self-check.** Before presenting:
   - Every decision, constraint and rejected approach in the chat appears in the brief or was deliberately dropped as irrelevant.
   - Nothing in the brief is absent from the chat.
   - Word count of the brief is at or under the tier cap. If over, cut in this order: style details, file details, low-impact facts, examples. Never cut Goal, Decisions, Next step, Do not redo.
   - No secrets remain.
8. **Present** using the output format below.

## Brief format

Write the brief in the language the user used in the chat. Use this skeleton. Omit a section when it has no content, except Goal and Open items / next step.

```
# Handoff: <topic> | <mode> | <tier>
## Goal
## Decisions made
## Key facts
## Current state
## Open items / next step
## Style and preferences
## Files and artifacts
## Do not redo
Resume: Continue from Open items. Do not re-ask answered questions. Treat Decisions made as settled unless I say otherwise.
```

Section order stays fixed so any new chat can parse it. Mode templates change what each section emphasizes. Do not add commentary inside the brief.

## Output format

Reply with exactly:

1. The brief in one code block. If the brief itself needs a code block, use a four-backtick outer fence.
2. One line: `Paste this as the first message of a new chat.`
3. One line: `Brief is about N words; this chat is about M words, so roughly X times shorter (estimate).` Estimate M from the conversation. Do not claim exact token savings.
4. Only if something was redacted: `Heads up: I replaced N item(s) (types: ...) with [REDACTED]. Re-add them yourself in the new chat if needed.`
5. Only if the mode was auto-detected and unclear: one line offering a different mode.

Add nothing else: no preamble, no recap, no sign-off.

## Attachments

If files were attached or pasted, list their names and what each is for under Files and artifacts. Do not paste their contents. Say the user must re-attach them in the new chat.

## Lean Mode (off by default)

Enable only when the user asks ("lean mode on", "keep replies short"). Read `references/lean-mode.md` and apply its rules to every later reply. Offer it once, in the heads-up line, only if the user has complained about long replies.

## Examples and tests

For output quality reference see `examples/example-general.md`, `examples/example-coding.md`, `examples/example-writing.md`. Read one only when unsure how a finished brief should look. Test scenarios are in `tests/test-cases.md`.
