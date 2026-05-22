# PRD — Crisp Marketplace Plugin como cérebro de resposta Hermes/LK

**Data:** 2026-05-21  
**Empresa/área:** LK Sneakers → CRM / Atendimento / Crisp  
**Decisão base:** implementar via **Crisp Marketplace Plugin + Hermes Brain**, **não via Hugo**.  
**Status:** PRD técnico v1 para aprovação antes de implementação.

---

## 1. Resumo executivo

Criar um plugin privado no Crisp Marketplace para conectar o Crisp Chat ao Hermes Brain. O plugin recebe eventos de conversa por **Plugin Hooks**, consulta o Hermes/Brain e fontes vivas aprovadas, decide se pode responder automaticamente e envia a resposta pelo **Crisp REST API**. Quando a resposta envolver risco comercial/operacional, o sistema escala para Larissa/humano em vez de inventar.

O MVP não usa Hugo, Workflow API nem MCP Hugo. Hugo pode permanecer fora do fluxo até existir uma decisão explícita futura.

---

## 2. Problema

Hoje a inteligência de resposta do Crisp tende a ficar fragmentada entre automações, Hugo/workflows, callbacks e conhecimento manual da operação. Isso cria risco de:

- respostas sem fonte viva;
- disponibilidade/preço incorretos;
- falhas de handoff para humano;
- pouca rastreabilidade do motivo da resposta;
- dificuldade de reaproveitar o Brain da LK em outros canais.

---

## 3. Objetivo

Construir uma camada oficial e auditável para o Crisp onde:

1. Crisp envia eventos para um endpoint Hermes via plugin.
2. Hermes normaliza a conversa e consulta Brain/fontes vivas.
3. Hermes classifica o risco da resposta.
4. Hermes responde via Crisp REST API somente quando permitido.
5. Hermes escala para humano quando faltar fonte, regra ou autorização.
6. Toda decisão relevante gera receipt/log sem expor segredo.

---

## 4. Não objetivos do MVP

- Não usar Hugo como cérebro principal.
- Não usar Hugo Workflow API.
- Não usar Hugo MCP API.
- Não publicar o plugin publicamente no Marketplace.
- Não alterar Docker/VPS/gateway produtivo sem plano/rollback e aprovação explícita.
- Não implementar escrita em Shopify/Tiny/CRM sem etapa posterior aprovada.
- Não prometer reserva, desconto, negociação ou prazo sem fonte aprovada.

---

## 5. Usuários e stakeholders

- **Cliente final:** pessoa conversando no WhatsApp/site via Crisp.
- **Larissa/time humano:** recebe escalonamentos e casos sensíveis.
- **Lucas:** aprova guardrails, autonomia e escopo produtivo.
- **Hermes Brain:** fonte operacional de regras, memória, receipts e contexto.
- **Crisp:** canal oficial de conversa e API de envio/leitura.

---

## 6. Arquitetura alvo

```text
Cliente no Crisp/WhatsApp/Site
  ↓
Crisp Plugin Hooks
  ↓ HTTPS POST
Hermes Crisp Plugin Gateway
  ↓ valida assinatura + idempotência
Fila/normalizador de eventos
  ↓
Motor de decisão Hermes Brain
  ↓ consulta regras + fontes vivas
Classificação A0-A4 de autonomia
  ↓
Ação:
  A0/A1: responder via REST API Crisp
  A2: sugerir/rascunhar ou responder com fonte forte, se permitido
  A3/A4: escalar para Larissa/humano
  ↓
Receipt/log seguro no Brain
```

---

## 7. Componentes

### 7.1 Crisp Marketplace Plugin

Responsável por:

- credenciais de produção do plugin;
- escopos REST mínimos;
- configuração do endpoint de Plugin Hooks;
- instalação privada no workspace/site da LK.

Credenciais já registradas no Doppler `lc-keys/prd`:

- `CRISP_MARKETPLACE_IDENTIFIER`
- `CRISP_MARKETPLACE_KEY`
- `CRISP_MARKETPLACE_SIGNING_SECRET`
- `CRISP_MARKETPLACE_PLUGIN_ID`
- `CRISP_MARKETPLACE_PLUGIN_URN`

Nunca imprimir valores em logs, receipts ou Telegram.

### 7.2 Hermes Crisp Plugin Gateway

Endpoint público HTTPS, versão inicial proposta:

```text
POST /integrations/crisp/plugin-hooks
GET  /integrations/crisp/health
```

Funções:

- receber eventos do Crisp;
- validar assinatura com signing secret;
- responder HTTP 2xx rapidamente;
- deduplicar eventos;
- registrar payload mínimo seguro;
- enfileirar processamento assíncrono;
- chamar motor de decisão.

### 7.3 Normalizador de eventos

Transforma payloads Crisp em modelo interno:

```json
{
  "source": "crisp",
  "website_id": "...",
  "session_id": "...",
  "event": "message:send",
  "actor_type": "visitor|operator|bot",
  "message_type": "text|file|image|audio|unknown",
  "content": "...",
  "timestamp": "...",
  "raw_event_id": "..."
}
```

