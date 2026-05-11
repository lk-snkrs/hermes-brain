# LK SEO/CRO — execução Shopify aprovada — 2026-05-11

## Aprovação

Lucas aprovou o preview: “aprovo fazer tudo”. Execução limitada aos campos aprovados e seguros via Shopify Admin GraphQL.

## Resultado

- Alterações executadas e verificadas: 8
- Falhas de verificação: 0
- Itens pulados/pendentes: 1

## Guardrails cumpridos

- Não alterei preço, estoque, variantes, SKU, imagem, tema, app, Merchant, Search Console, campanha, Klaviyo ou WhatsApp.
- Usei Doppler para secrets, sem imprimir valores.
- Salvei backup/rollback no JSON de auditoria.

## Executados

### https://lksneakers.com.br/products/nike-dunk-low-rose-whisper
- Recurso: product `nike-dunk-low-rose-whisper`
- Status: success
- Verificado live: True
- SEO title anterior: `Tênis Nike Dunk Low Rose Whisper Rosa por R$ 1.499,99 em até 10x | LK Sneakers`
- SEO title novo: `Nike Dunk Low Rose Whisper Rosa | LK Sneakers`
- Meta anterior: `Tênis Nike Dunk Low Rose Whisper Rosa oferece conforto e estilo únicos. Conheça esse modelo exclusivo e garanta o seu par na LK Sneakers!`
- Meta nova: `Nike Dunk Low Rose Whisper original em rosa, com curadoria LK Sneakers, autenticidade garantida e compra em até 10x sem juros.`

### https://lksneakers.com.br/products/nike-dunk-low-ocean-bliss
- Recurso: product `nike-dunk-low-ocean-bliss`
- Status: success
- Verificado live: True
- SEO title anterior: `Tênis Nike Dunk Low Ocean Bliss Azul por R$ 1.549,90 em até 10x | LK Sneakers`
- SEO title novo: `Nike Dunk Low Ocean Bliss Azul | LK Sneakers`
- Meta anterior: `Tênis Nike Dunk Low Ocean Bliss Azul combina estilo e conforto. Conheça nosso modelo exclusivo e garanta o seu par hoje mesmo na LK Sneakers.`
- Meta nova: `Nike Dunk Low Ocean Bliss original em azul claro, com curadoria LK Sneakers, autenticidade garantida e até 10x sem juros.`

### https://lksneakers.com.br/products/nike-dunk-low-teddy-bear-pink
- Recurso: product `nike-dunk-low-teddy-bear-pink`
- Status: success
- Verificado live: True
- SEO title anterior: `Tênis Nike Dunk Low Teddy Bear Pink Rosa por R$ 2.499,99 em até 10x | LK Sneakers`
- SEO title novo: `Nike Dunk Low Teddy Bear Pink | LK Sneakers`
- Meta anterior: `Tênis Nike Dunk Low Teddy Bear Pink Rosa combina estilo e conforto. Compre online e destaque-se com este modelo exclusivo que é perfeito para qualquer ocasião.`
- Meta nova: `Nike Dunk Low Teddy Bear Pink original, textura premium e curadoria LK Sneakers, com autenticidade garantida e até 10x sem juros.`

### https://lksneakers.com.br/products/air-jordan-1-mid-wolf-grey
- Recurso: product `air-jordan-1-mid-wolf-grey`
- Status: success
- Verificado live: True
- SEO title anterior: `Tênis Nike Air Jordan 1 Mid Wolf Grey Cinza por R$ 1.999,90 em até 10x | LK Sneakers`
- SEO title novo: `Air Jordan 1 Mid Wolf Grey Cinza | LK Sneakers`
- Meta anterior: `Experimente o Tênis Air Jordan 1 Mid Wolf Grey Cinza, um modelo exclusivo que combina estilo e conforto. Conheça nossa coleção e compre online!`
- Meta nova: `Air Jordan 1 Mid Wolf Grey original, curadoria premium LK Sneakers, autenticidade garantida e compra em até 10x sem juros.`

### https://lksneakers.com.br/products/air-jordan-1-low-sunset-haze
- Recurso: product `air-jordan-1-low-sunset-haze`
- Status: success
- Verificado live: True
- SEO title anterior: `Tênis Nike Air Jordan 1 Low Sunset Haze Laranja por R$ 1.599,99 em até 10x | LK Sneakers`
- SEO title novo: `Air Jordan 1 Low Sunset Haze | LK Sneakers`
- Meta anterior: `Tênis Air Jordan 1 Low Sunset Haze Laranja oferece estilo e conforto inigualáveis. Conheça este modelo exclusivo e compre online para elevar seu visual.`
- Meta nova: `Air Jordan 1 Low Sunset Haze original, tons suaves e curadoria LK Sneakers, com autenticidade garantida e até 10x sem juros.`

### https://lksneakers.com.br/products/supreme-x-nike-air-force-1-low-box-logo-white
- Recurso: product `supreme-x-nike-air-force-1-low-box-logo-white`
- Status: success
- Verificado live: True
- SEO title anterior: `Tênis Nike Air Force 1 Low x Supreme White Branco por R$ 2.999,99 em até 10x | LK Sneakers`
- SEO title novo: `Supreme x Nike Air Force 1 Low White | LK Sneakers`
- Meta anterior: `Tênis Nike Air Force 1 Low x Supreme White Branco combina estilo e conforto. Conheça esse modelo exclusivo e eleve seu visual com autenticidade. Compre online!`
- Meta nova: `Supreme x Nike Air Force 1 Low White original, box logo e curadoria LK Sneakers, com autenticidade garantida e até 10x sem juros.`

### https://lksneakers.com.br/collections/nike-dunk
- Recurso: collection `nike-dunk`
- Status: success
- Verificado live: True
- SEO title anterior: `Nike Dunk Low, High &amp; SB Original | 179 Colorways | LK Sneakers`
- SEO title novo: `Nike Dunk Original: Low, High e Edições | LK Sneakers`
- Meta anterior: `Nike Dunk Low, High e SB originais: 179 colorways (Panda, Chunky Dunky, Grateful Dead) a partir de R$ 650 em 10x. Pronta entrega SP.`
- Meta nova: `Nike Dunk original na LK Sneakers: curadoria premium, modelos femininos e masculinos, autenticidade garantida e até 10x sem juros.`

### https://lksneakers.com.br/collections/sneakers
- Recurso: collection `sneakers`
- Status: success
- Verificado live: True
- Título/H1 anterior: `Sneakers for You`
- Título/H1 novo: `Tênis e Sneakers Originais`
- Intro opcional: não escrita para evitar sobrescrever descriptionHtml existente.

## Pulados / pendentes

### https://lksneakers.com.br/
- Escopo: homepage SEO title/meta
- Motivo: homepage Online Store SEO preferences not exposed as safe product/collection GraphQL mutation; no theme/admin hack attempted

## Rollback

O rollback está no JSON: para cada item executado, restaurar os campos em `backup` via o mesmo recurso Shopify GraphQL.

## Artefatos

- `reports/lk-seo-cro-shopify-execution-2026-05-11.json`
- `reports/lk-seo-cro-shopify-execution-2026-05-11.md`
