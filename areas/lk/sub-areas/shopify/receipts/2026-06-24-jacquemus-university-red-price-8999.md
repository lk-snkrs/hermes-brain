# Receipt — Shopify price update — Jacquemus University Red para R$ 8.999,99

- Data/hora: 2026-06-24T14:31:11.735013+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify
- Responsável humano: Lucas Cimino
- Pedido original: Lucas pediu no Telegram: diminuir o preço do Jacquemus University Red / Jacquemus x Nike para R$ 8.999,99.
- Classificação: external-write
- Fontes usadas:
- Shopify Admin API resolve: produto único encontrado, product_id=9030659473630, handle=tenis-nike-moon-shoe-sp-jacquemus-university-red-vermelho; snapshot antes em /opt/data/profiles/lk-shopify/workdirs/shopify-price-change/20260624T143046Z_jacquemus_university_red_before_8999.json; values_printed=false.
- O que foi feito:
- Atualizado via Shopify Admin REST PUT /variants/{id}.json o campo price para 8999.99 em todas as 12 variantes do produto Tênis Nike Moon Shoe SP Jacquemus University Red Vermelho.
- Output/artefato:
- Readback Shopify GraphQL confirmou 12/12 variantes com price=8999.99; HTTP statuses de update=[200]; verify em /opt/data/profiles/lk-shopify/workdirs/shopify-price-change/20260624T143046Z_jacquemus_university_red_after_8999.json; values_printed=false.
- Aprovação: Aprovação explícita e escopada no próprio comando de Lucas: “diminua para 8.999,,99 por favor”. Escopo interpretado: alterar preço de todas as variantes do mesmo produto recém-ajustado para R$ 8.999,99.
- Envio/publicação: Resposta no Telegram com evidência, risco e rollback.
- Writes externos: Shopify Admin write: product variant price atualizado em 12 variantes do product_id=9030659473630.
- Riscos/bloqueios: Compare-at price existente permaneceu inalterado em 3999.99, abaixo do novo preço; não foi alterado porque Lucas solicitou somente preço. Pode exigir revisão de merchandising/compare-at se a vitrine destacar desconto/anomalia.
- Rollback/mitigação: Usar snapshot antes para restaurar price=9999.99 nas 12 variantes; snapshot anterior do ajuste inicial também permite voltar para price=6999.99. compareAtPrice não foi alterado.
- Próximos passos: Se Lucas quiser, revisar/remover compare-at price desse produto para evitar sinalização comercial inconsistente; isso exigirá aprovação escopada separada.
- Onde foi documentado no Brain: Receipt criado pelo Memory OS writer; snapshot e readback locais armazenados no workdir do perfil.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
