# Receipt — Crosswalk Tiny↔Shopify U204LMMC

- Gerado em: 2026-06-09T10:47:09Z
- Pedido Lucas: primeira prioridade é o cruzamento perfeito entre Tiny e Shopify.
- Escopo: read-only/local.
- Produto piloto: `U204LMMC` / Tênis New Balance 204L Arid Timberwolf Bege.
- Fonte Shopify: Admin GraphQL `productVariants` por prefixo `U204LMMC*`.
- Fonte Tiny: API `produtos.pesquisa` por código exato + `produto.obter.estoque`.
- Depósito Tiny oficial: `LK | CONTROLE ESTOQUE`.
- Secrets impressos: false.
- Writes externos executados: 0.

## Artefatos gerados

- Script: `areas/lk/sub-areas/stock/scripts/lk_stock_tiny_shopify_crosswalk.py`
- JSON: `areas/lk/sub-areas/stock/reports/tiny-shopify-crosswalk-u204lmmc-20260609T104627Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/tiny-shopify-crosswalk-u204lmmc-20260609T104627Z.csv`

## Resultado do piloto

Resumo do crosswalk:

- Linhas totais verificadas: 12.
- Matches exatos Shopify SKU ↔ Tiny código com estoque resolvido: 11.
- Duplicidade de código exato no Tiny bloqueada: 1.
- Shopify sem Tiny: 0 após retry/backoff.
- Tiny sem Shopify: 0.
- Disponibilidade bloqueada: 1 linha.

## Divergência crítica encontrada

Tamanho 34 / Shopify `U204LMMC-1`:

- Shopify variant: `gid://shopify/ProductVariant/47557591105758`.
- Tiny retornou 2 produtos ativos com código exato `U204LMMC-1`:
  - Tiny id `1065903206`, saldo `LK | CONTROLE ESTOQUE` = 1.
  - Tiny id `1071214192`, saldo `LK | CONTROLE ESTOQUE` = 2.
- Classificação: `tiny_duplicate_exact_code_blocked`.
- Decisão segura: não afirmar disponibilidade final desse tamanho até saneamento da duplicidade no Tiny.

## Estoque resolvido nos tamanhos sem bloqueio

- 35 / `U204LMMC-2`: 3.
- 36 / `U204LMMC-3`: 0.
- 37 / `U204LMMC-4`: 0.
- 38 / `U204LMMC-5`: 1.
- 39 / `U204LMMC-6`: 0.
- 40 / `U204LMMC-7`: 0.
- 41 / `U204LMMC-8`: 1.
- 42 / `U204LMMC-9`: 0.
- 43 / `U204LMMC-10`: 0.
- 44 / `U204LMMC-11`: 0.

## Validação

Comando executado:

```text
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 17 tests in 1.842s
OK
```

## Próximo gate recomendado

Antes de usar qualquer fila P0/P1 como verdade operacional ampla, rodar o crosswalk por produto/prefixo e produzir uma fila de saneamento:

1. `matched_exact_sku_stock_resolved` pode entrar na análise de estoque.
2. `tiny_duplicate_exact_code_blocked` precisa saneamento Tiny/operacional.
3. `shopify_variant_tiny_missing` precisa saneamento SKU/cadastro.
4. `tiny_only_shopify_missing` precisa decisão se é produto físico sem superfície Shopify ou divergência de cadastro.

Bloqueios mantidos:

- Tiny write: 0.
- Shopify write: 0.
- Compra/transferência/reserva: 0.
- Cron/runtime novo: 0.
