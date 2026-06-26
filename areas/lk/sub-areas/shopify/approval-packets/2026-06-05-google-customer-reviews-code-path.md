# Approval packet — Google Customer Reviews via código / Shopify

Data: 2026-06-05
Merchant Center ID: `5297679409`

## Correção de entendimento

Lucas confirmou que no app `Simprosys Google Shopping Feed` da LK não há área de **Google Customer Reviews / Store Ratings / GCR**. O link disponível aponta para `Proviews - Product Reviews Q&A`, outro app da Simprosys.

Portanto, o caminho Simprosys deixa de ser o caminho primário.

## Veredito técnico

Código é possível, mas **não no tema comum** (`theme.liquid`).

A superfície correta é uma destas:

1. **Legacy Order Status Page / Additional Scripts** — melhor caminho se o campo ainda existir no Admin.
2. **Custom app/checkout extension/app proxy** para thank-you/order-status — caminho de desenvolvimento se a loja já está 100% em Checkout Extensibility sem Additional Scripts.
3. **GTM/Customer Pixel** — não recomendado como caminho principal para o popup nativo porque pode ficar sandboxed/sem acesso correto.

## Por que não colocar no `theme.liquid`

O `theme.liquid` roda em páginas públicas normais, mas o Google exige o opt-in na confirmação do pedido, com dados reais:

- `order_id`
- `email`
- `delivery_country`
- `estimated_delivery_date`

No tema normal esses dados não existem. Colar no `theme.liquid` não resolve o alerta e pode criar script inútil em toda a loja.

## Snippet para legacy Additional Scripts

Usar somente se existir o campo:

Shopify Admin → Settings → Checkout → Order status page / Additional scripts

```liquid
{% if first_time_accessed %}
<!-- BEGIN Google Customer Reviews Opt-in -->
<script src="https://apis.google.com/js/platform.js?onload=renderOptIn" async defer></script>
<script>
  window.renderOptIn = function() {
    window.gapi.load('surveyoptin', function() {
      window.gapi.surveyoptin.render({
        "merchant_id": 5297679409,
        "order_id": "{{ checkout.name | escape }}",
        "email": "{{ checkout.order.email | default: checkout.email | escape }}",
        "delivery_country": "{{ checkout.order.shipping_address.country_code | default: checkout.shipping_address.country_code | default: 'BR' }}",
        "estimated_delivery_date": "{{ checkout.order.created_at | default: checkout.created_at | date: '%s' | plus: 1209600 | date: '%F' }}"
      });
    });
  };

  window.___gcfg = {
    lang: '{{ shop_locale.iso_code | default: "pt-BR" }}'
  };
</script>
<!-- END Google Customer Reviews Opt-in -->
{% endif %}
```

Nota: `1209600` = 14 dias. Ajustar se a LK quiser prazo estimado diferente.

## QA obrigatório

- Pedido-teste com e-mail não `@lksneakers.com.br` e não e-mail do Merchant Center.
- Endereço BR.
- Sem VPN/proxy.
- Confirmar popup na página de confirmação.
- Não esperar e-mail imediato; Google envia após a data estimada.

## Rollback

- Remover o bloco de Additional Scripts, se esse caminho for usado.
- Se for custom app/extension, desabilitar o bloco/app/feature.

## Próxima decisão

Verificar no Admin se ainda existe o campo **Additional Scripts**. Se existir, usar o snippet acima. Se não existir, partir para custom app/extension, não tema comum.
