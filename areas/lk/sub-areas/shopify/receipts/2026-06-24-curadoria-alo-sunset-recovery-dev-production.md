# Receipt — Curadoria LK PDP — Alo Sunset + Recovery DEV + Production merge

- Data/hora: 2026-06-24T15:42:44.186996+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify theme
- Responsável humano: Lucas Cimino
- Pedido original: Adicionar Curadoria LK / Outras variações para Alo Yoga Sunset Sneaker e Alo Yoga Recovery Mode; Lucas aprovou explicitamente DEV e merge Production.
- Classificação: external-write
- Fontes usadas:
- Approval packet areas/lk/sub-areas/shopify/approval-packets/2026-06-24-curadoria-alo-sunset-recovery-pdp.md; QA local /opt/data/profiles/lk-shopify/workdirs/curadoria-alo-next-20260624/20260624T151135Z_static_qa.json; values_printed=false.
- O que foi feito:
- DEV: upload para theme 155065450718 dos assets snippets/lk-variante-top30-visited-v2.liquid e snippets/lk-variante-alo-sunset-recovery-20260624.liquid. Production: PR #87 no GitHub lk-snkrs/lk-new-theme, branch hermes/alo-sunset-recovery-curadoria-20260624 para production, merge commit 5ec3fceb4c3b5497e31ce8c79c1e0ddd1e1c0131.
- Output/artefato:
- DEV readback SHA OK em /opt/data/profiles/lk-shopify/workdirs/curadoria-alo-next-20260624/20260624T154009Z_dev_upload_readback.json. Production Shopify readback OK no theme 155065417950 em /opt/data/profiles/lk-shopify/workdirs/curadoria-alo-next-20260624/20260624T154155Z_production_readback.json. Public QA 3 rounds em 4 PDPs amostrais OK: marker esperado presente, 2 cards, current excluído.
- Aprovação: Lucas escreveu no Telegram: “APROVO: DEV: Aprovo DEV Curadoria Alo Sunset Recovery” e “APROVO: Production: Aprovo merge Production Curadoria Alo Sunset Recovery”.
- Envio/publicação: Resposta no Telegram com mudança, evidência, QA e rollback.
- Writes externos: Shopify Asset API DEV theme write em 2 assets; GitHub PR #87 criado e mergeado para production; nenhum write direto no Shopify Production via Asset API.
- Riscos/bloqueios: Grupos pequenos renderizam 2 cards por PDP. Public QA amostral estabilizou, mas Shopify edge/cache pode variar em outros nós logo após merge.
- Rollback/mitigação: Reverter PR #87/merge commit 5ec3fceb4c3b5497e31ce8c79c1e0ddd1e1c0131 para remover o render line e deletar o snippet. Para DEV, restaurar backup /opt/data/profiles/lk-shopify/workdirs/curadoria-alo-next-20260624/20260624T154009Z_dev_before_assets.json.
- Próximos passos: Monitorar; se algum handle específico ficar never_ok, preparar repair focado. Próxima exploração sugerida deve começar com histórico/source readback para evitar retrabalho.
- Onde foi documentado no Brain: Receipt criado via Memory OS writer; approval packet e QA artifacts referenciados.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
