# Receipt — Chatwoot order_created 132018 hotfix — lista de produtos em linha única

- Data/hora: 2026-06-24T20:19:35.199131+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Atendimento / Chatwoot lifecycle
- Responsável humano: Lucas Cimino
- Pedido original: Lucas respondeu 'Corrigir' ao alerta do lifecycle exception monitor com falhas order_created template_parameter_issue_132018.
- Classificação: infra-sensitive
- Fontes usadas:
- Monitor lifecycle 20260624T200415Z; Rails read-only dos failed messages; código runtime Chatwoot; smoke sem envio; monitor reexecutado.
- O que foi feito:
- Identificado padrão: lk_online_pedido_realizado_v1 falhava com Meta 132018 quando BODY {{3}} recebia lista de produtos multi-linha/longa. Corrigido Shopify::OrderNotificationService#product_list para gerar resumo single-line, até 2 itens + marcador de itens extras, limite 140 chars. Patch aplicado em source local e nos containers chatwoot-rails-1/chatwoot-sidekiq-1; containers reiniciados. Monitor ajustado para tratar falhas 132018 anteriores ao cutoff desta correção como contexto, alertando apenas reaparecimento após cutoff.
- Output/artefato:
- Ruby syntax OK nos dois containers; smoke Rails sem envio: newline_count=0, under_limit=true, extra_marker=true; monitor --print: Status ok; cron normal stdout bytes=0; Rails HTTP interno 200; Rails runner OK; query pós-cutoff: order_created_132018_failures_after_fix=0; values_printed=false.
- Aprovação: Aprovação explícita em Telegram: Lucas pediu 'Corrigir'.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: Sem WhatsApp/manual send, sem Shopify/Tiny/Meta write. Writes locais/infra: arquivos Ruby em Chatwoot source local e containers, restart de chatwoot-rails-1/chatwoot-sidekiq-1, monitor local/Brain.
- Riscos/bloqueios: Mudança em Chatwoot produção; mitigada com backups, syntax check, smoke sem envio, restart limitado a rails/sidekiq e monitor silencioso OK.
- Rollback/mitigação: Backups em /opt/data/backups/chatwoot-lifecycle/20260624T201425Z-order-created-132018-product-list/. Para rollback: restaurar order_notification_service.rails.rb.bak e .sidekiq.rb.bak via docker cp, restaurar source se necessário, e docker restart chatwoot-rails-1 chatwoot-sidekiq-1. Reverter monitor script se necessário.
- Próximos passos: Monitorar próximo order_created com 3+ itens: deve evitar 132018. Se 132018 reaparecer após cutoff 2026-06-24T20:14:25Z, monitor volta a alertar.
- Onde foi documentado no Brain: Sim, receipt Brain e reports lifecycle gerados em /opt/data/profiles/lk-ops/cron/output/lk-chatwoot-lifecycle-exception-monitor/.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
