# Apollo backfill — bajar todo el histórico de conversaciones

Exporta todas las conversaciones (reuniones + llamadas) de Apollo.io vía su API
REST y las guarda como archivos, listas para subir al repo `Transcripts`.

## 1. Requisitos

- **Master API key de Apollo.** Apollo.io › Settings › Integrations › API →
  *Create new key* con **"Set as master key"** activado (el export necesita el
  scope `conversations/export`; el master key lo cubre).
- Python 3.8+.
- `gh` autenticado con escritura en `mago-tera/Transcripts` (solo para el paso 2).

## 2. Bajar todo (no sube nada, deja archivos locales)

```bash
export APOLLO_API_KEY="tu_master_api_key"
export NOTIFY_EMAIL="marketing@teramot.com"
python3 apollo_backfill.py
```

Opcionales: `START_TIME`, `END_TIME` (ISO 8601, default = todo hasta hoy),
`OUT_DIR` (default `./apollo_export`).

El export de Apollo es **asíncrono** (llega también un mail cuando está listo);
el script poolea solo hasta 30 min. Genera:

```
apollo_export/
├── apollo-export-raw.json   # el crudo completo, por si acaso
├── INDEX.md                 # tabla: fecha | tema | transcript | id
├── raw/                     # un .json por conversación
└── transcripts/             # un .md por conversación que tenga transcript
```

Revisá `INDEX.md` y un par de `.md` para confirmar que el transcript vino bien.
Si la primera corrida imprime campos raros, pasámelos y ajusto el parseo
(`find_transcript` en el script).

## 3. Subir al repo

```bash
OUT_DIR=./apollo_export ./apollo_push_to_github.sh
```

Sube los `.md` + `INDEX.md` a `mago-tera/Transcripts/apollo-backfill/`. El crudo
`raw/*.json` queda fuera por defecto (descomentá en el script si lo querés
versionar).

## 4. Después

- Estos `.md` son el **archivo neutral** (respaldo). El resumen de 4 secciones
  (caso de uso / roles / valor / señales) y el update de Attio se hace con la
  skill `upload-transcript`, por conversación o en lote, cuando quieras.
- De acá en adelante, las calls nuevas entran por el grabador que elijas
  (Fireflies / tl;dv) con sync nativo a Attio — Apollo deja de ser el archivo.

## Notas

- Si el rango completo falla por tamaño, corré por tramos (ej. año por año)
  cambiando `START_TIME`/`END_TIME`.
- La API puede limitar por plan/scopes; si el export da 403, revisá que el key
  sea master.
