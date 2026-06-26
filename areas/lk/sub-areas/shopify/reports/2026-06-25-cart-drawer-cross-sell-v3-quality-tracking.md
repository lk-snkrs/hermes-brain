# Cart drawer cross-sell v3 — quality review + tracking spec

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** `snippets/lk-cart-drawer.liquid` / `cart-drawer__upsell-inner`
- **Status:** análise local/Brain concluída; **nenhum write Shopify/theme/GitHub Production executado neste passo**.
- **Base:** mapa v2 public-filtered em Production após PR #100/#101.
- **Pedido:** fazer 1–3: revisar regras, criar v3 curado leve, definir tracking/telemetria.

## 1) Revisão das 26 handles / 46 regras finais

Resumo:

| Métrica | Resultado |
|---|---:|
| Regras revisadas | 46 |
| Regras mantidas | 37 |
| Regras removidas | 9 |
| Handles antes | 26 |
| Handles v3 após curadoria | 22 |
| Regras v3 após curadoria | 37 |

### Critério de curadoria leve

Mantém regra quando tem pelo menos uma dessas evidências:

1. mesmo modelo/família clara;
2. mesma família de cuidado/acessório, ex. Jason Markk;
3. mesma família Rhode;
4. mesma categoria + co-compra forte;
5. co-compra muito forte mesmo sem modelo explícito;
6. mesma categoria + sequencial curto com score alto.

Remove regra quando parece coincidência para o cart drawer:

- sequencial-only cross-category;
- beleza → sneaker/apparel sem co-compra;
- toy → sneaker;
- camiseta → sneaker sequencial-only;
- tênis de marcas/modelos sem relação clara, com pouca co-compra.

## Bons cross-sells mantidos — amostra

| X | Y | Support 180d | Mesmo pedido | Seq 30/90/180 | Conf. | Score | Motivo |
|---|---|---:|---:|---:|---:|---:|---|
| `calca-alo-yoga-suit-up-trouser-regular-azul-marinho` | `calca-alo-yoga-suit-up-trouser-regular-preto` | 6 | 6 | 0 / 0 / 0 | 0.7500 | 92.5 | mesma_categoria+co-compra_forte |
| `camiseta-saint-studio-boxy-supima-breuer-preto` | `camiseta-saint-studio-classy-suedine-supima-chairs-branco` | 6 | 3 | 3 / 3 / 3 | 1.0000 | 90.8 | mesmo_modelo/familia |
| `slide-nike-mind-001-light-smoke-grey-cinza` | `slide-nike-mind-001-black-chrome-preto` | 9 | 7 | 2 / 2 / 2 | 0.3462 | 89.6 | mesmo_modelo/familia |
| `slide-nike-mind-001-black-chrome-preto` | `slide-nike-mind-001-light-smoke-grey-cinza` | 8 | 7 | 1 / 1 / 1 | 0.3333 | 87.8 | mesmo_modelo/familia |
| `camiseta-saint-studio-classy-suedine-supima-chairs-branco` | `camiseta-saint-studio-boxy-supima-breuer-preto` | 5 | 3 | 2 / 2 / 2 | 0.4545 | 87.6 | mesmo_modelo/familia |
| `calca-alo-yoga-suit-up-trouser-regular-preto` | `calca-alo-yoga-suit-up-trouser-regular-azul-marinho` | 6 | 6 | 0 / 0 / 0 | 0.4000 | 87.5 | mesma_categoria+co-compra_forte |
| `jason-markk-repel-spray` | `jason-markk-essential-kit` | 12 | 12 | 0 / 0 / 0 | 0.3243 | 87.4 | mesmo_modelo/familia |
| `tenis-new-balance-9060-quartz-grey-cinza` | `tenis-new-balance-9060-angora-sea-salt-bege` | 4 | 3 | 1 / 1 / 1 | 0.5714 | 84.4 | mesmo_modelo/familia |
| `tenis-new-balance-9060-angora-sea-salt-bege` | `tenis-new-balance-9060-rich-oak-marrom` | 4 | 3 | 1 / 1 / 1 | 0.5000 | 84.4 | mesmo_modelo/familia |
| `tenis-new-balance-9060-angora-sea-salt-bege` | `tenis-new-balance-9060-mushroom-arid-stone-camurca` | 4 | 3 | 1 / 1 / 1 | 0.5000 | 84.4 | mesmo_modelo/familia |
| `tenis-new-balance-9060-angora-sea-salt-bege` | `tenis-new-balance-9060-quartz-grey-cinza` | 4 | 3 | 1 / 1 / 1 | 0.5000 | 84.4 | mesmo_modelo/familia |
| `tenis-new-balance-9060-team-away-grey-cinza` | `tenis-new-balance-9060-mushroom-arid-stone-camurca` | 3 | 3 | 0 / 0 / 0 | 0.7500 | 81.2 | mesmo_modelo/familia |
| `calca-saint-studio-alfaiataria-leve-prega-dupla-cinza` | `calca-saint-studio-alfaiataria-leve-prega-dupla-marrom` | 3 | 3 | 0 / 0 / 0 | 0.7500 | 81.2 | mesmo_modelo/familia |
| `slide-nike-mind-001-solar-red-vermelho` | `slide-nike-mind-001-black-chrome-preto` | 3 | 3 | 0 / 0 / 0 | 0.6000 | 81.2 | mesmo_modelo/familia |
| `calca-saint-studio-alfaiataria-leve-prega-dupla-preta` | `calca-saint-studio-alfaiataria-leve-prega-dupla-marrom` | 3 | 3 | 0 / 0 / 0 | 0.6000 | 81.2 | mesmo_modelo/familia |

