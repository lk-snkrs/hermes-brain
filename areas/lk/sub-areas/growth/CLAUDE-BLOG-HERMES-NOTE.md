# Claude Blog no universo LK Growth / Hermes

Data: 2026-05-19
Fonte: https://github.com/AgriciDaniel/claude-blog
Repo local: `/opt/data/profiles/lk-growth/external-repos/claude-blog`
Commit local: `901e921`
Release/documentação lida: README, CHANGELOG, CLAUDE.md, docs/COMMANDS.md, docs/MCP-INTEGRATION.md
Status: instalado/sincronizado no perfil `lk-growth` como skills Hermes

## O que é

Claude Blog é um ecossistema de skills para criação, otimização e gestão de conteúdo editorial/blog em escala. Ele gera briefs, outlines, artigos, calendários, clusters, schema, auditorias, reescritas, checagem de fatos e conteúdo multilíngue, com foco duplo em Google SEO e citações por IA — ChatGPT, Perplexity, Gemini e AI Overviews.

No contexto LK, ele entra como a camada de `content engine` dentro de Growth: transforma demanda de GSC/GA4/Shopify/paid/SERP em guias, FAQs, artigos, páginas de apoio, clusters e blocos citáveis que reforçam PDPs/coleções e AI visibility.

## Instalação Hermes

Categoria local: `content-seo`

- Main orchestrator: `blog`
- Sub-skills instaladas/sincronizadas: 28 diretórios `blog*`.
- Backups antes da sincronização: `/opt/data/profiles/lk-growth/skill-backups/claude-blog-20260519-101940`

Principais skills:

- `blog` — orquestrador
- `blog-write` — escrever novo artigo
- `blog-rewrite` — reescrever/atualizar conteúdo existente
- `blog-analyze` — score 0-100
- `blog-brief` — brief editorial
- `blog-outline` — outline SERP-informed
- `blog-calendar` — calendário editorial
- `blog-strategy` — estratégia de conteúdo
- `blog-seo-check` — validação on-page
- `blog-schema` — JSON-LD BlogPosting/FAQ/Breadcrumb
- `blog-geo` — AI citation readiness
- `blog-audit` — health assessment de blog/site
- `blog-cannibalization` — canibalização de keywords
- `blog-factcheck` — verificação de estatísticas/fontes
- `blog-cluster` — topic clusters/hub-and-spoke
- `blog-flow` — FLOW framework
- `blog-multilingual`, `blog-translate`, `blog-localize`, `blog-locale-audit` — internacionalização/localização
- `blog-image`, `blog-audio`, `blog-notebooklm`, `blog-google` — recursos avançados/opcionais

Arquivos principais:

- `/opt/data/profiles/lk-growth/skills/content-seo/blog/SKILL.md`
- `/opt/data/profiles/lk-growth/skills/content-seo/blog/references/`
- `/opt/data/profiles/lk-growth/skills/content-seo/blog/templates/`
- `/opt/data/profiles/lk-growth/skills/content-seo/blog/scripts/`
- `/opt/data/profiles/lk-growth/skills/content-seo/blog/references/hermes-lk-adaptation.md`
- `/opt/data/profiles/lk-growth/skills/content-seo/blog/references/agents/`
- `/opt/data/profiles/lk-growth/skills/content-seo/blog/references/upstream-docs/`

## Como usar no Hermes

1. Carregar `blog` como skill orquestradora.
2. Para trabalhos focados, carregar sub-skill específica:
   - Brief/outline: `blog-brief`, `blog-outline`
   - Escrita/reescrita: `blog-write`, `blog-rewrite`
   - Qualidade/SEO/GEO: `blog-analyze`, `blog-seo-check`, `blog-geo`, `blog-schema`, `blog-factcheck`
   - Estratégia: `blog-strategy`, `blog-calendar`, `blog-cluster`, `blog-cannibalization`
   - Repurpose: `blog-repurpose`
3. Quando a documentação upstream fala em agentes Claude Code, usar `delegate_task` do Hermes e passar os prompts copiados em `references/agents/`.
4. Quando a documentação upstream fala em `~/.claude/skills/blog/...`, resolver para `/opt/data/profiles/lk-growth/skills/content-seo/blog/...`.

## Para que serve na LK

Use Claude Blog quando o problema de Growth for conteúdo/autoridade/citabilidade, não apenas title/meta/PDP/theme/feed.

Casos práticos:

- GSC mostra busca informacional com impressões, mas LK não tem página/artigo forte.
- Uma coleção/PDP precisa de conteúdo de apoio para capturar intenção topo/meio de funil.
- AI Search/GEO precisa de respostas citáveis, FAQ e blocos answer-first.
- Meta/Google Ads ou influenciadores geram perguntas recorrentes que deveriam virar artigo/FAQ.
- Conteúdo existente está velho, genérico, sem fonte, sem schema ou canibalizando outra página.
- Precisamos criar calendário editorial premium e comercialmente útil.
- Precisamos transformar artigo em assets sociais, email interno, roteiro de vídeo ou FAQ.

