# Example: general (Standard)

Mode: general
Tier: Standard
Cap: 400

All names and numbers below are fictional.

## Source conversation (condensed)

- User: planning a 5-day trip to Lisbon for two people, 12 to 16 June, total budget EUR 1,800 excluding flights. Partner is vegetarian. They dislike organized tours. Wants a day-by-day plan.
- Assistant suggested staying in Alfama; user preferred Baixa because it is near the metro. Agreed on Baixa. Hotel shortlist: Hotel Duque (EUR 120/night), Casa Pombal (EUR 95/night). User picked Casa Pombal but has not booked; wants to check cancellation terms.
- Assistant proposed a day trip to Sintra and a boat tour on the Tagus. User rejected the boat tour ("tourist trap") and accepted Sintra on day 3, by train, not tour bus.
- Assistant proposed a Pena Palace ticket with a guide, user rejected: "no guides".
- Day 1 and Day 2 outlines were written and approved. Day 3 is Sintra. Days 4 and 5 not planned yet.
- User asked for plain bullet lists, no emojis, concise answers. Mentioned they speak a little Portuguese and like trying local restaurants.
- User pasted a flight confirmation PDF (flights.pdf) but only to confirm arrival 12 June 14:20 and departure 16 June 19:05.

## Brief

```
# Handoff: Lisbon trip plan | general | Standard
## Goal
Day-by-day plan for 2 people in Lisbon, 12 to 16 June. Budget EUR 1,800 total excluding flights.
## Decisions made
- Stay in Baixa (near metro), not Alfama.
- Preferred hotel: Casa Pombal, EUR 95/night.
- Day 3: Sintra by train.
- Day 1 and Day 2 outlines approved.
## Key facts
- Arrival 12 June 14:20, departure 16 June 19:05 (from flights.pdf).
- Partner is vegetarian; restaurants must have vegetarian mains.
- User dislikes organized tours; "no guides".
- User speaks a little Portuguese and likes trying local restaurants.
## Current state
- Done: hotel choice, Day 1, Day 2, Day 3 outline.
- Not booked: hotel (user wants to check cancellation terms first).
- Not planned: Day 4 and Day 5.
## Open items / next step
1. Plan Day 4 and Day 5 within the remaining budget.
2. Then give a rough budget table (hotel, food, transport, tickets) against EUR 1,800.
3. Cancellation terms for Casa Pombal: unconfirmed, user to check.
## Style and preferences
- Plain bullet lists, no emojis, concise answers.
## Files and artifacts
- flights.pdf (attached earlier): flight confirmation. Re-attach if needed.
## Do not redo
- Alfama as base: user prefers Baixa for metro access.
- Boat tour on the Tagus: user called it a tourist trap.
- Guided tours or guides (incl. Pena Palace guide): user does not want them.
- Hotel Duque (EUR 120/night): more expensive, not chosen.
Resume: Continue from Open items. Do not re-ask answered questions. Treat Decisions made as settled unless I say otherwise.
```

Paste this as the first message of a new chat.
Brief is about 270 words; this chat is about 1,500 words, so roughly 5 times shorter (estimate).

## Fidelity check against references/fidelity-rules.md

- Every line traces to a message above. Hotel prices, dates and times are verbatim.
- Cancellation terms marked unconfirmed. No invented Day 4 or 5 content.
- Rejected items kept with reasons.
