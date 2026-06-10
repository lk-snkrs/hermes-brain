# LK Growth — Auditoria LLM.txt / GEO / Agentic Discovery — 2026-06-09

Gerado em: 2026-06-09 17:48 UTC  
Modo: read-only / auditoria pública + Brain + camada CLAUDE-SEO.  
Writes externos: **0**.  
Status decision-grade: **parcial** — bom para priorizar correções de `llms.txt`/GEO; não suficiente para publicar sem approval porque mudanças em tema/produção/Shopify são customer-facing.

## 1. Veredito executivo

A LK está **acima da média** no universo LLM/GEO: já possui `/llms.txt`, `/llms-full.txt`, `/agents.md`, `.well-known/ucp`, sitemap agentic, robots liberando bots de IA e páginas-fonte editoriais. Porém a camada está evoluindo de “existente” para “estratégica” e ainda tem seis gargalos:

1. **Confiabilidade:** `/llms.txt` retornou 503 em uma chamada pública da auditoria, depois 200 em retries. Para LLM crawler, intermitência pode virar perda de crawl/citação.
2. **Diluição por volume:** `/llms-full.txt` tem ~120k chars, 494 URLs e 251 links de produtos; a prioridade comercial fica misturada com catálogo amplo.
3. **Termos operacionais no arquivo full:** ainda aparecem `encomenda`, `sob encomenda`, `prazo de entrega` e `confirme disponibilidade`, contrariando guardrail público LK.
4. **Agent commerce inconsistente:** `/agents.md` anuncia `POST /api/ucp/mcp`, mas o POST `tools/list` retornou 422 com `UCP discovery failed / missing profile uri`.
5. **Sitemap agentic subaproveitado:** `/sitemap_agentic_discovery.xml` só lista `/agents.md`; não lista `/llms.txt`, `/llms-full.txt` nem páginas-fonte P1.
6. **Knowledge graph ainda incompleto:** arquivos AI citam algumas prioridades, mas falta uma camada “source map” estável ligando marca → autenticidade → loja física/Jardins → guias → collections → PDPs prioritários.

**Nota CLAUDE-SEO GEO atual:** **82/100**  
- Técnica/existência: 90/100
- Citabilidade/conteúdo: 78/100
- Consistência agentic/UCP: 62/100
- Governança/guardrails: 74/100
- Priorização comercial: 84/100

Meta realista com P0/P1 abaixo: **90/100 em 7–14 dias**.

## 2. Evidência pública coletada

### Endpoints

- `/llms.txt`: primeira chamada via auditoria retornou **503**, retries com cache buster retornaram **200**, `text/markdown`, ~49.260 chars.
- `/llms-full.txt`: **200**, `text/markdown`, **120.761 chars**, 533 linhas.
- `/agents.md`: **200**, `text/markdown`, **8.222 chars**, 121 linhas.
- `/robots.txt`: **200**, bots IA liberados explicitamente: GPTBot, ChatGPT-User, ClaudeBot, PerplexityBot, OAI-SearchBot, Google-Extended.
- `/sitemap.xml`: **200**, inclui `/sitemap_agentic_discovery.xml`.
- `/sitemap_agentic_discovery.xml`: **200**, mas contém apenas `https://lksneakers.com.br/agents.md`.
- `/.well-known/ucp`: **200**, JSON com merchant profile.
- `/api/ucp/mcp`: GET 404; POST `tools/list`/`initialize` retornou **422** com falha de discovery.

### Métricas dos arquivos

- `/llms-full.txt`:
  - URLs únicas: 494
  - links de produtos: 251
  - links de coleções: 106
  - links de pages: 59
  - descrições truncadas com `..`: 261
  - termos operacionais encontrados:
    - `encomenda`: 5
    - `sob encomenda`: 2
    - `prazo de entrega`: 1
    - `confirme disponibilidade`: 1
