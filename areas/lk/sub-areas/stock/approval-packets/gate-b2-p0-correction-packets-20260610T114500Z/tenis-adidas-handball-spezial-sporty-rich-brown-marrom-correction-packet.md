# Correction packet Gate B2 P0 — Tênis adidas Handball Spezial Sporty & Rich Brown Marrom

- Handle: `tenis-adidas-handball-spezial-sporty-rich-brown-marrom`
- Gerado em: `20260610T114500Z`
- Lane: `TINY_DUPLICATE_PACKET`
- Escopo: packet de correção, sem executar write externo.
- Linhas avaliadas: 7
- shopify_variant_tiny_missing: 1
- matched_exact_sku_stock_resolved: 3
- tiny_duplicate_exact_code_blocked: 3
- Tiny write: 0
- Shopify write: 0
- Disponibilidade/pronta entrega: bloqueada até saneamento + readback Tiny oficial no fluxo aprovado.

## Proposta automática por tipo
### tiny_duplicate_exact_code_blocked (3)
- Ação proposta: Preparar diff Tiny: escolher item canônico e tratar duplicados de código exato; disponibilidade permanece bloqueada.
- `IH2612-2` / Shopify SKU `IH2612-2` / tamanho `36`
  - Duplicados Tiny: 2; candidatos: Tiny 1063353898 saldo 0.0 desc N; Tiny 1057960254 saldo 0.0 desc N
  - Candidato canônico conservador para revisão: Tiny ID `1057960254` (menor ID; não executar sem aprovação).
- `IH2612-8` / Shopify SKU `IH2612-8` / tamanho `37`
  - Duplicados Tiny: 2; candidatos: Tiny 1069938132 saldo 0.0 desc N; Tiny 1063992031 saldo 0.0 desc N
  - Candidato canônico conservador para revisão: Tiny ID `1063992031` (menor ID; não executar sem aprovação).
- `IH2612-10` / Shopify SKU `IH2612-10` / tamanho `39`
  - Duplicados Tiny: 2; candidatos: Tiny 1069938138 saldo 0.0 desc N; Tiny 1069538196 saldo 0.0 desc N
  - Candidato canônico conservador para revisão: Tiny ID `1069538196` (menor ID; não executar sem aprovação).
### shopify_variant_tiny_missing (1)
- Ação proposta: Preparar mapeamento/cadastro/ajuste de código Tiny exato correspondente ao SKU Shopify; sem prometer disponibilidade.
- `IH2612` / Shopify SKU `IH2612` / tamanho `parent/base`
  - Sem Tiny código exato confirmado; precisa candidato/cadastro/ajuste antes de disponibilidade.
### matched_exact_sku_stock_resolved (3)
- Ação proposta: Pode registrar como mapeamento exato resolvido na base local; saldo Tiny LK | CONTROLE ESTOQUE observado no read-only.
- `IH2612-12` / Shopify SKU `IH2612-12` / tamanho `34`
  - Tiny código `IH2612-12` / Tiny ID `1069538184` / depósito `LK | CONTROLE ESTOQUE` / saldo `0.0` / desconsiderar `N`
- `IH2612-1` / Shopify SKU `IH2612-1` / tamanho `35`
  - Tiny código `IH2612-1` / Tiny ID `1057960256` / depósito `LK | CONTROLE ESTOQUE` / saldo `0.0` / desconsiderar `N`
- `IH2612-13` / Shopify SKU `IH2612-13` / tamanho `38`
  - Tiny código `IH2612-13` / Tiny ID `1069538191` / depósito `LK | CONTROLE ESTOQUE` / saldo `0.0` / desconsiderar `N`

## Diff/execução externa
- Não executado.
- Este packet não é autorização de correção. Para executar, precisa aprovação escopada por handle/lote com destino (Tiny/Shopify), diff e rollback.

## Rollback
- Nenhum write externo feito. Rollback atual: descartar este packet/JSON local.

## Próximo gate sugerido
- Aprovar diff Tiny específico para escolher item canônico e resolver duplicados; nenhum write ainda.

## Artefatos
- JSON: `areas/lk/sub-areas/stock/approval-packets/gate-b2-p0-correction-packets-20260610T114500Z/tenis-adidas-handball-spezial-sporty-rich-brown-marrom-correction-packet.json`
- Fonte: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-investigation-20260610T113047Z.csv`
