# Stock Cockpit identity remediation — passos 1 a 3 — 2026-06-30

- generated_at_utc: `2026-06-30T14:22:00.203095+00:00`
- values_printed: false
- external_writes_executed: 0

## 1) Resolver 18 SKU duplicados no Shopify

Resultado executado em modo read-only: foi criada fila de decisão com evidência viva Shopify Admin.

Artefatos:

- `areas/lk/sub-areas/stock/reports/stock-cockpit-identity-remediation-1-2-20260630/step1_shopify_duplicate_18_queue.json`
- `areas/lk/sub-areas/stock/reports/stock-cockpit-identity-remediation-1-2-20260630/step1_shopify_duplicate_18_queue.csv`

Status: 18/18 ainda precisam preview de normalização SKU por variante. Nenhuma mutação Shopify foi executada.

## 2) Triar 116 Tiny exact missing

Resultado executado em modo read-only: fila de triagem humana/lk-stock criada com buckets acionáveis.

Buckets:

- `tiny_mapping_or_cadastro_required_no_size_match`: 7
- `tiny_ambiguous_mapping_required`: 91
- `blocked_by_shopify_duplicate_before_tiny_mapping`: 18

Artefatos:

- `areas/lk/sub-areas/stock/reports/stock-cockpit-identity-remediation-1-2-20260630/step2_missing116_triage_queue.json`
- `areas/lk/sub-areas/stock/reports/stock-cockpit-identity-remediation-1-2-20260630/step2_missing116_triage_queue.csv`

Status: 0 linhas `write_ready=true`.

## 3) Wrapper governado Tiny `produto.alterar` / `codigo`

Implementado no `lk-tiny`:

- comando: `lk-tiny produtos codigo-alterar`
- endpoint: `produto.alterar.php`
- operação: `codigo`-only
- padrão: `--dry-run`, sem token e sem write
- live write exige: `--allow-write`, approval escopado, precheck `produto.obter`, bloqueio contra sobrescrever `codigo` não vazio, e payload sem `grade` para evitar normalização indevida de nome/tamanho.

Arquivos alterados:

- `/opt/data/lk-tiny-cli/lk_tiny_cli/cli.py`
- `/opt/data/lk-tiny-cli/tests/test_cli_core.py`
- `/opt/data/lk-tiny-cli/skills/lk-tiny/SKILL.md`

Validação TDD:

- RED inicial: 3 testes falharam como esperado.
- GREEN: `15 passed`.
- Dry-run direto do CLI: `ok=true`, `external_write_performed=false`, `writes_performed=0`.
- Dry-run via broker: ok como dry-run; observação: broker filtra approval metadata, portanto live write fica bloqueado até path broker-compatible ser ajustado/validado.

## Guardrails preservados

- Shopify write: 0
- Tiny write: 0
- Supabase write: 0
- Customer/vendor/campaign contact: 0
- Secrets printed: 0

## Próximo estado

As filas estão prontas para decisão humana/lk-stock/lk-shopify por linha. O wrapper existe para dry-run/preview governado, mas nenhum write deve ser executado até haver linha exata + approval + readback/rollback.
