# LK OS, Pareto-compatible vs Lucas-operational Split read-only, 2026-05-11

Generated at: `2026-05-11T20:24:13.686800+00:00`

## Veredito operacional

A Fase 3 agora tem a fronteira formal entre o que é compatível com Pareto/Meta e o que pode orientar decisão operacional de Lucas. Pareto-compatible mantém a linguagem de plataforma; Lucas-operational só avança quando há ponte Shopify/Tiny ou identidade confirmada.

## Resumo

- Linhas Pareto-compatible: 11
- Linhas Lucas-operational: 14
- Linhas que podem virar análise operacional interna agora: 2
- Linhas que seguem platform_signal/investigação: 13

## Regras fixadas

### Pareto-compatible

- Match influencer primarily by Meta ad_name using Maicon rule.
- Sum all ad_id rows under the same normalized influencer.
- Keep Maria, Maria Fernanda and Mariah separated.
- Numbers remain platform_signal and are compatible with Pareto/Meta dashboard language.

### Lucas-operational

- Do not decide product, stock, budget, coupon or creative from campaign/adset generic names.
- Require Shopify/Tiny bridge for product/SKU/size consequences.
- Silvia/Helena have usable bridge for internal analysis; Lala remains investigation in this recorte.
- Even when usable, execution still requires explicit approval for campaign/coupon/send/write.

## Linhas principais

### Silvia
- Status identidade: `validated_needs_official_handle_coupon_registry`
- Bridge: `strong`
- Pareto-compatible spend: R$ 10.829,11; compras: 38.0; valor: R$ 144.971,35
- Lucas-operational spend: n/d; compras: n/d; valor: n/d
- Decisão operacional permitida agora: `True`
- Limite: may_prepare internal product/stock analysis only, still no campaign/coupon/send/write without approval

### Helena
- Status identidade: `mapped_needs_official_registry_and_ad_id_bridge`
- Bridge: `partial`
- Pareto-compatible spend: R$ 3.952,76; compras: 32.0; valor: R$ 107.414,76
- Lucas-operational spend: n/d; compras: n/d; valor: n/d
- Decisão operacional permitida agora: `True`
- Limite: may_prepare internal product/stock analysis only, still no campaign/coupon/send/write without approval

### Lala Noleto
- Status identidade: `investigation_required_before_operational_use`
- Bridge: `none_found_in_recorte`
- Pareto-compatible spend: R$ 7.155,62; compras: 55.0; valor: R$ 166.660,76
- Lucas-operational spend: R$ 7.155,62; compras: 55.0; valor: R$ 166.660,76
- Decisão operacional permitida agora: `False`
- Limite: do not use for stock/campaign/budget decision until Shopify/Tiny bridge or official registry is confirmed

### Maria
- Status identidade: `not_in_identity_bridge`
- Bridge: `not_evaluated_in_current_identity_bridge_keep_separate`
- Pareto-compatible spend: R$ 907,85; compras: 2.0; valor: R$ 741,54
- Lucas-operational spend: R$ 907,85; compras: 2.0; valor: R$ 741,54
- Decisão operacional permitida agora: `False`
- Limite: do not use for stock/campaign/budget decision until Shopify/Tiny bridge or official registry is confirmed

### Maria Fernanda
- Status identidade: `not_in_identity_bridge`
- Bridge: `not_evaluated_in_current_identity_bridge_keep_separate`
- Pareto-compatible spend: R$ 224,07; compras: 0.0; valor: R$ 0,00
- Lucas-operational spend: R$ 224,07; compras: 0.0; valor: R$ 0,00
- Decisão operacional permitida agora: `False`
- Limite: do not use for stock/campaign/budget decision until Shopify/Tiny bridge or official registry is confirmed

### Mariah
- Status identidade: `not_in_identity_bridge`
- Bridge: `not_evaluated_in_current_identity_bridge_keep_separate`
- Pareto-compatible spend: R$ 193,18; compras: 0.0; valor: R$ 0,00
- Lucas-operational spend: R$ 193,18; compras: 0.0; valor: R$ 0,00
- Decisão operacional permitida agora: `False`
- Limite: do not use for stock/campaign/budget decision until Shopify/Tiny bridge or official registry is confirmed

## O que não foi feito

- Nenhuma chamada live a Meta, Shopify, GA4, Metricool, Klaviyo ou Tiny.
- Nenhuma campanha, orçamento, criativo, cupom, UTM, Shopify/Tiny, cliente, estoque, preço, banco de produção ou cron foi alterado.
- Nenhum envio externo foi feito.

## Próximo passo seguro

Usar esta fronteira no e-mail semanal interno: uma seção Pareto-compatible para conferência de mídia e uma seção Lucas-operational para decisões que exigem ponte Shopify/Tiny. O e-mail deve ser preview-only até aprovação e sem jargão de dashboard.
