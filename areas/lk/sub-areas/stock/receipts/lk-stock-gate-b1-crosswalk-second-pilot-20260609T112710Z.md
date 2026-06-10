# LK Stock — Gate B.1 crosswalk local/offline — segundo piloto controlado

- Data UTC: 2026-06-09T11:27:10Z
- Escopo aprovado: continuar teste local/offline após piloto `U204LMMC`.
- Runtime ativado: Nenhum.
- Webhook/cron/bot ativado: Nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos executados: 0.
- Secrets impressos: não.

## SKUs selecionados

Selecionados via Shopify Admin GraphQL read-only entre produtos ativos com grade real:

- `DD1503118` — Tênis Nike Dunk Low Rose Whisper Rosa.
- `DD1503123` — Tênis Nike Dunk Low Ocean Bliss Azul.
- `BQ6472105` — Tênis Nike Air Jordan 1 Mid Wolf Grey Cinza.
- `DC0774101` — Tênis Nike Air Jordan 1 Low Panda (2023) Preto.

## Artefatos locais

- DB SQLite: `areas/lk/sub-areas/stock/data/gate_b1_crosswalk_second_pilot_20260609T112131Z.db`
- Reports JSON/CSV por SKU em `areas/lk/sub-areas/stock/reports/tiny-shopify-crosswalk-<sku>-gateb1-20260609T112131Z.*`

## Resultado agregado persistido no DB

```json
{
  "total": 40,
  "allowed": 37,
  "blocked": 3,
  "writes_externos": 0
}
```

Por prefixo:

```json
[
  {"prefix":"BQ6472105","total":9,"allowed":9,"blocked":0},
  {"prefix":"DC0774101","total":12,"allowed":9,"blocked":3},
  {"prefix":"DD1503118","total":10,"allowed":10,"blocked":0},
  {"prefix":"DD1503123","total":9,"allowed":9,"blocked":0}
]
```

Issues abertas:

```json
[
  {"sku":"DC0774101","issue_type":"shopify_variant_tiny_missing","severity":"blocked","status":"open"},
  {"sku":"DC0774101-14","issue_type":"tiny_duplicate_exact_code_blocked","severity":"blocked","status":"open"},
  {"sku":"DC0774101-15","issue_type":"tiny_duplicate_exact_code_blocked","severity":"blocked","status":"open"}
]
```

## Observação operacional

O segundo piloto encontrou comportamento útil para saneamento: 3 produtos cruzaram 100% limpos; 1 produto (`DC0774101`) revelou problemas reais de mapeamento no Tiny/Shopify que devem bloquear disponibilidade nos SKUs afetados.

Detalhe `DC0774101`:

- Parent/base `DC0774101`: Shopify possui SKU/base mas Tiny não retornou código exato resolvido.
- `DC0774101-14` tamanho 42: duplicidade de código exato no Tiny; disponibilidade bloqueada.
- `DC0774101-15` tamanho 42.5: duplicidade de código exato no Tiny; disponibilidade bloqueada.

## Correção técnica durante o piloto

Os testes exibiam `ResourceWarning: unclosed database` porque `sqlite3.Connection` usado em `with connect(...)` não fecha por padrão ao sair do context manager. Foi ajustado o helper local `stock_local_db.connect` para retornar uma conexão que fecha no `__exit__`.

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado final:

```text
Ran 20 tests in 6.528s
OK
```

## Decisão recomendada

Gate B.1 está validado para expansão controlada de crosswalk local, mas ainda não para runtime real automático. Próximo passo seguro: rodar um lote maior read-only/local de catálogo ativo e gerar uma fila de saneamento SKU antes de ativar cron/webhook.
