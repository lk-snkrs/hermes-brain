# Auditoria e propagação — CLI/MCP-first para agentes, crons e scripts

Data: 2026-06-27
Status: executado em escopo local/documental/configuração local

## Política ensinada

1. CLI oficial ou wrapper Hermes/Doppler-first primeiro.
2. MCP segundo quando a CLI/wrapper não cobrir melhor o caso ou quando MCP for a superfície governada adequada.
3. API direta/raw apenas como exceção justificada; writes externos exigem aprovação escopada, rollback/readback e verificação.
4. Secrets nunca são impressos; `values_printed=false`.

## Cobertura aplicada

- Profile AGENTS/SOUL revisados/ensinados: 34
- Cron registries atualizados: 7
- Cron prompts atualizados: 50
- Scripts com header de política adicionada: 42
- Arquivo central de scripts criado/atualizado: `/opt/data/scripts/AGENTS.md`
- Backup local: `/opt/data/backups/cli-mcp-all-agents-policy-20260627T105044Z`

## Cron registries atualizados

- `/opt/data/cron/jobs.json:18`
- `/opt/data/profiles/lk-content/cron/jobs.json:4`
- `/opt/data/profiles/lk-growth/cron/jobs.json:11`
- `/opt/data/profiles/lk-ops/cron/jobs.json:3`
- `/opt/data/profiles/lk-stock/cron/jobs.json:4`
- `/opt/data/profiles/lk-trends/cron/jobs.json:1`
- `/opt/data/profiles/mordomo/cron/jobs.json:9`

## Arquivos alterados/criados

