# Receipt — Receipt — FAQ Intent v2 Apply — 20260616

- Data/hora: 2026-06-16T15:50:35.715149+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK/Growth
- Responsável humano: Lucas Cimino
- Pedido original: Aplicar FAQ Intent v2 aprovado no PDP Nike Mind 001 e na coleção Nike Vomero Premium
- Classificação: external-write
- Fontes usadas:
- Aprovação explícita Lucas Telegram + Approval Packet FAQ Intent v2 + Shopify GraphQL + fetch público
- O que foi feito:
- Atualizado descriptionHtml do PDP Nike Mind 001 e descriptionHtml da collection Nike Vomero Premium; readback Shopify OK; fetch público PDP OK; fetch público collection mostrou FAQ antigo vindo de theme section lk-collection.liquid, fora do escopo de write production theme
- Output/artefato:
- areas/lk/sub-areas/growth/work/faq-intent-v2-apply-20260616/apply-results.json
- Aprovação: Aprovo aplicar o FAQ Intent v2 de 2026-06-16 no PDP Nike Mind 001 Black Chrome e na coleção Nike Vomero Premium, somente nos blocos FAQ/descrição listados, com rollback/readback, sem alterar preço, estoque, desconto, campanhas, GMC/feed, Klaviyo/WhatsApp ou theme production fora do escopo. FAQ global do tema deve ficar apenas como dev-preview/packet separado.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: Shopify GraphQL productUpdate.descriptionHtml e collectionUpdate.descriptionHtml; nenhum theme production write
- Riscos/bloqueios: Sem risco externo; escopo local/documental.
- Rollback/mitigação: Rollback salvo em work/faq-intent-v2-apply-20260616/before.json, product-description-before.html e collection-description-before.html
- Próximos passos: Observar próximos ciclos e evoluir somente por escopo aprovado.
- Onde foi documentado no Brain: areas/lk/sub-areas/growth/work/faq-intent-v2-apply-20260616/readback-checks.json
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
