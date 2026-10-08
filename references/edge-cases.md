# Edge cases

## Contents
- Very short chats
- Attached files
- Multiple unrelated topics
- Chats with images or pasted data
- Already-handed-off chats
- Unclear mode or tier
- Non-English chats
- Nothing decided yet

## Very short chats

Short means roughly under 10 messages, or a single question answered with no lasting decisions, constraints or state. Do not produce a brief. Reply in one or two lines: a handoff is not needed because the chat is short; the user can simply restate the request in a new chat. If the user insists, produce a Mini brief.

## Attached files

List each file under Files and artifacts: name, type, what it is for, and which part was used if stated. Never paste file contents. Add to Open items: `Re-attach <names> in the new chat.` If key numbers were pulled from a file and discussed in the chat, keep those numbers and name the file as the source.

## Multiple unrelated topics

If the chat holds two or more topics with no shared goal, do not merge them. Reply with one line listing the topics and ask which brief(s) the user wants, offering one brief per topic. If the user says "all", output separate code blocks, each with its own paste line, each within the tier cap. Shared facts that apply to every topic go in each brief that needs them.

## Chats with images or pasted data

Describe an image only by what the chat established about it (`screenshot of the checkout error, shows HTTP 500`). Do not describe pixels you cannot support. Keep small pasted data that later work depends on (under about 10 lines). For larger data, name it and say it must be pasted again.

## Already-handed-off chats

If the chat began with a handoff brief, treat that brief as the baseline. Merge it with what changed since. Move completed items to Done, add new decisions, keep prior Do not redo entries. Do not duplicate the old brief inside the new one.

## Unclear mode or tier

Pick the closest mode and the Standard tier. Do not ask. State the choice in the header line and offer the alternative in one line.

## Non-English chats

Write the whole brief, headings included, in the user's language. Keep the Resume line in the same language. Keep code, identifiers and quoted text in their original language.

## Nothing decided yet

If the chat is exploratory with no decisions, say so: `Decisions made: none yet`. Put the open question under Goal and the first step under Open items. Do not manufacture decisions.