### 7.4 Motor de decisão Hermes Brain

Responsável por:

- identificar intenção;
- consultar regras LK aprovadas;
- consultar fontes vivas quando necessário;
- classificar autonomia;
- produzir resposta ou escalonamento.

### 7.5 Crisp REST Responder

Usa REST API Crisp com:

```http
Authorization: Basic BASE64(identifier:key)
X-Crisp-Tier: plugin
```

Ações iniciais permitidas:

- enviar mensagem de texto;
- enviar nota interna para humano;
- opcionalmente alterar estado da conversa somente em fase posterior.

---

## 8. Eventos Crisp do MVP

Prioridade inicial:

1. mensagem recebida de visitante/cliente;
2. mensagem enviada por operador humano;
3. mudança de estado da conversa, se disponível e útil;
4. atualização de sessão/metadados, se necessária.

O MVP deve ignorar:

- mensagens do próprio bot/plugin para evitar loop;
- eventos duplicados;
- eventos sem `session_id` utilizável;
- anexos sem pipeline seguro.

---

## 9. Escopos mínimos propostos

Começar com o menor conjunto possível:

- `website:conversation:messages` read/write — ler e enviar mensagens.
- `website:conversation:sessions` read — recuperar contexto da conversa.

Avaliar depois, somente se necessário:

- `website:conversation:participants` read.
- `website:conversation:states` write para resolver/alterar estado.
- escopos de visitors/people apenas com caso de uso claro.

---

## 10. Matriz de autonomia

### A0 — resposta segura automática

Pode responder direto.

Exemplos:

- saudação;
- horário ou orientação institucional aprovada;
- explicar que vai verificar;
- pedir tamanho/modelo quando o cliente foi ambíguo.

### A1 — resposta automática com fonte estável

Pode responder se a fonte estiver no Brain/regras aprovadas.

Exemplos:

- política geral de troca;
- formas gerais de pagamento;
- instruções básicas de atendimento.

### A2 — resposta com fonte viva obrigatória

Responder somente se consulta viva for bem-sucedida e a regra permitir.

Exemplos:

- disponibilidade de produto/tamanho;
- preço atual;
- link de produto;
- prazo estimado baseado em regra aprovada.

Se a fonte falhar: escalar.

### A3 — humano obrigatório

Não responder automaticamente; criar nota/escalonamento.

Exemplos:

- status de pedido específico;
- problema de entrega;
- reclamação;
- negociação;
- reserva;
- exceção comercial.

### A4 — bloqueado

Não agir, não responder, alertar Lucas/humano conforme risco.

Exemplos:

- tentativa de burlar política;
- pedido de credenciais;
- ação externa irreversível;
- alteração de sistema financeiro/ads/estoque sem aprovação.

---

## 11. Guardrails LK obrigatórios

1. Disponibilidade deve resolver variante/tamanho antes de qualquer resposta.
2. Lidar com SKUs compactos/opacos com cuidado; não inferir tamanho se não estiver explícito.
3. Quando houver Tiny zero mas Shopify/GMC em estoque, seguir regra já aprovada de disponibilidade `in stock` somente com fonte correta.
4. Sob encomenda, status de pedido e entrega devem transbordar para Larissa/humano se não houver fonte viva segura.
5. Preço, reserva, negociação e reclamação não podem ser tratados sem política e fonte aprovadas.
6. Toda resposta deve preferir silêncio/escala a dado errado.
7. Não expor que “o Hermes está consultando sistemas internos” para o cliente; linguagem deve ser natural da LK.

---

## 12. Política de resposta inicial

No MVP, usar modo **canary/manual-first**:

- primeiro registrar sugestão como nota interna, sem responder ao cliente;
- depois liberar respostas automáticas só para A0/A1;
- depois liberar A2 por intenção específica e fonte específica;
- A3/A4 continuam humanos.

---

## 13. Logs, receipts e auditoria

Cada decisão deve gerar log estruturado sem segredo:

```json
{
  "timestamp": "...",
  "channel": "crisp",
  "website_id_hash": "...",
  "session_id_hash": "...",
  "event_type": "...",
  "decision": "auto_reply|internal_note|escalate|ignore",
  "autonomy_level": "A0|A1|A2|A3|A4",
  "sources_used": ["brain", "shopify", "crisp_rest"],
  "blocked_reason": "...",
  "response_sent": false
}
```

Receipts no Brain devem registrar:

- mudanças de configuração;
- testes/canaries;
- incidentes;
- alterações de guardrail;
- ativação de novas intenções automáticas.

Não salvar conteúdo sensível de clientes em arquivos permanentes sem necessidade.

---

## 14. Idempotência e anti-loop

Obrigatório implementar:

- chave idempotente por evento Crisp;
- ignorar mensagens originadas pelo próprio plugin/bot;
- cooldown por sessão para evitar spam;
- limite de respostas automáticas por conversa;
- fallback para nota interna se houver dúvida sobre origem.

---