## Pares removidos — amostra

| X | Y | Support 180d | Mesmo pedido | Seq 30/90/180 | Conf. | Score | Motivo |
|---|---|---:|---:|---:|---:|---:|---|
| `lip-case-rhode-by-hailey-bieber-grey-cinza` | `air-jordan-1-low-gs-se-concord` | 6 | 0 | 6 / 6 / 6 | 0.6000 | 89.1 | cross_categoria_fraco; sequencial_only |
| `lip-case-rhode-by-hailey-bieber-grey-cinza` | `camiseta-masp-x-leonilson-o-grande-rio-branco` | 6 | 0 | 0 / 6 / 6 | 0.6000 | 86.3 | cross_categoria_fraco; sequencial_only |
| `medicom-toy-bearbrick-series-48-100-toy-art-blind-box-lacrado` | `tenis-onitsuka-tiger-mexico-66-triple-black-preto` | 3 | 2 | 0 / 1 / 1 | 0.6000 | 80.2 | cross_categoria_fraco |
| `tenis-onitsuka-tiger-mexico-66-triple-black-preto` | `medicom-toy-bearbrick-series-48-100-toy-art-blind-box-lacrado` | 3 | 2 | 0 / 1 / 1 | 0.6000 | 80.2 | cross_categoria_fraco |
| `camiseta-saint-studio-boxy-supima-breuer-preto` | `tenis-nike-mind-002-light-smoke-grey-cinza` | 3 | 0 | 3 / 3 / 3 | 0.5000 | 79.6 | cross_categoria_fraco; sequencial_only |
| `camiseta-saint-studio-boxy-supima-breuer-preto` | `polo-slyce-classics-piquet-off-white` | 3 | 0 | 3 / 3 / 3 | 0.5000 | 79.6 | sequencial_only |
| `camiseta-saint-studio-boxy-supima-breuer-preto` | `tenis-nike-mind-002-black-hyper-crimson-preto` | 3 | 0 | 3 / 3 / 3 | 0.5000 | 79.6 | cross_categoria_fraco; sequencial_only |
| `tenis-on-running-cloudtilt-loewe-denim-grey-cinza` | `tenis-nike-vomero-premium-white-bright-crimson-branco` | 3 | 1 | 0 / 2 / 2 | 0.5000 | 79.2 | fraco para cart drawer |
| `tenis-on-running-cloudtilt-loewe-denim-grey-cinza` | `tenis-nike-vomero-premium-flat-stout-marrom` | 3 | 1 | 0 / 2 / 2 | 0.5000 | 79.2 | fraco para cart drawer |

## 2) Mapa v3 curado leve

Arquivo local gerado:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/cart_drawer_cross_sell_candidate_map_v3_curated_light.json`

Arquivo de auditoria das decisões:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/cross_sell_v2_rules_quality_review.json`

