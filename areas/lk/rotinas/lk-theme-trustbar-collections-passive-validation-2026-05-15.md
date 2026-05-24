# LK Theme — validação passiva trustbar collections

Gerado em: `2026-05-15T20:25:00Z`
Status: `passive_validation_pass_no_hotfix`

## Veredito

Trustbar/benefícios LK está presente e íntegra nas rotas principais de collection. Não há hotfix recomendado.

## Rotas validadas

- `/collections/all`: HTTP `200`, trustbar completa `PASS`.
- `/collections/sale`: HTTP `200`, trustbar completa `PASS`.
- `/collections/sneakers`: HTTP `200`, trustbar completa `PASS`.
- `/collections/roupas`: HTTP `200`, trustbar completa `PASS`.
- `/collections/athleisure`: HTTP `200`, trustbar completa `PASS`.
- `/collections/eyewear`: HTTP `200`, trustbar completa `PASS`.
- `/collections/collectibles`: HTTP `200`, trustbar completa `PASS`.

Observação: o menu `APPARELS` aponta para `/collections/roupas`; `/collections/apparels` retorna 404, mas não é a rota usada pelo header.

## Itens conferidos

Em todas as rotas válidas, o HTML continha:

- `ORIGINALIDADE`
- `GARANTIDA`
- `EM ATÉ 10X`
- `SEM JUROS`
- `FRETE`
- `GRÁTIS`
- `LOJA FÍSICA`
- `JARDINS SP`

## Validação visual

Browser vision confirmou na collection carregada:

- trustbar aparece antes dos filtros/produtos;
- blocos alinhados horizontalmente;
- textos legíveis;
- divisórias e ícones íntegros;
- sem sobreposição/corte/desalinhamento grave.

Screenshot local: `/opt/data/cache/screenshots/browser_screenshot_e0986aee16014a2cabefc43bb6945058.png`

## O que não foi feito

- Nenhum hotfix.
- Nenhum Shopify/theme write.
- Nenhum deploy.
- Nenhuma alteração CSS/Liquid.
- Nenhuma campanha/envio.

## Decisão

Congelar como PASS. Só reabrir se aparecer regressão objetiva em rota específica, principalmente mobile.
