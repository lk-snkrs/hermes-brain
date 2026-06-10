# Receipt — Gate B.1 local/offline crosswalk table test U204LMMC

- Gerado em: 2026-06-09T11:15:46Z
- Aprovação Lucas: “Aprovo, vamos primeiro fazer um teste depois se der certo expandimos tá?”
- Escopo interpretado: implementar/testar localmente o Gate B.1 para `U204LMMC`, sem webhook real, sem cron real, sem runtime, sem Tiny/Shopify write.
- Runtime ativado: Nenhum.
- Writes externos: 0.
- Secrets impressos: false.

## Arquivos alterados/criados

- `areas/lk/sub-areas/stock/scripts/schema_gate_b.sql`
  - adiciona migração `gate_b_v1_1_crosswalk`;
  - adiciona `sku_crosswalk`;
  - adiciona `sku_mapping_issues`.
- `areas/lk/sub-areas/stock/scripts/stock_local_db.py`
  - adiciona persistência local do crosswalk;
  - bloqueia duplicidade Tiny em issue aberta;
  - mantém `writes_externos: 0`.
- `areas/lk/sub-areas/stock/scripts/lk_stock_tiny_shopify_crosswalk.py`
  - adiciona `--db` para gravar resultado do crosswalk na SQLite local.
- `areas/lk/sub-areas/stock/evaluation/test_stock_crosswalk_persistence.py`
  - testa schema novo;
  - testa bloqueio de duplicidade Tiny;
  - testa match exato permitido.

## DB local de teste gerado

- `areas/lk/sub-areas/stock/data/gate_b1_crosswalk_u204lmmc_test.db`

## Artefatos do crosswalk gerados no teste

- JSON: `areas/lk/sub-areas/stock/reports/tiny-shopify-crosswalk-u204lmmc-gateb1-20260609T111459Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/tiny-shopify-crosswalk-u204lmmc-gateb1-20260609T111459Z.csv`

## Resultado gravado na tabela local

Resumo SQLite `sku_crosswalk`:

- Total: 12 linhas.
- Permitidas pelo crosswalk: 11.
- Bloqueadas: 1.
- Issue aberta: `U204LMMC-1` / `tiny_duplicate_exact_code_blocked`.

Linha bloqueada:

- SKU: `U204LMMC-1`
- Tamanho: 34
- Status: `tiny_duplicate_exact_code_blocked`
- Confiança: `blocked`
- Disponibilidade permitida: `0`
- Motivo: Tiny retornou dois produtos ativos com código exato `U204LMMC-1`; não afirmar disponibilidade até saneamento.

Linhas resolvidas:

- `U204LMMC` parent/base — saldo 0
- `U204LMMC-2` / 35 — saldo 3
- `U204LMMC-3` / 36 — saldo 0
- `U204LMMC-4` / 37 — saldo 0
- `U204LMMC-5` / 38 — saldo 1
- `U204LMMC-6` / 39 — saldo 0
- `U204LMMC-7` / 40 — saldo 0
- `U204LMMC-8` / 41 — saldo 1
- `U204LMMC-9` / 42 — saldo 0
- `U204LMMC-10` / 43 — saldo 0
- `U204LMMC-11` / 44 — saldo 0

## Comandos de verificação executados

### Testes offline

```text
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 19 tests in 4.561s
OK
```

Observação: o runner imprimiu `ResourceWarning` de conexões SQLite em testes antigos de `stock_webhook_ingest.py`; os testes passaram. Não houve falha funcional do Gate B.1.

### Crosswalk live read-only + persistência local

```text
python3 /opt/data/scripts/hermes_doppler.py run -- python3 areas/lk/sub-areas/stock/scripts/lk_stock_tiny_shopify_crosswalk.py \
  --sku-prefix U204LMMC \
  --include-parent \
  --db areas/lk/sub-areas/stock/data/gate_b1_crosswalk_u204lmmc_test.db \
  --json-out areas/lk/sub-areas/stock/reports/tiny-shopify-crosswalk-u204lmmc-gateb1-20260609T111459Z.json \
  --csv-out areas/lk/sub-areas/stock/reports/tiny-shopify-crosswalk-u204lmmc-gateb1-20260609T111459Z.csv
```

Resultado resumido:

```json
{
  "rows_persisted": 12,
  "blocked_rows": 1,
  "writes_externos": 0
}
```

## Próximo passo se Lucas aprovar expansão

Expandir em lote controlado para mais alguns SKUs/produtos antes de ativar cron/webhook:

1. rodar crosswalk local em 3–5 produtos reais;
2. gerar fila `sku_mapping_issues`;
3. revisar divergências com Lucas/operação;
4. só depois preparar approval packet para sync madrugada e webhook real.

## Bloqueios preservados

- Webhook público: não ativado.
- Cron real/madrugada: não ativado.
- Telegram/bot/runtime: não ativado.
- Tiny write: 0.
- Shopify write: 0.
- Compra/transferência/reserva/fornecedor/cliente: 0.
