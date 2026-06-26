# Receipt — LK Tiny Local Stock DB Phase A

Timestamp: 2026-05-26T17:54:05+00:00
Owner: LK Ops / Atendimento
Executor: Hermes local

## Escopo executado

Implementada a Fase A local do PRD `areas/lk/rotinas/prd-lk-tiny-local-stock-db-event-refresh-2026-05-26.md`.

## Arquivos alterados/criados

- `scripts/lk_tiny_stock_local_db.py`
  - Novo módulo SQLite local para snapshot de estoque Tiny por SKU/tamanho.
  - Tabelas: `stock_by_sku`, `stock_events`, `refresh_queue`.
  - Funções: schema/init, upsert, lookup com frescor, ledger de evento, fila local.

- `scripts/lk_hermes_whatsapp_responder.py`
  - Responder agora consulta `lk_tiny_stock_local.sqlite` antes do cache TTL antigo e antes de Tiny live amplo.
  - Respostas via snapshot local exibem `Última leitura oficial Tiny`.
  - Leituras live Tiny feitas pelo resolver passam a upsertar também na base local.

- `scripts/lk_shopify_tiny_stock_sync_dryrun.py`
  - Processor dry-run agora atualiza a base local quando uma leitura Tiny retorna `status=ok`.
  - Registra evento em `stock_events`.
  - Mantido `write_executed=False`; não escreve em Shopify/Tiny.

- `tests/test_lk_tiny_stock_local_db.py`
  - Testes de schema/upsert/lookup/frescor/event ledger/fila.

- `tests/test_lk_whatsapp_assisted_sale.py`
  - Teste de caminho rápido do responder via Tiny local snapshot antes de cache/live Tiny.

- `scripts/tests/test_lk_shopify_tiny_stock_sync_dryrun.py`
  - Teste de atualização local DB pelo dry-run.
  - Testes isolados em SQLite temporário para não poluir DB operacional.

- `areas/lk/rotinas/implementation-plan-lk-tiny-local-stock-db-phase-a-2026-05-26.md`
  - Implementation Plan TDD/Superpowers salvo antes da execução.

## Verificação executada

1. Syntax check:

```bash
python3 -m py_compile /opt/data/scripts/lk_tiny_stock_local_db.py /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py
```

Resultado: exit 0.

2. Testes unitários principais:

```bash
python3 -m unittest /opt/data/tests/test_lk_tiny_stock_local_db.py /opt/data/tests/test_lk_whatsapp_assisted_sale.py -v
```

Resultado: 9 testes, OK.

3. Testes do dry-run processor:

```bash
python3 - <<'PY'
import importlib.util
p='/opt/data/scripts/tests/test_lk_shopify_tiny_stock_sync_dryrun.py'
spec=importlib.util.spec_from_file_location('dryrun_tests',p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for name in sorted(n for n in dir(m) if n.startswith('test_')):
    getattr(m, name)()
    print(f'{name}: ok')
PY
```

Resultado: 5 testes, OK.

4. Smoke CLI local, sem envio externo:

```bash
python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --ask '@Hermes cliente quer Onitsuka Tiger Mexico 66 38, o que temos?' --stock-only --json-output
```

Resultado: exit 0. Resposta usou `Tiny local snapshot`, exibiu `Última leitura oficial Tiny: 2026-05-26T17:53:50.625507+00:00`, SKU `1183C102250-5`, saldo `3`.

5. Observação de smoke amplo:

- A pergunta `New Balance 9060 38` sem snapshot positivo fresco tentou fallback Tiny live e atingiu timeout de 120s. Isso confirma que a Fase A melhora o caminho quando a base local está populada, mas o universo 9060 ainda depende de alimentar/reconciliar snapshots suficientes ou otimizar timeout/fallback futuro.

## Guardrails preservados

- Sem escrita em Shopify.
- Sem escrita em Tiny.
- Sem criação de webhook.
- Sem criação de cron.
- Sem envio WhatsApp/Telegram externo durante testes.
- Eventos Shopify continuam apenas dry-run e usam saldo absoluto Tiny, nunca delta local.

## Rollback

- Para desativar o caminho novo do responder: remover/ignorar a chamada a `local_stock_db_instock_variants_for_candidates` e manter cache antigo/live Tiny.
- Para desativar atualização por eventos: remover chamada `update_local_stock_db_from_tiny_event` no dry-run processor.
- Para limpar DB local: mover `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/lk_tiny_stock_local.sqlite` para backup. Não afeta Tiny/Shopify.

## Status

Fase A local implementada e verificada em código/testes/smoke local. Runtime do serviço WhatsApp não foi reiniciado nesta execução para evitar alteração operacional sem aprovação explícita de produção.
