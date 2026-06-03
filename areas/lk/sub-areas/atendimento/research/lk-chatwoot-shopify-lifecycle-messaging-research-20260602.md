---
title: LK Chatwoot + Shopify lifecycle messaging research
created_at_utc: 2026-06-02
area: lk/atendimento
systems: [shopify, chatwoot, whatsapp]
status: research-first
---

# LK Chatwoot + Shopify lifecycle messaging research

## Pedido do Lucas

Lucas aprovou o MVP 1B em princípio, mas pediu que o primeiro passo fosse pesquisar internet/docs/blogs/fóruns/Reddit sobre melhores práticas de carrinho abandonado e integração Shopify + Chatwoot antes de implementar. Também sinalizou que Chatwoot será usado depois para mensagens de ciclo de pedido/venda:

- Pedido feito
- Pedido aprovado
- Pedido enviado
- Pedido recebido
- Follow-up de venda

## Fontes consultadas

### Oficiais / primárias

1. Shopify Admin REST Webhook resource
   - `https://shopify.dev/docs/api/admin-rest/latest/resources/webhook`
   - Achados: webhooks reduzem chamadas periódicas, executam código após eventos, são escopados ao app que criou a inscrição, inscrições criadas no Admin podem não aparecer via API daquele app.

2. Shopify Abandoned Checkouts resource
   - `https://shopify.dev/docs/api/admin-rest/latest/resources/abandoned-checkouts`
   - Achados: abandoned checkout requer escopo `orders`; checkout é considerado abandonado quando cliente adicionou contato mas não completou compra; recurso serve para remarketing, comportamento, tracking e itens abandonados; possui recovery URL; expõe consentimentos de email/SMS; `completed_at` e `closed_at` precisam ser filtrados.

3. Shopify HTTPS webhook endpoint guidance
   - `https://shopify.dev/docs/apps/build/webhooks/subscribe/https`
   - Achados: cada entrega tem `X-Shopify-Hmac-SHA256`; validar HMAC com corpo bruto; cada entrega tem ID para dedupe; usar `X-Shopify-Webhook-Id`; Shopify exige resposta 200, tem timeout de conexão de 1s e total de 5s; recomenda fila assíncrona e job de reconciliação periódico para dados perdidos; retries 8 vezes em 4h e pode deletar subscription criada via Admin API após falhas consecutivas.

4. Chatwoot WhatsApp Cloud docs
   - `https://www.chatwoot.com/docs/product/channels/whatsapp/whatsapp-cloud/`
   - Achados: Chatwoot suporta WhatsApp Cloud por Embedded Signup ou Manual Setup; Embedded Signup é recomendado para novo número; Manual exige Phone Number ID, Business Account ID/WABA e API key/token; Chatwoot auto-configura webhook/tokens via embedded.

5. Chatwoot API — create contact
   - `https://developers.chatwoot.com/api-reference/contacts/create-contact`
   - Achados: contato aceita `inbox_id`, `name`, `email`, `phone_number`, `identifier`, `additional_attributes`, `custom_attributes`.

6. Chatwoot API — create conversation
   - `https://developers.chatwoot.com/api-reference/conversations/create-new-conversation`
   - Achados: conversa aceita `source_id`, `inbox_id`, `contact_id`, `additional_attributes`, `custom_attributes`, `status`, `assignee_id`, `team_id`, `snoozed_until`.

7. Chatwoot API — create message
   - `https://developers.chatwoot.com/api-reference/messages/create-new-message`
   - Achados: mensagens podem ser privadas (`private: true`); para WhatsApp é possível usar `template_params`; templates precisam ser pré-aprovados no WhatsApp Business Manager.

8. Meta WhatsApp template/pricing/opt-in docs
   - `https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates/`
   - `https://developers.facebook.com/docs/whatsapp/pricing/`
   - `https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/`
   - Achados: modelos/template são necessários fora da janela de atendimento; cobrança desde 2025 é por mensagem template entregue; categorias: marketing, utilidade, autenticação; mensagens não-template só dentro da janela de atendimento; opt-in é obrigatório antes de enviar WhatsApp, com nome da empresa claro, expectativa de categorias de mensagens e opção de recusa.

### Benchmarks / blogs especialistas

1. Shopify blog — abandoned cart emails
   - `https://www.shopify.com/blog/abandoned-cart-emails`
   - Achados: abandono médio em torno de 70%; email de recuperação deve ter lembrete amigável, CTA claro, produto/benefício, prova social, personalização; não promete recuperar tudo; usado como fluxo de retenção/receita.

2. Klaviyo abandoned cart benchmarks
   - `https://www.klaviyo.com/blog/abandoned-cart-benchmarks`
   - Achados: abandoned cart flows tiveram maior revenue per recipient e conversão entre flows analisados; média citada: RPR US$3,65, placed order rate 3,33%, open rate 50,5%, click rate 6,25%; top 10% muito acima. Indica valor alto de um fluxo básico bem implementado e A/B testing.

