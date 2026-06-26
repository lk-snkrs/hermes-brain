# LK Stock — validação New Balance 740 publicável

Data/hora: 2026-06-26T09:12:53Z  
Pedido origem: Mesa COO / Collection Optimizer — decidir se `/collections/new-balance-740` pode sair do bloqueio.  
Escopo: validação read-only Stock OS/Tiny; sem Tiny write, sem Shopify write, sem publicação, sem compra, sem fornecedor, sem campanha, sem contato externo.

## Veredito

**Classificação LK Stock:** `indisponível-sem venda` / `não publicável por estoque`.

Motivo: os 8 SKUs vendáveis do produto `Tênis New Balance 740 x Concepts Saignée Verde` resolvem com match exato Shopify↔Tiny, mas todos estão com saldo `0` no depósito Tiny `LK | CONTROLE ESTOQUE`. Não há divergência SKU-Tiny a corrigir neste item; o bloqueio operacional é estoque zero. O produto também segue arquivado/não publicado no snapshot Shopify originador, mas a conclusão deste handoff é apenas da camada Stock/Tiny.

## Evidência Stock OS local

- Pointer Stock OS: `areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`
- DB apontada: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_tiny_full_sync_20260626T082006Z.db`
- Pointer atualizado em: `2026-06-26T08:45:52Z`
- Último sync Tiny reportado: `status=ok`, `rows_failed=0`, `quantity_source=Tiny produto.obter.estoque / LK | CONTROLE ESTOQUE`, writes externos `0`.
- Lookup local por `U740GP2-*`: 8 linhas encontradas em `current_local_stock`, todas `CONSULTABLE_LOCAL_RESOLVED_BY_FULL_LIVE_MATCH`, `local_consult_safe=1`, `identity_resolved_safe=1`, `public_availability_safe=0`, `availability_claim_allowed=0`, `stock_quantity_max_observed=0.0`.

## Evidência live read-only Tiny/Shopify

Comando executado via Doppler `lk-stock`, sem imprimir secrets, com `secrets_printed=false`:

- JSON: `areas/lk/sub-areas/stock/reports/lk-stock-nb740-live-crosswalk-20260626T091220Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/lk-stock-nb740-live-crosswalk-20260626T091220Z.csv`
- Summary live: `total_rows=9`, `matched_exact_sku_stock_resolved=9`, `unresolved_or_blocked=0`, `shopify_duplicate_sku_blocked=0`, `tiny_duplicate_exact_code_blocked=0`, `shopify_variant_tiny_missing=0`, `tiny_only_shopify_missing=0`, writes externos `0`.

## Grade auditada

| SKU Shopify | Tamanho | Tiny código | Tiny id | Saldo `LK | CONTROLE ESTOQUE` | Status |
|---|---:|---|---:|---:|---|
| `U740GP2-1` | 37 | `U740GP2-1` | `1061338165` | 0 | match exato, sem estoque |
| `U740GP2-2` | 38 | `U740GP2-2` | `1061338168` | 0 | match exato, sem estoque |
| `U740GP2-3` | 39 | `U740GP2-3` | `1061338171` | 0 | match exato, sem estoque |
| `U740GP2-4` | 40 | `U740GP2-4` | `1061338174` | 0 | match exato, sem estoque |
| `U740GP2-5` | 41 | `U740GP2-5` | `1061338177` | 0 | match exato, sem estoque |
| `U740GP2-6` | 42 | `U740GP2-6` | `1061338180` | 0 | match exato, sem estoque |
| `U740GP2-7` | 43 | `U740GP2-7` | `1061338183` | 0 | match exato, sem estoque |
| `U740GP2-8` | 44 | `U740GP2-8` | `1061338186` | 0 | match exato, sem estoque |

Observação: o parent/base `U740GP2` também apareceu no crosswalk live com saldo `0`, mas não é variante vendável para decisão de grade pública.

## Recomendação / próximo dono

- Manter `/collections/new-balance-740` bloqueada neste momento.
- Não criar coleção/guia público para este produto como se houvesse pronta entrega.
- Não há correção SKU-Tiny necessária para os 8 tamanhos: a identidade está resolvida; o problema é saldo zero.
- Se Lucas quiser continuar a frente, o próximo passo é decisão comercial separada: compra/reposição via fluxo Júlio/Notion ou plano LK Shopify para produto arquivado, ambos exigindo aprovação escopada conforme o caso.

## Guardrails

- Tiny write: `0`
- Shopify write: `0`
- Compra/fornecedor: `0`
- Cliente/campanha/WhatsApp/Klaviyo/GMC: `0`
- Secrets impressos: `0` (`values_printed=false`; `secrets_printed=false` no report live)
- Public availability claim: `0`

## Continuidade

- Reminder OS loop needed: `no` para a validação Stock, porque o veredito de estoque está fechado.
- Owner seguinte: `lk-collection-optimizer`/Mesa COO para manter bloqueio da frente ou pedir novo approval packet; `lk-shopify` só se houver decisão futura de tratar status/arquivamento; Júlio/Notion só se houver decisão futura de compra/reposição.
- Gatilho de revisão: nova compra/entrada de estoque Tiny para `U740GP2-*`, novo sync Stock OS com saldo positivo, ou aprovação explícita de Lucas para caminho comercial separado.
