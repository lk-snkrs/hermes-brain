# Gate B2 — Correção local/cache dos matches exatos P0 (20260610T114437Z)

## Escopo aprovado
- Lucas escolheu `A`: correção local/cache dos 6 matches exatos resolvidos.
- Escopo limitado a SQLite/cache local + receipt/PRD; sem write Tiny/Shopify.

## Execução
- DB local/cache criado: `areas/lk/sub-areas/stock/data/gate_b2_p0_resolved_local_cache_20260610T114437Z.db`
- Backup antes do apply: `areas/lk/sub-areas/stock/data/gate_b2_p0_resolved_local_cache_20260610T114437Z.before_apply.bak`
- Fonte: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-investigation-20260610T113047Z.csv`
- Linhas aplicadas: 6
- Tabelas locais atualizadas: `products`, `variants`, `sku_crosswalk`, `stock_snapshots`, `event_ledger`, `receipts`.
- Gate C manual pós-apply: `ok_silent`, alertas `0`, `telegram_sent=false`, `runtime_ativado=Nenhum`.

## SKUs cacheados
- `FQ8138-600-45` tamanho `45` / handle `tenis-jordan-4-retro-toro-bravo-2026-vermelho` / Tiny `FQ8138-600-45` / saldo LK Controle Estoque `0`
- `FQ8138-600-46` tamanho `46` / handle `tenis-jordan-4-retro-toro-bravo-2026-vermelho` / Tiny `FQ8138-600-46` / saldo LK Controle Estoque `0`
- `CW1588601-4` tamanho `37` / handle `nike-dunk-low-pink-red-white` / Tiny `CW1588601-4` / saldo LK Controle Estoque `0`
- `IH2612-12` tamanho `34` / handle `tenis-adidas-handball-spezial-sporty-rich-brown-marrom` / Tiny `IH2612-12` / saldo LK Controle Estoque `0`
- `IH2612-1` tamanho `35` / handle `tenis-adidas-handball-spezial-sporty-rich-brown-marrom` / Tiny `IH2612-1` / saldo LK Controle Estoque `0`
- `IH2612-13` tamanho `38` / handle `tenis-adidas-handball-spezial-sporty-rich-brown-marrom` / Tiny `IH2612-13` / saldo LK Controle Estoque `0`

## Limites
- Este cache local não corrige Tiny nem Shopify.
- Não é promessa de pronta entrega/disponibilidade pública.
- Disponibilidade ao cliente continua exigindo fonte viva e fluxo aprovado.

## Writes externos
- Tiny write: 0
- Shopify write: 0
- Cliente/fornecedor/compra/transferência: 0
- Cron/webhook/runtime novo: 0

## Rollback
- Restaurar o backup `areas/lk/sub-areas/stock/data/gate_b2_p0_resolved_local_cache_20260610T114437Z.before_apply.bak` sobre `areas/lk/sub-areas/stock/data/gate_b2_p0_resolved_local_cache_20260610T114437Z.db` ou descartar o DB local/cache criado nesta etapa.
