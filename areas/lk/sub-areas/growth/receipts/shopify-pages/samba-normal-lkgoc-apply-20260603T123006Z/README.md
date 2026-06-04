# Adidas Samba normal — Guia + LKGOC

UTC: 2026-06-03T12:40:23.906688+00:00

## Approval
Lucas aprovou no Telegram: `Aprovado`.

## Escopo executado
- Guia: `/pages/guia-adidas-samba`
- Coleção LKGOC: `/collections/adidas-samba`
- Collection ID: `468244332766`
- Page ID: `127404081374`
- Tema main atual: `lk-new-theme/dev` / `155065450718`

## Alterações
- Refeito guia Adidas Samba em padrão editorial/LKGOC.
- Adicionada seção “Radar de mídia” com Vogue, Who What Wear, GQ, Highsnobiety/Hypebeast.
- Adicionado bloco “Por que entra no radar da curadoria LK”.
- Seleção visual com 8 produtos, número par.
- Mobile com cards em 2 colunas onde faz sentido.
- Reescrita FAQ sem promessa pública de prazo/estoque.
- Coleção `/collections/adidas-samba`: criado snippet `snippets/lk-samba-normal-lkgoc-v4.liquid` e render no `sections/lk-collection.liquid`, porque o tema renderizava bloco hardcoded/cacheado em vez do `body_html` novo.
- Suprimido rich content antigo da coleção para `adidas-samba`, removendo visual/HTML com “prazo de entrega” e “Produtos em estoque”.

## QA público
Guia:
- Status: `200`
- Marker LKGOC: `1`
- Radar de mídia: `1`
- Veículos de moda: `1`
- Product cards: `17`
- Prazo/estoque público: prazo `0`, estoque `0`

Coleção:
- Status: `200`
- Snippet marker: `1`
- Radar de mídia: `2`
- Veículos de moda: `2`
- Prazo/estoque público: prazo `0`, estoque `0`

## Screenshots
- `samba-guide-mobile.png`
- `samba-collection-mobile.png`

## Rollback
- Guia: restaurar `page.before.json` em Page ID `127404081374`.
- Coleção body: restaurar `collection.before.json` em Collection ID `468244332766`.
- Tema: restaurar `sections__lk-collection.before-render-snippet-patch.liquid` em `sections/lk-collection.liquid` e remover/ignorar `snippets/lk-samba-normal-lkgoc-v4.liquid` se necessário.
