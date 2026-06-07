# Approval packet — Curadoria LK PDP — SB Dunk Low collabs/cápsulas DEV

Data: 2026-06-06
Status: pronto para aprovação explícita de upload em DEV

## Contexto

Lucas respondeu `Aprovo` após o merge Production do grupo Dunk Low regular e a recomendação de preparar a próxima rodada SB Dunk Low collabs/cápsulas.

Como ainda não havia payload fechado para este novo grupo, esta execução ficou em modo seguro/read-only e preparou o approval packet abaixo. Upload em DEV continua sendo Shopify theme write e exige aprovação explícita do payload.

## Fonte / cobertura

Fonte scan: `/opt/data/tmp/lk_curadoria_dunk_low_regular_split_readonly_20260606.json`

- SB/collabs total: `65`
- Já cobertos: `13`
- Uncovered: `52`
- Candidatos validados nesta rodada: `12`
- Selecionados para payload DEV: `10`

## Payload proposto

Marker sugerido:

`top30-nike-sb-dunk-low-collabs-breadth`

Grupo: Nike SB Dunk Low collabs/cápsulas — ícones e colaborações, separado do Dunk Low regular para não misturar intenção de compra.

Produtos selecionados:

1. `born-x-raised-x-nike-sb-dunk-low-one-block-at-a-time`
   - Label: `Born x Raised`
   - Title: `Tênis Born Raised x Nike SB Dunk Low One Block At A Time Azul`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-born-x-raised-x-nike-sb-dunk-low-one-block-at-a-time-azul-414676.jpg?v=1710449673`
2. `sean-cliver-x-dunk-low-sb-holiday-special`
   - Label: `Sean Cliver`
   - Title: `Tênis Sean Cliver x Dunk Low SB Holiday Special Azul`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-sean-cliver-x-dunk-low-sb-holiday-special-azul-825758.jpg?v=1710449799`
3. `april-skateboards-x-nike-sb-dunk-low-turbo-green`
   - Label: `April Skate`
   - Title: `Tênis April Skateboards x Nike SB Dunk Low Turbo Green Azul`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-april-skateboards-x-nike-sb-dunk-low-turbo-green-azul-691493.jpg?v=1710449673`
4. `travis-scott-x-nike-dunk-low-cactus-jack-937689726`
   - Label: `Travis Cactus`
   - Title: `Tênis Travis Scott x Nike Dunk Low Cactus Jack Preto`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-travis-scott-x-nike-dunk-low-cactus-jack-preto-232906.jpg?v=1710449756`
5. `tenis-nike-sb-dunk-low-x-futura-skateboard-bleached-aqua-azul`
   - Label: `Futura`
   - Title: `Tênis Nike Sb Dunk Low x Futura Skateboard Bleached Aqua Azul`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-nike-sb-dunk-low-x-futura-skateboard-bleached-aqua-azul-lk-sneakers-170953.jpg?v=1716091512`
6. `albino-preto-x-nike-sb-dunk-low-pearl-white`
   - Label: `Albino & Preto`
   - Title: `Tênis Albino & Preto x Nike SB Dunk Low Pearl White Bege`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-albino-preto-x-nike-sb-dunk-low-pearl-white-bege-124328.jpg?v=1710449670`
7. `ben-jerrys-x-dunk-low-sb-chunky-dunky`
   - Label: `Chunky Dunky`
   - Title: `Tênis Ben & Jerry's x Dunk Low SB Chunky Dunky Colorido`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-ben-jerrys-x-dunk-low-sb-chunky-dunky-colorido-478219.jpg?v=1710449673`
8. `concepts-x-nike-sb-dunk-low-orange-lobster`
   - Label: `Orange Lobster`
   - Title: `Tênis Concepts x Nike SB Dunk Low Orange Lobster Laranja`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-concepts-x-nike-sb-dunk-low-orange-lobster-laranja-733817.jpg?v=1710449674`
9. `grateful-dead-x-nike-sb-dunk-low-yellow-bear`
   - Label: `Grateful Dead`
   - Title: `Tênis Grateful Dead x Nike SB Dunk Low Yellow Bear Amarelo`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-grateful-dead-x-nike-sb-dunk-low-yellow-bear-amarelo-159297.jpg?v=1710449675`
10. `jarritos-x-nike-sb-dunk-low`
    - Label: `Jarritos`
    - Title: `Tênis Jarritos x Nike SB Dunk Low Branco/Verde`
    - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-jarritos-x-nike-sb-dunk-low-brancoverde-947192.jpg?v=1710449676`

## Validação prévia

Todos os 10 selecionados passaram:

- PDP público: HTTP `200`
- Product `.js`: HTTP `200`
- Imagem CDN: HTTP `200`

Também foram encontrados mais 2 candidatos válidos para reserva:

- `why-so-sad-x-nike-sb-dunk-low-the-predatory-bird` — `Why So Sad?`
- `tenis-nike-sb-dunk-low-x-there-skateboarding-ultra-humanized-preto` — `THERE Skate`

## Interpretação semântica

Seguro para agrupar porque são SB Dunk Low / Dunk Low collabs ou cápsulas reconhecíveis. Mantém separação do grupo Dunk Low regular, evitando misturar colorways mainstream com colaborações de alto apelo.

## Escopo proposto do write DEV

- Tema DEV: `155065450718` (`unpublished`)
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`
- Inserir apenas o novo bloco `top30-nike-sb-dunk-low-collabs-breadth`
- Não tocar Production
- Não tocar produtos, preço, estoque, Tiny, GMC, Klaviyo, Meta, checkout ou campanhas

## QA pós-DEV previsto

- Admin Asset API readback e SHA
- Marker count `1`
- Arrays alinhados `10/10/10/10`
- Current-product exclusion simulado
- 10/10 imagens `200`
- Sem URL malformada / placeholder
- Preview público se Shopify permitir; se preview redirecionar/anti-bot, marcar como inconclusivo e confiar em readback/static QA

## Rollback DEV

Backup do asset DEV antes do PUT e restauração do backup via Admin Asset API se necessário.

## Aprovação necessária

Para aplicar em DEV, Lucas precisa aprovar explicitamente este payload, por exemplo:

`Aprovo DEV SB Dunk collabs`
