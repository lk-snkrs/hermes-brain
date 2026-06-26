# PRD — Elle, Cérebro de Atendimento LK conectado ao Chatwoot

- Data: 2026-06-02
- Dono: LK Ops / Atendimento
- Produto: Elle — assistente operacional de atendimento LK
- Sistemas: Chatwoot, WhatsApp Business API, Shopify, Tiny, Hermes Brain
- Status: PRD v0 para revisão do Lucas

## 1. Resumo executivo

Criar a Elle, um cérebro de atendimento da LK Sneakers conectado ao Chatwoot para auxiliar e, futuramente, responder clientes no WhatsApp Business API com segurança operacional.

A Elle deve ler conversas do Chatwoot, entender intenção, consultar fontes vivas quando necessário, sugerir respostas para atendentes, aplicar labels/fila, e transbordar para humano quando houver risco. A Shopify será usada como contexto de cliente/pedido. Tiny permanece fonte oficial de estoque/disponibilidade.

A implantação deve começar em modo assistivo: a Elle gera nota privada/sugestão dentro do Chatwoot, sem enviar resposta pública. Resposta automática só deve ser liberada depois de validação por fases, com escopo restrito, kill switch e aprovação explícita.

## 2. Objetivos

### Objetivos principais

1. Centralizar atendimento WhatsApp no Chatwoot com inteligência operacional.
2. Reduzir tempo de primeira resposta sem comprometer precisão.
3. Ajudar atendentes com sugestões baseadas em política LK, histórico, Shopify e Tiny.
4. Identificar risco e fazer transbordo humano automaticamente.
5. Preparar base para automação segura e auditável.

### Objetivos secundários

1. Criar base de conhecimento viva no Hermes Brain para atendimento.
2. Padronizar tom, macros e decisões operacionais.
3. Medir volume por motivo: pedido, estoque, troca, devolução, prazo, reclamação, financeiro, VIP.
4. Criar trilha de auditoria de decisões da IA.

## 3. Não objetivos nesta fase

1. Não criar chatbot/widget no site.
2. Não ativar Captain/IA nativa do Chatwoot sem aprovação.
3. Não enviar mensagens automáticas ao cliente na fase 1.
4. Não alterar produtos, estoque, preço, pedido, tema, campanha ou webhook Shopify.
5. Não usar Shopify como fonte de verdade de estoque.
6. Não tomar decisão final automática sobre reclamação, desconto, reserva, troca complexa, devolução complexa ou prazo sensível.
7. Não comprar, reservar produto ou contatar fornecedor automaticamente.

## 4. Estado atual confirmado

1. Chatwoot self-hosted online em `https://chat.lkskrs.online`.
2. Conta Chatwoot: `LK Sneakers`, Account ID `1`.
3. Labels operacionais já criadas:
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
4. Time criado: `atendimento whatsapp`, auto-assign desligado.
5. Shopify conectada no Chatwoot:
   - loja `lk-sneakerss.myshopify.com`
   - feature `shopify_integration` habilitada
   - hook enabled.
6. Website inbox/chatbot não criado por decisão do Lucas.
7. WhatsApp Business API inbox ainda pendente de dados Meta.

## 5. Personas

### Cliente LK

Quer resposta rápida, humana e precisa sobre pedido, disponibilidade, prazo, troca, devolução, produto e compra.

### Atendente LK

Precisa de contexto rápido, sugestão de resposta, resumo do caso, risco e próximos passos.

### Lucas / Operação

Precisa de controle, rastreabilidade, qualidade e garantia de que automação não vai prometer preço, estoque, prazo ou desconto errado.

### Elle

Assistente operacional que prioriza segurança: ajuda primeiro, automatiza só quando permitido, e escala quando necessário.

## 6. Princípios de produto

1. Humano-first: automação serve o atendimento, não substitui decisão sensível.
2. Fonte viva antes de promessa.
3. Tiny é estoque oficial.
4. Shopify é contexto de pedido/cliente, não verdade final de disponibilidade.
5. Se houver ambiguidade, perguntar ou transbordar.
6. Toda ação automática deve ser auditável.
7. O cliente nunca deve perceber incerteza inventada.
8. Silêncio/escalação é melhor que resposta errada.

## 7. Escopo funcional

### 7.1 Ingestão de eventos Chatwoot

A Elle deve receber eventos do Chatwoot quando:

