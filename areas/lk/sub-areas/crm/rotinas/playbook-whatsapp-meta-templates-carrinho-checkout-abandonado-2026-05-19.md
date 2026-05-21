# Playbook — Templates WhatsApp Meta para Carrinho/Checkout Abandonado LK

Data: 2026-05-19
Status: documento operacional / pré-configuração n8n + Crisp
Dono: Lucas Cimino / LK Sneakers
Área: LK CRM + CRO + Atendimento

## Contexto

Lucas confirmou que o Crisp não faz, sozinho, disparo de carrinho abandonado no WhatsApp. A solução operacional da LK deve usar n8n orquestrando a API do Crisp/WhatsApp para recuperação de carrinho e checkout abandonado.

Regra crítica: mensagens iniciadas pela empresa fora da janela de atendimento do WhatsApp precisam usar templates aprovados na Meta/WhatsApp Business Platform antes de qualquer disparo em produção.

## Stack confirmado / observado

- Loja: Shopify LK.
- Atendimento: site → Crisp/WhatsApp Business API.
- Automação: n8n em `n8n.lucascimino.com`.
- Crisp Website ID observado no site: presente.
- Workflows n8n existentes, inativos, para:
  - `LK - Carrinho Abandonado 30min`.
  - `LK - Carrinho Abandonado 24h`.
  - `LK - Carrinho Abandonado 72h`.
- Endpoint usado nos workflows existentes: plugin WhatsApp do Crisp (`plugins.crisp.chat/.../whatsapp.../template/send`).
- Templates referenciados nos workflows:
  - `carrinho_abandonado_30min`.
  - `carrinho_abandonado_24h`.
  - `carrinho_abandonado_72h`.

## Fonte externa estudada

Pesquisa Meta/WhatsApp Business Platform via SERP/DataForSEO e documentação pública:

- Meta for Developers — Template fundamentals: templates são ativos da WhatsApp Business Account e têm categorias específicas.
- Meta for Developers — Template categorization: categorias principais incluem Marketing, Utility e Authentication.
- Meta for Developers — Send message templates / Cloud API: templates aprovados são usados para mensagens iniciadas pela empresa.
- SERP de referência indicou explicitamente que lembretes de abandoned cart tendem a cair em Marketing, não Utility.

Nota: a documentação Meta é dinâmica e a classificação final é decidida pela Meta durante review; este playbook deve ser revisado antes de submissão final se a política mudar.

## Implicação para LK

### Checkout abandonado

Mais confiável para WhatsApp, porque geralmente já há dados de contato no checkout:

- nome;
- telefone;
- produto;
- link de recuperação;
- status de pagamento/conclusão.

Pode ser automatizado se houver consentimento/opt-in adequado e template Meta aprovado.

### Carrinho abandonado

Só é viável por WhatsApp se houver telefone associado antes do checkout. Caso contrário, não há destinatário válido para WhatsApp.

A LK deve tratar “carrinho abandonado” como:

- carrinho com telefone conhecido; ou
- evento de checkout iniciado, ainda não pago; ou
- lead capturado pelo Crisp/site antes do checkout.

## Categorias Meta recomendadas

### `carrinho_abandonado_30min`

Categoria recomendada para submissão: **Marketing**.

Motivo: a mensagem tenta recuperar uma compra não concluída e incentiva retorno ao checkout. Mesmo com tom consultivo, isso é reengajamento comercial.

Evitar tentar classificar como Utility, salvo se a mensagem for estritamente transacional e ligada a uma ação indispensável solicitada pelo cliente. Risco alto de recategorização para Marketing.

### `carrinho_abandonado_24h`

Categoria recomendada: **Marketing**.

Se incluir cupom, desconto, benefício, escassez ou incentivo, será Marketing com ainda mais clareza.

### `carrinho_abandonado_72h`

Categoria recomendada: **Marketing**.

Tom deve ser de último toque consultivo e sem pressão, mas continua sendo recuperação comercial.

## Estrutura recomendada de template Meta

### Regras gerais

- Idioma: `pt_BR`.
- Nome técnico: minúsculo, snake_case, sem acento.
- Variáveis numeradas na Meta; no n8n/Crisp mapear para nome, produto, link/cupom.
- Evitar excesso de variáveis no começo/fim da mensagem.
- Evitar promessas de estoque/prazo no texto fixo.
- Não usar “pronta entrega”, “encomenda” ou “estoque” como taxonomia.
- Usar tom LK: premium, humano, consultivo, sem pressão.
- Incluir opt-out operacional onde fizer sentido: “Se preferir, é só me avisar que não envio novos lembretes.”
- Não enviar se o checkout já foi pago/concluído.
- Não enviar sem telefone válido/opt-in.

