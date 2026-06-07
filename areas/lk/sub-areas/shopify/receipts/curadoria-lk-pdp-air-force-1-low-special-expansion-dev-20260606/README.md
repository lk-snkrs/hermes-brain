# Curadoria LK PDP — AF1 Special Expansion — DEV receipt

## Status
- Data: `2026-06-06T14:20:36+00:00`.
- Ação: aplicação aprovada em DEV.
- Aprovação Lucas: `Aprovo DEV AF1 Special Expansion`.

## Escopo
- Tema DEV: `155065450718` (`lk-new-theme/dev`, role `unpublished`).
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`.
- Grupo: `top30-nike-air-force-1-low-special`.
- Mudança: expandir grupo de 7 para 18 itens adicionando 11 AF1 Low special/collab.

## Itens adicionados
1. `tenis-a-ma-maniere-x-air-force-1-low-triple-white-branco` — `A Ma Maniére White`
2. `tenis-nike-air-force-1-low-protro-kobe-bryant-mamba-mentality-amarelo` — `Kobe Mamba`
3. `tenis-nike-air-force-1-low-protro-kobe-bryant-siempre-hermanos-marrom` — `Kobe Hermanos`
4. `nike-air-force-1-low-shadow-light-soft-pink` — `Shadow Pink`
5. `tenis-nike-air-force-1-low-valentines-day-2025` — `Valentines 2025`
6. `nike-air-force-1-low-world-champ` — `World Champ`
7. `nike-air-force-1-low-world-champ-lakers` — `World Champ Lakers`
8. `tenis-nike-air-force-1-low-x-a-ma-maniere-while-you-were-sleeping-rose` — `A Ma Maniére Rose`
9. `tenis-nike-air-force-1-low-x-g-dragon-peaceminusone-para-noise-3-0-preto` — `G-Dragon Para-Noise`
10. `tenis-nike-air-force-1-low-x-nocta-certified-lover-boy-branco` — `NOCTA CLB`
11. `tenis-nike-air-force-1-low-x-supreme-wheat-marrom` — `Supreme Wheat`

## Backup / readback antes
- Backup local: `/opt/data/tmp/lk-dev-before-af1-special-expansion.liquid`.
- SHA256 antes: `5ade88a839deb895d031a90ee96feba1757e8783d4d4a91886e097ecbcc0f78b`.
- Grupo AF1 Special antes: 7 handles / 7 labels / 7 imagens.
- Arrays: 29 grupos alinhados.

## Aplicação
- Método: Shopify Asset API PUT no tema DEV aprovado.
- Candidate aplicado a partir do readback DEV atual, não como substituição cega da Production.
- SHA256 candidato/readback pós-polling: `5f725da9067e988cb2e8e52664d35d1c65aaeaef68d9fc7df02b0934438137fc`.
- Readback convergiu na tentativa 2.
- Artefatos:
  - `/opt/data/tmp/lk-dev-af1-special-expansion-candidate-from-dev.liquid`
  - `/opt/data/tmp/lk-dev-after-af1-special-expansion.liquid`
  - `/opt/data/tmp/lk-dev-af1-special-expansion-apply-result.json`

## QA estático pós-write
- Marker `top30-nike-air-force-1-low-special`: count `1`.
- Arrays Curadoria: 29 grupos alinhados em todos os 5 arrays.
- Grupo AF1 Special pós-expansão: 18 handles / 18 labels / 18 imagens.
- Todos os 11 novos handles presentes no readback.
- Erros estáticos: nenhum.
- Duplicados: nenhum.
- URL malformada/placeholder: nenhum detectado.

## Controle Production
- Production `155065417950` conferida após DEV write:
  - SHA256: `dc30f0059f131a3b326698edc3094eb02db4a949bbac91a5b3b900571353b2a8`.
  - AF1 count: 7.
  - Expansion presente: `false`.
- Portanto o write ficou restrito ao DEV.

## QA visual DEV via CDP
Amostras testadas com `preview_theme_id=155065450718`:

- `tenis-a-ma-maniere-x-air-force-1-low-triple-white-branco`
- `tenis-nike-air-force-1-low-protro-kobe-bryant-mamba-mentality-amarelo`
- `tenis-nike-air-force-1-low-x-supreme-wheat-marrom`

Resultado nas 3 PDPs:
- Bloco renderizado: `true`.
- Marker: `top30-nike-air-force-1-low-special`.
- Cards: `5`.
- `railDisplay`: `grid`.
- Labels: `fontWeight 300` no `span` e `300` no `::after`.

Caveat: a URL final removeu o parâmetro `preview_theme_id`, mas o bloco renderizou para handles que Production ainda não cobre; isso indica preview/cookie DEV efetivo. Por segurança, Production readback separado confirmou que Production continua sem a expansão.

Artefatos QA:
- `/opt/data/tmp/lk_af1_special_expansion_dev_qa/summary.json`

## Risco
- Baixo: alteração restrita ao grupo Curadoria em DEV.
- Sem produto/preço/estoque/checkout/collection/GMC/Klaviyo/ads/Tiny.
- Pequena cautela histórica: `NOCTA CLB` e `Supreme Wheat` tinham sido instáveis em rodada anterior, mas passaram em HTML/JS/CDN na rodada de aprovação e renderizaram em QA DEV para Supreme Wheat.

## Rollback DEV
- Restaurar `/opt/data/tmp/lk-dev-before-af1-special-expansion.liquid` no asset DEV `snippets/lk-variante-top30-visited-v2.liquid`.
- Alternativamente remover os 11 handles/labels/imagens adicionados no grupo `top30-nike-air-force-1-low-special`.

## Próxima decisão
- Se Lucas aprovar, preparar PR/merge para Production deste escopo.
- Production exige aprovação explícita separada.
