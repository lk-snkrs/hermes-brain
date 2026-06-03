# Approval packet — remover bloco PDP “Outras cores” (`pi-color-siblings`)

Data: 2026-06-02T15:48:14.211572+00:00

## Pedido
Remover do PDP a feature antiga de variações por cor exibida como “Outras cores”, classe `pi-color-siblings`.

## Asset afetado
- Tema production atual: `lk-new-theme/production` / theme id `155065417950`
- Asset: `sections/lk-pdp.liquid`

## Mudança proposta
Remoção cirúrgica de:
- CSS do bloco `/* Color siblings — "Outras cores" */`
- Render Liquid baseado em `product.metafields.custom.color_siblings.value`
- Markup `.pi-color-siblings`, label “Outras cores”, thumbnails e links para produtos irmãos

## Não mexe em
- Nome do produto (`pi-name`)
- Marca/vendor (`pi-brand`)
- Colorway textual (`pi-colorway`)
- Reviews Judge.me
- SKU
- Preço
- Seletor de tamanho
- Botão de compra/chat
- Schema/reviews

## Validação local do patch
- Blocos CSS removidos: 1
- Blocos Liquid removidos: 1
- Ocorrências `pi-color-siblings` antes: 21
- Ocorrências `pi-color-siblings` depois: 0
- Ocorrências `color_siblings` depois: 0
- `pi-colorway` preservado: True
- Judge.me preservado: True
- Indício de size picker preservado: True

## Risco
Baixo/médio:
- Baixo porque remove um bloco isolado de UI/CSS no PDP.
- Médio por estar em asset production global de PDP; qualquer erro Liquid afetaria páginas de produto.

## Rollback
Reaplicar o arquivo salvo em:
`receipts/theme-dev/remove-pi-color-siblings-candidate-20260602T154724Z/sections__lk-pdp.liquid.before`

## Candidate
Arquivo candidato:
`receipts/theme-dev/remove-pi-color-siblings-candidate-20260602T154724Z/sections__lk-pdp.liquid.candidate`

Diff:
`receipts/theme-dev/remove-pi-color-siblings-candidate-20260602T154724Z/diff.patch`

## Aprovação necessária
Exige aprovação explícita de Lucas para write em Shopify production.
Frase sugerida:
“aprovado aplicar remoção do pi-color-siblings em production”
