# Receipt — Google Reviews cron sync para Shopify metafield

- Data/hora: 2026-06-25T16:46:18.780320+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify
- Responsável humano: lk-shopify
- Pedido original: Lucas aprovou: Aprovo sync cron, em resposta ao pedido para o Trust Grid do /cart sempre puxar a quantidade correta de avaliações Google usando a lógica do cron.
- Classificação: external-write
- Fontes usadas:
- Cron state /opt/data/profiles/lk-shopify/cron/state/lk_google_reviews_state.json; script /opt/data/profiles/lk-shopify/scripts/lk_google_reviews_monitor.py; wrapper /opt/data/profiles/lk-shopify/scripts/lk_google_reviews_monitor.sh; Doppler helper profile map; Shopify Admin GraphQL readback; artifact /opt/data/profiles/lk-shopify/cron/output/lk-google-reviews-monitor/2026-06-25_16-45-03.json.
- O que foi feito:
- Patchado o cron lk_google_reviews_monitor.py para, após leitura Google Places OK, sincronizar shop.metafields.lk_google.reviews via Shopify Admin GraphQL. Atualizado wrapper para usar hermes_doppler.py run --profile lk-shopify. Atualizado helper Doppler profile map lk-shopify para injetar GOOGLE_API_KEY/GOOGLE_PLACES_API_KEY sem imprimir valores. Executado sync imediato aprovado.
- Output/artefato:
- Metafield Shopify lk_google.reviews atualizado de count 384 para 420; state cron atualizado para userRatingCount 420; segundo run retornou rc=0 e stdout_bytes=0, com artifact status ok_same e shopify_metafield_sync ok_same. values_printed=false.
- Aprovação: Aprovação explícita atual de Lucas: Aprovo sync cron.
- Envio/publicação: Telegram final com evidência, estado atual e rollback.
- Writes externos: Shopify Admin GraphQL metafieldsSet para shop.metafields.lk_google.reviews; mudança local em cron script/wrapper e helper Doppler map. Sem theme/checkout/produto/preço/estoque/campanha.
- Riscos/bloqueios: Cron passa a fazer write recorrente em Shopify metafield após Google Places OK. Failure mode tratado com alerta e artifact; OK/no-change fica silencioso. Checkout extension continua não atualizada automaticamente e ainda exige deploy manual se o texto hardcoded do checkout precisar refletir 420.
- Rollback/mitigação: Restaurar backups em /opt/data/profiles/lk-shopify/workdirs/google-reviews-cron-sync-20260625/*.before para script/wrapper; remover GOOGLE keys do profile map se necessário; opcionalmente restaurar metafield para valor anterior 384 via Admin GraphQL se Lucas pedir rollback visual.
- Próximos passos: Revalidar /cart público quando Shopify/edge/429 permitirem; se Lucas quiser checkout também em 420, preparar approval packet/deploy da checkout extension separadamente.
- Onde foi documentado no Brain: Skill reference cart-trust-grid-google-reviews-parity-20260625 atualizada com o sync aprovado e contrato silent-OK.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