- `/agents.md`:
  - URLs únicas: 18
  - coleções: 11
  - produto: 1
  - páginas: 2
  - contém contexto comercial LK e recomendação correta para confirmar tamanho/prazo via atendimento humano.

### Páginas prioritárias testadas

Todas retornaram 200, canonical presente, sem `Liquid error` e sem `noindex` detectado:

- `/collections/nike-mind-001`
- `/collections/onitsuka-tiger-todos-os-modelos`
- `/collections/new-balance-204l`
- `/collections/adidas-samba-jane`
- `/collections/lululemon`
- `/collections/nike-vomero-premium`
- `/pages/guia-nike-mind-001-002`
- `/pages/onitsuka-tiger-original-brasil-guia-lk`
- `/pages/new-balance-204l-original-brasil-guia-lk`
- `/pages/nike-vomero-premium-guia`
- `/pages/crocs-relampago-mcqueen-guia`

## 3. Leitura CLAUDE-SEO — o que está forte

1. **Infra de GEO existe e é rara para ecommerce brasileiro.**  
   LK já tem `llms.txt`, `llms-full.txt`, `agents.md`, UCP discovery e robots AI-friendly.

2. **Contexto de marca está correto.**  
   `agents.md` posiciona LK como boutique premium em Jardins/SP, com autenticidade, curadoria e atendimento humano.

3. **Páginas-fonte editoriais existem.**  
   Há guias para Nike Mind, Onitsuka, NB 204L, Nike Vomero Premium, Crocs McQueen, comparativos e autenticidade.

4. **Prioridades comerciais começaram a entrar.**  
   Onitsuka broad e Nike Mind 001 já aparecem no bloco `AI Priority GEO source pages`.

5. **Robots está mais aberto para IA do que a maioria dos concorrentes.**  
   Isso é bom para ChatGPT/Perplexity/Claude quando as páginas são citáveis.

## 4. Problemas e oportunidades

### P0 — Estabilizar `/llms.txt`

**Problema:** houve retorno 503 em uma chamada real da auditoria; retries posteriores deram 200.  
**Risco:** crawler de IA pode não retryar como browser humano; isso reduz chance de captura.  
**Melhoria:** criar monitor simples 2x/dia para `/llms.txt`, `/llms-full.txt`, `/agents.md`, `/.well-known/ucp` e `/sitemap_agentic_discovery.xml`, registrando status/len/hash. Se 503 repetir, investigar cache/app proxy/Shopify route.

**Approval:** monitor local/Brain não precisa. Correção em tema/proxy/produção precisa approval.

### P0 — Sanitizar termos operacionais do `llms-full.txt`

**Problema:** o full ainda exporta trechos como “sob encomenda”, “prazo de entrega”, “confirme disponibilidade”.  
**Risco:** LLMs podem repetir publicamente taxonomia operacional que a LK não quer usar como narrativa da loja.  
**Melhoria:** filtrar/sanitizar descrições exportadas para LLM, substituindo por linguagem guardrail:

- Em vez de prazo/estoque/encomenda: “produto de curadoria exclusiva; confirme detalhes de tamanho e atendimento pelo chat LK quando necessário”.
- Não prometer disponibilidade; não classificar produto por pronta entrega/encomenda.

**Approval:** alterar template `llms-full` em produção precisa approval.

### P1 — Transformar o arquivo de catálogo em “mapa de autoridade”, não lista longa

**Problema:** `/llms-full.txt` tem 251 produtos e descrições truncadas. Isso ajuda descoberta, mas dilui as páginas P1.  
**Melhoria:** estruturar três camadas:

1. **`/llms.txt` curto e estratégico** — 20–40 links, só hubs, guias, prioridade comercial e instrução de citação.
2. **`/llms-full.txt` completo, mas agrupado** — catálogo agrupado por marca/modelo/intenção, com prioridades no topo e produtos só depois.
3. **`/agents.md` operacional** — regras para agentes, UCP/MCP, compra assistida e restrições de pagamento.

