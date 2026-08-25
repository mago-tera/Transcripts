#!/usr/bin/env python3
"""
apollo_backfill.py — Baja TODO el histórico de conversaciones de Apollo.io.

Flujo (API REST de Apollo, master API key):
  1. POST /api/v1/conversations/export  {start_time, end_time, email} -> export_id
  2. GET  /api/v1/conversations/export/{id} (poll) -> redirect_url
  3. Descarga el JSON gzippeado y lo parte en un archivo por conversación.

No sube nada a ningún lado: deja todo en OUT_DIR para que lo revises.
Después, `apollo_push_to_github.sh` (o el paso 2 de este README) empuja al repo.

Uso:
  export APOLLO_API_KEY="tu_master_api_key"
  export NOTIFY_EMAIL="marketing@teramot.com"
  python3 apollo_backfill.py
  # opcionales:
  #   START_TIME=2015-01-01T00:00:00Z END_TIME=2026-08-25T00:00:00Z OUT_DIR=./apollo_export

Requisitos: Python 3.8+. Sin librerías externas (usa urllib).
"""
import gzip
import io
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

API_BASE = "https://api.apollo.io/api/v1"
API_KEY = os.environ.get("APOLLO_API_KEY", "").strip()
NOTIFY_EMAIL = os.environ.get("NOTIFY_EMAIL", "").strip()
START_TIME = os.environ.get("START_TIME", "2015-01-01T00:00:00Z")
END_TIME = os.environ.get("END_TIME", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
OUT_DIR = os.environ.get("OUT_DIR", "./apollo_export")
POLL_SECONDS = int(os.environ.get("POLL_SECONDS", "15"))
POLL_MAX_MIN = int(os.environ.get("POLL_MAX_MIN", "30"))

if not API_KEY or not NOTIFY_EMAIL:
    sys.exit("ERROR: seteá APOLLO_API_KEY y NOTIFY_EMAIL como variables de entorno.")


def _req(method, url, body=None, headers=None, raw=False):
    data = json.dumps(body).encode() if body is not None else None
    h = {"Content-Type": "application/json", "x-api-key": API_KEY, "Cache-Control": "no-cache"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            payload = r.read()
            return payload if raw else json.loads(payload.decode() or "{}")
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} en {method} {url}: {e.read().decode()[:500]}")


def slugify(text, maxlen=50):
    text = (text or "conversacion").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return (text[:maxlen] or "conversacion").strip("-")


def find_transcript(conv):
    """Busca el texto del transcript entre nombres de campo comunes."""
    for key in ("transcript", "transcript_text", "formatted_transcript", "text"):
        v = conv.get(key)
        if isinstance(v, str) and v.strip():
            return v
    # segmentos/oraciones con speaker + texto
    for key in ("segments", "sentences", "transcript_segments", "utterances"):
        seg = conv.get(key)
        if isinstance(seg, list) and seg:
            lines = []
            for s in seg:
                if not isinstance(s, dict):
                    continue
                spk = s.get("speaker") or s.get("speaker_name") or s.get("host") or ""
                txt = s.get("text") or s.get("sentence") or s.get("content") or ""
                lines.append(f"**{spk}**: {txt}".strip())
            if lines:
                return "\n\n".join(lines)
    return None


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    raw_dir = os.path.join(OUT_DIR, "raw")
    md_dir = os.path.join(OUT_DIR, "transcripts")
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(md_dir, exist_ok=True)

    print(f"1/3  Disparando export {START_TIME} -> {END_TIME} ...")
    resp = _req("POST", f"{API_BASE}/conversations/export",
                body={"start_time": START_TIME, "end_time": END_TIME, "email": NOTIFY_EMAIL})
    export_id = resp.get("export_id") or resp.get("id")
    if not export_id:
        sys.exit(f"No vino export_id. Respuesta: {json.dumps(resp)[:500]}")
    print(f"     export_id = {export_id}")

    print(f"2/3  Esperando a que el export esté listo (hasta {POLL_MAX_MIN} min) ...")
    redirect_url = None
    deadline = time.time() + POLL_MAX_MIN * 60
    while time.time() < deadline:
        r = _req("GET", f"{API_BASE}/conversations/export/{export_id}")
        redirect_url = r.get("redirect_url")
        if redirect_url:
            break
        print("     ... todavía procesando")
        time.sleep(POLL_SECONDS)
    if not redirect_url:
        sys.exit("Timeout esperando el export. Reintentá más tarde con el mismo export_id.")

    print("3/3  Descargando y descomprimiendo ...")
    blob = _req("GET", redirect_url, raw=True) if redirect_url.startswith("https://api.apollo.io") \
        else urllib.request.urlopen(redirect_url, timeout=300).read()
    try:
        text = gzip.decompress(blob).decode("utf-8", "replace")
    except OSError:
        text = blob.decode("utf-8", "replace")  # por si no viene gzippeado

    # el export puede ser un JSON array, un objeto {conversations:[...]}, o JSON-lines
    convs = []
    text_stripped = text.lstrip()
    try:
        parsed = json.loads(text)
        if isinstance(parsed, list):
            convs = parsed
        elif isinstance(parsed, dict):
            convs = parsed.get("conversations") or parsed.get("data") or [parsed]
    except json.JSONDecodeError:
        for line in text.splitlines():
            line = line.strip()
            if line:
                try:
                    convs.append(json.loads(line))
                except json.JSONDecodeError:
                    pass

    # guardá el crudo completo por las dudas
    with open(os.path.join(OUT_DIR, "apollo-export-raw.json"), "w", encoding="utf-8") as f:
        f.write(text)

    print(f"\nConversaciones encontradas: {len(convs)}")
    if convs:
        print("Campos de la primera conversación (para ajustar el parseo si hace falta):")
        print("  " + ", ".join(sorted(convs[0].keys())))

    index = []
    written = 0
    for c in convs:
        cid = str(c.get("id") or c.get("_id") or c.get("conversation_id") or written)
        topic = c.get("topic") or c.get("title") or c.get("name") or "conversacion"
        start = c.get("start_time") or c.get("started_at") or c.get("created_at") or ""
        date = (start or "")[:10] or "sin-fecha"
        base = f"{date}-{slugify(topic)}-{cid[:8]}"

        with open(os.path.join(raw_dir, base + ".json"), "w", encoding="utf-8") as f:
            json.dump(c, f, ensure_ascii=False, indent=2)

        tr = find_transcript(c)
        if tr:
            with open(os.path.join(md_dir, base + ".md"), "w", encoding="utf-8") as f:
                f.write(f"# {topic}\n\n**Fecha:** {start}  \n**Apollo ID:** {cid}\n\n---\n\n{tr}\n")
        index.append((date, topic, cid, bool(tr)))
        written += 1

    index.sort(reverse=True)
    with open(os.path.join(OUT_DIR, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write(f"# Apollo backfill — {len(index)} conversaciones\n\n")
        f.write(f"Export {START_TIME} → {END_TIME}. Generado {datetime.now().isoformat(timespec='seconds')}.\n\n")
        f.write("| Fecha | Tema | Transcript | Apollo ID |\n|---|---|---|---|\n")
        for date, topic, cid, has_tr in index:
            f.write(f"| {date} | {topic} | {'✅' if has_tr else '—'} | {cid} |\n")

    with_tr = sum(1 for *_ , h in index if h)
    print(f"\nListo. {written} archivos en {raw_dir}/ ; {with_tr} con transcript en {md_dir}/")
    print(f"Índice: {os.path.join(OUT_DIR, 'INDEX.md')}")
    print("Revisá y después subilos al repo (ver README, paso 2).")


if __name__ == "__main__":
    main()
