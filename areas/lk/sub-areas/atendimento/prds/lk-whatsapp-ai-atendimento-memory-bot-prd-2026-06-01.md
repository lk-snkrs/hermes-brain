# PRD — LK WhatsApp AI Atendimento com Memória e Aprovação

Data: 2026-06-01
Área: LK / Atendimento / WhatsApp / Operações
Autor: Hermes LK Ops
Método: Superpowers — brainstorming + PRD-first + guardrails antes de implementação
Status: PRD v1 — decisão Lucas registrada: seguir com Opção 3 (inbox/plataforma intermediária: Crisp/Twilio/Z-API/WATI). Default recomendado para desenho: Crisp/inbox com humano + IA, salvo escolha posterior de outro provider.

## 1. Contexto

Lucas quer que Hermes ajude a responder clientes pelo WhatsApp como um bot/assistente de atendimento prévio, com memória por cliente e capacidade de consultar fontes da LK antes de sugerir ou enviar respostas.

O objetivo não é substituir o atendimento humano nem liberar respostas sensíveis sem controle. O objetivo é criar uma camada de triagem e assistência que:

- leia mensagens recebidas no WhatsApp;
- entenda intenção do cliente;
- recupere memória/contexto do cliente;
- consulte fontes vivas quando necessário;
- gere rascunhos ou respostas seguras;
- escale para humano quando houver risco;
- só envie automaticamente quando a classe da mensagem estiver dentro dos guardrails aprovados.

## 2. Problema

Hoje o atendimento depende de memória humana e troca manual entre WhatsApp, Shopify, Tiny, CRM e contexto informal. Isso gera:

- demora para responder perguntas simples;
- inconsistência na resposta sobre estoque, tamanho, modelo e pedido;
- risco de prometer disponibilidade/preço/prazo sem fonte viva;
- perda de histórico útil por cliente;
- dificuldade de saber quando o bot deve responder, sugerir ou calar.

## 3. Objetivos

### Objetivos do MVP

1. Conectar uma fonte de mensagens WhatsApp a Hermes de forma segura.
2. Criar memória operacional por cliente/conversa.
3. Classificar mensagens por tipo e risco.
4. Gerar rascunhos de resposta para atendimento.
5. Auto-responder apenas casos simples e aprovados.
6. Escalar para humano casos sensíveis.
7. Registrar receipts e aprendizado reutilizável no Brain/SQLite.

### Objetivos específicos para LK

- Responder dúvidas simples sobre produtos quando estoque for verificado em Tiny/SQLite local.
- Usar Tiny como fonte de verdade de estoque.
- Usar Shopify como superfície de pedido/produto/evento, não como ledger de estoque.
- Não prometer preço, desconto, reserva, prazo, troca ou solução de reclamação sem fonte viva ou humano.
- Aprender preferências e histórico do cliente sem armazenar dados desnecessários.

## 4. Não-objetivos do MVP

- Não criar robô que responde tudo sozinho.
- Não enviar negociação, desconto, promessa de entrega ou reserva sem aprovação.
- Não substituir Larissa/time de atendimento.
- Não escrever em Tiny/Shopify/CRM no MVP sem aprovação separada.
- Não usar polling pesado como arquitetura principal quando webhook/event-driven for possível.
- Não depender de memória do LLM como fonte de verdade.

## 5. Usuários

### Cliente final

Pessoa que chama a LK pelo WhatsApp perguntando sobre produto, tamanho, pedido, troca, disponibilidade ou atendimento geral.

### Atendente LK

Pessoa que precisa responder rápido, com segurança e tom correto.

### Lucas / Gestão

Precisa de visibilidade, controle, métricas e segurança operacional.

## 6. Princípios de produto

1. Fonte viva antes de promessa.
2. Silêncio é melhor que resposta errada.
3. Memória ajuda contexto, mas não vira fonte de verdade para estoque/preço/status.
4. Primeiro observar, depois sugerir, depois responder automaticamente só o que for seguro.
5. Toda automação externa deve ter modo de rollback.
6. WhatsApp deve ser limpo: nada de logs técnicos para cliente.
7. Humanos assumem reclamações, negociações, exceções e baixa confiança.

