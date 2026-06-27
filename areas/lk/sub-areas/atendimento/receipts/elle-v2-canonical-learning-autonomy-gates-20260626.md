# Receipt — Elle Brain v2 — canonicalização, regression candidates e gate de autonomia

- Data/hora: 2026-06-26T19:51:24.821825+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK / Atendimento / Elle / Chatwoot WhatsApp
- Responsável humano: Hermes LK Ops
- Pedido original: Lucas aprovou “fazer do 1 ao 4”: reconciliar runtime/fonte canônica, garantir aprendizado→regressão, medir v2 e só expandir autonomia se relatórios confirmarem qualidade.
- Classificação: customer-facing
- Fontes usadas:
- Runtime elle-chatwoot; fonte /opt/elle-chatwoot; Dockerfile; scripts learner/verifier/observer; logs sanitizados; values_printed=false.
- O que foi feito:
- Zerado source_runtime_drift sem recriar container; Dockerfile passou a copiar elle_brain_v2.py; criado exporter de regression candidates; learner wrapper integrado; criado autonomy gate; observer/relatório 07h mostram v2 gate; smokes finais rodados.
- Output/artefato:
- check_drift OK; tests=38 OK; learner ok com v2_lessons_loaded=8 e regression_candidates_total=14; OpenRouter verifier OK processed=9 v2_used=3 v2_skipped=5 v2_errors=0; autonomy_gate=hold por eval_bad=5 e eval_medium_high=1.
- Aprovação: Aprovação explícita no Telegram: “fazer do 1 ao 4”.
- Envio/publicação: Nenhum envio manual a cliente; runtime customer-facing já estava ativo antes; scripts/smokes foram read-only/classify/health.
- Writes externos: customer-facing runtime/source/script changes; 0 Shopify/Tiny/stock writes; sem container recreate para não perder env; values_printed=false.
- Riscos/bloqueios: Autonomy gate em HOLD: não expandir autonomia além do 100% safe-only atual até janela limpa; docker-compose ainda não declara envs, então recriação exige plano/env backup.
- Rollback/mitigação: Backup em /opt/data/backups/elle-v2-canonical-learning-gates/20260626T194417Z; rollback rápido desligando /data/elle_brain_v2_canary.json enabled=false e reiniciando elle-chatwoot; rollback completo restaurando arquivos do backup.
- Próximos passos: Manter v2 100% safe-only, monitorar próximas janelas; só considerar expansão quando v2 autonomy gate sair de hold para go_review_only e revisão humana confirmar qualidade.
- Onde foi documentado no Brain: Report: areas/lk/sub-areas/atendimento/reports/elle-brain-v2/elle-v2-canonical-learning-autonomy-gates-20260626.md; receipt atual; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