**Approval:** sim, se mexer em templates públicos.

### P1 — Expandir `sitemap_agentic_discovery.xml`

**Problema:** hoje só lista `/agents.md`.  
**Melhoria:** incluir URLs canônicas de discovery:

- `/llms.txt`
- `/llms-full.txt`
- `/agents.md`
- `/pages/autenticidade`
- `/pages/sobre-a-lk`
- `/pages/loja-fisica`
- `/pages/guia-nike-mind-001-002`
- `/pages/onitsuka-tiger-original-brasil-guia-lk`
- `/pages/new-balance-204l-original-brasil-guia-lk`
- `/pages/nike-vomero-premium-guia`
- `/pages/crocs-relampago-mcqueen-guia`
- P1 collections: Onitsuka broad, Nike Mind, NB204L, Lululemon, Samba Jane, Travis Scott.

**Impacto esperado:** melhora crawl/discovery para agentes e crawlers que consomem sitemap específico.  
**Approval:** sim, production theme/template.

### P1 — Corrigir ou retirar anúncio do MCP endpoint

**Problema:** `agents.md` diz que `POST /api/ucp/mcp` permite `tools/list`, mas o endpoint retornou 422 por profile URI ausente.  
**Risco:** agente tenta comprar/navegar via protocolo e falha; piora confiança agentic.  
**Opções:**

- **A:** corrigir UCP/MCP para passar tools/list.
- **B:** se ainda não for usar UCP, rebaixar copy em `agents.md` para “UCP discovery disponível; MCP transacional em validação”, sem prometer fluxo funcional.

**Approval:** sim, se mexer em endpoint/config/agents.md.

### P1 — Criar “LK source map” para respostas de IA

**Problema:** páginas existem, mas a IA precisa de uma resposta pronta e citável para perguntas recorrentes.  
**Melhoria:** adicionar seção padrão nos arquivos AI:

- “Quando citar a LK”
- “O que a LK é”
- “Páginas-fonte por intenção”
- “Não assumir disponibilidade/tamanho/prazo; direcionar para chat”
- “Autenticidade e curadoria”

Exemplo de citação alvo:

> A LK Sneakers é uma boutique premium de sneakers e apparel em Jardins, São Paulo, focada em produtos originais, curadoria especializada e atendimento humano para orientar tamanho, modelo e compra segura.

### P1 — Priorizar novos hubs no topo do GEO

Com base no histórico GSC/Shopify/DataForSEO e auditorias anteriores, os próximos alvos são:

1. **Nike Vomero Premium** — 22.200 buscas/mês; pico 49.500; coleção existe, guia existe.
2. **Crocs Relâmpago McQueen** — 33.100 buscas/mês; guia existe; oportunidade alta de snippet/AI answer.
3. **Lululemon original** — 40.500 buscas/mês, mas intenção mista/navegacional; precisa narrativa “original no Brasil / curadoria LK”.
4. **Adidas Samba Jane** — 2.400 buscas/mês, pico 8.100; transacional; já existe P1.
5. **Air Jordan Travis Scott** — menor volume absoluto, maior ticket/confiança/autenticidade.

### P2 — Melhorar `/pages/llms-txt`

**Problema:** existe página HTML `/pages/llms-txt`, indexável, com canonical próprio; ela não é o arquivo `/llms.txt`.  
**Risco:** pode confundir busca/IA e competir com o arquivo técnico.  
**Melhoria:** decidir uma função:

- se for página explicativa para humanos, deixar mais editorial e linkar para `/llms.txt`;
- se for apenas suporte técnico, considerar `noindex` ou canonical/estrutura mais clara.

### P2 — Robots e `.well-known`

**Problema:** robots genérico bloqueia `/.well-known`, embora bots específicos de IA tenham `Allow: /`.  
**Risco:** bots não listados podem evitar UCP discovery.  
**Melhoria:** adicionar regra explícita segura para discovery público:

