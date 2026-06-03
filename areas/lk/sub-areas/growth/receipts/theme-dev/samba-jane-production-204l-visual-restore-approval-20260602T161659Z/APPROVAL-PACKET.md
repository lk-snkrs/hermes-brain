# Approval packet — restaurar visual 204L da coleção Samba Jane

## Diagnóstico
- O print do Lucas mostra layout default branco, não padrão 204L.
- Asset production atual tem `0` ocorrências de `lk-samba-jane-coll-preview`.
- A versão dev aprovada em 2026-05-26 tinha o bloco visual `lk-samba-jane-coll-preview` com hero escuro, collage editorial e regra para esconder a trust strip.

## Mudança proposta
- Asset: `sections/lk-collection.liquid`
- Theme production: `155065417950`
- Inserir CSS/HTML/JS do bloco visual Samba Jane antes da trust strip.
- Escopo condicionado a `collection.handle == 'adidas-samba-jane'`.
- Não mexe em PDP, preço, produto, checkout, GMC, Klaviyo ou campanhas.

## Impacto esperado
- Topo da coleção volta ao padrão 204L: fundo preto `#101010`, curadoria LK, collage editorial e trust strip oculta nessa coleção.
- Mantém guia dedicado via painel existente abaixo do grid.

## Risco
- Médio/baixo: alteração em section global, mas Liquid/HTML é condicionado ao handle Samba Jane.
- Cache público Shopify pode demorar a refletir na URL limpa; section render deve refletir primeiro.

## Rollback
- Reaplicar `sections__lk-collection.production.before.liquid`.

## Aprovação necessária
- Write em Shopify production.
