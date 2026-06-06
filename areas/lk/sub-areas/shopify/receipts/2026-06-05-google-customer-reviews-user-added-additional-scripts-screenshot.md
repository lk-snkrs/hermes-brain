# Receipt — Google Customer Reviews código adicionado manualmente por Lucas

Data: 2026-06-05

## Contexto

Lucas perguntou se o campo mostrado no Shopify Admin era o local correto e informou: `adicionei`.

Imagem recebida no Telegram:

- `/opt/data/profiles/lk-shopify/image_cache/img_3eda3be5b8ce.jpg`

A imagem mostra a área de checkout/pós-compra com:

- seção `Página de pós-compra`;
- opção de app pós-compra com `Nenhum` selecionado;
- campo `Scripts adicionais` contendo o final do snippet de Google Customer Reviews opt-in.

## Interpretação

O campo parece ser a superfície correta ou próxima da correta para scripts adicionais pós-compra/order status, não o tema comum `theme.liquid`.

A evidência visual mostra apenas o trecho final do snippet, portanto ainda falta confirmar se o bloco completo foi colado, incluindo:

- `{% if first_time_accessed %}` no início;
- `<script src="https://apis.google.com/js/platform.js?onload=renderOptIn" async defer></script>`;
- `window.renderOptIn`;
- `window.gapi.load('surveyoptin', ...)`;
- `merchant_id: 5297679409`;
- `order_id`, `email`, `delivery_country`, `estimated_delivery_date`;
- `{% endif %}` no final.

## Status

Write foi feito manualmente por Lucas no Shopify Admin. Hermes não executou write externo.

## Próximo QA

1. Salvar a configuração no Admin, se ainda não foi salva.
2. Fazer pedido-teste controlado com e-mail externo não-LK/não-Merchant Center, endereço BR, sem VPN/proxy.
3. Na página de confirmação, validar se aparece o opt-in do Google Customer Reviews.
4. Registrar evidência visual sem PII.
5. Lembrar que o e-mail de review só deve vir após a data estimada de entrega.

## Rollback

Remover o bloco do campo `Scripts adicionais` e salvar.
