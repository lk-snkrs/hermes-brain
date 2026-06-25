# Hermes Webhooks Shopify — reconciliação read-only do blocker de assinatura

- Data: 2026-06-24
- Escopo: Shopify Admin read-only, Vercel/Hermes signature path, Doppler presence checks, live gateway env booleans.
- Writes externos: `0`
- Deploys/restarts: `0`
- Secrets impressos: `values_printed=false`

## Veredito corrigido

O blocker Shopify **não é o secret provider Shopify na Vercel**.

A validação read-only indica:

```text
Shopify HMAC com SHOPIFY_WEBHOOK_SECRET -> aceito pela Vercel
Vercel assina forward com HERMES_WEBHOOK_SECRET -> Hermes route rejeita
Hermes static route lk-shopify-pos-restock espera WEBHOOK_SECRET legado
```

Ou seja: **o drift principal está na assinatura Vercel → Hermes**, não em Shopify → Vercel.

## Evidências

### Shopify Admin registry

Read-only via Admin API:

- REST status: `200`
- Webhooks totais: `33`
- GraphQL `webhookSubscriptions`: `0` nodes para este token/app view
- Webhooks apontando para Vercel/camada Hermes existem.

Rotas relevantes encontradas:

| Host | Path | Tópicos observados |
|---|---|---|
| `hermes-webhooks.vercel.app` | `/webhooks/lk-shopify-pos-restock` | `orders/paid` |
| `hermes-webhooks.vercel.app` | `/webhooks/lk-shopify-orders-ingest` | `orders/create`, `orders/updated`, `orders/cancelled` |
| `hermes-webhooks.vercel.app` | `/webhooks/lk-shopify-birthday-klaviyo-sync` | `orders/create` |
| `hermes-webhooks.vercel.app` | `/webhooks/lk-online-waba-dryrun` | múltiplos tópicos de orders/refunds/fulfillments |
| `hermes-webhooks.lucascimino.com` | `/webhooks/lk-stock-shopify-sales-os` | `orders/create`, `orders/paid`, `orders/updated`, `orders/cancelled`, `refunds/create` |

Observação: POS restock ainda usa o alias técnico `hermes-webhooks.vercel.app`, não o custom domain. Não é a causa do erro, pois o mesmo probe falha igual no custom e no alias.

### Probes de HMAC Shopify

Probes no-op contra `lk-shopify-pos-restock`:

| Secret candidate usado para assinar | Resultado |
|---|---|
| `SHOPIFY_WEBHOOK_SECRET` | Vercel aceita provider HMAC; upstream Hermes retorna `401 Invalid signature` |
| `SHOPIFY_ADMIN_TOKEN` | Vercel rejeita `invalid_shopify_signature` |
| `SHOPIFY_API_TOKEN` | Vercel rejeita `invalid_shopify_signature` |
| `SHOPIFY_ACCESS_TOKEN` | Vercel rejeita `invalid_shopify_signature` |

Isso mostra que `SHOPIFY_WEBHOOK_SECRET` é o candidato correto para Shopify → Vercel.

### Config/runtime Hermes

Config local da rota static:

```yaml
lk-shopify-pos-restock:
  secret_doppler: WEBHOOK_SECRET
```

Doppler `lc-keys/prd`:

| Secret name | Status |
|---|---|
| `WEBHOOK_SECRET` | ausente |
| `HERMES_WEBHOOK_SECRET` | presente |
| `SHOPIFY_WEBHOOK_SECRET` | presente |

Live process env, booleans apenas:

- gateway default principal: `WEBHOOK_SECRET_present=true`, `HERMES_WEBHOOK_SECRET_present=false`, `SHOPIFY_WEBHOOK_SECRET_present=false`
- há processos auxiliares/perfis com combinações diferentes, mas a rota static relevante está no default.

Vercel local source assina o forward para Hermes com `HERMES_WEBHOOK_SECRET`.

## Diagnóstico final

A rota `lk-shopify-pos-restock` ficou presa em um segredo legado:

```text
Hermes route config -> WEBHOOK_SECRET
Doppler canonical/public Vercel proxy -> HERMES_WEBHOOK_SECRET
```

Como `WEBHOOK_SECRET` nem existe no Doppler `lc-keys/prd`, o estado atual depende de env legado no processo gateway, e não da fonte canônica Doppler-first.

## Approval packet gerado

Criei o packet:

`areas/operacoes/approval-packets/hermes-webhooks-shopify-route-secret-alignment-20260624.md`

Recomendação do packet:

1. backup de `/opt/data/config.yaml`;
2. patch somente da rota `lk-shopify-pos-restock` para `secret_doppler: HERMES_WEBHOOK_SECRET`;
3. restart/verificação do gateway default com `HERMES_WEBHOOK_SECRET` injetado via Doppler;
4. repetir probe Shopify no-op até:
   - HTTP `200`
   - `status=ignored`
   - `reason=not_paid_active_pos_order`
   - `sent_count=0`
   - `queued_count=0`

## Limites respeitados

- Sem alteração em Shopify webhook registry.
- Sem alteração em Vercel env/deploy.
- Sem alteração em gateway/config/runtime.
- Sem restart.
- Sem WhatsApp/e-mail/campanha.
- Sem Docker/VPS/Traefik.
- Nenhum secret value impresso.
