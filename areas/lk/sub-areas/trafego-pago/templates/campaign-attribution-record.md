# Template — Dicionário Canônico de Campanha/Influencer LK

Status: template read-only. Preencher com dados verificados; usar `[a confirmar]` quando a evidência ainda não existir.

## Registro

- canonical_id: `[ex: influencer_lala_noleto_2026_q2]`
- status: `[draft | mapped | validated | ambiguous | deprecated]`
- influencer_name: `[nome]`
- influencer_handle: `[handle]`
- platform: `[Meta | Google | Klaviyo | orgânico | misto]`
- paid_source: `[Meta Ads | Google Ads | Metricool | outro]`
- commercial_window: `[datas de início/fim ou janela usada]`

## Naming pago

- meta_campaign_name_patterns:
  - `[padrão 1]`
- meta_adset_name_patterns:
  - `[padrão 1]`
- meta_ad_name_patterns:
  - `[padrão 1]`
- google_campaign_name_patterns:
  - `[padrão 1]`

## Evidência Shopify/GA4 esperada

- utm_source_expected: `[a confirmar]`
- utm_medium_expected: `[a confirmar]`
- utm_campaign_expected: `[a confirmar]`
- utm_content_expected: `[a confirmar]`
- coupon_patterns:
  - `[a confirmar]`
- landing_url_patterns:
  - `[a confirmar]`
- shopify_match_rule: `[exato / normalizado / cupom / landing / combinado]`

## Produto esperado

- expected_product_theme: `[ex: Dia das Mães, feminino premium, corrida, Onitsuka, New Balance etc.]`
- expected_brand: `[marca]`
- expected_model: `[modelo]`
- expected_skus:
  - `[SKU Shopify]`
- expected_size_range: `[grade/tamanhos esperados]`

## Performance apurada

- spend: `[R$]`
- platform_attributed_revenue: `[R$]`
- platform_attributed_roas: `[x]`
- shopify_evidence_orders: `[n]`
- shopify_evidence_revenue: `[R$]`
- operational_roas: `[R$ Shopify compatível / custo compatível]`
- confidence_level: `[alta | média | baixa]`

## Consequência de estoque

- produtos/SKUs vendidos:
  - `[nome + SKU + tamanho + quantidade]`
- Tiny `LK | CONTROLE ESTOQUE` no momento da análise: `[resumo]`
- efeito: `[sem ação | repor estoque | checar sourcing | risco de ruptura | campanha segura | campanha não recomendada]`
- lead_time_relevante: `[ex: Brasil curto / importação ~30 dias / a confirmar]`

## Recomendação

- leitura: `[interpretação]`
- próxima ação sugerida: `[ação]`
- aprovação necessária: `[não / sim: Lucas]`
- riscos/limites: `[atribuição, UTM, cupom, janela, estoque]`
