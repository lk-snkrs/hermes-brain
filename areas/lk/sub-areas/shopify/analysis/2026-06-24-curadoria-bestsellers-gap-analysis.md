# Análise — Best sellers x Curadoria LK PDP

- **Data:** 2026-06-24
- **Agente:** lk-shopify
- **Superfície:** Shopify theme / Curadoria LK PDP (`lk-variante`)
- **Modo:** read-only; nenhum write externo.
- **Pedido:** analisar best sellers da loja e relações com possíveis falhas/falsas relações e o que falta implementar/melhorar na Curadoria para sugerir outros produtos.

## Fontes

- Shopify público: `/collections/all?sort_by=best-selling`, páginas 1–5, 100 produtos únicos.
- Shopify Admin read-only por handle para título/vendor/tags/status/imagem.
- Shopify Production readback do tema `155065417950` para snippets `lk-variante*`.
- Public PDP marker probe para `data-lk-variante`.

Artifacts:

- Raw analysis: `/opt/data/profiles/lk-shopify/workdirs/curadoria-bestseller-analysis-20260624/20260624T194901Z_bestseller_curadoria_analysis.json`
- Refined summary: `/opt/data/profiles/lk-shopify/workdirs/curadoria-bestseller-analysis-20260624/20260624T194935Z_refined_summary.json`

## Leitura executiva

A Curadoria já cobre bem alguns campeões importantes: Moon Shoe Jacquemus, Vomero Premium core, New Balance 530, parte forte de Mexico 66, NB204L, NB9060 e vários Onitsuka.

Os maiores gaps acionáveis em best sellers são:

1. **Onitsuka Tiger Mexico 66 / Sabot / SD** — cluster grande, top ranks fortes, mas 6 gaps públicos entre top100.
2. **New Balance 9060** — 5 gaps públicos entre top100; alguns aparecem em source mas não renderizam público.
3. **Adidas Samba OG / Samba Jane** — Samba OG tem 5 gaps; Samba Jane tem 3 gaps e source/public divergente.
4. **New Balance 204L / 530** — poucos gaps, mas ranks relevantes; bom para repair incremental.
5. **Autry Medalist rank #1** — best seller #1 sem Curadoria; só virar grupo se houver outros Autry/Medalist públicos suficientes.

## Oportunidades principais

### Onitsuka Tiger Mexico 66

- Top100 count: 24
- Covered: 18
- Gaps: 6
- Melhor rank: #2

Gaps:

| Rank | Produto | Handle |
|---:|---|---|
| 39 | Mexico 66 Birch Green | `tenis-onitsuka-tiger-mexico-66-brich-green-branco` |
| 82 | Mexico 66 Sabot Oatmeal Habanero | `tenis-onitsuka-tiger-mexico-66-sabot-oatmeal-habanero-bege` |
| 92 | Mexico 66 SD Vin Clay Canyon Cream | `tenis-onitsuka-tiger-mexico-66-sd-clay-canyon-cream-marrom` |
| 93 | Mexico 66 SD Licorice Brown Champagne | `tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom` |
| 94 | Mexico 66 Gold White | `tenis-onitsuka-tiger-mexico-66-gold-white-dourado` |
| 98 | Mexico 66 Sabot Black Cream | `tenis-onitsuka-tiger-mexico-66-sabot-black-cream-preto` |

Recomendação: split por subfamília, sem misturar todos:
- Mexico 66 regular
- Mexico 66 SD
- Mexico 66 Sabot

### New Balance 9060

- Top100 count: 13
- Covered: 8
- Gaps: 5
- Melhor rank: #4

Gaps:

| Rank | Produto | Handle |
|---:|---|---|
| 63 | 9060 Rose Sugar Angora | `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` |
| 76 | 9060 Moonrock Linen Dark Artic Grey | `tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza` |
| 77 | 9060 Angora Sea Salt | `tenis-new-balance-9060-angora-sea-salt-bege` |
| 78 | 9060 Black Cement Black Cat | `new-balance-9060-black-cement-black-cat-preto` |
| 99 | 9060 Linen Burgundy | `tenis-new-balance-9060-linen-burgundy-bege` |

