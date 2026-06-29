# Honcho all-agents post-repair audit — 2026-06-28

- Generated at UTC: `2026-06-28T18:32:37.983125+00:00`
- Profiles checked: `17`
- Profiles passing configured+active+protocol-aware: `17/17`
- Gateway count issues: `[]`
- Missing gates: `[]`
- Secrets printed: `false`
- Writes externos: `0`

## Matrix

| profile | configured | active | protocol aware | live gateway | recent log Honcho |
|---|---:|---:|---:|---:|---:|
| default | True | True | True | 1 | False |
| brain-process | True | True | True | None | False |
| hermes-ops-readonly | True | True | True | None | False |
| lc-claude-cli | True | True | True | 1 | False |
| lk-analyst-readonly | True | True | True | None | False |
| lk-collection-optimizer | True | True | True | 1 | False |
| lk-content | True | True | True | 1 | False |
| lk-content-reviewer | True | True | True | None | False |
| lk-finance | True | True | True | 1 | False |
| lk-growth | True | True | True | 1 | False |
| lk-ops | True | True | True | 1 | False |
| lk-shopify | True | True | True | 1 | False |
| lk-stock | True | True | True | 1 | True |
| lk-trends | True | True | True | 1 | False |
| mordomo | True | True | True | 1 | False |
| spiti | True | True | True | 1 | False |
| spiti-atendimento | True | True | True | 1 | False |

## Interpretation

Status: **OK for configured, active, functioning, and protocol-aware** across audited profiles.

`useful` remains a behavioral criterion: next real agent interactions should show fewer repeated questions, correct use of Honcho for history-dependent decisions, and explicit noise handling when Honcho returns irrelevant context.
