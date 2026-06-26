# TOOLS — LK CRM

## Fontes e sistemas

- Shopify LK: pedidos, clientes, produtos e histórico comercial em modo read-only salvo aprovação.
- Tiny: estoque e dados operacionais quando a mensagem depende de disponibilidade.
- Supabase/CRM autorizado: segmentações e data spine quando disponível.
- Klaviyo: campanhas, listas, templates e métricas; writes/envios só com aprovação.
- Crisp/Hugo/WhatsApp: atendimento e templates; contato externo só com aprovação.
- Brain: playbooks, decisions, receipts, lessons e guardrails.

## Skills relacionadas

- `crisp-customer-chat-automation` quando envolver Crisp/Hugo.
- `lk-shopify-readonly` quando dados Shopify forem necessários.
- `google-workspace` apenas quando houver documento/planilha autorizada.

## Secrets

Credenciais vivem no Doppler `lc-keys/prd` ou local seguro aprovado. Documentar nomes, nunca valores.
