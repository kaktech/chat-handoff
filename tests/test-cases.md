# Test cases

Run each scenario in a real chat with the skill enabled. A scenario passes only if every "Must" holds and no "Must not" occurs. All data is fictional.

## Contents
1. Plain trigger, default tier
2. Mini request
3. Full request
4. Coding chat with secrets
5. Writing chat with voice feedback
6. Research with mixed verification
7. Business plan with owners and numbers
8. Study session
9. Very short chat
10. Multiple unrelated topics
11. Attached files
12. Non-English chat
13. Mode override
14. Lean Mode
15. Chat that already started from a handoff

## 1. Plain trigger, default tier

Chat: 30+ messages planning a product launch. User then says "this chat is getting long".
Must: one code block; Standard tier; 8 fixed headings; Resume line last; one paste line; one size-note line; at most 400 words in the brief.
Must not: preamble, recap, extra advice.

## 2. Mini request

Chat: any substantial chat. User: "mini handoff".
Must: brief at most 150 words; Goal, Decisions, Current state, Open items, Do not redo present; rejected options kept.
Must not: more than one line per section.

## 3. Full request

Chat: long debugging chat, user says "full handoff".
Must: at most 900 words; exact error text, commands and file paths preserved; detail in Key facts and Do not redo.
Must not: pasted full files.

## 4. Coding chat with secrets

Chat: user pastes `.env` lines: `STRIPE_SECRET_KEY=sk_live_51Hxxxxxxxxxxxxxxxx`, `DB_PASSWORD=hunter2hunter2`, and a card number `4242 4242 4242 4242` while describing a bug.
Must: all three replaced with `[REDACTED]`; variable names kept; warning line states 3 items and types; no value repeated in the warning.
Must not: any of the three strings anywhere in the reply.

## 5. Writing chat with voice feedback

Chat: user rejects "too salesy" intro, approves a second one, sets 600 words, US English, audience: first-time founders.
Must: audience, length, spelling variant, voice feedback in the user's words; rejected intro style under Do not redo; draft status stated.
Must not: full draft pasted; invented sections.

## 6. Research with mixed verification

Chat: user and assistant discuss three claims; one was checked against a named source, one came from memory, two sources conflict.
Must: claims split into Verified (with source), Unverified or unconfirmed, Conflicting; sources copied exactly.
Must not: any unverified claim shown as verified.

## 7. Business plan with owners and numbers

Chat: budget of 45,000 NGN per unit, launch 3 March, owners Ada (pricing) and Tunde (supplier), no date for supplier contract.
Must: numbers with currency intact; stakeholders listed; supplier contract date marked `unconfirmed`; next step lists owner and due.
Must not: rounded numbers; guessed dates.

## 8. Study session

Chat: learner studies organic chemistry, gets SN1 vs SN2 wrong twice, understands nomenclature, exam 20 May.
Must: Understood vs Shaky split; the exact misconception recorded; exam date; preferred teaching style.
Must not: SN1/SN2 marked as understood.

## 9. Very short chat

Chat: 3 messages, one factual question answered.
Must: replies in one or two lines that a handoff is not needed; no brief.
Must not: a full brief (unless the user insists, then Mini).

## 10. Multiple unrelated topics

Chat: half on a CV rewrite, half on fixing a Python script, no shared goal.
Must: lists the two topics and offers one brief per topic; if user says "both", two separate code blocks with separate paste lines.
Must not: one merged brief.

## 11. Attached files

Chat: user attached `budget.xlsx` and `logo.png`; discussion used totals from the sheet.
Must: both files listed with purpose; key totals kept with file named as source; Open items says to re-attach.
Must not: file contents pasted; imagined contents of the logo.

## 12. Non-English chat

Chat entirely in Spanish about planning a wedding.
Must: whole brief including headings and Resume line in Spanish; names and numbers unchanged.
Must not: English headings or mixed languages.

## 13. Mode override

Chat: a mixed design-and-code discussion auto-detected as coding. User says "make it a business handoff".
Must: uses business template; header shows `business`; stakeholders, deadlines, numbers emphasized.
Must not: ignore the override.

## 14. Lean Mode

User: "lean mode on". Then asks two ordinary questions.
Must: replies `Lean Mode on.`; later replies have no greeting, no restated question, no closing offer; code complete. On handoff, brief includes `Lean Mode: on` under Style and preferences.
Must not: shortened code or removed warnings.

## 15. Chat that already started from a handoff

Chat: first message is an earlier brief; 20 messages follow with new decisions; a task finishes; one earlier decision is reversed.
Must: new brief merges both; completed task under Done; reversed decision updated, old choice under Do not redo with reason; previous Do not redo kept; old brief not duplicated.
Must not: stale decisions that were reversed.

## Fidelity probes (run on any scenario)

- Add a number to the brief that was not in the chat: self-check must catch it.
- Ask the assistant to "just fill in the missing owner": it must write `unconfirmed`, not invent.
