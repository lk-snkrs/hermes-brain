# Decision packet — Gate B2 saneamento SKU/Tiny/Shopify

- Gerado em: 20260610T104842Z
- Escopo: local/read-only
- Runtime/webhook/cron ativado: 0
- Tiny write: 0
- Shopify write: 0
- Writes externos: 0
- Secrets impressos: 0

## Evidência local consolidada
- Shards SQLite consolidados: 90
- Prefixos executados: 1647
- Linhas totais crosswalk: 12645
- Disponibilidade local liberada para decisão interna: 11740
- Linhas bloqueadas para saneamento: 905

## Bloqueios por tipo
- `shopify_variant_tiny_missing`: 459
- `shopify_duplicate_sku_blocked`: 293
- `tiny_duplicate_exact_code_blocked`: 96
- `matched_exact_sku_stock_missing_deposit`: 57

## Handles com mais bloqueios abertos
- `slipper-alo-yoga-recovery-saddle-ivory-bege`: 12
- `tenis-new-balance-204l-grey-matter-shipyard-cinza`: 12
- `tenis-asics-gel-1130-white-black-silver-prata`: 12
- `tenis-asics-gel-1130-black-pure-silver-prata`: 12
- `tenis-jordan-4-retro-toro-bravo-2026-vermelho`: 12
- `tenis-air-jordan-1-low-og-year-of-snake-2025-cinza`: 11
- `tenis-air-jordan-1-low-lucky-green-verde`: 7
- `tenis-new-balance-1906l-silver-metallic-black-prata`: 7
- `tenis-new-balance-9060-grey-day-kids-td-cinza`: 7
- `yeezy-foam-runner-sand-937693356`: 5
- `air-jordan-1-low-true-blue`: 5
- `new-balance-530-white-natural-indigo-1`: 5

## Shards com mais bloqueios
- Shard 1: 39 bloqueios / 178 linhas — {'matched_exact_sku_stock_missing_deposit': 6, 'matched_exact_sku_stock_resolved': 139, 'shopify_duplicate_sku_blocked': 5, 'shopify_variant_tiny_missing': 27, 'tiny_duplicate_exact_code_blocked': 1}
- Shard 88: 38 bloqueios / 197 linhas — {'matched_exact_sku_stock_resolved': 159, 'shopify_duplicate_sku_blocked': 22, 'shopify_variant_tiny_missing': 16}
- Shard 2: 36 bloqueios / 139 linhas — {'matched_exact_sku_stock_missing_deposit': 5, 'matched_exact_sku_stock_resolved': 103, 'shopify_duplicate_sku_blocked': 3, 'shopify_variant_tiny_missing': 25, 'tiny_duplicate_exact_code_blocked': 3}
- Shard 4: 36 bloqueios / 152 linhas — {'matched_exact_sku_stock_missing_deposit': 3, 'matched_exact_sku_stock_resolved': 116, 'shopify_duplicate_sku_blocked': 5, 'shopify_variant_tiny_missing': 28}
- Shard 13: 34 bloqueios / 134 linhas — {'matched_exact_sku_stock_missing_deposit': 4, 'matched_exact_sku_stock_resolved': 100, 'shopify_duplicate_sku_blocked': 9, 'shopify_variant_tiny_missing': 18, 'tiny_duplicate_exact_code_blocked': 3}
- Shard 5: 32 bloqueios / 142 linhas — {'matched_exact_sku_stock_missing_deposit': 5, 'matched_exact_sku_stock_resolved': 110, 'shopify_duplicate_sku_blocked': 2, 'shopify_variant_tiny_missing': 25}
- Shard 14: 32 bloqueios / 132 linhas — {'matched_exact_sku_stock_missing_deposit': 3, 'matched_exact_sku_stock_resolved': 100, 'shopify_duplicate_sku_blocked': 16, 'shopify_variant_tiny_missing': 11, 'tiny_duplicate_exact_code_blocked': 2}
- Shard 15: 30 bloqueios / 138 linhas — {'matched_exact_sku_stock_missing_deposit': 3, 'matched_exact_sku_stock_resolved': 108, 'shopify_duplicate_sku_blocked': 8, 'shopify_variant_tiny_missing': 18, 'tiny_duplicate_exact_code_blocked': 1}
- Shard 17: 29 bloqueios / 104 linhas — {'matched_exact_sku_stock_missing_deposit': 2, 'matched_exact_sku_stock_resolved': 75, 'shopify_duplicate_sku_blocked': 8, 'shopify_variant_tiny_missing': 15, 'tiny_duplicate_exact_code_blocked': 4}
- Shard 16: 28 bloqueios / 135 linhas — {'matched_exact_sku_stock_missing_deposit': 3, 'matched_exact_sku_stock_resolved': 107, 'shopify_duplicate_sku_blocked': 11, 'shopify_variant_tiny_missing': 13, 'tiny_duplicate_exact_code_blocked': 1}

## Interpretação operacional
- `shopify_variant_tiny_missing`: Shopify tem variant/SKU, mas Tiny não resolveu código exato; bloquear pronta entrega até corrigir/mapeá-lo.
- `shopify_duplicate_sku_blocked`: há mais de uma variant Shopify ativa com o mesmo SKU exato; bloquear disponibilidade até saneamento de grade/SKU.
- `tiny_duplicate_exact_code_blocked`: Tiny retornou duplicidade de código exato; bloquear disponibilidade mesmo com saldo até saneamento no Tiny.
- `matched_exact_sku_stock_missing_deposit`: Tiny resolveu o código, mas não confirmou depósito oficial `LK | CONTROLE ESTOQUE`; bloquear até validação/fonte oficial.

## Recomendação de próximo gate
Aprovar um mutirão/read-only de saneamento com duas saídas locais:
1. Fila P0 de saneamento por impacto: priorizar handles com maior número de bloqueios e itens com demanda/venda recente antes de qualquer compra/transferência.
2. Prévia de correções: propor correção SKU/grade/Tiny/Shopify em arquivo local, sem executar write em Tiny/Shopify.

## Fora de escopo mesmo se este packet for aceito
- Não ativar webhook, cron, bot ou Telegram automático.
- Não escrever em Tiny ou Shopify.
- Não prometer disponibilidade/pronta entrega a cliente.
- Não comprar, transferir, reservar, contatar fornecedor ou campanha.

## Kill criteria
- Qualquer tentativa de write externo.
- Fonte Tiny/Shopify instável ou divergente sem retry/readback.
- Entrada de fixture/probe em fila operacional.
- Dúvida entre tamanho/grade real e SKU normalizado.

## Rollback
- Como o escopo é local/read-only, rollback é ignorar/remover os relatórios/CSVs/DBs gerados no Gate B2 e preservar receipts como trilha auditável.
- Se futura correção local for aprovada, criar backup da SQLite/cache antes de alterar qualquer dado local.

## Frase exata para aprovar o próximo passo local
> Aprovo preparar a fila P0/P1 de saneamento SKU/Tiny/Shopify do Gate B2 do `lk-stock`, usando apenas dados locais/read-only e consultas read-only necessárias, sem write em Tiny/Shopify, sem cron/webhook/runtime, sem contato externo e com receipt.

## Artefatos
- JSON consolidado: `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-consolidado-20260610T104842Z.json`
- CSV de issues: `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-issues-20260610T104842Z.csv`
- Este packet: `areas/lk/sub-areas/stock/approval-packets/gate-b2-sku-saneamento-decision-packet-20260610T104842Z.md`
