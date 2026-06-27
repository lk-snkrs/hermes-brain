# Receipt — PDP Product Suggestions v2 DEV

- Data/hora: 2026-06-26T14:24:02.210322+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK / Shopify
- Responsável humano: lk-shopify
- Pedido original: Lucas aprovou DEV Product Suggestions v2 no PDP usando Recommendations API filtrada + fallback Liquid, sem Production merge.
- Classificação: external-write
- Fontes usadas:
- Approval packet areas/lk/sub-areas/shopify/approval-packets/pdp-product-suggestions-v2-dev-20260626.md; DEV theme 155065450718; readback Shopify; QA preview/simulação API.
- O que foi feito:
- Patch DEV em sections/lk-pdp.liquid: bloco Relacionados virou Product Suggestions v2 com /recommendations/products.json intent=related, filtro por tipo/vendor, exclusão de produto atual e handles de Curadoria LK, fallback Liquid filtrado, marker data-lk-related-v2=recommendations-filtered-20260626.
- Output/artefato:
- DEV readback HTTP 200; SHA12 776e9099ffc8; marker v2 e fetch API presentes; old filtered marker removido; unfiltered collection limit:4 ausente. QA: HTTP 200 e Liquid errors 0 nos PDPs Saint George, AJ1 Panda e Onitsuka Triple Black; JS extraído passou node --check; simulação filtrou cross-type e removeu NB9060 Bone Sparrow.
- Aprovação: Aprovo DEV Product Suggestions v2 no PDP usando Recommendations API filtrada + fallback Liquid, sem Production merge.
- Envio/publicação: Telegram
- Writes externos: Shopify DEV/unpublished theme only: Theme 155065450718 asset sections/lk-pdp.liquid. Sem Production merge. Sem produto/preço/estoque/Tiny/checkout/GMC/Klaviyo/ads/WhatsApp. values_printed=false.
- Riscos/bloqueios: Médio: JS client-side no PDP; se API não retornar candidatos bons, fallback Liquid filtrado mantém bloco coerente ou esconde. Curadoria LK preservada e usada para evitar duplicação.
- Rollback/mitigação: Restaurar /opt/data/profiles/lk-shopify/workdirs/pdp-product-suggestions-v2-20260626/dev_before_sections__lk-pdp.liquid no asset DEV sections/lk-pdp.liquid; ou voltar para backup anterior em /opt/data/profiles/lk-shopify/workdirs/pdp-relacionados-relevance-20260626/.
- Próximos passos: Lucas validar preview DEV; Production merge exige aprovação separada.
- Onde foi documentado no Brain: Workdir /opt/data/profiles/lk-shopify/workdirs/pdp-product-suggestions-v2-20260626 com before/target/readback/QA/script extraído.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
