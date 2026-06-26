# Receipt — Production merge Curadoria LK PDP Bestsellers 1-3

- Data/hora: 2026-06-25T10:13:06.982886+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK / Shopify
- Responsável humano: Lucas Cimino
- Pedido original: Lucas aprovou: aprovo merge. Executar merge Production do batch Curadoria Bestsellers 1-3 já validado em DEV.
- Classificação: external-write
- Fontes usadas:
- Approval packet areas/lk/sub-areas/shopify/approval-packets/2026-06-24-curadoria-bestsellers-1-3-pdp.md; DEV receipt areas/lk/sub-areas/shopify/receipts/2026-06-25-curadoria-bestsellers-1-3-dev-apply.md; GitHub PR #90; Shopify Admin Asset API readback Production.
- O que foi feito:
- Criado PR GitHub #90 em lk-snkrs/lk-new-theme, merge squash para production; Shopify Production readback confirmou os dois assets com SHA alvo; static QA dos 6 markers passou.
- Output/artefato:
- PR https://github.com/lk-snkrs/lk-new-theme/pull/90; production SHA 348f6c96827f4cafcbe07f967628cc85ea18dd29; readback report /opt/data/profiles/lk-shopify/workdirs/curadoria-bestsellers-1-3-20260624/prod-merge/20260625T100953Z_shopify_production_readback.json; public QA reports com marker ainda ausente no HTML público imediato.
- Aprovação: Lucas: aprovo merge
- Envio/publicação: Nenhum envio externo/campanha.
- Writes externos: GitHub PR/merge para branch production do tema; Shopify Production atualizado pelo fluxo GitHub/sync. Sem direct Asset API Production manual.
- Riscos/bloqueios: Public HTML imediato retornou 200 mas não mostrou os markers novos em 3 rounds + retry; source/readback Production está correto. Classificado como public render/edge/snippet lookup cache não provado, sem rollback automático.
- Rollback/mitigação: Reverter PR #90/commit de merge em GitHub production; isso remove render line e split snippet; depois aguardar sync e confirmar readback Shopify + public QA.
- Próximos passos: Monitorar estabilização pública; se markers continuarem ausentes após janela de cache, preparar repair packet (ex.: inline/hotfix de render lookup) antes de novo write.
- Onde foi documentado no Brain: areas/lk/sub-areas/shopify/receipts/2026-06-25-curadoria-bestsellers-1-3-production-merge.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