## 7. Arquitetura recomendada

### Opção A — wacli / WhatsApp linked device

Uso de conta WhatsApp conectada como dispositivo via `wacli`.

Vantagens:

- Já existe no ambiente.
- Boa para grupos internos e protótipos rápidos.
- Permite leitura local e envio via conta conectada.

Riscos:

- Sessão pode desconectar.
- Não é tão robusto quanto API oficial.
- Pode ter limites/risco operacional se usado para atendimento crítico em volume.

Uso recomendado:

- Piloto interno.
- Assistência ao time.
- Grupos internos.
- Observe-only e draft mode.

### Opção B — WhatsApp Business Cloud API oficial

Uso da API oficial da Meta/WhatsApp Business.

Vantagens:

- Mais robusta para atendimento real.
- Webhooks oficiais.
- Melhor para SLA e produção.
- Melhor governança para templates e conversas.

Riscos:

- Setup mais burocrático.
- Regras de templates e janela de 24h.
- Pode exigir ajuste de número/Business Manager.

Uso recomendado:

- Produção para clientes.
- Bot com mensagens transacionais e atendimento contínuo.

### Opção C — plataforma intermediária: Crisp, Z-API, Twilio, WATI, etc.

Uso de uma plataforma de atendimento/mensageria com API e caixa compartilhada.

Vantagens:

- Inbox para humanos.
- Webhooks e handoff mais prontos.
- Pode ter tags, notas internas e atribuição.

Riscos:

- Custo e lock-in.
- Diferença entre provider e fonte de verdade.
- Precisa validar segurança, webhook e controle de envio.

Uso recomendado:

- Se a LK quiser uma central de atendimento com humano + bot.
- Especialmente se Crisp já fizer parte do stack de chat/site.

## 8. Recomendação

Fazer em fases:

### Fase 0 — PRD e desenho de política

Este documento.

### Fase 1 — Observe-only

Hermes lê mensagens, classifica e registra sinais, mas não responde clientes.

Saídas:

- intenção detectada;
- risco;
- cliente/conversa;
- fontes necessárias;
- rascunho opcional;
- sugestão de próxima ação.

### Fase 2 — Draft para humano

Hermes gera rascunho e entrega para o atendente aprovar/copiar/enviar.

### Fase 3 — Auto-resposta segura

Hermes responde automaticamente apenas classes A0/A1, por exemplo:

- saudação simples;
- horário/endereço/link básico já aprovado;
- confirmação de recebimento;
- pergunta de estoque quando Tiny/SQLite tiver match confiável e resposta não prometer reserva;
- pedido de informação faltante.

### Fase 4 — Handoff operacional

Hermes cria tarefas, tags, notas internas e follow-ups, sempre com recibo.

### Fase 5 — Produção avançada

Somente depois de métricas e confiança: mais automações, CRM e integrações de escrita com aprovações específicas.

## 9. Matriz de autonomia A0-A4

### A0 — Pode auto-responder

Condições:

- pergunta simples;
- resposta aprovada e conhecida;
- sem preço negociado;
- sem promessa de reserva/prazo;
- sem reclamação sensível;
- sem status de pedido incerto.

Exemplos:

- “Oi, tudo bem? Já te ajudo.”
- “Me manda o tamanho que você procura?”
- “Vou verificar disponibilidade certinha antes de confirmar.”

### A1 — Pode auto-responder com fonte viva

Condições:

- consulta Tiny/SQLite/Shopify/CRM feita;
- match alto;
- resposta não promete reserva;
- inclui linguagem segura.

Exemplo:

- “No momento encontrei disponibilidade no estoque consultado para esse modelo/tamanho. Quer que eu encaminhe para o atendimento finalizar?”

### A2 — Rascunho para aprovação humana

Casos:

- disponibilidade com baixa confiança;
- múltiplos produtos parecidos;
- cliente quer desconto;
- prazo/entrega;
- troca simples;
- status de pedido com dados parciais.

