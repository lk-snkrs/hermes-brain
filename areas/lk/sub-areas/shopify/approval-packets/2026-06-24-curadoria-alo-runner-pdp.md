# Approval packet — Curadoria LK PDP / Alo Yoga ALO Runner

- **Data:** 2026-06-24
- **Agente:** lk-shopify
- **Superfície:** Shopify theme / PDP `lk-variante`
- **URL alvo:** https://lksneakers.com.br/products/tenis-alo-yoga-alo-runner-gravel-bege
- **Pedido Lucas:** adicionar o grid `Curadoria LK / Outras variações` (`class="lk-variante"`) para o produto ALO Runner Gravel.
- **Status:** aguardando aprovação explícita para write externo/theme.

## Histórico verificado

- Busca Brain recente por `tenis-alo-yoga-alo-runner-gravel-bege`, `alo-runner`, `Alo Runner`, `Alo Yoga`, `lk-variante`: sem receipt/packet específico prévio para este handle/grupo.
- Shopify Production readback: `snippets/lk-variante-top30-visited-v2.liquid` não contém `alo-runner` nem o handle alvo.
- Public QA atual no alvo: fetch público retornou conteúdo, mas sem evidência de `lk-variante`/Curadoria nesse PDP.

## Evidência read-only

Produto alvo resolvido no Shopify Admin:

- Product ID: `8983509598430`
- Título: `Tênis Alo Yoga ALO Runner Gravel Bege`
- Handle: `tenis-alo-yoga-alo-runner-gravel-bege`
- Status: `ACTIVE`
- Vendor: `Alo Yoga`
- Product type: `Tênis`

Grupo proposto: **mesmo modelo/silhueta ALO Runner**, current product excluído no render.

| Card | Handle | Label |
|---|---|---|
| 1 | `tenis-alo-yoga-alo-runner-espresso-marrom` | Espresso |
| 2 | `tenis-alo-yoga-alo-runner-cinza` | Cinza |
| 3 | `tenis-alo-yoga-alo-runner-preto` | Preto |
| 4 | `tenis-alo-yoga-alo-runner-branco` | Branco |
| 5 | `alo-runner-sweet-pink-rosa` | Sweet Pink |

Observação: o grupo fonte tem 6 handles incluindo o alvo `Gravel`; para o PDP Gravel, renderiza 5 cards.

## Patch local preparado

Worktree local: `/opt/data/worktrees/lk-new-theme-alo-runner-curadoria-20260624`

Arquivos alterados localmente:

1. `snippets/lk-variante-alo-runner-20260624.liquid` — novo split snippet autocontido.
2. `snippets/lk-variante-top30-visited-v2.liquid` — 1 render line adicionada:
   ```liquid
   {%- render 'lk-variante-alo-runner-20260624', product: product -%}
   ```

Sem push, sem PR, sem upload Shopify e sem Production write executado.

## QA local/read-only

Relatório: `/opt/data/profiles/lk-shopify/workdirs/curadoria-alo-runner-20260624/static_qa.json`

- Array lengths: handles=6, labels=6, images=6, titles=6.
- Handles únicos: OK.
- Target `Gravel` está no grupo: OK.
- Simulação PDP Gravel: 5 cards, current excluído.
- Public product preflight: 6/6 PDPs HTTP 200.
- CDN image preflight: 6/6 imagens HTTP 200.
- Classes canônicas presentes: `lk-variante`, `lk-variante__head`, `lk-variante__rail`, `lk-variante__media`.
- Classes proibidas ausentes: `lk-variante__grid=0`, `lk-variante__image-wrap=0`.

## Risco

- Mudança de tema, portanto exige aprovação explícita atual.
- Production deve seguir caminho GitHub/PR/merge para `production` por padrão; não usar Asset API direto em Production.
- Shopify edge/cache pode atrasar a evidência pública após merge; readback de asset + QA estática são a prova primária de source.

## Rollback

- Remover a linha de render em `snippets/lk-variante-top30-visited-v2.liquid`.
- Remover `snippets/lk-variante-alo-runner-20260624.liquid`.
- Reverter PR/commit do branch se já houver merge.

## Aprovação necessária

Para executar, Lucas precisa aprovar explicitamente um dos escopos:

1. **DEV preview:** `Aprovo DEV Curadoria Alo Runner`
2. **Production via GitHub PR/merge:** `Aprovo merge Production Curadoria Alo Runner`

Sem aprovação, permanecer somente como patch local/approval packet.

## Reminder OS

- Reminder OS loop needed: yes
- Reminder OS owner: `lk-shopify`
- Reminder OS next action: aguardar aprovação explícita de Lucas; se aprovada DEV, aplicar em theme `lk-new-theme/dev`; se aprovada Production, abrir PR/merge via GitHub e depois verificar Shopify readback/public QA.
- Reminder OS review trigger: resposta de Lucas com aprovação explícita ou alteração de escopo.
- Reminder OS evidence: este approval packet + QA local/read-only em `/opt/data/profiles/lk-shopify/workdirs/curadoria-alo-runner-20260624/static_qa.json`.
- Writes externos: nenhum executado neste packet.