## Copy canônica para avaliação Meta

Prioridade máxima: usar a decisão viva em `../decisions/2026-05-20-checkout-abandonado-copy-canonica.md` como fonte de verdade antes de editar template Meta/Crisp/n8n. Se houver conflito entre este playbook e a decisão viva, a decisão viva prevalece.

A sequência deve parecer atendimento humano da LK, não automação agressiva. Deve recuperar intenção de compra sem prometer estoque/prazo e sem pressionar.

### Template 30min — principal, sem desconto

Nome sugerido: `lk_checkout_abandonado_30min`
Categoria: Marketing
Objetivo: recuperar logo após abandono, com tom de concierge.

Componentes:

- Header: imagem do produto, se a Meta/Crisp aceitar mídia no template.
- Body:

```text
Oi {{1}}, aqui é da LK. Vi que você estava olhando {{2}} e deixamos seu checkout salvo por aqui.

Na LK, todos os produtos têm garantia de originalidade. Se quiser, nosso atendimento pode te ajudar com a numeração e finalizar tudo com segurança.
```

Variáveis:

- `{{1}}`: primeiro nome.
- `{{2}}`: nome curto do produto/modelo.

Botão:

- Tipo: URL.
- Texto: `Finalizar compra`
- URL dinâmica: link de recuperação do checkout.

Observação: se a Meta exigir variável no botão como sufixo, o n8n deve enviar apenas o token/sufixo esperado pelo template aprovado.

### Template 24h — consultivo, sem cupom por padrão

Nome sugerido: `lk_checkout_abandonado_24h`
Categoria: Marketing
Objetivo: segundo toque, ainda sem desconto, reforçando atendimento humano e sem repetir o território “finalizar com segurança” do T1.

Body:

```text
Oi {{1}}, tudo bem?

Passando só para saber se ficou alguma dúvida sobre {{2}}. Se quiser, nosso atendimento pode te ajudar com numeração, detalhes do produto ou retomar seu checkout salvo.
```

Botão:

- Texto preferencial: `Finalizar compra`
- Header: imagem do produto quando o template/canal suportar `HEADER IMAGE`.

### Template 24h — alternativa com cupom, usar só com aprovação comercial

Nome sugerido: `lk_checkout_abandonado_24h_cupom`
Categoria: Marketing
Objetivo: recuperação com incentivo comercial controlado.

Body:

```text
Oi {{1}}, seu checkout da LK ainda está salvo.

Para facilitar sua decisão sobre {{2}}, separei uma condição especial para você finalizar: {{3}}.
```

Variáveis:

- `{{1}}`: primeiro nome.
- `{{2}}`: produto/modelo.
- `{{3}}`: cupom.

Guardrail: cupom/desconto só com aprovação comercial explícita de Lucas.

### Template 72h — último toque, sem pressão

Nome sugerido: `lk_checkout_abandonado_72h`
Categoria: Marketing
Objetivo: último lembrete consultivo, sem insistência.

Body:

```text
Oi {{1}}, passando só para saber se ainda faz sentido te ajudar com {{2}}.

A curadoria LK pode confirmar os detalhes pelo atendimento, sem pressa. Se não quiser receber novos lembretes, é só me avisar.
```

Botão:

- Preferência 1: `Falar com a LK`.
- Preferência 2: `Voltar ao checkout`.

### Copy que não deve ser usada

Evitar:

- “Seu carrinho está te esperando” — genérico e varejista demais.
- “Últimas unidades” — risco de promessa de estoque.
- “Finalize agora” — tom agressivo.
- “Pronta entrega” — fora do guardrail LK.
- “Desconto exclusivo” sem aprovação comercial.
- Mensagens longas com muitos emojis ou urgência artificial.

## Checklist antes de submeter na Meta

- [ ] Confirmar se os templates atuais `carrinho_abandonado_30min`, `carrinho_abandonado_24h`, `carrinho_abandonado_72h` já existem e qual o status: approved / pending / rejected / paused.
- [ ] Confirmar categoria atual na Meta: Marketing / Utility / Authentication.
- [ ] Confirmar idioma `pt_BR`.
- [ ] Confirmar se o botão dinâmico usa token, URL completa ou sufixo.
- [ ] Confirmar se imagem de header está aprovada e se a URL de imagem é pública/estável.
- [ ] Confirmar opt-in/origem do telefone.
- [ ] Confirmar regra de supressão: não enviar se pedido pago/concluído.
- [ ] Confirmar deduplicação por checkout/cliente/janela.
- [ ] Confirmar limite de frequência: 30min, 24h e 72h no máximo, sem repetição infinita.
- [ ] Fazer envio teste apenas para número interno antes de produção.

