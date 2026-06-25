# Receipt — Hermes Webhooks Shopify route secret alignment aplicado

- Data/hora: 2026-06-24T23:47:19.643759+00:00
- Agente/profile/cron: default
- Empresa/área: operacoes/hermes-webhooks
- Responsável humano: Hermes default
- Pedido original: Lucas aprovou alinhar lk-shopify-pos-restock para HERMES_WEBHOOK_SECRET, reiniciar/verificar gateway default e repetir probe Shopify no-op, sem writes em Shopify/Vercel/providers.
- Classificação: infra-sensitive
- Fontes usadas:
- /opt/data/config.yaml; /opt/data/hermes-webhooks/api/webhooks/[route].js; /opt/data/tmp/hermes_webhooks_signed_noop_probes.py; gateway log local; Doppler lc-keys/prd presence via runtime helper
- O que foi feito:
- Backup de config/runtime; patch da rota lk-shopify-pos-restock para secret_doppler HERMES_WEBHOOK_SECRET; hardening local do adaptador instalado para route secret_doppler e run_script; restart/verificação do gateway default; probe Shopify no-op assinado via Vercel.
- Output/artefato:
- Probe Shopify no-op retornou HTTP 200 status ignored reason not_paid_active_pos_order topic orders/paid; webhook/API health OK; fila POS sem jobs de probe; values_printed=false.
- Aprovação: Aprovado por Lucas no Telegram em 2026-06-24: patch config, restart/verificação gateway default e probe no-op; sem Vercel/Shopify/Doppler writes.
- Envio/publicação: Nenhum envio externo; no-op ignored.
- Writes externos: 0
- Riscos/bloqueios: Rota infra sensível; houve drift entre fonte Hermes e venv instalado, corrigido localmente com backup e py_compile.
- Rollback/mitigação: Restaurar config.yaml.before e site-webhook.py.before/hermes-bin.before dos backups criados; reiniciar gateway default; validar health e probe no-op.
- Próximos passos: Em ciclo de manutenção, reconciliar patch local do venv com pacote/source Hermes para evitar drift em upgrade.
- Onde foi documentado no Brain: /opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/reports/hermes-webhooks-shopify-route-secret-alignment-20260624-final.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
