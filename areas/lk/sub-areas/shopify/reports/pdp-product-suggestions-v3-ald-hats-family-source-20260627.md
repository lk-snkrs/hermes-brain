# Source packet — ALD hats family fallback for Product Suggestions v3

- Data/hora: 2026-06-27T11:00:33Z
- Escopo: reforço read-only de fonte família/Curadoria para acessórios ALD hats
- Fontes: Shopify public search suggest, product.js público e snippet Curadoria LK existente
- Writes externos: 0
- Consulta de estoque: 0
- values_printed=false

## Resultado

A Curadoria atual do Saint George já cobre 6 handles e renderiza até 5 excluindo o produto atual. Para o bloco inferior v3, após dedupe da Curadoria, a fonte pública ainda oferece candidatos ALD hats adicionais.

## Candidatos família `ald-hats` após dedupe Curadoria

| handle | title | label sugerido | HTTP |
|---|---|---|---:|
| `bone-aime-leon-dore-unisphere-preto` | Boné Aimé Leon Dore Unisphere Preto | `Aimé Leon Dore Unisphere` | `200` |
| `bone-6-panel-aime-leon-dore-cycling-logo-azul` | Boné 6 Panel Aimé Leon Dore Cycling Logo Azul | `6 Panel Aimé Leon` | `200` |
| `bone-5-panel-aime-leon-dore-unisphere-azul` | Boné 5 Panel Aimé Leon Dore Unisphere Azul | `5 Panel Aimé Leon` | `200` |
| `bone-5-panel-aime-leon-dore-unisphere-branco` | Boné 5 Panel Aimé Leon Dore Unisphere Branco | `5 Panel Aimé Leon` | `200` |
| `bone-aime-leon-dore-washed-script-jet-black-preto` | Boné Aime Leon Dore Washed Script Jet Black Preto | `Washed Script Jet Black` | `200` |
| `bone-aime-leon-micro-logo-hat-jet-black-preto` | Boné Aimé Leon Dore Micro Logo Jet Black Preto | `Aimé Leon Dore Micro` | `200` |
| `bone-aime-leon-dore-x-porsche-colorblock-logo-pristine-off-white` | Boné Aimé Leon Dore x Porsche Colorblock Logo Pristine Off White | `Aimé Leon Dore x` | `200` |

## Uso proposto no v3

Quando Recommendations API + dedupe da Curadoria retornar menos de 2 candidatos para um boné ALD, usar `family_fallback: ald-hats` com estes handles, mantendo:

- excluir produto atual;
- excluir handles já no bloco Curadoria LK;
- bloquear cross-type apparel/sneaker;
- manter elegibilidade Stock como filtro final quando LK Stock responder;
- esconder bloco se menos de 2 candidatos válidos.