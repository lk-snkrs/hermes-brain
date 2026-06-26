# Approval packet — LK Stock OS sequência B depois A

- Data/hora UTC: 2026-06-10T19:42:08.722931Z
- DB entrada: `areas/lk/sub-areas/stock/data/lk_stock_os_current_demand_scored_20260610T190741Z.db`
- DB saída local: `areas/lk/sub-areas/stock/data/lk_stock_os_current_p1_identity_then_p0_preview_20260610TSEQBA.db`
- Escopo: read-only/local; sem execução externa.

## B — P1 identity batch

- P1 analisados: 13
- Resolvidos local/live exact: 1
- Permanecem bloqueados: 12
- Status live: `{'BLOCKED_SHOPIFY_DUPLICATE_LIVE': 8, 'LIVE_EXACT_IDENTITY_AND_STOCK_RESOLVED': 1, 'BLOCKED_TINY_MISSING_LIVE': 1, 'BLOCKED_TINY_DUPLICATE_LIVE': 3}`

- **#1 — CDGP2**
  - Polo Comme des Garçons PLAY Red Emblem White Branco | tamanho `G/L`
  - Status live: `BLOCKED_SHOPIFY_DUPLICATE_LIVE` | Shopify exact: `3` | Tiny exact: `1` | saldo LK: `0.0`
  - Decisão: mantido bloqueado para saneamento
- **#2 — LIP**
  - The Peptide Lip Tints Rhode Multicolor | tamanho ``
  - Status live: `BLOCKED_SHOPIFY_DUPLICATE_LIVE` | Shopify exact: `5` | Tiny exact: `0` | saldo LK: `None`
  - Decisão: mantido bloqueado para saneamento
- **#3 — LIPCASE-11**
  - Lip Case Rhode By Hailey Bieber | tamanho `Iphone 16 Pro Max`
  - Status live: `LIVE_EXACT_IDENTITY_AND_STOCK_RESOLVED` | Shopify exact: `1` | Tiny exact: `1` | saldo LK: `0.0`
  - Decisão: resolvido no cache local
- **#4 — CD0461002**
  - Tênis Nike Air Jordan 1 High Seafoam Verde | tamanho `34`
  - Status live: `BLOCKED_SHOPIFY_DUPLICATE_LIVE` | Shopify exact: `8` | Tiny exact: `1` | saldo LK: `0.0`
  - Decisão: mantido bloqueado para saneamento
- **#5 — AIME11**
  - Boné 5 Panel Aimé Leon Dore Unisphere Azul | tamanho ``
  - Status live: `BLOCKED_SHOPIFY_DUPLICATE_LIVE` | Shopify exact: `2` | Tiny exact: `2` | saldo LK: `0.0`
  - Decisão: mantido bloqueado para saneamento
- **#6 — NDP006-3**
  - Camiseta Nude Project Global Soon Ash Cinza | tamanho `M/M`
  - Status live: `BLOCKED_SHOPIFY_DUPLICATE_LIVE` | Shopify exact: `2` | Tiny exact: `1` | saldo LK: `1.0`
  - Decisão: mantido bloqueado para saneamento
- **#7 — ST33**
  - Camiseta Boxy Saint Studio Supima Preto | tamanho `P/S`
  - Status live: `BLOCKED_SHOPIFY_DUPLICATE_LIVE` | Shopify exact: `4` | Tiny exact: `5` | saldo LK: `1.0`
  - Decisão: mantido bloqueado para saneamento
- **#8 — 1183A746-751-1**
  - Tênis Onitsuka Tiger Mexico 66 Kill Bill Slip-On Amarelo | tamanho `34`
  - Status live: `BLOCKED_TINY_MISSING_LIVE` | Shopify exact: `1` | Tiny exact: `0` | saldo LK: `None`
  - Decisão: mantido bloqueado para saneamento
- **#9 — 1183B566.201**
  - Tênis Onitsuka Tiger Mexico 66 Gold White Dourado | tamanho `39.5`
  - Status live: `BLOCKED_TINY_DUPLICATE_LIVE` | Shopify exact: `1` | Tiny exact: `2` | saldo LK: `0.0`
  - Decisão: mantido bloqueado para saneamento
