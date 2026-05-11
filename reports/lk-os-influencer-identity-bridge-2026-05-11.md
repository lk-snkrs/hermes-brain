# LK OS Influencer Identity Bridge, read-only

Generated at: `2026-05-11T20:18:19.657678+00:00`

## Veredito operacional

O próximo bloco seguro da Fase 3 foi separar identidade oficial de influencer, cupom, handle, ad_id e UTM da evidência de plataforma. O relatório não cria cupom, não mexe em campanha e não transforma ROAS de Meta em venda operacional.

## Resumo

- Influencers roteados: 3
- Alta confiança Shopify/Tiny: 1
- Média confiança: 1
- Baixa confiança/investigação: 1
- Receita Shopify com ponte direta nas matrizes: R$ 463.078,29
- Pedidos Shopify casados: 131

## Fila de identidade e ponte

### Silvia Heinz
- Status: `validated_needs_official_handle_coupon_registry`
- Confiança: `high`
- Handle oficial: `missing_pending_lucas_or_agency_confirmation`
- Cupons oficiais: `missing_pending_lucas_or_agency_confirmation`
- Pedidos Shopify casados: 117
- Receita Shopify: R$ 429.291,45
- Evidência Shopify: discount_code: 146, landing_site: 2
- Consequência estoque/Tiny: ruptura agora: 86, sem SKU no Shopify: 23, baixo estoque: 6, ok/monitorar: 1, mapear SKU no Tiny: 6
- Falta para operacionalizar: official_coupon_codes_or_confirmed_no_coupon, ad_id_or_utm_content_per_creative
- Próximo passo seguro: `collect_official_handle_coupon_ad_id_registry_preview_only`

### Helena Lunardelli
- Status: `mapped_needs_official_registry_and_ad_id_bridge`
- Confiança: `medium`
- Handle oficial: `missing_pending_lucas_or_agency_confirmation`
- Cupons oficiais: `missing_pending_lucas_or_agency_confirmation`
- Pedidos Shopify casados: 14
- Receita Shopify: R$ 33.786,84
- Evidência Shopify: note_attributes: 10, landing_site: 6, discount_code: 2
- Consequência estoque/Tiny: sem SKU no Shopify: 2, ok/monitorar: 1, ruptura agora: 11, mapear SKU no Tiny: 2
- Falta para operacionalizar: official_coupon_codes_or_confirmed_no_coupon, ad_id_or_utm_content_per_creative
- Próximo passo seguro: `collect_official_handle_coupon_ad_id_registry_preview_only`

### Lala Noleto
- Status: `investigation_required_before_operational_use`
- Confiança: `low`
- Handle oficial: `missing_pending_lucas_or_agency_confirmation`
- Cupons oficiais: `missing_pending_lucas_or_agency_confirmation`
- Pedidos Shopify casados: 0
- Receita Shopify: R$ 0,00
- Evidência Shopify: n/d
- Consequência estoque/Tiny: n/d
- Falta para operacionalizar: official_coupon_codes_or_confirmed_no_coupon, ad_id_or_utm_content_per_creative, shopify_bridge_evidence
- Próximo passo seguro: `investigate_real_bridge_before_stock_campaign_decision`

## Template de cadastro oficial, preview-only

Preencher depois com Lucas/Pareto/LK, sem criar cupom nem alterar campanha automaticamente:

- Silvia Heinz: handle oficial, cupons oficiais, utm_content, ad_ids, temas de produto, janela comercial, owner e status.
- Helena Lunardelli: handle oficial, cupons oficiais, utm_content, ad_ids, temas de produto, janela comercial, owner e status.
- Lala Noleto: handle oficial, cupons oficiais, utm_content, ad_ids, temas de produto, janela comercial, owner e status.

## O que não foi feito

- Nenhuma chamada live a Meta, Shopify, Tiny, GA4, Metricool ou Klaviyo.
- Nenhum cupom foi criado ou alterado.
- Nenhuma campanha, anúncio, budget, UTM, criativo, tag, Shopify/Tiny, cliente, estoque, preço, banco de produção ou cron foi alterado.
- Nenhum envio externo foi feito.

## Próximo passo seguro

Usar esta fila para Lucas/Pareto/LK preencher handles/cupons/ad_ids oficiais. Depois, gerar a ponte `ad_id/utm_content/cupom/landing/referrer/note/tag` com status validated/mapped/ambiguous/investigation, ainda sem mexer em mídia ou criar cupom.