- `/opt/data/profiles/brain-process/AGENTS.md`
- `/opt/data/profiles/brain-process/SOUL.md`
- `/opt/data/profiles/hermes-ops-readonly/AGENTS.md`
- `/opt/data/profiles/hermes-ops-readonly/SOUL.md`
- `/opt/data/profiles/lc-claude-cli/AGENTS.md`
- `/opt/data/profiles/lc-claude-cli/SOUL.md`
- `/opt/data/profiles/lk-analyst-readonly/AGENTS.md`
- `/opt/data/profiles/lk-analyst-readonly/SOUL.md`
- `/opt/data/profiles/lk-collection-optimizer/AGENTS.md`
- `/opt/data/profiles/lk-collection-optimizer/SOUL.md`
- `/opt/data/profiles/lk-content/AGENTS.md`
- `/opt/data/profiles/lk-content/SOUL.md`
- `/opt/data/profiles/lk-content-reviewer/AGENTS.md`
- `/opt/data/profiles/lk-content-reviewer/SOUL.md`
- `/opt/data/profiles/lk-finance/AGENTS.md`
- `/opt/data/profiles/lk-finance/SOUL.md`
- `/opt/data/profiles/lk-growth/AGENTS.md`
- `/opt/data/profiles/lk-growth/SOUL.md`
- `/opt/data/profiles/lk-ops/AGENTS.md`
- `/opt/data/profiles/lk-ops/SOUL.md`
- `/opt/data/profiles/lk-shopify/AGENTS.md`
- `/opt/data/profiles/lk-shopify/SOUL.md`
- `/opt/data/profiles/lk-stock/AGENTS.md`
- `/opt/data/profiles/lk-stock/SOUL.md`
- `/opt/data/profiles/lk-trends/AGENTS.md`
- `/opt/data/profiles/lk-trends/SOUL.md`
- `/opt/data/profiles/mordomo/AGENTS.md`
- `/opt/data/profiles/mordomo/SOUL.md`
- `/opt/data/profiles/spiti/AGENTS.md`
- `/opt/data/profiles/spiti/SOUL.md`
- `/opt/data/profiles/spiti-atendimento/AGENTS.md`
- `/opt/data/profiles/spiti-atendimento/SOUL.md`
- `/opt/data/home/.hermes/profiles/lk-collection-optimizer/AGENTS.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/AGENTS.md`
- `/opt/data/profiles/lk-stock/skills/productivity/lk-stock/SKILL.md`
- `/opt/data/scripts/lk_trends_cloudflare_email.py`
- `/opt/data/scripts/honcho_utility_auditor.py`
- `/opt/data/scripts/zipper_supabase_readonly_audit.py`
- `/opt/data/scripts/hermes_doppler.py`
- `/opt/data/scripts/lk_content_klaviyo_webhook_ingest.py`
- `/opt/data/scripts/mordomo_zipperspiti_crm_reports.py`
- `/opt/data/scripts/mordomo_whatsapp_personal.py`
- `/opt/data/scripts/honcho_memory_watchdog.py`
- `/opt/data/scripts/fetch_hermes_docs.py`
- `/opt/data/scripts/hermes_host_docker_observability.py`
- `/opt/data/scripts/honcho_memory_quality_auditor.py`
- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`
- `/opt/data/scripts/fix_artist_pdf_names.py`
- `/opt/data/scripts/honcho_intelligence_layer.py`
- `/opt/data/scripts/zipper_gmail_style_learner.py`
- `/opt/data/scripts/brain_sync_safe.py`
- `/opt/data/scripts/youtube_transcriptapi_fetch.py`
- `/opt/data/scripts/lk_report_external_delivery.py`
- `/opt/data/scripts/probe_artist_pdfs_schema.py`
- `/opt/data/scripts/log_carine_followup_response.py`
- `/opt/data/scripts/lk_crisp_human_reply_learning.py`
- `/opt/data/scripts/lk_valentines_top_customers_preview.py`
- `/opt/data/scripts/log_carine_adriana_send.py`
- `/opt/data/scripts/zipper_gmail_draft_helper.py`
- `/opt/data/scripts/zipper_sales_report_external_delivery.py`
- `/opt/data/scripts/honcho_semantic_contamination_auditor.py`
- `/opt/data/scripts/find_zipper_artist_pdf.py`
- `/opt/data/scripts/hermes_cli_integrations.py`
- `/opt/data/scripts/save_zpr_artist_pdfs.py`
- `/opt/data/scripts/lk_pos_postpurchase_shopify_reconciler.py`
- `/opt/data/scripts/lk_hugo_doppler_upsert_secrets.py`
- `/opt/data/scripts/lk_valentines_evolution_sender.py`
- `/opt/data/scripts/mordomo_email_intake_readonly_probe.py`
- `/opt/data/scripts/send_carine_adriana_email.py`
- `/opt/data/scripts/hermes_daily_intelligence_preflight.py`
- `/opt/data/scripts/lk_store_sale_restock_alert.py`
- `/opt/data/scripts/hermes_memory_os_context_intelligence.py`
- `/opt/data/scripts/lk_pos_postsale_chatwoot_layer.py`
- `/opt/data/scripts/zipper_os_cockpit.py`
- `/opt/data/scripts/lk_hermes_whatsapp_watchdog.sh`
- `/opt/data/scripts/install_honcho_hostinger.sh`
- `/opt/data/scripts/watchdog_claude_proxy.sh`
- `/opt/data/cron/jobs.json`
- `/opt/data/profiles/lk-content/cron/jobs.json`
- `/opt/data/profiles/lk-growth/cron/jobs.json`
- `/opt/data/profiles/lk-ops/cron/jobs.json`
- `/opt/data/profiles/lk-stock/cron/jobs.json`
- `/opt/data/profiles/lk-trends/cron/jobs.json`
- `/opt/data/profiles/mordomo/cron/jobs.json`
- `/opt/data/scripts/AGENTS.md`
- `/opt/data/home/.hermes/profiles/lk-growth/AGENTS.md`

## Não ações

- Não houve restart de runtime/gateway/Docker/VPS.
- Não houve envio externo, API write, WhatsApp, e-mail, Shopify/Tiny/Supabase mutation ou deploy.
- Não houve impressão de secrets.

## Rollback

Restaurar os arquivos a partir de `{backup_root}` e reverter alterações de prompts/headers se necessário.

values_printed=false
