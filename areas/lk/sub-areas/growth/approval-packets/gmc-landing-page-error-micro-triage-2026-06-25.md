# Approval packet — GMC landing_page_error micro-triagem — 2026-06-25

- Criado UTC: 2026-06-25T11:40:00Z
- Modo: read-only / preview
- Writes executados: 0
- values_printed=false
- Fonte principal: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-product-data-ranking-review-2026-06-25.md`
- CSV de offers: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-landing-page-error-packet-2026-06-25.csv`

## Problema

`landing_page_error` subiu para `161` produtos / `483` instâncias no Merchant Center, com reprovação em Shopping, DisplayAds e SurfacesAcrossGoogle. Delta vs 2026-06-18: `+152` produtos.

O bounded public `.js` check em 80 URLs encontrou:

- `ok`: 58
- `http_404`: 2
- `http_429`: 20

Interpretação: há mistura de links públicos ainda servíveis, 404 reais e limite/crawl público. Portanto, não é caso de bulk delete/suppress nem correção cega de PDP; precisa micro-triagem por offer/source.

## Escopo proposto

Micro-triagem readback/diagnóstico de 20–50 offers com `landing_page_error`, separando cada linha em:

1. `Shopify 404/despublicado`;
2. `link de feed antigo`;
3. `cache/reprocessamento Merchant`;
4. `produto que deve ser suprimido/removido do destino`;
5. `falso positivo / aguardar reprocessamento`.

## Ação após aprovação

Se Lucas aprovar, executar somente a micro-triagem/correção do escopo aprovado, com:

- snapshot do Product resource e source por offer antes;
- identificação do surface dono: Simprosys/API feed, ProductInput, supplemental/local feed ou Shopify publication/link;
- correção apenas no menor surface reversível;
- readback do Product link e productstatuses depois;
- sem `fetchNow`, delete, suppress, feed bulk ou Shopify write fora do escopo.

## Risco de overwrite

Médio/alto se a correção for feita no ProductInput enquanto Simprosys/API continuar enviando link antigo. O write precisa acontecer no surface dono ou será sobrescrito no próximo sync.

## Rollback

- Reverter o valor anterior do link/surface pelo mesmo canal usado na correção.
- Restaurar publication/suppression state se houver mudança aprovada nessa camada.
- Confirmar por readback Merchant/Product + productstatuses.

## Approval necessário

Qualquer GMC/feed/ProductInput/dataSource/Simprosys write, `fetchNow`, Shopify write, suppress/delete ou alteração de publicação exige aprovação explícita atual.

Frase segura:

> aprovado GMC landing_page_error micro-triagem 20-50 offers com snapshot readback e rollback
