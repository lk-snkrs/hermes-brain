# Receipt — Gate C0 local/offline implementation (`lk-stock`)

Data UTC: 2026-06-08T19:53:06Z
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Status: **implementado e testado local/offline; runtime/cron Gate C não ativado**

## Aprovação

Lucas aprovou explicitamente:

> Aprovo Gate C0: implementar e testar runner operacional read-only local/offline, sem cron novo, sem Telegram real exceto stdout de teste, sem writes externos.

## Artefatos criados

- Runner local/offline:
  - `areas/lk/sub-areas/stock/scripts/lk_stock_gate_c_operational_queue.py`
- Testes Gate C0:
  - `areas/lk/sub-areas/stock/evaluation/test_lk_stock_gate_c_operational_queue.py`

## Contrato implementado

O runner lê a base local Gate B e produz stdout somente quando há exceção acionável:

- `P0`;
- `P1`;
- `needs_sku_resolution`;
- `fonte_stale`/falha de freshness.

Quando não há gatilho, retorna OK silencioso (`stdout == ""`).

Todo output material inclui:

- gatilho;
- produto;
- SKU/tamanho;
- Tiny código quando resolvido;
- fonte/freshness;
- evidência;
- risco;
- ação proposta;
- dono seguinte;
- `Writes externos executados: 0`;
- aprovação necessária.

## Guardrails preservados

- Cron novo: `0`.
- Telegram real: `0`.
- Tiny write: `0`.
- Shopify write: `0`.
- Compra/transferência/reserva/campanha/fornecedor/cliente: `0`.
- Promessa de disponibilidade/pronta entrega: `0`.
- Se freshness estiver `stale`, output diz `NÃO CONFIRMADO` e manda consultar Tiny/fonte viva antes de afirmar disponibilidade/ruptura.

## TDD / evidência

### RED

Antes de criar o runner, o teste Gate C0 foi executado e falhou como esperado porque o módulo ainda não existia:

```text
ModuleNotFoundError: No module named 'lk_stock_gate_c_operational_queue'
FAILED (errors=1)
```

### GREEN focado

Após implementar o runner:

```text
python3 -m unittest areas/lk/sub-areas/stock/evaluation/test_lk_stock_gate_c_operational_queue.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.556s

OK
```

Cobertura dos testes:

1. OK silencioso sem P0/P1/SKU/falha.
2. P0 gera output acionável sem promessa de disponibilidade.
3. P1 gera output acionável.
4. `needs_sku_resolution` gera handoff para saneamento SKU.
5. `stale` gera alerta de fonte e `NÃO CONFIRMADO`.
6. Output contém campos contratuais e `Writes externos executados: 0`.

## Dry-run manual na base local atual

Comando:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_gate_c_operational_queue.py --db /opt/data/profiles/lk-stock/state/lk-stock-gate-b.sqlite
```

Resultado: gerou 1 alerta local/offline acionável, sem envio Telegram real:

```text
Gatilho: fonte_stale
Produto: Nike Air Max Plus Black
SKU/tamanho: NK-AMP-BLK-40 / 40
Fonte/freshness: stale
Evidência: NÃO CONFIRMADO — SKU/variante/Tiny sem confiança alta; decisão bloqueada até saneamento. Consultar Tiny/fonte viva agora antes de afirmar disponibilidade/ruptura.
Writes externos executados: 0
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

## Verificação final

Suíte completa local Gate B/C após criação do receipt:

```text
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
.................
----------------------------------------------------------------------
Ran 17 tests in 9.533s

OK
```

Dry-run JSON final na base local atual:

```json
{
  "status": "actionable",
  "alert_count": 1,
  "writes_externos": 0,
  "telegram_sent": false,
  "runtime_ativado": "Nenhum"
}
```

## Próximo gate

Gate C0 está pronto local/offline. Para ativar rotina real/cron/Telegram, ainda precisa de aprovação separada de Gate C1/C2 com escopo, kill switch e receipt.