## Fluxo diário recomendado

### 1. Descoberta de oportunidade

Fonte preferencial:

- GSC queries/impressões/CTR/posição;
- GA4 sessões e engajamento;
- Shopify receita/conversão quando conteúdo apoia PDP/coleção;
- Meta/Google Ads e influenciadores como sinal de demanda;
- SERP/DataForSEO/Ahrefs para lacunas competitivas;
- Atendimento/chat quando há perguntas recorrentes.

Se não houver demanda ou justificativa estratégica, não priorizar conteúdo só porque dá para escrever.

### 2. Brief antes de artigo

Produzir primeiro um pacote de decisão:

- tema;
- intenção de busca;
- público;
- target query;
- página destino ou cluster ligado;
- fontes necessárias;
- estrutura proposta;
- impacto esperado;
- esforço/risco;
- aprovação necessária.

### 3. Draft e validação

Depois do brief aprovado ou quando for só rascunho interno:

- `blog-outline` para estrutura;
- `blog-write` ou `blog-rewrite` para conteúdo;
- `blog-seo-check` para on-page;
- `blog-geo` para citabilidade/AI readiness;
- `blog-schema` para JSON-LD proposto;
- `blog-factcheck` para estatísticas e claims.

### 4. Publicação só com aprovação

Claude Blog pode preparar conteúdo, mas não publica. Qualquer write externo precisa aprovação explícita atual de Lucas:

- Shopify/blog/page/article;
- Klaviyo/email/WhatsApp;
- posts sociais;
- campanhas;
- schema em produção;
- alterações customer-facing.

Após publicação aprovada: registrar rollback/receipt/evidência e agendar revisão de impacto em ~7 dias.

## Metodologia principal aprendida

### 6 pilares de otimização

1. Answer-first formatting: cada H2 abre com resposta direta e citável.
2. Dados reais e fontes: estatísticas precisam de fonte nomeada.
3. Visual media: imagens, charts, vídeos quando úteis.
4. FAQ schema: perguntas/respostas extraíveis por IA.
5. Estrutura legível por IA: chunks de 50-150 palavras, hierarquia clara.
6. Freshness: data de atualização e fontes recentes.

### Score 0-100

- Content Quality: 30 pts
- SEO Optimization: 25 pts
- E-E-A-T Signals: 15 pts
- Technical Elements: 15 pts
- AI Citation Readiness: 15 pts

Bandas:

- 90-100: Exceptional
- 80-89: Strong
- 70-79: Acceptable
- 60-69: Below Standard
- <60: Rewrite

### Quality gates

- Zero estatística fabricada.
- Parágrafo nunca acima de 150 palavras.
- Heading hierarchy sem pular níveis.
- Fontes Tier 1-3; evitar content mills/afiliados fracos.
- Alt text em imagens.
- Máximo 1 menção autopromocional por peça.
- Não gerar conteúdo sem pesquisa.

## Recursos avançados e cautelas

- `blog-google` compartilha lógica com Google APIs: para LK, preferir os conectores já validados de GSC/GA4/PageSpeed/CrUX quando disponíveis e declarar a fonte.
- `blog-image` usa Gemini/nanobanana MCP; não configurar novo MCP ou gravar secrets sem necessidade. Qualquer imagem customer-facing precisa aprovação.
- `blog-audio` usa Gemini TTS; útil para narração/resumo, mas envio externo precisa aprovação.
- `blog-notebooklm` pode ser útil para pesquisa source-grounded, mas requer autenticação/ambiente próprio.
- DataForSEO é recomendado pelo upstream para SERP/keyword/AI visibility. No LK Growth, DataForSEO MCP já foi instalado/validado, mas ferramentas ativas dependem de reload/restart; evitar chamadas pagas em massa sem escopo/custo.

## Guardrails LK

- Tom premium, humano e minimalista.
- Não criar taxonomia pública de `pronta entrega`, `encomenda` ou `estoque`.
- Disponibilidade e prazo vão para chat/atendimento.
- Linguagem preferida: curadoria exclusiva, autenticidade, atendimento humano, orientação especializada.
- Paid/influencer signals servem como demanda/contexto, não como autorização de campanha.
- Blog/content nunca substitui dados comerciais como fonte de verdade.

## Implementação no dia a dia

Claude Blog passa a ser obrigatório como camada quando o LK Growth envolver:

- calendário/editorial;
- guias e conteúdos informacionais;
- FAQ/knowledge base;
- GEO/AI citation pages;
- topic clusters;
- conteúdo de apoio a coleções/PDPs;
- atualização ou auditoria de blog;
- repurpose de conteúdo.

Para auditorias Growth completas, marcar conteúdo/taxonomia comercial e GEO/AI Search usando Claude Blog quando houver componente editorial, depois de priorizar por GA4/GSC/Shopify/GMC/demanda.
