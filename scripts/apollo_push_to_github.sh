#!/usr/bin/env bash
# apollo_push_to_github.sh — sube el resultado del backfill al repo Transcripts.
# Requiere: gh autenticado con acceso de escritura a mago-tera/Transcripts.
# Uso:  OUT_DIR=./apollo_export ./apollo_push_to_github.sh
set -euo pipefail

OUT_DIR="${OUT_DIR:-./apollo_export}"
REPO="${REPO:-mago-tera/Transcripts}"
DEST="${DEST:-apollo-backfill}"   # carpeta destino dentro del repo

[ -d "$OUT_DIR" ] || { echo "No existe $OUT_DIR — corré apollo_backfill.py primero."; exit 1; }

TMP="$(mktemp -d)"
echo "Clonando $REPO ..."
gh repo clone "$REPO" "$TMP/repo" -- --depth 1
mkdir -p "$TMP/repo/$DEST"

# Copiá transcripts (.md) y el índice. El crudo (raw/*.json) es opcional: descomentá si lo querés versionar.
cp -r "$OUT_DIR/transcripts" "$TMP/repo/$DEST/transcripts" 2>/dev/null || true
cp "$OUT_DIR/INDEX.md" "$TMP/repo/$DEST/INDEX.md" 2>/dev/null || true
# cp -r "$OUT_DIR/raw" "$TMP/repo/$DEST/raw"

cd "$TMP/repo"
git add "$DEST"
if git diff --cached --quiet; then
  echo "Nada nuevo para commitear."; exit 0
fi
git commit -m "Apollo backfill: import histórico de conversaciones"
git push
echo "Subido a $REPO/$DEST"
rm -rf "$TMP"
