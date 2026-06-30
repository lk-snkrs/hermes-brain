# MAPA — LK Ops

Subárea operacional para receipts, backups e evidências do profile `lk-ops`.

## Escopo

- atendimento e operação LK;
- chat/WhatsApp/Klaviyo-safe conforme aprovação;
- handoffs para LK Stock, LK Shopify, LK Growth e Mordomo;
- artefatos de Skill Surface Diet e runtime validation do profile `lk-ops`.

## Guardrails

- Sem writes externos, envios, Klaviyo/WhatsApp/Shopify/Tiny/Supabase, Docker/VPS/Traefik/Main ou secrets sem aprovação escopada, rollback e readback.
- Receipts operacionais devem usar `/opt/data/scripts/hermes_memory_os_receipt_writer.py`.
