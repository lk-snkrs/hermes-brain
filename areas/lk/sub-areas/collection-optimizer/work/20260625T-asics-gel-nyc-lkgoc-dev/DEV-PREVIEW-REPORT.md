# DEV Preview — ASICS GEL-NYC LKGOC Lite pós-grid

Data: 2026-06-25  
Aprovação Lucas: “Aprovo seguir” após backlog audit.  
Theme DEV: `lk-new-theme/dev` (`theme_id=155065450718`, `role=unpublished`)  
Production/main: **não promovido**.  
Writes externos: Shopify theme DEV/unpublished, limitado a `sections/lk-collection.liquid` e `snippets/lk-goc-collection.liquid`.  
values_printed: false

## Status

**PASS** — preview DEV aplicado e QA público passou.

## O que foi feito

1. `sections/lk-collection.liquid`
   - adiciona override curto de banner para `asics-gel-nyc`;
   - mantém vitrine produto-first;
   - renderiza o Guia LK no ponto pós-grid controlado pelo tema.
2. `snippets/lk-goc-collection.liquid`
   - adiciona bloco LKGOC Lite para `asics-gel-nyc`;
   - inclui Guia editorial LK, cards de escolha, FAQ visual e bloco citável;
   - não adiciona schema próprio porque o tema já emite 1 `FAQPage` para o handle no preview, evitando duplicidade.

## Evidência usada

- Backlog audit: `asics-gel-nyc` priorizada #1.
- DataForSEO Brasil: keyword `asics gel nyc`, volume 60.500, intenção transacional/informacional.
- SERP Brasil: ASICS Brasil, Artwalk, Danki, Ostore, Netshoes e Google Popular Products indicam demanda comercial e comparação por colorway/modelo.
- Fonte ASICS oficial via fetch direto ficou indisponível por robots/conexão; fallback foi SERP + dados públicos + padrão LKGOC.

## QA DEV público

| Handle | HTTP | H1 | FAQPage | Guia LK | Bloco citável | Liquid error | Pós-grid |
|---|---:|---:|---:|---:|---:|---:|---|
| `asics-gel-nyc` | 200 | 1 | 1 | 1 | 1 | não | PASS |
| `new-balance-204l` benchmark DEV | 200 | 1 | 1 | 1 | 0 | não | PASS básico |

### Sequência ASICS GEL-NYC

`1 itens` 2938 → `Ordenar:` 2946 → `Guia editorial LK` 3413

Resultado: **PASS**.

## Production untouched

| Handle | HTTP | Guia LK público | Bloco citável público | DEV guide público? | Liquid error |
|---|---:|---:|---:|---:|---:|
| `asics-gel-nyc` | 200 | 0 | 0 | não | não |

## Screenshots

- `asics-dev-v2-mobile.png`
- `asics-dev-v2-desktop.png`
- `204l-dev-mobile.png`

## Rollback DEV

Rollback preparado, não executado:

`rollback_dev_asics_gel_nyc_assets.py`

Backups:

- `backup-before-sections__lk-collection.liquid`
- `backup-before-snippets__lk-goc-collection.liquid`

## Próxima aprovação necessária

Para production/main, ainda precisa aprovação explícita porque é mudança customer-facing.

Frase segura:

> Aprovo promover para production/main o LKGOC Lite pós-grid de ASICS GEL-NYC validado no DEV `lk-new-theme/dev` (`theme_id=155065450718`), limitado a `sections/lk-collection.liquid` e `snippets/lk-goc-collection.liquid`, sem preço, estoque, produtos, ordenação, GMC, Klaviyo, campanhas ou checkout, com backup, readback público, QA mobile/desktop e rollback.
