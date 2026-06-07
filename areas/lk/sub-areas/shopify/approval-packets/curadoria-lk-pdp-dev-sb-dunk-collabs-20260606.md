# Approval packet — Curadoria LK PDP — DEV SB Dunk Low collabs

Data: 2026-06-06
Status: read-only packet preparado; nenhum upload/write feito nesta etapa

## Contexto

Lucas disse: `Aprovo seguir` após o merge Production do grupo Dunk Low regular. Interpretei como continuidade segura/read-only para preparar o próximo lote, não como autorização de upload ainda, porque o pacote exato de candidatos não tinha sido apresentado antes.

## Escopo proposto para DEV

Tema DEV: `155065450718` (`unpublished`)
Asset alvo: `snippets/lk-variante-top30-visited-v2.liquid`
Marker proposto:

`top30-nike-sb-dunk-low-collabs-breadth`

Grupo: Nike SB Dunk Low collabs/cápsulas premium, separado do Dunk Low regular recém-merged.

## Produtos propostos

1. `albino-preto-x-nike-sb-dunk-low-pearl-white`
   - Label curto: `Albino & Preto`
   - Título Admin: Tênis Albino & Preto x Nike SB Dunk Low Pearl White Bege

2. `april-skateboards-x-nike-sb-dunk-low-turbo-green`
   - Label curto: `April Turbo`
   - Título Admin: Tênis April Skateboards x Nike SB Dunk Low Turbo Green Azul

3. `ben-jerrys-x-dunk-low-sb-chunky-dunky`
   - Label curto: `Chunky Dunky`
   - Título Admin: Tênis Ben & Jerry's x Dunk Low SB Chunky Dunky Colorido

4. `born-x-raised-x-nike-sb-dunk-low-one-block-at-a-time`
   - Label curto: `Born x Raised`
   - Título Admin: Tênis Born Raised x Nike SB Dunk Low One Block At A Time Azul

5. `concepts-x-nike-sb-dunk-low-orange-lobster`
   - Label curto: `Orange Lobster`
   - Título Admin: Tênis Concepts x Nike SB Dunk Low Orange Lobster Laranja

6. `crenshaw-skate-club-x-nike-sb-dunk-low`
   - Label curto: `Crenshaw`
   - Título Admin: Tênis Crenshaw Skate Club x Nike SB Dunk Low Multicolor

7. `fly-streetwear-x-dunk-low-pro-sb-gardenia`
   - Label curto: `Fly Gardenia`
   - Título Admin: Tênis Fly Streetwear x Dunk Low Pro SB 'Gardenia' Azul

8. `grateful-dead-x-nike-sb-dunk-low-yellow-bear`
   - Label curto: `Grateful Dead`
   - Título Admin: Tênis Grateful Dead x Nike SB Dunk Low Yellow Bear Amarelo

9. `jarritos-x-nike-sb-dunk-low`
   - Label curto: `Jarritos`
   - Título Admin: Tênis Jarritos x Nike SB Dunk Low Branco/Verde

10. `huf-x-nike-sb-dunk-low-new-york`
    - Label curto: `HUF New York`
    - Título Admin: Tênis HUF x Nike SB Dunk Low New York Branco/Azul

## Evidência read-only

Scanner executado:

`/opt/data/tmp/lk_curadoria_dunk_low_regular_split_readonly_20260606.py`

Output:

`/opt/data/tmp/lk_curadoria_dunk_low_regular_split_readonly_20260606.json`

Contagem:

- `regular`: 121 total / 27 cobertos / 94 descobertos / 30 validados public-ok por urllib
- `sb_collab`: 65 total / 13 cobertos / 52 descobertos
- selecionados: 10/10 ainda não cobertos em DEV+Production
- imagens: 10/10 HTTP 200

Validação pública:

- `mcp_fetch_fetch` conseguiu extrair páginas dos candidatos selecionados e confirmou conteúdo PDP para Jarritos, Albino & Preto, April, Chunky Dunky, Born x Raised, Orange Lobster, Crenshaw, Fly Gardenia, Grateful Dead, HUF New York.
- `urllib` direto recebeu `429` nas páginas SB, então a validação pública por urllib ficou anti-bot/inconclusiva; não é falha de produto porque `mcp_fetch_fetch` leu as PDPs e as imagens responderam 200.

## Interpretação semântica

Aprovável como grupo único porque todos são:

- Nike SB Dunk Low / Dunk Low Pro SB
- collabs/cápsulas premium
- adultos/publicados
- diferentes do grupo Dunk Low regular já aplicado

Não misturei TD/kids nem Dunk High.

## Risco

Baixo no source, médio no QA público imediato:

- Baixo: só adiciona bloco de Curadoria, sem produto/preço/estoque.
- Médio: páginas públicas SB deram `429` para urllib, então preview público pode precisar de fetch/browser ou marcar anti-bot-inconclusivo.

## Rollback DEV

Antes do upload DEV, criar backup do asset atual e restaurar esse backup se qualquer validação estática/readback falhar.

## Aprovação necessária

Para upload em DEV, a aprovação precisa ser explícita para este pacote, por exemplo:

`Aprovo DEV SB Dunk collabs`

Isso autoriza apenas o upload no tema DEV/unpublished, não Production.
