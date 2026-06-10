# Receipt — regra anti-fixture permanente no LK Stock

Data UTC: 2026-06-09T11:24:28Z
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Executor: Hermes Agent default / LC Hermes Central
Status: **concluído — regra promovida para rotina, contrato e teste local**

## Escopo aprovado

Lucas respondeu **Fazer** à Decisão 2/3 da Mesa COO 2026-06-09: transformar o erro de fixture/teste da LK Stock em regra operacional permanente.

## Origem

- Receipt de rollback: `areas/lk/sub-areas/stock/receipts/lk-stock-rollback-wrong-p0-fixture-blend-dm0032005-40-20260608T211459Z.md`.
- Fechamento Ágil: `reports/daily-consolidation/2026-06-09.md`.

## Mudanças executadas

- Criada rotina canônica: `areas/lk/sub-areas/stock/rotinas/anti-fixture-operational-scoring.md`.
- Indexada no `MAPA.md` e `_index.md` da subárea LK Stock e no índice global `empresa/rotinas/_index.md`.
- Atualizados `stock-control-loop-v0.md` e `best-seller-ready-stock-score-v0.md` para aplicar a rotina antes de score/fila.
- Atualizados `AGENTS.md` e `MEMORY.md` do LK Stock com o bloqueio permanente.
- Atualizado `scripts/stock_score.py` para excluir fontes fixture/probe/test antes de consultar:
  - `sales_velocity`;
  - `demand_signals`;
  - `stock_snapshots`.
- Adicionado teste de regressão em `evaluation/test_stock_score.py` para provar que fixture/probe/test não gera P0/P1.
- Ajustado helper de testes Gate C para usar fontes operacionais fictícias (`shopify`/`growth_signal`) em cenários que precisam simular dado válido.

## Regra promovida

`shopify_fixture`, `tiny_fixture`, `manual_fixture`, `GATEB-PROBE-*` e qualquer fonte marcada como fixture/probe/teste não podem alimentar blend, score, P0/P1, quantidade de compra/reposição ou recomendação operacional. Se só houver fonte de teste, a decisão deve bloquear e consultar fonte viva.

## Verificação

Fechamento validado em 2026-06-09:

- `python3 -m unittest areas/lk/sub-areas/stock/evaluation/test_stock_score.py areas/lk/sub-areas/stock/evaluation/test_lk_stock_gate_c_operational_queue.py areas/lk/sub-areas/stock/evaluation/test_stock_webhook_ingest.py` → 10 testes, OK.
- `python3 scripts/brain_health_check.py --json /tmp/brain-health-lk-stock-anti-fixture-20260609.json` → `fail_count=0`, `warn_count=0`.
- `python3 scripts/operational_docs_guard.py --root . --json` → `scanned_files=368`, `fail_count=0`.
- Secret scan focado nas linhas adicionadas do diff → `findings=0`.
- `git diff --check` nos arquivos tocados → OK.

Observação: uma varredura ingênua de arquivo inteiro sinalizou falso positivo pré-existente no índice global por causa do caminho textual `task-router...`; a validação final focou linhas adicionadas/alteradas desta execução e retornou `0` findings.

## Writes externos

- Tiny write: `0`
- Shopify write: `0`
- Compra/fornecedor: `0`
- Cliente/WhatsApp/email/campanha: `0`
- Cron/runtime/gateway: `0`
- Docker/VPS/banco externo: `0`
- Secrets impressos/movidos: `0`

## Rollback

Reverter os arquivos tocados neste receipt:

- `areas/lk/sub-areas/stock/rotinas/anti-fixture-operational-scoring.md`
- `areas/lk/sub-areas/stock/MAPA.md`
- `areas/lk/sub-areas/stock/_index.md`
- `empresa/rotinas/_index.md`
- `areas/lk/sub-areas/stock/rotinas/stock-control-loop-v0.md`
- `areas/lk/sub-areas/stock/rotinas/best-seller-ready-stock-score-v0.md`
- `areas/lk/sub-areas/stock/AGENTS.md`
- `areas/lk/sub-areas/stock/MEMORY.md`
- `areas/lk/sub-areas/stock/scripts/stock_score.py`
- `areas/lk/sub-areas/stock/evaluation/test_stock_score.py`
- `areas/lk/sub-areas/stock/evaluation/test_lk_stock_gate_c_operational_queue.py`

O rollback é local/documental+código local; não exige Tiny/Shopify/GMC/runtime porque nada externo foi alterado.
