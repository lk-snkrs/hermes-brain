# Handoff — LK Trends x Collection Optimizer: Global top models → site candidates

Data: 2026-06-14T15:22:00Z
Owner atual: [LK] Otimização de Coleções / LK Trends read-only
Status: pesquisa read-only concluída; nenhum write Shopify/Tiny/fornecedor executado.
Pedido Lucas: pesquisar com LK Trends os modelos bombando fora do Brasil e adicionar no site os 6 mais vendidos nos últimos 6 meses.

## Guardrail

- LK Trends identifica oportunidade; não compra, não reserva, não negocia e não publica.
- Shopify/product/collection writes exigem aprovação explícita atual + pacote com preview/readback/rollback.
- Qualquer disponibilidade/grade/estoque deve ir para `lk-stock`; este agente não consulta estoque.
- “Últimos 6 meses”: KicksDev probe atual retornou `sales/daily` com janela confiável de 90d + `orders_all_returned` por produto. Para 180d exato, precisa extensão de coleta se a API retornar histórico suficiente por data bruta. Ranking abaixo usa **liquidez 90d como proxy principal**, Google US/BR 12m como validação de demanda e presença pública LK.

## Fontes executadas

- KicksDev/KicksDB read-only via Doppler `lc-keys/prd`, secret name apenas: `KICKS_API_KEY`, values_printed=false.
- Probe 1: `areas/lk/sub-areas/trends/reports/kicksdev-probes/lk-trends-kicksdev-probe-20260614T151613Z.json|md`
- Probe 2: `areas/lk/sub-areas/trends/reports/kicksdev-probes/lk-trends-kicksdev-probe-20260614T151830Z.json|md`
- DataForSEO Google Keyword Overview US/en e Brazil/pt para demanda externa/local.
- Busca pública LK via `/search/suggest.json` para presença de produtos/coleções.

## Ranking inicial — top model families para LK

### 1) Nike x Jacquemus Moon Shoe SP — manter/expandir, não “novo add”

Evidência internacional:
- KicksDev StockX top 3 colorways somam ~41.480 vendas 90d:
  - Aluminum Pink: 17.348 vendas 90d.
  - Soft Pearl: 12.432 vendas 90d.
  - Fauna Brown: 11.700 vendas 90d.
- Forte liquidez internacional, mas Google BR para termo exato é pequeno; é mais fashion/collab premium que busca massiva.

Presença LK pública:
- Produtos encontrados: Off White, Medium Brown, Alabaster.
- Coleção encontrada: `/collections/nike-x-jacquemus-moon-shoe-sp`.

Ação recomendada:
- Não criar do zero; validar gap de colorway/grade com `lk-stock`/compras.
- Se houver colorways fortes ausentes: pacote de sourcing/Shopify específico.

### 2) Nike P-6000 — GAP principal para adicionar

Evidência internacional:
- KicksDev StockX:
  - Metallic Silver: 11.742 vendas 90d; 30.077 all returned.
  - Black: 3.458 vendas 90d; 7.621 all returned.
  - Triple White: 2.374 vendas 90d; 4.920 all returned.
- GOAT Metallic Silver: 1.110 vendas 90d.
- Google US: 110.000 buscas/mês; transacional.
- Google BR: 8.100 buscas/mês; transacional.

Presença LK pública:
- Busca LK: 0 produtos, 0 coleções.

Ação recomendada:
- **Adicionar ao site como prioridade**, mas via fluxo Shopify aprovado: criar collection/hub + no mínimo 2–3 PDPs se houver sourcing/imagens/dados.
- Colorways âncora: Metallic Silver, Black, Triple White / White Metallic Silver Black.

### 3) Onitsuka Tiger Mexico 66 — já coberto; reforçar colorways

Evidência internacional:
- KicksDev StockX:
  - Birch Peacoat: 8.206 vendas 90d.
  - Silver Off White: 5.215 vendas 90d.
  - Birch Kale Red Gold: 241 vendas 90d.
- GOAT Kill Bill 2023: 404 vendas 90d.
- Google US: 110.000 buscas/mês; +82% YoY.
- Google BR: 6.600 buscas/mês; +50% YoY.

Presença LK pública:
- Produtos encontrados: Kill Bill, White Black, SD Kill Bill.
- Coleções: `/collections/onitsuka-tiger-mexico-66` e Fringe.

Ação recomendada:
- Já existe; validar se colorways globais fortes estão cobertas: Silver Off White e Birch Peacoat.

### 4) New Balance 204L — já coberto; manter como gold source