Recomendação: repair/expansão do grupo 9060 com cap 5; conferir se alguns já estão no source mas não renderizam por edge/condição.

### Adidas Samba OG / Samba Jane

Samba OG:
- Top100 count: 9
- Covered: 4
- Gaps: 5
- Melhor rank: #5

Gaps:
- `tenis-adidas-samba-og-cream-white-core-black-bege`
- `tenis-adidas-samba-og-core-black-wonder-white-preto`
- `tenis-adidas-samba-og-preloved-red-leopard-pack-marrom`
- `tenis-adidas-samba-og-crochet-pack-orbit-green-verde`
- `tenis-adidas-samba-og-off-white-cyber-metallic-branco`

Samba Jane:
- Top100 count: 3
- Covered público: 0
- Gaps: 3

Gaps:
- `tenis-adidas-samba-jane-scarlet-gum-vermelho`
- `tenis-adidas-samba-jane-white-black-branco`
- `tenis-adidas-samba-jane-black-white-gum-preto`

Recomendação: separar OG regular/crochet/leopard de Samba Jane. Samba Jane é grupo pequeno fechado e pode render 2 cards por PDP.

### New Balance 204L / 530

Gaps pontuais:

- NB204L: `tenis-new-balance-204l-sea-salt-linen-bege`
- NB530: `tenis-new-balance-530-arid-stone-cinza`

Recomendação: repair incremental, não batch prioritário isolado.

### Autry Medalist

- Rank #1: `tenis-autry-medalist-low-ll15-branco`
- Sem Curadoria.

Recomendação: antes de implementar, fazer scan Autry/Medalist. Se houver 3+ produtos públicos relacionados, vira prioridade alta; se for produto único, não forçar Curadoria no PDP.

## Possíveis falhas/falsas relações

Não apareceu um falso positivo claro do tipo “produto com marker totalmente errado”.

O que apareceu foi mais importante operacionalmente: **source contém handle, mas público não renderizou Curadoria**. Isso pode ser edge/cache, render condition, grupo antigo com handle em comentário/source, ou produto/template peculiar.

Casos para revisão focada:

- Samba Jane: 3 handles parecem estar no source, mas não renderizaram público.
- NB9060: alguns handles estão no source mas não renderizaram público.
- Mexico 66: alguns gaps também aparecem como source/public divergente.
- Yeezy 350 Onyx e AJ1 Mid Panda apareceram como source/public divergente, mas precisam checar se o grupo existe e se deveria renderizar nesses PDPs.

## O que não deve entrar automaticamente em Curadoria PDP

Best sellers de outras categorias não devem virar Curadoria de sneaker sem lógica própria:

- Rhode beauty/cases
- Jason Markk cleaning kit
- Camisetas/calças/bonés/apparel
- Havaianas/Crocs collab isolados

Para esses, a melhor superfície pode ser cart drawer/upsell ou collection recommendations, não `lk-variante` de PDP sneaker.

## Ordem recomendada

1. **Mexico 66 repair/expansion**, separado por regular/SD/Sabot.
2. **NB9060 repair/expansion**, cap 5 e readback público focado nos handles divergentes.
3. **Samba OG + Samba Jane**, separados; Samba Jane como grupo pequeno fechado.
4. **Autry Medalist scan** para confirmar se há família suficiente.
5. **NB204L + NB530 pontuais** como batch pequeno de manutenção.

## Próximo passo seguro

Preparar approval packet do próximo batch **sem write externo**:

- `Mexico 66 regular/SD/Sabot repair`
- `NB9060 expansion`
- `Samba OG/Jane repair`

Depois Lucas decide se executa em DEV/Production.