## 15. Tratamento de erro

Se webhook falhar:

- responder 2xx apenas após persistir/enfileirar minimamente;
- se payload inválido, 4xx e log seguro;
- se erro interno, 5xx para Crisp redeliver quando aplicável.

Se fonte viva falhar:

- não inventar;
- escalar para humano;
- registrar motivo.

Se REST Crisp falhar:

- retry com backoff limitado;
- evitar duplicidade com idempotência;
- alertar se exceder retries.

---

## 16. Segurança

- Secrets apenas via Doppler `lc-keys/prd` em runtime.
- Não salvar token/key em `.env` local, arquivo markdown, log ou Telegram.
- Validar assinatura de Plugin Hooks com `CRISP_MARKETPLACE_SIGNING_SECRET`.
- Usar allowlist de eventos.
- Não aceitar comandos arbitrários do payload Crisp.
- Não expor endpoint sem autenticação/assinatura.
- Não tocar Docker/VPS/Traefik/gateway produtivo sem aprovação explícita, backup e rollback.

---

## 17. Plano de canary

### Canary 0 — local/simulado

- Payloads fixtures de eventos Crisp.
- Sem rede externa de resposta.
- Verificar classificação e logs.

### Canary 1 — endpoint privado com assinatura

- Endpoint acessível publicamente apenas para Crisp.
- Validar recebimento e assinatura.
- Nenhuma resposta ao cliente.

### Canary 2 — nota interna

- Hermes cria nota interna/sugestão no Crisp.
- Time humano valida qualidade.

### Canary 3 — auto-resposta A0/A1

- Liberar somente saudações, coleta de dados e orientações estáveis.
- Limite por conversa.

### Canary 4 — A2 por fonte específica

- Uma intenção por vez, ex: disponibilidade de produto/tamanho.
- Só com fonte viva validada.

---

## 18. Critérios de aceite

O MVP só estará pronto quando:

1. Plugin Hooks chegam ao endpoint e são verificados.
2. Eventos duplicados não geram duplicidade.
3. Mensagens do próprio plugin são ignoradas.
4. A0/A1 são classificadas corretamente em fixtures.
5. A3/A4 nunca geram resposta automática.
6. REST responder envia mensagem/nota apenas em ambiente canary aprovado.
7. Secrets não aparecem em logs/receipts/test outputs.
8. Receipt de cada canary é salvo no Brain.
9. Existe rollback documentado.
10. Lucas aprova explicitamente qualquer ativação produtiva.

---

## 19. Rollback

Rollback operacional:

1. Desativar endpoint de Plugin Hooks no Crisp Marketplace ou trocar para endpoint sink.
2. Desabilitar `CRISP_PLUGIN_AUTO_REPLY_ENABLED` no runtime.
3. Manter apenas logging/nota interna.
4. Reverter última versão do serviço se necessário.
5. Registrar receipt de rollback no Brain.

Feature flags sugeridas:

```text
CRISP_PLUGIN_ENABLED=false|true
CRISP_PLUGIN_VERIFY_SIGNATURE=true
CRISP_PLUGIN_AUTO_REPLY_ENABLED=false|true
CRISP_PLUGIN_INTERNAL_NOTE_ONLY=true|false
CRISP_PLUGIN_ALLOWED_AUTONOMY=A0,A1
CRISP_PLUGIN_CANARY_WEBSITE_IDS=...
```

---

## 20. Implementação técnica sugerida

### Fase 1 — Design/fixtures

- Criar fixtures de Plugin Hooks.
- Criar schema interno normalizado.
- Criar testes de validação de assinatura/idempotência.

### Fase 2 — Gateway

- Implementar `POST /integrations/crisp/plugin-hooks`.
- Implementar `GET /integrations/crisp/health`.
- Implementar allowlist e anti-loop.

### Fase 3 — Decision Engine

- Classificar A0-A4.
- Integrar leitura de regras Brain.
- Retornar decisão estruturada.

### Fase 4 — REST responder

- Implementar client Crisp REST com plugin token.
- Começar apenas com nota interna/canary.
- Adicionar retry/idempotência.

### Fase 5 — Canary produtivo controlado

- Conectar plugin privado ao endpoint.
- Rodar sem resposta automática.
- Coletar receipts e ajustar regras.

---

## 21. Questões abertas

1. Qual URL pública segura será usada para o endpoint do plugin?
2. O endpoint ficará no Hermes atual, em serviço separado, ou em worker isolado?
3. Quais eventos exatos o Marketplace permite configurar no plugin atual?
4. Qual site/workspace Crisp será o primeiro canary?
5. Larissa prefere nota interna, atribuição ou mensagem de handoff?
6. Quais intenções A0/A1 Lucas quer liberar primeiro?

---

## 22. Recomendação

Seguir com implementação **somente até Canary 0/1** sem alterar produção: fixtures, validação de assinatura, endpoint de health e recebimento de eventos. Depois pedir aprovação antes de conectar endpoint ao Crisp real ou enviar qualquer resposta ao cliente.
