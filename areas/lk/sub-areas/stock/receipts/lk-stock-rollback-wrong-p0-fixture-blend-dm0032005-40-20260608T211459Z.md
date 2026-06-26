# Receipt — rollback de P0 indevido por fixture/blend (`DM0032005-40`)

Data UTC: 2026-06-08T21:14:59Z
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Status: **erro reconhecido, recomendação P0/preview superseded e base local saneada**

## O erro

Lucas apontou corretamente que eu incluí um item indevido no blend/recomendação.

Causa raiz: usei como demanda real uma linha da base local originada de fixture/teste:

- Arquivo fixture: `areas/lk/sub-areas/stock/fixtures/webhook_shopify_order_paid.json`
- Linha fixture: `Nike Air Max Plus Black`, SKU `NK-AMP-BLK-40`, quantidade `6`
- Registro na SQLite: `sales_velocity.source = shopify_fixture`

Depois eu resolvi o placeholder para `DM0032005-40` e tratei essa quantidade de fixture como demanda real. Isso gerou um `P0` e um preview de reposição que **não deveria ter sido criado como recomendação operacional**.

## Correção executada

- Criei backup da base antes do rollback/quarentena.
- Restaurei a base para antes da correção SKU e removi da base operacional Gate B/C a linha Air Max derivada de fixture.
- Removidos da SQLite local para esse caso:
  - `sales_velocity`: 1 linha
  - `scores`: 1 linha
  - `variants`: 1 linha
  - `products`: 1 linha
- Inserido receipt local SQLite marcando o rollback.

## Estado após correção

Gate C local:

```json
{
  "status": "ok_silent",
  "alert_count": 0,
  "writes_externos": 0,
  "telegram_sent": false,
  "runtime_ativado": "Nenhum"
}
```

Ou seja: o item saiu da fila operacional/blend.

## Artefatos superseded

Os artefatos abaixo ficam preservados como trilha de auditoria, mas estão **superseded / não usar para execução**:

- `areas/lk/sub-areas/stock/approval-packets/p0-reposicao-transferencia-dm0032005-40-20260608T204715Z.md`
- `areas/lk/sub-areas/stock/approval-packets/preview-reposicao-compra-dm0032005-40-20260608T205324Z.md`
- `areas/lk/sub-areas/stock/receipts/lk-stock-p0-packet-dm0032005-40-20260608T204715Z.md`
- `areas/lk/sub-areas/stock/receipts/lk-stock-preview-reposicao-compra-dm0032005-40-20260608T205324Z.md`

## Regra adicionada

Fixtures, probes, dados `shopify_fixture`, `tiny_fixture`, `GATEB-PROBE-*` e qualquer linha de teste **nunca podem entrar em blend, P0/P1, quantidade de compra ou recomendação operacional**.

Antes de recomendar compra/transferência, a origem de demanda precisa ser venda real/read-only ou fonte comercial viva, não fixture.

## Verificação

```text
Ran 17 tests in 3.826s
OK
```

## Writes externos

- Tiny write: `0`
- Shopify write: `0`
- Compra/fornecedor: `0`
- Comunicação externa: `0`
- Cron/runtime novo: `0`
