# Receipt — LK Stock Shopify SKU from Tiny safe apply

- Data/hora: 2026-06-12T01:11:36.716542+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock OS + Shopify
- Responsável humano: Lucas Cimino
- Pedido original: Adicionar no Shopify o SKU que está no Tiny para produtos/variantes sem SKU, usando somente alvos seguros.
- Classificação: external-write
- Fontes usadas:
- Relatório de candidatos Shopify sem SKU/barcode; Tiny read-only title fallback; Shopify REST Admin GET/PUT variant; readback GET pós-write.
- O que foi feito:
- Executado SKU-only Shopify write para 4 variantes seguras: variant tinha SKU vazio, Tiny código não vazio, match Tiny exato por título, e produto tinha variante única no handle. 11 candidatas foram puladas por Tiny código vazio ou mapeamento multi-variante ambíguo.
- Output/artefato:
- Report/backup: areas/lk/sub-areas/stock/reports/lk-stock-shopify-sku-from-tiny-safe-apply-20260612T011049Z.json. Atualizadas e verificadas: 45771412930782=fv3623-151; 45849007292638=DQ8394301; 47437381992670=DB4612-100; 47553172668638=w51154r. Suíte Stock OS 30 tests OK.
- Aprovação: Lucas pediu explicitamente no Telegram: Adicione na Shopify o sku que está no Tiny por favor. Escopo aplicado somente a SKU de variante com alvo seguro; sem preço/estoque/título/tema.
- Envio/publicação: Nenhum envio externo/customer-facing; apenas write administrativo Shopify SKU-only.
- Writes externos: Shopify SKU-only variant PUT em 4 variantes; Tiny write 0; preço/estoque/título/produto/tema/cliente 0.
- Riscos/bloqueios: Variantes com Tiny código vazio não foram alteradas. Produto Voodoo multi-variante com mesmo candidato Tiny foi pulado para evitar SKU errado sem mapeamento de tamanho.
- Rollback/mitigação: Usar backup no JSON report para restaurar sku anterior null nas 4 variantes via Shopify REST PUT /variants/{id}.json se Lucas pedir rollback.
- Próximos passos: Revarrer Shopify/DB local depois do próximo sync e resolver filas puladas: Tiny código vazio exige código canônico; multi-variante exige mapeamento por tamanho/grade.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/reports/lk-stock-shopify-sku-from-tiny-safe-apply-20260612T011049Z.json
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
