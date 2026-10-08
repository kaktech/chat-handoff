# Coding template

Use for debugging, building features, code review, scripts, devops, data work in code.

## Emphasis

Key facts (stack, versions, repo state), Current state (errors, commands run), Files and artifacts, Do not redo. Identifiers are copied exactly: file paths, function names, flags, error text, versions.

## Brief skeleton

```
# Handoff: <project or bug> | coding | <tier>
## Goal
<what must work when finished; acceptance criterion if stated>
## Decisions made
- <architecture, library, approach chosen> (reason)
## Key facts
- Stack: <language, framework, versions, runtime, OS>
- Repo: <name, branch, last commit or uncommitted state if known>
- Constraints: <must not change X, perf limits, style rules>
- Error (exact): `<message or code>` at <file:line>
- Commands run: `<cmd>` -> <result>
## Current state
- Done: ...
- Half-done: <file and what is missing>
- Failing/blocked: <test or error, cause if known, else unconfirmed>
## Open items / next step
1. <first action, with file or command>
## Style and preferences
- <code style, comments, test framework, explanation depth, language>
## Files and artifacts
- `<path>`: <purpose>; last changed: <what>
## Do not redo
- <approach>: <why it failed, with error if known>
Resume: Continue from Open items. Do not re-ask answered questions. Treat Decisions made as settled unless I say otherwise.
```

## Rules

- Keep short snippets only when they are the bug or the fix. Otherwise point to the file and line.
- Never paste whole files. List them under Files and artifacts.
- Redact env values, tokens and connection strings; keep variable names.
- If the root cause was never confirmed, write `Cause: unconfirmed` plus the leading hypothesis.
