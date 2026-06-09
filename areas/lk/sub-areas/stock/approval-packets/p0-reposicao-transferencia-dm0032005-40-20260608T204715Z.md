# Approval packet P0 — reposição/transferência/compra (`DM0032005-40`)

Data UTC: 2026-06-08T20:47:15Z
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Status: **SUPERSEDED — não usar para execução. Lucas apontou que a demanda usada vinha de fixture/teste, não de blend/venda real. Ver rollback `areas/lk/sub-areas/stock/receipts/lk-stock-rollback-wrong-p0-fixture-blend-dm0032005-40-20260608T211459Z.md`. Nenhum write externo foi executado.**

## Gatilho

Após saneamento local do placeholder `NK-AMP-BLK-40`, o Gate C recalculado classificou o item como `P0`.

- Produto: `Tênis Air Max Plus Black University Blue Preto`
- SKU/tamanho: `DM0032005-40 / 40`
- Tiny código: `DM0032005-40`
- Tiny id: `937674228`
- Shopify variant legacy ID: `44265045295326`
- Fonte/freshness: `fonte_viva_consultada_agora`
- Risco: **venda perdida**

## Fonte viva consultada agora

Consulta read-only executada em 2026-06-08T20:46:20Z via Doppler runtime env, sem imprimir secrets.

- Shopify Admin GraphQL: `200`, sem erros, 1 candidato exato por SKU.
- Tiny API read-only: 1 candidato exato por código.
- Depósito avaliado: `LK | CONTROLE ESTOQUE`.
- Saldo Tiny oficial no depósito: `0.0`.
- `desconsiderar`: `N`.
- `availability_claim_allowed`: `true` somente porque Tiny/fonte viva foi consultada.
- Writes externos: `0`.

## Evidência operacional local

- Vendas/sinal 30d no índice local: `6.0` unidades.
- Estoque Tiny oficial reconfirmado: `0`.
- Score Gate C recalculado: `21.0`.
- Prioridade: `P0`.
- Explicação: `Venda/demanda forte com estoque Tiny zerado ou crítico.`

## Decisão recomendada

Recomendação do `lk-stock`: **abrir decisão de abastecimento para o tamanho 40**.

Ordem segura de ação:

1. Verificar se há par físico em outra origem/loja/deposito interno para transferência para `LK | CONTROLE ESTOQUE`.
2. Se não houver transferência viável, avaliar compra/reposição com fornecedor.
3. Só depois de aprovação explícita, executar qualquer write em Tiny/Shopify, compra, reserva ou comunicação externa.

## Aprovação necessária

Para eu avançar para ação externa, preciso de uma aprovação escopada. Opções:

### Opção A — somente preparar pedido/contato, sem enviar

```text
Aprovo preparar preview de reposição/compra para DM0032005-40, sem enviar e sem write Tiny/Shopify.
```

### Opção B — investigar transferência interna read-only

```text
Aprovo investigar fontes internas/depósitos para transferência do DM0032005-40, read-only, sem reserva e sem write Tiny/Shopify.
```

### Opção C — executar uma ação específica

Use só se já quiser autorizar execução real:

```text
Aprovo [ação exata] para DM0032005-40, destino LK | CONTROLE ESTOQUE, quantidade [X], com [canal/sistema], e rollback/receipt.
```

## Guardrails

- Não prometi pronta entrega ao cliente.
- Não reservei produto.
- Não comprei.
- Não transferi.
- Não alterei Tiny.
- Não alterei Shopify.
- Não criei cron/runtime Gate C.
- Este packet é local/documental.

## Receipt relacionado

- Correção local SKU: `areas/lk/sub-areas/stock/receipts/lk-stock-local-sku-correction-nk-amp-blk-40-to-dm0032005-40-20260608T204258Z.md`
