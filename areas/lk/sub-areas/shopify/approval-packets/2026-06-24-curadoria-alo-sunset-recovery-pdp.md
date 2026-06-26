# Approval packet — Curadoria LK PDP / Alo Sunset + Recovery Mode

- **Data:** 2026-06-24
- **Agente:** lk-shopify
- **Superfície:** Shopify theme / PDP `lk-variante`
- **Pedido Lucas:** “vamos continuar” após recomendação de explorar Alo Sunset + Alo Recovery Mode.
- **Status:** patch local preparado; aguardando aprovação explícita para DEV/Production writes.

## Histórico verificado

- Após o merge do ALO Runner, Production source contém `lk-variante-alo-runner-20260624`.
- Source Production atual **não contém** os handles de Sunset/Recovery Mode.
- Public marker probe nos 6 handles retornou `marker_count=0`, ou seja, sem bloco Curadoria LK renderizado para esses grupos.
- Não houve write externo neste packet.

## Grupos propostos

### Grupo 1 — Alo Yoga Sunset Sneaker

Marker: `top30-alo-sunset-colorways`

| Produto | Handle | Label |
|---|---|---|
| Sunset Black | `tenis-alo-yoga-alo-sunset-sneaker-black-preto-1069543022` | Black |
| Sunset Espresso | `tenis-alo-yoga-alo-sunset-sneaker-espresso-marrom-1069543068` | Espresso |
| Sunset Sandstone | `tenis-alo-yoga-alo-sunset-sneaker-sandstone-bege` | Sandstone |

### Grupo 2 — Alo Yoga Recovery Mode

Marker: `top30-alo-recovery-mode-colorways`

| Produto | Handle | Label |
|---|---|---|
| Recovery Mode Clay | `tenis-alo-yoga-alo-recovery-mode-sneaker-clay-1069542922` | Clay |
| Recovery Mode Pink Wild Rose | `tenis-alo-yoga-alo-recovery-mode-sneaker-pink-wild-rose-rosa-1069542992` | Pink Wild Rose |
| Recovery Mode Pink/White | `tenis-alo-yoga-alo-recovery-mode-sneaker-pink-wild-rose-rosa-copia` | Pink/White |

## Patch local preparado

Worktree local:

`/opt/data/worktrees/lk-new-theme-alo-runner-curadoria-20260624`

Arquivos alterados localmente:

1. `snippets/lk-variante-alo-sunset-recovery-20260624.liquid` — novo split snippet autocontido com 2 grupos.
2. `snippets/lk-variante-top30-visited-v2.liquid` — 1 render line adicionada:
   ```liquid
   {%- render 'lk-variante-alo-sunset-recovery-20260624', product: product -%}
   ```

Sem upload Shopify, sem PR/push e sem Production write executado neste packet.

## QA local/read-only

Relatórios:

- Scan Shopify/public: `/opt/data/profiles/lk-shopify/workdirs/curadoria-alo-next-20260624/20260624T150943Z_handle_scan.json`
- Static QA: `/opt/data/profiles/lk-shopify/workdirs/curadoria-alo-next-20260624/20260624T151135Z_static_qa.json`

Resultado:

- 6/6 produtos encontrados em Shopify Admin como `ACTIVE` e públicos.
- 6/6 PDPs públicas HTTP 200.
- 6/6 imagens CDN HTTP 200.
- Arrays alinhados: cada grupo com handles=3, labels=3, images=3, titles=3.
- Simulação: current product excluído; cada PDP renderiza 2 cards.
- Classes canônicas presentes: `lk-variante`, `lk-variante__head`, `lk-variante__rail`, `lk-variante__media`.
- Classes proibidas ausentes: `lk-variante__grid=0`, `lk-variante__image-wrap=0`.

## Risco

- Grupos pequenos: cada PDP terá 2 cards, não 5. Isso é semanticamente limpo, mas visualmente menos denso.
- Mudança de tema exige aprovação explícita.
- Production deve seguir GitHub PR/merge para `production`; sem Asset API direto em Production.
- Após merge, public QA pode sofrer edge/cache intermitente como no ALO Runner.

## Rollback

- Remover a linha de render em `snippets/lk-variante-top30-visited-v2.liquid`.
- Remover `snippets/lk-variante-alo-sunset-recovery-20260624.liquid`.
- Se já mergeado, reverter o PR/commit correspondente.
- Se aplicado em DEV, restaurar backup DEV gerado antes do upload.

## Aprovação necessária

Para executar, Lucas precisa aprovar explicitamente:

1. **DEV preview:** `Aprovo DEV Curadoria Alo Sunset Recovery`
2. **Production via GitHub PR/merge:** `Aprovo merge Production Curadoria Alo Sunset Recovery`

Pode aprovar só DEV primeiro se quiser validar antes do merge.

## Reminder OS

- Reminder OS loop needed: yes
- Reminder OS owner: `lk-shopify`
- Reminder OS next action: aguardar aprovação explícita de Lucas; se aprovada DEV, aplicar em `lk-new-theme/dev`; se aprovada Production, abrir PR/merge via GitHub e depois verificar Shopify readback/public QA.
- Reminder OS review trigger: resposta de Lucas com aprovação explícita ou mudança de escopo.
- Reminder OS evidence: este approval packet + QA local/read-only nos paths acima.
- Writes externos: nenhum executado neste packet.
