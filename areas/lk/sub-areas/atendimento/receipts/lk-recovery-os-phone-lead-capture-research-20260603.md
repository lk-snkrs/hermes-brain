# LK Recovery OS — pesquisa para aumentar match de telefone/leads

Data: 2026-06-03 BRT
Escopo: pesquisa read-only e recomendações operacionais; sem alteração em Shopify/Klaviyo/Worker/DB.

## Pergunta
Como aumentar a chance de identificar telefone/leads de visitantes não logados, incluindo quem colocou produto no carrinho mas não preencheu checkout/e-mail.

## Fontes consultadas
- Klaviyo — custom ecommerce integration / events: https://help.klaviyo.com/hc/en-us/articles/115005082927
- Klaviyo — tracking cookies / __kla_id / Extended ID / Shopify-branded onsite tracking: https://help.klaviyo.com/hc/en-us/articles/360034666712
- Klaviyo — web tracking / Active on Site / Viewed Product: https://help.klaviyo.com/hc/en-us/articles/115005076767-Klaviyo-Web-Tracking
- Klaviyo — Shopify onsite tracking app embed / Added to Cart: https://help.klaviyo.com/hc/en-us/articles/4425956184731
- Klaviyo Client Event API: https://developers.klaviyo.com/en/reference/create_client_event
- Shopify Web Pixels standard events: https://shopify.dev/docs/api/web-pixels-api/standard-events
- Shopify Customer Privacy API: https://shopify.dev/docs/api/customer-privacy

## Achados
- Klaviyo `__kla_id` identifica visitantes quando eles já preencheram form Klaviyo ou clicaram link de email/SMS Klaviyo; `_kx` em links ajuda associação de sessão.
- Klaviyo Extended ID pode reidentificar por identificadores first-party por até 1 ano, mas requer atenção/consentimento e perfil Klaviyo pré-existente.
- Shopify/Klaviyo onsite tracking captura Active on Site, Viewed Product, Viewed Collection, Submitted Search e Added to Cart; Added to Cart/Shopify pixel identifica perfis quando visitante envia form Klaviyo/Shopify, entra checkout, loga na loja/Shop account etc.
- Shopify Web Pixels expõe eventos úteis antes do checkout: `product_added_to_cart`, `cart_viewed`, `product_viewed`, `checkout_started`, `checkout_contact_info_submitted`.
- Shopify Customer Privacy API deve governar analytics/marketing consent; Shopify adverte não ler/modificar cookies Shopify diretamente e não registrar consentimento automaticamente.
- Klaviyo client-side events não devem atualizar identificadores sensíveis; atualização de identificadores de perfil deve ser server-side/private API.

## Recomendações
1. Otimizar captura determinística já permitida:
   - garantir Klaviyo app embed + behavioral events Shopify ativos;
   - capturar e persistir `__kla_id`, `_kx`, cart token, product_added_to_cart/cart_viewed/viewed_product/search;
   - habilitar/validar Extended ID apenas com consentimento/privacy copy.
2. Aumentar pontos de identificação antes do checkout:
   - pop-up/embedded Klaviyo com email + telefone/WhatsApp opcional e consentimento;
   - CTA WhatsApp/“consultar tamanho no WhatsApp” com produto/cart token;
   - back-in-stock/avise-me com telefone;
   - oferta pequena/benefício para identificar antes de checkout.
3. Enriquecimento server-side:
   - se email existir, buscar telefone em Klaviyo Profile API e Shopify Customer/order history;
   - se Klaviyo profile id existir, buscar perfil Klaviyo para telefone/email, respeitando consentimento;
   - se só cookie/cart sem perfil, não inventar identidade; esperar reidentificação ou pedir lead.
4. Evitar fingerprinting/probabilístico agressivo sem revisão legal/consentimento.

## Status
Pesquisa entregue ao Lucas; nenhuma mudança executada em produção.
