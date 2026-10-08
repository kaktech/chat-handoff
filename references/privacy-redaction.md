# Privacy redaction

Run on the draft brief before output. Replace each match with `[REDACTED]`. Keep the label so the new chat knows what was there (`DB password: [REDACTED]`).

## Contents
- What to redact
- What to keep
- Procedure
- Warning line

## What to redact

| Type | Look for |
|---|---|
| API keys and tokens | Prefixes like `sk-`, `pk_live_`, `ghp_`, `gho_`, `xox[abp]-`, `AKIA`, `AIza`, `ya29.`, `Bearer <long string>`; any 20+ character mixed-case/digit string next to words like key, token, secret |
| Passwords and passphrases | Anything after password, passwd, pwd, passphrase, PIN, "my login is" |
| Private keys and certs | `-----BEGIN ... PRIVATE KEY-----` blocks, SSH keys, JWTs (`eyJ...` three dot-separated parts) |
| Connection strings | `postgres://user:pass@host`, `mongodb+srv://`, `redis://:pass@`; redact the credential part, keep the scheme and host name only if not sensitive |
| Personal IDs | National ID, passport, SSN, tax ID, driver licence, BVN, NIN, bank account numbers, IBAN |
| Card data | 13 to 19 digit card numbers (spaces or dashes allowed), CVV, expiry paired with a card |
| Contact data | Private phone numbers, home addresses, personal emails, only when they are not needed for the task. If needed (e.g. the task is writing to that person), keep and mention it in the warning |
| Auth codes | One-time codes, recovery codes, magic-link URLs with tokens |

## What to keep

- Variable names (`STRIPE_SECRET_KEY`) without the value.
- Public identifiers: project names, usernames the user chose to share, public URLs without tokens.
- Fake or placeholder values clearly labelled as such (`sk-xxxx`, `example@example.com`).

## Procedure

1. Scan the whole conversation, not only the brief text. Pasted logs and configs hide secrets.
2. Redact in the brief. Keep structure intact.
3. Count items removed and note their types, never the values.
4. If a redacted value is required to continue, put `[REDACTED]: user must re-supply` in Open items.
5. When unsure whether a string is a secret, redact it.

## Warning line

Append once, after the paste line: `Heads up: I replaced N item(s) (types: API key, password) with [REDACTED]. Re-add them yourself in the new chat if needed.` Omit the line when nothing was removed. Do not repeat the removed values in the warning.
