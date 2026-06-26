# Approval packet — Curadoria LK PDP — Air Jordan 1 Low + High DEV

Data: 20260606T210430Z

## Status

- Recomendado para DEV: `True`
- Padrão canônico: Curadoria LK PDP breadth-first, read-only packet antes de DEV write.
- DEV SHA: `32a044cf70547725fbeebe9a065e45067826e815508b919e370b5a2377b5b8ae`
- Production SHA: `142523f70dd41b79be7468a2d5a0a7a9c50f3ae8427febff1c03f06870e51265`

## Grupos propostos

### `top30-air-jordan-1-low-adult-breadth`

- Já existe em DEV: `False`
- Já existe em Production: `False`
- Produtos: `10`
- Render esperado por PDP: `5`

- `tenis-air-jordan-1-low-eastside-golf-azul-marinho` — `Eastside Golf` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-low-elephant-brown-marrom` — `Elephant Brown Marrom` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-low-floral-canvas-rosa` — `Floral Canvas Rosa` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-low-lunar-new-year-photon-dust-cinza` — `Lunar New Year Photon Dust` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-low-multicolor-sashiko-colorido` — `Multicolor Sashiko` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-low-team-gold-amarelo` — `Team Gold Amarelo` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-low-year-of-dragon-2024-vinho` — `Year of Dragon 2024` — public `200` / js `200` / img `200`
- `air-jordan-1-low-all-star-carbon-fiber` — `All-Star Carbon Fiber` — public `200` / js `200` / img `200`
- `air-jordan-1-low-alternate-bred-toe` — `Alternate Bred Toe` — public `200` / js `200` / img `200`
- `air-jordan-1-low-aluminium` — `Aluminium Azul` — public `200` / js `200` / img `200`

### `top30-air-jordan-1-high-og-breadth`

- Já existe em DEV: `False`
- Já existe em Production: `False`
- Produtos: `10`
- Render esperado por PDP: `5`

- `tenis-nike-air-jordan-1-high-fragment-design-x-union-la-varsity-red-branco` — `Fragment Design x Union LA V` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-high-og-black-white-preto` — `OG Black White Preto` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-high-og-black-metallic-gold-preto` — `OG Black Metallic Gold` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-high-og-green-glow-verde` — `OG Green Glow Verde` — public `200` / js `200` / img `200`
- `air-jordan-1-high-rebellionaire` — `OG Rebellionaire Cinza` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-high-og-shattered-backboard-laranja` — `OG Shattered Backboard` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-high-og-sp-x-travis-scott-mocha` — `OG Sp x Travis Scott Mocha` — public `200` / js `200` / img `200`
- `air-jordan-1-high-og-starfish` — `OG Starfish Laranja` — public `200` / js `200` / img `200`
- `air-jordan-1-high-og-stealth` — `OG Stealth Cinza` — public `200` / js `200` / img `200`
- `tenis-air-jordan-1-high-og-unc-toe-azul` — `OG UNC Toe Azul` — public `200` / js `200` / img `200`

## Interpretação

- Separação semântica: AJ1 Low adulto separado de AJ1 High/OG adulto.
- Excluí GS/PS/TD/kids/infantil.
- Não mistura AJ1 com AJ4, Dunk ou outros modelos.

## Risco

- DEV write altera apenas tema unpublished; Production exige aprovação separada depois do readback/QA.
- Preview público pode redirecionar para live; nesse caso readback/Admin Asset API + QA estático serão fonte primária.

## Rollback DEV

- Fazer backup do asset DEV antes do PUT e restaurar via Asset API se necessário.

## Aprovação necessária

Para eu subir em DEV, responda: `Aprovo DEV AJ1 Low High`