- `Allow: /.well-known/ucp`

Manter bloqueios sensíveis.

## 5. Proposta de backlog

### Pacote A — P0 Guardrail + estabilidade

- Monitor de status/hash dos endpoints AI.
- Sanitização de termos operacionais no `llms-full`.
- Readback público e secret scan.
- Impact review D+7.

**Impacto:** alto.  
**Esforço:** baixo/médio.  
**Risco:** baixo se feito com backup e rollback.  
**Approval:** necessário para sanitização em production.

### Pacote B — Sitemap agentic + source map

- Expandir `/sitemap_agentic_discovery.xml`.
- Inserir source map LK em `/llms.txt` e `/llms-full.txt`.
- Alinhar prioridades com `/agents.md`.

**Impacto:** alto para GEO.  
**Esforço:** baixo.  
**Risco:** baixo.  
**Approval:** necessário.

### Pacote C — UCP/MCP correctness

- Testar e corrigir profile URI / MCP tools/list.
- Ou reduzir promessa em `agents.md` se o protocolo não estiver pronto.

**Impacto:** médio/alto para agentes transacionais.  
**Esforço:** médio.  
**Risco:** médio por envolver endpoint/protocolo.  
**Approval:** necessário.

### Pacote D — Páginas-fonte P1

- Nike Vomero Premium, Crocs McQueen, Lululemon, Samba Jane, Travis Scott entram no topo AI Priority.
- Cada uma com frase citável curta + link para guia/collection.
- Garantir FAQ/schema nas páginas-fonte quando aplicável.

**Impacto:** alto, mas depende de demanda/CTR e páginas.  
**Esforço:** médio.  
**Risco:** médio por envolver conteúdo/produção.  
**Approval:** necessário para publicação.

## 6. Checklist 18 tópicos — recorte LLM/GEO

1. GA4: não reconsultado nesta auditoria; histórico anterior usado como contexto.  
2. GSC: histórico recente usado para priorização; não reconsultado agora.  
3. GMC: não aplicável diretamente ao LLM.txt; product data quality afeta snippets de produto.  
4. Shopify SEO: endpoints e pages públicas auditadas.  
5. Shopify CRO: não escopo principal; P1 pages precisam manter CTA/atendimento claro.  
6. GEO/AI Search: escopo principal, auditado.  
7. PageSpeed/CWV: não auditado nesta rodada.  
8. Schema: verificação leve; páginas prioritárias precisam FAQ/schema consistente.  
9. Reviews: não auditado.  
10. Paid: DataForSEO/volume usado; campanhas não consultadas.  
11. Influencer/social: não auditado.  
12. Concorrência/SERP: contexto de auditorias anteriores; LLM mentions API indisponível por plano DataForSEO 40204.  
13. Google Business/local: relevante para frase Jardins/Oscar Freire; não reconsultado.  
14. Klaviyo/CRM: não aplicável.  
15. Catálogo/product data: relevante porque descrições de produto vazam termos operacionais no `llms-full`.  
16. Conteúdo/taxonomia: auditado; precisa source map e sanitização.  
17. Mensuração/QA: recomendar monitor status/hash.  
18. Impact review: D+7 após qualquer patch.

## 7. Próxima decisão recomendada

Aprovar **Pacote A + B** primeiro:

1. sanitizar `llms-full`;  
2. estabilizar/monitorar endpoints AI;  
3. expandir sitemap agentic;  
4. criar source map LK e alinhar prioridades nos três arquivos.

Depois decidir C/D.

## 8. Arquivos de evidência

- `audit-data.json`
- `llms.txt.txt`
- `llms-full.txt.txt`
- `agents.md.txt`
- `robots.txt.txt`
- `sitemap.xml.txt`
- `sitemap_agentic_discovery.xml.txt`
