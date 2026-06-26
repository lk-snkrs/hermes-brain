# Audit Superpowers — Dashboard Estoque LK

- Gerado em: 2026-06-23 14:27:39 UTC
- Escopo: `estoque.lkskrs.online` / repo `LK-Estoque-Web-inicial` / Stock OS DB local
- Modo: read-only audit; sem deploy e sem alterações produtivas
- Skills aplicadas: `superpowers`, `lk-stock`, `verification-before-completion`, `doppler-secrets-operations`

## Evidência coletada

### Fonte/DB Stock OS

- Pointer: `areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`
- Stage: `tiny_full_sync_nightly_completed`
- DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_tiny_full_sync_20260623T132043Z.db`
- DB size observado: ~128.83 MB
- Último Tiny full sync: `20260623T132043Z`, status `ok`, `rows_scanned=975`, `rows_updated=975`, `rows_failed=0`, `rows_skipped=0`
- Guardrails DB: `public_availability_safe=0`, `availability_claim_allowed=0`

### Métricas DB atual

- `current_local_stock`: 12.592 linhas
- Estoque positivo: 874 linhas / 1.245 unidades / 428 produtos únicos positivos por handle/title/SKU
- Zero: 11.679 linhas
- Negativo: 39 linhas
- Consultável + identidade resolvida: 11.692 linhas
- Consultável + identidade pendente: 549 linhas
- Bloqueado/local não consultável: 351 linhas
- `current_stock_scored`: 903 linhas
  - P0: 4
  - P1: 13
  - P2: 1
  - P3: 885
- `demand_signals_stock_os`: 352 linhas; `units_signal=3486`; `store_units_signal=1444`

### Produção / container

- `https://estoque.lkskrs.online/health`: HTTP 200
- `/api/estoque/summary` autenticado via env do container: HTTP 200
- Container `lk-estoque-web`: running; image `lk-estoque-web-web`; rede `lk-estoque-web_default`
- Autenticação: `DASHBOARD_PASSWORD` presente no container; valor não impresso (`values_printed=false`)

### Testes/verificação

- Repo `/opt/data/worktrees/lk-stock/LK-Estoque-Web-inicial`
- `npm test`: 36/36 pass
- Adapter Python: `python3 -m unittest areas/lk/sub-areas/stock/evaluation/test_stock_api_adapter.py`: 7/7 pass
- Impeccable detector: `npx --yes impeccable detect --json src/public src/index.js` retornou `[]`

## Achados principais

### 1. Dashboard ainda está truncando a base de estoque

Produção `/api/estoque/summary` retornou:

- `stock_os_total_count=12592`
- `stock_os_result_count=10000`
- `stock_os_truncated=true`
- `total=10000`

Impacto: o painel não enxerga 2.592 linhas da Stock OS DB na carga principal. Isso distorce contagem, filtros, cards, ruptura, grade e qualquer cockpit operacional baseado no feed.

### 2. Fila operacional do dashboard não reflete a fila de decisão real do DB

DB `current_stock_scored` mostra:

- P0 real de decisão: 4
- P1 real: 13

Mas o dashboard, via adapter atual + normalização, mostra:

- P0: 21
- P1: 795
- P2: 1852
- P3: 7332

Causa provável: o adapter `/api/lk-stock/lookup` emite `priority` vindo de saneamento (`P0_saneamento`, `P1_saneamento`, etc.) e não emite/mescla `action_priority`, `action_lane`, `operational_score`, `units_signal`, `revenue_signal` de `current_stock_scored`. O frontend normaliza `priority` como se fosse fila operacional. Resultado: saneamento vira falsa fila de decisão, e a fila real P0/P1 de compra/reposição fica mascarada.

### 3. Camada demanda × estoque está quase cega no universo Estoque

No feed processado pelo dashboard:

- `resultsWithOperationalScore=0`
- `resultsWithDemand=0`
- `demandNoStock=0`
- `highDemandLowStock=0`

Mas o DB tem `demand_signals_stock_os` e `current_stock_scored` com sinais reais. Ou seja: a informação existe, mas não chega ao contrato consumido pelo dashboard de estoque.

### 4. Thumbnails não estão no contrato Stock OS do adapter

No feed processado:

- `resultsWithThumb=0`

