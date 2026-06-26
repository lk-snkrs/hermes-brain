# Hermes Webhooks Vercel — auditoria read-only

- Data: 2026-06-24
- Escopo: projeto `/opt/data/hermes-webhooks`, Vercel `hermes-webhooks`, domínio `hermes-webhooks.lucascimino.com`, rotas públicas e assinatura/negação básica.
- Pedido Lucas: seguir com Vercel e auditar sem deploy/write.
- Writes externos/deploys: `0`
- Secrets impressos: `values_printed=false`

## Veredito

**Seguir com Vercel é adequado.** A camada pública está saudável, com custom domain e alias técnico respondendo, secrets esperados presentes no Doppler e na Vercel Production, rotas recusando tráfego sem assinatura e subscriptions Hermes existentes.

O estado é **operacional para manter**, com hardening recomendado antes de chamar 100% end-to-end para cada provedor crítico.

## Evidência pública

| Checagem | Resultado |
|---|---|
| `https://hermes-webhooks.lucascimino.com/health` | `200`, `{"status":"ok","platform":"webhook"}` |
| `https://hermes-webhooks.vercel.app/health` | `200`, `{"status":"ok","platform":"webhook"}` |
| Vercel deploy inspect | `target=production`, `status=Ready` |
| Vercel CLI smoke | `ok` |
| Node syntax check | `api/webhooks/[route].js` OK; `api/health.js` OK |
| Subscription scripts | 14 checados; 0 ausentes |

## Env/secrets — presença, sem valores

Vercel Production lista os nomes esperados como encrypted:

- `SHOPIFY_WEBHOOK_SECRET`
- `HERMES_WEBHOOK_SECRET`
- `EVOLUTION_WEBHOOK_PROXY_SECRET`
- `EVOLUTION_HERMES_ROUTE_SECRET`
- `LK_STOCK_HERMES_ROUTE_SECRET`
- `LK_STOCK_TINY_WEBHOOK_SECRET`
- `KLAVIYO_WEBHOOK_SECRET_LK_CONTENT`
- `KLAVIYO_HERMES_ROUTE_SECRET_LK_CONTENT`

Doppler `lc-keys/prd` também reportou `OK` para os mesmos nomes. Nenhum valor foi lido/impresso.

## Rotas e comportamento de segurança

Probes negativos no custom domain:

| Rota | GET | POST sem auth |
|---|---:|---:|
| `lk-shopify-pos-restock` | `405` | `401 missing_shopify_signature` |
| `lk-stock-shopify-order-paid` | `405` | `401 missing_shopify_signature` |
| `lk-stock-shopify-product-update` | `405` | `401 missing_shopify_signature` |
| `lk-stock-tiny-stock-snapshot` | `405` | `401 missing_generic_signature` |
| `lk-evolution-delivery-reconciliation` | `405` | `401 missing_evolution_proxy_secret` |
| `lk-content-klaviyo-test` | `405` | `401 missing_klaviyo_signature` |

Isso prova que a camada pública está viva e rejeita tráfego não autenticado. Não prova, sozinho, que eventos reais de Shopify/Evolution/Klaviyo estão configurados na tela/admin de cada provedor.

## Rotas/subscriptions Hermes encontradas

Principais subscriptions ativas com `deliver=log`:

- `lk-shopify-pos-restock` — `orders/paid`
- `lk-stock-shopify-order-paid` — `orders/paid`
- `lk-stock-shopify-product-update` — `products/update`, `products/create`
- `lk-stock-tiny-stock-snapshot` — `tiny_stock_snapshot`
- `lk-stock-tiny-events` — `tiny_webhook`
- `lk-evolution-delivery-reconciliation`
- `lk-content-klaviyo-events`
- outras rotas LK Shopify/online WABA/sales OS/tiny sync locais

Todos os scripts declarados pelas subscriptions existem no filesystem.

## Lacunas / riscos controlados

1. **Prova end-to-end provider-specific ainda não foi executada nesta auditoria.**
   - Fiz apenas health + probes negativos sem assinatura.
   - Próximo passo seguro: probes assinados no-op com payload inelegível, sem disparar WhatsApp/write externo.

2. **`package-lock.json` está untracked no repo local.**
   - Não bloqueia runtime, mas deve ser decidido: commitar se for artefato legítimo de build/reproducibilidade ou remover se ruído.

3. **Tiny subscriptions aparecem `has_secret=false` no arquivo Hermes.**
   - A Vercel exige segredo na borda e re-assina para Hermes, mas vale confirmar se o Hermes Gateway está validando pela secret global/route como esperado para Tiny, ou se essas rotas estão dependendo só da barreira Vercel.

4. **Health endpoint aponta para upstream `https://crisp-hooks.srv1331756.hstgr.cloud/health`.**
   - Isso está funcionando, mas o nome `crisp-hooks` é semanticamente antigo para uma infraestrutura canônica `hermes-webhooks`. Não é bug funcional; é dívida de clareza/documentação.

## Recomendação

Manter Vercel como padrão oficial:

```text
Shopify / Evolution / Klaviyo / Tiny
  -> hermes-webhooks Vercel
  -> Hermes webhook nativo
  -> script/agent/ledger/receipt
```

Próximos hardenings recomendados, em ordem:

1. **Signed no-op probes por provedor crítico** — Shopify, Evolution, Klaviyo e Tiny, sem envio externo e com verificação determinística.
2. **Provider registry readback** — confirmar nos admins/APIs que Shopify/Evolution/Klaviyo/Tiny apontam para `hermes-webhooks.lucascimino.com` nas rotas certas.
3. **Resolver `package-lock.json` untracked** — commit ou limpeza.
4. **Documentar/renomear semanticamente o upstream `crisp-hooks`** se/quando houver janela segura; não precisa mudar agora.

## Limites respeitados

- Sem deploy Vercel.
- Sem alteração de env/secrets.
- Sem alteração de provider webhook registry.
- Sem Shopify/Tiny/Klaviyo/Evolution writes.
- Sem envio WhatsApp/e-mail.
- Sem gateway/VPS/Docker/Traefik changes.
