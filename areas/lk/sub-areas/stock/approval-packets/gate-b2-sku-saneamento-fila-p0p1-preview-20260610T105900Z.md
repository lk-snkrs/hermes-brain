# Preview — Fila P0/P1 de saneamento SKU/Tiny/Shopify — Gate B2

- Gerado em: 20260610T105900Z
- Escopo: local/read-only
- Base: issues consolidadas do Gate B2
- Tipo de prioridade: saneamento de mapeamento, não compra/reposição/disponibilidade
- Tiny write: 0
- Shopify write: 0
- Cron/webhook/runtime novo: 0
- Contato externo/cliente/fornecedor: 0

## Resumo
- Issues SKU/tamanho bloqueadas: 905
- Handles com bloqueio: 558
- P0_saneamento: 9
- P1_saneamento: 141
- P2_saneamento: 408

## Critério de priorização
- Peso 5: `matched_exact_sku_stock_missing_deposit` e `tiny_duplicate_exact_code_blocked`
- Peso 3: `shopify_duplicate_sku_blocked`
- Peso 2: `shopify_variant_tiny_missing`
- P0: 10+ bloqueios no handle, score >= 24 ou 3+ bloqueios críticos
- P1: 4+ bloqueios, score >= 8 ou pelo menos 1 bloqueio crítico

## Top P0
### slipper-alo-yoga-recovery-saddle-ivory-bege
- Produto: Slipper Alo Yoga Recovery Saddle/Ivory Bege
- Score saneamento: 35
- Bloqueios: 12 | SKUs afetados: 12
- Principal: `shopify_duplicate_sku_blocked`
- Counts: `{'shopify_duplicate_sku_blocked': 11, 'shopify_variant_tiny_missing': 1}`
- Amostra SKUs: `a0827u, a0827u-1, a0827u-10, a0827u-11, a0827u-2, a0827u-3, a0827u-4, a0827u-5, a0827u-6, a0827u-7, a0827u-8, a0827u-9`
- Ação preview: Mapear SKU Shopify sem Tiny exato; decidir se corrige SKU Shopify ou cadastra/ajusta código Tiny. Sem prometer disponibilidade até resolver.

### tenis-asics-gel-1130-black-pure-silver-prata
- Produto: Tênis ASICS Gel-1130 Black Pure Silver Prata
- Score saneamento: 35
- Bloqueios: 12 | SKUs afetados: 12
- Principal: `shopify_duplicate_sku_blocked`
- Counts: `{'shopify_duplicate_sku_blocked': 11, 'shopify_variant_tiny_missing': 1}`
- Amostra SKUs: `1201A906-001, 1201A906-001-34, 1201A906-001-35, 1201A906-001-36, 1201A906-001-37, 1201A906-001-38, 1201A906-001-39, 1201A906-001-40, 1201A906-001-41, 1201A906-001-42, 1201A906-001-43, 1201A906-001-44`
- Ação preview: Mapear SKU Shopify sem Tiny exato; decidir se corrige SKU Shopify ou cadastra/ajusta código Tiny. Sem prometer disponibilidade até resolver.

### tenis-asics-gel-1130-white-black-silver-prata
- Produto: Tênis ASICS Gel-1130 White Black Silver Prata
- Score saneamento: 35
- Bloqueios: 12 | SKUs afetados: 12
- Principal: `shopify_duplicate_sku_blocked`
- Counts: `{'shopify_duplicate_sku_blocked': 11, 'shopify_variant_tiny_missing': 1}`
- Amostra SKUs: `1201A933-100, 1201A933-100-34, 1201A933-100-35, 1201A933-100-36, 1201A933-100-37, 1201A933-100-38, 1201A933-100-39, 1201A933-100-40, 1201A933-100-41, 1201A933-100-42, 1201A933-100-43, 1201A933-100-44`
- Ação preview: Mapear SKU Shopify sem Tiny exato; decidir se corrige SKU Shopify ou cadastra/ajusta código Tiny. Sem prometer disponibilidade até resolver.

### tenis-jordan-4-retro-toro-bravo-2026-vermelho
- Produto: Tênis Jordan 4 Retro Toro Bravo 2026 Vermelho
- Score saneamento: 35
- Bloqueios: 12 | SKUs afetados: 12
- Principal: `shopify_duplicate_sku_blocked`
- Counts: `{'shopify_duplicate_sku_blocked': 11, 'shopify_variant_tiny_missing': 1}`
- Amostra SKUs: `FQ8138-600, FQ8138-600-34, FQ8138-600-35, FQ8138-600-36, FQ8138-600-37, FQ8138-600-38, FQ8138-600-39, FQ8138-600-40, FQ8138-600-41, FQ8138-600-42, FQ8138-600-43, FQ8138-600-44`
- Ação preview: Mapear SKU Shopify sem Tiny exato; decidir se corrige SKU Shopify ou cadastra/ajusta código Tiny. Sem prometer disponibilidade até resolver.