1. Nova mensagem de cliente chegar.
2. Conversa for criada.
3. Conversa mudar de status.
4. Label for aplicada/removida.
5. Atendente assumir conversa.
6. Mensagem privada for adicionada, se necessário para feedback.

### 7.2 Leitura de contexto

Para cada conversa, a Elle deve conseguir ler:

1. Mensagem atual.
2. Histórico recente da conversa.
3. Dados do contato: nome, telefone, e-mail, identificadores.
4. Inbox/canal.
5. Labels atuais.
6. Status da conversa.
7. Agente/time responsável.
8. Contexto Shopify disponível:
   - cliente
   - pedidos
   - status financeiro
   - fulfillment/status de entrega
   - link admin do pedido, quando seguro para uso interno.
9. Estoque Tiny ou snapshot operacional validado, quando a intenção envolver disponibilidade.
10. Políticas e macros do Brain Atendimento LK.

### 7.3 Classificação de intenção

A Elle deve classificar a conversa em uma ou mais intenções:

1. Saudação/início.
2. Consulta de pedido.
3. Prazo/entrega.
4. Disponibilidade/estoque/tamanho.
5. Produto/recomendação.
6. Troca.
7. Devolução.
8. Pagamento/financeiro.
9. Reclamação.
10. VIP/cliente recorrente.
11. Encomenda/preorder.
12. Cancelamento.
13. Pós-venda.
14. Outro/ambíguo.

### 7.4 Classificação de risco

Cada evento deve receber risco:

- Baixo: resposta factual, FAQ, pedido de dado, saudação, horário, endereço.
- Médio: pedido, prazo simples, troca simples, produto com alguma ambiguidade.
- Alto: reclamação, atraso, desconto, reserva, disponibilidade sem fonte, chargeback, ameaça, cliente irritado, decisão financeira, prazo sensível, encomenda/preorder, devolução sensível.

### 7.5 Ações possíveis

#### Fase 1 — assistivo, sem resposta pública

A Elle pode:

1. Criar nota privada no Chatwoot com sugestão de resposta.
2. Criar resumo da conversa.
3. Aplicar labels internas.
4. Sugerir próxima ação.
5. Sugerir transbordo humano.
6. Sugerir consulta Tiny/Shopify quando faltar fonte.

#### Fase 2 — automação restrita

Após aprovação, a Elle pode enviar resposta pública apenas para casos baixo risco, por exemplo:

1. Saudação inicial dentro da janela WhatsApp.
2. Pedido de e-mail/CPF/número do pedido para localizar compra.
3. Horário/endereço da loja.
4. Aviso de que vai verificar estoque.
5. Confirmação de recebimento e encaminhamento para humano.
6. FAQ de troca/devolução sem decisão específica.

#### Fase 3 — automação com fonte viva

Após validação, a Elle pode responder com base em fonte viva:

1. Status de pedido com Shopify, sem prometer prazo não confirmado.
2. Disponibilidade por SKU/tamanho após consulta Tiny oficial ou snapshot fresco com fallback.
3. Informação de produto se não envolver preço/promessa comercial sensível.

## 8. Transbordo humano

### Deve transbordar sempre

1. Reclamação ou cliente irritado.
2. Pedido atrasado ou divergente.
3. Solicitação de desconto/negociação.
4. Reserva de produto.
5. Cancelamento ou reembolso.
6. Troca/devolução fora de política simples.
7. Disponibilidade ambígua ou produto/tamanho não resolvido.
8. Encomenda/preorder.
9. Problemas financeiros/pagamento.
10. Pedido de fornecedor/atacado/parceria.
11. Qualquer confiança baixa.
12. Fora da janela de 24h do WhatsApp sem template aprovado.

### Ações de transbordo

1. Aplicar label `humano`.
2. Aplicar label de motivo, ex: `reclamacao`, `pedido`, `estoque`.
3. Atribuir ao time `atendimento whatsapp` ou deixar em fila conforme decisão operacional.
4. Criar nota privada com:
   - resumo
   - motivo do transbordo
   - evidências consultadas
   - sugestão de resposta
   - risco
5. Opcionalmente responder ao cliente, se aprovado:
   - “Vou chamar uma pessoa do nosso time para te ajudar com isso.”

## 9. Brain Atendimento LK

### Conteúdos necessários

