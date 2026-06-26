# Approval packet — Curadoria LK PDP Batch Cloudsolo Loewe DEV

Data: 2026-06-06

## Contexto

Lucas pediu para seguir com LK PDP Thumbnail / Curadoria LK PDP após correção de tipografia das labels.

Este pacote é **read-only / aprovação DEV**. Nenhum write Shopify foi executado nesta preparação.

## Fonte e baseline

Render ativo confirmado:

- `sections/lk-pdp.liquid` renderiza `snippets/lk-variante-top30-visited-v2.liquid`.

Scan read-only:

- Catálogo Shopify Admin GraphQL: `2331` produtos lidos.
- Handles já cobertos no snippet ativo: `318` produtos do catálogo.
- Família On Running/Cloud detectada sem Curadoria ativa: `20` produtos sellable/publicados.
- Recorte semanticamente seguro escolhido: **On Running Cloudsolo x Loewe**.

Arquivos locais de evidência:

- `/opt/data/tmp/lk_curadoria_candidate_scan.json`
- `/opt/data/tmp/lk_cloudsolo_loewe_candidates_validated.json`

## Grupo proposto

Marker sugerido:

- `top30-on-running-cloudsolo-loewe`

Nome interno:

- `On Running Cloudsolo Loewe`

Critério semântico:

- Mesma colaboração/cápsula: `On Running x Loewe`.
- Mesma silhueta principal: `Cloudsolo`.
- Exclui outros modelos On/Loewe como `Cloudtilt`, `Cloudmonster` e `LightSpray`, para não misturar silhuetas.
- Grupo tem 16 produtos, permitindo renderizar 5 alternativas mesmo quando o produto atual está dentro do grupo.

## Handles / labels / imagens validados

Todos abaixo retornaram:

- `/products/{handle}.js`: HTTP `200`
- imagem CDN: HTTP `200`

1. `tenis-on-running-cloudsolo-loewe-lime-green-amarelo`
   - Label: `Lime Green`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-lime-green-amarelo-lk-3mf30662420-1-5650597.png?v=1761461062`

2. `tenis-on-running-cloudsolo-loewe-black-preto`
   - Label: `Black`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-black-preto-lk-3mf30660553-1-5687905.png?v=1761461062`

3. `tenis-on-running-cloudsolo-loewe-turquoise-azul`
   - Label: `Turquoise`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-turquoise-azul-lk-3mf30661748-1-8467880.png?v=1761461062`

4. `tenis-on-running-cloudsolo-loewe-white-light-grey-cinza`
   - Label: `White Light Grey`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-white-light-grey-cinza-lk-3wf30604607-1-5444067.png?v=1761461062`

5. `tenis-on-running-cloudsolo-loewe-white-orange-laranja`
   - Label: `White Orange`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-white-orange-laranja-lk-3mf30660663-1-3481287.png?v=1761461062`

6. `tenis-on-running-cloudsolo-loewe-dark-sand-cream-bege`
   - Label: `Dark Sand Cream`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-dark-sand-cream-bege-lk-3mf30664615-1-9720280.png?v=1761461062`

7. `tenis-on-running-cloudsolo-loewe-sand-turquoise-bege`
   - Label: `Sand Turquoise`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-sand-turquoise-bege-lk-3mf30664606-1-3838841.png?v=1761461062`

8. `tenis-on-running-cloudsolo-loewe-black-white-preto`
   - Label: `Black / White`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-blackwhite-preto-lk-3wf30600299-1-4567422.png?v=1761461062`

9. `tenis-on-running-cloudsolo-loewe-khaki-green-sand-verde`
   - Label: `Khaki Green Sand`
   - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-khaki-green-sand-verde-lk-3wf30604724-1-1119889.png?v=1764666675`

10. `tenis-on-running-cloudsolo-loewe-dark-brown-black-marrom`
    - Label: `Dark Brown Black`
    - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-dark-brown-black-marrom-lk-3mf30664611-1-3691081.png?v=1766830336`

11. `tenis-on-running-cloudsolo-loewe-black-eggshell-preto`
    - Label: `Black Eggshell`
    - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-black-eggshell-preto-lk-3mf30665476-9614730.png?v=1778853131`

12. `tenis-on-running-cloudsolo-loewe-red-eggshell-vermelho`
    - Label: `Red Eggshell`
    - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-red-eggshell-vermelho-lk-3986629.png?v=1778853132`

13. `tenis-on-running-cloudsolo-loewe-taupe-eggshell-marrom`
    - Label: `Taupe Eggshell`
    - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-taupe-eggshell-marrom-lk-8146236.png?v=1778853133`

14. `tenis-on-running-cloudsolo-loewe-teal-eggshell-azul`
    - Label: `Burgundy Eggshell`
    - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-burgundy-eggshell-bordo-lk-8035675.png?v=1778853130`
    - Observação: o handle contém `teal-eggshell`, mas o título/imagem públicos dizem `Burgundy Eggshell`; manter label pelo título/imagem real.

15. `tenis-on-running-cloudsolo-loewe-sand-burgundy-bege`
    - Label: `Sand Burgundy`
    - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-sand-burgundy-bege-lk-8943141.png?v=1778853130`

16. `tenis-on-running-cloudsolo-loewe-teal-eggshell-azul-1`
    - Label: `Teal Eggshell`
    - Image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-on-running-cloudsolo-loewe-teal-eggshell-azul-lk-3856405.png?v=1778853130`

## Patch esperado no DEV

Adicionar 1 grupo ao snippet ativo:

- Theme DEV: `155065450718` / `lk-new-theme/dev` / role deve ser confirmado como `unpublished` antes de upload.
- Asset alvo: `snippets/lk-variante-top30-visited-v2.liquid`.
- Inserção: adicionar marker, name, handles, labels e images nos arrays `lk_top30_*` mantendo alinhamento de índices.

## QA DEV após apply aprovado

Checks mínimos:

- readback Admin API do asset DEV;
- marker novo aparece 1 vez;
- arrays `markers/names/handles/labels/images` continuam com mesmo comprimento;
- grupo novo tem 16 handles, 16 labels, 16 imagens;
- nenhum URL `https:https://` ou `https://https://`;
- simulação de exclusão do produto atual retorna 5 cards;
- public preview/CDP em pelo menos 3 PDPs Cloudsolo:
  - bloco `Curadoria LK / Outras variações` presente;
  - rail `display:grid`;
  - 5 cards;
  - produto atual excluído;
  - imagens carregadas;
  - labels com peso visual 300 após correção CSS.

## Risco

Baixo/médio:

- Grupo é semanticamente forte, mas On/Loewe tem outros modelos próximos (`Cloudtilt`, `Cloudmonster`). Eles foram intencionalmente excluídos para preservar a coerência da silhueta Cloudsolo.
- Um handle tem divergência nominal (`teal-eggshell` no handle, Burgundy no título/imagem); mantive o label pelo título/imagem públicos.

## Rollback

Restaurar o backup pré-write do snippet DEV `snippets/lk-variante-top30-visited-v2.liquid`.

## Aprovação necessária para DEV

Texto de aprovação sugerido:

`Aprovo aplicar no tema DEV 155065450718 o pacote Curadoria LK PDP Cloudsolo Loewe em snippets/lk-variante-top30-visited-v2.liquid, adicionando o grupo top30-on-running-cloudsolo-loewe com os 16 handles/labels/imagens listados, sem mexer em Production, produtos, preço, estoque ou checkout.`