### tenis-new-balance-204l-grey-matter-shipyard-cinza
- Produto: Tênis New Balance 204L Grey Matter Shipyard Cinza
- Score saneamento: 35
- Bloqueios: 12 | SKUs afetados: 12
- Principal: `shopify_duplicate_sku_blocked`
- Counts: `{'shopify_duplicate_sku_blocked': 11, 'shopify_variant_tiny_missing': 1}`
- Amostra SKUs: `U204L86W, U204L86W-1, U204L86W-10, U204L86W-11, U204L86W-2, U204L86W-3, U204L86W-4, U204L86W-5, U204L86W-6, U204L86W-7, U204L86W-8, U204L86W-9`
- Ação preview: Mapear SKU Shopify sem Tiny exato; decidir se corrige SKU Shopify ou cadastra/ajusta código Tiny. Sem prometer disponibilidade até resolver.

### tenis-air-jordan-1-low-og-year-of-snake-2025-cinza
- Produto: Tênis Nike Air Jordan 1 Low Og Year of Snake 2025 Cinza
- Score saneamento: 33
- Bloqueios: 11 | SKUs afetados: 11
- Principal: `shopify_duplicate_sku_blocked`
- Counts: `{'shopify_duplicate_sku_blocked': 11}`
- Amostra SKUs: `HF3144 100-1, HF3144 100-10, HF3144 100-11, HF3144 100-2, HF3144 100-3, HF3144 100-4, HF3144 100-5, HF3144 100-6, HF3144 100-7, HF3144 100-8, HF3144 100-9`
- Ação preview: Revisar grade Shopify com SKU duplicado; atribuir SKU filho/tamanho correto ou corrigir variante duplicada. Não deduplicar silenciosamente.

### air-jordan-1-low-true-blue
- Produto: Tênis Nike Air Jordan 1 Low True Blue Azul
- Score saneamento: 25
- Bloqueios: 5 | SKUs afetados: 5
- Principal: `tiny_duplicate_exact_code_blocked`
- Counts: `{'tiny_duplicate_exact_code_blocked': 5}`
- Amostra SKUs: `553560412-2, 553560412-3, 553560412-4, 553560412-5, 553560412-6`
- Ação preview: Revisar duplicidade de código exato no Tiny; escolher registro canônico/merge/desativação operacional antes de disponibilidade.

### nike-dunk-low-pink-red-white
- Produto: Tênis Nike Dunk Low Pink Red White Rosa
- Score saneamento: 17
- Bloqueios: 4 | SKUs afetados: 4
- Principal: `tiny_duplicate_exact_code_blocked`
- Counts: `{'shopify_variant_tiny_missing': 1, 'tiny_duplicate_exact_code_blocked': 3}`
- Amostra SKUs: `CW1588601-4, CW1590-601-1, CW1590-601-3, CW1590-601-5`
- Ação preview: Mapear SKU Shopify sem Tiny exato; decidir se corrige SKU Shopify ou cadastra/ajusta código Tiny. Sem prometer disponibilidade até resolver.

### tenis-adidas-handball-spezial-sporty-rich-brown-marrom
- Produto: Tênis adidas Handball Spezial Sporty & Rich Brown Marrom
- Score saneamento: 17
- Bloqueios: 4 | SKUs afetados: 4
- Principal: `tiny_duplicate_exact_code_blocked`
- Counts: `{'shopify_variant_tiny_missing': 1, 'tiny_duplicate_exact_code_blocked': 3}`
- Amostra SKUs: `IH2612, IH2612-10, IH2612-2, IH2612-8`
- Ação preview: Mapear SKU Shopify sem Tiny exato; decidir se corrige SKU Shopify ou cadastra/ajusta código Tiny. Sem prometer disponibilidade até resolver.

## Próxima execução bloqueada
A fila acima é preview local. Para executar correções em Tiny/Shopify, ainda precisa de aprovação escopada por item/lote, snapshot/readback e rollback. Para transformar em fila com demanda/venda real, usar Shopify orders/read-only antes de qualquer compra/transferência.

## Artefatos
- JSON completo: `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-fila-p0p1-20260610T105900Z.json`
- CSV fila: `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-fila-p0p1-20260610T105900Z.csv`
- Este preview: `areas/lk/sub-areas/stock/approval-packets/gate-b2-sku-saneamento-fila-p0p1-preview-20260610T105900Z.md`