Diferença v2 → v3:

| Versão | Handles | Regras | Observação |
|---|---:|---:|---|
| v2 public-filtered | 26 | 46 | Ativo em Production hoje |
| v3 curated-light | 22 | 37 | Gerado localmente; ainda não aplicado no tema |

### Recomendação

A v3 é melhor como próxima iteração porque reduz pares que até têm sinal estatístico, mas parecem ruins para UX de cross-sell no carrinho.

**Não apliquei v3 em Shopify** neste passo porque isso seria novo theme/GitHub write; precisa approval explícito se Lucas quiser publicar.

## 3) Tracking / telemetria pro bloco

Objetivo: medir se o bloco melhora comportamento real, sem PII.

### Eventos propostos

#### `lk_cart_cross_sell_view`

Disparar quando o bloco renderiza ao menos 1 card.

Payload:

```json
{
  "event": "lk_cart_cross_sell_view",
  "surface": "cart_drawer",
  "map_version": "v3-curated-light-20260625",
  "strategy": "by_handle|model_fallback",
  "anchor_handles": ["<product-handle-in-cart>"],
  "rendered_handles": ["<recommended-handle>"],
  "rendered_count": 1,
  "cart_item_count": 1
}
```

#### `lk_cart_cross_sell_click`

Disparar quando clica no card/nome/imagem.

```json
{
  "event": "lk_cart_cross_sell_click",
  "surface": "cart_drawer",
  "map_version": "v3-curated-light-20260625",
  "anchor_handle": "<product-handle-in-cart>",
  "recommended_handle": "<clicked-handle>",
  "position": 1,
  "strategy": "by_handle",
  "score_bucket": "80_90"
}
```

#### `lk_cart_cross_sell_add`

Disparar quando o botão `Adicionar` do card retorna sucesso/erro.

```json
{
  "event": "lk_cart_cross_sell_add",
  "surface": "cart_drawer",
  "map_version": "v3-curated-light-20260625",
  "anchor_handle": "<product-handle-in-cart>",
  "recommended_handle": "<added-handle>",
  "position": 1,
  "status": "success|error",
  "error_type": null
}
```

### Transporte técnico recomendado

No tema, usar camada dupla e não bloquear UX:

```js
window.dataLayer = window.dataLayer || [];
window.dataLayer.push(payload);
window.dispatchEvent(new CustomEvent(payload.event, { detail: payload }));
```

Assim GTM/GA4 pode capturar depois sem acoplar o tema a um vendor específico.

### Métricas de decisão

| Métrica | Fórmula | Uso |
|---|---|---|
| CTR do bloco | `click / view` | relevância visual/copy |
| ATC rate | `cross_sell_add_success / view` | utilidade comercial |
| Click→ATC | `cross_sell_add_success / click` | qualidade do PDP/card/candidato |
| Cobertura | `views com rendered_count > 0 / cart opens` | cobertura do mapa |
| Empty/fallback rate | `sem regra ou sem candidato / cart opens` | necessidade de ampliar mapa |
| Regra vencedora | adds por `anchor_handle → recommended_handle` | limpar/expandir v4 |

### Guardrails de dados

- Não enviar nome, e-mail, telefone, customer_id, order_id ou endereço.
- Handles de produtos são OK.
- Variant ID pode ser omitido ou enviado só se necessário para debug técnico; preferência: `recommended_handle` + `position`.
- Nenhum evento deve bloquear add-to-cart ou checkout.

## Approval packet sugerido para próxima publicação

Se Lucas quiser aplicar v3 + tracking no tema:

`Aprovo DEV e merge Production cart drawer cross-sell v3 curated-light + tracking`

Escopo do próximo write:

- substituir mapa v2 public-filtered pelo v3 curated-light;
- adicionar atributos/eventos de telemetria no bloco de upsell;
- manter `/collections/all` ausente;
- não mexer em produto, preço, estoque, checkout, metafields, GMC, ads, Klaviyo, WhatsApp ou e-mail.

## Rollback futuro

Se v3/tracking for publicado e precisar voltar:

1. reverter PR da v3/tracking;
2. voltar para PR #101 / mapa v2 public-filtered;
3. validar Shopify Production readback e QA público.

`values_printed=false`.
