# Receipt — LK Stock U204LMMC read-only analysis

- Gerado em: 2026-06-09T09:25:56Z
- Pedido Lucas: exemplo de tênis para ver estoque/analisar (`u204lmmc`)
- Produto resolvido: Tênis New Balance 204L Arid Timberwolf Bege
- Shopify handle: `tenis-new-balance-204l-timberwolf-bege`
- Fonte de estoque: Tiny API `produto.obter.estoque`, depósito `LK | CONTROLE ESTOQUE`
- Fonte de demanda: Shopify Admin GraphQL orders read-only, últimos 90 dias, até 600 pedidos recentes escaneados
- Secrets impressos: false
- Writes externos executados: 0

## Estoque Tiny por tamanho

- 34 / Shopify SKU `U204LMMC-1`: Tiny exact match não resolvido; disponibilidade bloqueada até saneamento SKU.
- 35 / `U204LMMC-2`: saldo Tiny `LK | CONTROLE ESTOQUE` = 3.
- 36 / `U204LMMC-3`: saldo = 0.
- 37 / `U204LMMC-4`: saldo = 0.
- 38 / `U204LMMC-5`: saldo = 1.
- 39 / `U204LMMC-6`: saldo = 0.
- 40 / `U204LMMC-7`: saldo = 0.
- 41 / `U204LMMC-8`: saldo = 1.
- 42 / `U204LMMC-9`: saldo = 0.
- 43 / `U204LMMC-10`: saldo = 0.
- 44 / `U204LMMC-11`: saldo = 0.

## Demanda Shopify lida

Últimos 7 dias:

- 36 / `U204LMMC-3`: 2 unidades vendidas.
- 37 / `U204LMMC-4`: 2 unidades vendidas.

Últimos 30 dias:

- 37 / `U204LMMC-4`: 6 unidades.
- 36 / `U204LMMC-3`: 3 unidades.
- 39 / `U204LMMC-6`: 3 unidades.
- 38 / `U204LMMC-5`: 1 unidade.
- 35 / `U204LMMC-2`: 1 unidade.

Últimos 90 dias:

- 37 / `U204LMMC-4`: 6 unidades.
- 36 / `U204LMMC-3`: 4 unidades.
- 39 / `U204LMMC-6`: 4 unidades.
- 38 / `U204LMMC-5`: 3 unidades.
- 35 / `U204LMMC-2`: 2 unidades.

## Classificação operacional

- P0: 37, 36, 39 — venderam nos últimos 30 dias e estão com saldo Tiny 0.
- P1: 38 — vendeu nos últimos 30/90 dias e tem apenas 1 unidade.
- P2/monitorar: 35 — saldo 3 com baixa demanda recente; 41 — saldo 1 sem demanda capturada no recorte; 40/42/43/44 — sem saldo, mas sem demanda no recorte lido.
- Needs SKU resolution: 34 — Shopify tem `U204LMMC-1`, mas Tiny exact match não resolveu no lookup por código exato.

## Recomendação segura

1. Gerar packet de reposição/transferência para tamanhos 36/37/39 primeiro.
2. Incluir tamanho 38 como reposição conservadora/atenção.
3. Sanear SKU do tamanho 34 antes de qualquer promessa/decisão nele.
4. Não executar compra, transferência, Tiny write, Shopify write ou promessa ao cliente sem aprovação escopada.

## Correção técnica feita durante análise

O script `areas/lk/sub-areas/stock/scripts/lk_stock_sku_mapping_readonly_lookup.py` ainda carregava fallback hardcoded de investigação anterior (`Nike Air Max Plus`), contaminando candidatos em lookup genérico. Foi removido e generalizado para tokens do título atual.

Verificação após correção:

```text
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
Ran 17 tests in 3.494s
OK
```
