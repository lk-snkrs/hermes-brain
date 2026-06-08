# Nike Mind — execução aprovada dos 3 pacotes

UTC: 2026-06-07T12:45:33.782576+00:00

## Aprovação
Lucas aprovou os 3 caminhos: GTIN/GMC, SEO/GEO e CRO.

## Executado em produção

### SEO/GEO — Admin OK
- Smart collection `nike-mind-001` atualizada via Shopify Admin.
- Title da collection: `Nike Mind 001 e 002`.
- SEO nativo via GraphQL:
  - title: `Nike Mind 001 e 002 Original | Curadoria LK`
  - description: `Compare Nike Mind 001 e 002 na LK Sneakers. Curadoria premium, autenticidade e atendimento humano para escolher o modelo ideal.`
- DescriptionHtml atualizado com blocos citáveis/FAQ:
  - Nike Mind 001 vs Nike Mind 002
  - O que o Nike Mind faz?
  - Para que serve?
  - Autenticidade/curadoria LK
- UserErrors GraphQL: `[]`.

### Theme/CRO — Admin OK / público não confirmado
- Production theme: `155065417950` (`lk-new-theme/production`).
- Assets alterados com snapshot:
  - `snippets/lk-goc-collection.liquid`
  - `sections/lk-collection.liquid`
- Admin readback confirmou:
  - branch `nike-mind-001` no snippet;
  - CTA `Ver guia 001 vs 002`;
  - CTA `Ver seleção LK`;
  - trust `Atendimento humano`;
  - fallback section marker `lk-nike-mind-approved-cro-20260607`.
- Readback público em HTML ainda NÃO mostrou o CTA/marker depois de múltiplas tentativas. Pode ser caminho condicional/template/cache. Não considerar CRO como publicamente validado até nova checagem.

### Public QA
- URL: `https://lksneakers.com.br/collections/nike-mind-001`
- Público já mostra sinal de nova descrição/override: `conforto sensorial` presente.
- Público ainda mostra head antigo:
  - title: `Nike Mind 001 Original na LK Sneakers`
  - description: `Compre Nike Mind original na LK Sneakers...`
- Admin SEO nativo está correto; discrepância pública registrada para follow-up/cache/theme head override.

## GTIN/GMC — aprovado, mas não executado por ausência de fonte verificável
- Não foi feito write de barcode/GTIN.
- Motivo: busca local/autenticada não encontrou GTIN/EAN real por SKU; os arquivos tinham SKUs, mas nenhum EAN/GTIN próximo.
- Guardrail aplicado: não inventar GTIN/EAN.
- Próximo passo: fonte operacional/confiável com tabela `SKU → GTIN/EAN` ou decisão separada por fallback GMC (`identifier_exists`/MPN/brand) conforme política.

## Rollback
- Restaurar `before__snippets__lk-goc-collection.liquid`.
- Restaurar `before__sections__lk-collection.liquid` ou `before3__sections__lk-collection.liquid` para desfazer apenas fallback.
- Restaurar smart collection a partir de `before__smart_collection_nike_mind_001.json`.

## Arquivos principais
- `QA.json`
- `ROLLBACK.md`
- `before__smart_collection_nike_mind_001.json`
- `after_graphql_collection_seo_update.json`
- `public_qa_after_graphql_seo.json`
- `public_qa_after_cro_fallback.json`
