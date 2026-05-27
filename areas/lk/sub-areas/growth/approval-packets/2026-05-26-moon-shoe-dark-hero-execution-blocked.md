# Execution blocked — Moon Shoe dark hero

Data: 2026-05-26

## Pedido limpo

Lucas pediu para aplicar em produção o hero escuro aprovado para a página Moon Shoe.

## Destino

- Shopify production theme: `155065417950`
- Página: `https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk`

## Status

Não aplicado neste turno por boundary read-only/approval-packet do roteamento atual.

## Evidências disponíveis

- Approval packet criado: `2026-05-26-moon-shoe-dark-hero-approval.md`
- Kicker já reduzido para `9.5px` em turno anterior com readback Shopify Admin OK.
- CSS proposto preserva corpo branco e altera apenas o hero inicial para bloco escuro.

## Preview técnico aprovado

Hero inicial com fundo `#111111`, H1 e textos em off-white, CTA principal invertido branco/preto, CTA secundário transparente com borda clara.

## Risco

Baixo/médio: alteração visual customer-facing acima da dobra em produção.

## Rollback

Remover o bloco CSS `LK hotfix proposal 2026-05-26: Moon Shoe dark editorial hero` ou restaurar backups em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/`

## Próximo passo

Executar em um turno sem boundary read-only, usando a aprovação explícita de Lucas e verificando via Shopify Admin readback + browser público desktop/mobile.
