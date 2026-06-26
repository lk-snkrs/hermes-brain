# LK Stock OS — Demand/Score enrichment — 20260610T190741Z

## Resultado

- DB origem: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_identity_resolved_20260610T172139Z.db`
- DB enriquecida: `areas/lk/sub-areas/stock/data/lk_stock_os_current_demand_scored_20260610T190741Z.db`
- Linhas Stock OS: 903
- SKUs com sinal local de venda/demanda: 352
- Linhas da DB com demanda casada por SKU normalizado: 18
- Demanda com identidade resolvida: 5
- Demanda ainda bloqueada por identidade: 13
- P0 candidatos locais: 4
- P1 candidatos locais: 13

## Top 20 por score operacional

- P1 · CDGP2 · Polo Comme des Garçons PLAY Red Emblem White Branco · tam G/L · unidades sinal 30.0 · estoque DB None · risco BLOCKED_IDENTITY · score 246.0
- P1 · LIP · The Peptide Lip Tints Rhode Multicolor · tam  · unidades sinal 19.0 · estoque DB None · risco BLOCKED_IDENTITY · score 181.95
- P1 · LIPCASE-11 · Lip Case Rhode By Hailey Bieber · tam Iphone 16 Pro Max · unidades sinal 13.0 · estoque DB None · risco BLOCKED_IDENTITY · score 134.85
- P0 · 205759 610-8 · Crocs Classic Clog x The Cars Lightning McQueen Vermelho · tam 41 · unidades sinal 6.0 · estoque DB 0.0 · risco SOLD_AND_ZERO_STOCK_IN_DB · score 98.0
- P1 · CD0461002 · Tênis Nike Air Jordan 1 High Seafoam Verde · tam 34 · unidades sinal 10.0 · estoque DB 0.0 · risco BLOCKED_IDENTITY · score 94.54
- P1 · AIME11 · Boné 5 Panel Aimé Leon Dore Unisphere Azul · tam  · unidades sinal 9.0 · estoque DB None · risco BLOCKED_IDENTITY · score 80.25
- P0 · FQ1180001-11 · Tênis Yuto Horigome x Nike SB Dunk Low Azul · tam 44 · unidades sinal 3.0 · estoque DB 0.0 · risco SOLD_AND_ZERO_STOCK_IN_DB · score 72.0
- P1 · NDP006-3 · Camiseta Nude Project Global Soon Ash Cinza · tam M/M · unidades sinal 7.0 · estoque DB 1.0 · risco BLOCKED_IDENTITY · score 68.25
- P0 · IH2612-1 · Tênis adidas Handball Spezial Sporty & Rich Brown Marrom · tam 35 · unidades sinal 3.0 · estoque DB 0.0 · risco SOLD_AND_ZERO_STOCK_IN_DB · score 68.0
- P0 · 205759 610-7 · Crocs Classic Clog x The Cars Lightning McQueen Vermelho · tam 40 · unidades sinal 3.0 · estoque DB 0.0 · risco SOLD_AND_ZERO_STOCK_IN_DB · score 66.5
- P1 · ST33 · Camiseta Boxy Saint Studio Supima Preto · tam P/S · unidades sinal 5.0 · estoque DB None · risco BLOCKED_IDENTITY · score 45.42
- P1 · 1183A746-751-1 · Tênis Onitsuka Tiger Mexico 66 Kill Bill Slip-On Amarelo · tam 34 · unidades sinal 3.0 · estoque DB None · risco BLOCKED_IDENTITY · score 34.05
- P1 · 1183B566.201 · Tênis Onitsuka Tiger Mexico 66 Gold White Dourado · tam 39.5 · unidades sinal 3.0 · estoque DB None · risco BLOCKED_IDENTITY · score 31.8
- P1 · CQ9446400 · Tênis Nike Air Jordan 1 Low Alternate Royal Toe Azul · tam 34 · unidades sinal 3.0 · estoque DB 0.0 · risco BLOCKED_IDENTITY · score 31.35
- P1 · PC9060GY-2 · Tênis New Balance 9060 Kids Raincloud Cinza (Infantil) · tam 33 · unidades sinal 3.0 · estoque DB None · risco BLOCKED_IDENTITY · score 30.9
- P1 · 41499672090-4 · Chinelo Havaianas x Dolce & Gabbana Carreto Ciciliano Vermelho · tam 41/42 · unidades sinal 2.0 · estoque DB None · risco BLOCKED_IDENTITY · score 23.85
- P1 · 553558065-1 · Tênis Nike Air Jordan 1 Low Lucky Green Verde · tam 40 · unidades sinal 2.0 · estoque DB None · risco BLOCKED_IDENTITY · score 23.51
- P2 · DD139110-38 · Tênis Nike Dunk Low Black OG Panda Preto · tam 38 · unidades sinal 2.0 · estoque DB 4.0 · risco DEMAND_WITH_STOCK_OBSERVED · score 21.6
- P3 · 553560412-2 · Tênis Nike Air Jordan 1 Low True Blue Azul · tam 35 · unidades sinal 0.0 · estoque DB None · risco BLOCKED_IDENTITY · score 0.0
- P3 · 553560412-3 · Tênis Nike Air Jordan 1 Low True Blue Azul · tam 36 · unidades sinal 0.0 · estoque DB None · risco BLOCKED_IDENTITY · score 0.0

## Guardrails

- Tiny write: 0
- Shopify write: 0
- Writes externos: 0
- `public_availability_safe`: 0
- `availability_claim_allowed`: 0

Esta etapa usa nossa database Stock OS como superfície canônica e enriquece com fontes locais de vendas/Data Spine. Não promete disponibilidade pública e não executa compra/reposição.
