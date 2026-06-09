# Receipt — Gate C1 piloto manual assistido (`lk-stock`)

Data UTC: 2026-06-08T19:56:08Z
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Status: **piloto manual executado; runtime/cron/Telegram real não ativado**

## Aprovação

Lucas respondeu `APROVO` após a recomendação de próximo passo:

> Gate C1 piloto manual assistido: usar esse runner para produzir fila acionável sob demanda e ajustar falsos positivos/ruído antes de qualquer cron/Telegram real.

Interpretação segura: aprovação para execução manual assistida do runner Gate C na base local atual, sem cron novo, sem Telegram real, sem writes externos.

## Execução

Comando executado:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_gate_c_operational_queue.py --db /opt/data/profiles/lk-stock/state/lk-stock-gate-b.sqlite
```

Resumo JSON:

```json
{
  "status": "actionable",
  "alert_count": 1,
  "writes_externos": 0,
  "telegram_sent": false,
  "runtime_ativado": "Nenhum"
}
```

## Resultado operacional

O piloto manual encontrou 1 alerta acionável local/offline:

```text
LK Stock — decisão necessária

Gatilho: fonte_stale
Produto: Nike Air Max Plus Black
SKU/tamanho: NK-AMP-BLK-40 / 40
Tiny código: não resolvido
Fonte/freshness: stale
Evidência: NÃO CONFIRMADO — SKU/variante/Tiny sem confiança alta; decisão bloqueada até saneamento. Consultar Tiny/fonte viva agora antes de afirmar disponibilidade/ruptura.
Risco: decisão bloqueada por fonte stale
Ação proposta: consultar Tiny/fonte viva agora antes de afirmar disponibilidade/ruptura; não executar write externo
Dono seguinte: lk-stock/Lucas
Writes externos executados: 0
Aprovação necessária: não para diagnóstico; sim para qualquer write externo
```

## Leitura da base local

Resumo SQLite read-only no momento do piloto:

```json
{
  "products": 3,
  "variants": 2,
  "stock_snapshots": 1,
  "sales_velocity": 2,
  "demand_signals": 0,
  "scores": 2,
  "event_ledger": 3,
  "receipts": 1,
  "scores_by_priority": [
    {"priority": "P3", "freshness": "live", "count": 1},
    {"priority": "needs_sku_resolution", "freshness": "stale", "count": 1}
  ]
}
```

## Decisão operacional

- Não há P0/P1 confirmado neste piloto.
- Há bloqueio de decisão por `fonte_stale` + `needs_sku_resolution` no item `NK-AMP-BLK-40`.
- O runner corretamente **não prometeu disponibilidade** e indicou consulta Tiny/fonte viva antes de afirmar ruptura/disponibilidade.
- O alerta é útil como validação do Gate C1: a rotina não ficou ruidosa com inventário; gerou uma única decisão/bloqueio acionável.

## Guardrails preservados

- Cron novo: `0`.
- Telegram real: `0`.
- Tiny write: `0`.
- Shopify write: `0`.
- Compra/transferência/reserva/campanha/fornecedor/cliente: `0`.
- Promessa de disponibilidade/pronta entrega: `0`.
- Runtime ativado: `Nenhum`.

## Próximo passo recomendado

Antes de qualquer Gate C2/cron, corrigir a qualidade da base local/freshness:

1. Rodar reconciliação Gate B/fonte viva para renovar snapshot e mapping.
2. Se persistir `needs_sku_resolution`, gerar packet de saneamento SKU/Tiny/Shopify.
3. Só depois considerar Gate C2 com cron/Telegram real, mediante aprovação separada.
