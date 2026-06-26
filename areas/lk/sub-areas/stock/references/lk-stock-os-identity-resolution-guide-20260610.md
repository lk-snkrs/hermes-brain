# LK Stock OS — guia da resolução local de identidade

Última atualização: `20260610T172139Z`

Use a tabela `identity_resolution_decisions` para auditar por SKU/handle o motivo da decisão local.
A tabela `current_local_stock` da DB apontada foi atualizada apenas para os casos `CONSULTABLE_LOCAL_RESOLVED_BY_LIVE_EXACT_MATCH`.

## Status novo
- `CONSULTABLE_LOCAL_RESOLVED_BY_LIVE_EXACT_MATCH`: identidade SKU↔Tiny aceita no cache local porque houve match exato SKU+handle com estoque Tiny lido em lote read-only e sem duplicidade exata Shopify/Tiny.

## Consulta rápida
```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_os_query.py --status CONSULTABLE_LOCAL_RESOLVED_BY_LIVE_EXACT_MATCH --limit 20
```

## Guardrail

Regra corrigida por Lucas em 2026-06-10T17:32:11Z: confirmação operacional deve usar primeiro nossa database Stock OS apontada por `areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`.

Tiny / `LK | CONTROLE ESTOQUE` continua sendo a fonte primária que alimenta/valida a DB. Se a DB estiver stale, sem observação suficiente, sem SKU resolvido ou com bloqueio/duplicidade, consultar Tiny/fonte viva antes de responder disponibilidade.
