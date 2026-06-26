# LK Crisp/Hugo — Cérebro de Respostas com aprendizado Larissa

Data: 2026-05-21
Status: desenho aprovado conceitualmente pelo Lucas; implementação produtiva exige credenciais Crisp/Hugo e aprovação de exposição MCP/infra.

## Objetivo

Criar um agente de atendimento LK no Crisp/Hugo onde toda resposta automática passe por um cérebro central de resposta, usando o MCP do Hugo/Crisp, e que aprenda diariamente com as respostas reais da Larissa.

## Fontes oficiais consultadas

- Crisp Hugo MCP API: `https://docs.crisp.chat/guides/hugo/mcp-api/`
- Crisp Hugo MCP Server: `https://docs.crisp.chat/guides/hugo/mcp-server/`
- Crisp Hugo Workflow API: `https://docs.crisp.chat/guides/hugo/workflow-api/`

## Princípios não negociáveis

1. O bot nunca responde sobre:
   - produto sob encomenda;
   - status de pedido;
   - entrega/rastreamento/prazo pós-compra.
2. Qualquer uma dessas intenções transborda para Larissa/humano.
3. Respostas automáticas devem ser curtas, reais, com tom humano de atendente LK, e baseadas no cérebro documentado.
4. Estoque/produto só pode usar fontes verificáveis e deve preservar tamanho quando houver tamanho na pergunta.
5. Aprendizado diário nunca publica regra automaticamente sem rastreabilidade: cada lesson deve conter exemplo, categoria, confiança e fonte Larissa.
6. Sem segredos em logs, Brain ou respostas.

## Arquitetura proposta

```text
Cliente no Crisp
  ↓
Hugo AI Agent / Workflow
  ↓ sempre chama
MCP Server LK Response Brain
  ↓
Classificador de intenção + guardrails
  ├─ bloqueado: sob encomenda/status pedido/entrega → transbordo Larissa
  ├─ permitido com fonte: gera draft/resposta curta
  └─ incerto: transbordo Larissa
  ↓
Crisp/Hugo responde ou cria handoff
```

## Como usar cada API do Hugo/Crisp

### 1. Hugo MCP API — nosso servidor para Hugo consultar

Criar um MCP server público/HTTPS com assinatura verificada. Hugo vai chamar esse servidor quando precisar de ferramentas internas LK.

Ferramentas iniciais propostas:

- `lk_classify_intent`
  - Entrada: mensagem do cliente, `X-Crisp-Session-Id`, contexto resumido.
  - Saída: `allowed | handoff_required`, motivo, categoria.
  - Bloqueia obrigatoriamente sob encomenda, status de pedido e entrega.

- `lk_draft_reply`
  - Entrada: mensagem + categoria + contexto aprovado.
  - Saída: resposta curta em PT-BR, com fonte usada e nível de confiança.
  - Só funciona se `lk_classify_intent.allowed=true`.

- `lk_handoff_to_larissa`
  - Entrada: motivo e resumo para humano.
  - Saída: instrução de transbordo; sem inventar resposta ao cliente.

- `lk_search_response_brain`
  - Consulta Brain/knowledge base de respostas aprovadas, tom Larissa, políticas e exemplos.

- `lk_stock_lookup_public_safe` (opcional, fase 2)
  - Consulta catálogo/estoque read-only, preservando tamanho; não toca sob encomenda.

Segurança MCP:

- Usar Bearer token + Request Signing do Crisp.
- Verificar `X-Crisp-Signature` com HMAC-SHA256 no payload `{timestamp}.{website_id}.{raw_request_body}`.
- Rejeitar requisições com timestamp acima de 300s.
- Registrar `X-Crisp-Session-Id` como correlação, não como segredo.

### 2. Hugo MCP Server — Hugo como fonte consultável por agentes externos

O endpoint `https://app.hugo.ai/api/mcp/` expõe a ferramenta `search` para pesquisar base Hugo (`webpage`, `helpdesk`, `answer`, `document`) com `Authorization: Bearer WEBSITE_TOKEN`.

Uso recomendado no LK Response Brain:

- consultar artigos/respostas oficiais Hugo antes de gerar resposta;
- cruzar com Brain LK e guardrails;
- nunca usar resultado Hugo para responder temas bloqueados; nesses casos, apenas encaminhar à Larissa.

