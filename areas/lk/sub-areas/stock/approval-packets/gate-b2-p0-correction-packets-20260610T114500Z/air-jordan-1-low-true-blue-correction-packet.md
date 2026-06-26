# Correction packet Gate B2 P0 — Tênis Nike Air Jordan 1 Low True Blue Azul

- Handle: `air-jordan-1-low-true-blue`
- Gerado em: `20260610T114500Z`
- Lane: `TINY_DUPLICATE_PACKET`
- Escopo: packet de correção, sem executar write externo.
- Linhas avaliadas: 1
- tiny_duplicate_exact_code_blocked: 1
- Tiny write: 0
- Shopify write: 0
- Disponibilidade/pronta entrega: bloqueada até saneamento + readback Tiny oficial no fluxo aprovado.

## Proposta automática por tipo
### tiny_duplicate_exact_code_blocked (1)
- Ação proposta: Preparar diff Tiny: escolher item canônico e tratar duplicados de código exato; disponibilidade permanece bloqueada.
- `553560412-2` / Shopify SKU `553560412-2` / tamanho `35`
  - Duplicados Tiny: 2; candidatos: Tiny 951352895 saldo 0.0 desc N; Tiny 952363402 saldo 0.0 desc N
  - Candidato canônico conservador para revisão: Tiny ID `951352895` (menor ID; não executar sem aprovação).

## Diff/execução externa
- Não executado.
- Este packet não é autorização de correção. Para executar, precisa aprovação escopada por handle/lote com destino (Tiny/Shopify), diff e rollback.

## Rollback
- Nenhum write externo feito. Rollback atual: descartar este packet/JSON local.

## Próximo gate sugerido
- Aprovar diff Tiny específico para escolher item canônico e resolver duplicados; nenhum write ainda.

## Artefatos
- JSON: `areas/lk/sub-areas/stock/approval-packets/gate-b2-p0-correction-packets-20260610T114500Z/air-jordan-1-low-true-blue-correction-packet.json`
- Fonte: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-investigation-20260610T113047Z.csv`