O site ainda tem fallback `/api/product-thumbnail?handle=...`, mas o contrato de estoque não entrega `thumbnail_url`. Isso deixa a UI dependente de fallback público por card, mais lento/frágil, e enfraquece busca visual para vendedor.

### 5. Endpoint principal é pesado demais para carga inicial

Produção `/api/estoque` retornou `Content-Length: 7.807.903` bytes para 10.000 linhas e ainda truncado. O adapter completo com 10.000 resultados tinha ~12 MB. Para mobile/Telegram browser e operação de loja, o painel precisa carregar primeiro resumo/cockpit e buscar detalhe sob demanda.

### 6. Vendas já tem cockpit acionável melhor que Estoque puro

`/api/vendas/executive-summary` em produção retornou:

- status `attention`
- freshness `ok`
- `generated_at=2026-06-23T05:41:41.214880Z`
- `last_order_at=2026-06-23T03:26:48Z`
- `action_counts`: P0 31, P1 18, P2 1, total 50

Isso reforça que a direção correta é unificar a primeira viewport como “Hoje no estoque”: filas de decisão cruzando estoque + venda + grade + identidade, e não uma lista de inventário filtrada por marca.

### 7. Saúde/guardrails estão bons

Pontos positivos verificados:

- Tiny write: 0
- Shopify write: 0
- Writes externos: 0
- Public availability: 0
- `npm test`: 36/36 pass
- Teste adapter: 7/7 pass
- Impeccable detector: clean (`[]`)
- `health`: HTTP 200

## Recomendações P0/P1/P2

### P0 — Corrigir contrato de dados antes de qualquer polimento visual

1. Resolver truncamento: permitir feed completo ou, melhor, trocar a carga inicial por summary/detail paginado.
2. Adapter deve mesclar `current_local_stock` + `current_stock_scored` por SKU/handle e emitir:
   - `action_priority`
   - `action_lane`
   - `operational_score`
   - `units_signal`
   - `revenue_signal`
   - `store_units_signal`
3. Separar claramente:
   - `sanitation_priority` / `identity_priority`
   - `action_priority` / `decision_priority`

Critério de aceite P0:

- `/api/estoque/summary` não truncar sem aviso bloqueante, ou carregar só summary real sem depender do feed inteiro.
- Dashboard P0/P1 bater com `current_stock_scored`: P0 4, P1 13 no snapshot atual, salvo mudança de DB.
- `demandNoStock` e `highDemandLowStock` deixarem de ser zero quando houver sinais reais.

### P1 — Transformar a primeira tela em cockpit de controle

1. Primeira viewport: `Hoje no estoque`, com:
   - P0 decisão agora
   - P1 identidade bloqueando decisão
   - grade quebrada
   - baixo estoque
   - dados stale/partial
2. Sidebar de marca deve continuar como filtro contextual, não navegação principal.
3. Mostrar “atendimento” separado de “decisão de compra/reposição”.

Critério de aceite P1:

- Operador abre o painel e vê imediatamente “o que fazer hoje”.
- Vendedor consegue buscar produto disponível sem ver fila de compra.
- Compra/reposição nunca vira promessa pública nem compra automática.

### P1 — Enriquecer contrato com imagem/cache

Emitir `thumbnail_url` estável no adapter/read model, em vez de depender só do fallback por handle.

Critério de aceite:

- `resultsWithThumb` > 0 e crescendo por enriquecimento local/cache.
- Cards principais mostram imagem sem chamadas públicas por card na carga inicial.

### P2 — Deltas/movimento desde última sync

Derivar “mudou desde o último sync” de `tiny_full_sync_item_ledger`, não de campos `previous_estoque` ausentes no payload.

Critério de aceite:

- Entrou estoque
- Saiu estoque
- Foi a zero
- Voltou positivo
- Negativo/anômalo
- Sync stale/partial

## Veredito

O dashboard está seguro e testado, mas ainda não é plenamente um sistema de controle de estoque. A base Stock OS está rica e fresca; o gargalo está no contrato adapter → dashboard: truncamento, falta de merge com score/demanda e confusão entre prioridade de saneamento e prioridade de decisão.

Próximo passo recomendado: uma correção P0 no adapter/API para entregar summary/detail operacional e mesclar `current_stock_scored`, sem deploy externo até aprovação escopada.

## Writes

- Tiny write: 0
- Shopify write: 0
- Notion write: 0
- Compra/fornecedor: 0
- Deploy/prod change: 0
- Public availability promise: 0
