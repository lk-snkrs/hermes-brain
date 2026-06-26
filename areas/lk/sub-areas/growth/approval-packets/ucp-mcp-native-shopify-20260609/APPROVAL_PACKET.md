# Approval Packet — UCP/MCP Shopify Native

Data: 2026-06-09T18:27:47.568317+00:00
Escopo: decisão sobre corrigir UCP/MCP nativo Shopify vs manter rebaixado/desativado publicamente.

## Diagnóstico read-only

- `/.well-known/ucp`: 200, gerado por camada nativa/Shopify/app, não por theme Liquid.
- `/.well-known/ucp/2026-04-08`: 200, mesmo perfil nativo.
- Endpoint anunciado: `https://lk-sneakerss.myshopify.com/api/ucp/mcp`.
- `POST /api/ucp/mcp` com `tools/list`: 422.
- `POST /api/ucp/mcp` com handshake `initialize`: 422.
- Domínio custom e myshopify retornam o mesmo erro.
- Headers/parâmetros comuns de profile URI testados não resolveram.
- Erro: `UCP discovery failed / invalid_profile_url / Missing profile uri`.

## Interpretação

A correção não está em theme Shopify. A rota é nativa/app/proxy Shopify e envolve agentic commerce/profile negotiation. Corrigir na origem pode impactar catálogo, carrinho, checkout ou permissões de agentes; portanto não deve ser feito como patch rápido de Growth sem acesso/fluxo nativo claro.

## Mitigação já aplicada

- `agents.md` não promete mais MCP/UCP funcional.
- `llms-full.txt` marca MCP/UCP como experimental.
- `robots.txt` e `llms.txt` não promovem sitemap agentic fraco.
- O endpoint quebrado fica despromovido, não usado como fonte prioritária.

## Recomendação

Opção recomendada agora: **manter despromovido/rebaixado** e abrir correção nativa Shopify/UCP como projeto separado.

Não recomendo tentar ativar checkout agentic direto agora, porque:

- não há evidência de configuração segura acessível via theme/Admin API comum;
- pode mexer em pagamento/checkout;
- UCP exige profile de agente, trust tier e negociação de capacidades;
- para LK, o valor imediato de SEO/GEO já está capturado sem depender de MCP checkout.

## Próximo passo se Lucas quiser corrigir nativamente

1. Entrar no Shopify Admin/Dev Dashboard ligado à loja.
2. Identificar app/camada que gera `/.well-known/ucp` e `/api/ucp/mcp`.
3. Verificar configuração de agent profile / profile URI / UCP agent trust.
4. Validar `tools/list` com CLI oficial ou agente com profile válido.
5. Só depois re-promover UCP em `agents.md` e `llms-full.txt`.

## Aprovação necessária

Qualquer mudança nativa UCP/MCP/Shopify app/checkout precisa de aprovação explícita e idealmente acesso ao dashboard nativo correspondente.
