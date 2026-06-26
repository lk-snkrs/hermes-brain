# LK-TRENDS — Rendering failure and email-safe correction

Date: 2026-05-31

## Failure reported

Lucas reported that the first Gmail API newsletter arrived visually wrong: it rendered like plain/un-styled text on mobile instead of a premium visual HTML newsletter.

## Diagnosis

The first send was technically valid MIME (`multipart/alternative`, HTML part present), but relied on browser-style HTML/CSS:

- `<style>` block in `<head>`
- CSS variables
- grid/flex layout
- external Google Fonts
- browser-preview oriented structure

This passes MIME verification but is not a reliable Gmail/mobile newsletter format.

## Correction created

New email-safe HTML file:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/trends/newsletters/lk-trends-mapa-calor-email-safe-2026-05-31.html`

Validation:

- table-based layout: yes
- inline styles: yes
- no `<style>` tag: yes
- no external fonts: yes
- no CSS grid: yes
- no script: yes
- expected marker: yes
- secret-pattern hits: 0

## Guardrail

Do not resend without explicit current approval from Lucas for the corrected email-safe version.
