# Approval packet — Curadoria LK PDP — Dunk Low regular

Data: 2026-06-06
Perfil: LK Shopify
Status: read-only, sem upload DEV/Production nesta etapa

## Pedido

Lucas respondeu `Aprovo 1` depois da recomendação:

1. Dunk Low regular
2. Nike SB Dunk Low collabs/cápsulas

Interpretação segura: avançar com a opção 1, preparando a rodada Dunk Low regular. Como upload em DEV ainda é Shopify theme write, este packet pede aprovação explícita do payload DEV antes de qualquer PUT.

## Evidências read-only

Script executado:

- `/opt/data/tmp/lk_curadoria_dunk_low_regular_split_readonly_20260606.py`

Resultado:

- Output JSON: `/opt/data/tmp/lk_curadoria_dunk_low_regular_split_readonly_20260606.json`
- Timestamp: `2026-06-06T17:39:46.475271+00:00`
- DEV groups atuais: `43`
- Production groups atuais: `43`

Split Dunk:

- Dunk Low regular:
  - total: `121`
  - covered: `17`
  - uncovered: `104`
  - primeiros `30/30` validados com PDP HTML `200`, product `.js` `200`, imagem `200`
- SB/collabs:
  - total: `65`
  - covered: `13`
  - uncovered: `52`
  - primeiros `5` public_ok no sweep inicial
  - deferido para rodada separada

## Subagentes / lanes

### Lane 1 — Parser / Cobertura

- O gap maior ainda é Dunk Low.
- Split confirmou que há massa suficiente para uma rodada regular sem misturar SB/collabs.
- Production já está em `43` grupos após NB 9060 + Air Max 1.

### Lane 2 — Curadoria Semântica

Regra proposta:

- Incluir apenas **Dunk Low regular / colorways / releases não-SB**.
- Excluir SB, skate/collabs pesadas, Lobster, Ben & Jerry's, Grateful Dead, Born x Raised, April, Albino & Preto etc.
- Labels curtos para mobile.

### Lane 3 — Validação pública / imagens

Os candidatos abaixo foram detectados como public_ok no scan read-only:

- PDP HTML `200`
- `/products/<handle>.js` `200`
- imagem CDN `200`
- sem `TenisMoldeLK`

### Lane 4 — Risco / Rollback

- Risco principal: grupo amplo demais se misturar regular com SB/collabs. Foi mitigado com split.
- Risco secundário: alguns handles antigos podem ter título/handle pouco padronizado; por isso a primeira rodada usa candidatos limpos e labels manuais.
- Upload só deve ir para DEV primeiro, com backup e QA estático.

## Payload proposto para DEV

Marker proposto:

`top30-nike-dunk-low-regular-breadth`

Aria:

`Curadoria LK Nike Dunk Low regular`

Produtos propostos:

- `nike-dunk-low-ucla` — `UCLA`
- `dunk-low-light-ocean-bliss` — `Ocean Bliss`
- `dunk-low-next-nature-pink-pale-coral` — `Pink Coral`
- `nba-x-nike-dunk-low-chicago` — `NBA Chicago`
- `tenis-nike-dunk-low-halloween-2021-laranja` — `Halloween`
- `tenis-nike-dunk-low-miami-dolphins-azul` — `Miami Dolphins`
- `tenis-nike-dunk-low-university-blue-azul` — `University Blue`
- `tenis-nike-dunk-low-bicoastal-verde` — `Bicoastal`
- `nike-dunk-low-black-paisley` — `Black Paisley`
- `nike-dunk-low-black-panda` — `Black Panda`

Render esperado:

- 10 handles no grupo.
- Cada PDP do grupo renderiza até 5 alternativas, excluindo o produto atual.

## O que fica para depois

Rodada separada para SB/collabs/cápsulas, por exemplo:

- Albino & Preto x SB Pearl White
- April Skateboards x SB Turbo Green
- Ben & Jerry's Chunky Dunky
- Born x Raised One Block At A Time
- Concepts Orange Lobster

## Plano se DEV for aprovado

1. Revalidar role dos temas:
   - DEV `155065450718` precisa estar `unpublished`
   - Production `155065417950` precisa estar `main`
2. Backup remoto do asset DEV antes do PUT.
3. Inserir somente o bloco `top30-nike-dunk-low-regular-breadth` no DEV.
4. Readback/poll por SHA e marker.
5. QA estático:
   - marker único;
   - arrays `handles/labels/images/titles` alinhados;
   - render esperado `5` cards;
   - current-product exclusion;
   - sem URL malformada;
   - sem `TenisMoldeLK`;
   - imagens HTTP 200.
6. Confirmar Production unchanged.
7. Receipt Brain.

## Decisão necessária

Para executar upload no DEV, aprovar explicitamente:

`Aprovo DEV Dunk Low regular`

Sem essa aprovação explícita, manter como packet read-only.