### A3 — Escalar para humano sem rascunho final

Casos:

- reclamação;
- cliente irritado;
- chargeback;
- item com defeito;
- pedido atrasado;
- negociação fora da política;
- pedido de reserva;
- pagamento ou reembolso.

### A4 — Bloqueado

Casos:

- prometer desconto/reserva/prazo sem aprovação;
- contatar fornecedor;
- emitir decisão final de reclamação;
- alterar pedido/estoque/preço;
- enviar campanha/bulk message;
- manipular dados sensíveis sem base legal/operacional.

## 10. Memória do atendimento

### O que memorizar

Por cliente/conversa:

- nome preferido;
- canal/origem;
- histórico resumido de interesse;
- tamanhos buscados;
- marcas/modelos de interesse;
- última intenção;
- pendências abertas;
- tom adequado, quando aprendido de respostas humanas;
- flags de risco: reclamação, atraso, troca, VIP, atacado, fornecedor, etc.

### O que não memorizar

- dados de cartão;
- documentos sensíveis desnecessários;
- prints brutos sem necessidade;
- segredos/tokens;
- promessa comercial que não foi confirmada;
- estoque/preço como fato durável.

### Regra crítica

Memória pode dizer: “cliente costuma comprar New Balance 38”.

Memória não pode dizer: “tem New Balance 38 disponível hoje”.

Disponibilidade atual precisa vir de Tiny/SQLite local atualizado ou consulta live.

## 11. Fontes de verdade

### Estoque

- Tiny: fonte final.
- SQLite local: mirror operacional rápido, alimentado por fullsync e webhooks.
- Shopify: evento/superfície, não ledger.

### Pedido

- Shopify/Tiny/CRM conforme o dado.

### Política comercial

- Brain LK + decisões aprovadas pelo Lucas/time.

### Conversa

- WhatsApp provider/inbox escolhido.
- Memória resume, não substitui a conversa original.

## 12. Componentes técnicos

### Ingress de mensagens

Recebe mensagens via:

- wacli webhook/sync para piloto; ou
- WhatsApp Cloud API webhook; ou
- Crisp/Twilio/Z-API webhook.

Responsabilidades:

- validar assinatura/token;
- normalizar payload;
- deduplicar eventos;
- identificar cliente e conversa;
- ignorar mensagens do próprio bot;
- evitar loops.

### Router de intenção

Classifica:

- saudação;
- produto/estoque/tamanho;
- status de pedido;
- troca/devolução;
- reclamação;
- negociação/desconto;
- follow-up;
- humano necessário;
- spam/irrelevante.

### Policy engine

Aplica A0-A4 e decide:

- responder automaticamente;
- gerar rascunho;
- pedir dado faltante;
- escalar;
- bloquear.

### Memory service

Armazena memória mínima e auditável:

- SQLite local para MVP;
- possível CRM/Supabase no futuro;
- logs com hash/IDs minimizados quando possível.

### Source resolvers

Conectores read-only:

- Tiny estoque;
- Shopify pedido/produto;
- SQLite local estoque;
- Brain políticas;
- eventualmente CRM/Crisp.

### Reply composer

Gera resposta com tom LK:

- curta;
- humana;
- sem jargão técnico;
- sem prometer além da fonte;
- com handoff quando necessário.

### Delivery gateway

Envia por WhatsApp apenas quando autorizado pela política e pelo estágio do rollout.

## 13. Fluxo de mensagem

1. Cliente envia mensagem no WhatsApp.
2. Provider envia webhook para Hermes.
3. Hermes valida assinatura e deduplica.
4. Hermes normaliza conversa/cliente.
5. Hermes consulta memória do cliente.
6. Hermes classifica intenção e risco.
7. Se for estoque/produto, consulta SQLite/Tiny.
8. Policy engine decide A0-A4.
9. Composer gera resposta ou rascunho.
10. Delivery envia, cria nota interna ou escala para humano.
11. Memory service atualiza resumo/pending state.
12. Receipt é salvo para auditoria.

