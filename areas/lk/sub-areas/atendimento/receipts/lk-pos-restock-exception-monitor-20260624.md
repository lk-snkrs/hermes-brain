# Receipt — LK POS restock exception monitor — alerta quando automação fica muda

- Data/hora: 2026-06-24T20:31:52.317724+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Atendimento / POS restock
- Responsável humano: Lucas Cimino
- Pedido original: Lucas apontou falha drástica: automação de venda loja física -> reposição/recompra parou e Hermes não percebeu.
- Classificação: infra-sensitive
- Fontes usadas:
- Shopify Admin read-only via Doppler; state local lk_store_sale_restock; gateway health/noop; Brain receipts anteriores; sem estoque/Tiny.
- O que foi feito:
- Criado watchdog /opt/data/profiles/lk-ops/scripts/lk_pos_restock_exception_monitor.py e job cron lk-pos-restock-exception-monitor a cada 30min. O monitor compara POS pagos recentes no Shopify com last_webhook_at do handler local e valida health/noop da rota. Silent-OK quando saudável; alerta Telegram/origin quando houver POS pago sem handler avançar.
- Output/artefato:
- Execução manual detectou 6 POS pagos em 72h; último POS 2026-06-24 13:34 BRT; último handler 2026-06-22 05:18 BRT; gateway health=200; noop local=200; status atenção. Cron registrado em jobs.json com deliver=origin. values_printed=false.
- Aprovação: Aprovado por Lucas no Telegram/voz em 2026-06-24 como correção de erro claro: corrigir a falha drástica de observabilidade da automação POS restock. Escopo executado: writes locais de monitor/cron/Brain somente; sem envio externo e sem alteração Shopify/Tiny/Meta/Vercel.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: Nenhum envio WhatsApp; nenhum write Shopify/Tiny/Meta/Vercel. Writes locais/infra: script monitor, cron jobs.json, reports Brain/local.
- Riscos/bloqueios: Pode alertar a cada 30min enquanto o fluxo estiver realmente quebrado; isso é intencional até corrigir Vercel/proxy ou rota Shopify. Sem PII/secrets.
- Rollback/mitigação: Restaurar /opt/data/backups/lk-ops-cron/jobs-20260624T202534Z-pos-restock-exception-monitor.json para /opt/data/profiles/lk-ops/cron/jobs.json e remover/pausar o script se necessário.
- Próximos passos: Aprovação necessária para write externo: redeploy do Vercel hermes-webhooks ou troca do webhook Shopify para upstream direto. Sem isso, monitor continuará alertando o descompasso.
- Onde foi documentado no Brain: Sim, receipt Brain, monitor Brain em areas/lk/sub-areas/atendimento/monitoring/pos-restock/ e skill lk-shopify-readonly atualizada.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