1. Tom de voz LK.
2. Política de troca/devolução.
3. Regras de estoque e disponibilidade.
4. Regras de encomenda/preorder.
5. Regras de prazo/entrega.
6. Endereço/horário/contatos oficiais.
7. Macros aprovadas.
8. Respostas proibidas.
9. Matriz de risco.
10. Critérios de transbordo.
11. Glossário de produtos/marcas/tamanhos.
12. Procedimento de consulta Tiny.
13. Procedimento de consulta Shopify.
14. Regras LGPD/PII.

### Estrutura sugerida no Brain

- `areas/lk/sub-areas/atendimento/prd/`
- `areas/lk/sub-areas/atendimento/policies/`
- `areas/lk/sub-areas/atendimento/macros/`
- `areas/lk/sub-areas/atendimento/playbooks/`
- `areas/lk/sub-areas/atendimento/receipts/`
- `areas/lk/sub-areas/atendimento/evaluation/`

## 10. Integração com Shopify

### Uso permitido

1. Encontrar cliente por e-mail/telefone.
2. Ver pedidos recentes.
3. Ver status financeiro e fulfillment.
4. Ver itens comprados.
5. Ver contexto de pós-venda.
6. Ajudar o atendente com resumo.

### Uso não permitido sem aprovação específica

1. Alterar pedido.
2. Cancelar pedido.
3. Criar reembolso.
4. Alterar tags/notas/metafields.
5. Alterar produto/preço/estoque/tema.
6. Enviar campanha ou mensagem externa.

## 11. Integração com Tiny / estoque

### Regra principal

Tiny é a fonte de verdade para estoque/disponibilidade.

### Fluxo de disponibilidade

1. Resolver produto, variante, SKU e tamanho.
2. Se ambíguo, perguntar ao cliente ou escalar.
3. Consultar Tiny ou snapshot Tiny fresco.
4. Se fonte estiver ausente/stale, não prometer disponibilidade.
5. Responder com tamanho explícito.
6. Se for necessário reserva, desconto ou encomenda, transbordar humano.

## 12. WhatsApp Business API

### Regras

1. Dentro da janela de 24h: pode responder livremente conforme regras de automação aprovadas.
2. Fora da janela de 24h: só template aprovado pela Meta.
3. Templates devem ser criados/aprovados no WhatsApp Manager/Meta.
4. Chatwoot pode usar templates aprovados.
5. Não iniciar conversa automática sem aprovação.

### Templates recomendados

1. Solicitação de dados para localizar pedido.
2. Atualização de status/prazo.
3. Solicitação de dados para troca.
4. Aviso de disponibilidade.
5. Reativação pós-atendimento.
6. Encaminhamento para humano.

## 13. Modos de operação

### Modo 0 — leitura e diagnóstico

- Sem writes no Chatwoot.
- Apenas coleta métricas e simula decisões.

### Modo 1 — nota privada

- Cria notas privadas.
- Aplica labels se aprovado.
- Não envia mensagem pública.

### Modo 2 — resposta automática baixa criticidade

- Envia apenas respostas aprovadas de baixo risco.
- Mantém logs e kill switch.

### Modo 3 — resposta com fonte viva

- Responde pedido/estoque apenas com Shopify/Tiny verificados.
- Transborda em qualquer ambiguidade.

### Modo 4 — operação avançada

- Triagem, roteamento, resposta e follow-up com templates, mantendo aprovação por categoria.

## 14. Guardrails técnicos

1. Kill switch global.
2. Flag por inbox/canal.
3. Allowlist de intents automáticas.
4. Denylist de temas sensíveis.
5. Rate limit por conversa/cliente.
6. Janela de silêncio para evitar múltiplas respostas em sequência.
7. Idempotência por message_id/event_id.
8. Logs com decisão, fonte e confiança.
9. Não armazenar tokens em logs/Brain.
10. Redação automática de PII em relatórios.
11. Rollback: desativar webhook/agent e voltar para humano.
12. Modo dry-run antes de produção.

## 15. Métricas de sucesso

### Operacionais

1. Tempo de primeira resposta.
2. Tempo médio de resolução.
3. % conversas com sugestão útil.
4. % conversas transbordadas corretamente.
5. % respostas automáticas sem intervenção.
6. Taxa de erro operacional.

### Qualidade

