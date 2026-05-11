# LK — Execução correção Tiny `codigo` P0 — 2026-05-11

## Veredito

Execução aprovada por Lucas concluída com sucesso: 2/2 códigos Tiny preenchidos e verificados ao vivo.

## Escopo aprovado

- Preencher apenas `codigo` no Tiny para os 2 itens candidatos P0.
- Não alterar Shopify.
- Não alterar preço, estoque ou produto.

## Resultado

### Tênis New Balance 204L Cortado Marrom — tamanho 39
- Tiny ID: `1069544054`
- `codigo` antes: `[vazio]`
- `codigo` depois: `NB-0254942-39`
- Status write: `OK`
- Status verificação: `OK`
- Alterações não-código detectadas: `0`
- Rollback: restaurar `codigo` para `[vazio]` no Tiny ID `1069544054`

### Tênis Nike x Skims Rift Mesh Archaeo Brown Marrom — tamanho 36
- Tiny ID: `1069544710`
- `codigo` antes: `[vazio]`
- `codigo` depois: `NKS-1065310-36`
- Status write: `OK`
- Status verificação: `OK`
- Alterações não-código detectadas: `0`
- Rollback: restaurar `codigo` para `[vazio]` no Tiny ID `1069544710`

## Observação técnica

A API Tiny `produto.alterar` retornou `OK` mas ignorou payload parcial sem raiz `produtos[].produto`. O formato que efetivamente atualizou e validou foi o layout oficial com `produtos[].produto` aplicado diretamente ao registro da variação filha, incluindo campos obrigatórios existentes e alterando somente `codigo`.

Tentativa via produto pai com `variacoes` foi bloqueada pelo Tiny porque os siblings também estavam com `codigo` vazio: `É necessário informar o código para um produto variação.` Portanto, não foi usada para evitar preencher códigos não aprovados.

## Guardrails verificados

- Sem write em Shopify.
- Sem alteração intencional de preço/estoque/produto.
- Snapshot antes/depois verificou `nome`, `preco`, `preco_promocional`, `unidade`, `origem`, `situacao`, `tipo`, `grade` e `idProdutoPai`; nenhuma alteração não-código foi detectada.
- Secrets usados apenas em processo; não foram impressos nem versionados.

## Próximo passo

- Esses 2 itens deixam o bloqueio de `codigo` Tiny vazio.
- Ainda restam 4 P0 com `codigo` canônico a decidir e 9 P0 sem match Tiny seguro; não mover para sourcing sem resolver.
