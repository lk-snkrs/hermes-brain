# Approval Packet — Curadoria LK PDP: Nike Air Force 1 Low Special/Collabs — DEV

Data: 2026-06-06 13:50 UTC  
Escopo: read-only concluído; solicitação de aprovação para write em tema DEV/unpublished.

## Evidência read-only

- Baseline ativo confirmado no tema/repo local: `sections/lk-pdp.liquid` renderiza `snippets/lk-variante-top30-visited-v2.liquid`.
- Snippet ativo contém arrays `lk_top30_*` e marker Cloudsolo já presente: `top30-on-running-cloudsolo-loewe`.
- Scan Shopify Admin read-only: 2331 produtos analisados.
- Cluster manual encontrado: `nike-air-force-1-low`, 24 produtos ativos/publicados com imagem; 18 não cobertos pelo parser de Curadoria atual.
- Validação pública final do lote proposto: 7/7 PDP público HTTP 200, 7/7 `.js` HTTP 200, 7/7 imagens CDN HTTP 200.
- Produto descartado do lote: `tenis-nike-air-force-1-low-x-supreme-wheat-marrom` porque `.js`/página retornaram 503 no teste público; `NOCTA White` também ficou fora do lote aprovado porque a página HTML retornou 503 apesar de `.js` 200.

## Interpretação

Próximo lote recomendado: **Nike Air Force 1 Low Special/Collabs**.

Justificativa semântica:

- Mesma silhueta base: Nike Air Force 1 Low.
- Grupo intencionalmente nomeado como special/collabs para não misturar com uma eventual família regular branca/preta/Shadow/general release.
- Produtos são edições especiais/collabs reconhecíveis: Supreme, Ambush, Tiffany, Off-White.
- 7 itens é suficiente para a regra do bloco: em qualquer PDP do grupo, o produto atual é excluído e sobram 6 candidatos; o rail renderiza no máximo 5 cards.

## Preview proposto

Marker:

`top30-nike-air-force-1-low-special`

Nome interno:

`Nike Air Force 1 Low special/collabs`

Itens propostos:

- `tenis-nike-air-force-1-low-x-supreme-black-preto` — label: `Supreme Black`
- `supreme-x-nike-air-force-1-low-box-logo-white` — label: `Supreme White`
- `ambush-x-nike-air-force-1-low-black` — label: `Ambush Black`
- `ambush-x-nike-air-force-1-low-phantom` — label: `Ambush Phantom`
- `ambush-x-nike-air-force-1-low-game-royal-and-vivid-sulphur` — label: `Ambush Game Royal`
- `tiffany-co-x-nike-air-force-1-low-1837` — label: `Tiffany 1837`
- `off-white-x-nike-air-force-1-low-green-brooklyn` — label: `Off-White Brooklyn`

Imagens CDN validadas:

- Supreme Black: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-nike-air-force-1-low-x-supreme-black-preto-176733.jpg?v=1712765614`
- Supreme White: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-nike-air-force-1-low-x-supreme-white-branco-lk-cu9225100-194274091274-699353.png?v=1741489954`
- Ambush Black: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-ambush-x-nike-air-force-1-low-black-preto-841105.jpg?v=1710449669`
- Ambush Phantom: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-ambush-x-nike-air-force-1-low-phantom-branco-827437.jpg?v=1710449673`
- Ambush Game Royal: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-ambush-x-nike-air-force-1-low-game-royal-and-vivid-sulphur-azul-673663.jpg?v=1710449673`
- Tiffany 1837: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-tiffany-co-x-nike-air-force-1-low-1837-preto-338080.jpg?v=1710449755`
- Off-White Brooklyn: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-off-white-x-nike-air-force-1-low-green-brooklyn-verde-561590.jpg?v=1710449755`

## Risco

Baixo/médio:

- Baixo técnico: alteração isolada no snippet de Curadoria PDP, sem produto/preço/estoque/checkout.
- Médio semântico: collabs diferentes dentro da mesma silhueta. Mitigação: nomear como special/collabs e excluir AF1 regular/general release.
- Sem write executado até agora.

## QA planejado se aprovado para DEV

1. Backup/readback do asset DEV `snippets/lk-variante-top30-visited-v2.liquid` no tema `155065450718`.
2. Aplicar apenas o novo grupo/arrays no DEV.
3. Readback DEV: marker count 1, arrays alinhados, 7 handles/labels/imagens.
4. Static QA: sem duplicados, sem `https:https`, sem placeholder, current product excluído, render count esperado 5.
5. Preview/CDP em 2–3 PDPs do grupo:
   - bloco `Curadoria LK / Outras variações` visível;
   - marker `top30-nike-air-force-1-low-special`;
   - 5 cards renderizados;
   - produto atual excluído;
   - `span.lk-variante__label font-weight:300` e `::after font-weight:300`.

## Rollback

- DEV: restaurar backup/readback do asset `snippets/lk-variante-top30-visited-v2.liquid` criado antes do PUT.
- Production: nenhum impacto sem aprovação separada de merge para Production.

## Próxima decisão

Aprovar ou rejeitar o write no tema DEV/unpublished `155065450718` para inserir o grupo `top30-nike-air-force-1-low-special`.

Frase operacional esperada se aprovado: **“Aprovo DEV Air Force 1 Low Special”**.