3. Omnisend abandoned cart email guide/report
   - `https://www.omnisend.com/blog/abandoned-cart-email/`
   - Achados: automações comportamentais geram receita desproporcional; abandoned cart junto com welcome series concentrou grande parte da receita automatizada; recomenda personalização, timing, storytelling/trust signals antes de desconto, testes de timing/assunto/conteúdo.

4. Tidio abandoned cart email guide
   - `https://www.tidio.com/blog/abandoned-cart-email/`
   - Achados: recomenda sequência de múltiplas mensagens, tipicamente 3 etapas; primeira algumas horas após abandono como lembrete; follow-up dias depois; incentivos/descontos devem ser usados com cuidado.

5. Baymard cart abandonment rate/reasons
   - `https://www.baymard.com/lists/cart-abandonment-rate`
   - Achados: média documentada 70,22%; principais motivos evitáveis incluem custos extras, entrega lenta, falta de confiança, criação obrigatória de conta, checkout longo, política de devolução, erros, total não claro, falta de pagamento. Para LK, recuperação deve tratar objeções reais sem inventar prazo/estoque/preço.

### Reddit/fóruns

- Tentativa de acessar Reddit por fetch/autonomous foi bloqueada por `robots.txt` do Reddit. Não usar como fonte direta nesta rodada.
- Busca programática em DuckDuckGo/Bing e Shopify Community não retornou resultados confiáveis dentro do ambiente. Resultado: basear decisão em docs oficiais + fontes especialistas verificáveis; Reddit fica como opcional manual se Lucas trouxer links específicos.

## Síntese de melhores práticas

### 1. Carrinho abandonado não é só evento, é condição temporal

O evento útil é: checkout/cart criado ou atualizado. O abandono real exige:

- contato presente;
- recovery URL presente;
- `completed_at` vazio;
- `closed_at` vazio;
- idade mínima desde última atualização, ex.: 30-60 min;
- não houve pedido pago posterior;
- cliente não foi acionado recentemente;
- opt-in/consentimento adequado quando houver WhatsApp;
- idempotência por checkout/cart token e webhook delivery ID.

Portanto o desenho correto é híbrido:

- webhook para capturar evento em tempo real;
- fila/delayed eligibility check para esperar abandono real;
- reconciliação periódica leve para falhas de webhook.

### 2. Webhook Shopify precisa ser rápido e assíncrono

Shopify recomenda:

- validar `X-Shopify-Hmac-SHA256` usando corpo bruto;
- responder 200 rapidamente;
- processar em fila assíncrona;
- dedupe com `X-Shopify-Webhook-Id`;
- correlacionar com `X-Shopify-Event-Id` se houver múltiplas subscriptions;
- reconciliação periódica via API.

Para LK: endpoint webhook não deve criar conversa imediatamente; deve salvar evento e agendar verificação.

### 3. Chatwoot é camada de atendimento, não detector de carrinho

Chatwoot entra após a elegibilidade:

- criar/atualizar contato;
- criar/abrir conversa;
- adicionar labels;
- atribuir time;
- inserir nota privada com contexto e recovery URL;
- opcionalmente enviar template WhatsApp aprovado em fases posteriores.

MVP seguro: private note e fila humana antes de qualquer envio público.

### 4. WhatsApp exige opt-in, categoria correta e template fora da janela

Para carrinho abandonado por WhatsApp, normalmente é mensagem iniciada pela empresa; logo:

- precisa opt-in válido;
- fora da janela de 24h, usar template pré-aprovado;
- carrinho abandonado tende a ser marketing, não utilidade;
- pedidos transacionais podem usar template de utilidade quando confirmam pedido/pagamento/envio;
- mensagens livres só dentro da janela de atendimento aberta pelo cliente;
- monitorar qualidade/bloqueios/opt-out.

### 5. Sequência recomendada para carrinho abandonado

Base de mercado: sequência de 2-3 toques performa melhor que uma mensagem única, mas desconto não deve vir primeiro.

Proposta LK:

- T+45 min: lembrete humano/leve, sem desconto, com recovery URL.
- T+20-24h: reforço com benefícios/trust signals, loja física/Jardins, atendimento humano, formas de pagamento/segurança. Sem prometer estoque.
- T+48-72h: último toque com incentivo só se aprovado comercialmente; para LK pode ser cupom pequeno/frete/condição, mas exige aprovação e regra de margem.

No MVP Chatwoot, começar apenas com nota privada para humano antes de automatizar templates.

### 6. Conteúdo para LK Sneakers

Não usar pressão agressiva. Sneakers/alto ticket pedem confiança e atendimento consultivo.

Elementos bons:

- produto e tamanho quando disponíveis;
- recovery URL;
- lembrete curto;
- “se tiver dúvida de tamanho/modelo, te ajudo por aqui”;
- prova de confiança: loja física, atendimento humano, troca/devolução quando política confirmada;
- não falar que “ainda tem estoque” sem Tiny.

Elementos a evitar:

- prometer disponibilidade;
- prometer prazo;
- desconto automático sem regra;
- muitas mensagens;
- texto genérico demais;
- disparo sem opt-in.

## Arquitetura recomendada LK — MVP 1B

### Componentes

