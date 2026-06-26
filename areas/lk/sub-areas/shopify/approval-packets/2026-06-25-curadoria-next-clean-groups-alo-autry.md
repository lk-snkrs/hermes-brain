# Approval packet — Curadoria LK PDP next clean groups: Alo Suit Up + Autry Medalist

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme / PDP `lk-variante`
- **Modo:** read-only discovery + packet; **nenhum write Shopify/GitHub/tema executado neste packet**.

## Histórico verificado

Antes de recomendar novo batch, verifiquei o histórico recente e a fonte canônica:

- Batch Curadoria Bestsellers 1–3 fechado no público após PRs #90, #91 e #92.
- Sweep pós-PR #92: `19/19` handles estáveis, sem duplicidade.
- Brain analysis: `areas/lk/sub-areas/shopify/analysis/2026-06-25-curadoria-bestsellers-1-3-post92-full-sweep.md`.
- Busca de receipts/packets de 2026-06-25 confirmou que o ciclo anterior já foi executado/validado; este packet não repete o mesmo batch.

## Discovery read-only

Relatórios brutos:

- Best-sellers + coverage público: `/opt/data/profiles/lk-shopify/workdirs/curadoria-next-discovery-20260625/20260625T153415Z_best_sellers_public_coverage.json`
- Recheck Admin + público top 90: `/opt/data/profiles/lk-shopify/workdirs/curadoria-next-discovery-20260625/20260625T153919Z_top90_gap_recheck_admin.json`
- Busca por grupos candidatos: `/opt/data/profiles/lk-shopify/workdirs/curadoria-next-discovery-20260625/20260625T154032Z_model_search_candidates.json`
- Source needle readback Production: `/opt/data/profiles/lk-shopify/workdirs/curadoria-next-discovery-20260625/20260625T154049Z_production_source_needles.json`
- Preflight corrigido produto+imagem: `/opt/data/profiles/lk-shopify/workdirs/curadoria-next-discovery-20260625/20260625T154134Z_packet_candidate_corrected_preflight.json`

## Grupos que NÃO viraram novo packet

O primeiro scan bruto sugeria NB530, Vomero Premium e Nike Mind como gaps, mas o recheck específico mostrou que já estão cobertos no público:

- New Balance 530: marker `top30-nb-530`.
- Nike Vomero Premium: marker `top30-vomero-premium`.
- Nike Mind 001/002: markers `top30-nike-mind-001` e `top30-nike-mind-002-colorways`.

Portanto, não recomendo mexer neles agora.

## Grupo 1 — Alo Yoga Suit Up Trouser

**Motivo:** grupo limpo, 4 produtos ativos, mesma família/modelo (`Suit Up Trouser`) com variação por comprimento e cor. Atualmente sem Curadoria pública e sem ocorrência no source Production (`needle_counts = 0`).

| Handle | Label sugerido | Observação |
|---|---|---|
| `calca-alo-yoga-suit-up-trouser-long-preto` | Long Preto | ativo, produto+imagem 200 |
| `calca-alo-yoga-suit-up-trouser-long-azul-marinho` | Long Azul | ativo, produto+imagem 200 |
| `calca-alo-yoga-suit-up-trouser-regular-azul-marinho` | Regular Azul | ativo, produto+imagem 200 |
| `calca-alo-yoga-suit-up-trouser-regular-preto` | Regular Preto | ativo, produto+imagem 200 |

Marker proposto:

`top30-alo-suit-up-trouser-20260625`

Render esperado: cada PDP exibe até 3 alternativas, excluindo o produto atual.

## Grupo 2 — Autry Medalist Low

**Motivo:** produto rank #1 do scan (`Autry Medalist Low LL15`) e outro colorway/modelo ativo. Grupo pequeno, mas semanticamente limpo.

| Handle | Label sugerido | Observação |
|---|---|---|
| `tenis-autry-medalist-low-ll15-branco` | LL15 Branco | ativo, produto+imagem 200 |
| `tenis-autry-medalist-low-ls75-branco` | LS75 Branco | ativo, produto+imagem 200 |

Marker proposto:

`top30-autry-medalist-low-20260625`

Caveat: grupo de 2 produtos renderiza só 1 card por PDP após excluir o produto atual.

## Source/readback prévio

Production source read-only mostrou ausência desses handles/markers nos assets principais:

- `sections/lk-pdp.liquid`: `alo-suit-up-trouser = 0`, `tenis-autry-medalist-low = 0`
- `snippets/lk-variante-top30-visited-v2.liquid`: `alo-suit-up-trouser = 0`, `tenis-autry-medalist-low = 0`

## Risco

- É theme write; exige aprovação explícita.
- Alo é apparel, não sneaker. Ainda assim é variação de família/modelo clara e já há precedente de Alo Runner Curadoria. Se Lucas preferir manter Curadoria PDP só para sneaker/silhouette, executar apenas Autry ou pedir um pacote sneaker-only.
- Autry é grupo pequeno: bom por ranking, mas pouco denso.

## Plano de execução se aprovado

1. Criar split snippet dedicado para o batch.
2. Inserir render line no ativo `lk-variante-top30-visited-v2` ou section equivalente, preservando guards e sem duplicar blocos existentes.
3. Aplicar primeiro em DEV/unpublished com backup + readback + static QA.
4. Se aprovado para Production, abrir PR GitHub para `production`, mergear, aguardar Shopify sync, readback e public QA multi-round.

## Rollback

- DEV: restaurar backup dos assets tocados ou remover render line + snippet dedicado.
- Production: reverter PR/commit do batch, aguardar sync, readback dos assets e public QA dos PDPs afetados.

## Aprovações necessárias

Para aplicar em DEV/unpublished:

`Aprovo DEV Curadoria Alo Suit Up + Autry Medalist`

Para já autorizar também o merge Production **após DEV readback OK**:

`Aprovo DEV e merge Production Curadoria Alo Suit Up + Autry Medalist`

Escopo dessas aprovações: somente theme/PDP Curadoria para os 2 grupos acima. Não inclui produto, preço, estoque, metafields, campanhas, GMC, Klaviyo ou ads.
