# F2-002 — Inventário MCP/DataForSEO e candidatos de integração

Gerado em: 2026-05-30T22:29:07+00:00  
Status: **concluído / read-only**  
Escopo: inventário local de MCPs configurados e análise de candidatos para as integrações usadas por Lucas/LK/Zipper/SPITI/Hermes.  
Guardrail: não alterou configs, não instalou MCP novo, não reiniciou profiles, não imprimiu secrets e não executou writes externos.

## Resumo executivo

Hoje o único MCP realmente configurado no Hermes é **DataForSEO**, e apenas nos profiles:

- `lk-shopify`
- `lk-trends`

O server físico fica em:

- `/opt/data/profiles/lk-growth/mcp-servers/dataforseo/`

Mas o profile `lk-growth` em si **não tem `mcp_servers` configurado** no `config.yaml` inspecionado. Isso é uma inconsistência útil: o MCP foi preparado dentro da área LK Growth, mas só está exposto para LK Shopify e LK Trends.

Recomendação: o próximo MCP que mais faz sentido estudar é **Supabase MCP em modo read-only**, porque atende Zipper e SPITI diretamente, onde temos CRM, vendas, obras, conversas, leilões e dados operacionais. Em segundo lugar vem **n8n MCP read-only** para observabilidade de workflows. Shopify MCP pode ser útil, mas é mais perigoso porque muitos servers expõem mutations; deve entrar só com whitelist/list/get e approval separado.

## Evidência local — MCP configurado por profile

Inspeção read-only dos `config.yaml` locais:

- `default`: sem `mcp_servers`
- `brain-process`: sem `mcp_servers`
- `hermes-ops-readonly`: sem `mcp_servers`
- `lc-claude-cli`: sem `mcp_servers`
- `lk-analyst-readonly`: sem `mcp_servers`
- `lk-content-reviewer`: sem `mcp_servers`
- `lk-growth`: sem `mcp_servers`
- `lk-ops`: sem `mcp_servers`
- `lk-shopify`: `dataforseo`
- `lk-trends`: `dataforseo`
- `mordomo`: sem `mcp_servers`
- `spiti`: sem `mcp_servers`

Config observada para `dataforseo` nos profiles onde existe:

- command: `/opt/data/profiles/lk-growth/mcp-servers/dataforseo/run-dataforseo-mcp.sh`
- args: `[]`
- timeout: `180`
- connect_timeout: `60`
- sampling: `enabled: false`

Ponto positivo: `sampling` está desligado.

## Runtime live observado

Profiles live observados por processo:

- PID 1: `/opt/data`
- PID 27: `/opt/data/profiles/mordomo`
- PID 47: `/opt/data/profiles/lk-growth`
- PID 52: `/opt/data/profiles/spiti`
- PID 62: `/opt/data/profiles/lk-ops`
- PID 66: `/opt/data/profiles/lk-shopify`
- PID 71: `/opt/data/profiles/lk-trends`

Conclusão: `lk-shopify` e `lk-trends` estão live e têm MCP DataForSEO configurado; `lk-growth` está live, contém o diretório do server, mas não expõe o server via `mcp_servers` na config lida.

## DataForSEO MCP — status

Arquivos verificados:

- `package.json`: `dataforseo-mcp-server` versão `2.9.2`
- wrapper: `run-dataforseo-mcp.sh`

Características do wrapper:

- busca credenciais via Doppler no start do processo;
- não persiste valores em arquivo novo;
- exporta `DATAFORSEO_FULL_RESPONSE=false`;
- exporta `DATAFORSEO_SIMPLE_FILTER=true`;
- habilita módulos: `AI_OPTIMIZATION`, `SERP`, `KEYWORDS_DATA`, `ONPAGE`, `DATAFORSEO_LABS`, `BACKLINKS`, `BUSINESS_DATA`, `DOMAIN_ANALYTICS`, `CONTENT_ANALYSIS`.

Teste read-only de descoberta via `mcporter`:

