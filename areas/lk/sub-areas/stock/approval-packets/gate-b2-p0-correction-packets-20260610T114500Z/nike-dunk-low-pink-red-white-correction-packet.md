# Correction packet Gate B2 P0 — Tênis Nike Dunk Low Pink Red White Rosa

- Handle: `nike-dunk-low-pink-red-white`
- Gerado em: `20260610T114500Z`
- Lane: `LOCAL_CACHE_RESOLVED_ZERO_STOCK`
- Escopo: packet de correção, sem executar write externo.
- Linhas avaliadas: 1
- matched_exact_sku_stock_resolved: 1
- Tiny write: 0
- Shopify write: 0
- Disponibilidade/pronta entrega: bloqueada até saneamento + readback Tiny oficial no fluxo aprovado.

## Proposta automática por tipo
### matched_exact_sku_stock_resolved (1)
- Ação proposta: Pode registrar como mapeamento exato resolvido na base local; saldo Tiny LK | CONTROLE ESTOQUE observado no read-only.
- `CW1588601-4` / Shopify SKU `CW1588601-4` / tamanho `37`
  - Tiny código `CW1588601-4` / Tiny ID `941604662` / depósito `LK | CONTROLE ESTOQUE` / saldo `0.0` / desconsiderar `N`

## Diff/execução externa
- Não executado.
- Este packet não é autorização de correção. Para executar, precisa aprovação escopada por handle/lote com destino (Tiny/Shopify), diff e rollback.

## Rollback
- Nenhum write externo feito. Rollback atual: descartar este packet/JSON local.

## Próximo gate sugerido
- Aprovar registro local/cache dos matches exatos resolvidos; sem Tiny/Shopify write.

## Artefatos
- JSON: `areas/lk/sub-areas/stock/approval-packets/gate-b2-p0-correction-packets-20260610T114500Z/nike-dunk-low-pink-red-white-correction-packet.json`
- Fonte: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-investigation-20260610T113047Z.csv`
