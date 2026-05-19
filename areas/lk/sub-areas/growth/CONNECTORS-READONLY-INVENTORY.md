# LK Growth OS — Inventário de conectores read-only

Última revisão: 2026-05-19.

## Princípios

- Este inventário valida conectores para leitura/análise do LK Growth OS.
- Nenhum teste abaixo autoriza write, mutation, campaign send, tema, produto, preço, estoque, Merchant/GSC/GA4 write ou contato externo.
- Segredos ficam no Doppler `lc-keys/prd`; este documento registra apenas nomes de chaves e status, nunca valores.
- Relatório Growth só é `decision-grade` quando a fonte obrigatória para a decisão estiver OK ou quando o bloqueio estiver explicitamente declarado.

## Resultado da validação 2026-05-19

### Shopify Admin — OK

- Status: `OK`.
- Tipo: read-only.
- Teste feito: Admin GraphQL `query { shop { ... } products(first: 1) { ... } }`.
- Resultado: loja consultada e `products(first:1)` retornou 1 produto.
- Segredos usados sem exposição: `SHOPIFY_STORE_URL`/`SHOPIFY_STORE` e `SHOPIFY_ACCESS_TOKEN`/`SHOPIFY_ADMIN_TOKEN`.
- Uso no Growth: catálogo, handles, SEO fields, collection/PDP context, CRO/Shopify evidence.
- Limite: Shopify stock não é verdade final de estoque; Tiny continua fonte de estoque.

### Google Search Console — OK

- Status: `OK`.
- Tipo: read-only.
- Propriedade validada: `sc-domain:lksneakers.com.br`.
- Teste feito: Search Analytics query com dimensão `query`, janela recente e `rowLimit=1`.
- Resultado: retornou 1 linha.
- Segredos/credenciais sem exposição: `GSC_SITE_URL` + service account JSON via Doppler.
- Uso no Growth: impressões, cliques, CTR, posição, queries/páginas, avaliação pós-mudança SEO.
- Limite: dados GSC costumam ter atraso de 2-3 dias.

### Google Merchant Center — OK

- Status: `OK`.
- Tipo: read-only.
- Teste feito: Content API `products.list?maxResults=1`.
- Resultado: retornou 1 recurso.
- Segredos/credenciais sem exposição: `MERCHANT_CENTER_ID_LK` + service account JSON via Doppler.
- Uso no Growth: status de produtos, títulos/feed/ProductInput context, GMC review semanal.
- Limite: qualquer alteração em Merchant/ProductInput exige approval packet + rollback; não é parte deste inventário.

### GA4 Data API — OK

- Status: `OK`.
- Tipo: read-only.
- Validação/correção atualizada em 2026-05-19:
  - Antes da correção, `GA4_LK_PROPERTY_ID` apontava para uma propriedade que retornava HTTP 403 e não aparecia em `accountSummaries` para nenhuma das service accounts disponíveis.
  - `GOOGLE_ANALYTICS_PROPERTY_ID` retornava `OK` com métricas via GA4 Data API `runReport` e aparecia nas propriedades acessíveis.
  - Lucas confirmou que havia acesso; o segredo canônico `GA4_LK_PROPERTY_ID` foi padronizado no Doppler para a propriedade funcional já acessível, preservando `GOOGLE_ANALYTICS_PROPERTY_ID` como referência compatível.
  - Reteste pós-correção: `GA4_LK_PROPERTY_ID` retornou `OK` com métricas `sessions` e `totalUsers` via `GA4_LK_SERVICE_ACCOUNT`.
- Uso no Growth: sessões, usuários, landing pages, conversão e receita em relatórios SEO/CRO/GEO e impact review.
- Guardrail: esta foi uma correção de secret/config no Doppler; nenhuma alteração foi feita dentro do GA4 UI/Admin. Relatórios devem continuar declarando janela de dados e propriedade usada quando relevante.

### PageSpeed Insights / CrUX — OK via API key dedicada

- Status: `OK` para uso read-only recorrente.
- Validação atualizada em 2026-05-19:
  - Lucas habilitou as APIs no projeto Google Cloud correto `fluid-griffin-323417` / `797436119355`.
  - API key salva no Doppler `lc-keys/prd` como `PAGESPEED_API_KEY` e `GOOGLE_API_KEY` para compatibilidade com scripts Claude SEO que procuram `GOOGLE_API_KEY`.
  - PageSpeed Insights v5 mobile para `https://lksneakers.com/`: `OK`, Lighthouse performance score presente, CrUX embutido no PSI presente.
  - CrUX API origin-level: `OK` para `https://lksneakers.com.br` com métricas INP, LCP, CLS, TTFB e form factors.
  - CrUX retornou 404 para `https://lksneakers.com` e `https://www.lksneakers.com`; tratar como ausência de field data nesses origins, não falha de auth.
- Uso no Growth: Core Web Vitals field data, PSI/Lighthouse lab data, comparação mobile/desktop e impact review técnico.
- Guardrail: chave fica no Doppler; não registrar valor em relatórios. Para Claude SEO nativo, preferir injetar `GOOGLE_API_KEY` a partir do Doppler em tempo de execução, evitando persistir a chave em `~/.config/claude-seo/google-api.json`.
- Evidência detalhada: `reports/pagespeed-crux-readiness-2026-05-19.md`.
- Regra operacional: para field data decision-grade da LK, priorizar o origin com CrUX disponível (`https://lksneakers.com.br`) e declarar fallback/ausência quando a URL testada estiver em origin sem dados CrUX.

### Klaviyo / CRM signals — OK

