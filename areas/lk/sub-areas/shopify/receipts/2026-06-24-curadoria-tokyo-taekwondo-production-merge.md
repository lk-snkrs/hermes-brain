# Receipt — Curadoria LK PDP — Adidas Tokyo Mary Jane + Taekwondo regular/Mei Production merge

- Data/hora: 2026-06-24T19:18:01.133194+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify theme
- Responsável humano: Lucas Cimino
- Pedido original: Adicionar Curadoria LK / Outras variações para Adidas Tokyo Mary Jane e Adidas Taekwondo regular/Mei; Lucas aprovou “Aprovo merge” em resposta ao packet.
- Classificação: external-write
- Fontes usadas:
- Approval packet areas/lk/sub-areas/shopify/approval-packets/2026-06-24-curadoria-tokyo-taekwondo-pdp.md; static/preflight QA /opt/data/profiles/lk-shopify/workdirs/curadoria-tokyo-taekwondo-20260624/20260624T190954Z_static_preflight.json; values_printed=false.
- O que foi feito:
- Production via GitHub PR #89 em lk-snkrs/lk-new-theme; branch hermes/tokyo-taekwondo-curadoria-20260624; merge commit 822ccca51bfc1c2388e0dbbbfe7382491d87d9c0. Criado split snippet snippets/lk-variante-tokyo-taekwondo-20260624.liquid e render line em snippets/lk-variante-top30-visited-v2.liquid. Sem direct Asset API em Production. DEV não foi aplicado porque Lucas aprovou apenas merge.
- Output/artefato:
- Shopify Production readback OK no theme 155065417950 em /opt/data/profiles/lk-shopify/workdirs/curadoria-tokyo-taekwondo-20260624/20260624T191618Z_production_readback.json. Public QA inicial: Tokyo 6/9 OK, Taekwondo 2/9 OK; focused QA: Tokyo Sandy Pink 6/6 OK, Taekwondo Core Black 4/6 OK, Taekwondo Mei Clear Pink 0/6 never_ok imediato. Source/readback correto, público parcial/edge ou possível render caveat para Mei.
- Aprovação: Lucas escreveu “Aprovo merge” no Telegram em resposta ao approval packet que pedia “Aprovo merge Production Curadoria Tokyo Taekwondo”.
- Envio/publicação: Resposta no Telegram com PR/merge, readback, QA público parcial, caveat de Mei never_ok e rollback.
- Writes externos: GitHub PR #89 criado e mergeado para production. Nenhum write direto no Shopify Production via Asset API. Nenhum upload DEV.
- Riscos/bloqueios: PDP Taekwondo Mei Clear Pink Gum ainda não renderizou o marker em focused QA imediato apesar de estar ACTIVE/template default; pode ser edge/cache ou render-condition/semântica do handle. Não fazer rollback automático; monitorar/rodar QA tardio ou preparar repair focado se persistir.
- Rollback/mitigação: Reverter PR #89/merge commit 822ccca51bfc1c2388e0dbbbfe7382491d87d9c0 para remover render line e deletar snippets/lk-variante-tokyo-taekwondo-20260624.liquid.
- Próximos passos: Rodar QA tardio do Taekwondo Mei; se permanecer never_ok, preparar diagnóstico/repair focado ou remover o Mei do grupo se Lucas preferir sem caveat.
- Onde foi documentado no Brain: Receipt criado via Memory OS writer; approval packet e QA artifacts referenciados.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