## Checklist n8n/Crisp antes de produção

- [ ] Workflows permanecem inativos enquanto templates não estiverem aprovados.
- [ ] Revalidar webhook Shopify correto para checkout criado/atualizado.
- [ ] Normalizar telefone para formato WhatsApp.
- [ ] Checar status do checkout/pedido imediatamente antes do envio.
- [ ] Logar receipt sem expor tokens.
- [ ] Registrar erro de API Crisp/Meta por template rejeitado, paused, missing parameter ou recipient inválido.
- [ ] Ter kill switch para pausar todos os disparos.
- [ ] Ativar primeiro apenas 30min, monitorar 24–48h, depois 24h/72h.

## Aprovações necessárias

Exigem aprovação explícita atual de Lucas:

- criar/editar/submeter template na Meta;
- alterar template no Crisp;
- alterar workflow n8n;
- ativar workflow;
- enviar teste real por WhatsApp;
- enviar qualquer mensagem para cliente;
- criar cupom/desconto Shopify.

Permitido sem aprovação adicional:

- auditoria read-only dos workflows;
- inventário dos templates e status se a credencial permitir leitura;
- draft de copy/template;
- pacote de aprovação com risco/rollback.

## Rollback / Kill switch

- Desativar workflow n8n.
- Pausar template na Meta/Crisp se necessário.
- Remover/invalidar cupom criado para teste.
- Registrar receipt e motivo.

## Decisão recomendada

1. Primeiro mapear status real dos templates no Meta/Crisp.
2. Se não aprovados, submeter os três como Marketing.
3. Ajustar n8n para usar nomes aprovados e parâmetros exatos.
4. Testar internamente.
5. Ativar produção em rollout gradual: 30min → 24h → 72h.

## Pesquisa — melhores práticas Shopify + n8n para carrinho/checkout abandonado

Data: 2026-05-19

### Fontes consultadas

- Shopify Dev — Abandoned checkouts REST resource: expõe `abandoned_checkout_url`, dados de contato, consentimentos (`buyer_accepts_sms_marketing`, email marketing etc.) e checkout para recuperação.
- Shopify Help / SERP: Shopify tem automações de abandoned checkout e cada email contém link para o cliente completar checkout; abandoned checkouts antigos podem ser removidos do admin após cerca de 3 meses.
- n8n workflow templates:
  - Smart Shopify agent: monitora abandono de checkout, usa espera estratégica e envia mensagens personalizadas somente se necessário.
  - Recover Shopify abandoned carts with email/SMS/WhatsApp/Facebook: escuta eventos via webhook, normaliza/enriquece dados, segmenta cliente, checa status antes de cada toque, registra touchpoints e usa sequência multicanal.
  - Abandoned cart recovery via Gmail/Sheets/Twilio: trigger em checkout criado, espera 1h, checa se abandonado, envia recuperação e registra log.
- SERPs de melhores práticas 2025/2026: sequência comum de 3 toques em 30–60min/1h, 24h e 48–72h; primeiro toque sem desconto; incentivo só depois; mensagens personalizadas com produto/imagem/link; limite de frequência e opt-in.
- WhatsApp/cart recovery SERPs: WhatsApp funciona melhor com opt-in, poucas mensagens por abandono, personalização, timing rápido e sem excesso de pressão.

### Descobertas principais

1. Priorizar checkout abandonado sobre carrinho puro.

Checkout abandonado é mais operacionalmente confiável porque a Shopify normalmente já tem telefone/email, nome, item, preço e `abandoned_checkout_url`. Carrinho puro antes do checkout só vira WhatsApp se a LK já conhece o telefone do cliente.

2. Melhor timing é rápido, mas não instantâneo.

Padrão de mercado:

- 30–60min ou 1h: lembrete útil, sem desconto.
- 24h: segundo toque, reforço de ajuda/social proof/condição.
- 48–72h: último toque; desconto/cupom só se a margem e política comercial permitirem.

Para LK, manter 30min / 24h / 72h é coerente, desde que haja checagem de pedido antes de cada envio.

3. Primeiro toque não deve ter cupom.

Boas práticas recomendam não treinar cliente a abandonar carrinho para ganhar desconto. O primeiro toque deve ser assistência/recuperação de intenção, especialmente para marca premium.

