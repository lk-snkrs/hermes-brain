# LK Phase 5 P1, WhatsApp Evolution send log, 2026-05-11

## Veredito

Mensagens enviadas via Evolution.

## Modo

- EXECUTE_SEND

## Contagens

- input_rows: 7
- deduped_phone_recipients: 7
- sent: 6
- failed: 1
- dry_run_not_sent: 0

## Falha diagnosticada

- 1 destinatário falhou com HTTP 400.
- Validação posterior no Evolution indicou `exists=false` para o número no WhatsApp.
- Não fiz retry automático para evitar loop/envio errado.
- O detalhe com `customer_ref` fica apenas no audit privado; sem telefone/nome no Brain.

## Arquivo privado de auditoria

- `/opt/data/hermes_bruno_ingest/private_exports/lk_crm/lk_phase5_p1_whatsapp_evolution_audit_2026-05-11.csv`

## Guardrails

- Uses approved physical-store-only WhatsApp file
- Dedupes by normalized phone before sending
- No phone numbers, names, or message bodies in Brain report
- Does not touch Klaviyo/Shopify/Tiny/Supabase
