# Gate B — Base Local Read-only Implementation Plan

> **For Hermes:** executar somente após aprovação escopada de Lucas para implementação local. Webhook/cron produtivos continuam bloqueados até aprovação separada.

**Goal:** Construir a base local read-only do `lk-stock`, com schema versionado, backfill read-only, ingestão webhook em modo seguro e cron diário de reconciliação.

**Architecture:** SQLite local como cache/índice operacional; fontes vivas continuam sendo a verdade para disponibilidade. Toda atualização grava ledger auditável, freshness e receipt quando material. A primeira entrega deve ser local/dry-run, sem runtime público e sem writes externos.

**Tech Stack:** Python 3.13, SQLite, scripts locais em `areas/lk/sub-areas/stock/scripts/`, testes em `areas/lk/sub-areas/stock/evaluation/`, Brain docs em `areas/lk/sub-areas/stock/`.

---

## Guardrails

- Tiny / `LK | CONTROLE ESTOQUE` continua fonte final para disponibilidade.
- Base local não promete estoque sozinha.
- Writes externos: `0`.
- Webhook público, cron ativo, gateway/bot e Vercel/env/secrets exigem aprovação separada.
- Secrets não entram no Brain, logs ou Telegram.
- Telegram só P0/falha/aprovação; OK fica silencioso.

## Entregas do Gate B

1. Schema SQLite versionado.
2. Camada local de leitura/escrita auditável.
3. Backfill inicial em dry-run/read-only.
4. Ingestor de evento webhook em modo fixture/local.
5. Cron diário em dry-run/local.
6. Regras de freshness e stale.
7. Testes offline cobrindo idempotência, freshness e bloqueio de disponibilidade sem fonte viva.
8. Receipt de piloto local.

---

## Status de execução — 2026-06-08T17:37:44Z

Lucas aprovou a implementação local/offline/dry-run e a primeira versão foi criada.

Status por tarefa:

1. **Task 1 — diretórios operacionais:** implementada.
2. **Task 2 — schema SQL versionado:** implementada em `scripts/schema_gate_b.sql`.
3. **Task 3 — módulo de banco local:** implementada em `scripts/stock_local_db.py`; teste criado em `evaluation/test_stock_local_db.py`.
4. **Task 4 — normalizador de eventos:** implementada em `scripts/stock_event_normalizer.py`; teste criado em `evaluation/test_stock_event_normalizer.py`.
5. **Task 5 — ingestão webhook local/dry-run:** implementada em `scripts/stock_webhook_ingest.py`; fixtures e teste criados.
6. **Task 6 — cron diário local/dry-run:** implementada em `scripts/stock_daily_reconcile.py`; teste criado.
7. **Task 7 — score local:** implementada em `scripts/stock_score.py`; teste criado.
8. **Task 8 — consulta A1:** implementada em `scripts/stock_query_a1.py`; teste criado.
9. **Task 9 — approval packet runtime:** implementada em `approval-packets/gate-b-runtime-activation-preview.md`.
10. **Task 10 — verificação final local:** executada em 2026-06-08T17:47:00Z com `python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'`; resultado: 11 testes em 2.937s, `OK`. Também foram executadas verificações manuais de schema, idempotência webhook fixture e freshness/query A1.

Comando canônico de verificação quando runner estiver disponível:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Receipts:

- Planejamento: `areas/lk/sub-areas/stock/receipts/lk-stock-prd-gate-b-implementation-plan-20260608T172027Z.md`
- Implementação local: `areas/lk/sub-areas/stock/receipts/lk-stock-gate-b-local-implementation-20260608T173403Z.md`

Runtime externo ativado: `0`.
Writes externos: `0`.

---

## Task 1 — Criar diretórios operacionais

**Objective:** Preparar estrutura local do Gate B sem tocar runtime.

**Files:**

- Create: `areas/lk/sub-areas/stock/scripts/`
- Create: `areas/lk/sub-areas/stock/evaluation/`
- Create: `areas/lk/sub-areas/stock/data/.gitkeep`

