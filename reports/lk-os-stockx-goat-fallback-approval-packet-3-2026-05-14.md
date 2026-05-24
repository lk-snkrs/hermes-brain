# LK OS — StockX/GOAT fallback approval packet — 3 sem match Droper

Gerado em: `2026-05-14T23:26:27.275943+00:00`

Status: `stockx_goat_approval_packet_ready_not_executed`

## Veredito

Depois do payload Notion/Júlio dos 15 matches Droper, os 3 itens sem tamanho exato forte no Droper ficam elegíveis para um fallback StockX/GOAT **somente se aprovado**.

## Aprovação requerida

`Aprovo consultar StockX/GOAT read-only para os 3 candidatos LK Compras sem match Droper forte, com normalização de tamanho, sem compra, sem reserva, sem contato, sem WhatsApp, sem Notion write e sem alterações em Shopify/Tiny/Merchant.`

## Escopo autorizado se aprovado

- Lookup read-only em StockX/GOAT para os 3 itens abaixo.
- Normalizar tamanho US Men/Women para LK/BR/EU antes de comparar.
- Capturar preço/disponibilidade/link/taxas quando visível.
- Preparar comparação e preview Júlio/Notion.

## Não autorizado

- Compra/reserva/pagamento.
- Contato fornecedor/vendedor.
- WhatsApp.
- Notion write.
- Shopify/Tiny/Merchant write.
- Campanha/cliente.

## Candidatos

### 1. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 36
- SKU: `HV8547-700-3`
- Query base: `Nike Moon Shoe SP Jacquemus Alabaster`
- Demanda 120d: 3 un · R$ 15.999,97
- Status Droper: `not_found_exact_size`
- Relacionados Droper vistos: Jacquemus x Nike Moon Shoe SP Alabaster Feminino R$ 6.500,00 tamanhos 43,42,40.5,40,39,38,37 https://droper.app/produto/1045237
- Próximo se aprovado: StockX/GOAT read-only com normalização de tamanho para `36`.

### 2. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 37.5
- SKU: `HV8547-700-10`
- Query base: `Nike Moon Shoe SP Jacquemus Alabaster`
- Demanda 120d: 1 un · R$ 4.999,99
- Status Droper: `not_found_exact_size`
- Relacionados Droper vistos: Jacquemus x Nike Moon Shoe SP Alabaster Feminino R$ 6.500,00 tamanhos 43,42,40.5,40,39,38,37 https://droper.app/produto/1045237
- Próximo se aprovado: StockX/GOAT read-only com normalização de tamanho para `37.5`.

### 3. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 42.5
- SKU: `1183C015101`
- Query base: `Mexico 66 SD Cream Birch`
- Demanda 120d: 1 un · R$ 2.499,99
- Status Droper: `not_found_exact_size`
- Relacionados Droper vistos: sem relacionados Droper úteis
- Próximo se aprovado: StockX/GOAT read-only com normalização de tamanho para `42.5`.

## Próximo gate após lookup aprovado

- Se StockX/GOAT encontrar opção viável: gerar comparação e preview Júlio/Notion sem write.
- Se não encontrar: manter em backlog/monitor, sem ação externa.