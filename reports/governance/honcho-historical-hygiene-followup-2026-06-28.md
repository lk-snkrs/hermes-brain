# Honcho historical hygiene follow-up — 2026-06-28

Generated at UTC: `2026-06-28T19:56:49.904494+00:00`

## Purpose

Continue after the Honcho best-practice runtime fix by auditing historical semantic noise and tightening observability without deleting provider history by heuristic.

## Current findings

| Metric | Result |
|---|---:|
| Utility status | attention |
| Utility score | 80 |
| Semantic score | 55 |
| Semantic contamination ratio | 0.75 |
| Ingestion filter active | True |
| Filter events observed | 491 |
| Sanitized cleanup candidates | 173 |
| Safe to delete now | False |
| Semantic auditor status | attention |
| Semantic auditor contamination ratio | 0.76 |
| Semantic auditor useful ratio | 0.33 |
| Raw content printed | false |
| Values printed | false |

## Actions taken

1. Ran the sanitized Honcho utility scorer.
2. Ran the sanitized cleanup candidate exporter.
3. Ran the semantic contamination auditor.
4. Ran the quality auditor and found it was too verbose for session/queue evidence.
5. Patched `honcho_memory_quality_auditor.py` so reports use session hashes and aggregate queue metrics instead of raw session IDs / giant queue dumps.
6. Copied patched Honcho hygiene scripts to `~/.hermes/scripts/` for cron execution.
7. Created daily local semantic contamination audit cron: `ba8ca37bfebd`.

## Interpretation

The ingestion filter is active and preventing many new operational payloads from entering Honcho, but historical semantic contamination remains high. The cleanup exporter found sanitized candidate hashes, but deletion is **not safe now** because message-delete granularity and provider rollback/snapshot have not been confirmed.

## Non-actions

- No Honcho deletion.
- No provider mutation.
- No database write.
- No Docker/VPS/Traefik change.
- No raw examples, PII, customer/order content, tokens or secrets printed.

## Recommended next decision

If Lucas wants to actually clean historical contamination, use the approval packet:

`areas/operacoes/approval-packets/honcho-provider-snapshot-and-historical-cleanup-20260628.md`

That packet is intentionally scoped to first create/verify rollback snapshot and delete granularity before any destructive cleanup.
