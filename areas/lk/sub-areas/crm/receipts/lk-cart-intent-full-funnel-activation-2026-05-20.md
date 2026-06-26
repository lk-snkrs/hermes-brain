# LK — Cart Intent Full-Funnel WhatsApp: captura ativa + envio pendente de template

Data UTC: 2026-05-20
Agente: Hermes LK Growth

## Aprovação

Lucas respondeu `3` ao pacote de decisão: aprovar implementar e ativar envio real quando elegível.

## O que foi feito

### 1. Checkout abandonado atual validado

Na execução n8n `11395` (`2026-05-20T21:00:16Z`), o fluxo ativo de checkout abandonado enviou T1 para um novo checkout elegível:

- Workflow: `kWQbmEMuvdipcGjd`
- Checkout: `39501064339678`
- Produto: `Tênis On Running Cloudsolo Loewe Sand Burgundy Bege`
- Touchpoint: `30min`
- Crisp: `request_accepted`
- `request_id`: `3d11e26d-fcbc-4abe-9e0a-df4249e595db`
- Telefone redigido: final `9623`

### 2. Novo template Meta para carrinho/intenção ampla

Template submetido no WABA canônico LK `1478026007140488`:

- Nome: `lk_carrinho_abandonado_30min_v1`
- Categoria: `MARKETING`
- Idioma: `pt_BR`
- Status inicial: `PENDING`
- CTA: `Finalizar compra`
- URL base: `https://lksneakers.com.br/cart/{{1}}`

Observação: primeira tentativa com HEADER IMAGE foi recusada por falta de header example handle válido; foi submetida versão sem header para acelerar aprovação.

### 3. Novo workflow n8n ativo para intenção/carrinho

Workflow criado e ativado:

- ID: `XLODECE4MvNRNCQ9`
- Nome: `LK - Cart Intent 30min Full Funnel - Crisp (ATIVO)`
- Status verificado: `active: true`
- `versionId == activeVersionId`: `ef271317-48cb-46e7-92ea-4bb4a4ca4c08`

Fluxo:

1. `LK Cart Intent Webhook`
2. `Wait 30 min`
3. `Filtrar cart intent elegíveis`
4. `Preparar payload Crisp Cart`
5. `Crisp Send cart intent`
6. `Marcar cart enviado no dedup`
7. `Supabase Persist Cart Result`

Enquanto o template Meta está `PENDING`, o workflow captura eventos mas bloqueia envio com motivo `cart_template_not_approved_yet`.

### 4. Captura no tema Shopify production

Asset alterado:

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Asset: `layout/theme.liquid`
- Marcador: `<!-- LK cart intent capture v1 -->`
- Endpoint: `https://n8n.lucascimino.com/webhook/lk-cart-intent-v1`

Comportamento do script:

- observa `add_to_cart`, `cart_update`, `cart_change` por form submit, fetch e XHR;
- busca `/cart.js`;
- envia evento para n8n com cart, customer liquid quando disponível, página e referrer;
- usa debounce de 10s por estado de carrinho;
- não expõe segredo no front-end.

Backup local pré-write:

- `/opt/data/hermes_bruno_ingest/.secrets/shopify_theme_backups/lk-cart-intent-20260520T210436Z/`

Verificação:

- Asset API readback contém o marcador e endpoint.
- PDP live verificado contém `lk-cart-intent-v1` e `__lkCartIntentCaptureV1`.

### 5. Template aprovado e envio liberado

Auditoria posterior em `2026-05-20T21:08Z` verificou que o template `lk_carrinho_abandonado_30min_v1` já estava `APPROVED` no WABA canônico LK `1478026007140488`.

Ação executada com base na aprovação `3` do Lucas:

- Workflow liberado: `XLODECE4MvNRNCQ9`
- Node alterado: `Filtrar cart intent elegíveis`
- Flag liberado: `staticData.config.cartTemplateApproved = true`
- Readback: `active: true`
- `versionId == activeVersionId`: `4ed82930-484e-4f0d-8a95-43440ac36ca1`
- Backup raw n8n pré-release: `/opt/data/hermes_bruno_ingest/.secrets/n8n_workflow_backups_cart_intent_before_release_20260520T2109Z.json`

O cron provisório `48d63306554e` criado para aguardar aprovação Meta foi removido porque a liberação já foi feita manualmente.

## Rollback

### Pausar envio de cart intent

- Patchar o node `Filtrar cart intent elegíveis` para `cartTemplateApproved = false`; ou
- Desativar workflow `XLODECE4MvNRNCQ9`.

### Remover captura do tema

- Restaurar `layout/theme.liquid` a partir do backup acima; ou
- Remover o bloco entre `<!-- LK cart intent capture v1 -->` e `<!-- /LK cart intent capture v1 -->`.

## Riscos / observações

- Até aprovação Meta, nenhum envio de cart intent deve sair; somente captura/log.
- Carrinho sem telefone confiável não recebe WhatsApp.
- O fluxo usa cap/dedup em staticData + persistência Supabase para envios aceitos.
- Template sem imagem foi priorizado para speed; versão com imagem pode ser criada depois com upload/handle correto.
