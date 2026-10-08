# Fidelity rules

A handoff brief is a lossy copy. These rules keep the loss harmless.

## Contents
- Hard rules
- Uncertainty labels
- Compression rules
- Self-check procedure
- Common failures

## Hard rules

1. **Never invent.** Every fact, decision, name, number and file in the brief must trace to a message in the chat.
2. **Verbatim where it matters.** Copy exactly: numbers with units, dates, names, code identifiers, file paths, flags, error messages, URLs, versions.
3. **Keep the user's wording for requirements.** Quote short phrases ("no jargon", "under 2 pages"). Do not paraphrase them into something broader or narrower.
4. **Decisions need confirmation.** Only list a decision if the user chose or accepted it. An assistant suggestion the user never answered is not a decision. Put it in Open items.
5. **Do not upgrade status.** "Tried" is not "works". "Suggested" is not "agreed". "Probably" stays unconfirmed.
6. **No new advice.** The brief records the chat. It does not add recommendations, fixes or next steps the chat did not reach, except the single obvious next step derived from the last unresolved point.
7. **Keep contradictions visible.** If the user changed their mind, record the latest choice and put the earlier one under Do not redo with the reason.

## Uncertainty labels

- Use the word `unconfirmed` for anything not verified in the chat: `Deadline: 14 March (unconfirmed)`.
- Use `unknown` when the chat never says (owner, version, cause).
- Never fill a gap with a plausible guess.

## Compression rules

- Drop: pleasantries, restated questions, explanations the user already understood, abandoned tangents with no lasting effect.
- Keep: constraints, rejected options and their reasons, exact values, anything the user said they care about.
- Merge duplicates. Prefer fragments over sentences. One fact per line.
- Rejected options are always kept, even in Mini, as one line, because losing them causes repeated work.

## Self-check procedure

Run silently before output.

1. List every decision, constraint and rejection you can find in the chat. Tick each against the brief.
2. List every line of the brief. Find its source message. Delete any line with no source.
3. Re-read numbers, names and identifiers against the chat character by character.
4. Count words in the brief (headings and Resume line included). Compare with the cap: Mini 150, Standard 400, Full 900.
5. Confirm no secret remains.
6. Confirm Open items starts with one concrete first step.

## Common failures

| Failure | Fix |
|---|---|
| Brief states a fix "worked" when the user never confirmed | Mark `unconfirmed` |
| Numbers rounded or units dropped | Copy exactly |
| Rejected idea missing | Add to Do not redo with the reason |
| Assistant's earlier proposal listed as decision | Remove or move to Open items |
| Brief written as a story | Rewrite as fragments under the fixed headings |
| Over the cap | Trim style, files, low-impact facts first |
