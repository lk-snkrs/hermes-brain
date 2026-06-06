# PRD — LK pós-venda WhatsApp 30min para compras POS

Data: 2026-06-05
Área: LK Ops / Atendimento
Status: rascunho v0.1 — aguardando copy/mensagem final de Lucas e aprovação de implementação/produção
Solicitante: Lucas Cimino

## 1. Pedido original

Lucas pediu um novo projeto para que, para cada cliente que comprar na loja física, o sistema envie uma mensagem para a cliente **30 minutos depois da compra**.

Condições dadas por Lucas:

- venda da loja física = pedido Shopify realizado no **POS**;
- descobrir o vendedor pelo pedido de venda;
- o vendedor está em uma tag no pedido no formato `vendedor: Nome do Vendedor`;
- Lucas vai mandar a mensagem/copy que deverá ser enviada.

## 2. Objetivo

Criar um fluxo automático de pós-venda para compras presenciais da LK Sneakers:

1. detectar pedido pago feito no POS;
2. identificar cliente contactável;
3. extrair vendedor pela tag `vendedor: <nome>`;
4. aguardar 30 minutos após a compra;
5. enviar mensagem WhatsApp ao cliente usando a copy aprovada;
6. registrar receipt local/Brain com status, vendedor, pedido e resultado, sem expor dados sensíveis.

## 3. Não objetivo / fora de escopo

Este projeto **não** deve:

- enviar mensagem sem copy aprovada por Lucas;
- prometer disponibilidade, troca, desconto, prazo, reserva ou preço sem fonte/aprovação;
- alterar Shopify, Tiny, estoque, preço ou pedido;
- alterar tags do pedido;
- contatar fornecedor;
- criar campanha em massa sem rate limit/kill switch;
- enviar para pedidos não-POS;
- enviar se não houver telefone válido/consentimento operacional mínimo;
- substituir atendimento humano em reclamações sensíveis.

## 4. Fonte de verdade e gatilho

### Fonte/gatilho

- Shopify é o gatilho/evento do pedido POS.
- Tiny continua sendo fonte de verdade de estoque, mas este fluxo não precisa consultar estoque por padrão.

### Evento recomendado

- Webhook Shopify `orders/paid`, reaproveitando o padrão já validado no projeto POS restock.

### Critérios para considerar elegível

Pedido elegível quando:

- `financial_status` em `paid`, `partially_paid`, `partially_refunded` se aprovado;
- `cancelled_at` vazio;
- pedido POS:
  - `source_name == "pos"`, ou
  - `app_id == 129785`;
- telefone do cliente disponível no payload ou recuperável de forma autorizada;
- ainda não foi enviado pós-venda para aquele pedido;
- passou a janela de 30 minutos desde `created_at`/horário da venda.

## 5. Extração do vendedor

### Regra principal

Ler tags do pedido Shopify e procurar padrão:

```text
vendedor: Nome do Vendedor
```

### Normalização

- aceitar variações de caixa: `Vendedor:`, `VENDEDOR:`;
- trim de espaços;
- preservar nome humano para personalização;
- se houver múltiplas tags `vendedor:`, usar a primeira válida e registrar alerta de ambiguidade.

### Fallback

Se vendedor não for encontrado:

- não bloquear necessariamente o envio, se Lucas aprovar mensagem sem vendedor;
- registrar `seller_missing=true`;
- usar copy fallback sem nome do vendedor.

Decisão pendente: Lucas confirmar se vendedor ausente deve **bloquear envio** ou **enviar sem personalização**.

## 6. Mensagem / copy

Lucas informou que vai mandar a mensagem.

### Variáveis que o template poderá usar

- `{cliente_nome}` — primeiro nome do cliente, se disponível;
- `{vendedor_nome}` — extraído da tag `vendedor:`;
- `{pedido_nome}` — ex.: `#1234`;
- `{loja}` — LK Sneakers;
- `{produto_resumo}` — opcional, nomes dos itens comprados, se aprovado;
- `{link_contato}` — opcional, se houver link/canal aprovado.

### Guardrail de copy

A mensagem não pode conter promessa material sem fonte viva/aprovação, como:

- desconto garantido;
- prazo de troca/devolução se não for política validada;
- disponibilidade de novos produtos;
- reserva;
- brinde;
- condição comercial.

## 7. Canal de envio

Opções possíveis, a confirmar por Lucas antes da implementação:

### Opção A — WhatsApp direto via wacli/conta LK

- Prós: rápido, usa infraestrutura local já existente.
- Contras: pode ter risco operacional/compliance e depende da conta WhatsApp certa; precisa rate limit e logs fortes.

### Opção B — WhatsApp Business API / Chatwoot

- Prós: mais governável, melhor histórico, templates e caixa de atendimento.
- Contras: pode exigir template aprovado se fora da janela permitida e integração adicional.

### Recomendação inicial

Para produção, preferir **Chatwoot/WhatsApp Business API** se já estiver operacional para atendimento. Para MVP controlado, pode ser feito com wacli/conta aprovada somente após aprovação explícita de Lucas contendo:

- conta WhatsApp exata;
- texto exato;
- público/escopo;
- rate limit;
- kill switch;
- rollback.

## 8. Arquitetura proposta

### Componentes

