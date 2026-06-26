# LK Ranking continuation — depois das melhorias da semana passada — 2026-06-22

**Registrado:** 2026-06-22T13:28:31.295029+00:00  
**Origem:** Lucas confirmou: “vamos continuar, já fizemos algumas melhorias na semana passada”.  
**Modo:** Brain/local only; writes externos 0; values_printed=false.

## Melhorias já feitas / não repetir sem medir

### Nike Mind 001 PDPs
- Pacote B CTR Produtos aplicado em 2026-06-19 nos PDPs:
  - `slide-nike-mind-001-light-smoke-grey-cinza`
  - `slide-nike-mind-001-pearl-pink-rosa`
- Depois houve correção de nomenclatura para **Nike Mind Slide 001**.
- FAQ7 implementado no `custom.faq` e body limpo nos 2 PDPs.
- Patch de parity no `sections/lk-pdp.liquid`: se `custom.faq` existir, FAQ visual e JSON-LD devem usar FAQ do produto; institucional só fallback.
- QA de 2026-06-20 confirmou estabilização pública nos 2 PDPs: HTTP 200, H1 único, 7 FAQ visíveis e 7 em FAQPage, sem FAQ genérico legado.
- Impact review comercial ainda pendente por janela curta: D+7 ~2026-06-26.

### Nike Vomero Premium PDP
- Pacote B CTR Produtos aplicado no PDP `tenis-nike-vomero-premium-white-bright-crimson-branco` em 2026-06-19.
- Public readback inicial oscilou por cache; precisa revalidar antes de novo write.

### Nike Mind 002
- Nike Mind 002 Black Hyper Crimson já teve receipt aprovado em 2026-06-17 para SEO/FAQ (`receipts/product-seo/nike-mind-002-black-hyper-crimson-20260617T144556Z/receipt.md`).
- Não tratar Mind 002 como vazio; próxima onda deve mapear os demais PDPs/collection/hub e evitar duplicação com Mind 001.

## Achados atuais de continuação

### Collections com duplicação editorial/schema aparente
Fetch público de 2026-06-22 mostra que as collections já têm conteúdo rico, mas com blocos repetidos/duplicados:

- `/collections/nike-mind-001`: conteúdo de guia aparece duas vezes, com dois blocos “Guia editorial LK” e duas áreas citáveis/FAQ. O relatório de 2026-06-20 já apontava 2 `FAQPage` JSON-LD.
- `/collections/nike-vomero-premium`: também mostra dois blocos “Guia editorial LK”/citáveis, indicando risco semelhante de duplicação e excesso textual.

## Estratégia correta daqui para frente

Não reabrir os PDPs Mind 001 já corrigidos antes do D+7, salvo bug público. A próxima melhoria deve ser **consolidação de collection/hub e schema único**, pois:

1. preserva o que já foi aplicado;
2. reduz ruído de FAQ/guia duplicado;
3. melhora leitura para Google/AI sem mexer em preço/estoque/disponibilidade;
4. cria arquitetura clara Mind 001 vs Mind 002 vs Vomero vs Onitsuka.

## Próximos packets recomendados

### Packet A — Nike Mind hub/collection cleanup
- Escopo: `/collections/nike-mind-001` e guia `/pages/guia-nike-mind-001-002` se necessário.
- Objetivo: consolidar conteúdo repetido em um bloco canônico, deixar 1 FAQ visual e 1 FAQPage JSON-LD, reforçar links para Mind 001 e Mind 002.
- Sem alterar PDPs Mind 001 já corrigidos antes de D+7, exceto links internos se explicitamente aprovado.

### Packet B — Vomero Premium collection cleanup
- Escopo: `/collections/nike-vomero-premium` e `/pages/nike-vomero-premium-guia`.
- Objetivo: remover duplicação de guia/FAQ, preservar conteúdo premium e estruturar snippet citável curto.
- PDP White Bright Crimson só revalidar; não novo write até impact/readback ficar claro.

### Packet C — Onitsuka Tiger CTR/source-page expansion
- Escopo: collection todos modelos + source/guide intent `original / Mexico 66 / onde comprar`.
- Objetivo: capturar CTR e AI citation sem refazer layout aprovado.

### Packet D — 204L protect/benchmark
- Escopo: QA/paridade, não reescrita.
- Objetivo: manter como gold source e benchmark de score.

## Aprovação necessária no futuro

Qualquer aplicação em Shopify production/theme/schema/content precisa de aprovação explícita com wording escopado e rollback.
