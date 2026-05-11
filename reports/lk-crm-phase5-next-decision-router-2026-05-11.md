# LK CRM Phase 5 Next Decision Router, read-only

Generated at: `2026-05-11T20:48:21.031156+00:00`

## Veredito

Fase 5 está consolidada como pendente seguro: P1 Klaviyo fica em Draft, WhatsApp P1 não deve ser repetido automaticamente, e o próximo avanço seguro é P2 preview ou refresh read-only de Data Spine/RFM.

## Resumo

- Opções de decisão: 4
- Execuções externas liberadas agora: 0
- Opções read-only liberadas agora: 1

## Decision router

### crm_phase5_p1_klaviyo_draft

- Título: P1 Klaviyo loja física, manter draft até revisão final
- Status: `needs_manual_ui_verification_before_send`
- Próximo passo seguro: Confirmar no painel Klaviyo que o template aprovado está selecionado no campaign message; depois pedir aprovação explícita para enviar/agendar ou manter pausado.
- Execução liberada agora: `False`
- Decisões aceitas: keep_draft, verify_ui_only, approve_send_later_with_final_checklist, pause_or_archive
- Bloqueios: ui_template_selection_unverified, lucas_final_send_approval_missing
- Source labels: manual_approval, platform_signal

### crm_phase5_p1_whatsapp_concierge_status

- Título: P1 WhatsApp concierge, pós-execução e bloqueio de repetição
- Status: `executed_partial_prior_approval_context`
- Próximo passo seguro: Não reenviar automaticamente. Usar auditoria privada para evitar duplicidade; se avançar, preparar somente follow-up preview com dedupe e validação de número.
- Execução liberada agora: `False`
- Decisões aceitas: hold_no_followup, prepare_followup_preview_only, prepare_failure_resolution_preview
- Bloqueios: new_lucas_approval_for_any_followup, dedupe_against_private_audit, validate_failed_number_before_retry
- Source labels: manual_approval

### crm_phase5_p2_or_reactivation_preview

- Título: Preparar P2 ou reativação fria como preview, não campanha
- Status: `needs_preview_from_rfm_queue`
- Próximo passo seguro: Gerar P2 read-only a partir do RFM/local SQL, com Tiny stock gate e copy preview. Não reutilizar automaticamente a fila P1.
- Execução liberada agora: `False`
- Decisões aceitas: prepare_p2_preview_only, prepare_reactivation_preview_only, defer_p2
- Bloqueios: fresh_p2_segment_preview, tiny_stock_gate, lucas_approval_before_any_list_campaign_or_send
- Source labels: fact_shopify, fact_tiny_stock, derived_reconciliation

### crm_phase5_return_to_data_spine_option

- Título: Voltar para Fase 1 Data Spine, auditoria de base antes de CRM P2
- Status: `safe_readonly_option`
- Próximo passo seguro: Se Lucas preferir reduzir risco antes de P2, atualizar snapshot read-only de Data Spine/RFM e freshness sem campanha ou envio.
- Execução liberada agora: `True`
- Decisões aceitas: refresh_data_spine_readonly, defer_data_spine
- Bloqueios: nenhum para análise read-only
- Source labels: fact_shopify, fact_tiny_stock, fact_ga4, platform_signal

## Bloqueios globais

- No Klaviyo send/schedule without final Lucas approval and UI template verification.
- No WhatsApp follow-up without fresh approval, dedupe and number validation.
- No P2 campaign/list creation before read-only preview and Tiny stock gate.
- No deep Klaviyo UI link unless verified in logged-in panel.

## O que não foi feito

- klaviyo_send
- klaviyo_schedule
- klaviyo_list_or_campaign_create
- whatsapp_send
- email_send
- sms_send
- customer_tag_or_note
- shopify_write
- tiny_write
- supabase_write
- production_db_write
- cron_creation
- live_api_call