### 3. Workflow API — gatilhos e transbordo

Usar `POST https://app.hugo.ai/api/agent/trigger/` com `session_id` e `instruction` para acionar Hugo com instrução específica.

Usar `POST https://app.hugo.ai/api/scenario/{workflow_id}/trigger/` para rodar fluxo de handoff/transbordo, passando variáveis como:

```json
{
  "session_id": "...",
  "variables": {
    "handoff_reason": "blocked_topic_order_status",
    "summary_for_larissa": "Cliente perguntou sobre entrega/status; bot não pode responder.",
    "source": "lk_response_brain"
  }
}
```

Token nunca deve ir para client-side.

## Regras de transbordo

Transbordar imediatamente para Larissa/humano quando detectar:

- `sob encomenda`, `encomenda`, `consigo encomendar`, `não tem no site mas consegue?`;
- `cadê meu pedido`, `status`, `rastreio`, `entrega`, `prazo`, `transportadora`, `código de rastreio`;
- reclamação, pedido com problema, troca/devolução complexa;
- intenção ambígua com risco financeiro/operacional;
- baixa confiança ou fonte insuficiente.

Texto interno sugerido para o handoff:

```text
Transbordar para Larissa: cliente perguntou sobre {categoria_bloqueada}. O bot não deve responder esse tema. Resumo: {resumo_curto}. Última mensagem: {mensagem_cliente}
```

## Aprendizado diário com Larissa — 21h

Cron diário às 21h deve:

1. Buscar conversas Crisp do dia que tiveram resposta da Larissa.
2. Extrair pares `pergunta do cliente → resposta Larissa`.
3. Remover PII e dados sensíveis.
4. Classificar por categoria:
   - tamanho/numeração;
   - disponibilidade em estoque;
   - pagamento;
   - troca/devolução simples;
   - tom/acolhimento;
   - bloqueados: sob encomenda, status pedido, entrega.
5. Gerar lessons estruturadas:
   - pergunta padrão;
   - resposta aprovada/paráfrase;
   - quando usar;
   - quando não usar;
   - fonte Crisp session ID;
   - data;
   - confiança.
6. Atualizar arquivos do Brain, não memória solta:
   - `knowledge/lk-response-brain/approved-answer-patterns.md`
   - `knowledge/lk-response-brain/larissa-tone.md`
   - `knowledge/lk-response-brain/blocked-topics.md`
   - `knowledge/lk-response-brain/daily-lessons/YYYY-MM-DD.md`
7. Se encontrar regra nova de alto impacto, enviar resumo para Lucas aprovar antes de ativar.

## Prompt/política do agente

```text
Você é o atendimento assistido da LK Sneakers no Crisp. Responda como atendente real, curto, natural e sem jargão interno.
Antes de responder, consulte o LK Response Brain via MCP.
Nunca responda sobre produto sob encomenda, status de pedido ou entrega/rastreamento/prazo pós-compra. Nesses casos, faça handoff para Larissa/humano.
Se faltar fonte, não invente: transborde.
Se responder disponibilidade/estoque com tamanho informado, confirme o tamanho explicitamente.
```

## MVP seguro

Fase 0 — Preparação:
- criar Brain docs e guardrails;
- definir credenciais necessárias no Doppler;
- confirmar Crisp Website ID, Website Token, Hugos workflows IDs e nome/ID da Larissa.

Fase 1 — Read-only:
- MCP server só classifica e gera drafts internos;
- nenhum envio automático ao cliente;
- logs/receipts por sessão.

Fase 2 — Resposta automática limitada:
- responder apenas FAQ baixo risco e estoque com fonte;
- handoff obrigatório para bloqueados;
- rate limit e kill switch.

Fase 3 — Aprendizado 21h:
- cron diário com resumo para Brain;
- ativação de novas regras só com confiança/approval.

## Pendências para implementação

- Credencial Crisp/Hugo em Doppler: website token, signing secret MCP, workflow IDs.
- Decidir endpoint HTTPS: Cloudflare Tunnel/Traefik/subdomínio ou ambiente isolado.
- Confirmar identificador da Larissa no Crisp para filtrar respostas humanas.
- Confirmar se o Hugo deve responder diretamente ou se o MCP apenas gera draft + workflow decide.