- `mcporter` disponível: `0.11.3`
- Node disponível: `v20.19.2`
- npm disponível: `9.2.0`
- tools DataForSEO descobertas: `79`

Categorias úteis descobertas:

- AI Optimization / LLM mentions
- SERP orgânico
- YouTube SERP/subtitles/comments/info
- Google Ads keyword/search volume
- Google Trends
- DataForSEO Labs: ranked keywords, competitors, keyword ideas, keyword overview, search intent
- OnPage: instant pages, content parsing, lighthouse
- Backlinks: summary, anchors, referring domains, competitors, new/lost
- Domain analytics / technologies / WHOIS
- Content analysis
- Business listings

## Valor do DataForSEO para LK

Bom piloto para:

- LK SEO/GEO: SERP, keywords, concorrentes, intenção de busca, páginas ranqueadas.
- LK Trends: trend radar e validação de demanda.
- LK Shopify: auditoria de páginas, OnPage, Lighthouse, conteúdo e comparação com concorrentes.
- AI citation readiness: LLM mentions e AI Optimization.

Riscos:

- pode consumir créditos/custo por chamadas;
- responses podem ser grandes;
- módulos de SERP/OnPage/Backlinks devem ser chamados com escopo pequeno;
- não deve virar fonte única para decisão comercial sem cruzar com Shopify/Tiny/GMC/analytics.

Whitelist inicial recomendada para piloto:

- `dataforseo_labs_google_keyword_overview`
- `dataforseo_labs_google_ranked_keywords`
- `dataforseo_labs_google_serp_competitors`
- `dataforseo_labs_search_intent`
- `serp_organic_live_advanced`
- `on_page_instant_pages`
- `on_page_lighthouse`
- `ai_opt_llm_ment_agg_metrics`
- `ai_opt_llm_ment_top_domains`
- `ai_opt_llm_ment_top_pages`

Bloquear inicialmente:

- chamadas em lote amplas;
- backlink bulk sem limite;
- qualquer scan grande de domínio inteiro;
- `ai_optimization_llm_response` com web_search sem objetivo claro, por custo/ruído.

## Candidatos MCP por integração usada

### 1. Supabase MCP — prioridade alta

Disponibilidade encontrada:

- pacote: `@supabase/mcp-server-supabase`
- versão observada via npm: `0.8.1`
- descrição: MCP server for interacting with Supabase

Onde ajudaria:

- Zipper: `vendas_tango`, CRM/Main, contacts, conversations, followups, contents, artists, exhibitions.
- SPITI: Hub/Supabase, leilões, obras, clientes, CRM e análises internas.
- LK: se houver Supabase operacional/analytics, leitura consolidada.

Por que vale:

- hoje temos muitos scripts/read-only customizados; MCP poderia padronizar schema discovery e queries pequenas.
- o valor é alto para “perguntar ao banco” sem reescrever script a cada consulta.

Risco:

- banco é fonte sensível e pode ter mutations;
- exige token/connection segura;
- pode misturar empresas se o profile errado tiver acesso amplo.

Recomendação:

- fazer primeiro em profile read-only dedicado, por empresa ou por projeto;
- credenciais em Doppler;
- role read-only quando possível;
- whitelist só de list/get/query/select/schema;
- sem sampling;
- sem mutation tools.

Status sugerido: **F2-006/F2-007 candidato principal**.

### 2. n8n MCP — prioridade alta/média para observabilidade

Disponibilidade encontrada:

- pacote: `n8n-mcp`
- versão observada via npm: `2.56.0`
- descrição: Integration between n8n workflow automation and Model Context Protocol

Onde ajudaria:

- inventariar workflows;
- checar status de automações;
- diagnosticar falhas de rotina;
- evitar “workflow fantasma” sem saber onde está.

Risco:

- n8n costuma ter actions/mutations e credentials internas;
- pausar/rodar workflow é A3/A4 dependendo do impacto.

Recomendação:

- começar como read-only: list workflows, get workflow, executions/status;
- bloquear run/activate/deactivate/update/delete;
- só em profile de ops/read-only.

