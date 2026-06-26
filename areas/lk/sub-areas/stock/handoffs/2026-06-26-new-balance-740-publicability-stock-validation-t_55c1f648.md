# LK Stock — validação Tiny/Stock OS para publicabilidade New Balance 740

Data/hora: 2026-06-26T09:16:45Z  
Kanban task: `t_55c1f648`  
Origem: `lk-shopify` / task `t_1f079009` — superfície Shopify read-only validada, mas publicação/destravamento dependia de estoque real.  
Escopo: READ-ONLY em Stock OS/Tiny/Shopify crosswalk; sem Tiny write, sem Shopify write, sem compra, sem fornecedor, sem campanha e sem promessa externa.

## Veredito

**Classificação LK Stock:** `indisponível/sem venda` / `não publicável por estoque`.

Os 8 SKUs/tamanhos vendáveis do produto `Tênis New Balance 740 x Concepts Saignée Verde` têm match exato Shopify↔Tiny, mas todos retornaram saldo `0` no depósito Tiny `LK | CONTROLE ESTOQUE`. Não há correção SKU/Tiny indicada para esta grade; o bloqueio é estoque zerado.

Status de decisão solicitado:

- `publicável`: não
- `não publicável`: sim, por estoque zero
- `precisa correção SKU/Tiny`: não, identidade resolvida por match exato
- `indisponível/sem venda`: sim
- `status de evidência`: `confirmado` por Stock OS local + reconfirmação live Tiny read-only

## Evidência Stock OS local

- Pointer Stock OS: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`
- DB ativa: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_tiny_full_sync_20260626T082006Z.db`
- Pointer atualizado em: `2026-06-26T08:45:52Z`
- Query local em `current_local_stock`: 8/8 SKUs encontrados.
- Status local: todos `CONSULTABLE_LOCAL_RESOLVED_BY_FULL_LIVE_MATCH`, `local_consult_safe=1`, `identity_resolved_safe=1`, `stock_quantity_max_observed=0.0`, `public_availability_safe=0`, `availability_claim_allowed=0`, `needs_live_tiny_confirmation=1`.
- Fonte local: `tiny_full_sync`, freshness `tiny_full_sync_nightly`, `source_observed_at=2026-06-25T12:20:18Z`.

## Reconfirmação live read-only Tiny/Shopify

Comando executado via Doppler profile `lk-stock`, sem imprimir secrets:

`/opt/data/scripts/hermes_doppler.py run --profile lk-stock -- python3 areas/lk/sub-areas/stock/scripts/lk_stock_tiny_shopify_crosswalk.py --sku-prefix U740GP2 --include-parent`

Artefatos live:

- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/reports/lk-stock-nb740-live-crosswalk-20260626T091614Z.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/reports/lk-stock-nb740-live-crosswalk-20260626T091614Z.csv`

Resumo live:

- `generated_at=2026-06-26T09:16:45.126973Z`
- `scope=tiny_shopify_crosswalk_read_only`
- Shopify queries: HTTP 200, `ok=true`, sem GraphQL errors para `sku:U740GP2*` e `U740GP2`
- Tiny queries: 9/9 HTTP 200, Tiny `OK`, `exact_count=1` para parent/base e 8 variantes
- `matched_exact_sku_stock_resolved=9`
- `unresolved_or_blocked=0`
- `shopify_duplicate_sku_blocked=0`
- `tiny_duplicate_exact_code_blocked=0`
- `shopify_variant_tiny_missing=0`
- `tiny_only_shopify_missing=0`
- `writes_externos=0`
- `secrets_printed=false`

## Grade validada

| Tamanho | SKU Shopify | Tiny código | Tiny id | Tiny situação | Depósito | Saldo |
|---:|---|---|---:|---|---|---:|
| 37 | `U740GP2-1` | `U740GP2-1` | `1061338165` | `A` | `LK | CONTROLE ESTOQUE` | 0 |
| 38 | `U740GP2-2` | `U740GP2-2` | `1061338168` | `A` | `LK | CONTROLE ESTOQUE` | 0 |
| 39 | `U740GP2-3` | `U740GP2-3` | `1061338171` | `A` | `LK | CONTROLE ESTOQUE` | 0 |
| 40 | `U740GP2-4` | `U740GP2-4` | `1061338174` | `A` | `LK | CONTROLE ESTOQUE` | 0 |
| 41 | `U740GP2-5` | `U740GP2-5` | `1061338177` | `A` | `LK | CONTROLE ESTOQUE` | 0 |
| 42 | `U740GP2-6` | `U740GP2-6` | `1061338180` | `A` | `LK | CONTROLE ESTOQUE` | 0 |
| 43 | `U740GP2-7` | `U740GP2-7` | `1061338183` | `A` | `LK | CONTROLE ESTOQUE` | 0 |
| 44 | `U740GP2-8` | `U740GP2-8` | `1061338186` | `A` | `LK | CONTROLE ESTOQUE` | 0 |

Observação: o parent/base `U740GP2` também apareceu no crosswalk live com saldo `0`, mas não é variante vendável para decisão de grade pública.

## Recomendação operacional

- Não destravar/publicar o produto ou coleção como pronta entrega neste momento.
- Manter bloqueio de publicabilidade para `/collections/new-balance-740` enquanto não houver entrada Tiny/Stock OS positiva para `U740GP2-*`.
- Não há ajuste SKU/Tiny necessário para os 8 tamanhos; a identidade está resolvida.
- Se Lucas quiser avançar, tratar como decisão comercial separada: compra/reposição com Júlio/fornecedor ou estratégia Shopify para produto arquivado — ambas fora deste escopo e exigem aprovação escopada conforme o caso.

## Guardrails

- Tiny write: `0`
- Shopify write: `0`
- Compra/fornecedor: `0`
- Cliente/campanha/WhatsApp/Klaviyo/GMC: `0`
- Secrets impressos: `0` (`values_printed=false`; `secrets_printed=false`)
- Public availability claim: `0`

## Continuidade

- Reminder OS loop needed: `no` para a validação Stock; a decisão de estoque está fechada com evidência confirmada.
- Owner seguinte: `lk-collection-optimizer`/Mesa COO para manter bloqueio ou pedir novo pacote de aprovação; `lk-shopify` apenas se houver decisão futura de status/publicação; Júlio/Notion apenas se houver decisão futura de compra/reposição.
- Gatilho de revisão: nova entrada/compra Tiny para `U740GP2-*`, novo sync Stock OS com saldo positivo, ou aprovação explícita de Lucas para caminho comercial separado.
