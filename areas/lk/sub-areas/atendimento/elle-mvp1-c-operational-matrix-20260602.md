# Elle MVP 1C — Matriz operacional Chatwoot

- Data: 2026-06-02
- Produto: Elle — Cérebro de Atendimento LK
- Modo aprovado: C — nota privada + labels + transbordo automático para humano
- Canal alvo: Chatwoot / WhatsApp Business API
- Conta Chatwoot: LK Sneakers / Account ID 1
- Time padrão de transbordo: `atendimento whatsapp`

## 1. Escopo do modo C

A Elle pode, no MVP 1C:

1. Ler conversa e contexto.
2. Classificar intenção e risco.
3. Aplicar labels internas.
4. Criar nota privada para atendente.
5. Transbordar/atribuir para time humano quando a regra exigir.

A Elle não pode, no MVP 1C:

1. Enviar resposta pública ao cliente.
2. Prometer preço, disponibilidade, reserva, desconto, prazo ou negociação.
3. Alterar Shopify, Tiny, WhatsApp/Meta, pedido, produto, estoque, tema, campanha ou automação externa.
4. Encerrar conversa automaticamente.
5. Usar Shopify como fonte final de estoque.

## 2. Labels disponíveis

Labels já preparadas no Chatwoot:

- `pedido`
- `estoque`
- `troca`
- `devolucao`
- `prazo`
- `reclamacao`
- `vip`
- `financeiro`
- `humano`
- `whatsapp-api`

## 3. Regras gerais

### 3.1 Fonte de verdade

- Estoque/disponibilidade: Tiny ou snapshot operacional Tiny fresco.
- Pedido/cliente/contexto: Shopify/Chatwoot.
- Política/macros: Hermes Brain Atendimento LK.

### 3.2 Risco

- Baixo: FAQ, saudação, pedido de dado, endereço, horário, informação institucional.
- Médio: pedido simples, status simples, produto com pouca ambiguidade, troca/devolução simples.
- Alto: reclamação, atraso, financeiro, negociação, desconto, reserva, cancelamento, reembolso, disponibilidade ambígua, encomenda, cliente irritado, baixa confiança.

### 3.3 Transbordo

Toda conversa de risco alto recebe:

- label `humano`
- label de motivo
- atribuição/sugestão ao time `atendimento whatsapp`
- nota privada com resumo, risco e motivo

No MVP 1C, o transbordo é interno. Não há mensagem automática pública.

## 4. Matriz por intenção

### 4.1 Saudação / abertura

- Labels: `whatsapp-api`
- Risco: baixo
- Transborda: não, salvo linguagem agressiva ou pedido sensível na mesma mensagem
- Fontes: Brain macros
- Nota privada:
  - resumo da mensagem
  - sugestão de cumprimento
  - pedir dado se necessário
- Proibido: responder publicamente automático no MVP 1C

### 4.2 Pedido / status de compra

- Labels: `pedido`, `whatsapp-api`
- Risco: médio
- Transborda quando:
  - cliente reclama de atraso
  - pedido divergente
  - pedido não localizado
  - pedido cancelado/reembolsado
  - cliente pede decisão de prazo/compensação
- Fontes:
  - Shopify para pedido/cliente
  - Brain para política de comunicação
- Nota privada:
  - pedido encontrado ou não
  - status financeiro/fulfillment se disponível
  - sugestão de resposta sem prometer prazo sensível
- Proibido:
  - cancelar pedido
  - reembolsar
  - alterar pedido
  - prometer data sem fonte

### 4.3 Prazo / entrega

- Labels: `prazo`, `pedido`, `whatsapp-api`
- Risco: médio/alto
- Transborda sempre se:
  - atraso
  - cliente irritado
  - entrega divergente
  - transportadora/problema logístico
  - prazo prometido anteriormente
- Fontes:
  - Shopify fulfillment/status
  - Brain políticas
  - fonte logística se disponível futuramente
