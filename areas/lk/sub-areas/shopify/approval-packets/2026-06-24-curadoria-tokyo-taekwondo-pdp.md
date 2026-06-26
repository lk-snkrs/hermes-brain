# Approval packet — Curadoria LK PDP / Adidas Tokyo Mary Jane + Taekwondo regular/Mei

- **Data:** 2026-06-24
- **Agente:** lk-shopify
- **Superfície:** Shopify theme / PDP `lk-variante`
- **Pedido Lucas:** “Seguir os dois” após scan apontar dois próximos gaps: Adidas Tokyo Mary Jane e Adidas Taekwondo regular/Mei leftovers.
- **Status:** patch local preparado; aguardando aprovação explícita para DEV/Production writes.

## Histórico verificado

- Antes de sugerir o batch, foi feito scan read-only de Production/source e público.
- Source Production atual foi relido do Shopify para evitar branch local stale.
- Gaps prontos encontrados: 3 Tokyo Mary Jane + 3 Taekwondo regular/Mei.
- Não houve upload Shopify, PR, merge ou write externo neste packet.

## Grupos propostos

### Grupo 1 — Adidas Tokyo Mary Jane

Marker: `top30-adidas-tokyo-mary-jane-20260624`

| Produto | Handle | Label |
|---|---|---|
| Adidas Tokyo Mary Jane Sandy Pink Earth Strata | `tenis-adidas-tokyo-mary-jane-sandy-pink-earth-strata-rosa` | Sandy Pink |
| Adidas Tokyo Mary Jane Cream White Red Gold Metallic | `tenis-adidas-tokyo-mary-jane-cream-white-red-gold-metallic-creme` | Cream Red Gold |
| Adidas Tokyo Mary Jane Crystal Sky Cream White | `tenis-adidas-tokyo-mary-jane-crystal-sky-cream-white-azul` | Crystal Sky |

### Grupo 2 — Adidas Taekwondo regular/Mei leftovers

Marker: `top30-adidas-taekwondo-regular-mei-20260624`

| Produto | Handle | Label |
|---|---|---|
| adidas Taekwondo Cloud White | `tenis-adidas-taekwondo-cloud-white-branco` | Cloud White |
| adidas Taekwondo Core Black | `tenis-adidas-taekwondo-core-black-preto` | Core Black |
| Adidas Taekwondo Mei Ballet Clear Pink Gum | `sapatilha-onitsuka-tiger-wmns-taekwondo-mei-ballet-clear-pink-gum-camurca` | Mei Clear Pink |

## Patch local preparado

Worktree local:

`/opt/data/worktrees/lk-new-theme-tokyo-taekwondo-20260624`

Arquivos preparados:

1. `snippets/lk-variante-tokyo-taekwondo-20260624.liquid` — novo split snippet com 2 grupos.
2. `snippets/lk-variante-top30-visited-v2.liquid` — render line adicionada após o batch Vomero/Mind/Taekwondo CLOT:
   ```liquid
   {%- render 'lk-variante-tokyo-taekwondo-20260624', product: product -%}
   ```

Observação: a worktree foi reconciliada com Shopify Production readback para incluir as alterações recentes de PR #87/#88, porque o `origin/production` local estava stale.

## QA local/read-only

Relatório:

`/opt/data/profiles/lk-shopify/workdirs/curadoria-tokyo-taekwondo-20260624/20260624T190954Z_static_preflight.json`

Resultado:

- 6/6 PDPs públicas HTTP 200.
- 6/6 imagens CDN HTTP 200.
- Dois grupos com arrays alinhados: handles=3, labels=3, images=3, titles=3.
- Handles únicos por grupo.
- Simulação: current product excluído; cada PDP renderiza 2 cards.
- Classes canônicas presentes: `lk-variante`, `lk-variante__head`, `lk-variante__rail`, `lk-variante__media`.
- Classes proibidas ausentes: `lk-variante__grid=0`, `lk-variante__image-wrap=0`.

## Risco

- Grupos pequenos renderizam 2 cards por PDP.
- Taekwondo regular/Mei mistura dois regulares (`Cloud White`, `Core Black`) com um `Mei Ballet`; é aceitável como leftover/repair pequeno, mas semanticamente menos limpo que CLOT separado.
- Theme write exige aprovação explícita.
- Production deve seguir GitHub PR/merge; sem direct Asset API Production.
- Public QA pós-merge pode ter edge/cache intermitente.

## Rollback

- Remover render line em `snippets/lk-variante-top30-visited-v2.liquid`.
- Remover `snippets/lk-variante-tokyo-taekwondo-20260624.liquid`.
- Se já mergeado, reverter o PR/merge correspondente.
- Se aplicado em DEV, restaurar backup DEV gerado antes do upload.

## Aprovação necessária

Para executar os dois grupos, Lucas precisa aprovar explicitamente:

1. **DEV:** `Aprovo DEV Curadoria Tokyo Taekwondo`
2. **Production:** `Aprovo merge Production Curadoria Tokyo Taekwondo`

Pode aprovar ambos na mesma mensagem se quiser execução sequencial: DEV readback primeiro, depois PR/merge Production e QA público.

## Writes externos

Nenhum executado neste packet. Apenas read-only, patch local e documentação Brain.
