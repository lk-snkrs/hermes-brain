# Checkout LK — Microfunil de conversão (#9) — auditoria read-only e proposta

## Status

Auditoria read-only inicial concluída.

## Evidência local/Doppler

- `SHOPIFY_STORE_URL`: presente no Doppler.
- `SHOPIFY_ACCESS_TOKEN`: presente no Doppler.
- `GA4_PROPERTY_ID`: presente no Doppler.
- `GOOGLE_APPLICATION_CREDENTIALS`: ausente no Doppler consultado.
- `GTM_CONTAINER_ID`: ausente no Doppler consultado.

## Evidência Shopify/app

- App checkout atual: `/opt/data/projects/lk-gift-bag-checkout-app`.
- Busca local por `pixel`, `analytics`, `checkout_started`, `checkout_completed`, `dataLayer`, `gtag`, `fbq`, `klaviyo` não encontrou implementação própria de tracking no app de checkout.
- Evidência anterior de Admin GraphQL:
  - `webPixel`: `No web pixel was found for this app.`
  - `webPixels`: campo inexistente no schema usado.
  - `customerEvents`: campo inexistente no schema usado.

## Interpretação

O app de checkout atual resolve UI/atributos, mas não parece medir microfunil próprio. A mensuração provavelmente depende de Shopify Analytics, canais/app pixels já instalados no Admin, GA4/Google app, Meta/Klaviyo/Simprosys ou Customer Events no Admin UI.

Como `GOOGLE_APPLICATION_CREDENTIALS` e `GTM_CONTAINER_ID` não estão disponíveis no Doppler consultado, não foi possível consultar GA4/GTM daqui sem nova configuração/acesso. Não foram feitos writes.

## Microfunil recomendado

Eventos/etapas desejadas:

1. `checkout_started`
2. `contact_step_visible`
3. `contact_info_entered`
4. `delivery_step_visible`
5. `shipping_method_visible`
6. `shipping_method_selected`
7. `payment_step_visible`
8. `payment_method_selected`
9. `pay_now_clicked`
10. `checkout_error`
11. `purchase_completed`

## Camada recomendada

### Mínimo seguro, sem custom pixel novo

Usar Shopify Analytics + GA4 existente, se os eventos nativos já chegam:

- `begin_checkout`
- `add_shipping_info`
- `add_payment_info`
- `purchase`

Limitação: pode não medir visibilidade de blocos, clique em `PAGAR AGORA`, erros por campo ou abandono exato por etapa.

### Ideal para Shopify Plus

Criar Web Pixel Extension / Customer Events para eventos granulares, com consentimento e sem PII:

- event name
- checkout/token hash não reversível se permitido
- cart subtotal bucket
- shipping threshold bucket (`below_499`, `above_499`)
- step/interaction
- timestamp
- device

Destino possível:

- GA4 Measurement Protocol
- endpoint próprio Vercel/Supabase
- Shopify Customer Events compatível

## Atenção LGPD/PII

Não enviar:

- e-mail
- telefone
- nome
- endereço
- CPF
- CEP completo se desnecessário

Usar apenas eventos agregados, buckets e IDs anônimos quando possível.

## Próxima decisão necessária

Para implementar mensuração granular, Lucas precisa aprovar uma destas opções:

### Opção A — Auditoria GA4/Shopify Analytics somente leitura

Escopo: confirmar quais eventos nativos já chegam e montar baseline.

Dependência: acesso GA4/GTM ou service account válida.

### Opção B — Criar Web Pixel Extension custom

Escopo: implementar tracking granular de microfunil no checkout.

Exige: write/deploy de app Shopify + destino de dados + rollback.

### Opção C — Usar Vercel/Supabase endpoint interno

Escopo: pixel manda eventos anonimizados para endpoint próprio.

Exige: app/pixel write + backend write + política de dados.

## Não-ações

- Nenhum pixel foi criado.
- Nenhum evento foi enviado.
- Nenhum GA4/GTM/Shopify Customer Event foi alterado.
- Nenhuma campanha/Klaviyo/Meta foi alterada.
