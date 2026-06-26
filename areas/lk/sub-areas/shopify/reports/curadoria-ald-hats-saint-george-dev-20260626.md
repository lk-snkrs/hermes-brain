# Receipt — DEV Curadoria LK bonés ALD no PDP Saint George Bege/Marrom

Data: 2026-06-26  
Profile: `lk-shopify`  
Escopo aprovado por Lucas: `Aprovo DEV Curadoria LK bonés ALD no PDP do Saint George Bege/Marrom, sem Production merge.`

## Superfície

- DEV theme: `155065450718`
- PDP alvo: `/products/bone-aime-leon-dore-saint-george-logo-hat-bege-marrom`
- Classe/padrão: `.lk-variante`
- Arquivos alterados no DEV:
  - `snippets/lk-variante-ald-hats-saint-george-20260626.liquid`
  - `sections/lk-pdp.liquid`

## Seleção de produtos

Fonte: Shopify Admin read-only. Não houve consulta de estoque/disponibilidade.

Grupo renderizado no PDP alvo, excluindo o produto atual:

1. `bone-aime-leon-dore-saint-george-logo-hat-bege-verde` — Saint George Verde
2. `bone-aime-leon-dore-micro-logo-hat-bege-verde` — Micro Logo Bege
3. `bone-aime-leon-dore-porsche-nylon-logo-jet-black-preto` — Porsche Black
4. `bone-aime-leon-dore-unisphere-verde` — Unisphere Verde
5. `bone-aime-leon-dore-washed-script-plaza-taupe-bege` — Washed Script Taupe

## Readback DEV

- Snippet PUT: `200`
- Section PUT: `200`
- Snippet antes: `404` / novo asset
- Section SHA antes: `99bddffce5cd`
- Section SHA alvo/readback: `61846f6f20ef`
- Snippet SHA alvo/readback: `fb97de5d06ad`
- `values_printed=false`

## QA público DEV

URL testada:

`https://lksneakers.com.br/products/bone-aime-leon-dore-saint-george-logo-hat-bege-marrom?preview_theme_id=155065450718`

Resultados:

- HTTP `200`
- Liquid errors: `0`
- `data-lk-variante="ald-hats-saint-george-20260626"`: presente
- `Curadoria LK`: presente
- Título: `Outros bonés`
- Links sugeridos: `5`
- Link para produto atual dentro do bloco: `0`
- Browser/CDP: bloco presente, dimensões mobile aproximadas `389x155`, 5 itens com imagem, JS exceptions `0`

## Backup / rollback

Backups DEV:

`/opt/data/profiles/lk-shopify/workdirs/curadoria-ald-hats-saint-george-20260626/backups/`

Rollback DEV:

1. Remover render em `sections/lk-pdp.liquid`:
   - `{%- render 'lk-variante-ald-hats-saint-george-20260626', product: product -%}`
2. Restaurar section a partir de `dev_before_sections__lk-pdp.liquid`.
3. Opcionalmente remover o snippet novo do DEV.

## Limites

- Sem Production merge.
- Sem alteração em produto, preço, estoque, metafield, Tiny, GMC, Klaviyo ou checkout.
- Sem promessa de disponibilidade; a seleção é editorial/relacional.

## Aprendizado propagado

Skill atualizada: `lk-shopify-theme-cro` agora inclui padrão de Curadoria LK para famílias de acessórios usando `.lk-variante`, com exclusão do produto atual, imagens válidas e sem consulta de estoque.