- Nota privada:
  - status observado
  - risco
  - sugestão segura
- Proibido:
  - prometer nova data final sem validação humana/fonte logística

### 4.4 Estoque / disponibilidade / tamanho

- Labels: `estoque`, `whatsapp-api`
- Risco: médio/alto
- Transborda se:
  - produto/tamanho/SKU ambíguo
  - Tiny ausente/stale
  - pedido de reserva
  - pedido de desconto/negociação
  - encomenda/preorder
  - inconsistência Shopify vs Tiny
- Fontes:
  - Tiny ou snapshot operacional Tiny fresco
  - Shopify só para contexto do produto, nunca verdade final de estoque
- Nota privada:
  - produto resolvido
  - tamanho explícito
  - fonte/freshness Tiny
  - sugestão ou bloqueio
- Proibido:
  - afirmar disponibilidade sem Tiny
  - prometer reserva
  - calcular estoque por delta Shopify

### 4.5 Produto / recomendação

- Labels: `estoque` se envolver disponibilidade; `whatsapp-api`
- Risco: baixo/médio
- Transborda se:
  - envolve disponibilidade real
  - preço/desconto
  - reserva
  - recomendação complexa ou cliente VIP
- Fontes:
  - Brain catálogo/políticas
  - Shopify contexto de produto
  - Tiny se estoque
- Nota privada:
  - intenção do cliente
  - produtos citados
  - perguntas de clarificação

### 4.6 Troca

- Labels: `troca`, `whatsapp-api`
- Risco: médio/alto
- Transborda sempre se:
  - troca fora de política simples
  - produto usado/danificado
  - prazo limite
  - troca internacional/encomenda
  - cliente insatisfeito
- Fontes:
  - Brain política de troca
  - Shopify pedido/contexto
- Nota privada:
  - pedido/cliente, se localizado
  - política aplicável
  - dados faltantes
  - sugestão de resposta
- Proibido:
  - aprovar troca automaticamente
  - prometer custo/prazo final

### 4.7 Devolução

- Labels: `devolucao`, `whatsapp-api`, normalmente `humano`
- Risco: alto
- Transborda: sim, sempre no MVP 1C
- Fontes:
  - Brain política
  - Shopify pedido/contexto
- Nota privada:
  - resumo
  - pedido relacionado
  - dados faltantes
  - risco
- Proibido:
  - aprovar devolução/reembolso automaticamente

### 4.8 Reclamação

- Labels: `reclamacao`, `humano`, `whatsapp-api`
- Risco: alto
- Transborda: sim, sempre
- Fontes:
  - Brain política de atendimento sensível
  - Shopify se pedido relacionado
- Nota privada:
  - resumo objetivo
  - tom do cliente
  - pedido/contexto
  - sugestão empática sem decisão final
- Proibido:
  - decisão final automática
  - culpar cliente/transportadora
  - prometer compensação

### 4.9 Financeiro / pagamento

- Labels: `financeiro`, `humano`, `whatsapp-api`
- Risco: alto
- Transborda: sim, sempre
- Fontes:
  - Shopify status financeiro se pedido existe
  - Brain política
- Nota privada:
  - pedido/status financeiro observado
  - risco
  - sugestão de encaminhamento
- Proibido:
  - alterar pagamento
  - prometer estorno/reembolso
  - pedir dados sensíveis excessivos

### 4.10 VIP / cliente recorrente

- Labels: `vip`, motivo principal, `whatsapp-api`
- Risco: depende da intenção; mínimo médio
- Transborda: sim se cliente pede negociação, reserva, reclamação ou pedido sensível
- Fontes:
  - Shopify histórico de pedidos
  - Brain regra VIP se existir
- Nota privada:
  - indicação de recorrência
  - resumo do histórico relevante sem expor PII desnecessária
  - sugestão de cuidado humano

### 4.11 Encomenda / preorder

