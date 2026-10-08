# Contributing

Thanks for helping. Keep the skill small: every line in `SKILL.md` costs tokens in every chat that triggers it.

## Ground rules

- Follow the official Agent Skills format: `name` lowercase/hyphens matching the folder, `description` at most 1,024 characters, third person, no XML tags.
- `SKILL.md` stays under 150 lines. Put detail in `references/` and link it directly from `SKILL.md` (one level deep).
- Plain imperative language. No filler.
- Never weaken fidelity or privacy rules to save words.
- Examples use fictional data only. No real keys, even expired ones.

## Workflow

1. Fork and branch.
2. Make your change.
3. Run `python3 scripts/validate.py` and fix every error.
4. Run `bash scripts/package.sh` and confirm the zip lists `chat-handoff/SKILL.md` first-level.
5. Run the relevant scenarios in `tests/test-cases.md` on a real chat and tick `tests/checklist.md`.
6. Add an entry to `CHANGELOG.md`.
7. Open a pull request describing what changed and which scenarios you ran.

## Adding a mode template

1. Create `references/templates/<mode>.md` with the eight section headings in a skeleton block and the Resume line.
2. Add the mode to `SKILL.md` step 3 and to `TEMPLATES` in `scripts/validate.py`.
3. Add a test scenario.

## Adding an example

Include `Mode:`, `Tier:`, `Cap:`, a condensed fake source conversation, and a `## Brief` code block. The validator checks the word cap and sections.

## Reporting problems

Include the tier, the mode, the chat length, what the brief missed or invented, and which test scenario it resembles. Do not paste private conversations.
