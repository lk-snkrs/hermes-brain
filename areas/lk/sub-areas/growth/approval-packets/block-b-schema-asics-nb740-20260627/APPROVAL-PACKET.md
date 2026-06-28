# Approval Packet — Bloco B pós readback: schema Tokyo/Speedcat, cleanup ASICS, NB740 canônico

Data: 2026-06-27
Owner: [LK] Growth
Status: aguardando aprovação explícita
Base: Bloco A read-only concluído via Shopify CLI oficial
values_printed=false

## Diagnóstico confirmado

1. `snippets/lk-goc-schema-extra.liquid` existe em production e contém schema para Adidas Tokyo e Puma Speedcat.
2. `sections/lk-collection.liquid` production **não renderiza** esse snippet atualmente.
3. Por isso `/collections/adidas-tokyo` e `/collections/puma-speedcat` estão `FAQPage=0` no HTML público.
4. `asics-gel-nyc` existe no Admin, mas está sem SEO title/description; o público usa fallback e `og:description` global com `Envio imediato e troca grátis`.
5. `new-balance-740` não retornou como collection Admin por handle e a URL pública finaliza na collection geral.

## Escopo proposto

### Ação 1 — restaurar schema Tokyo/Speedcat em production

- Fazer backup/readback de `sections/lk-collection.liquid` e `snippets/lk-goc-schema-extra.liquid`.
- Aplicar patch mínimo para renderizar uma única vez o snippet `lk-goc-schema-extra` no section de collection.
- QA público:
  - Tokyo `FAQPage=1`;
  - Speedcat `FAQPage=1`;
  - controle sem vazamento/duplicidade indevida;
  - `Liquid error=false`.

### Ação 2 — cleanup SEO/meta ASICS Gel NYC

- Fazer backup Admin da collection `asics-gel-nyc`.
- Definir SEO title/meta premium ou ajustar fonte necessária para remover termo operacional de head/meta/OG.
- Sem mudança de produtos, preço, estoque ou visual.
- QA público: head/meta/OG sem `envio imediato` e sem `troca grátis`.

### Ação 3 — handoff NB740 para LK Shopify

- Abrir handoff para LK Shopify validar/criar collection canônica `new-balance-740` usando produtos ativos já existentes.
- Growth não consulta estoque e não altera grade/preço/produtos.
- Após collection canônica, Growth prepara guia/FAQ/schema em DEV antes de produção.

## Risco e rollback

| Ação | Risco | Rollback |
|---|---|---|
| Render schema extra | médio-baixo | Restaurar backup do section/snippet e readback público. |
| ASICS meta cleanup | baixo-médio | Restaurar SEO/metafields anteriores via backup Admin. |
| NB740 handoff | médio | LK Shopify com rollback próprio de collection/template/metafields. |

## Aprovação sugerida

`Aprovo Bloco B: restaurar em produção o render único do snippet lk-goc-schema-extra para recuperar FAQPage schema em Adidas Tokyo e Puma Speedcat; limpar SEO/meta/OG da collection ASICS Gel NYC para remover termos operacionais; e abrir handoff para LK Shopify criar/validar a collection canônica New Balance 740. Sem alterar preço, estoque, produtos, ordenação, GMC, campanhas, Klaviyo, checkout ou consultar estoque.`