1. **Webhook receiver Shopify POS pós-venda**
   - rota sugerida: `lk-shopify-pos-postpurchase-30min`;
   - valida HMAC Shopify via proxy Vercel + HMAC Hermes, mesmo padrão do POS restock.

2. **Processor local**
   - script sugerido: `/opt/data/scripts/lk_pos_postpurchase_30min.py`;
   - recebe payload do pedido;
   - valida elegibilidade;
   - extrai cliente, telefone, vendedor, pedido e itens;
   - grava job pendente local.

3. **Fila local / scheduler seguro**
   - persistência SQLite ou JSON state em:
     `/opt/data/hermes_bruno_ingest/local_sql/lk_pos_postpurchase_30min/`;
   - job com `send_after = purchase_time + 30min`;
   - dedupe por `order_id` e `webhook_id`;
   - retries limitados;
   - kill switch por arquivo/env.

4. **Sender aprovado**
   - wacli ou Chatwoot/WhatsApp API, conforme decisão;
   - envia somente quando job elegível e copy aprovada.

5. **Receipt/handoff**
   - registrar status em Brain/receipts sem PII integral;
   - log local com hash de telefone, pedido, vendedor e status.

## 9. Fluxo operacional

```text
Shopify orders/paid
  ↓
Vercel proxy valida Shopify HMAC
  ↓
Hermes webhook valida HMAC Hermes
  ↓
Processor POS pós-venda
  ↓
Filtro POS/pago/não cancelado
  ↓
Extrai cliente/telefone/vendedor tag vendedor:
  ↓
Cria job send_after = compra + 30min
  ↓
Scheduler verifica jobs vencidos
  ↓
Renderiza copy aprovada
  ↓
Envia WhatsApp aprovado
  ↓
Registra receipt + dedupe
```

## 10. Regras de dedupe e segurança

- nunca enviar duas vezes para o mesmo `order_id`;
- se Shopify reenviar webhook, tratar como duplicate;
- se pedido for cancelado antes dos 30 min, não enviar;
- se telefone estiver ausente/inválido, não enviar e registrar `missing_phone`;
- se copy não estiver configurada/aprovada, não enviar;
- se kill switch ativo, não enviar;
- se houver erro no envio, retry limitado e depois `failed_needs_human`;
- registrar todos os status sem imprimir telefone completo no Telegram/Brain.

## 11. Status possíveis

- `received`
- `ignored_not_pos`
- `ignored_not_paid`
- `ignored_cancelled`
- `missing_phone`
- `missing_message_template`
- `scheduled`
- `sent`
- `duplicate`
- `failed_retry_pending`
- `failed_needs_human`
- `killed_by_switch`

## 12. Métricas de aceite

MVP aprovado quando:

- payload POS pago gera job agendado para +30min;
- payload não-POS é ignorado sem envio;
- pedido cancelado antes do envio é bloqueado;
- vendedor é extraído corretamente de tag `vendedor: Nome`;
- vendedor ausente segue a regra aprovada;
- telefone ausente não envia;
- dedupe impede reenvio;
- mensagem usa exatamente a copy aprovada;
- teste dry-run mostra preview sem envio;
- teste controlado envia para 1 pedido/telefone aprovado;
- receipt registra status e rollback.

## 13. Riscos

### Risco: envio externo indevido

Mitigação:

- require aprovação explícita da copy e canal;
- dry-run primeiro;
- kill switch;
- rate limit;
- dedupe.

### Risco: telefone errado/incompleto

Mitigação:

- validar formato E.164/BR;
- usar telefone do customer/order do Shopify;
- se ambíguo, não enviar.

### Risco: mensagem fora de política WhatsApp

Mitigação:

- se via WhatsApp Business API/Chatwoot, validar janela/template;
- se via wacli, escopo de MVP controlado antes de produção.

### Risco: vendedor não identificado

Mitigação:

- tag parser robusto;
- fallback aprovado;
- alerta/handoff para pedidos sem tag.

## 14. Rollback

- pausar/remover rota webhook `lk-shopify-pos-postpurchase-30min`;
- ativar kill switch local;
- parar scheduler local;
- manter state/log para auditoria;
- não remover receipts;
- se houver mensagem enviada indevida, registrar incidente e escalar Lucas.

## 15. Decisões pendentes de Lucas

1. Enviar por qual canal?
   - WhatsApp direto via wacli/conta LK;
   - Chatwoot/WhatsApp Business API;
   - outro.
2. Qual é a mensagem/copy exata?
3. Se a tag `vendedor:` faltar, envia sem vendedor ou bloqueia?
4. O envio deve incluir nome do produto/pedido ou só agradecimento geral?
5. Enviar para todos os clientes POS ou começar com canary limitado?
6. Qual conta/remetente WhatsApp deve mandar?

## 16. Aprovação necessária para implementação

Este PRD ainda **não autoriza produção**.

Para implementar, Lucas deve aprovar explicitamente:

- canal de envio;
- copy final;
- conta/remetente;
- comportamento para vendedor ausente;
- canary ou produção total;
- permissão para criar rota/script/scheduler local;
- permissão para enviar teste externo controlado.

## 17. Próximo passo recomendado

Lucas enviar a copy da mensagem. Depois preparar:

1. preview de mensagem com variáveis;
2. plano técnico de implementação;
3. approval packet para dry-run;
4. canary com 1 pedido POS controlado.
