# Approval packet — Curadoria LK PDP — próximos produtos / rodada pós-merge

Data: 2026-06-06
Perfil: LK Shopify
Status: read-only, sem upload DEV/Production nesta etapa

## Pedido

Lucas pediu: "Vamos próximos produtos" após merge para Production da rodada anterior.

Interpretação segura: continuar autonomamente com descoberta read-only, priorização e pacote de aprovação DEV. Não autoriza upload em DEV/Production sem aprovação explícita do escopo.

## Evidências read-only

Scans executados:

1. Scanner Curadoria padrão:
   - Arquivo: `/opt/data/tmp/lk_curadoria_more_products_readonly_20260606.json`
   - Timestamp: `2026-06-06T17:12:10.100079+00:00`
   - Product count: `2331`
   - DEV: `607` handles / `41` groups
   - Production: `603` handles / `41` groups

2. Deep scan de próximos clusters:
   - Arquivo: `/opt/data/tmp/lk_curadoria_next_products_deep_scan_20260606.json`
   - Timestamp: `2026-06-06T17:15:49.377700+00:00`
   - Top clusters por cobertura + public_ok:
     - `nike-dunk-low`: total `186`, covered `30`, uncovered `156`, `12/12` primeiros public_ok
     - `new-balance-9060`: total `53`, covered `25`, uncovered `28`, `12/12` primeiros public_ok
     - `nike-air-max-1`: total `8`, covered `0`, uncovered `8`, `8/8` public_ok
     - `crocs-clog`: total `4`, covered `0`, uncovered `4`, `4/4` public_ok
     - `nike-air-jordan-1-high`: total `27`, covered `8`, uncovered `19`, `3/12` public_ok
     - `adidas-gazelle`: total `31`, covered `16`, uncovered `15`, `3/12` public_ok

## Subagentes / lanes de análise

### 1. Parser / Cobertura

- A rodada anterior já está em Production no source/readback.
- Próximo maior gap bruto: Dunk Low/SB e NB 9060.
- Melhor grupo novo limpo, sem depender de mexer em grupo antigo: Air Max 1.

### 2. Curadoria Semântica

Ordem sugerida:

1. **New Balance 9060 — expansão adulta/cromática**
   - Alta relevância comercial e modelo já forte na LK.
   - Deve excluir kids/TD no primeiro pacote para não misturar adulto/infantil.
   - Melhor como expansão/ajuste de grupo existente, com labels curtos.

2. **Nike Air Max 1 — novo grupo regular/collabs**
   - 8 produtos, 8 public_ok, sem cobertura atual.
   - Mesmo modelo, grupo semanticamente limpo apesar de collabs Patta/Travis/Concepts/Kasina.
   - Bom para breadth + qualidade sem mexer em grupos complexos.

3. **Nike Dunk Low / SB Dunk Low — separar antes de aplicar**
   - Maior oportunidade bruta: 156 uncovered no scan.
   - Risco: mistura regular, SB, collabs e cápsulas. Não deve virar um grupo único genérico.
   - Recomendação: subrodada separada para split `Dunk Low regular` vs `SB Dunk Low collabs`.

4. **Crocs Classic Clog collabs/personagens — grupo pequeno**
   - 4/4 public_ok, mas categoria diferente da maioria dos sneakers.
   - Bom se objetivo for cobertura breadth/novidade; menor prioridade CRO.

5. **AJ1 High / Gazelle / AJ4 / Yeezy 350 — laterais**
   - Têm gaps, mas poucos public_ok no primeiro sweep. Melhor revalidar em segunda passada antes de upload.

### 3. Validação pública / imagens

Public_ok significa: PDP HTML `200` + `/products/<handle>.js` `200` + CDN image `200` no momento do scan.

Candidatos limpos imediatos:

#### New Balance 9060 adultos — proposta inicial

