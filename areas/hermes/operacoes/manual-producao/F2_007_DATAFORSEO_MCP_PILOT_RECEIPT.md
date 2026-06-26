# F2-007 — Piloto MCP DataForSEO pequeno

Gerado em: 2026-05-30T22:29:07+00:00  
Status: **executado / piloto read-only externo pequeno**  
Escopo: validar que o MCP DataForSEO já configurado consegue responder uma consulta LK SEO/GEO pequena sem alterar runtime, config ou dados externos.  
Guardrail: uma keyword, duas tools, sem batch amplo, sem writes externos, sem secrets no output.

## MCP usado

- Server: `dataforseo`
- Caminho físico: `/opt/data/profiles/lk-growth/mcp-servers/dataforseo/`
- Wrapper: `run-dataforseo-mcp.sh`
- Cliente ad-hoc: `mcporter`
- Config nativa observada anteriormente: disponível em `lk-shopify` e `lk-trends`; sampling desligado.

## Consulta executada

Keyword: `tênis premium`  
Local: `Brazil`  
Idioma: `pt`

Tools chamadas:

1. `dataforseo_labs_google_keyword_overview`
2. `dataforseo_labs_search_intent`

## Resultado resumido

`dataforseo_labs_google_keyword_overview` retornou status OK:

- search volume: `480`
- competition: `1`
- competition level: `HIGH`
- CPC estimado: `0.21`
- low top of page bid: `0.05`
- high top of page bid: `0.36`
- trend mensal: `+22%`
- trend trimestral: `+50%`
- trend anual: `-34%`
- intent no overview: `transactional`

`dataforseo_labs_search_intent` retornou status OK:

- intent principal: `informational`
- probabilidade: `0.539`
- intent secundário: `commercial`
- probabilidade: `0.34`

## Leitura operacional

O MCP funciona e entrega dado útil em latência aceitável para uso pontual. A divergência entre `overview` e `search_intent` reforça que DataForSEO deve ser tratado como sinal analítico, não como decisão automática.

Para LK, o uso mais promissor é:

- descobrir intenção e volume de keywords;
- comparar demanda de termos de coleção/produto;
- validar oportunidade SEO/GEO;
- enriquecer approval packets de páginas/coleções;
- apoiar Trend radar com dados externos.

## Limites do piloto

- não mede custo com precisão;
- não valida chamadas grandes;
- não valida backlinks/onpage/batch;
- não prova que o native MCP está carregado no runtime do profile até haver restart/descoberta ativa;
- não substitui Shopify/Tiny/GMC/GA4/Metricool como fontes de verdade operacionais.

## Próxima ação recomendada

Manter DataForSEO como piloto MCP aprovado para consultas pequenas, com whitelist:

- keyword overview;
- search intent;
- ranked keywords;
- SERP competitors;
- organic SERP live;
- on-page instant/lighthouse apenas por URL específica.

Bloquear sem approval:

- scans amplos;
- batch/bulk backlinks;
- domínio inteiro;
- loops automáticos;
- qualquer rotina recorrente que consuma créditos sem orçamento/limite.
