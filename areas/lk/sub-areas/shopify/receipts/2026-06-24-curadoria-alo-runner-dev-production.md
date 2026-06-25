# Receipt — Curadoria LK PDP — Alo Runner DEV + Production merge

- Data/hora: 2026-06-24T14:55:01.537282+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify theme
- Responsável humano: Lucas Cimino
- Pedido original: Adicionar o grid Curadoria LK / Outras variações (class lk-variante) na PDP https://lksneakers.com.br/products/tenis-alo-yoga-alo-runner-gravel-bege; Lucas aprovou explicitamente DEV Curadoria Alo Runner e merge Production Curadoria Alo Runner.
- Classificação: external-write
- Fontes usadas:
- Approval packet areas/lk/sub-areas/shopify/approval-packets/2026-06-24-curadoria-alo-runner-pdp.md; Shopify Admin read-only resolveu product_id=8983509598430; QA local em /opt/data/profiles/lk-shopify/workdirs/curadoria-alo-runner-20260624/static_qa.json; values_printed=false.
- O que foi feito:
- DEV: upload para theme 155065450718 (lk-new-theme/dev) dos assets snippets/lk-variante-top30-visited-v2.liquid e snippets/lk-variante-alo-runner-20260624.liquid, com backup antes. Production: PR #86 no GitHub lk-snkrs/lk-new-theme, branch hermes/alo-runner-curadoria-20260624 para production, merge commit a3231273737694875445d66187dfca9a1e5cb6de.
- Output/artefato:
- DEV readback OK para ambos assets: /opt/data/profiles/lk-shopify/workdirs/curadoria-alo-runner-20260624/20260624T145133Z_dev_upload_readback.json. Production Shopify readback OK no theme 155065417950: render line e split snippet presentes, /opt/data/profiles/lk-shopify/workdirs/curadoria-alo-runner-20260624/20260624T145342Z_production_readback.json. Public QA mostrou render intermitente por edge/cache; focused Gravel teve sucesso em 4/8 tentativas, com marker top30-alo-runner-colorways, 5 cards e current excluído.
- Aprovação: Lucas escreveu no Telegram: “Aprovo DEV Curadoria Alo Runner” e “Aprovo merge Production Curadoria Alo Runner”. Escopo limitado ao grupo Curadoria LK Alo Runner.
- Envio/publicação: Responder no Telegram com source/readback OK, QA pública parcial/intermitente e rollback.
- Writes externos: Shopify Asset API DEV theme write em 2 assets; GitHub PR #86 criado e mergeado para production, acionando pipeline/sync do tema; nenhum write direto no Shopify Production via Asset API.
- Riscos/bloqueios: Public storefront ainda alterna entre HTML antigo e novo em algumas requisições, típico de Shopify edge/cache pós-merge. Source/readback está OK; não recomendar rollback só por cache rotativo.
- Rollback/mitigação: Reverter PR #86/merge commit a3231273737694875445d66187dfca9a1e5cb6de para remover o render line e o snippet. Para DEV, restaurar backup /opt/data/profiles/lk-shopify/workdirs/curadoria-alo-runner-20260624/20260624T145133Z_dev_before_assets.json.
- Próximos passos: Monitorar public QA com cache-buster até estabilizar; se algum handle ficar never_ok após propagação, preparar repair focado.
- Onde foi documentado no Brain: Receipt criado via Memory OS writer; approval packet e QA artifacts locais referenciados.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
