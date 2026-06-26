# Approval packet — Nike Mind guide LKGOC rewrite from zero

Data UTC: 20260606T094233Z
URL alvo: https://lksneakers.com.br/pages/guia-nike-mind-001-002
Tipo: LKGOC Correção/Rewrite-from-zero — guia dedicado/source page

## O que foi feito localmente

- Reescrita completa do body da página usando contrato `lk-goc-guide-*`.
- Mantido padrão visual/editorial do guia 204L/Moon Shoe, sem criar novo design system.
- Candidato limpo de `lk-source-page-*`, `lk-204l-*` e `lk-lkgoc-*`.
- Conteúdo reorganizado para: hero, definição, Mind 001, Mind 002, comparativo, styling, tamanho, sinais editoriais, leitura LK, produtos, FAQ e CTA.
- FAQPage JSON-LD único no candidato.
- 8 produtos preservados a partir da página pública atual.

## Arquivos

- Candidate body: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/drafts/nike-mind-guide-lkgoc-rewrite-20260606T094233Z/candidate-body.html`
- Extract público atual para rollback/referência: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/drafts/nike-mind-guide-lkgoc-rewrite-20260606T094233Z/public-current-article-extract.html`
- QA local: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/drafts/nike-mind-guide-lkgoc-rewrite-20260606T094233Z/qa-local.json`

## QA local

```json
{
  "has_lk_goc_guide": true,
  "has_legacy_lk_source_page": false,
  "has_lk_204l": false,
  "has_lk_lkgoc": false,
  "faq_schema_count": 1,
  "details_count": 8,
  "product_cards_precise": 8,
  "external_source_cards_precise": 3,
  "script_ld_json_count": 1,
  "body_chars": 24914,
  "font_typo_cormoriph": false
}
```

## Bloqueios antes de publicar

- Ainda não é decision-grade de produção: falta write/readback autenticado Shopify, preview DEV e QA visual desktop/mobile.
- Pelo canônico LKGOC, produção só após DEV/preview/readback e approval explícita atual.

## Rollback

- Restaurar o body público atual registrado em `public-current-article-extract.html` ou snapshot Shopify Admin antes do write.

## Decisão pedida

Aprovar aplicação do candidato em Shopify DEV/unpublished para preview e QA visual. Após preview aprovado, fazer merge/promoção para produção com receipt.
