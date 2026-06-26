# Approval packet — saneamento SKU/Tiny/Shopify (`NK-AMP-BLK-40`)

Data UTC: 2026-06-08T20:07:19Z
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Status: **packet de decisão — investigação read-only executada; nenhum write externo executado**

## Gatilho

Gate C1/C1+ manual apontou bloqueio persistente:

- Gatilho: `fonte_stale`
- Score/local: `needs_sku_resolution`
- Produto: `Nike Air Max Plus Black`
- SKU/tamanho: `NK-AMP-BLK-40 / 40`
- Tiny código na base local: `não resolvido`
- Freshness: `stale`

## Evidência local

Resumo read-only da SQLite Gate B após reconciliação:

```json
{
  "scores_by_priority": [
    {"priority": "P3", "freshness": "live", "count": 1},
    {"priority": "needs_sku_resolution", "freshness": "stale", "count": 1}
  ],
  "variants": [
    {
      "sku": "NK-AMP-BLK-40",
      "size": "40",
      "tiny_codigo": null,
      "mapping_confidence": "medium",
      "source": "local"
    }
  ]
}
```

O Gate B reconcile executou sem stdout acionável, mas não resolveu o mapping do item `NK-AMP-BLK-40` porque não há snapshot Tiny vivo correspondente na base local.

## Bloqueio operacional

Não é seguro afirmar:

- disponibilidade;
- pronta entrega;
- ruptura real;
- necessidade de compra/reposição/transferência.

Motivo: a base local mostra demanda/variante Shopify, mas não tem `tiny_codigo` confiável nem snapshot Tiny/fonte viva para o SKU/tamanho.

## Ação proposta

Resolver o mapeamento SKU/Tiny/Shopify antes de qualquer decisão de estoque:

1. `lk-stock`/`lk-ops`: consultar Tiny / `LK | CONTROLE ESTOQUE` para localizar produto/tamanho correspondente.
2. `lk-shopify`: validar variant Shopify do SKU `NK-AMP-BLK-40`, tamanho `40`, e correspondência com o código Tiny correto.
3. Se encontrado Tiny correto: registrar snapshot read-only/ingest autorizado no Gate B e recalcular score.
4. Se não encontrado: abrir divergência SKU para correção operacional antes de qualquer compra/reposição.

## Donos sugeridos

- Primário: `lk-stock`.
- Apoio Tiny/processo físico: `lk-ops`.
- Apoio variant/SKU Shopify: `lk-shopify`.
- Decisão final se houver reposição/compra: Lucas.

## Guardrails

- Tiny write: `0`.
- Shopify write: `0`.
- Compra/transferência/reserva/cliente/fornecedor/campanha: `0`.
- Promessa de disponibilidade/pronta entrega: `0`.
- Este packet é read-only e não autoriza mutation.

## Resultado da investigação read-only — 2026-06-08T20:22:54Z

Escopo aprovado por Lucas e executado sem write externo.

### `NK-AMP-BLK-40`

```json
{
  "status": "shopify_variant_not_resolved",
  "confidence": "blocked",
  "shopify_exact_sku_candidates": 0,
  "tiny_exact_codigo_candidates": 0,
  "resolved_tiny_codigo": null,
  "resolved_tiny_id": null,
  "availability_claim_allowed": false,
  "writes_externos": 0
}
```

Veredito: `NK-AMP-BLK-40` não é SKU/código operacional confiável no Shopify/Tiny; deve ser tratado como placeholder local incorreto.

### Candidato canônico provável

Se o produto pretendido era **Air Max Plus Black University Blue, tamanho 40**, a consulta cruzada read-only encontrou match exato:

- Shopify produto: `Tênis Air Max Plus Black University Blue Preto`.
- Shopify handle: `air-max-plus-black-university-blue`.
- Shopify status: `ACTIVE`.
- Shopify SKU: `DM0032005-40`.
- Shopify variant legacy ID: `44265045295326`.
- Tiny código: `DM0032005-40`.
- Tiny id: `937674228`.
- Tiny depósito `LK | CONTROLE ESTOQUE`: saldo `0.0`, `desconsiderar: N`.

Conclusão: para esse candidato específico, há fonte Tiny viva e o saldo oficial está zerado no tamanho 40. Nenhum write Tiny/Shopify/base local foi executado.

## Aprovação necessária

Para corrigir **apenas a base local/fila Gate B/C** substituindo o placeholder `NK-AMP-BLK-40` pelo mapping `DM0032005-40` e recalcular a fila:

> Aprovo correção local Gate B/C do placeholder `NK-AMP-BLK-40` para `DM0032005-40`, com update apenas na SQLite/receipt local, sem Tiny/Shopify write.

Para qualquer correção em Tiny/Shopify, compra, transferência ou comunicação externa, será necessária aprovação separada com payload/target/rollback.