## 14. Requisitos funcionais

### RF1 — Receber mensagens

O sistema deve receber mensagens WhatsApp por webhook/sync e criar evento normalizado.

### RF2 — Identificar cliente/conversa

O sistema deve mapear número/JID/conversation_id para um perfil de memória.

### RF3 — Classificar intenção

O sistema deve classificar intenção principal e nível A0-A4.

### RF4 — Consultar fontes

Para estoque, pedido ou política, o sistema deve consultar fonte viva antes de gerar resposta final.

### RF5 — Criar memória resumida

O sistema deve atualizar memória com preferências e pendências, sem guardar dado sensível desnecessário.

### RF6 — Gerar rascunho

O sistema deve gerar resposta sugerida para humano nos casos A2.

### RF7 — Auto-responder casos seguros

O sistema pode auto-responder A0/A1 apenas após aprovação do rollout.

### RF8 — Escalar risco

O sistema deve marcar A3/A4 como humano necessário e não enviar decisão final.

### RF9 — Anti-loop

O sistema deve ignorar mensagens do bot, operador ou plugin.

### RF10 — Auditoria

Toda ação relevante deve registrar evento, decisão de política e fonte usada.

## 15. Requisitos não funcionais

- Latência alvo para A0: até 5 segundos.
- Latência alvo para A1 estoque via SQLite: até 10 segundos.
- Falha segura: sem fonte → sem promessa.
- Logs com segredos redigidos.
- Idempotência por message_id/delivery_id.
- Modo silent-OK para rotinas recorrentes.
- Rollback simples: desligar auto-send e manter observe-only.

## 16. Dados e schema inicial

### Tabela `customer_memory`

Campos sugeridos:

- `customer_id`
- `phone_hash`
- `display_name`
- `last_seen_at`
- `summary`
- `preferences_json`
- `risk_flags_json`
- `open_items_json`
- `tone_notes`
- `updated_at`

### Tabela `conversation_events`

Campos sugeridos:

- `event_id`
- `provider`
- `conversation_id`
- `customer_id`
- `direction`
- `message_type`
- `body_redacted`
- `intent`
- `autonomy_level`
- `policy_decision`
- `source_refs_json`
- `created_at`

### Tabela `reply_decisions`

Campos sugeridos:

- `decision_id`
- `event_id`
- `draft_text`
- `final_text`
- `decision`
- `approved_by`
- `sent_at`
- `blocked_reason`
- `created_at`

## 17. Métricas de sucesso

### Operacionais

- % mensagens classificadas corretamente.
- % mensagens com resposta sugerida útil.
- tempo médio até rascunho.
- tempo médio até resposta final.
- número de bloqueios corretos A3/A4.

### Qualidade

- taxa de correção humana nos rascunhos.
- taxa de escalonamento necessário.
- incidentes de promessa indevida: alvo zero.
- respostas com fonte viva quando exigido: alvo 100%.

### Negócio

- redução de tempo de primeira resposta.
- aumento de conversões assistidas.
- recuperação de clientes interessados por produto/tamanho.

## 18. Rollout

### Canary 0 — Local observe-only

- Lê mensagens de um canal/conta controlada.
- Não envia nada.
- Gera relatório local.

Critério de avanço:

- 50 mensagens analisadas;
- sem vazamento de dados sensíveis;
- classificação aceitável.

### Canary 1 — Draft interno

- Envia rascunhos para Telegram/atendente.
- Humano envia manualmente.

Critério de avanço:

- 80% dos rascunhos aproveitáveis;
- zero promessa indevida.

### Canary 2 — Auto-resposta A0

- Auto-responde apenas saudação, coleta de tamanho e confirmação simples.

Critério de avanço:

- zero incidentes;
- baixa taxa de intervenção.

### Canary 3 — Auto-resposta A1 com fonte viva

- Produto/estoque simples com Tiny/SQLite confiável.

Critério de avanço:

- 100% respostas com source_ref;
- bloqueio correto em baixa confiança.

## 19. Riscos

### Risco: responder cliente com dado errado de estoque

