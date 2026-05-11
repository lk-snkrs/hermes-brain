**LK OS Daily Brief, 2026-05-10**
Preview interno, não enviado automaticamente. Gatilho: p0_p1_anomaly.

• Vendas: **R$ 34.809,92** em **9 pedidos**. Fonte: `fact_shopify`.
• GA4: **4301 sessões**, **8 transações GA4**. Fonte: `fact_ga4`, não receita oficial.
• Conversão aproximada: **0.21%** pedidos Shopify / sessões GA4.
• Tiny: ruptura `5`, baixo estoque `3`, unknown `1`. Fonte: `fact_tiny_stock`.

**Alertas acionáveis**
• [P0] Preparar preview de reposição/sourcing para SKUs vendidos com saldo zero no Tiny. Motivo: 5 SKU(s) vendidos aparecem em ruptura no depósito oficial. Fonte: `derived_reconciliation`.
• [P1] Revisar cobertura dos SKUs com saldo menor ou igual à venda do dia. Motivo: 3 SKU(s) com venda do dia encostando no saldo oficial. Fonte: `derived_reconciliation`.
• [P1] Resolver mapeamento Shopify SKU ↔ Tiny antes de campanha ou reposição automática. Motivo: 1 SKU(s) vendido(s) sem candidato Tiny seguro ou sem saldo legível. Fonte: `derived_reconciliation`.

**Guardrail**
• Isto é preview interno. Não enviou Telegram automático, Klaviyo, WhatsApp, campanha, fornecedor, compra ou alteração em Shopify/Tiny/banco.
