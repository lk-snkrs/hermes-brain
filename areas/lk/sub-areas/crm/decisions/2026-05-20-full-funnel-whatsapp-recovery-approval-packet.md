# LK — Approval packet: recuperação full-funnel por WhatsApp

Data UTC: 2026-05-20
Agente: Hermes LK Growth

## Contexto

Lucas sinalizou que a LK deve recuperar não só checkout abandonado, mas também carrinho/intenção ampla, com maior volume de mensagens. O fluxo ativo atual cobre apenas Shopify `abandonedCheckouts` com telefone válido e não captura todo add-to-cart/intenção.

## Decisão proposta

Construir uma arquitetura full-funnel em camadas:

1. Checkout abandonado com telefone — manter e endurecer o fluxo atual.
2. Carrinho/intenção ampla — capturar eventos de produto/carrinho/begin checkout em Supabase, inicialmente log-only.
3. Identity resolution — mapear sessão/email/customer/Crisp para telefone confiável.
4. Régua WhatsApp — disparar apenas quando houver telefone confiável, abandono validado, dedup e cap.

## Guardrail comercial

Apesar da necessidade de volume, não fazer blast indiscriminado. WhatsApp é customer-facing e tem risco de bloqueio, reclamação, queda de qualidade do número e perda de entregabilidade. A régua deve ser agressiva em cobertura, mas controlada em elegibilidade.

## Fase 0 — Imediata / sem envio

- Inventariar fontes disponíveis: Shopify Customer Events, tema Shopify, Crisp session data, Klaviyo/Shopify customer data, n8n workflows antigos.
- Criar tabelas Supabase para eventos e identidade.
- Capturar eventos `product_view`, `add_to_cart`, `cart_update`, `begin_checkout`, `checkout_created`.
- Não enviar mensagem ainda.
- Medir por 24h: volume total, identificados por email, identificados por telefone, recuperáveis por WhatsApp, compradores antes do envio.

Risco: baixo.
Aprovação necessária: nenhuma para auditoria/read-only; sim para inserir script/eventos no tema production.

## Fase 1 — WhatsApp controlado

- Enviar T1 apenas para eventos com telefone confiável.
- Rechecar compra antes do envio.
- Cap inicial: 1 sequência ativa por telefone por 96h.
- Registrar Crisp `request_id`, callback, status, opt-out e falhas.
- Kill switch n8n + Supabase flag.

Aprovação necessária: explícita de Lucas antes de qualquer envio real.

## Fase 2 — Escala

- Relaxar critérios com base em dados reais: valor mínimo, categorias, sessões repetidas, produto premium, recorrência de interesse.
- Criar filas por prioridade.
- Medir receita recuperada, reclamação, bloqueios, opt-outs e conversão.

## Riscos

- Envio excessivo pode afetar qualidade WhatsApp/Meta.
- Captura de intenção sem telefone não permite WhatsApp direto.
- Mensagens de recuperação são Marketing, não Utility.
- Ativar workflows antigos inativos é arriscado: placeholders, Meta direto, sem Supabase/callback.

## Recomendação

Não ativar workflows antigos. Criar fluxo novo com observabilidade primeiro e disparo controlado depois.

## Aprovação necessária para writes/customer-facing

- Inserir script/evento no tema production.
- Criar/alterar workflow n8n ativo.
- Enviar mensagens reais.
- Criar cupons/descontos.
- Alterar templates Meta/Crisp.
