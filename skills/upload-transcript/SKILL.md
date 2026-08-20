---
name: upload-transcript
description: Format a meeting/call transcript into a standardized sales markdown, upload it to the mago-tera/Transcripts GitHub repo, and update the matching lead in the Attio "deals" board. Use when the user pastes a transcript (or points to one in Apollo) and asks to save, upload, or push it to GitHub as markdown. Triggers on "subir/cargar/subí esta transcript", "transcript a github", "repo Transcripts", or dropping a raw meeting dialogue to be archived.
---

# Upload transcript to mago-tera/Transcripts + update Attio CRM

Turn a raw meeting/call transcript into a standardized markdown document, push it
to the GitHub repo **`mago-tera/Transcripts`** (default branch `main`), and then
update the matching deal in **Attio** (the "deals" object).

## When to use

- The user pastes a raw transcript (speaker-by-speaker dialogue) and asks to
  upload / save / push it to GitHub.
- The user asks to pull a transcript from Apollo and archive it (see Apollo note
  below — the connector may need auth).

## Required output structure

Every transcript markdown MUST have these four sections, in this order, written
in the transcript's language (usually Spanish). Synthesize from the dialogue —
do not paste the raw transcript. Be concrete and quote real phrases where they
add value.

1. **Caso de uso** — what the client/prospect is trying to do, the concrete
   Teramot setup shown (sources connected, gold tables, dashboards, MCP, bots,
   API), and any extensions they're considering.
2. **Roles y áreas afectadas** — which roles/departments touch or benefit from
   the solution (e.g. consultor, comercial/reposición, CFO/finanzas, gerencia,
   vendedores, análisis comercial).
3. **Testimonios y valor** — verbatim or near-verbatim quotes and the value
   drivers (retention, build-vs-buy, manual-work replaced, time saved). Include a
   **product-feedback / pain** note if the prospect flagged limitations.
4. **Señales de compra** — buying signals ranked by strength: commitments made,
   pricing/white-label interest, expansion plans, new opportunities, follow-ups
   requested, relationship warmth.

Start the file with a title `# Reunión Teramot — <contraparte>` and a short
header block: **Participantes**, **Fecha** (use the real date if known; if not
in the transcript, write `(no especificada en la transcripción)` — never
fabricate one), and **Cliente/contexto** when relevant.

## Steps

1. **Verify GitHub access** (the account should be `mago-tera`):
   ```
   gh auth status
   gh repo view mago-tera/Transcripts --json name,defaultBranchRef
   ```
2. **Write the markdown** to a scratch file using the four-section structure
   above.
3. **Pick a filename**: kebab-case, descriptive of the counterpart, e.g.
   `lucio-estanislao-sallent.md` or `2026-08-18-andromeda-teramot.md`. Prefix
   with the ISO date only when it's known.
4. **Upload** via the GitHub contents API (base64-encoded, no local clone):
   ```bash
   CONTENT=$(base64 -w0 <file.md>)
   gh api -X PUT repos/mago-tera/Transcripts/contents/<file.md> \
     -f message="Add transcript: <counterpart>" \
     -f content="$CONTENT" \
     --jq '.content.html_url'
   ```
   If the file already exists, the API returns 422 — fetch its `sha` with
   `gh api repos/mago-tera/Transcripts/contents/<file.md> --jq .sha` and pass
   `-f sha="$SHA"` to update it.
5. **Report** the resulting `html_url` to the user as a clickable link.
6. **Update the Attio CRM** (see below).

## Update the Attio "deals" board

After the markdown is uploaded, update the matching lead. The **`deals`** object
(not a list) holds the pipeline. Key attribute slugs: `name`, `stage` (status),
`owner` (required, actor-reference), `deal_type` (select: Teramot / Partner /
BSL), `source_channel` (select), `next_step` (text), `last_contact` /
`first_contact` (timestamp), `notes` (text), `associated_company`,
`associated_people`. Stage options in order: Lead, Qualified, Freemiun (sic),
Proposal Sent, POC, Won, cs actions, Activos/Soporte, Lost, churn.

Steps:
1. **Find the deal**: `search-records` on object `deals` with the company or
   person name from the transcript.
2. **Create it if missing** (`create-record` on `deals`). Required: `name`,
   `stage`, `owner`. Owner: Lucio's membership id is
   `5f4479fd-fc57-4361-b7cf-c06c71d86ca6` (his email is NOT a workspace member —
   don't pass `lucio@teramot.com` as owner, it errors). New deals from a first
   demo → `stage` "Qualified"; partner/reseller plays → `deal_type` "Partner",
   otherwise "Teramot".
3. **Add a note** (`create-note`, parent_object `deals`) with the transcript's
   four sections (condensed) and the GitHub link at the top. One note per
   transcript.
4. **Update `next_step`** with the concrete next step from the meeting.
5. **Update `last_contact`** with the meeting date — ONLY if the date is known
   (from the transcript, the Apollo conversation, or the user). Never fabricate a
   date; skip the field if unknown and say so.
6. **Update `stage` when the change is clear** from the signals (e.g. a "Lost"
   deal that is actively using the product again → move out of Lost). If the
   right stage is ambiguous, leave it and tell the user what you'd suggest. Always
   report any stage change you make and why.

Report the Attio `web_url`(s) of the deals you touched.

## Pulling from Apollo (optional source)

If the transcript should come from Apollo.io instead of pasted text:
- Tools: `apollo_conversations_search` (find the conversation id) →
  `apollo_conversations_get_transcript` (fetch it).
- The Apollo MCP connector requires authentication. If it errors with
  "requires authentication", tell the user to connect Apollo in claude.ai
  Connector settings (or `/mcp` in an interactive session) — do not ask for
  tokens or codes. Once connected, search, confirm the right conversation with
  the user (topic + start_time), fetch the transcript, then follow the steps
  above.

## Notes

- One transcript per file. Batch requests: write and upload each one, then give
  the user all the links.
- Never fabricate dates, names, quotes, or numbers not present in the source.
- Keep the synthesis substantially shorter than the raw transcript.
