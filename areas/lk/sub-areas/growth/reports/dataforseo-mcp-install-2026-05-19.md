# DataForSEO MCP Install — LK Growth

Data: 2026-05-19
Área: LK / Growth / SEO-CRO-GEO
Modo: configuração técnica read-only; sem consultas pagas de SERP/keyword/backlink

## Resumo executivo

- Package instalado localmente no perfil LK Growth: `dataforseo-mcp-server@2.9.2`.
- Wrapper criado para buscar credenciais no Doppler em runtime, sem persistir valores no config.
- `config.yaml` atualizado com `mcp_servers.dataforseo`.
- Teste MCP stdio executado via client temporário: OK.
- Tools descobertas: 79.
- Próximo passo operacional: reiniciar/recarregar o agente Hermes para expor as tools no toolset ativo desta conversa.

## Arquivos/configuração

- Diretório do server: `/opt/data/profiles/lk-growth/mcp-servers/dataforseo/`
- Wrapper: `/opt/data/profiles/lk-growth/mcp-servers/dataforseo/run-dataforseo-mcp.sh`
- Config Hermes: `/opt/data/profiles/lk-growth/config.yaml`
- Secrets usados no Doppler `lc-keys/prd`:
  - `DATAFORSEO_LOGIN`
  - `DATAFORSEO_PASSWORD`

## Validação executada

1. Instalação NPM local:
   - pacote: `dataforseo-mcp-server`
   - versão: `2.9.2`

2. Teste do wrapper:
   - comando iniciou server stdio;
   - DataForSEO client initialized;
   - nenhum segredo impresso.

3. Teste MCP client/list tools:
   - conexão MCP: OK;
   - total de tools: 79;
   - tools-chave disponíveis:
     - `serp_organic_live_advanced`
     - `kw_data_google_ads_search_volume`
     - `dataforseo_labs_google_keyword_ideas`
     - `dataforseo_labs_bulk_keyword_difficulty`
     - `dataforseo_labs_search_intent`
     - `backlinks_summary`
     - `on_page_instant_pages`
     - `on_page_lighthouse`
     - `ai_optimization_chat_gpt_scraper`
     - `ai_opt_llm_ment_search`

## Guardrails

- Não foram feitas consultas pagas relevantes; apenas account/auth previamente e listagem MCP de tools.
- DataForSEO deve seguir orçamento/guardrail de custo antes de chamadas live.
- Evitar operações em lote sem aprovação explícita.
- Secrets ficam no Doppler; config usa wrapper sem valores sensíveis.

## Status

`MCP SERVER INSTALADO E VALIDADO / EXPOSIÇÃO NO AGENTE ATIVO DEPENDE DE RELOAD OU RESTART`
