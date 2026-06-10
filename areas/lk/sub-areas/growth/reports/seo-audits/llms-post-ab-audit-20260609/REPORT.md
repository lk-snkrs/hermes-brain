# LK Growth — Pós-audit LLM/GEO após Pacote A+B

Data: 2026-06-09T18:08:38.747323+00:00
Escopo: read-only, sem writes externos.

## Veredito executivo

Sim: está melhor.

A camada AI/GEO da LK saiu de uma nota estimada ~82/100 para ~91/100 no pós-audit técnico. O ganho veio de:

- Source Map LK presente em `/llms.txt`, `/llms-full.txt` e `/agents.md`.
- Prioridades comerciais alinhadas nos 3 arquivos AI.
- Sanitização dos termos operacionais críticos com contagem 0 para:
  - pronta entrega
  - encomenda
  - estoque
  - sob encomenda
  - prazo de entrega
  - confirme disponibilidade
- Endpoints principais com HTTP 200 no readback.
- Monitor local rodando OK e sem falhas.
- `robots.txt` agora anuncia/permite descoberta AI.

Ainda não é 95+/100 por 4 pontos:

1. `/llms.txt` está grande demais para a função estratégica: 51.142 chars, 222 URLs. Ideal: 20–40 links.
2. `/sitemap_agentic_discovery.xml` ainda lista só `/agents.md`.
3. `/api/ucp/mcp` segue quebrando `tools/list` com 422 / `missing profile uri`.
4. `agents.md` ainda promete UCP/MCP como se estivesse funcional; precisa corrigir endpoint ou rebaixar promessa.

## Evidência técnica

### Endpoints

- `/llms.txt`: 200, 51.142 chars, Source Map presente, 222 URLs.
- `/llms-full.txt`: 200, 122.338 chars, Source Map presente, 492 URLs.
- `/agents.md`: 200, 9.721 chars, Source Map presente, 21 URLs.
- `/robots.txt`: 200, contém `Allow: /.well-known/ucp` e sitemap agentic relativo.
- `/.well-known/ucp`: 200.
- `/sitemap_agentic_discovery.xml`: 200, mas apenas 1 URL: `/agents.md`.
- `/api/ucp/mcp`: 422 em `tools/list`; erro `UCP discovery failed`, `invalid_profile_url`, `Missing profile uri`.

### Prioridades GEO presentes nos 3 arquivos AI

- Nike Mind 001: OK.
- Onitsuka Tiger todos os modelos: OK.
- New Balance 204L: OK.
- Nike Vomero Premium: OK.
- Crocs Relâmpago McQueen: OK.
- Lululemon: OK.
- Adidas Samba Jane: OK.
- Air Jordan Travis Scott: OK.

### Páginas-fonte prioritárias

Todas responderam 200, sem `Liquid error`, com canonical e H1 principal:

- `/collections/nike-mind-001`: FAQPage presente.
- `/collections/onitsuka-tiger-todos-os-modelos`: FAQPage presente.
- `/collections/new-balance-204l`: FAQPage presente.
- `/collections/nike-vomero-premium`: sem FAQPage.
- `/pages/crocs-relampago-mcqueen-guia`: sem FAQPage.
- `/collections/lululemon`: FAQPage presente.
- `/collections/adidas-samba-jane`: FAQPage presente.
- `/collections/air-jordan-travis-scott`: FAQPage presente.
- `/pages/autenticidade`: FAQPage presente; 2 H1 detectados.
- `/pages/loja-fisica`: sem FAQPage.
- `/pages/sobre-a-lk`: sem FAQPage; 2 H1 detectados.

## Demanda Google validada no DataForSEO

- Lululemon: 40.500 buscas/mês.
- Onitsuka Tiger: 33.100 buscas/mês.
- Crocs Relâmpago McQueen: 33.100 buscas/mês.
- Nike Vomero Premium: 22.200 buscas/mês.
- Nike Mind 001: 18.100 buscas/mês.
- New Balance 204L: 9.900 buscas/mês, tendência anual muito forte.
- Adidas Samba Jane: 2.400 buscas/mês, pico recente 8.100.
- Air Jordan Travis Scott: 1.300 buscas/mês.

Observação: consulta DataForSEO de menções LLM por domínio retornou acesso negado no plano atual, então o relatório mede prontidão técnica/GEO e demanda, não incremento real de citações em ChatGPT.

## O que melhorou

