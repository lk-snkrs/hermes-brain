# LK Recovery OS — audit root cause after PR28

Data: 2026-06-03 13:00 UTC
Status: `root_cause_is_scoring_product_extraction_plus_contact_inheritance_gap`

## Pedido

Lucas: "Seguir e auditar onde está o erro".

Escopo executado: auditoria read-only em DB + código local. Nenhum envio, nenhum write externo/produção, nenhum deploy.

## Sintoma atual

Audit live corrigido por `cluster_uuid`:

### 1h

- `storefront_events`: 1014
- `with_cart`: 387
- `candidates`: 8
- `candidates_with_cart`: 8
- `cart_clusters_with_phone`: 1
- `candidates_with_phone`: 1

### 24h

- `storefront_events`: 9765
- `with_cart`: 3573
- `candidates`: 132
- `candidates_with_cart`: 132
- `cart_clusters_with_phone`: 1
- `candidates_with_phone`: 1

O único `candidate_with_phone` é o candidate manual/backfill `id=130`.

## Causa raiz 1 — scoring não valoriza carrinho real (`cart_update`) e perde `product_id`

Código: `workers/recovery-os/src/types.ts`

- `BEHAVIORAL_EVENT_TYPES` inclui `cart_create` e `cart_update`.
- `SCORING_WEIGHTS` não define peso para `cart_create`/`cart_update`.
- Resultado: `cart_update` vale `0` por `SCORING_WEIGHTS[e.event_type] ?? 0`.

Código: `workers/recovery-os/src/scoring.ts`

- bônus de repetição usa apenas `product_id`:
  - `if ((e.event_type === "view_product" || e.event_type === "product_view") && e.product_id) ...`
- Mas eventos storefront recentes têm `product_title`, não `product_id`, na tabela `identity_events`.

Evidência DB 24h:

- `view_product`: 4282 com título, `0` com `product_id`
- `cart_update`: 127 com título, `0` com `product_id`
- `cart_view`: 92 com título, `0` com `product_id`
- `add_to_cart`: 23 com título, `0` com `product_id`

Para o cluster com telefone + carrinho (`36c19640-926a-4a54-a38f-e33f34815c96`):

- Eventos 72h:
  - `view_product`: 4
  - `cart_update`: 7
  - `identity_update`: 9
- Score reconstruído pelo código atual:
  - base score: `40`
  - repeat bonus: `0`
  - total: `40`
- Min score provável: `50`
- Portanto ele não materializaria candidato automaticamente pelo scoring; o candidate com telefone só existe porque foi criado manualmente.

Se `cart_update` tivesse peso 50, esse mesmo cluster teria score aproximado `390`.

## Causa raiz 2 — extração do produto usa página, não item do carrinho

Código: `workers/recovery-os/src/inbound.ts` linhas ~252-270:

- `productId` vem de `payload.product_id` ou `payload.product.product_id`.
- `productTitle` vem de `payload.product_title` ou `payload.product.title`.
- Não há fallback para `payload.cart.items[0].product_id`, `variant_id`, `product_title`, `image`, `url`.

Evidência DB raw_events 24h:

- `raw_events.payload.cart.items[0].product_id` existe em:
  - `add_to_cart`: 23/44 recentes
  - `cart_update`: 127/127
  - `cart_view`: 92/92
  - `view_product`: 133/4491
- Mas `identity_events.product_id` para esses mesmos tipos ficou `0`.

Exemplo do cluster com telefone:

- `raw_events.cart.items[0].product_title`: `Jason Markk Essential Kit de Limpeza`
- `raw_events.product.title`: `New Balance 204L`
- `identity_events.product_title`: `New Balance 204L`

Ou seja: o pipeline está pegando o produto da página/contexto, não o item real do carrinho. O manual backfill criou o candidate correto com `Jason Markk Essential Kit de Limpeza` porque leu `cart.items[0]`.

## Causa raiz 3 — novo link em cluster com telefone não herda telefone existente

Código: `workers/recovery-os/src/clusters.ts`

- `attachToCluster()` encontra/reusa cluster via email/customer/medium existing link.
- Mas no upsert do novo link usa apenas `link.phone_hash`/`link.phone_e164` do evento atual.
- Se o cluster já tem `primary_phone_e164`, mas o evento storefront atual só trouxe email/customer/cart, o novo `cart_token` fica sem telefone no próprio row.

Evidência DB para cluster com telefone + carrinho:

- cluster tem `primary_phone_e164` e `primary_phone_hash`.
- links com telefone no cluster: `phone_hash`, `email_hash`, `klaviyo_profile_id`, `customer_id`.
- `cart_token` recente no mesmo cluster: `phone_hash=false`, `phone_e164=false`, `email_hash=true`.
- identity_events recentes do mesmo cluster: `events_with_phone=0`, embora cluster tenha telefone.

Isso não bloqueia totalmente se o scoring buscasse telefone em `identity_clusters`, mas gera métricas/propagação fracas e deixa `phone_hash` ausente nos events/candidates quando nenhum patch posterior roda.

## Hipótese validada

O erro não é mais "não tem Klaviyo/telefone". O gargalo atual é:

1. eventos de carrinho reais (`cart_update`) chegam e têm produto no raw payload;
2. promoção para `identity_events` perde `product_id` e usa o produto da página em vez do item do carrinho;
3. scoring dá peso 0 para `cart_update` e depende de `product_id` para bônus;
4. quando um cluster já tem telefone, novos links/events não herdam automaticamente o telefone do cluster;
5. por isso o sistema só gerou prova por backfill manual, não como fluxo live autônomo.

## Próximo patch recomendado

1. Em `inbound.ts`, extrair produto prioritariamente de `payload.cart.items[0]` para `cart_update`, `cart_view`, `add_to_cart`:
   - `product_id`
   - `variant_id`
   - `product_title/title`
   - `image/featured_image.url`
   - `url`
2. Em `types.ts`, adicionar peso para:
   - `cart_update`: provavelmente 50 ou 60
   - `cart_create`: provavelmente 50
3. Em `scoring.ts`, permitir repeat bonus por chave fallback `product_id || product_url || product_title`.
4. Em `attachToCluster()` ou após stitching, quando o cluster já tem primary phone/email, propagar para novos links/events/candidates mesmo se o evento atual não trouxer telefone.
5. Criar testes RED antes:
   - cart payload com `cart.items[0].product_id` vira `identity_events.product_id`.
   - `cart_update` pesa suficiente para gerar candidate.
   - link `cart_token` anexado a cluster com primary phone herda telefone ou dispara propagation.

## Segurança

- Nenhum envio foi feito.
- Nenhuma flag de go-live/send foi alterada.
- Nenhum DB write foi executado nesta auditoria.
