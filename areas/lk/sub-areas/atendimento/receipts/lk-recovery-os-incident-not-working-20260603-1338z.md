# LK Recovery OS — incident audit after Lucas dissatisfaction

Data: 2026-06-03 13:38 UTC
Status: `incident_confirmed_not_operationally_working`

## Trigger

Lucas declarou estar totalmente insatisfeito e que o LK Recovery OS não está funcionando.

## Verificação read-only realizada

### Runtime / captura

- Worker `/healthz`: HTTP 200, `{"service":"lk-recovery","status":"ok"}`
- Eventos últimos 6h:
  - `raw_events_6h`: 8234
  - `raw_with_cart_6h`: 1715
  - `raw_with_email_6h`: 3820
  - `raw_with_phone_6h`: 1038
  - `cart_links_6h`: 1079
  - `phone_links_6h`: 2436
  - `cart_phone_clusters_6h`: 1

### Candidatos

- `candidates_6h`: 42
- `pending`: 42
- `with_phone`: 1
- `with_cart`: 42
- `with_recovery_link`: 42
- `score_under_50`: 0
- `latest_candidate`: 2026-06-03 13:20:01 UTC

Há pelo menos 1 candidato contactável selecionável pelo T1 scoring:

- candidate id `130`
- criado em 2026-06-03 12:32:28 UTC
- state `pending`
- score `60`
- tem `phone_e164`, `phone_hash`, produto, imagem e cart permalink

### Mensagens / ação

- `recovery_messages_total`: 0
- `non_dry_run_messages`: 0
- `accepted_like`: 0

### Falha operacional isolada

Audit log últimas 48h:

- `t1_order_recheck_unavailable`: 21 ocorrências
- último: 2026-06-03 13:32:22 UTC
- details: `{"reason":"shopify_recheck_failed_or_missing_creds"}`

Código T1 falha fechado antes de enviar/criar contexto quando não consegue revalidar pedido Shopify:

- `alreadyOrderedAfterCheckout()` retorna `unable_to_check` quando Shopify credencial está ausente/inválida ou API falha.
- O runner registra `t1_order_recheck_unavailable` e `continue`.

### Secret/token check sem expor valores

Cloudflare Worker tem secret names:

- `SHOPIFY_ACCESS_TOKEN`
- `SHOPIFY_STORE_URL`
- outros necessários presentes por nome

Doppler read-only check contra Shopify:

- `SHOPIFY_ACCESS_TOKEN` → `orders.json`: HTTP 404
- `SHOPIFY_ADMIN_TOKEN` → `orders.json`: HTTP 200
- `SHOPIFY_API_TOKEN` → `orders.json`: HTTP 404

Conclusão provável: o Worker usa `SHOPIFY_ACCESS_TOKEN`, mas o token válido para recheck de orders no Doppler é `SHOPIFY_ADMIN_TOKEN`. Sem corrigir o secret usado pelo Worker, o T1 falha fechado.

### Segundo problema de observabilidade/ação

Mesmo com `LK_CHATWOOT_INTERNAL_ONLY=true`, quando `LK_RECOVERY_DRY_RUN=true`, o código atualmente faz:

- `skip_chatwoot_internal_dry_run`
- não cria `recovery_messages`
- não cria contexto interno Chatwoot

Isso mantém segurança, mas faz o sistema parecer morto/sem saída operacional. Para validar operação sem envio ao cliente, o dry-run deveria pelo menos criar evidência/audit de candidato processável ou permitir contexto interno explicitamente aprovado.

## Veredito honesto

Lucas está correto: do ponto de vista operacional, o Recovery OS não está funcionando como produto de recuperação. Ele captura eventos e cria candidatos, mas a etapa de ação está bloqueada por recheck Shopify indisponível/inválido e por dry-run silencioso no modo Chatwoot interno.

## Approval packet recomendado

1. Atualizar secret de produção do Worker `SHOPIFY_ACCESS_TOKEN` para o valor válido de `SHOPIFY_ADMIN_TOKEN` do Doppler, sem expor valor.
2. Revalidar T1 em dry-run/internal-only.
3. Se continuar seguro, ajustar código para que `dry_run + chatwoot_internal_only` gere evidência operacional (`recovery_messages.dry_run=true` ou audit específico) em vez de skip silencioso.
4. Manter `LK_LIVE_SEND_ENABLED=false`, `LK_WHATSAPP_SEND_ENABLED=false`, `LK_EMAIL_SEND_ENABLED=false`.
