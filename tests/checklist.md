# Manual QA checklist

Tick every box on at least three real long chats of different types before releasing.

## Triggering
- [ ] Fires on: "new chat", "this chat is getting long", "hand off", "handoff", "summarize so I can continue", "wrap up this conversation", "continue in a fresh chat", "save my progress", "context is getting full"
- [ ] Does not fire on unrelated "summarize this article" requests
- [ ] "mini handoff" and "full handoff" change the tier

## Output shape
- [ ] Exactly one code block with the brief
- [ ] One paste instruction line
- [ ] One size-note line, labelled as an estimate
- [ ] No preamble, recap or sign-off
- [ ] Eight fixed headings (Mini may omit empty ones), Resume line last
- [ ] Brief within cap: Mini 150, Standard 400, Full 900 (count it)

## Content
- [ ] Goal states the end result, not the last question
- [ ] Every real decision present; no assistant suggestion listed as a decision
- [ ] Rejected options present with reasons
- [ ] Numbers, names, identifiers and errors copied exactly
- [ ] Uncertain items marked `unconfirmed`
- [ ] Next step is concrete and first in Open items
- [ ] Nothing in the brief that is not in the chat

## Privacy
- [ ] Keys, passwords, tokens, IDs and card numbers replaced with `[REDACTED]`
- [ ] Redaction warning appears only when something was removed
- [ ] Removed values never appear in the reply

## Edge cases
- [ ] Very short chat: no brief
- [ ] Unrelated topics: offers one brief per topic
- [ ] Attachments: listed, not pasted
- [ ] Brief language matches the chat language

## The real test
- [ ] Paste the brief into a fresh chat and ask the next question. The new chat continues without asking things already answered.
- [ ] Ask the new chat "what did we decide about X?" for three decisions. All three answers are correct.
- [ ] Ask the new chat about one rejected option. It does not suggest it again.

## Lean Mode
- [ ] Off by default
- [ ] "lean mode on" confirms once, then cuts preambles, restated questions and closing recaps
- [ ] Code and warnings stay complete