Evidência internacional:
- KicksDev StockX:
  - Mushroom Arid Stone: 6.598 vendas 90d; 16.135 all returned.
  - Sea Salt: 195 vendas 90d.
- Google US: 165.000 buscas/mês; spike enorme em 2026-03.
- Google BR: 12.100 buscas/mês; maio/2026 40.500.

Presença LK pública:
- Produtos encontrados: Arid Timberwolf, Mushroom Arid Stone, Sea Salt Linen.
- Coleção: `/collections/new-balance-204l`.

Ação recomendada:
- Não é novo add. Usar como referência visual/canônica LKGOC e validar gap de replenishment.

### 5) Nike Vomero Premium — já coberto; expandir colorways certas

Evidência internacional:
- KicksDev StockX:
  - Pale Ivory Jade Horizon: 4.969 vendas 90d.
  - Sail Coconut Milk: 2.696 vendas 90d; 5.113 all returned.
- GOAT: Sail Total Orange 87 90d; White Bright Crimson 55; White Lapis Total Orange 73.
- Google US: 60.500 buscas/mês; +5.592% YoY.
- Google BR: 22.200 buscas/mês; +70.614% YoY.

Presença LK pública:
- Produtos encontrados: Black Volt, Particle Rose Burgundy, Alabaster.
- Coleção: `/collections/nike-vomero-premium`.

Ação recomendada:
- Já existe; validar se temos Sail Coconut Milk / Pale Ivory Jade Horizon / White Lapis / White Bright Crimson.

### 6) Salomon XT-6 — GAP secundário forte

Evidência internacional:
- KicksDev StockX:
  - Cloudburst Icy Pink: 4.246 vendas 90d.
  - Vanilla Ice Almond Milk: 1.765 vendas 90d.
  - Vanilla Ice Oxford Tan: 717 vendas 90d.
- Google US: 22.200 buscas/mês; +83% YoY.
- Google BR: 2.400 buscas/mês; menor, mas tendência gorpcore/premium.

Presença LK pública:
- Busca LK: 0 produtos, 0 coleções.

Ação recomendada:
- Adicionar ao site se fizer sentido para curadoria premium/gorpcore.
- Começar por 2–3 colorways âncora, não coleção grande.

## Próximos candidatos se Lucas quiser 8–10

- ASICS Gel-NYC: forte Google US/BR e liquidez relevante; LK tem produtos mas não coleção pública. Candidato a collection/hub.
- ASICS Gel-Kayano 14: demanda US/BR enorme; LK tem coleção e produtos, mas KicksDev StockX deu erro 500 no probe; GOAT mostra liquidez moderada.
- Puma Speedcat: Google US/BR muito forte, LK já tem coleção/produtos; liquidez resale menor que buzz search.
- Adidas SL 72: Google BR fortíssimo e LK já tem coleção/produtos; liquidez resale menor no probe.

## Decisão operacional sugerida

### Sprint Site Add / Reativação

1. **Adicionar novos ao site — dependem de Shopify + dados de produto + aprovação:**
   - Nike P-6000
   - Salomon XT-6

2. **Já existem no site — fazer gap/replenishment + LKGOC/refino:**
   - Nike x Jacquemus Moon Shoe SP
   - Onitsuka Tiger Mexico 66
   - New Balance 204L
   - Nike Vomero Premium

3. **Se a intenção do Lucas for literalmente “6 novos modelos inexistentes”, rodar novo filtro apenas em modelos com zero presença LK e excluir os já cobertos.**

## Aprovação necessária

Para executar “adicionar no site”, preparar approval packet com:
- modelo/colorway/SKU;
- imagens/origem autorizada;
- descrição/title/meta;
- preço e disponibilidade validados por donos corretos;
- collection/tagging;
- rollback/readback.

Sem aprovação escopada, só pesquisa local/read-only e pacote de preview.

## Reminder OS

Reminder OS loop needed: yes
Owner: LK Collection Optimizer + LK Trends; handoff posterior para LK Shopify se Lucas aprovar write.
Próxima ação concreta: preparar Approval Packet Shopify para Nike P-6000 e Salomon XT-6, e gap-check `lk-stock`/compras para colorways dos 4 modelos já existentes.
Gatilho de revisão: aprovação explícita de Lucas para pacote Shopify/sourcing ou pedido de “filtrar só modelos inexistentes”.
Evidência verificável: arquivos KicksDev/DataForSEO e busca pública LK citados acima.
Status/writes externos: nenhum write externo executado.
