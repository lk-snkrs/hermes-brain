# LK Cart Intent Trackers v2.2 Upgrade

Data: 2026-05-20
Aprovação: Lucas — "Melhorar tudo acima"

## Escopo aplicado

### Shopify tracker v2.2

Tema production: `155065417950`
Asset: `layout/theme.liquid`

Adicionado:

- marker `LK cart intent capture v2.2`;
- `window.__lkGetIdentity()` para debug controlado no console;
- `window.__lkCartIntentDebug.postEvent(...)` para canários internos;
- `event_id` único por evento;
- `lk_visitor_id` e `lk_session_id` first-party;
- captura ampliada de Crisp: session, email, phone, nickname quando disponíveis no browser;
- captura ampliada de Klaviyo: `_kx`, `klaviyo_id`, `__kla_id`, tentativa de parse de cookie para email/phone/first_name quando disponível;
- captura Meta: `_fbp`, `_fbc`, `fbclid`, `event_source_url`;
- captura Google: `_ga`, `gclid`;
- escuta de eventos adicionais de carrinho/theme/app:
  - `cart:updated`
  - `cart:refresh`
  - `cart:change`
  - `ajaxCart:afterCartLoad`
  - `product:added`
  - `theme:cart:change`
  - `cart:drawer:updated`
  - `cart_view` em `/cart`

### n8n workflow

Workflow: `XLODECE4MvNRNCQ9` — `LK - Cart Intent 30min Full Funnel - Crisp (ATIVO)`

Adicionado branch paralelo sem impactar o fluxo de envio:

`LK Cart Intent Webhook → Preparar log cart intent evento → Supabase Log Cart Intent Event`

Branch original preservado:

`LK Cart Intent Webhook → Wait 30 min → Filtrar cart intent elegíveis → Preparar payload Crisp Cart → Crisp Send cart intent → Marcar cart enviado no dedup → Supabase Persist Cart Result`

Readback:

- `active`: true
- `versionId`: `bb0b8bc4-234f-404b-ab06-4fec585588f5`
- `activeVersionId`: `bb0b8bc4-234f-404b-ab06-4fec585588f5`
- `triggerCount`: 1

### Supabase

Tabela criada/verificada:

`public.lk_crm_cart_intent_events`

Finalidade: registrar eventos sanitizados do tracker antes do filtro de elegibilidade.

Campos principais:

- `event_at`
- `event_id`
- `workflow_id`
- `event_name`
- `tracker_version`
- `page/path/referrer`
- `cart_token`
- `item_count`
- flags de identidade: `has_phone`, `has_email`, `has_klaviyo`, `has_meta`, `has_crisp`
- `phone_last4`, `email_domain`
- `payload` sanitizado sem tokens brutos/PII aberta

## Verificação

### HTML live

PDP verificada:

- `LK cart intent capture v2.2`: presente
- `__lkGetIdentity`: presente
- eventos custom de carrinho: presentes
- `sendBeacon`: presente
- marker v1: ausente

Home apresentou cache temporário com marker `v2` no HTML público, apesar de o asset `layout/theme.liquid` no Admin já estar com v2.2. PDP já serve v2.2 e eventos reais v2.2 chegaram ao Supabase. Monitorar dissipação do cache da home.

### n8n

- Workflow ativo e publicado na versão nova.
- Branch de log Supabase adicionada.
- Branch de envio original preservada.

### Supabase

Canário interno sem PII enviado para webhook:

- status webhook: 200 / workflow started;
- evento registrado em `lk_crm_cart_intent_events` com `tracker_version=cart_intent_capture_v2_2`;
- eventos reais v2.2 também já aparecem na tabela.

## Guardrails

- Pixel/Klaviyo anônimo continua sem envio.
- Envio depende de telefone BR direto ou resolvido pelo identity spine.
- Eventos são logados sanitizados antes do filtro.
- Branch de log tem `continueOnFail` para não derrubar o fluxo principal.
- Nenhum envio WhatsApp/customer-facing foi disparado manualmente; apenas canário `product_view` sem carrinho/telefone.

## Limitações / próximo nível

- Não foi adicionado lookup server-side direto no Crisp REST Inbox porque não há credencial REST Crisp dedicada confirmada no Doppler; foi melhorada a captura client-side via `$crisp.get`.
- Klaviyo foi ampliado via `_kx`/`__kla_id`/cookie parse/client-side. Lookup server-side por `_kx` ainda depende de confirmar endpoint/mapeamento confiável no Klaviyo; a API key existe, mas não foi usada para lookup incerto que pudesse gerar falso positivo.

## Rollback

Backup bruto:

`/opt/data/hermes_bruno_ingest/.secrets/lk-cart-intent-trackers-v22-20260520T225107Z`

Contém:

- `theme.liquid.before`
- `theme.liquid.after`
- `theme.liquid.readback`
- `n8n_workflow_before.json`
- `n8n_workflow_after.json`
- JS validado
- `receipt.json`

Rollback Shopify: restaurar `theme.liquid.before`.
Rollback n8n: restaurar `n8n_workflow_before.json` via API.
Supabase: manter tabela é seguro; se necessário, remover branch n8n e deixar tabela órfã sem impacto.