1. Precisão de classificação de intenção.
2. Precisão de transbordo.
3. Taxa de resposta rejeitada pelo atendente.
4. Casos em que a IA tentou responder assunto proibido.
5. Satisfação do cliente/CSAT, se disponível.

### Segurança

1. Zero promessa errada de estoque/preço/prazo.
2. Zero envio fora de janela sem template.
3. Zero vazamento de token/PII.
4. Zero alteração externa não aprovada.

## 16. MVP recomendado

### MVP 1 — Elle Copiloto

Entregável:

1. Webhook Chatwoot read-only.
2. Classificador de intenção/risco.
3. Consulta Brain Atendimento.
4. Consulta Shopify contextual quando contato tiver e-mail/telefone.
5. Consulta Tiny apenas para intenção estoque/disponibilidade.
6. Nota privada com sugestão.
7. Labels automáticas opcionais.
8. Dashboard/relatório semanal simples.

Critério de sucesso:

- 80% das conversas recebem classificação correta.
- 70% das sugestões são aproveitáveis.
- 0 mensagens públicas automáticas.
- 0 writes externos além de nota privada/labels se aprovado.

### MVP 2 — Respostas automáticas seguras

Entregável:

1. Automação de saudação/FAQ baixo risco.
2. Kill switch.
3. Lista de intents permitidas.
4. Auditoria por conversa.
5. Transbordo humano automático.

Critério de sucesso:

- 95% de precisão nos casos automáticos.
- 0 respostas automáticas em temas proibidos.
- Atendente consegue intervir a qualquer momento.

## 17. Riscos e mitigação

### Risco: resposta errada de estoque

Mitigação: Tiny obrigatório, tamanho explícito, fallback humano.

### Risco: resposta automática sensível

Mitigação: denylist e classificação de risco.

### Risco: loop de mensagens

Mitigação: idempotência, cooldown por conversa e ignorar mensagens do próprio bot.

### Risco: Shopify parecer fonte de estoque

Mitigação: regra fixa no prompt e no policy engine.

### Risco: fora da janela WhatsApp

Mitigação: detectar janela; se fora, só template aprovado ou humano.

### Risco: vazamento de PII/tokens

Mitigação: redaction em logs e proibição de salvar secrets no Brain.

## 18. Dependências

1. WhatsApp Business API conectado ao Chatwoot.
2. API token Chatwoot seguro em cofre/Doppler.
3. Webhook Chatwoot configurado com assinatura/secret.
4. Brain Atendimento LK organizado.
5. Acesso read-only a Shopify via Chatwoot/API.
6. Acesso Tiny/snapshot operacional para estoque.
7. Lista de macros aprovadas.
8. Definição de quem é humano responsável por cada fila.

## 19. Perguntas em aberto

1. A fase 1 deve criar apenas nota privada ou também aplicar labels automaticamente?
2. Quem será o humano/time responsável pelo transbordo no Chatwoot?
3. Quais respostas podem ser 100% automáticas no primeiro piloto?
4. A Elle pode responder “vou chamar uma pessoa” automaticamente em casos de risco?
5. Qual será o horário de atendimento humano oficial?
6. Quais dados o cliente pode ser solicitado a enviar: CPF, e-mail, número do pedido, telefone?
7. Qual política oficial atual de troca/devolução deve entrar no Brain?
8. Devemos usar templates WhatsApp no MVP ou deixar para depois?
9. Qual métrica define que a fase 1 está pronta para fase 2?
10. Quem aprova macros e respostas automáticas finais?

## 20. Recomendação Superpowers

Aplicando o fluxo Superpowers/brainstorming, a recomendação é não ir direto para automação pública.

Abordagem recomendada:

1. Construir primeiro o PRD e matriz de risco.
2. Aprovar o modo de operação MVP 1.
3. Montar o Brain Atendimento LK.
4. Rodar Chatwoot em modo nota privada/draft-only.
5. Medir qualidade.
6. Só então liberar respostas automáticas por intent.

## 21. Pedido de decisão inicial

Decisão mais importante para avançar:

Escolher o modo do MVP 1:

- Opção A: nota privada apenas, sem labels automáticas.
- Opção B: nota privada + labels automáticas.
- Opção C: nota privada + labels + transbordo automático para time humano.

Recomendação: Opção B para primeiro piloto. Ela gera valor operacional sem enviar mensagem ao cliente e já organiza a fila.
