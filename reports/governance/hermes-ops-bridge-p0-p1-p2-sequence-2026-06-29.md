# Hermes Ops Bridge — P0/P1/P2 sequence

Data: 2026-06-29

## Resultado

Lucas aprovou executar P0, P1 e P2 em sequência. Implementação concluída mantendo o contrato: local/read-only, sem restart, sem cron novo, sem dashboard/API, sem Docker/VPS/Traefik mutation e sem writes externos.

Script principal:

`/opt/data/scripts/hermes_ops_bridge_readonly.py`

Testes:

`/opt/data/scripts/tests/test_hermes_ops_bridge_readonly.py`

## P0 — feito

| Item | Implementação |
|---|---|
| `qa` | Gate local por classe: `all`, `brain`, `runtime`, `script`, `cron`. |
| `maintenance-score` | Score local 0–100 com grade `green/watch/action_required`. |
| `daily-delta` | Compara estado atual contra `skill-surface-diet-recurring/latest.json`. |

## P1 — feito

| Item | Implementação |
|---|---|
| `maintenance-ledger` | Lista receipts recentes com title/path/mtime para enxergar cadeia de manutenção. |
| `telegram-noise` | Audita jobs Telegram/origin potencialmente ruidosos: daily/report/digest/weekly/monthly. |

## P2 — feito read-only

| Item | Implementação |
|---|---|
| `host-audit` | Snapshot local read-only de host/Docker/compose/Traefik candidates. |
| Docker | Apenas `docker ps` e `docker compose ls`; sem exec/run/restart/stop. |
| Host | `uname`, `df`, `free`; `ss` tentou rodar, mas binário ausente. |
| Traefik/compose | Lista candidatos locais de compose/traefik paths; sem ler secrets nem alterar arquivos. |

## Subcomandos finais do Ops Bridge

- `status`
- `profile-map`
- `cron-inventory`
- `health`
- `logs`
- `smoke`
- `qa`
- `maintenance-score`
- `daily-delta`
- `maintenance-ledger`
- `telegram-noise`
- `host-audit`
- `packet`
- `receipt`

## Piloto final medido

| Métrica | Resultado |
|---|---:|
| Profiles configurados | `16` |
| Gateways rodando | `13` |
| Profiles fora de config v30 | `0` |
| API/webhook enabled | `default` PID 1 apenas |
| Cron jobs | `108` |
| Cron enabled | `90` |
| Cron paused | `18` |
| Cron enabled non-ok | `0` |
| QA | `pass`, failures `0` |
| Maintenance score | `82/100`, grade `watch` |
| Daily delta | `0` mudanças |
| Maintenance ledger | `30` receipts recentes |
| Telegram noise findings | `8` candidatos |
| Host audit | `6` checks, `46` compose/traefik candidates |

## Findings acionáveis

### Maintenance score: `82/100 — watch`

Deduções:

- `skill diet warnings: -8`
- `telegram noise findings: -10`

Interpretação: sistema está funcional e sem falha crítica nos gates locais, mas ainda há ruído/avisos que precisam curadoria antes de chamar de “green”.

### Telegram noise candidates: `8`

Candidatos detectados:

- Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram
- Skill Surface Diet daily drift audit read-only
- Skill Surface Diet weekly supervised review prompt
- Skill Surface Diet monthly heavy-skill curation audit
- LK Stock Gate B daily freshness reconcile read-only
- LK Supabase public exposure security gate daily
- LC Mordomo OS WhatsApp daily digest 17h
- LC Mordomo OS daily 06h self-review

Observação: finding não significa “pausar”. Significa revisar se a entrega no Telegram está realmente acionável ou se deve ficar silent/local. O relatório Hermes diário é explicitamente obrigatório em Telegram por correção anterior do Lucas, então deve ser melhorado, não suprimido.

## Guardrails preservados

- `values_printed=false`.
- Nenhum secret value preservado.
- Nenhum comando mutável registrado no Ops Bridge.
- Nenhum cron criado/alterado.
- Nenhum gateway/profile reiniciado.
- Nenhum Docker/VPS/Traefik alterado.
- Nenhum write externo.
- P2 host/docker/traefik ficou read-only.

## Próxima recomendação

Não criar cron do Ops Bridge ainda. Usar manualmente nas próximas manutenções e, se o score/ruído estabilizar, propor depois um cron silent-OK separado para `maintenance-score`.
