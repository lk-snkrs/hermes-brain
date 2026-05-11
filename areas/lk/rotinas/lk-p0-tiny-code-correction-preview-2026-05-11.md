# LK — Preview de correção Tiny `codigo` para P0 residual

Data: 2026-05-11

## Veredito
Preparei o preview para os 6 P0 que tinham algum match Tiny. Só 2 têm `codigo` alvo sugerido com base no SKU Shopify e padrão de siblings; os outros 4 continuam sem alvo seguro e precisam decisão/cadastro de código antes de qualquer write.

## Resumo
- Linhas avaliadas: 6
- Candidatas a write Tiny `codigo` com alvo definido: 2
- Precisam decisão de `codigo` antes de write: 4

## Candidatas a aprovação de write Tiny `codigo`
### Tênis New Balance 204L Cortado Marrom — 39
- Shopify variant ID: `47856402596062`
- SKU Shopify atual: `NB-0254942-39`
- Tiny item/variação alvo: `1069544054` — Tamanho do calçado: 39
- Tiny codigo atual: `[vazio]`
- Tiny codigo proposto: `NB-0254942-39`
- Confiança: `media_alta`
- Rollback: restaurar codigo Tiny para vazio/anterior e revalidar; não mexer Shopify sem autorização separada

### Tênis Nike x Skims Rift Mesh Archaeo Brown Marrom — 36
- Shopify variant ID: `47868839035102`
- SKU Shopify atual: `NKS-1065310-36`
- Tiny item/variação alvo: `1069544710` — Tamanho do calçado: 36
- Tiny codigo atual: `[vazio]`
- Tiny codigo proposto: `NKS-1065310-36`
- Confiança: `media_alta`
- Rollback: restaurar codigo Tiny para vazio/anterior e revalidar; não mexer Shopify sem autorização separada

## Não candidatas ainda: precisam decidir `codigo` alvo
### Camiseta Pace Cotton Code Branca — G/L
- Shopify variant ID: `47512247599326`
- SKU Shopify atual: `[sem SKU]`
- Tiny match: `1065543106` — Tamanho: G/L
- Bloqueio: Shopify também está sem SKU ou Tiny está ambíguo/sem código canônico.
- Próximo passo: Lucas/Júlio definir `codigo` Tiny canônico; depois gero preview de write.

### Rhode Pocket Blush — Sleepy Girl - Soft Mauve
- Shopify variant ID: `46838740648158`
- SKU Shopify atual: `[sem SKU]`
- Tiny match: `1070288342` — Cor: Sleepy Girl - Soft Mauve
- Bloqueio: Shopify também está sem SKU ou Tiny está ambíguo/sem código canônico.
- Próximo passo: Lucas/Júlio definir `codigo` Tiny canônico; depois gero preview de write.

### Camiseta Pace Cotton Code Preta — G/L
- Shopify variant ID: `47512247730398`
- SKU Shopify atual: `[sem SKU]`
- Tiny match: `1065543087` — Tamanho: G/L
- Bloqueio: Shopify também está sem SKU ou Tiny está ambíguo/sem código canônico.
- Próximo passo: Lucas/Júlio definir `codigo` Tiny canônico; depois gero preview de write.

### Camiseta Pace Sketch Yourself Off White — P/S
- Shopify variant ID: `47019131568350`
- SKU Shopify atual: `[sem SKU]`
- Tiny match: `1063954611` — Tamanho: P/S
- Bloqueio: Shopify também está sem SKU ou Tiny está ambíguo/sem código canônico.
- Próximo passo: Lucas/Júlio definir `codigo` Tiny canônico; depois gero preview de write.

## Aprovação necessária
Para executar as 2 candidatas, a aprovação precisa ser explícita, por exemplo:

`aprovo preencher codigo Tiny dos 2 itens candidatos com os SKUs Shopify propostos, sem alterar Shopify, preço, estoque ou produto`

## O que este preview NÃO autoriza
- Não autoriza Shopify write.
- Não autoriza preço/estoque/produto.
- Não autoriza sourcing/compra.
- Não autoriza campanha ou contato com cliente.