- **#10 — CQ9446400**
  - Tênis Nike Air Jordan 1 Low Alternate Royal Toe Azul | tamanho `34`
  - Status live: `BLOCKED_SHOPIFY_DUPLICATE_LIVE` | Shopify exact: `5` | Tiny exact: `1` | saldo LK: `0.0`
  - Decisão: mantido bloqueado para saneamento
- **#11 — PC9060GY-2**
  - Tênis New Balance 9060 Kids Raincloud Cinza (Infantil) | tamanho `33`
  - Status live: `BLOCKED_TINY_DUPLICATE_LIVE` | Shopify exact: `1` | Tiny exact: `2` | saldo LK: `0.0`
  - Decisão: mantido bloqueado para saneamento
- **#12 — 41499672090-4**
  - Chinelo Havaianas x Dolce & Gabbana Carreto Ciciliano Vermelho | tamanho `41/42`
  - Status live: `BLOCKED_TINY_DUPLICATE_LIVE` | Shopify exact: `1` | Tiny exact: `2` | saldo LK: `0.0`
  - Decisão: mantido bloqueado para saneamento
- **#13 — 553558065-1**
  - Tênis Nike Air Jordan 1 Low Lucky Green Verde | tamanho `40`
  - Status live: `BLOCKED_SHOPIFY_DUPLICATE_LIVE` | Shopify exact: `2` | Tiny exact: `2` | saldo LK: `0.0`
  - Decisão: mantido bloqueado para saneamento

## A — P0 live reconfirm + preview

- P0 reconfirmados: 4
- Quantidade total sugerida em preview: 13
- Status preview: `{'preview_replenishment_candidate': 4}`

- **#1 — 205759 610-8**
  - Crocs Classic Clog x The Cars Lightning McQueen Vermelho | tamanho `41`
  - Live: `LIVE_EXACT_IDENTITY_AND_STOCK_RESOLVED` | saldo Tiny LK: `0.0` | demanda: `6.0` | receita sinal: R$ 2.999,98
  - Preview: `preview_replenishment_candidate` | qtd sugerida: `4`
  - Cálculo: units_signal=6.0; avg_daily=0.20; base_need_15d=3; current_tiny_lk=0.0; recommended_qty=4; cap=units_signal
- **#2 — FQ1180001-11**
  - Tênis Yuto Horigome x Nike SB Dunk Low Azul | tamanho `44`
  - Live: `LIVE_EXACT_IDENTITY_AND_STOCK_RESOLVED` | saldo Tiny LK: `0.0` | demanda: `3.0` | receita sinal: R$ 3.999,99
  - Preview: `preview_replenishment_candidate` | qtd sugerida: `3`
  - Cálculo: units_signal=3.0; avg_daily=0.10; base_need_15d=2; current_tiny_lk=0.0; recommended_qty=3; cap=units_signal
- **#3 — IH2612-1**
  - Tênis adidas Handball Spezial Sporty & Rich Brown Marrom | tamanho `35`
  - Live: `LIVE_EXACT_IDENTITY_AND_STOCK_RESOLVED` | saldo Tiny LK: `0.0` | demanda: `3.0` | receita sinal: R$ 2.999,99
  - Preview: `preview_replenishment_candidate` | qtd sugerida: `3`
  - Cálculo: units_signal=3.0; avg_daily=0.10; base_need_15d=2; current_tiny_lk=0.0; recommended_qty=3; cap=units_signal
- **#4 — 205759 610-7**
  - Crocs Classic Clog x The Cars Lightning McQueen Vermelho | tamanho `40`
  - Live: `LIVE_EXACT_IDENTITY_AND_STOCK_RESOLVED` | saldo Tiny LK: `0.0` | demanda: `3.0` | receita sinal: R$ 1.499,99
  - Preview: `preview_replenishment_candidate` | qtd sugerida: `3`
  - Cálculo: units_signal=3.0; avg_daily=0.10; base_need_15d=2; current_tiny_lk=0.0; recommended_qty=3; cap=units_signal

## Guardrails

- Tiny write: 0
- Shopify write: 0
- Writes externos: 0
- Pronta entrega pública: 0
- Runtime/cron novo: 0

## Aprovação necessária para executar algo

- Para P0: aprovar ação exata por SKU/quantidade/canal. Este packet é só preview.
- Para P1 bloqueados: aprovar saneamento externo somente com diff/rollback, se quiser mexer em Shopify/Tiny.
