# Decisão — UCP/MCP LK

Data: 2026-06-09T18:37:31.113263+00:00
Decisão Lucas: seguir com a opção segura.

## Decisão operacional

Manter UCP/MCP **despromovido/rebaixado** nos arquivos AI/GEO até validação nativa Shopify/Dev Dashboard.

## Motivo

- `/.well-known/ucp` existe e retorna 200, mas é camada nativa/app/proxy Shopify, não theme Liquid.
- `/api/ucp/mcp` segue retornando 422 em teste MCP `initialize`.
- Erro observado: `UCP discovery failed / Missing profile uri`.
- Corrigir na origem pode envolver agentic commerce, carrinho, checkout, permissões e trust tier de agentes.
- SEO/GEO principal já está forte sem depender de MCP checkout.

## Estado desejado

- `llms.txt`: não promover MCP/UCP.
- `agents.md`: tratar UCP/MCP como experimental/não prioritário.
- `robots.txt`: não promover sitemap agentic fraco.
- Não fazer writes nativos Shopify/UCP sem aprovação e contexto do dashboard.

## Próximo gatilho para retomar

Retomar só se houver acesso/instrução para Shopify Admin/Dev Dashboard ou evidência oficial de como configurar o `profile uri`/agent trust da loja.

## Evidência

Read-only check salvo em:

`areas/lk/sub-areas/growth/decisions/ucp-mcp/latest-readonly-check.json`
