# LK Variante — plano 3: correção client-side via asset já carregado

Data UTC: 2026-06-03T00:50:20.359251+00:00

## Diagnóstico

As PDPs stale ainda carregam `assets/lk-footer.js` do tema live (`t/91`) mesmo quando o HTML Liquid do bloco `lk-variante` vem antigo. Isso cria uma via de correção sem depender do re-render do HTML do produto: alterar um asset global já referenciado pelo HTML stale.

Asset observado em HTML stale: `https://lksneakers.com.br/cdn/shop/t/91/assets/lk-footer.js?v=64977926636341263331780325147`

## Proposta técnica

Adicionar ao fim de `assets/lk-footer.js` um IIFE pequeno e idempotente que:

1. roda somente no navegador;
2. procura `.lk-variante a[href*="/products/"]`;
3. identifica o handle do produto pelo href;
4. troca apenas o texto do `.lk-variante__label` quando o handle estiver no mapa aprovado;
5. não altera imagens, links, preço, estoque, botão, variantes, carrinho, checkout ou coleção.

## Escopo inicial do mapa

- AJ1 High regular: 5 labels
- Alo Serenity: 5 labels
- Adidas Sambae: 5 labels
- Adidas Tokyo: 5 labels
- Shox TL: 5 labels
- Yeezy 350: 5 labels
- Foam Runner: 5 labels

AJ1 Mid e NB 530 ficam fora do mapa porque já aparecem corretos/controle no HTML analisado; podem ser incluídos depois se necessário.

## Artefatos locais

- Atual público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/client-side-correction-plan-20260603/lk-footer.current-public.js`
- Proposto local: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/client-side-correction-plan-20260603/lk-footer.proposed-client-side-variante-fix.js`

## Risco

Baixo/médio: é JS global de footer, mas o seletor é extremamente restrito a `.lk-variante`. O maior risco é visual tardio: label antigo pode piscar por fração de segundo antes do JS executar.

## Rollback

Restaurar backup pré-write de `assets/lk-footer.js` ou remover somente o IIFE `LK Variante stale HTML client-side label correction`.

## Gate

Qualquer upload para Shopify theme é write. Exige aprovação explícita atual de Lucas antes de Dev ou Production.
