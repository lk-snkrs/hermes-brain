# LK Mission Control Snapshot — pós-GMC monitor 2026-05-14

Status: `mission_control_refresh_ready`
Modo: read-only/local documentation. Nenhum write externo, marketplace, WhatsApp, Notion, Shopify, Tiny, Merchant, campanha ou fornecedor foi acionado por este snapshot.

## Estado executivo

LK OS está `amarelo/verde`.

- Verde: GMC P2A principal terminou, rollback/progress preservados e readback por `products.get` bateu em 9.826/9.826 produtos, com 0 falhas.
- Verde: point repair de Bags executado e verificado: 44 patchados, 43 matches exatos, 1 variação apenas em `productTypes`.
- Amarelo: monitor `productstatuses` ainda mostra 494 produtos P2A com algum issue/destino reprovado; isto não recomenda reexecutar P2A em massa.
- Próximo gate: Droper read-only para 18 candidatos `stockout_exact_ready`, somente se Lucas aprovar inline.

## Monitor GMC pós-status

Fonte: `reports/lk-gmc-2026-05-14-p2a-post-status-monitor.md`.

- productstatuses lidos: 23.279
- IDs P2A esperados: 9.826
- IDs P2A encontrados: 9.826
- IDs ausentes: 0
- produtos P2A com issue/destino reprovado: 494
- issue instances P2A: 1.735
- `missing_item_attribute_for_product_type`: 136
  - color: 128
  - age group: 4
  - gender: 4
- destinos reprovados em IDs P2A: 39 instâncias
  - Shopping: 13
  - DisplayAds: 13
  - SurfacesAcrossGoogle: 13

Top residuals:

- price_updated: 987
- strikethrough_price_updated: 468
- missing_item_attribute_for_product_type: 136
- restricted_gtin: 68
- landing_page_error: 36
- availability_updated: 18

## Decision Inbox LK

Decisão atual:

> Aprovar ou não lookup Droper read-only para 18 rupturas fortes, sem compra, contato, WhatsApp, Notion write, StockX/GOAT ou alteração em sistemas.

Seguro agora:

- manter monitor/read-only;
- exibir pacote inline dos 18 candidatos;
- preparar comparação após lookup aprovado.

Bloqueado:

- consultar Droper sem aprovação;
- consultar StockX/GOAT sem novo escopo;
- compra/fornecedor/WhatsApp;
- Notion write;
- Shopify/Tiny/Merchant write;
- campanha/cliente.

## Pacote Droper

Fonte: `reports/lk-os-droper-readonly-approval-packet-18-2026-05-14.md`.

- candidatos: 18
- critério: Tiny zero no tamanho exato + demanda Shopify 120d + SKU/tamanho claros
- status: `approval_packet_ready_not_executed`

Texto de aprovação requerido:

`Aprovo consultar Droper read-only para os 18 candidatos stockout_exact_ready do LK OS, sem compra, sem contato, sem WhatsApp, sem Notion write, sem StockX/GOAT e sem alterações em Shopify/Tiny/Merchant.`

## Próxima ordem recomendada

1. Apresentar pacote inline de aprovação Droper para Lucas.
2. Se aprovado, executar apenas lookup Droper read-only nos 18 candidatos.
3. Gerar comparação e preview Júlio/Notion sem write.
4. Em paralelo futuro separado, criar pacotes para residuais GMC: preço/promotional price, color residual e landing page error.
