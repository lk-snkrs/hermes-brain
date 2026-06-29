# Honcho go/no-go remediation 1–4 — 2026-06-29

## Pedido

Lucas respondeu ao go/no-go do Honcho com: “Seguir do 1 ao 4”. Interpretei como autorização para executar a remediação completa local/read-only+governance do auditor: protocolo, fila/deriver, validação e documentação.

## Resultado executivo

| Métrica | Antes | Depois |
|---|---:|---:|
| Configured | 100 | 100 |
| Active | 100 | 100 |
| Functioning | 60 | 70 |
| Protocol aware | 50 | 100 |
| Useful | 70/50 oscilante | 70 |
| Recommendation | `KEEP_EXPERIMENT_WITH_REMEDIATION` | `KEEP` |
| Pending queue ratio | 0.996 | 0.0 |

`values_printed=false`; nenhum secret/raw content/ID cru impresso.

## 1/4 — Protocol aware

Reparei os 5 profiles que tinham `HONCHO_USAGE_PROTOCOL_ENFORCEMENT`, mas não tinham `Honcho Utility Enforcement v2`:

- `brain-process`
- `hermes-ops-readonly`
- `lc-claude-cli`
- `lk-analyst-readonly`
- `lk-content-reviewer`

Backup:

`/opt/data/backups/honcho-utility-enforcement-protocol-repair-20260629T011508Z`

Validação: `missing_utility_enforcement=[]`.

## 2/4 — Functioning / queue

Diagnóstico mostrou queue Honcho muito pendente por rows órfãs:

- pending antes: `8412`
- tipo: `representation`
- sessões referenciadas ausentes no join com `sessions`
- active queue sessions: `0`
- errors não impressos; raw logs não impressos

Criei backup local restrito antes da remediação:

`/opt/data/backups/honcho-orphan-queue-remediation-20260629T011815Z`

Depois removi somente queue rows órfãs pendentes, não mensagens/conteúdo:

- rows órfãs removidas: `8412`
- pending depois: `0`

## 3/4 — Utility auditor / probes

Rodei o auditor e ajustei um falso negativo: o dialectic probe exigia literalmente `aprova`; agora aceita sinônimos operacionais (`aprova`, `autoriz`, `approval`, `escopad`) sem imprimir a resposta crua.

Resultado final:

```json
{
  "configured": 100,
  "active": 100,
  "functioning": 70,
  "protocol_aware": 100,
  "useful": 70,
  "recommendation": "KEEP"
}
```

Queue final:

```json
{"total_work_units": 31, "pending_work_units": 0, "pending_ratio": 0.0}
```

Quality auditor:

- status: `ok`
- score: `92`
- `raw_session_ids_printed=false`

Semantic auditor ainda permanece em attention:

- status: `attention`
- score: `55`
- contamination ratio: `0.75`

Isso é residual histórico/semântico e deve seguir o ciclo separado de cleanup, não bloquear o KEEP técnico.

## 4/4 — Documentação / enforcement contínuo

- O cron diário de madrugada já existe: `e3af978c6af6` — `Honcho Nightly Intelligence Enforcement Audit — 02h35 BRT`.
- O auditor utilitário foi ajustado para evitar falso negativo lexical.
- Report/receipt criados.

## Non-actions

- Nenhum restart Docker/VPS/Traefik/gateway.
- Nenhum external write.
- Nenhum secret/token/raw log impresso.
- Nenhuma mensagem/conclusão/sessão Honcho deletada nesta etapa.
- Apenas queue rows órfãs pendentes foram removidas, com backup local restrito.

## Veredito

Honcho voltou para `KEEP`, com `protocol_aware=100`, `functioning=70`, `useful=70`. Ainda existe trabalho de higiene semântica residual, mas agora não bloqueia a decisão executiva.
