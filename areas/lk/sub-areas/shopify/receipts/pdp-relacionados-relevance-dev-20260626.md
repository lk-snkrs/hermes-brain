# Receipt — PDP Relacionados relevance DEV

- Data/hora: 2026-06-26T14:10:19.923045+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK / Shopify
- Responsável humano: lk-shopify
- Pedido original: Lucas aprovou DEV correção do bloco Relacionados do PDP com filtro por tipo/vendor, sem Production merge.
- Classificação: external-write
- Fontes usadas:
- Approval packet areas/lk/sub-areas/shopify/approval-packets/pdp-relacionados-relevance-dev-20260626.md; Shopify DEV Theme 155065450718; public preview QA.
- O que foi feito:
- Patch DEV em sections/lk-pdp.liquid: bloco Relacionados agora filtra candidatos por mesmo type+vendor, depois mesmo type, depois mesmo vendor; exclui produto atual antes de contar; escaneia até 32 e renderiza até 4; esconde bloco se menos de 2 cards.
- Output/artefato:
- DEV readback HTTP 200; SHA12 8780f0b0a391; marker data-lk-related-filtered=type-vendor-20260626. QA preview: 3 PDPs HTTP 200, Liquid errors 0, produto atual excluído; no boné Saint George removeu NB9060 Bone Sparrow e retornou 4 bonés relacionados.
- Aprovação: Aprovo DEV correção do bloco Relacionados do PDP com filtro por tipo/vendor, sem Production merge.
- Envio/publicação: Telegram
- Writes externos: Shopify DEV/unpublished theme only: Theme 155065450718 asset sections/lk-pdp.liquid. Sem Production merge. Sem produto/preço/estoque/Tiny/checkout/GMC/Klaviyo/ads/WhatsApp. values_printed=false.
- Riscos/bloqueios: Baixo/médio: pode reduzir quantidade de relacionados em PDPs com coleção ruim; preferível a exibir recomendações incoerentes. Curadoria LK permanece separada.
- Rollback/mitigação: Restaurar /opt/data/profiles/lk-shopify/workdirs/pdp-relacionados-relevance-20260626/dev_before_sections__lk-pdp.liquid no asset DEV sections/lk-pdp.liquid.
- Próximos passos: Lucas validar preview DEV; Production merge exige aprovação separada.
- Onde foi documentado no Brain: Workdir /opt/data/profiles/lk-shopify/workdirs/pdp-relacionados-relevance-20260626 com before/target/readback/QA.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
