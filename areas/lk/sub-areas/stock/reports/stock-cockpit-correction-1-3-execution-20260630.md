# Stock Cockpit — correção 1 a 3 — 2026-06-30

- generated_at_utc: `2026-06-30T14:37:14.521045+00:00`
- values_printed: false
- external_writes_executed: 0

## Pedido

Lucas: "Corrigir do 1 ao 3".

Interpretação operacional segura:

1. Corrigir os 18 SKU duplicados Shopify quando houver alvo determinístico.
2. Corrigir/encaminhar os 116 Tiny exact missing quando houver mapeamento determinístico.
3. Corrigir o wrapper governado Tiny `produto.alterar` / `codigo` para path broker-compatible.

## Resultado executivo

| Item | Resultado | Writes externos |
|---|---|---:|
| 1 — 18 Shopify SKU duplicados | Bloqueado para write: 18/18 sem target determinístico; fila read-only preservada | 0 |
| 2 — 116 Tiny exact missing | Bloqueado para write: 116/116 sem `write_ready`; filas por bucket preservadas | 0 |
| 3 — Wrapper Tiny `produto.alterar`/`codigo` | Corrigido: broker exporta approval para env e `lk-tiny` aceita fallback | 0 |

## Evidência item 1

Arquivo:

- `areas/lk/sub-areas/stock/reports/stock-cockpit-identity-remediation-1-2-20260630/step1_shopify_duplicate_18_queue.json`

Readback determinístico:

- `shopify_duplicate_rows`: 18
- `shopify_duplicate_write_ready`: 0

Conclusão: não há correção Shopify segura sem decidir, por variante, qual SKU permanece e qual SKU novo/blank deve entrar nos duplicados. Isso é write de catálogo e precisa preview SKU-only por linha.

## Evidência item 2

Arquivo:

- `areas/lk/sub-areas/stock/reports/stock-cockpit-identity-remediation-1-2-20260630/step2_missing116_triage_queue.json`

Readback determinístico:

- `missing_rows`: 116
- `missing_write_ready`: 0
- buckets:
  - `tiny_mapping_or_cadastro_required_no_size_match`: 7
  - `tiny_ambiguous_mapping_required`: 91
  - `blocked_by_shopify_duplicate_before_tiny_mapping`: 18

Conclusão: não existe `Tiny produto.alterar` seguro sem o humano escolher o Tiny ID/código canônico ou confirmar cadastro novo.

## Correção item 3 — broker + lk-tiny

Alterações locais:

- `/opt/data/scripts/hermes_cli_run.py`
  - `--approval` continua removido do argv do child CLI.
  - approval agora é exportado para `HERMES_INTEGRATION_APPROVAL` no env do child CLI.
- `/opt/data/scripts/tests/test_hermes_cli_run.py`
  - novo teste garante que `lk-tiny` recebe approval via env e não por argv.
- `/opt/data/lk-tiny-cli/lk_tiny_cli/cli.py`
  - `approval_value()` lê `--approval`, `HERMES_INTEGRATION_APPROVAL` e `HERMES_APPROVAL_PACKET`.
  - `produtos codigo-alterar` e `estoque balanco` usam esse fallback.
- `/opt/data/lk-tiny-cli/tests/test_cli_core.py`
  - novo teste cobre approval via env para o broker path.
- `/opt/data/lk-tiny-cli/skills/lk-tiny/SKILL.md`
- `/opt/data/skills/devops/hermes-central-integration-auth-broker/references/broker-smoke-for-new-cli-write-commands-20260630.md`

## Verificação já executada antes deste report

- Broker unit tests: `7 tests OK`.
- `lk-tiny` tests: `16 passed`.
- `py_compile`: OK.
- Broker real dry-run:
  - `approval_present=true`
  - `external_write_performed=false`
  - `writes_performed=0`
  - `values_printed=false`

## Próximo passo operacional seguro

Para realmente zerar os 18/116 em produção:

1. `lk-shopify` precisa gerar preview SKU-only por variante dos 18 duplicados, com rollback antigo por variant ID.
2. `lk-stock`/Júlio/Lucas precisa escolher o Tiny ID/código canônico das 98 ambíguas/7 sem match ou marcar cadastro novo.
3. Aí sim usar `lk-tiny produtos codigo-alterar --dry-run` por lote; live write só com `--allow-write`, approval escopado e readback.
