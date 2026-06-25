# Approval packet — Curadoria LK PDP / Best sellers gaps 1–3

- **Data:** 2026-06-24
- **Agente:** lk-shopify
- **Superfície:** Shopify theme / PDP `lk-variante`
- **Pedido Lucas:** “Fazer do 1 ao 3” após análise de best sellers apontar: Mexico 66, NB9060 e Samba/Samba Jane.
- **Status:** patch local preparado; aguardando aprovação explícita para DEV/Production writes.

## Histórico verificado

- Análise best sellers registrada em `areas/lk/sub-areas/shopify/analysis/2026-06-24-curadoria-bestsellers-gap-analysis.md`.
- Source Production foi relido do Shopify antes do patch para evitar branch local stale após PRs recentes.
- Patch local preparado em split snippet próprio, sem upload Shopify, sem PR e sem merge ainda.

## Grupos propostos

### 1A) Onitsuka Tiger Mexico 66 regular expansion

Marker: `top30-mexico66-regular-expansion-20260624`

| Produto | Handle | Label |
|---|---|---|
| Mexico 66 Birch Green | `tenis-onitsuka-tiger-mexico-66-brich-green-branco` | Birch Green |
| Mexico 66 Gold White | `tenis-onitsuka-tiger-mexico-66-gold-white-dourado` | Gold White |

### 1B) Onitsuka Tiger Mexico 66 Sabot expansion

Marker: `top30-mexico66-sabot-expansion-20260624`

| Produto | Handle | Label |
|---|---|---|
| Mexico 66 Sabot Oatmeal Habanero | `tenis-onitsuka-tiger-mexico-66-sabot-oatmeal-habanero-bege` | Oatmeal Habanero |
| Mexico 66 Sabot Black Cream | `tenis-onitsuka-tiger-mexico-66-sabot-black-cream-preto` | Black Cream |

### 1C) Onitsuka Tiger Mexico 66 SD expansion

Marker: `top30-mexico66-sd-expansion-20260624`

| Produto | Handle | Label |
|---|---|---|
| Mexico 66 SD Clay Canyon Cream | `tenis-onitsuka-tiger-mexico-66-sd-clay-canyon-cream-marrom` | Clay Canyon |
| Mexico 66 SD Licorice Brown Champagne | `tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom` | Licorice Brown |

### 2) New Balance 9060 expansion

Marker: `top30-nb-9060-expansion-20260624`

| Produto | Handle | Label |
|---|---|---|
| 9060 Rose Sugar Angora | `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` | Rose Sugar |
| 9060 Moonrock Linen Dark Artic Grey | `tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza` | Moonrock Linen |
| 9060 Angora Sea Salt | `tenis-new-balance-9060-angora-sea-salt-bege` | Angora Sea Salt |
| 9060 Black Cement Black Cat | `new-balance-9060-black-cement-black-cat-preto` | Black Cat |
| 9060 Linen Burgundy | `tenis-new-balance-9060-linen-burgundy-bege` | Linen Burgundy |

### 3A) Adidas Samba OG expansion

Marker: `top30-adidas-samba-og-expansion-20260624`

| Produto | Handle | Label |
|---|---|---|
| Samba OG Cream White Core Black | `tenis-adidas-samba-og-cream-white-core-black-bege` | Cream Black |
| Samba OG Core Black Wonder White | `tenis-adidas-samba-og-core-black-wonder-white-preto` | Black Wonder |
| Samba OG Preloved Red Leopard Pack | `tenis-adidas-samba-og-preloved-red-leopard-pack-marrom` | Red Leopard |
| Samba OG Crochet Pack Orbit Green | `tenis-adidas-samba-og-crochet-pack-orbit-green-verde` | Crochet Green |
| Samba OG Off White Cyber Metallic | `tenis-adidas-samba-og-off-white-cyber-metallic-branco` | Cyber Metallic |

### 3B) Adidas Samba Jane

Marker: `top30-adidas-samba-jane-20260624`

| Produto | Handle | Label |
|---|---|---|
| Samba Jane Scarlet Gum | `tenis-adidas-samba-jane-scarlet-gum-vermelho` | Scarlet Gum |
| Samba Jane White Black | `tenis-adidas-samba-jane-white-black-branco` | White Black |
| Samba Jane Black White Gum | `tenis-adidas-samba-jane-black-white-gum-preto` | Black Gum |

## Patch local preparado

Worktree local:

`/opt/data/worktrees/lk-new-theme-bestsellers-1-3-curadoria-20260624`

Arquivos preparados:

1. `snippets/lk-variante-bestsellers-1-3-20260624.liquid` — novo split snippet com 6 subgrupos.
2. `snippets/lk-variante-top30-visited-v2.liquid` — render line:
   ```liquid
   {%- render 'lk-variante-bestsellers-1-3-20260624', product: product -%}
   ```

## QA local/read-only

Relatório:

`/opt/data/profiles/lk-shopify/workdirs/curadoria-bestsellers-1-3-20260624/20260624T200244Z_static_preflight.json`

Resultado:

- 19/19 PDPs públicas HTTP 200.
- 19/19 imagens CDN HTTP 200.
- Arrays alinhados em todos os grupos: handles/labels/images/titles.
- Handles únicos por grupo.
- Current product excluído em simulação.
- Classes canônicas presentes: `lk-variante`, `lk-variante__head`, `lk-variante__rail`, `lk-variante__media`.
- Classes proibidas ausentes: `lk-variante__grid=0`, `lk-variante__image-wrap=0`.

## Riscos / caveats

- Mexico 66 regular/Sabot/SD expansion tem apenas 2 handles por subgrupo; cada PDP renderiza **1 card**. Isso preserva semântica forte, mas visualmente é menos denso.
- NB9060 e Samba OG são grupos mais densos e renderizam até 4 alternativas por PDP neste split.
- Samba Jane tem 3 handles e renderiza 2 cards por PDP.
- Production deve seguir GitHub PR/merge; sem direct Asset API Production.
- Public QA pós-merge pode ter edge/cache intermitente.

## Rollback

- Remover render line em `snippets/lk-variante-top30-visited-v2.liquid`.
- Remover `snippets/lk-variante-bestsellers-1-3-20260624.liquid`.
- Se já mergeado, reverter o PR/merge correspondente.
- Se aplicado em DEV, restaurar backup DEV gerado antes do upload.

## Aprovação necessária

Para executar este batch, Lucas precisa aprovar explicitamente:

1. **DEV:** `Aprovo DEV Curadoria Bestsellers 1-3`
2. **Production:** `Aprovo merge Production Curadoria Bestsellers 1-3`

Pode aprovar ambos na mesma mensagem para execução sequencial: DEV readback primeiro, depois PR/merge Production e QA público.

## Writes externos

Nenhum executado neste packet. Apenas read-only, patch local e documentação Brain.