- `new-balance-9060-black-cement-black-cat-preto` — `Black Cat`
- `tenis-new-balance-9060-black-castlerock-grey-preto` — `Castlerock`
- `tenis-new-balance-9060-black-magnet-preto` — `Black Magnet`
- `tenis-new-balance-9060-chrome-blue-azul` — `Chrome Blue`
- `tenis-new-balance-9060-eclipse-azul-marinho` — `Eclipse`
- `tenis-new-balance-9060-fall-suedes-pack-arid-stone-marrom` — `Arid Stone`
- `tenis-new-balance-9060-great-plains-marrom` — `Great Plains`
- `tenis-new-balance-9060-incense-raincloud-arid-stone-marrom` — `Incense`

Excluídos nesta rodada: `kids`, `TD`, infantis.

#### Nike Air Max 1 — novo grupo limpo

- `kasina-x-nike-air-max-1-won-ang-grey` — `Kasina Grey`
- `concepts-x-air-max-1-sp-mellow` — `Concepts Mellow`
- `tenis-nike-air-max-1-87-stranger-things-steve-harrington-branco` — `Stranger Things`
- `tenis-nike-air-max-1-x-patta-hyper-crimson-branco` — `Patta Crimson`
- `tenis-nike-air-max-1-x-patta-monarch-laranja` — `Patta Monarch`
- `tenis-nike-air-max-1-x-patta-noise-aqua-azul` — `Patta Aqua`
- `travis-scott-x-nike-air-max-1-cactus-brown` — `Cactus Brown`
- `travis-scott-x-nike-air-max-1-cactus-gold` — `Cactus Gold`

#### Nike Dunk Low/SB — preparar, mas não aplicar no mesmo pacote

Primeiros public_ok detectados incluem:

- `nike-dunk-low-ucla` — regular
- `dunk-low-light-ocean-bliss` — regular
- `dunk-low-next-nature-pink-pale-coral` — regular/Next Nature
- vários SB/collabs: Albino & Preto, April, Ben & Jerry's, Born x Raised, Orange Lobster, Crenshaw, Crushed D.C., Fly Streetwear, Grateful Dead.

Precisa de split antes de write.

## Risco

- NB 9060: mexer em grupo existente pode exigir cuidado com marker/array atual e possível bloco legacy desativado; aplicar só no DEV, com backup e static QA linha-a-linha.
- Air Max 1: grupo novo limpo, risco baixo.
- Dunk: alto impacto, mas maior risco semântico se misturar regular/SB/collabs. Não recomendado no mesmo pacote inicial.
- QA público pode ter 503/rate-limit; source/readback Admin + static QA serão prova principal no DEV.

## Recomendação de ordem

### Rodada A — recomendada agora para DEV

1. **NB 9060 adultos** — expansão curada, sem kids.
2. **Air Max 1** — novo grupo com 8 public_ok.

Motivo: combina impacto comercial + limpeza semântica + validação pública forte.

### Rodada B — depois

1. Split Nike Dunk Low regular.
2. Split Nike SB Dunk Low collabs.
3. Crocs Clog collabs/personagens se Lucas quiser breadth/novidade.

## Rollback plan se aprovado DEV

- Backup remoto do asset DEV antes do PUT.
- PUT somente no DEV `155065450718`.
- Readback/poll até marker/handles aparecerem.
- Static QA:
  - marker único;
  - arrays alinhados;
  - current excluído;
  - URLs sem `https:https://`;
  - sem `TenisMoldeLK`;
  - labels curtos.
- Confirmar Production unchanged.
- Receipt no Brain.

## Decisão necessária

Para executar upload DEV da Rodada A, Lucas precisa aprovar explicitamente:

`Aprovo DEV próximos produtos: NB 9060 adultos + Air Max 1`

Alternativas:

- Aprovar só Air Max 1.
- Aprovar só NB 9060 adultos.
- Segurar write e preparar primeiro split completo de Dunk Low/SB.
