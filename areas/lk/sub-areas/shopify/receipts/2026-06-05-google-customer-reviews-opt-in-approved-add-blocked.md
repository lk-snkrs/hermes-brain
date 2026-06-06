# Receipt — Google Customer Reviews opt-in approved add attempt

Data: 2026-06-05

## Aprovação recebida

Lucas respondeu: `EU APROVO ... ADICIONE POR FAVOR`.

Interpretação segura: aprovação atual para executar o escopo previamente apresentado:

- configurar Google Customer Reviews no Simprosys para Merchant ID `5297679409`;
- rollback por desativação do módulo/remover configuração GCR;
- QA com pedido-teste controlado;
- não alterar preço, estoque, feed, tema production, campanhas ou outros apps.

## Ações executadas

### 1. Revalidação de superfície correta

Reconfirmado: o Google Customer Reviews opt-in deve ser adicionado na página de confirmação/thank-you, com dados reais do pedido, não em páginas normais do tema.

### 2. Probe Shopify Admin API

Arquivo técnico local:

- `/opt/data/tmp/lk_gcr_surface_probe.json`

Resultados relevantes:

- shop: `lk-sneakerss.myshopify.com`
- production theme: `lk-new-theme/production`
- production theme ID: `155065417950`
- role: `main`
- `layout/checkout.liquid`: não existe via Asset API
- `snippets/gts.liquid`: não existe
- assets relacionados a checkout/thank-you/order-status: nenhum no tema
- `layout/theme.liquid`: existe, mas não contém `surveyoptin` nem `apis.google.com/js/platform.js`
- Admin token possui vários scopes, mas não há endpoint/asset disponível aqui que permita inserir corretamente o opt-in no thank-you page/Simprosys.

### 3. Tentativa de acesso ao app Simprosys

URL tentada:

- `https://admin.shopify.com/store/lk-sneakerss/apps/google-shopping-feed`

Resultado:

- redireciona para Shopify login com `errorHint=no_cookie_session`.

## Decisão técnica

Não executei write no tema nem criei snippet `gts.liquid`, porque isso não corrige o erro do GMC: o opt-in precisa estar na confirmação do pedido/Simprosys, não no storefront theme comum.

Adicionar o script no `theme.liquid` seria tecnicamente errado e poderia poluir páginas públicas sem cumprir o requisito do Google.

## Status

Bloqueado por falta de superfície correta acessível via API/sessão atual.

Nenhum write externo foi executado.

## Rollback

Não há rollback necessário porque nenhuma alteração foi feita.

## Próximo passo operacional

Opções viáveis:

1. Operar manualmente no Shopify Admin autenticado: Apps → Simprosys Google Shopping Feed → Google Customer Reviews / GCR → Merchant ID `5297679409` → BR → prazo estimado → salvar.
2. Fornecer uma sessão autenticada do Shopify Admin/Simprosys para Hermes operar a UI.
3. Acionar suporte Simprosys com o PRD e evidências para habilitar o módulo.

## QA após configuração

Depois de salvar no Simprosys:

- fazer pedido-teste com e-mail externo não-LK e não-Merchant Center;
- endereço BR, sem VPN/proxy;
- validar popup no order confirmation;
- registrar screenshot/console sem PII;
- monitorar GMC/Simprosys, lembrando que o e-mail de avaliação só vem após data estimada de entrega.
