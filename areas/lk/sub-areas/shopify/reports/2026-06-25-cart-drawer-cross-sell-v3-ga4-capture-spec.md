# Cart drawer cross-sell v3 — GA4/dataLayer capture spec

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** LK Sneakers storefront / cart drawer cross-sell
- **Status:** read-only/spec; **nenhum write em GA4/GTM/Shopify executado neste passo**.
- **Base:** PR #102 ativo em Production com eventos `lk_cart_cross_sell_view`, `lk_cart_cross_sell_click`, `lk_cart_cross_sell_add` no tema.

## Detecção pública read-only

Arquivos/evidência local:

- `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/gtm_ga4_public_detection_v3_tracking.json`

| URL | Status | dataLayer | GTM | GA4 ID | v3/eventos no HTML | `/collections/all` |
|---|---:|---:|---:|---|---:|---:|
| Home | 200 | sim | não detectado | `G-HVFGK8SQQT` | sim | não |
| PDP referência | 200 | sim | não detectado | `G-HVFGK8SQQT` | sim | não |

Interpretação:

- A loja já expõe `dataLayer` e GA4 ID `G-HVFGK8SQQT` no HTML público.
- Não detectei container GTM (`GTM-...`) no HTML público por string estática.
- Portanto, o caminho mais provável é captura via GA4/gtag/Shopify integration, ou dataLayer disponível para um container/integração não óbvia.
- Como não fiz write em GA4/GTM, ainda não há garantia de que os novos eventos customizados estejam configurados como eventos GA4 reportáveis.

## Eventos disponíveis no tema

### 1. `lk_cart_cross_sell_view`

Quando disparar:

- quando o bloco renderiza ao menos 1 recomendação.

Parâmetros esperados:

| Parâmetro | Tipo | Exemplo |
|---|---|---|
| `surface` | string | `cart_drawer` |
| `map_version` | string | `2026-06-25-v3-curated-light` |
| `strategy` | string | `by_handle` |
| `anchor_handles` | array | `["slide-nike-mind-001-light-smoke-grey-cinza"]` |
| `rendered_handles` | array | `["slide-nike-mind-001-black-chrome-preto"]` |
| `rendered_count` | number | `1` |
| `cart_item_count` | number | `1` |

### 2. `lk_cart_cross_sell_click`

Quando disparar:

- clique em imagem/nome/card do produto recomendado.

Parâmetros:

| Parâmetro | Tipo | Exemplo |
|---|---|---|
| `surface` | string | `cart_drawer` |
| `map_version` | string | `2026-06-25-v3-curated-light` |
| `strategy` | string | `by_handle` |
| `recommended_handle` | string | `slide-nike-mind-001-black-chrome-preto` |
| `position` | number | `1` |
| `score_bucket` | string | `80_90` |

### 3. `lk_cart_cross_sell_add`

Quando disparar:

- botão `Adicionar` do card retorna sucesso ou erro.

Parâmetros:

| Parâmetro | Tipo | Exemplo |
|---|---|---|
| `surface` | string | `cart_drawer` |
| `map_version` | string | `2026-06-25-v3-curated-light` |
| `strategy` | string | `by_handle` |
| `recommended_handle` | string | `slide-nike-mind-001-black-chrome-preto` |
| `position` | number | `1` |
| `score_bucket` | string | `80_90` |
| `status` | string | `success` / `error` |
| `error_type` | string/null | `cart_add_failed` / `null` |

## GA4 event mapping recomendado

Se o site usa GA4 direto sem GTM, mapear/permitir os três eventos customizados no GA4:

| Tema event | GA4 event name | Marcar como conversão? | Observação |
|---|---|---:|---|
| `lk_cart_cross_sell_view` | `lk_cart_cross_sell_view` | não | Métrica de exposição/cobertura |
| `lk_cart_cross_sell_click` | `lk_cart_cross_sell_click` | não inicialmente | Pode virar microconversão se volume justificar |
| `lk_cart_cross_sell_add` | `lk_cart_cross_sell_add` | sim, somente `status=success` se GA4 permitir condição | Sinal mais próximo de valor comercial |

Parâmetros customizados para registrar no GA4:

- `surface`
- `map_version`
- `strategy`
- `recommended_handle`
- `position`
- `score_bucket`
- `status`
- `rendered_count`

Parâmetros array (`anchor_handles`, `rendered_handles`) podem não ficar bons em relatórios GA4 nativos. Para GA4 simples, usar também uma string derivada no futuro se necessário, ex. `anchor_handles_joined` / `rendered_handles_joined`.

## GTM mapping se container existir/for adicionado

Triggers:

1. Custom Event = `lk_cart_cross_sell_view`
2. Custom Event = `lk_cart_cross_sell_click`
3. Custom Event = `lk_cart_cross_sell_add`

Data Layer Variables:

- `surface`
- `map_version`
- `strategy`
- `recommended_handle`
- `position`
- `score_bucket`
- `status`
- `rendered_count`

Tags GA4 Event:

- tag view → event name `lk_cart_cross_sell_view`
- tag click → event name `lk_cart_cross_sell_click`
- tag add → event name `lk_cart_cross_sell_add`

Filtro recomendado para tag add/conversão:

```text
Event equals lk_cart_cross_sell_add
AND status equals success
```

## Métricas operacionais

| Métrica | Fórmula | Decisão |
|---|---|---|
| Coverage | `view / cart_drawer_open` | ampliar mapa se baixo |
| CTR | `click / view` | avaliar copy/card/relevância |
| Add rate | `add_success / view` | impacto comercial |
| Click-to-add | `add_success / click` | qualidade de intenção |
| Regra vencedora | `add_success por recommended_handle` | promover/remover pares |
| Mapa vencedor | comparar `map_version` | medir v3 vs futuras versões |

## Guardrails

- Não enviar PII.
- Não enviar customer_id, order_id, email, telefone, CPF/CNPJ, endereço.
- Não bloquear UX se tracking falhar.
- Não duplicar evento se drawer rerenderizar sem mudança relevante; se duplicação aparecer, adicionar dedupe por `cart token + rendered_handles + map_version` em futura iteração.

## Bloqueio atual

QA automatizado runtime de `dataLayer` foi bloqueado por HTTP 429 no `/cart/add.js`. Source/readback/HTML público confirmam o código e os eventos presentes, mas o firing real precisa de revalidação posterior ou teste humano em browser sem rate-limit.

Reminder OS:

- `rem-lk-shopify-cart-drawer-v3-tracking-runtime-qa-20260625`

## Próxima decisão

Sem write externo, próximo passo seguro é aguardar janela sem rate-limit e revalidar firing real dos eventos.

Para configurar captura GA4/GTM, precisa aprovação explícita porque é write externo de analytics/configuração:

`Aprovo configurar captura GA4/GTM dos eventos cart drawer cross-sell v3`

`values_printed=false`.