- Clareza de entidade: LK agora se apresenta como boutique premium, originalidade, curadoria e atendimento humano.
- Menos risco operacional: termos críticos que poderiam induzir IA a prometer disponibilidade/prazo foram removidos dos arquivos centrais.
- Melhor roteamento de intenção: páginas comerciais prioritárias aparecem juntas e com contexto em `llms`, `llms-full` e `agents`.
- Melhor crawl/discovery: `robots.txt` aponta para sitemap agentic e libera bots AI principais.
- Monitoramento: existe rotina local para status/hash/tamanho/termos proibidos.

## O que ainda dá para melhorar

### Pacote C — enxugar `/llms.txt` para arquivo realmente estratégico

Impacto: alto para LLMs rápidos e crawlers com limite de contexto.
Esforço: baixo/médio.
Risco: baixo, com rollback simples.

Proposta:

- `/llms.txt`: manter só Source Map, 20–40 links prioritários e instruções de citação.
- `/llms-full.txt`: manter o inventário completo.
- Remover lista massiva de produtos do `/llms.txt`, que hoje dilui o sinal.

### Pacote D — corrigir sitemap agentic real

Impacto: médio/alto.
Esforço: médio, depende de localizar origem da rota.
Risco: médio.

Proposta de conteúdo mínimo:

- `/agents.md`
- `/llms.txt`
- `/llms-full.txt`
- `/pages/autenticidade`
- `/pages/loja-fisica`
- `/pages/sobre-a-lk`
- top 8 coleções GEO
- top guias editoriais GEO

### Pacote E — UCP/MCP: corrigir ou rebaixar promessa

Impacto: alto para agentic commerce correctness.
Esforço: médio/alto.
Risco: médio.

Opção 1: corrigir `profile uri` e validar `tools/list` 200.
Opção 2: alterar `agents.md` para deixar UCP como experimental/não garantido até funcionar.

Hoje, o risco é reputacional/técnico: o arquivo promete fluxo MCP funcional, mas o endpoint retorna 422.

### Pacote F — reforço schema/FAQ nas páginas prioritárias sem FAQPage

Impacto: médio.
Esforço: baixo/médio.
Risco: baixo se feito em dev theme/preview.

Candidatas:

- Nike Vomero Premium.
- Crocs Relâmpago McQueen guia.
- Loja Física.
- Sobre a LK.

### Pacote G — sanitização fina de termos amplos

Impacto: médio.
Esforço: baixo.
Risco: baixo.

Embora os termos críticos estejam zerados, ainda aparecem termos amplos como `prazo`, `disponibilidade` e `entrega` em alguns arquivos, principalmente por políticas/páginas e alguns marcadores antigos. Não é P0, mas dá para deixar mais limpo.

## 18 tópicos canônicos — cobertura

- GA4: não avaliado neste audit; precisa dados autenticados para impacto real.
- GSC: não avaliado neste audit; usar D+7/D+14 para queries e CTR.
- GMC: não alterado; residual anterior deve seguir monitorado separadamente.
- Shopify SEO: avaliado parcialmente em páginas-fonte/canonicals/H1/schema.
- Shopify CRO/theme: não avaliado profundamente; sem alterações visuais neste audit.
- GEO/AI Search: auditado em profundidade.
- PageSpeed/CrUX/CWV: não avaliado neste ciclo.
- Schema: avaliado parcialmente por marcadores FAQPage/Collection/Product.
- Reviews/prova social: não avaliado neste ciclo.
- Paid media: usado apenas como contexto de demanda; sem alterações.
- Influencer/social demand: não avaliado neste ciclo.
- Concorrência/SERP: demanda validada; SERP comparativa não refeita neste pós-audit.
- Google Business/local: loja física está referenciada; GBP não auditado.
- Klaviyo/CRM signals: não avaliado.
- Catálogo/product data quality: avaliado só como diluição em `llms-full`/`llms`.
- Conteúdo/taxonomia comercial: avaliado em GEO/source map.
- Mensuração/QA de eventos: não avaliado.
- Impact review/experimentation: recomendado D+7/D+14 via GSC/GA4.

## Recomendação de próximo passo

Executar Pacote C + E primeiro:

1. Pacote C: transformar `/llms.txt` no arquivo curto e decisivo da LK.
2. Pacote E: corrigir ou rebaixar UCP/MCP para não prometer agentic checkout quebrado.

Depois fazer Pacote D do sitemap agentic e Pacote F de FAQ/schema nas páginas que ainda não têm FAQPage.

Writes necessários: sim, para qualquer alteração em Shopify produção. Precisa aprovação explícita de Lucas antes de executar.