- Status: `OK` para leitura básica CRM/marketing signals.
- Tipo: read-only.
- Validação atualizada em 2026-05-19:
  - Secret presente no Doppler: `KLAVIYO_API_KEY`.
  - Testes executados sem mutation/send:
    - `GET /api/accounts/`: HTTP 200, retornou 1 conta.
    - `GET /api/lists/`: HTTP 200, retornou 1 lista.
    - `GET /api/metrics/`: HTTP 200, retornou 135 métricas.
- Uso no Growth: sinais de CRM, listas, métricas/eventos e demanda pós-campanha como contexto.
- Guardrail: nenhum campaign send, flow/list/profile mutation ou customer-facing action sem aprovação explícita atual.

### Meta/Paid/Influencer signals — OK

- Status: `OK` para leitura básica de paid/social demand signals.
- Tipo: read-only.
- Validação atualizada em 2026-05-19:
  - Secrets presentes no Doppler: `META_ACCESS_TOKEN`, `META_ADS_ACCOUNT_ID`, `META_APP_ID`, `META_APP_SECRET`.
  - Testes executados sem mutation:
    - `GET /me`: HTTP 200, token válido para leitura básica.
    - `GET /act_<account_id>`: HTTP 200, ad account ativa (`account_status=1`) e moeda BRL.
    - `GET /campaigns?limit=1`: HTTP 200, retornou 1 campanha.
    - `GET /insights?date_preset=last_7d`: HTTP 200, retornou 1 linha de insights.
  - `debug_token` com o app secret disponível falhou por mismatch de app, então a validação confiável é pelas chamadas reais de leitura acima.
- Uso no Growth: paid/social demand signals e triangulação comercial.
- Guardrail: nenhuma campanha, budget, creative, audience, pixel config ou send sem aprovação explícita atual.

### Ahrefs — OK via API token

- Status: `OK` para leitura pontual de backlink/domain metrics.
- Tipo: read-only, API paga/creditada.
- Validação atualizada em 2026-05-19:
  - Secret presente no Doppler: `AHREFS_API_TOKEN`.
  - Teste executado: Ahrefs API v3 `site-explorer/domain-rating` para `lksneakers.com.br` com `date` recente.
  - Resultado: HTTP 200; retornou `domain_rating=36.0` e `ahrefs_rank=2322408`.
- Uso no Growth: autoridade de domínio, backlinks, referring domains, link gap e concorrência off-page.
- Guardrail: usar com parcimônia por custo/créditos; não rodar crawls/backlink exports grandes sem aprovação operacional.

### DataForSEO — MCP INSTALADO / RELOAD PENDENTE

- Status: `MCP SERVER INSTALADO E VALIDADO / EXPOSIÇÃO NO AGENTE ATIVO DEPENDE DE RELOAD OU RESTART`.
- Tipo: API paga/creditada; usar com guardrail de custo.
- Validação atualizada em 2026-05-19:
  - Secrets salvos no Doppler `lc-keys/prd`: `DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD`, `DATAFORSEO_AUTH_B64`, `DATAFORSEO_API_LOGIN`, `DATAFORSEO_API_PASSWORD`.
  - Teste API executado: DataForSEO `GET /v3/appendix/user_data`; HTTP 200, `status_code=20000`, `status_message=Ok.`.
  - Package instalado localmente: `dataforseo-mcp-server@2.9.2` em `/opt/data/profiles/lk-growth/mcp-servers/dataforseo/`.
  - Wrapper seguro: `run-dataforseo-mcp.sh`, busca credenciais no Doppler em runtime sem gravar valores no config.
  - `config.yaml` atualizado com `mcp_servers.dataforseo`.
  - Teste MCP stdio/list tools: OK, 79 tools descobertas, incluindo `serp_organic_live_advanced`, `kw_data_google_ads_search_volume`, `backlinks_summary`, `on_page_lighthouse`, `ai_optimization_chat_gpt_scraper` e `ai_opt_llm_ment_search`.
  - Relatórios: `reports/dataforseo-readiness-2026-05-19.md` e `reports/dataforseo-mcp-install-2026-05-19.md`.
- Uso após reload/restart do agente: live SERP, keyword volume/difficulty/intent, competitor domain, backlinks, Google Images, AI visibility/LLM mentions.
- Guardrail: estimar/logar custo antes de consultas em lote; não rodar crawls, exports grandes ou listas extensas sem aprovação explícita.

## Matriz rápida

- Shopify Admin: OK.
- GSC: OK; Claude SEO `gsc_query.py` validado e corrigido para respeitar `--limit` como limite total de linhas.
- GMC: OK.
- GA4: OK via canônico `GA4_LK_PROPERTY_ID`, padronizado para a propriedade funcional acessível; reteste `runReport` OK.
- Claude SEO: OK, v1.9.9 instalado/sincronizado; venv e Playwright Chromium em cache local protegido.
- Doppler CLI: OK, v3.76.0 instalado em `~/.local/bin` com wrapper que carrega o token local autorizado sem imprimir segredos.
- PageSpeed/CrUX: OK via `PAGESPEED_API_KEY`/`GOOGLE_API_KEY`; PSI OK para `https://lksneakers.com/`; CrUX field data OK no origin `https://lksneakers.com.br`.
- Klaviyo: OK para accounts/lists/metrics read-only.
- Meta/Paid: OK para ad account/campaigns/insights read-only.
- Ahrefs: OK via `AHREFS_API_TOKEN`; teste API v3 retornou Domain Rating para `lksneakers.com.br`.
- DataForSEO: MCP server instalado/configurado e validado via list-tools; exposição no agente ativo depende de reload/restart.

## Próximas ações

1. Recarregar/reiniciar o agente Hermes para expor as 79 tools DataForSEO no toolset ativo e, depois, rodar smoke test controlado com orçamento baixo.
2. Atualizar este inventário sempre que um conector sair de pendente/parcial para OK ou quando credenciais forem rotacionadas.
