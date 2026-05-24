# LK GMC — Monitor pós A/B/C aprovado, 2026-05-14

Status: `post_abc_clean_for_target_scope`
Data: 2026-05-14
Modo: read-only de verificação. Nenhum Merchant/Shopify/Tiny/Notion/feed/campanha/WhatsApp/fornecedor write executado neste monitor.

## Contexto

Lucas aprovou corrigir o que deveria ser corrigido no LK OS. A execução A/B/C anterior criou cards Notion/Júlio, diagnosticou 12 produtos Shopify `DRAFT` que causavam 404 público e aplicou atributos não críticos no Merchant. Depois Lucas escolheu a opção de remover/suprimir os 12 IDs do Merchant em vez de publicar os DRAFTs no Shopify.

Este monitor existe para consolidar a pós-execução antes de avançar para novos gates do LK OS.

## Resultado verificado

- `fact_merchant_center`: 12/12 IDs Merchant DRAFT/404 seguem ausentes por `products.get` e `productstatuses.get` direto por ID exato.
- `fact_merchant_center`: 64/64 IDs da frente C não têm mais diagnóstico alvo de `color`, `ageGroup` ou `gender`.
- `fact_merchant_center`: 23.267 `productstatuses` lidos no baseline atual.
- `fact_merchant_center`: 524 linhas ainda têm algum issue geral no catálogo; isso é residual geral, não falha do escopo A/B/C.

Top diagnósticos gerais no baseline:

- `price_updated`: 1.089
- `strikethrough_price_updated`: 516
- `restricted_gtin`: 100
- `missing_item_attribute_for_product_type`: 44
- `availability_updated`: 30
- `landing_page_error`: 27
- `image_single_color`: 8
- `reserved_gtin`: 6
- `image_link_broken`: 6
- `landing_page_pending_crawl`: 5

## Artefatos

- Script: `scripts/lk_gmc_post_abc_monitor_20260514.py`
- Relatório público/sanitizado: `reports/lk-gmc-2026-05-14-post-abc-monitor.md`
- JSON técnico: `reports/lk-gmc-2026-05-14-post-abc-monitor.json`
- CSV resumo de issues: `reports/lk-gmc-2026-05-14-post-abc-monitor-issue-summary.csv`

## Não executado

- Nenhum novo patch/delete/write no Merchant.
- Nenhum publish/redirect/write no Shopify.
- Nenhum write no Tiny.
- Nenhum write adicional no Notion.
- Nenhum feed fetch/upload.
- Nenhum envio/campanha/WhatsApp/cliente/fornecedor/compra.

## Próximo gate seguro

1. Atualizar Mission Control/Status Surface para refletir que A/B/C está limpo no escopo alvo.
2. Gerar próximo preview residual por diagnóstico geral atual, com deduplicação por produto/atributo e amostras inline.
3. Se houver correção nova, pedir aprovação específica antes de qualquer Merchant/Shopify/Notion write.

## Regra operacional aprendida

Depois de um pacote GMC aprovado, sempre fazer monitor read-only de IDs exatos antes de propor nova escrita. Para deletes recentes, preferir `products.get` + `productstatuses.get` por ID exato após propagação, porque listas podem ter ghosts de consistência eventual.
