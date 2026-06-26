# Gate B2 — guia da worklist operacional local atual — 2026-06-10

## Objetivo

Usar a superfície estável `lk_stock_lookup_current.py` e a visão canônica Gate B2 para orientar saneamento local/humano por handle, lane e prioridade.

Esta worklist é **local/cache only**. Ela não corrige Tiny/Shopify, não promete pronta entrega e não ativa runtime.

## Artefatos atuais

- JSON: `areas/lk/sub-areas/stock/reports/gate-b2-current-operator-worklist-20260610T134734Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/gate-b2-current-operator-worklist-20260610T134734Z.csv`
- Packet MD: `areas/lk/sub-areas/stock/approval-packets/gate-b2-current-operator-worklist-20260610T134734Z.md`
- Fonte: `areas/lk/sub-areas/stock/data/gate_b2_current_pointer.json`

## Totais

- Linhas de worklist por handle/lane/prioridade: `694`
- Linhas bloqueadas para cleanup: `691`
- Linhas resolvidas apenas como referência: `3`
- SKUs canônicos fonte: `903`
- SKUs bloqueados fonte: `897`
- SKUs resolvidos fonte: `6`
- Handles únicos: `558`

## Códigos de ação

- `READONLY_TINY_CODE_INVESTIGATION`: investigar código exato no Tiny em leitura; se não houver match, manter lacuna local/packet.
- `SHOPIFY_DUPLICATE_PROPOSAL`: preparar proposta de deduplicação/correção Shopify por variant/handle; não executar write.
- `TINY_DUPLICATE_PROPOSAL`: preparar proposta de decisão para duplicidade de código exato Tiny; não executar write.
- `TINY_DEPOSIT_MAPPING_CHECK`: verificar depósito `LK | CONTROLE ESTOQUE`/mapeamento em leitura; manter bloqueado se depósito não resolver.
- `NO_WRITE_RESOLVED_CACHE`: usar como mapeamento local interno; reconfirmar Tiny/fonte viva antes de disponibilidade pública.

## Uso operacional

1. Abrir o CSV da worklist e ordenar por:
   - `priority` (`P0_saneamento` antes de `P1_saneamento`, antes de `P2_saneamento`);
   - `sequence` crescente.
2. Para cada item, consultar detalhes com:

```bash
python3 areas/lk/sub-areas/stock/scripts/lk_stock_lookup_current.py "<handle-ou-SKU>" --history --json
```

3. Executar apenas ação local/read-only correspondente ao `recommended_action_code`.
4. Se surgir proposta de alteração Tiny/Shopify, gerar packet de aprovação com diff/rollback/readback. Não executar por inferência.

## Guardrails

- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Cron/webhook/bot/runtime novo: `0`
- Disponibilidade pública/pronta entrega: `0`
- Disponibilidade final exige Tiny/fonte viva consultada no momento.