1. `lk-shopify-webhook-receiver`
   - endpoint público HTTPS;
   - valida HMAC Shopify;
   - registra payload mínimo/seguro;
   - dedupe por webhook ID;
   - responde 200 rápido;
   - salva evento em SQLite/arquivo persistente ou Postgres leve.

2. `delayed-eligibility-worker`
   - roda a cada poucos minutos;
   - busca eventos pendentes com idade >= 45 min;
   - consulta Shopify checkout/order para estado atual;
   - aplica filtros;
   - cria Chatwoot interno se elegível;
   - marca como processed/skipped.

3. `reconciliation-worker`
   - roda a cada 6h ou 1x/dia;
   - consulta checkouts recentes;
   - encontra eventos perdidos;
   - passa pela mesma elegibilidade;
   - não duplica.

4. Chatwoot internal action layer
   - API inbox `Shopify Carrinho Abandonado` para MVP interno;
   - futuramente WhatsApp inbox real para sends;
   - labels: `carrinho-abandonado`, `shopify`, `recuperacao`, `humano`, depois `pedido-feito`, `pedido-aprovado`, `pedido-enviado`, `pedido-recebido`, `follow-up-venda`.

### Tópicos Shopify candidatos

A confirmar por disponibilidade/permissões no shop/app atual:

- Checkout/cart lifecycle: capturar `checkouts/create` e/ou `checkouts/update` quando disponíveis no app/API atual.
- Orders lifecycle:
  - `orders/create` para pedido feito.
  - `orders/paid` para pedido aprovado/pago.
  - `fulfillments/create` ou fulfillment/order fulfillment event para pedido enviado.
  - `orders/fulfilled` / fulfillment delivered depende do carrier/tracking; pode exigir polling/fulfillment events ou app transportadora.
  - `orders/cancelled`, `refunds/create` para bloqueios/risco.

### Event taxonomy LK

- `cart_abandoned_candidate`
- `cart_abandoned_eligible`
- `cart_recovered`
- `order_created`
- `order_paid`
- `order_fulfilled_or_shipped`
- `order_delivered_candidate`
- `post_purchase_followup_due`

Cada evento deve ter:

- source: Shopify webhook/API/reconciliation;
- source ID/event ID;
- customer/contact ID;
- checkout/order ID;
- status atual;
- allowed_action: internal_only / utility_template / marketing_template / human_only;
- guardrail reason.

## Mensagens futuras via Chatwoot

### Pedido feito

Possível quando order/create chega.

- Pode ser utility se confirmar recebimento do pedido.
- Não deve prometer aprovação/prazo se pagamento ainda pendente.
- Chatwoot: criar conversa/nota ou enviar template utilidade quando WhatsApp inbox e template estiverem aprovados.

### Pedido aprovado

Possível em orders/paid ou financial_status paid.

- Utility.
- Pode informar que pagamento foi aprovado e equipe seguirá com separação/preparo.
- Não prometer estoque se não houver validação Tiny/processo operacional.

### Pedido enviado

Possível por fulfillment/create/update e tracking.

- Utility.
- Incluir código/link de rastreio se disponível.
- Se fulfillment for criado antes de envio real, não mandar “enviado” cedo demais; validar evento correto.

### Pedido recebido

Mais difícil; Shopify pode não saber entrega real sem tracking/carrier status.

- Melhor usar delivery event se transportadora/fulfillment fornece, ou regra de follow-up pós entrega estimada com linguagem cuidadosa: “chegou tudo certo?” apenas quando alto confidence.

### Follow-up de venda

Marketing/relacionamento.

- Exige opt-in e categoria marketing fora da janela.
- Deve ter cooldown, frequência máxima, segmentação por compra/produto, opt-out.
- Não misturar com mensagens transacionais.

## Regras anti-spam / reputação

- Máximo 1 conversa ativa de recuperação por checkout.
- Cooldown por telefone/email para carrinho: ex. 7 dias.
- Máximo 2-3 toques por carrinho.
- Não mandar se cliente comprou depois.
- Não mandar se conversa humana ativa/irritada/reclamação aberta.
- Respeitar opt-out.
- Registrar todo send com template, categoria, timestamp, motivo.
- Começar internal-only e liberar sends por fase.

## Decisão recomendada

Antes de implementar MVP 1B, desenhar o receiver como base universal de lifecycle messaging, não só carrinho:

- mesmo endpoint/processador para Shopify events;
- handlers separados por tipo de evento;
- estado/idempotência única;
- delayed jobs;
- Chatwoot adapter com `internal_only` por padrão;
- futuro WhatsApp sender com kill switch.

## Próximo passo técnico após pesquisa

Preparar implementation pack MVP 1B:

1. Listar webhooks existentes na Shopify para evitar duplicidade.
2. Confirmar tópicos disponíveis para checkout/cart/order/fulfillment no app/token atual.
3. Criar receiver `lk-shopify-lifecycle-receiver` com HMAC e fila.
4. Adicionar delayed check para carrinho abandonado.
5. Criar webhook Shopify apenas para tópico(s) necessários.
6. Smoke test com replay assinado.
7. Rodar em internal-only.
8. Registrar receipt.

Nenhuma mensagem pública deve ser ativada neste passo.