4. Personalização importa mais que urgência genérica.

Usar:

- primeiro nome;
- nome curto do produto/modelo;
- imagem do produto, se aprovada no template;
- link direto de recuperação;
- ajuda humana sobre numeração/autenticidade/finalização.

Evitar:

- urgência artificial;
- “últimas unidades”;
- “finalize agora”;
- desconto sem aprovação;
- texto genérico de varejo.

5. Para WhatsApp, compliance é parte do produto.

Antes de produção:

- opt-in/consentimento validado;
- template Meta aprovado, provavelmente categoria Marketing;
- opt-out simples;
- limite de 2–3 toques por abandono;
- não enviar se comprado/pago;
- não enviar fora de janela/regra definida.

6. n8n deve ser orquestrador, não só disparador.

Workflow robusto precisa:

- receber evento Shopify;
- enriquecer checkout/carrinho;
- normalizar telefone;
- deduplicar;
- aguardar janela;
- consultar Shopify antes de enviar;
- mandar template aprovado via Crisp;
- registrar touchpoint/receipt;
- pausar em caso de erro/qualidade.

### Implementação recomendada no n8n para LK

#### Workflow A — ingestão e normalização

Trigger:

- Shopify checkout/create ou webhook equivalente para checkout criado/atualizado.

Nós:

1. Webhook/Shopify Trigger.
2. Code node: normalizar payload.
3. HTTP Shopify: buscar checkout completo se necessário.
4. Code node: extrair `firstName`, `phone`, `productName`, `productImage`, `abandoned_checkout_url`, `checkoutToken`, `email`, `totalPrice`, `createdAt`.
5. IF: só continuar se telefone válido + opt-in/consentimento aceitável + checkout não pago.
6. Storage/Supabase/Sheet: criar registro `checkout_recovery_journey` com status `pending`.

#### Workflow B — toque 30min

1. Wait 30min.
2. HTTP Shopify: reconsultar checkout/pedido.
3. IF: abortar se pago/concluído, sem telefone, opt-out ou já tocado.
4. HTTP Crisp: enviar template `lk_checkout_abandonado_30min`.
5. Log touchpoint: timestamp, template, checkout id/token, response status.

#### Workflow C — toque 24h

1. Wait até 24h desde abandono.
2. Rechecar status.
3. Opcional: segmentar por valor, cliente novo/recorrente, produto premium.
4. Enviar `lk_checkout_abandonado_24h` sem cupom por padrão.
5. Cupom só se Lucas aprovar e se política de margem permitir.
6. Log touchpoint.

#### Workflow D — toque 72h

1. Wait até 72h.
2. Rechecar status e frequência.
3. Enviar último toque `lk_checkout_abandonado_72h`.
4. Marcar jornada como `closed_no_purchase` se não recuperar.

### Regras de supressão obrigatórias

- Não enviar se `completed_at`, pedido pago ou order associada existir.
- Não enviar se número inválido.
- Não enviar se cliente pediu opt-out.
- Não enviar mais de uma sequência ativa por telefone/checkouts muito próximos; priorizar o checkout mais recente ou de maior valor.
- Não enviar múltiplos canais no mesmo minuto; evitar colisão com Klaviyo/email.
- Não criar cupom automaticamente sem aprovação comercial.

### Métricas para medir

- Checkouts elegíveis.
- Mensagens enviadas por etapa.
- Erros Crisp/Meta por template/parâmetro/destinatário.
- Conversas respondidas.
- Checkouts recuperados até 7 dias.
- Receita recuperada.
- Opt-out/reclamação.
- Tempo até compra após toque.
- Performance por produto/coleção/ticket.

### Recomendação LK

Usar o n8n em rollout conservador:

1. Validar templates Meta.
2. Ativar apenas 30min com número interno/teste.
3. Ativar 30min em produção por 24–48h.
4. Só depois ativar 24h.
5. 72h por último, com copy leve e opt-out.
6. Cupom fica fora do MVP.

Para LK, a melhor recuperação não é “desconto”; é atendimento humano + autenticidade + segurança para finalizar compra.


## Auditoria Meta/Crisp — 2026-05-19

### 1) WABA/phone number correto para templates/automação

Leitura via Meta Graph API, read-only, sem expor tokens, corrigida por Lucas em 2026-05-19:

- Business Manager LK: `LK Sneakers & Streetwear`, verificado.
- WABA correta: `1478026007140488` — `LK Sneakers & Apparels`.
- Phone number principal observado no site e Meta: `+55 11 94956-5000`.
- Phone ID ativo/Cloud API: `1220780761111140`.
- Verified name: `LK Sneakers & Apparels`.
- Quality rating: `GREEN`.
- Account mode: `LIVE`.

