# Playbook — CRO/PDP/collection surface LK Shopify

Data: 2026-06-05
Status: template operacional local/read-only até aprovação escopada.

## Quando usar

Use quando a demanda é melhorar conversão na superfície Shopify: PDP, cart, collection, busca, filtros, landing/page, CTA, prova social, blocos de confiança, frete, parcelamento, layout produto-first.

## Workers

1. Shopify Surface Mapper
2. CRO/UX Reviewer
3. Preview/Diff Builder
4. Shopify QA Visual Worker
5. Rollback/Risk Reviewer
6. Readback/Receipt Verifier — após execução aprovada

## Fronteira

- LK Growth pode originar hipótese, dados e impacto comercial.
- LK Shopify traduz em preview técnico/QA/execução de superfície.
- `[LK] Otimização de Coleções` assume se virar LKGOC, guia editorial de coleção ou experiência de coleção completa.

## Fluxo

1. **Hipótese CRO**
   - Página/URL:
   - Problema/fricção:
   - Evidência: GA4/GSC/GMC/Judge.me/Shopify/read-only/observação:
   - Métrica esperada:

2. **Mapear superfície Shopify**
   - Objeto: PDP/collection/page/cart/theme section/metafield/menu/tag.
   - Campo/section/snippet afetado:
   - Dependências de app/script:

3. **Proposta de melhoria**
   - Mudança de layout/copy/bloco:
   - Antes/depois esperado:
   - Impacto mobile:
   - Risco para compra/SEO/tracking:

4. **Preview/QA**
   - Preview visual ou textual.
   - QA mobile-first.
   - CTA/frete/parcelamento/prova social revisados.
   - Se tocar theme, dev theme por padrão.

5. **Follow-up**
   - Métrica a observar:
   - Janela de avaliação:
   - Dono da análise de impacto: LK Growth se for métrica Growth; LK Shopify se for QA técnico.

## Bloqueios

- Não alterar preço, estoque, status, campanha ou checkout sem packet próprio.
- Não reescrever coleção editorial/LKGOC dentro do Shopify OS.
- Não publicar theme/live sem aprovação escopada.

## Aprovação sugerida

> Aprovo LK Shopify executar esta melhoria CRO na superfície [PDP/collection/cart/page/theme] exatamente com os campos/arquivos listados, QA mobile-first, readback e rollback. Não aprovo preço/estoque/campanha/LKGOC fora do escopo.
