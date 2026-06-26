# Memory OS / Honcho — follow-up Fases 1, 2 e 3 — 2026-06-26

## Pedido

Lucas pediu executar os próximos 3 itens:

1. Patchar `hermes_memory_os_adoption_linter.py` para suportar ledger ativo em tail/archive/rollup sem falso `attention`.
2. Ativar tail-only permanente para `reports/memory-hygiene/adoption-events.jsonl` com backup/rollback e verificação.
3. Fazer higiene Honcho segura por filtro/ingestão/IDs disponíveis, sem apagar memória no escuro.

## Veredito

Executado.

| Gate | Resultado |
|---|---|
| Adoption linter | `ok`, `gap_count=0` |
| Ledger ativo | tail-only 500 linhas ativo |
| Ledger original | backup raw + gzip + checksum/rollback |
| Honcho quality | `ok`, score `92/100` |
| Honcho semantic auditor | `attention`, score `55/100`, contamination ratio `0.75` |
| Honcho ingestion/config hygiene | aplicado em 17/17 `honcho.json` |
| Brain health | FAIL=0/WARN=0 |
| Secret scan focado | high_confidence_hits=0 |
| External writes | 0 |
| Runtime restarts | 0 |

## 1) Patch do adoption linter

Arquivo alterado:

```text
/opt/data/scripts/hermes_memory_os_adoption_linter.py
```

Mudança:

- `adoption-latest.json` continua guardando o relatório completo atual.
- `adoption-events.jsonl` passa a receber apenas evento compacto/sanitizado via `compact_log_event(report)`.
- O evento compacto preserva tendências e contagens sem despejar samples completos em todo ciclo.

Motivo:

- O JSONL histórico tinha crescido para ~80MB porque cada execução anexava o relatório completo.
- Tail-only antes gerava falso `attention`; depois do patch e reconciliação de 2 receipts novos, o linter ficou verde com ledger reduzido.

## 2) Tail-only permanente ativado

Arquivo ativo:

```text
reports/memory-hygiene/adoption-events.jsonl
```

Estado atual:

| Campo | Valor |
|---|---:|
| Original antes do tail | 80,903,515 bytes |
| Linhas originais | 3,446 |
| Archive gzip | 1,781,963 bytes |
| Tail ativo | 500 linhas |
| Tail ativo bytes | 9,836,382 bytes |

Backup/rollback:

```text
/opt/data/backups/memory-os-adoption-tail-active/20260626T004237Z/
```

Rollup:

```text
reports/memory-hygiene/adoption-events-rollup-latest.json
```

Validação:

```text
adoption_status=ok
gap_count=0
```

Nota: durante a execução apareceram 2 receipts recentes sem evidência de hook; eles foram registrados via `hermes_memory_os_event_hook.py` antes da ativação definitiva do tail.

## 3) Higiene Honcho segura

Ação tomada:

- Não apaguei memória Honcho antiga.
- Não usei deleção por heurística sem ID/rollback.
- Apliquei higiene preventiva de ingestão/configuração nos `honcho.json` para reduzir contaminação futura.

Arquivos atualizados:

```text
/opt/data/honcho.json
/opt/data/profiles/*/honcho.json
```

Escopo:

| Item | Resultado |
|---|---:|
| Arquivos atualizados | 17 |
| Host blocks atualizados | 33 |
| Root `observationMode` | `unified` |
| Host `observationMode` | `unified` |
| Granular `user.observeOthers` | `false` |
| Granular `ai.observeMe` | `false` |

Backups:

```text
/opt/data/backups/honcho-observation-unified-hygiene/20260626T004324Z/
/opt/data/backups/honcho-host-observation-unified-hygiene/20260626T004720Z/
/opt/data/backups/honcho-granular-observation-unified-hygiene/20260626T004935Z/
```

Resolver efetivo verificado em amostra:

- default
- lk-growth
- lk-shopify
- mordomo
- spiti

Todos resolveram:

```text
observation_mode=unified
user_observe_others=false
ai_observe_me=false
```

Interpretação:

- Isso reduz nova contaminação cruzada.
- O auditor semântico continua `attention` porque mede conteúdo histórico já contaminado; não é esperado zerar imediatamente sem remoção/curadoria dirigida.
- Próximo nível de higiene exigiria IDs/escopo de memória a remover ou política de ingestão mais profunda no provider.

## Non-actions

- Não houve external writes.
- Não houve restart.
- Não houve Docker/VPS/Traefik/secrets.
- Não houve deleção de memória Honcho.
- Não houve impressão de secrets, PII ou trechos brutos de pedido/cliente.

## Próximos passos opcionais

1. Observar se o contamination ratio cai nos próximos ciclos novos após `observation` unificado.
2. Se não cair, criar PRD/approval packet para higiene por IDs ou filtro de ingestão no provider.
3. Se Lucas quiser, fazer wave específica para compactar as 4 boot memories acima de 80%, com backup/readback/secret scan.
