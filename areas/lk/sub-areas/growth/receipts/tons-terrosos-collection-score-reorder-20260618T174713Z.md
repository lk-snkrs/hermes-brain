# Receipt — Tons terrosos — reorder por Collection Scoring System LK

- Data/hora: 2026-06-18T17:51:28.289755+00:00
- Agente/profile/cron: lk-growth
- Empresa/área: LK Sneakers / Growth / Shopify Collections
- Responsável humano: Hermes LK Growth
- Pedido original: Lucas aprovou aplicar o reorder da coleção Tons terrosos pelo Collection Scoring System LK.
- Classificação: external-write
- Fontes usadas:
- Shopify Admin API via Doppler/Hermes wrapper; GA4 Data API read-only; aprovação explícita no Telegram; script /opt/data/profiles/lk-growth/scripts/lk_collection_scoring_system.py; output /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/collection-scoring/tons-terrosos-sao-os-novos-neutros-20260618T174713Z/; values_printed=false.
- O que foi feito:
- Aplicado reorder manual da coleção Shopify tons-terrosos-sao-os-novos-neutros com fórmula 70% vendas + 30% visitas PDP, janelas 30/90/180 e gate comercial. Produtos lidos: 150. Produtos ranqueados: 150. Zero venda 180d: 0. Shopify collection ID 1128528838878. collectionReorderProducts executado sem userErrors.
- Output/artefato:
- Readback Admin: 150 itens, expected 150, mismatch_count_first_50_recorded 0. Storefront /products.json confirmou top 5 público: New Balance 204L Arid Timberwolf; New Balance 204L Mushroom Arid Stone; Nike Moon Shoe SP Jacquemus Off White; Nike Moon Shoe SP Jacquemus Medium Brown; Onitsuka Tiger Mexico 66 SD Beige Beet Juice.
- Aprovação: Aprovação explícita de Lucas no turno atual: “Aprovo aplicar o reorder da coleção Tons terrosos pelo Collection Scoring System LK.”
- Envio/publicação: Sem envio externo/customer-facing além da alteração da ordem da coleção já aprovada na Shopify.
- Writes externos: Shopify collectionReorderProducts na coleção 1128528838878; sem alterações de produto, preço, estoque, tema, descrição, campanha, GMC, Klaviyo ou Meta.
- Riscos/bloqueios: Cache/CDN da vitrine pode atrasar atualização HTML, mas products.json já refletiu a ordem. Score depende de pedidos Shopify e pageviews GA4 disponíveis no momento da execução.
- Rollback/mitigação: Snapshot antes do reorder salvo em /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/collection-scoring/tons-terrosos-sao-os-novos-neutros-20260618T174713Z/rollback-before-order.json. Para rollback, reordenar coleção pela sequência desse arquivo via collectionReorderProducts em batches <=250.
- Próximos passos: Revisar impacto em aproximadamente 7 dias: GA4 coleção/PDP, Shopify pedidos/revenue da coleção, CTR/engajamento se houver tráfego para a landing. Considerar curadoria manual top 24 apenas se Lucas quiser camada editorial além do score.
- Onde foi documentado no Brain: SOP canônico criado em COLLECTION-SCORING-SYSTEM-LK.md; skill lk-superpowers-collection-optimizer atualizada; relatório/ranking/readback em reports/collection-scoring/tons-terrosos-sao-os-novos-neutros-20260618T174713Z/.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