**Steps:**

1. Criar diretórios.
2. Adicionar `.gitkeep` em `data/`.
3. Garantir que bancos `.db` reais fiquem ignorados antes de qualquer dado vivo.

**Verification:**

- `search_files("*", target="files", path="areas/lk/sub-areas/stock", limit=20)` mostra diretórios/arquivos esperados.

---

## Task 2 — Criar schema SQL versionado

**Objective:** Materializar o schema do template Gate B em SQL.

**Files:**

- Create: `areas/lk/sub-areas/stock/scripts/schema_gate_b.sql`

**Required tables:**

- `schema_migrations`
- `products`
- `variants`
- `stock_snapshots`
- `sales_velocity`
- `demand_signals`
- `scores`
- `event_ledger`
- `receipts`

**Required constraints:**

- `event_ledger.idempotency_key` unique.
- `receipts.writes_externos default 0`.
- enum-like `CHECK` constraints for freshness, priority and mapping confidence.

**Verification:**

- Criar banco temporário local com o schema.
- Listar tabelas.
- Verificar que inserir duas vezes o mesmo `idempotency_key` falha.

---

## Task 3 — Criar módulo de banco local

**Objective:** Ter funções mínimas para inicializar DB, aplicar schema e gravar ledger.

**Files:**

- Create: `areas/lk/sub-areas/stock/scripts/stock_local_db.py`
- Test: `areas/lk/sub-areas/stock/evaluation/test_stock_local_db.py`

**Core functions:**

- `init_db(path: str) -> None`
- `record_event(conn, provider, event_type, idempotency_key, payload_hash, status, source_observed_at=None) -> bool`
- `mark_event_failed(conn, idempotency_key, reason) -> None`
- `get_freshness_summary(conn) -> dict`

**Expected behavior:**

- Duplicate idempotency returns false/ignored, not crash in normal ingest path.
- Direct DB constraint still protects uniqueness.

**Verification:**

- Tests pass offline with temporary SQLite DB.

---

## Task 4 — Criar normalizador de eventos local

**Objective:** Normalizar payloads de webhook sem depender de gateway público.

**Files:**

- Create: `areas/lk/sub-areas/stock/scripts/stock_event_normalizer.py`
- Test: `areas/lk/sub-areas/stock/evaluation/test_stock_event_normalizer.py`

**Supported event classes v0:**

- `shopify_order_paid` / venda.
- `shopify_product_update` / produto-variante.
- `tiny_stock_snapshot` / estoque.
- `manual_demand_signal` / sinal humano.

**Output normalized fields:**

- `provider`
- `event_type`
- `source_event_id` nullable
- `idempotency_key`
- `payload_hash`
- `observed_at`
- `entities_affected`

**Verification:**

- Fixtures iguais geram mesmo idempotency key.
- Payloads diferentes geram hashes diferentes.
- Evento sem ID usa hash estável do payload normalizado.

---

## Task 5 — Criar ingestão webhook em modo local/dry-run

**Objective:** Simular webhook sem ativar rota pública.

**Files:**

- Create: `areas/lk/sub-areas/stock/scripts/stock_webhook_ingest.py`
- Test: `areas/lk/sub-areas/stock/evaluation/test_stock_webhook_ingest.py`
- Create: `areas/lk/sub-areas/stock/fixtures/webhook_shopify_order_paid.json`

**Behavior:**

1. Recebe payload JSON local.
2. Normaliza.
3. Registra ledger.
4. Atualiza tabelas afetadas quando houver campos suficientes.
5. Recalcula freshness `live` para registros afetados.
6. Não envia Telegram.
7. Não escreve em Shopify/Tiny.

**Verification:**

- Rodar ingest duas vezes com mesmo fixture; segunda execução fica `ignored` por idempotência.
- Writes externos permanecem `0`.

---

## Task 6 — Criar cron diário em modo dry-run/local