Status sugerido: **bom segundo piloto, depois de Supabase ou junto com política MCP**.

### 3. Shopify MCP — prioridade média, risco alto

Disponibilidade encontrada via npm search:

- `@aiwerk/mcp-server-shopify` — Shopify Admin GraphQL API MCP server
- `shopify-mcp`
- outros proxies/commercial MCPs

Onde ajudaria:

- LK Shopify: leitura de produtos, pedidos, customers, inventory, collections, theme/catalog QA.
- LK Growth: SEO/CRO/GMC packets com leitura direta.

Por que não é primeiro:

- Shopify é superfície de produção;
- muitos MCPs expõem mutations de produto/order/customer/inventory;
- já temos scripts e skills específicas com approval/rollback.

Recomendação:

- só considerar MCP read-only/list/get/search;
- não usar para inventory sync: Tiny continua fonte de verdade;
- nenhum product/update/theme/write sem approval packet.

Status sugerido: **candidato controlado, não piloto inicial**.

### 4. Google Workspace MCP — prioridade média/baixa

Disponibilidade encontrada:

- `google-workspace-mcp`
- `@a-bonus/google-docs-mcp`
- `@aaronsb/google-workspace-mcp`
- `@mindstone/mcp-server-google-workspace`
- outros

Onde ajudaria:

- Gmail/Calendar/Drive/Docs/Sheets para Mordomo, Zipper relatórios, agenda e documentos.

Por que não é prioritário:

- já existe skill/CLI `google-workspace` no Hermes;
- Gmail/Calendar têm risco alto de external action e privacidade;
- OAuth e escopos precisam ser muito bem separados.

Recomendação:

- manter via skill/CLI atual por enquanto;
- se virar MCP, começar em Drive/Docs/Sheets read-only; Gmail/Calendar writes continuam bloqueados/escopados.

Status sugerido: **esperar; não instalar agora**.

### 5. Notion/Airtable MCP — prioridade depende de uso atual

Disponibilidade encontrada:

- Notion oficial: `@notionhq/notion-mcp-server` versão `2.2.1`
- Airtable community: `airtable-mcp-server`, `airtable-user-mcp`, etc.

Onde ajudaria:

- Notion `[LOJA ESTOQUE]` / compras / sourcing se ainda for fonte operacional.
- Airtable se alguma base continuar ativa.

Risco:

- fonte pode estar secundária/desatualizada;
- MCPs podem permitir writes estruturais/records;
- risco de duplicar verdade com Tiny/Shopify/Brain.

Recomendação:

- só habilitar se confirmar uma base ativa e qual pergunta recorrente resolve;
- read-only primeiro.

Status sugerido: **condicional**.

### 6. GitHub MCP — prioridade baixa

Disponibilidade encontrada:

- pacote oficial: `@modelcontextprotocol/server-github` versão `2025.4.8`

Onde ajudaria:

- issues/PRs/repos em linguagem natural.

Por que não é prioritário:

- já usamos `gh` CLI + skills de GitHub;
- MCP adiciona outra superfície com token de repo.

Recomendação:

- manter `gh` CLI para agora;
- considerar MCP só se for integrado ao cockpit/kanban com read-only first.

Status sugerido: **não prioritário**.

### 7. Playwright MCP — prioridade média para QA visual/local

Disponibilidade encontrada:

- pacote: `@playwright/mcp` versão `0.0.75`

Onde ajudaria:

- QA de Mission Control, Shopify theme/dev, páginas LK, Hub/SPITI, previews;
- captura de evidência visual e fluxos browser.

Risco:

- browser pode clicar/fazer login/alterar estado;
- precisa de allowlist de URLs e modo preview/read-only.

Recomendação:

- avaliar como ferramenta local de QA, não como integração de negócio;
- bloquear ações em produção/autenticadas sem approval.

Status sugerido: **bom candidato técnico, não depende de segredo**.

### 8. Klaviyo / Meta Ads / Google Ads / GA4 — prioridade baixa/média, com cautela

Disponibilidade encontrada:

