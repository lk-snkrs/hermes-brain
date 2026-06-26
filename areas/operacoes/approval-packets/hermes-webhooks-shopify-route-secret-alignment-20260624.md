# Approval packet — alinhar assinatura Shopify Vercel → Hermes

- Data: 2026-06-24
- Área: Operações Hermes / LK Shopify webhooks
- Classificação: infra-sensitive / gateway runtime / secrets
- Pedido/decisão: Lucas aprovou seguir com validação 1→4 dos webhooks Vercel. A etapa read-only confirmou que Shopify provider HMAC passa na Vercel, mas o encaminhamento Vercel → Hermes falha por assinatura da rota Hermes.
- Status atual: **aguardando aprovação escopada para mutação de config/runtime**.

## Diagnóstico read-only

Evidências sem imprimir valores:

1. Shopify Admin REST read-only retornou `33` webhooks.
2. Existem webhooks Shopify apontando para Vercel:
   - `hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock` para `orders/paid`.
   - múltiplas rotas `hermes-webhooks.vercel.app/webhooks/lk-online-waba-dryrun`.
   - `hermes-webhooks.lucascimino.com/webhooks/lk-stock-shopify-sales-os` para `orders/create`, `orders/paid`, `orders/updated`, `orders/cancelled`, `refunds/create`.
3. Probe Shopify no-op assinado com `SHOPIFY_WEBHOOK_SECRET` passou a validação provider na Vercel, mas recebeu `401 Invalid signature` do upstream Hermes.
4. Probes assinados com candidatos errados (`SHOPIFY_ADMIN_TOKEN`, `SHOPIFY_API_TOKEN`, `SHOPIFY_ACCESS_TOKEN`) foram rejeitados pela Vercel com `invalid_shopify_signature`.
5. Portanto, o blocker principal **não é o Shopify provider secret**. É o segredo usado na ponte Vercel → Hermes.
6. Config live local da rota está como:
   - rota: `lk-shopify-pos-restock`
   - `secret_doppler: WEBHOOK_SECRET`
7. Doppler `lc-keys/prd`:
   - `WEBHOOK_SECRET`: ausente
   - `HERMES_WEBHOOK_SECRET`: presente
   - `SHOPIFY_WEBHOOK_SECRET`: presente
8. Processo gateway default tem `WEBHOOK_SECRET` no ambiente, mas não tem `HERMES_WEBHOOK_SECRET`/`SHOPIFY_WEBHOOK_SECRET` no mesmo processo. Isso indica segredo legado local/runtime, fora da fonte canônica Doppler.
9. Vercel proxy assina o forward para Hermes com `HERMES_WEBHOOK_SECRET`.
10. Resultado: provider Shopify HMAC OK → Vercel forward assinado com `HERMES_WEBHOOK_SECRET` → Hermes route espera `WEBHOOK_SECRET` → `401 Invalid signature`.

## Ação proposta — opção recomendada

**Tornar `HERMES_WEBHOOK_SECRET` o segredo canônico da rota `lk-shopify-pos-restock`.**

Escopo exato:

1. Backup de `/opt/data/config.yaml`.
2. Patch local da rota:

```yaml
lk-shopify-pos-restock:
  secret_doppler: HERMES_WEBHOOK_SECRET
```

3. Ajustar/reiniciar somente o gateway default para injetar `HERMES_WEBHOOK_SECRET` via Doppler `lc-keys/prd`.
4. Verificar live process env com booleans apenas:
   - `HERMES_WEBHOOK_SECRET_present=true`
   - `DOPPLER_TOKEN` não exposto ao processo filho se aplicável
   - `values_printed=false`
5. Repetir probe Shopify no-op:
   - esperado: HTTP `200`
   - `status=ignored`
   - `reason=not_paid_active_pos_order`
   - `sent_count=0`
   - `queued_count=0`
6. Verificar logs sem valores de segredo.
7. Criar receipt final.

## Alternativas consideradas

### Alternativa B — copiar/alinhar `WEBHOOK_SECRET` para Doppler/Vercel

Não recomendada como primeira opção porque mantém nome legado `WEBHOOK_SECRET` e pode exigir mover segredo local/runtime para Doppler/Vercel. Funciona, mas perpetua ambiguidade.

### Alternativa C — alterar Vercel para assinar com segredo legado do gateway

Também não recomendada porque desloca Vercel para um segredo que hoje não é canônico no Doppler e exigiria env change + redeploy Vercel.

## Riscos

- Restart do gateway default é sensível: pode afetar Telegram/API/webhook por alguns segundos.
- Configuração errada pode quebrar `lk-shopify-pos-restock` até rollback.
- Outros webhooks dinâmicos não devem ser alterados neste pacote.

## Rollback

1. Restaurar backup de `/opt/data/config.yaml`.
2. Reiniciar gateway default no estado anterior.
3. Verificar `/health` local e público.
4. Repetir probe negativo para confirmar que rota rejeita assinatura inválida.

## Bloqueios / não fazer sem aprovação adicional

- Não alterar Shopify webhook registry.
- Não alterar Vercel env/deploy.
- Não alterar Tiny/Klaviyo/Evolution.
- Não enviar WhatsApp/e-mail/campanha.
- Não mexer em Docker/VPS/Traefik.
- Não imprimir valores de secrets.

## Pedido de aprovação

Aprovar exatamente:

> Patch em `/opt/data/config.yaml` da rota `lk-shopify-pos-restock` para usar `secret_doppler: HERMES_WEBHOOK_SECRET`, reinício/verificação do gateway default com Doppler-first, e repetição do probe Shopify no-op até `200 ignored`, sem writes em Shopify/Vercel/providers.