Correção importante: a WABA `2510782939372375` também retornou o mesmo phone ID em leitura Meta, mas Lucas confirmou que **não** é a fonte correta para configurar os templates da LK. Não usar `2510782939372375` como WABA-alvo para este fluxo.

Observação adicional: a WABA chamada `[CRISP] LK Sneakers Apparels` (`1325252949533317`) apareceu sem phone numbers e sem templates. Portanto, não deve ser assumida como canal operacional de envio sem confirmação adicional no Crisp.

### 2) Match com templates existentes

Os templates antigos `carrinho_abandonado_30min`, `carrinho_abandonado_24h`, `carrinho_abandonado_72h` estão `APPROVED`, `MARKETING`, `pt_BR`, mas na WABA `890575517349631`, que não retornou phone numbers na leitura Meta.

Conclusão: esses templates aprovados existem, mas provavelmente não são utilizáveis pelo número principal `+55 11 94956-5000`/Cloud API sem migração ou recriação na WABA operacional.

Além disso, a copy antiga tem problemas para o padrão LK:

- 24h e 72h usam cupom/10% e urgência de validade.
- 30min menciona disponibilidade/prazo no texto fixo.
- Tom mais automático e menos concierge.

### 3) Templates novos criados/submetidos na Meta

Com aprovação atual de Lucas no Telegram, foram criados via Meta Graph API os templates premium v2. Primeiro houve submissão por engano na WABA `2510782939372375`; após correção explícita de Lucas, os templates foram submetidos também na WABA correta `1478026007140488`.

Templates válidos para seguir no fluxo LK:

- `lk_checkout_abandonado_30min_v2`
  - WABA correta: `1478026007140488`
  - ID Meta: `2974977079371297`
  - categoria: `MARKETING`
  - idioma: `pt_BR`
  - status inicial/readback: `PENDING`

- `lk_checkout_abandonado_24h_v2`
  - WABA correta: `1478026007140488`
  - ID Meta: `949744811275279`
  - categoria: `MARKETING`
  - idioma: `pt_BR`
  - status inicial/readback: `PENDING`

- `lk_checkout_abandonado_72h_v2`
  - WABA correta: `1478026007140488`
  - ID Meta: `1391578509473920`
  - categoria: `MARKETING`
  - idioma: `pt_BR`
  - status inicial/readback: `PENDING`

Templates submetidos por engano na WABA `2510782939372375`:

- `1592240055740756` — `lk_checkout_abandonado_30min_v2` — `PENDING`.
- `1477752790704277` — `lk_checkout_abandonado_24h_v2` — `PENDING`.
- `2476432172830263` — `lk_checkout_abandonado_72h_v2` — `PENDING`.

Não usar os IDs da WABA `2510782939372375` no n8n/Crisp. Avaliar remoção/pausa dos templates errados após aprovação explícita, se a Meta permitir.

Nenhum fluxo n8n foi ativado e nenhuma mensagem foi enviada.

### Como criar templates Meta via API — padrão aprendido

Endpoint:

```text
POST /{whatsapp_business_account_id}/message_templates
```

Campos mínimos usados:

- `name`: snake_case, minúsculo, sem acento.
- `language`: `pt_BR`.
- `category`: `MARKETING`.
- `components`: `BODY` + `BUTTONS`.
- exemplos obrigatórios para variáveis do body e do botão URL.

Padrão de botão URL usado:

```json
{
  "type": "URL",
  "text": "Voltar ao checkout",
  "url": "https://lksneakers.com.br/checkouts/{{1}}",
  "example": ["abc123def"]
}
```

Implicação para n8n/Crisp: ao enviar, mapear o botão URL para o sufixo/token do checkout esperado pelo template, não necessariamente a URL completa. Validar contra a recovery URL real da Shopify antes de produção.

### Próximos gates antes de produção

- [ ] Aguardar status `APPROVED` dos três templates v2.
- [ ] Confirmar no Crisp se o canal de envio usa o phone ID `1220780761111140` ou a WABA `2510782939372375`.
- [ ] Corrigir o n8n para usar os nomes v2 apenas depois de aprovados.
- [ ] Validar regra de URL dinâmica: token/sufixo vs URL completa.
- [ ] Envio teste somente para número interno após aprovação explícita.
- [ ] Ativar produção primeiro apenas no 30min após teste interno aprovado.