- Klaviyo MCPs community: `klaviyo-mcp`, `@pipeworx/mcp-klaviyo`, `dtc-mcp`.
- Meta Ads MCPs community: `@cesteral/meta-mcp`, `meta-ads-mcp`, outros.
- Google Ads MCP: `@channel47/google-ads-mcp`.
- Google Analytics MCPs community: `@toolsdk.ai/google-analytics-mcp`, `mcp-google-analytics`, etc.

Onde ajudaria:

- LK Growth performance e auditorias.

Por que não é prioridade agora:

- campanhas/audiências/envios são alto risco;
- ownership externo: Pareto/FHITS em partes do processo;
- já há skills/APIs para SEO/Google/Metricool e relatórios.

Recomendação:

- GA4 read-only pode ser útil, mas Google APIs atuais talvez bastem;
- Meta/Klaviyo só read-only analytics, nunca sends/campaign changes sem approval;
- Google Merchant Center: não foi encontrado MCP claro/maduro; manter scripts/API/skills atuais.

Status sugerido: **não piloto MCP inicial**.

### 9. Tiny ERP / WhatsApp / Crisp / Metricool / Vercel / Stripe

Tiny ERP:

- não foi encontrado MCP claro/maduro via npm search;
- Tiny é fonte de estoque e exige wrappers próprios com governança rígida;
- manter scripts/API atuais e regra “Tiny verdade, Shopify gatilho/superfície”.

WhatsApp:

- usar `wacli`/skills atuais;
- MCP aumentaria risco de contato externo acidental.

Crisp:

- não foi encontrado MCP relevante/maduro; existe SDK/API oficial;
- para atendimento, melhor plugin/skill custom com guardrails do que MCP genérico.

Metricool:

- não foi encontrado MCP específico relevante;
- manter `metricool-api-analytics` skill/API.

Vercel:

- não apareceu MCP oficial claro; há adapters/frameworks genéricos;
- manter Vercel CLI/skill e PR workflow.

Stripe:

- pacote oficial `@stripe/mcp` existe, versão `0.3.3`;
- não parece central para as operações atuais descritas;
- pagamentos/financeiro são sensíveis; não priorizar.

## Matriz de recomendação

- **Ativar/experimentar primeiro:** DataForSEO, já existente, com whitelist pequena e limites de custo.
- **Próximo melhor candidato:** Supabase MCP read-only por projeto/empresa.
- **Bom candidato operacional:** n8n MCP read-only para inventário/status de workflows.
- **Bom candidato técnico:** Playwright MCP para QA visual/local/previews.
- **Candidato controlado, não inicial:** Shopify MCP read-only; alto risco de mutation.
- **Esperar:** Google Workspace MCP, GitHub MCP, Notion/Airtable MCP.
- **Evitar por enquanto:** Meta Ads/Klaviyo/Google Ads MCPs com actions; Tiny/WhatsApp/Crisp MCP genéricos; qualquer MCP que não permita separar read-only de write.

## Próxima ação recomendada

1. Usar DataForSEO como piloto MCP real pequeno, mas apenas em uma consulta LK SEO/GEO controlada:
   - 1 domínio ou 1 keyword;
   - 1 a 3 tools whitelist;
   - output local/Telegram curto;
   - registrar custo/latência/qualidade.
2. Abrir F2-006 com política MCP de negócio:
   - classes: read-only local, read-only external, paid API, database, external-write;
   - regras de Doppler, sampling off, whitelist e approval packet.
3. Preparar approval packet separado para Supabase MCP read-only, especificando:
   - projeto/empresa;
   - role/token read-only;
   - tools permitidas;
   - queries de teste;
   - rollback: remover server do config e não reiniciar/ativar sem validação.

## Não feito

- Nenhum MCP novo instalado.
- Nenhum `config.yaml` editado.
- Nenhum profile reiniciado.
- Nenhum secret impresso.
- Nenhuma consulta produtiva de negócio executada via MCP, exceto descoberta de schema/tools do DataForSEO já configurado.
