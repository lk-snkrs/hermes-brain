# Curadoria LK — Commercial Order Apply Dev Receipt

Data UTC: `2026-06-02T12:44:38.451139+00:00`

## Escopo
- Aprovado por Lucas: “Aplicar”.
- Alterado somente tema dev `155065450718`.
- Production/produtos/preço/estoque/apps não alterados.

## Assets alterados
- `snippets/lk-variante-samba-jane.liquid`: readback `False`, sha `7d84f7330f631c5b`, size `2575` — White Black is top seller but excluded when current; Cream is fallback/proximity and handle corrected.
- `snippets/lk-variante-air-jordan-1-low.liquid`: readback `True`, sha `a1c9c3c424d46eea`, size `2396` — Ranked by 180d live sales inside regular AJ1 Low capsule; Light Smoke fallback/proximity.
- `snippets/lk-variante-air-jordan-1-low-travis.liquid`: readback `True`, sha `54d8dd17e0450468`, size `2500` — Ranked by 180d live sales inside Travis Scott capsule; 0-sale products kept as proximity fallback.

## QA

### samba_white_black
- status `200`; blocks `1`; items `5`; labels `White Blue Gum, Scarlet Gum, Black White Gum, Green White Gum, Cream Black Gum`; current in links `False`; Curadoria `1`; best seller text `False`; liquid errors `0`; markers `{'samba': 1, 'regular': 0, 'travis': 0}`

### samba_cream_fallback
- status `200`; blocks `1`; items `5`; labels `White Black, White Blue Gum, Scarlet Gum, Black White Gum, Green White Gum`; current in links `False`; Curadoria `1`; best seller text `False`; liquid errors `0`; markers `{'samba': 1, 'regular': 0, 'travis': 0}`

### aj1_regular_midnight
- status `200`; blocks `1`; items `5`; labels `Vintage Grey, Jade Smoke, Black Medium Grey, Taxi, Light Smoke Grey`; current in links `False`; Curadoria `1`; best seller text `False`; liquid errors `0`; markers `{'samba': 0, 'regular': 1, 'travis': 0}`

### aj1_regular_vintage
- status `200`; blocks `1`; items `3`; labels `Black Medium Grey, Taxi, Light Smoke Grey`; current in links `False`; Curadoria `1`; best seller text `False`; liquid errors `0`; markers `{'samba': 0, 'regular': 1, 'travis': 0}`

### travis_medium_olive
- status `200`; blocks `1`; items `5`; labels `Velvet Brown, Black Phantom, Reverse Mocha, Mocha, Canary`; current in links `False`; Curadoria `1`; best seller text `False`; liquid errors `0`; markers `{'samba': 0, 'regular': 0, 'travis': 1}`

### travis_velvet
- status `200`; blocks `1`; items `5`; labels `Medium Olive, Black Phantom, Reverse Mocha, Mocha, Canary`; current in links `False`; Curadoria `1`; best seller text `False`; liquid errors `0`; markers `{'samba': 0, 'regular': 0, 'travis': 1}`

### high_control
- status `200`; blocks `0`; items `0`; labels ``; current in links `False`; Curadoria `0`; best seller text `False`; liquid errors `0`; markers `{'samba': 0, 'regular': 0, 'travis': 0}`

### prod_control_samba
- status `200`; blocks `0`; items `0`; labels ``; current in links `False`; Curadoria `0`; best seller text `False`; liquid errors `0`; markers `{'samba': 0, 'regular': 0, 'travis': 0}`

## Rollback
Backups pré-upload salvos como `before__*` neste diretório; reupar esses assets para rollback dev.
