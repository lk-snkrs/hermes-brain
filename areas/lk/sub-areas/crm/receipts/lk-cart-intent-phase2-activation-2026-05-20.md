# LK — Cart Intent Phase 2 Tracking Activation

Data UTC: 2026-05-20T21:22:03.755010+00:00
Agente: Hermes LK Growth

## Aprovação

Lucas aprovou explicitamente: `Aprovo fase 2 agora`.

## O que foi ativado

### Shopify tracker v2

- Theme: `lk-new-theme/production` / ID `155065417950`
- Asset: `layout/theme.liquid`
- Marcador ativo: `LK cart intent capture v2`
- Endpoint preservado: `https://n8n.lucascimino.com/webhook/lk-cart-intent-v1`

Novos sinais capturados:

- Crisp: website/session identifier quando disponível no browser.
- Klaviyo: `_kx`/`kx`, `klaviyo_id`, cookie `__kla_id` e presença onsite.
- Meta/Instagram: `_fbp`, `_fbc`, `fbclid`.
- Google/Ads: `_ga`, `gclid`.
- UTM/landing/referrer.
- Product context em PDP.
- Eventos adicionais: `product_view` e `begin_checkout`, além de `add_to_cart` e `cart_update`.

### n8n workflow enriquecido

- Workflow: `XLODECE4MvNRNCQ9` / `LK - Cart Intent 30min Full Funnel - Crisp (ATIVO)`
- Status no readback: `active=True`
- Versão workflow: `7c40333c-5a8e-43c2-845f-9a7a369420b9`

Mudanças:

- `Filtrar cart intent elegíveis` agora lê `identities` e `attribution`.
- Registra `intentLog` no staticData do workflow para eventos capturados e skipped.
- Mantém envio WhatsApp apenas se houver telefone BR válido, carrinho com itens e dedup/frequency gate passar.
- Eventos como `product_view` ficam como captura/inteligência, sem disparo automático.

## Guardrails preservados

- Sem blast histórico.
- Sem envio por Pixel/Meta quando não há telefone.
- Sem enviar WhatsApp para visitante anônimo.
- Dedup por carrinho + identidade.
- Template e Crisp path existentes preservados.

## Rollback

- Theme: restaurar `/opt/data/hermes_bruno_ingest/.secrets/lk-cart-intent-phase2-20260520T212201Z/theme.liquid.before`.
- n8n: restaurar `/opt/data/hermes_bruno_ingest/.secrets/lk-cart-intent-phase2-20260520T212201Z/n8n_workflow_before.json`.
- Pausa emergencial: desativar `XLODECE4MvNRNCQ9` ou setar `cartTemplateApproved=false`.

## Backup privado

Artefatos com workflow/theme raw ficam fora do Brain em:

`/opt/data/hermes_bruno_ingest/.secrets/lk-cart-intent-phase2-20260520T212201Z`