**Objective:** Definir rotina diária sem criar cron real.

**Files:**

- Create: `areas/lk/sub-areas/stock/scripts/stock_daily_reconcile.py`
- Test: `areas/lk/sub-areas/stock/evaluation/test_stock_daily_reconcile.py`

**Behavior v0:**

1. Lê snapshots locais/fixtures.
2. Marca freshness `cron_diario` quando reconciliação é válida.
3. Marca `stale` quando fonte obrigatória falha ou está vencida.
4. Grava `event_ledger` do tipo `daily_reconcile`.
5. Gera receipt local se houver falha, divergência ou P0.

**Verification:**

- Fixture de sucesso marca `cron_diario`.
- Fixture de falha marca `stale`.
- Não há entrega Telegram em OK.

---

## Task 7 — Implementar cálculo de score local

**Objective:** Materializar P0/P1/P2/P3/needs_sku_resolution com explicação auditável.

**Files:**

- Create: `areas/lk/sub-areas/stock/scripts/stock_score.py`
- Test: `areas/lk/sub-areas/stock/evaluation/test_stock_score.py`

**Rules v0:**

- `needs_sku_resolution` se mapping confidence não for `high`.
- `P0` se venda/demanda forte + estoque Tiny zero ou 1 em tamanho relevante.
- `P1` se venda/demanda forte + estoque baixo/disperso.
- `P2` se sinal moderado ou monitoramento.
- `P3` se sem ação.

**Verification:**

- Testes por cenário cobrindo cada prioridade.
- Explicação não vazia em todo score.

---

## Task 8 — Criar comando de consulta A1 sobre base local

**Objective:** Gerar a fila “quais best sellers estão acabando?” usando base local como candidato e Tiny/fonte viva como confirmação declarada.

**Files:**

- Create: `areas/lk/sub-areas/stock/scripts/stock_query_a1.py`
- Test: `areas/lk/sub-areas/stock/evaluation/test_stock_query_a1.py`

**Behavior:**

- Lista P0/P1 primeiro.
- Inclui `needs_sku_resolution` quando bloqueia decisão.
- Omite P2 salvo flag `--include-p2`.
- Exige campo freshness.
- Se freshness `stale`, output deve dizer “não confirmado” e exigir fonte viva.

**Verification:**

- Output segue template `ruptura-best-sellers-a1.md`.
- Nenhuma disponibilidade afirmada com `stale`.

---

## Task 9 — Criar approval packet do Gate B runtime

**Objective:** Preparar o pacote que Lucas aprovaria antes de ativar webhook/cron reais.

**Files:**

- Create: `areas/lk/sub-areas/stock/approval-packets/gate-b-runtime-activation-preview.md`

**Must include:**

- rotas/eventos propostos;
- fontes e escopos read-only;
- nomes de secrets necessários, sem valores;
- cadência do cron diário;
- kill criteria;
- rollback;
- verificação;
- frase exata de aprovação.

**Verification:**

- Packet declara explicitamente que sem aprovação não há ativação.

---

## Task 10 — Rodar verificação final local

**Objective:** Provar que o Gate B está pronto para pedido de aprovação de implementação/runtime.

**Commands:**

- Rodar todos os testes offline.
- Validar schema em banco temporário.
- Rodar fixture webhook duas vezes e confirmar idempotência.
- Rodar cron dry-run sucesso/falha e confirmar freshness.
- Ler approval packet.

**Expected final status:**

- Testes offline passam.
- Runtime externo ativado: `0`.
- Writes externos executados: `0`.
- Receipt local criado.

---

## Próximo gate de aprovação

Para implementar localmente este plano, Lucas deve aprovar explicitamente algo como:

> Aprovo implementar localmente o Gate B do `lk-stock` em modo offline/dry-run, criando scripts, schema SQLite, fixtures e testes locais, sem ativar webhook público, cron real, gateway, bot ou write externo.

Para ativar runtime real depois, será necessário outro approval packet separado.
