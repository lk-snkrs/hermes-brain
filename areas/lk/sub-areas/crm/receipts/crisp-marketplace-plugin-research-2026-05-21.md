# Research — Crisp Marketplace plugin para Hermes/Hugo grande cérebro — 2026-05-21

## Pergunta

Lucas pediu pesquisa sobre como fazer a interação via plugin Crisp Marketplace, conforme orientação do Bruno, para construir o grande cérebro de resposta do Crisp Chat.

## Fontes consultadas

- Crisp REST API Authentication: `https://docs.crisp.chat/guides/rest-api/authentication/`
- Plugin Token: `https://docs.crisp.chat/guides/rest-api/authentication/plugin-token/`
- Plugins Quickstart: `https://docs.crisp.chat/guides/plugins/quickstart/`
- Plugin Hooks: `https://docs.crisp.chat/guides/web-hooks/plugin-hooks/`
- Web Hooks Reference: `https://docs.crisp.chat/references/web-hooks/v1/`
- Hugo MCP API Quickstart: `https://docs.crisp.chat/guides/hugo/mcp-api/quickstart/`
- Hugo MCP Request Signing: `https://docs.crisp.chat/guides/hugo/mcp-api/request-signing/`
- Hugo MCP Server Examples: `https://docs.crisp.chat/guides/hugo/mcp-api/server-examples/`
- Hugo Workflow API: `https://docs.crisp.chat/guides/hugo/workflow-api/`

## Achados principais

1. Crisp plugins rodam em servidor próprio do integrador e usam REST API e/ou RTM API.
2. Plugin Hooks recebem eventos em tempo real via HTTP POST para endpoint HTTPS público configurado no Marketplace.
3. Para responder mensagens, o plugin usa REST API `Send A Message In Conversation` autenticado com Plugin Token.
4. Plugin Token é keypair `identifier:key` gerado no Marketplace e enviado como `Authorization: Basic BASE64(identifier:key)` + `X-Crisp-Tier: plugin`.
5. Hugo pode chamar sistemas externos via MCP: cadastrar um MCP server público em `AI Agent > Integrations & MCP`.
6. Hugo MCP requests são assinados com HMAC-SHA256 usando headers `X-Crisp-Website-Id`, `X-Crisp-Timestamp`, `X-Crisp-Signature` e, quando houver conversa, `X-Crisp-Session-Id`.
7. Workflow API aciona Hugo/Workflows por `Authorization: Bearer YOUR_TOKEN`, separado das credenciais Marketplace.

## Arquitetura recomendada

- Crisp Marketplace Plugin: canal oficial, autenticação, escopos e eventos.
- Hermes Crisp Webhook: recebe Plugin Hooks, valida assinatura, normaliza evento e enfileira para decisão.
- Hermes Brain/RAG: busca contexto LK/Crisp/CRM/pedidos/regras aprovadas sem expor segredo.
- Hugo MCP Server: ferramenta que Hugo usa para consultar Hermes/Brain quando precisar de contexto ou ação.
- REST responder: envia resposta ao Crisp somente quando a política permite; casos bloqueados escalam para humano/Larissa.
- Workflow API: opcional para acionar um workflow específico ou agente Hugo com instrução contextual.

## Escopos prováveis

- `website:conversation:messages` read/write — ler/enviar mensagens.
- `website:conversation:sessions` read — contexto/metas da conversa.
- `website:conversation:participants` read/write se for necessário registrar participantes.
- `website:conversation:states` write se Hermes puder resolver/alterar estado; manter bloqueado no início.
- `website:visitors`/people scopes somente se realmente necessários.

## Guardrails

- Começar privado/dev, sem publicação pública e sem resposta automática irrestrita.
- Validar assinatura dos webhooks/MCP.
- Não enviar preço/disponibilidade/reserva/status pedido/reclamação sem fonte viva e regra aprovada.
- Não tocar Docker/VPS/gateway sem plano/rollback e aprovação.
- Não imprimir secrets; usar Doppler `lc-keys/prd`.

## Próximo passo seguro

Criar PRD técnico do plugin Hermes no Crisp com endpoints, fluxo de decisão, escopos mínimos, filas, logs, rollback e modo canary/manual antes de qualquer produção.