Mitigação:

- Tiny como fonte de verdade.
- SQLite com freshness metadata.
- Bloquear baixa confiança.

### Risco: bot prometer reserva/desconto/prazo

Mitigação:

- Policy engine A2/A3/A4.
- Testes de frases proibidas.
- Auto-send restrito.

### Risco: loop com atendente ou bot

Mitigação:

- Ignorar mensagens próprias/operator/plugin.
- Dedup por message_id.

### Risco: privacidade/memória excessiva

Mitigação:

- Memória resumida, minimizada.
- PII reduzida em logs.
- Não guardar dados sensíveis.

### Risco: wacli desconectar

Mitigação:

- Watchdog de auth/sync.
- Alerta somente quando desconectado.
- Para produção, avaliar WhatsApp Business Cloud API.

## 20. Decisões pendentes

1. Canal principal do MVP:
   - wacli com conta atual;
   - WhatsApp Cloud API oficial;
   - Crisp/Twilio/Z-API/WATI.

2. Conta/número usado:
   - número Hermes;
   - número atendimento LK;
   - número pessoal/gestão apenas para draft.

3. Primeiro modo:
   - observe-only;
   - draft para humano;
   - auto-resposta A0.

4. Onde o humano aprova:
   - Telegram Lucas;
   - grupo interno WhatsApp;
   - inbox da plataforma;
   - painel futuro.

5. Escopo inicial:
   - atendimento LK geral;
   - só estoque/produto;
   - só clientes do site;
   - só grupo interno.

## 21. Plano de implementação resumido

### Etapa 1 — Escolher provider e conta

Definir se o piloto será wacli ou WhatsApp Business/API/plataforma.

### Etapa 2 — Criar ingest observe-only

Webhook/sync normaliza mensagens e salva eventos.

### Etapa 3 — Criar memória local

SQLite com `customer_memory`, `conversation_events`, `reply_decisions`.

### Etapa 4 — Criar router A0-A4

Classificador determinístico + LLM controlado para nuance, sempre com policy final determinística.

### Etapa 5 — Integrar fontes LK

Tiny/SQLite estoque, Shopify pedido/produto, Brain políticas.

### Etapa 6 — Draft mode

Gerar rascunhos para humano com fonte e motivo.

### Etapa 7 — Auto A0

Liberar respostas simples pré-aprovadas.

### Etapa 8 — Auto A1 estoque confiável

Liberar estoque/produto com fonte viva e linguagem sem promessa de reserva.

## 22. Critério de pronto do MVP

O MVP está pronto quando:

- mensagens entram por provider escolhido;
- cada mensagem tem evento normalizado;
- cliente tem memória resumida atualizada;
- A0-A4 classifica corretamente em fixtures;
- estoque usa Tiny/SQLite com freshness;
- rascunho inclui fonte/risco;
- auto-send pode ser desligado por flag;
- logs não vazam segredos;
- existe receipt no Brain;
- testes cobrem assinatura, dedup, anti-loop, A0-A4 e bloqueios.

## 23. Recomendação final do Hermes

Para reduzir risco, começar com:

1. `observe_only` usando wacli se for piloto interno ou WhatsApp Cloud/Crisp se já for atendimento real.
2. Memória local SQLite por cliente.
3. Draft mode para humano.
4. Auto-resposta só A0 depois de validação.
5. Auto-resposta A1 estoque só quando Tiny/SQLite resolver com alta confiança.

Não recomendo começar com bot respondendo tudo diretamente ao cliente.

## 24. Próxima decisão para Lucas

Escolher a superfície do piloto:

- Opção 1: wacli, mais rápido para piloto, menos robusto.
- Opção 2: WhatsApp Business Cloud API, mais correto para produção.
- Opção 3: Crisp/Twilio/Z-API/WATI, melhor se quiser inbox humano + bot no mesmo lugar.

Minha recomendação: se for para clientes reais da LK, desenhar para WhatsApp Business Cloud API ou inbox oficial/intermediário; usar wacli apenas como piloto/controlado.
