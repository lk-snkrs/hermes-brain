# LK Growth Operating Guardrails


## Theme workflow — DEV first, then PRODUCTION merge

Recorded at: 2026-06-02T20:20:09.501428+00:00
Source: Lucas instruction via Telegram.

Rule:
- For LK theme/layout/collection changes, always apply changes in DEV first.
- Validate DEV preview/readback/HTML before any production action.
- After DEV validation, prepare merge/publish package for PRODUCTION with rollback and receipt.
- Production write still requires explicit scoped approval in the current turn, per LK external-write guardrail.
- Never patch PRODUCTION directly as the first step.
