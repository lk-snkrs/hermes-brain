# Receipt — Inventory Hub upstream Stock OS sync endpoint corrigido e deployado

- Data/hora: 2026-07-01T16:11:49.476744+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK/stock/inventory-hub
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas pediu: CORRIGIR corrigir/deployar o endpoint/fonte Hub upstream.
- Classificação: external-write
- Fontes usadas:
- Repo inventory-hub, Vercel deploy/readback, live hub.lksnk.dev, cronjob c45da7bb0fcb, Supabase sync dry-run/readback.
- O que foi feito:
- Deploy Vercel production do inventory-hub; adicionado domínio hub.lksnk.dev ao project correto; adicionadas envs Production necessárias de Supabase/Stock OS auth; endpoint interno validado com 8550 rows, MR530SG 98 rows/26 units, U204LMMC-6 qty 2.
- Output/artefato:
- Relatório: areas/lk/sub-areas/stock/reports/lk-inventory-hub-upstream-sync-endpoint-fix-deploy-20260701.md
- Aprovação: Aprovação explícita no Telegram: CORRIGIR corrigir/deployar o endpoint/fonte Hub upstream.
- Envio/publicação: Sem envio externo/customer-facing; somente Vercel prod/env/domain writes e readbacks.
- Writes externos: Vercel production deploy, Vercel env production add, Vercel domain assignment hub.lksnk.dev.
- Riscos/bloqueios: Vercel project anterior estava inacessível/deletado/transferido pela CLI; domínio foi atribuído ao project inventory-hub acessível. Rollback exige promover deploy anterior ou reatribuir/remover domínio/envs.
- Rollback/mitigação: Remover/reatribuir hub.lksnk.dev no Vercel, promover deployment anterior, remover envs adicionadas se necessário.
- Próximos passos: Monitorar próximo tick horário do cron Supabase; se necessário, auditar DNS ipStatus required-change separadamente sem bloquear porque domínio está misconfigured=false e live 200.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/reports/lk-inventory-hub-upstream-sync-endpoint-fix-deploy-20260701.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
