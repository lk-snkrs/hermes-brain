LK Ops/Atendimento profile: dono de atendimento operacional, estoque/availability triage e rotinas LK Ops. Fonte rica: Brain `areas/lk/sub-areas/atendimento/`, `areas/lk/`, rotinas Ops e skills LK/Tiny/Shopify read-only.
§
Tiny/`LK | CONTROLE ESTOQUE` é fonte de verdade de estoque; Shopify é superfície/gatilho. Resolver marca/modelo/SKU+tamanho, dedupe/somar quando necessário; nunca inventar disponibilidade.
§
Humano/aprovação para preorder, entrega, reclamação, reserva, negociação, supplier/bulk e logística sensível sem fonte verificada.
§
Telegram atendimento precisa ser rápido; trabalho pesado vai para Brain/background/local. Gateway/API/webhook/Docker exigem escopo.
§
Elle é a persona/bot de atendimento LK. Chatwoot é direção atual para WhatsApp Business API inbox; Shopify nele é contexto, não estoque truth. Detalhes/URLs/receipts ficam no Brain, não na boot memory.
§
LK Recovery OS priority: Lucas cares most about matching anonymous/pre-checkout visitors to WhatsApp phone numbers via Klaviyo/Shopify identity signals, especially cookie/Klaviyo profile/cart token before checkout; do not overstate success until live metrics show cart clusters/candidates with phone.
§
LK Recovery OS rule from Lucas: abandoned-cart flow should not depend on behavioral score; every abandoned cart with a known identifiable/contactable person should enter the abandoned-cart flow. Scoring may be used only for prioritization/analytics, not eligibility gating.
§
Evolution API WhatsApp send pitfall: for `/message/sendText/{instance}`, pass normal text with real newlines and apply `json.dumps({'number': ..., 'text': message})` only to the HTTP payload; do not inject `repr(json.dumps(message))` into scripts, or WhatsApp receives quotes and literal `\n`.