#!/usr/bin/env bash
# Build chat-handoff.zip for upload (claude.ai Settings > Skills, or the Skills API).
# The zip contains the skill folder as its root: chat-handoff/SKILL.md ...
# Only runtime files are shipped. Docs, tests and scripts stay in the repo.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME="chat-handoff"
DIST="$ROOT/dist"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

echo "Running validator..."
python3 "$ROOT/scripts/validate.py" "$ROOT"

mkdir -p "$STAGE/$NAME" "$DIST"
cp "$ROOT/SKILL.md" "$ROOT/LICENSE" "$STAGE/$NAME/"
cp -R "$ROOT/references" "$ROOT/examples" "$STAGE/$NAME/"
find "$STAGE" -name ".DS_Store" -delete

rm -f "$DIST/$NAME.zip"
(cd "$STAGE" && zip -r -X -q "$DIST/$NAME.zip" "$NAME")

echo "Checking zip structure..."
LISTING="$(unzip -Z1 "$DIST/$NAME.zip")"
echo "$LISTING"
echo "$LISTING" | grep -qx "$NAME/SKILL.md" || { echo "ERROR: $NAME/SKILL.md missing in zip" >&2; exit 1; }
if echo "$LISTING" | grep -v "^$NAME/" | grep -q .; then
  echo "ERROR: files outside $NAME/ in zip" >&2; exit 1
fi
echo
echo "Built $DIST/$NAME.zip ($(du -h "$DIST/$NAME.zip" | cut -f1))"
