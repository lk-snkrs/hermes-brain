# Receipt — correção local Gate B/C SKU (`NK-AMP-BLK-40` → `DM0032005-40`)

Data UTC: 2026-06-08T20:42:58Z
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Escopo aprovado por Lucas: correção local Gate B/C do placeholder `NK-AMP-BLK-40` para `DM0032005-40`, com update apenas na SQLite/receipt local, sem Tiny/Shopify write.
Status: **executado e verificado**

## Escopo executado

- Base local alterada: `/opt/data/profiles/lk-stock/state/lk-stock-gate-b.sqlite`.
- Backup criado antes do update: `/opt/data/profiles/lk-stock/state/lk-stock-gate-b.backup-before-sku-correction-20260608T204258Z.sqlite`.
- Tabelas locais afetadas: `products`, `variants`, `sales_velocity`, `scores`, `stock_snapshots`, `receipts`, `event_ledger`.
- Writes externos: `0`.
- Tiny write: `0`.
- Shopify write: `0`.
- Telegram real enviado por rotina: `false`.
- Runtime/cron novo ativado: `Nenhum`.

## Antes

- Produto local: `Nike Air Max Plus Black`.
- Variant id local: `1`.
- Provider variant id local: `var-air-max-plus-40`.
- SKU local: `NK-AMP-BLK-40`.
- Tamanho: `40`.
- Tiny código: `null`.
- Mapping confidence: `medium`.
- Score Gate C: `needs_sku_resolution`, score `6.0`, freshness `stale`.

## Depois

- Produto local: `Tênis Air Max Plus Black University Blue Preto`.
- Shopify handle local: `air-max-plus-black-university-blue`.
- Variant id local preservado: `1`.
- Provider variant id local: `44265045295326`.
- SKU local: `DM0032005-40`.
- Tiny código local: `DM0032005-40`.
- Mapping confidence: `high`.
- Snapshot local inserido:
  - Fonte: `tiny_readonly_investigation`.
  - Local: `LK | CONTROLE ESTOQUE`.
  - Quantidade: `0`.
  - Freshness: `fonte_viva_consultada_agora`.
  - Source observed at: `2026-06-08 20:22:54`.
- Score Gate C recalculado: `P0`, score `21.0`, freshness `fonte_viva_consultada_agora`.
- Explicação do score: `Venda/demanda forte com estoque Tiny zerado ou crítico.`

## Verificação SQLite

```json
{
  "variants_old_sku": 0,
  "stock_snapshots_old_sku": 0,
  "sales_velocity_old_sku": 0,
  "scores_old_sku": 0,
  "new_variant": {
    "id": 1,
    "sku": "DM0032005-40",
    "tiny_codigo": "DM0032005-40",
    "mapping_confidence": "high",
    "provider_variant_id": "44265045295326"
  },
  "new_score": {
    "sku": "DM0032005-40",
    "priority": "P0",
    "score": 21.0,
    "freshness": "fonte_viva_consultada_agora",
    "explanation": "Venda/demanda forte com estoque Tiny zerado ou crítico."
  }
}
```

## Gate C manual após correção

```text
LK Stock — decisão necessária

Gatilho: P0
Produto: Tênis Air Max Plus Black University Blue Preto
SKU/tamanho: DM0032005-40 / 40
Tiny código: DM0032005-40
Fonte/freshness: fonte_viva_consultada_agora
Evidência: Venda/demanda forte com estoque Tiny zerado ou crítico.
Risco: venda perdida
Ação proposta: gerar packet de reposição/transferência/compra após confirmação em Tiny/fonte viva; não executar write externo
Dono seguinte: Lucas/lk-ops
Writes externos executados: 0
Aprovação necessária: sim — aprovar qualquer compra/transferência/write antes de executar
```

## Testes

```text
Ran 17 tests in 1.579s
OK
```

## Próximo gate

A correção local removeu o bloqueio `needs_sku_resolution` e transformou o item em alerta operacional `P0` por venda/demanda forte com estoque Tiny zerado/crítico.

Qualquer compra, transferência, write Tiny/Shopify, comunicação externa ou automação/cron Gate C continua exigindo aprovação separada com payload/target/rollback.