- Labels: `estoque`, `humano`, `whatsapp-api`
- Risco: alto
- Transborda: sim, sempre
- Fontes:
  - Brain regras de encomenda
  - Tiny/Shopify apenas contexto
- Nota privada:
  - produto/tamanho desejado
  - fonte consultada
  - alerta de decisão humana
- Proibido:
  - prometer prazo/preço/reserva/encomenda automaticamente

### 4.12 Fora de escopo / ambíguo

- Labels: `humano`, `whatsapp-api`
- Risco: alto por incerteza
- Transborda: sim
- Fontes: Brain para triagem
- Nota privada:
  - por que está ambíguo
  - pergunta sugerida para clarificar

## 5. Formato padrão da nota privada

```text
Elle — sugestão interna

Resumo:
- [resumo curto da mensagem/conversa]

Intenção:
- [pedido/estoque/troca/devolucao/prazo/reclamacao/financeiro/etc.]

Labels sugeridas/aplicadas:
- [labels]

Risco:
- baixo | médio | alto

Fontes consultadas:
- Chatwoot: [sim/não]
- Shopify: [pedido/cliente encontrado?]
- Tiny: [consultado? freshness?]
- Brain: [política/macro]

Sugestão para o atendente:
- [texto que humano pode revisar/copiar]

Transbordo:
- [sim/não]
- Motivo: [regra acionada]

Bloqueios:
- [ex: não prometer estoque sem Tiny, não aprovar devolução]
```

## 6. Plano técnico sem produção ainda

### 6.1 Componentes

1. Webhook receiver da Elle.
2. Validador de assinatura/secret do webhook.
3. Filtro de eventos Chatwoot.
4. Idempotência por event/message id.
5. Classificador de intenção/risco.
6. Recuperador de contexto Chatwoot.
7. Consulta Shopify via contexto Chatwoot/API quando necessário.
8. Consulta Tiny/snapshot para estoque.
9. Policy engine de guardrails.
10. Writer Chatwoot:
   - nota privada
   - labels
   - assignment/transbordo
11. Audit log local/Brain.
12. Kill switch.

### 6.2 Eventos permitidos no MVP

- `message_created` de cliente/incoming
- `conversation_created`
- opcional: `conversation_updated` quando status/labels mudam

Ignorar:

- mensagens outbound do atendente
- notas privadas criadas pela própria Elle
- eventos repetidos
- conversas resolvidas, salvo regra futura

### 6.3 Writes Chatwoot permitidos após aprovação técnica

No MVP 1C, os únicos writes candidatos são:

1. Criar nota privada.
2. Aplicar/remover labels operacionais.
3. Atribuir ao time/agente humano.

Não permitido:

1. Mensagem pública.
2. Fechar conversa.
3. Criar automação que envia para cliente.
4. Alterar inbox/canal produtivo sem nova aprovação.

## 7. Critérios de aceite MVP 1C

1. Nenhuma mensagem pública automática enviada.
2. Todas as notas privadas têm risco, fontes e sugestão.
3. Reclamação/financeiro/devolução sempre recebem `humano`.
4. Estoque só recebe sugestão com Tiny/fonte oficial ou bloqueio claro.
5. Shopify usado somente como contexto.
6. Eventos duplicados não criam notas duplicadas.
7. Kill switch testado.
8. Logs não contêm tokens.
9. Operação pode ser desligada sem quebrar Chatwoot.

## 8. Approval packet para próxima etapa

Antes de criar webhook/agent produtivo, Lucas deve aprovar explicitamente:

```text
Aprovo o MVP 1C da Elle no Chatwoot em modo sem mensagem pública:
- criar notas privadas
- aplicar labels operacionais
- transbordar para o time atendimento whatsapp
- não enviar mensagens públicas ao cliente
- não alterar Shopify/Tiny/WhatsApp/produtos/pedidos/estoque/preço/tema
- usar Shopify só como contexto e Tiny como fonte de estoque
```

Sem esse approval packet, o estado atual permanece documentação/plano.
