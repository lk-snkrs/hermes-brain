**LK OS Weekly CEO Review, 2026-05-04 a 2026-05-10**
Preview interno, não enviado automaticamente. Gatilho: `p0_p1_anomaly`.

• Shopify: **R$ 312.261,74** em **97 pedidos**. Fonte: `fact_shopify`.
• GA4: **29605 sessões**, **55 transações GA4**. Fonte: `fact_ga4`, não receita oficial.
• Conversão aproximada: **0.33%** pedidos Shopify / sessões GA4.
• Tiny: ruptura `8`, baixo estoque `3`, unknown `3`. Fonte: `fact_tiny_stock`.
• Meta: gasto sinalizado **R$ 9.374,42**, ROAS plataforma `15.01`. Fonte: `platform_signal`.
• Metricool/Google Ads: linhas `21`, status `200`. Fonte: `platform_signal`.

**Prioridades**
• [P0] Preparar fila de sourcing/reposição para SKUs vendidos na semana com saldo zero no Tiny. Motivo: 8 SKU(s) vendidos aparecem em ruptura no depósito oficial. Fonte: `derived_reconciliation`.
• [P1] Revisar cobertura dos SKUs com venda semanal encostando no saldo oficial. Motivo: 3 SKU(s) têm saldo menor ou igual à venda da semana. Fonte: `derived_reconciliation`.
• [P1] Priorizar saneamento SKU Shopify ↔ Tiny antes de escalar mídia dos produtos vendidos. Motivo: 3 SKU(s) vendidos sem candidato Tiny seguro ou sem saldo legível. Fonte: `derived_reconciliation`.

**Guardrail**
• Preview interno. Não enviou Telegram automático, cron, Klaviyo, WhatsApp, campanha, fornecedor, compra ou alteração em Shopify/Tiny/banco.
