# PRD — Implantação Paperclip para SPITI Auction

> Status: rascunho v0.1
> Data: 2026-05-05
> Dono: Lucas Cimino
> Apoio: Hermes Agent + Paperclip
> Empresa Paperclip proposta: **SPITI Auction Growth & Product OS**

---

## 1. Resumo executivo

A SPITI Auction já tem um projeto crítico em andamento, o **Spiti Hub**, que será o sistema operacional interno da casa de leilões/galeria: CRM, obras, leilões, vendas, financeiro, marketing, IA, integrações e migração gradual de Tango/FileMaker + spiti-financial. Em paralelo, Lucas quer usar o **Paperclip** como camada de orquestração de agentes autônomos para organizar, delegar, auditar e acelerar o trabalho de produto, SEO, conteúdo, mídia paga, newsletter, analytics e futuro site público.

O objetivo deste PRD é definir a implantação inicial do Paperclip para a SPITI: quais empresas/projetos criar, qual missão inserir no onboarding, quais agentes contratar, quais rotinas configurar, quais skills/imports usar, quais integrações priorizar e quais guardrails impedirão ações perigosas sem aprovação humana.

A visão não é “um chatbot para ajudar no marketing”. A visão é uma **mini-empresa operacional de IA**, governada pelo Lucas, com times de produto/engenharia, SEO/conteúdo, performance criativa, analytics e growth, trabalhando em issues rastreáveis e PRs seguros.

---

## 2. Base de conhecimento usada

### 2.1 Paperclip

Pesquisa feita em `paperclip.ing`, docs públicas e GitHub `paperclipai/paperclip`.

Pontos fundamentais:

- Paperclip é um **control plane para empresas tocadas por agentes**.
- Conceitos centrais:
  - **Company**: boundary isolado com missão, agentes, tasks, projetos e orçamento.
  - **Agent**: funcionário IA com cargo, manager, adapter, orçamento e política de execução.
  - **Task/Issue**: unidade rastreável de trabalho, com status, comentários e dono.
  - **Project**: agrupamento de trabalho vinculado a repo/diretório/meta.
  - **Heartbeat/Routine**: execução agendada/event-driven; agentes não precisam ficar acordando à toa.
  - **Approvals**: camada de governança para contratação, estratégia, orçamento e decisões de risco.
  - **Skills**: procedimentos reutilizáveis carregados sob demanda.
  - **Adapters**: Claude Code, Codex, Hermes Local, OpenClaw, HTTP, Process etc.
- O Paperclip não substitui os agentes; ele coordena agentes, custos, auditoria, tasks e governança.
- O adapter `hermes_local` é especialmente relevante porque roda Hermes Agent com memória persistente, session search, ferramentas, skills, delegação e MCP.
- Em Docker, Paperclip expõe por padrão porta `3100`, usa `PAPERCLIP_HOME` para persistência e pode usar DB embutido ou `DATABASE_URL` externo.
- Paperclip tem API JSON para companies, agents, issues, approvals, routines e secrets.

### 2.2 Claude SEO / Codex SEO

Pesquisa feita em `AgriciDaniel/claude-seo` e `AgriciDaniel/codex-seo`.

Pontos úteis:

- `claude-seo` é uma suíte grande de SEO para Claude Code: auditoria, técnico, página, conteúdo, E-E-A-T, schema, sitemap, imagens, GEO/AEO, local/maps, performance, backlinks, Google APIs, DataForSEO, Firecrawl, geração de relatórios.
- O repo menciona **21+ sub-skills**, subagents e extensões.
- Comandos principais:
  - `/seo audit <url>` — auditoria completa; crawla até 500 páginas, score e plano de ação.
  - `/seo page <url>` — análise profunda de página.
  - `/seo technical <url>` — crawlability, indexability, segurança, URL, mobile, CWV, schema, JS rendering.
  - `/seo content <url>` — E-E-A-T, qualidade, IA citation readiness.
  - `/seo schema <url>` — detectar/validar/gerar JSON-LD.
  - `/seo geo <url>` — otimização para AI Overviews/AI search.
  - `/seo google ...` — GSC, GA4, PageSpeed, CrUX, URL Inspection, Indexing API, Keyword Planner.
  - `/seo image-gen ...` — assets visuais SEO/social, se extensão Banana/nanobanana MCP estiver instalada.
  - `/seo plan <type>` — estratégia SEO por tipo de negócio.
- Para o nosso setup, como o modelo Hermes atual é GPT-5.5 via `openai-codex`, o **`codex-seo` pode ser mais natural para agentes Codex**, mas o `claude-seo` original segue útil como referência e/ou skill instalada em agentes Claude Code se o Paperclip estiver usando `claude_local`.
- `seo-google` depende de credenciais Google: API key, OAuth/service account, GSC property, GA4 property ID e, se usar Keyword Planner, Google Ads developer token/customer ID.

### 2.3 Contexto SPITI existente

Fontes internas consultadas:

- `hermes-brain/memories/spiti.md`
- `spiti-hub-github.md`
- `spiti-hub/docs/prd-spiti-hub.md`
- `spiti-hub/docs/operacao-spiti.md`

Pontos críticos:

- SPITI é casa de leilões + galeria; site atual: `https://www.spiti.art`, hospedado no Artlogic.
- Instagram: `@spiti.auction`.
- Endereço: Rua Amauri, 62 — Jardim Europa — São Paulo/SP.
- Stack do Spiti Hub: React + Vite + Tailwind, Supabase, Vercel, Claude API, Evolution/WhatsApp, MailerLite, Meta Marketing API, Google Ads API.
- Repo privado: `spiti-auction/spiti-hub`.
- Fluxo GitHub: `main` produção, `dev` staging, PR para `dev`.
- O Spiti Hub já passou por rodadas recentes de hardening via PRs, lint/build OK e bundle splitting.
- Regra operacional: **silêncio > dado errado**; não inventar lances, dados, métricas ou clientes.
- Regra de ações externas: campanhas, WhatsApp, email, postagens, anúncios e contato com clientes exigem preview/aprovação do Lucas.
- Supabase SPITI: project ref `rmdugdkantdydivgnimb`.

---

## 3. Objetivo do produto

Implantar uma Company no Paperclip para a SPITI que funcione como **sistema de gestão de agentes** para:

1. Gestão, melhoria e desenvolvimento seguro do **Spiti Hub**.
2. Produção automatizada, mas governada, de conteúdo SEO/blog.
3. Produção de arte e variações criativas para Instagram/tráfego pago.
4. Produção de newsletters, possivelmente via MailerLite.
5. Leitura de dados de GA4, GSC, PageSpeed/CrUX e eventualmente Google Ads/Meta.
6. Implementação de melhorias SEO usando `claude-seo`/`codex-seo`.
7. Integração segura com Supabase e base de dados SPITI.
8. Planejamento e execução futura de um site público próprio, substituindo ou complementando Artlogic.

---

## 4. Não-objetivos iniciais

Nesta implantação inicial do Paperclip, **não fazer**:

- Não enviar WhatsApp, email/newsletter, post no Instagram ou campanha paga sem aprovação humana explícita.
- Não mexer em `main`/produção do Spiti Hub sem PR/revisão.
- Não alterar Supabase produção sem migração revisada e rollback.
- Não trocar Artlogic imediatamente.
- Não criar campanhas pagas automaticamente no Meta/Google sem orçamento, público, criativo e copy aprovados.
- Não importar toda a base Tango/FileMaker dentro do Paperclip. O Paperclip orquestra o trabalho; o Hub/Supabase são a fonte operacional.
- Não duplicar o Hermes Brain: o Brain continua memória/procedimentos; Paperclip organiza empresa, agentes e tasks.

---

## 5. Company Paperclip inicial

### 5.1 Nome recomendado

**SPITI Auction Growth & Product OS**

Alternativas:

- `SPITI Auction AI Operating System`
- `SPITI Hub + Growth Studio`
- `SPITI Product, SEO & Growth`

Recomendação: usar o primeiro porque deixa claro que inclui produto + crescimento, sem restringir só marketing.

### 5.2 Texto para campo “Mission / goal” do Paperclip

Copiar/colar no onboarding:

```text
Build and operate SPITI Auction's AI-assisted product and growth organization. The company must safely improve Spiti Hub, grow qualified demand for SPITI through SEO/content/newsletter/paid-social creative, and prepare the future replacement or complement of the current Artlogic public site. All work must be traceable in issues, respect SPITI's premium art-auction brand voice, use verified data only, open GitHub PRs for code changes, and request Lucas approval before any external action such as customer contact, newsletter send, social post, paid campaign, production deploy, database migration, or budget-impacting decision.
```

Versão PT-BR, se o campo aceitar melhor em português:

```text
Construir e operar a organização de produto e crescimento assistida por IA da SPITI Auction. A empresa deve melhorar com segurança o Spiti Hub, aumentar demanda qualificada para a SPITI via SEO/conteúdo/newsletter/criativos para mídia paga, e preparar a futura substituição ou complemento do site público atual em Artlogic. Todo trabalho deve ser rastreável em issues, respeitar o tom premium da SPITI, usar apenas dados verificados, abrir PRs no GitHub para código, e pedir aprovação de Lucas antes de qualquer ação externa como contato com clientes, envio de newsletter, postagem social, campanha paga, deploy em produção, migração de banco ou decisão com impacto de orçamento.
```

---

## 6. Estrutura organizacional de agentes

### 6.1 Fase 1 — time mínimo viável

Criar poucos agentes primeiro. Evitar muitos heartbeats e ruído.

#### 1. CEO / Chief of Staff — `SPITI Chief of Staff`

- **Função:** priorizar, quebrar metas em projetos/issues, cobrar status, criar aprovações para decisões importantes.
- **Adapter recomendado:** `hermes_local` ou `codex_local`.
- **Por quê:** precisa de contexto, memória, leitura de docs, coordenação e capacidade de usar skills.
- **Heartbeat:** sem timer; wake on assignment/on demand.
- **Permissões:** pode propor contratações e criar tasks; não pode aprovar ações externas.
- **Budget mensal inicial:** moderado/alto, pois coordena tudo.

Instruções base:

```text
You are SPITI Chief of Staff. Convert Lucas' strategic goals into projects, issues, approval requests, and safe execution plans. You must enforce SPITI's rule: silence is better than wrong data. Never authorize external communications, customer outreach, paid ads, database writes, production deploys, or GitHub merges without Lucas approval. Keep work in small auditable issues and prefer PRs to direct changes.
```

#### 2. Product Engineer — `Spiti Hub Engineer`

- **Função:** melhorias do Spiti Hub, bugs, PRs, testes, lint/build, code review.
- **Adapter recomendado:** `codex_local` ou `hermes_local` com workdir do repo.
- **Projeto principal:** `Spiti Hub`.
- **Workspace:** clone do repo em branch feature a partir de `dev`.
- **Regras:** PR sempre para `dev`; nunca `main`; rodar lint/build/secret scan; não mexer Supabase/Vercel/prod sem aprovação.

Instruções base:

```text
Work on the private repository spiti-auction/spiti-hub using feature branches from dev and PRs back to dev. Never push to main. Before PR, run git diff --check, secret scan, npm run lint --if-present, and npm run build. Treat migrations, auth, Supabase client, Vercel config, GitHub Actions, billing, campaigns, and external communications as high-risk and request approval.
```

#### 3. SEO Strategist — `SPITI SEO Strategist`

- **Função:** auditoria SEO, arquitetura de conteúdo, calendário editorial, schema, GSC/GA4, plano site novo.
- **Adapter recomendado:** `claude_local` com `claude-seo` instalado OU `codex_local` com `codex-seo`.
- **Skills:** `seo-plan`, `seo-audit`, `seo-content`, `seo-google`, `seo-schema`, `seo-geo`, `seo-technical`.
- **Heartbeat:** rotinas semanais/mensais, não intervalo constante.
- **Saídas:** briefs, outlines, calendário, tickets de implementação, relatórios.

#### 4. Content Editor — `SPITI Editorial Producer`

- **Função:** transformar brief SEO + dados verificados em post de blog, meta title, meta description, FAQ, schema, newsletter draft.
- **Tom:** sofisticado, cultural, premium; sem hard-sell; sem inventar proveniência, preço, biografia ou dados de leilão.
- **Approval:** todo conteúdo externo exige aprovação Lucas antes de publicação/envio.

#### 5. Creative Performance Designer — `SPITI Paid Social Creative`

- **Função:** gerar conceitos e prompts para arte de Instagram/tráfego pago, variações de copy, briefing visual, checklist de asset.
- **Ferramentas possíveis:** Paperclip + agente com image generation/banana ou Hermes `image_generate`, mas sempre como **draft**.
- **Approval:** nenhum criativo vai para campanha/post sem revisão humana.

#### 6. Analytics Analyst — `SPITI Analytics Analyst`

- **Função:** GA4, GSC, Search Console, PageSpeed/CrUX, funil orgânico, relatórios semanais/mensais.
- **Skills:** `seo-google` e scripts GA4/GSC.
- **Dados:** só reportar dados coletados via API/exports verificados; se credencial faltante, gerar checklist de acesso.

### 6.2 Fase 2 — agentes opcionais

Depois de estabilizar a Fase 1:

- **Newsletter Manager**: MailerLite, segmentação, calendário, templates, testes A/B.
- **Supabase Data Engineer**: schema, RLS, views, functions, importações, qualidade de dados.
- **Site Architect**: arquitetura e implementação do futuro site público SPITI.
- **Ads Ops Analyst**: Meta Ads/Google Ads; inicialmente só análises e drafts de campanha.
- **Art Catalog Researcher**: apoio editorial/curatorial; precisa de regras rígidas de fonte e revisão humana.

---

## 7. Projetos Paperclip recomendados

Criar estes projetos dentro da Company:

### P1. Spiti Hub — Produto & Engenharia

- **Descrição:** desenvolvimento seguro do Spiti Hub.
- **Repo:** `spiti-auction/spiti-hub`.
- **Branch base:** `dev`.
- **Agentes:** Chief of Staff, Spiti Hub Engineer, Supabase Data Engineer.
- **Definition of Done:** PR aberto/mergeado em `dev`, lint/build OK, sem secrets, sem impacto externo não aprovado.

Backlog inicial:

- Criar inventário atualizado de módulos e gaps do Spiti Hub.
- Checar PRs recentes e estado de `dev`.
- Criar mapa Supabase/migrations/RLS.
- Criar issues da próxima onda do Hub.
- Preparar governança de PRs para agentes Paperclip.

### P2. SPITI SEO & Content Engine

- **Descrição:** operação SEO, blog posts, topical authority e GEO/AEO.
- **Site atual:** `https://www.spiti.art` (Artlogic).
- **Site futuro:** a definir.
- **Agentes:** SEO Strategist, Content Editor, Analytics Analyst.
- **Skills:** `claude-seo`/`codex-seo`.
- **Outputs:** auditoria, strategy, calendário, briefs, posts, schema, relatórios.

Backlog inicial:

- Rodar auditoria SEO do site atual `spiti.art`.
- Configurar leitura GSC/GA4 se credenciais existirem.
- Definir pilares editoriais: artistas, leilões, guias de compra/venda, mercado de arte, bastidores curatoriais.
- Criar calendário editorial de 90 dias.
- Criar template de blog post SPITI com E-E-A-T e citability.
- Definir processo de revisão curatorial antes de publicação.

### P3. SPITI Newsletter & CRM Activation

- **Descrição:** newsletter editorial e comercial com MailerLite, usando dados de CRM/Hub com aprovação humana.
- **Agentes:** Newsletter Manager, Content Editor, Analytics Analyst.
- **Integrações:** MailerLite, Supabase, eventualmente GA4/GSC.
- **Outputs:** drafts, segmentação, calendário, relatório pós-envio.

Backlog inicial:

- Validar credenciais MailerLite no Doppler.
- Mapear listas/grupos atuais.
- Criar template editorial premium.
- Criar rotina de newsletter mensal/quinzenal.
- Criar checklist de aprovação antes de envio.

### P4. SPITI Paid Social Creative Studio

- **Descrição:** conceitos, copies e artes para Instagram/Meta Ads.
- **Agentes:** Creative Performance Designer, Ads Ops Analyst.
- **Outputs:** briefs, prompts, variações, assets em rascunho, plano de testes.
- **Guardrail:** nunca subir campanha ou gastar verba sem approval.

Backlog inicial:

- Criar guia visual para assets SPITI.
- Criar 10 conceitos de campanha para captação de consignantes.
- Criar 10 conceitos para preview/leilão.
- Criar matriz de formatos: feed 1:1, stories 9:16, reels cover, ads 4:5.
- Criar naming convention e checklist de aprovação.

### P5. SPITI Analytics & Growth Intelligence

- **Descrição:** dados de GA4, GSC, Search Console, PageSpeed, CrUX, funis, dashboards e insights.
- **Agentes:** Analytics Analyst, SEO Strategist.
- **Outputs:** relatórios, alertas, dashboards, recomendações.

Backlog inicial:

- Configurar GSC property.
- Configurar GA4 property.
- Criar relatório semanal orgânico: cliques, impressões, CTR, posição, páginas, queries.
- Criar relatório mensal: tráfego orgânico, conversões, páginas de entrada, oportunidades.
- Criar baseline Core Web Vitals.

### P6. Future SPITI Public Site

- **Descrição:** planejamento do site próprio para substituir/complementar Artlogic.
- **Agentes:** Site Architect, SEO Strategist, Product Engineer, Content Editor.
- **Outputs:** PRD, arquitetura, sitemap, stack, design brief, migração gradual.

Backlog inicial:

- Auditar limitações atuais do Artlogic.
- Definir escopo do site público: institucional, catálogo, blog, artista, leilões, SEO, captação.
- Decidir stack: Vercel/Next.js + Supabase? reaproveitar Spiti Hub? site separado?
- Criar sitemap ideal e estratégia de migração.
- Definir canonical/redirect plan para não perder SEO.

---

## 8. Rotinas Paperclip recomendadas

Regra: evitar heartbeat de poucos minutos. Usar rotinas agendadas e event-driven.

### R1. Weekly Spiti Hub Triage

- **Frequência:** segunda-feira 09:00.
- **Agente:** Chief of Staff + Product Engineer.
- **Objetivo:** revisar PRs/issues, estado do `dev`, riscos, próximos tickets.
- **Saída:** resumo + backlog priorizado + approvals necessários.

### R2. Weekly SEO Opportunity Scan

- **Frequência:** terça-feira 09:00.
- **Agente:** SEO Strategist.
- **Objetivo:** revisar GSC/GA4, queries com impressões altas/CTR baixa, páginas em queda, oportunidades de conteúdo.
- **Saída:** 3–5 oportunidades priorizadas.

### R3. Monthly SEO Audit Lite

- **Frequência:** primeiro dia útil do mês.
- **Agente:** SEO Strategist + Analytics Analyst.
- **Objetivo:** PageSpeed/CrUX, indexação, sitemap, schema, principais páginas.
- **Saída:** relatório mensal com ações.

### R4. Editorial Calendar Planning

- **Frequência:** quinzenal.
- **Agente:** Content Editor + SEO Strategist.
- **Objetivo:** planejar blog/newsletter próximos 30 dias.
- **Saída:** calendário, briefs e drafts.

### R5. Paid Social Creative Sprint

- **Frequência:** semanal ou por campanha.
- **Agente:** Creative Performance Designer.
- **Objetivo:** gerar conceitos de criativos, hooks, copies e prompts.
- **Saída:** pacote de rascunhos para aprovação.

### R6. Newsletter Draft Review

- **Frequência:** mensal/quinzenal conforme estratégia.
- **Agente:** Newsletter Manager + Content Editor.
- **Objetivo:** produzir draft e segmentação; criar approval para Lucas.
- **Saída:** preview, assunto, preheader, segmentos, riscos.

---

## 9. Integrações e credenciais

### 9.1 Doppler como fonte de verdade

Manter padrão atual: Doppler `lc-keys/prd` é fonte de verdade. Não colar tokens em chat. Não imprimir secrets.

Credenciais esperadas/possíveis:

- GitHub SPITI: `GITHUB_SPITI_HUB_TOKEN` já existe em Doppler, mas foi colado em chat no passado; considerar rotação futura.
- Supabase SPITI: URL, anon key, service role (service role só em ambientes seguros/edge/server, nunca frontend/agente sem escopo).
- MailerLite: API key/list IDs.
- Google:
  - GSC property / service account / OAuth.
  - GA4 property ID.
  - PageSpeed API key.
  - Google Ads developer token e customer ID, se usar Keyword Planner/Ads.
- Meta Ads:
  - `META_ACCESS_TOKEN`
  - `META_AD_ACCOUNT_ID`
  - permissões de Custom Audience/campaigns.
- Anthropic/OpenAI/Codex, conforme adapter.
- Firecrawl/DataForSEO, se for usar auditoria SEO mais robusta.

### 9.2 Integração GitHub

- Paperclip agent de engenharia deve trabalhar via feature branch e PR.
- Base branch: `dev`.
- `main` é produção.
- GitHub remote sem token embutido.
- PR checklist obrigatório:
  - `git diff --check`
  - secret scan
  - `npm run lint --if-present`
  - `npm run build`
  - revisar mudanças sensíveis.

### 9.3 Integração Supabase

- Para leitura analítica: usar views/RPC com permissões mínimas.
- Para escrita/migration: sempre via PR + review + rollback.
- Separar chaves:
  - anon/front-safe.
  - service role só server-side e com approval.
- Criar views para analytics/marketing em vez de dar acesso bruto irrestrito.

### 9.4 Integração MailerLite

- Primeiro estágio: Paperclip gera **draft** de newsletter e plano de segmento.
- Segundo estágio: integração lê listas e cria campanha rascunho.
- Terceiro estágio: envio só após approval Lucas.

### 9.5 Integração GA4/GSC

- Inicialmente read-only.
- Relatórios semanais/mensais.
- Integrar com `seo-google` ou scripts próprios.
- Criar baseline antes de mudanças de site.

### 9.6 Integração Artlogic / site público atual

- Tratar Artlogic como site público vigente.
- Primeiro: auditoria e conteúdo off-platform/manual.
- Futuro: site próprio com migração controlada.
- Qualquer migração precisa plano de canonical, redirects, sitemap, robots, schema e QA.

---

## 10. Processo de conteúdo SEO

### 10.1 Fluxo end-to-end

1. Analytics/SEO identifica oportunidade.
2. SEO Strategist cria brief:
   - keyword/intent
   - público
   - ângulo SPITI
   - fontes necessárias
   - estrutura H1/H2/H3
   - schema recomendado
   - links internos
   - meta title/description
3. Content Editor cria draft.
4. Revisão de factualidade:
   - artistas, datas, preços, leilões, proveniência e dados de mercado precisam fonte.
   - se não houver fonte, marcar como pendente.
5. Lucas aprova.
6. Implementação/publicação conforme stack atual ou futura.
7. Analytics acompanha performance.

### 10.2 Pilares editoriais iniciais

- **Comprar arte em leilão**: guias para novos compradores, comissão, lances, retirada, pagamento.
- **Vender/consignar arte**: como funciona avaliação, captação, consignação, exposição.
- **Artistas e movimentos**: perfis curatoriais, sempre com fontes e linguagem premium.
- **Mercado de arte brasileiro**: tendências, educação, contexto cultural.
- **Bastidores SPITI**: montagem, preview, leilão presencial/online, catalogação.
- **Colecionismo**: conservação, documentação, certificado, composição de acervo.
- **Pós-leilão**: oportunidades, vendas diretas, obras remanescentes.

### 10.3 Template de qualidade para post

- Título claro e editorial, sem clickbait.
- Lead com resposta direta ao intent.
- Autor/revisor identificável quando possível.
- Fontes e links externos confiáveis.
- Fotos/obras com direitos verificados.
- JSON-LD: Article/FAQ/Breadcrumb conforme caso.
- Metadados: title, description, OG image, canonical.
- CTA sutil: conhecer próximos leilões, falar com especialista, consignar obra.

---

## 11. Processo de criativos para tráfego pago

### 11.1 Fluxo

1. Brief de campanha: objetivo, público, promessa, verba, canal, datas.
2. Creative Designer gera conceitos e variações.
3. Lucas aprova direção.
4. Produção de assets finais.
5. Ads Ops configura campanha rascunho.
6. Lucas aprova campanha/verba/envio.
7. Publicação.
8. Analytics reporta performance.

### 11.2 Famílias de criativo

- Captação de obras/consignantes.
- Divulgação de leilão futuro.
- Preview/exposição presencial.
- Destaques de artistas/lotes.
- Educação para novos compradores.
- Pós-leilão/venda direta.
- Institucional/premium brand.

### 11.3 Guardrails visuais e de copy

- Não prometer valorização/investimento garantido.
- Não usar preço/lance sem fonte confirmada.
- Não usar obra/imagem sem direito de uso.
- Não falar “última chance”/hard-sell agressivo fora do tom SPITI.
- Preferir sofisticação, contexto cultural, confiança e exclusividade discreta.

---

## 12. Site novo — visão inicial

A SPITI hoje usa Artlogic. O Paperclip deve apoiar o planejamento de um site próprio, mas isso é um projeto separado e precisa discovery.

### 12.1 Perguntas de discovery

- O site novo substitui Artlogic totalmente ou complementa?
- O catálogo/leilão público fica no Spiti Hub, no site novo ou segue no LeilõesBR/Artlogic?
- O site precisa login de cliente?
- Precisa blog nativo?
- Precisa páginas de artistas?
- Precisa páginas indexáveis de leilões passados/lotes vendidos?
- Como preservar URLs/canonicals atuais?
- Quem publica conteúdo hoje e com qual fluxo de aprovação?

### 12.2 Recomendação preliminar

- Criar site público separado do Hub interno, possivelmente Next.js/Vercel, consumindo dados publicados do Supabase/Hub por views/API seguras.
- Hub continua sistema interno/backoffice.
- Site público consome apenas dados aprovados/publicáveis.
- Blog/SEO devem nascer já com schema, sitemap, imagens otimizadas, CMS ou MDX controlado.

---

## 13. Governança e approvals

### 13.1 Sempre exige aprovação Lucas

- Envio de WhatsApp, email, newsletter ou campanha.
- Postagem ou agendamento em Instagram/social.
- Criação/ativação de campanha paga.
- Alteração de orçamento.
- Deploy em produção.
- Merge para `main`.
- Migração Supabase ou alteração RLS.
- Uso de service role ou export de dados pessoais.
- Acesso/uso de lista de clientes para targeting.
- Publicação de conteúdo factual sobre artista/obra/leilão sem revisão.
- Alteração em Artlogic/site público live.

### 13.2 Pode ser automático com logs

- Criar issues internas.
- Gerar drafts.
- Rodar auditorias read-only.
- Rodar lint/build/test local.
- Abrir PR para `dev` com checklist.
- Gerar relatórios read-only.
- Criar propostas de segmentação sem envio.

### 13.3 Política LGPD/dados

- Usar dados pessoais apenas para finalidade legítima de CRM/marketing SPITI.
- Preferir dados agregados em relatórios.
- Hash email/telefone para Customer Match/Custom Audiences.
- Manter opt-out/descadastro.
- Registrar quem aprovou envio/campanha.

---

## 14. Métricas de sucesso

### 14.1 Operacionais

- 100% das ações de agentes rastreadas em issues/PRs.
- 0 ação externa sem approval.
- Tempo de triagem semanal do Spiti Hub reduzido.
- Ciclo de PR do Hub mais previsível.

### 14.2 Produto/engenharia

- Lint/build sempre OK em PRs.
- Redução de bugs regressivos.
- Roadmap Spiti Hub mais claro e atualizado.
- Migrações Supabase documentadas e reversíveis.

### 14.3 SEO/conteúdo

- Baseline GSC/GA4 estabelecido.
- Calendário editorial de 90 dias criado.
- Publicar X posts/mês após aprovação.
- Melhorar CTR orgânico em queries com alta impressão.
- Crescer páginas indexadas de qualidade.
- Melhorar Core Web Vitals no site futuro.

### 14.4 Newsletter/CRM

- Primeira newsletter enviada com tracking e approval.
- Taxa de abertura/click estabelecida como baseline.
- Segmentos CRM definidos sem duplicidade.

### 14.5 Paid social

- Biblioteca de criativos e prompts criada.
- Campanhas com naming convention.
- Relatório de desempenho por criativo.

---

## 15. Roadmap de implantação

### Semana 0 — Setup seguro

- Criar Company no Paperclip.
- Inserir missão.
- Criar Chief of Staff e Product Engineer.
- Criar projetos P1–P6.
- Importar ou documentar skills essenciais.
- Definir budgets baixos/moderados.
- Desligar timer heartbeats por padrão.
- Criar guardrails/approvals.

### Semana 1 — Engenharia + SEO baseline

- Conectar Spiti Hub repo ao projeto Paperclip.
- Validar fluxo PR para `dev`.
- Criar auditoria SEO inicial do `spiti.art`.
- Mapear credenciais GSC/GA4 disponíveis.
- Criar backlog de quick wins.

### Semana 2 — Conteúdo e newsletter

- Criar calendário editorial 90 dias.
- Criar 3 briefs de blog.
- Criar 1 newsletter draft.
- Validar MailerLite read-only/draft.
- Criar template editorial SPITI.

### Semana 3 — Criativos e analytics

- Criar guia de assets pagos.
- Gerar 10 conceitos de campanha.
- Criar relatório semanal GA4/GSC.
- Definir dashboards e KPIs.

### Semana 4 — Site futuro discovery

- Auditar Artlogic.
- Criar PRD do site público.
- Definir arquitetura preliminar.
- Criar plano SEO de migração.

### 30–90 dias

- Operação recorrente de rotinas.
- Produção de conteúdo aprovada.
- PRs incrementais no Hub.
- Primeiras campanhas/newsletters com approval.
- Roadmap do site novo pronto para execução.

---

## 16. Configuração inicial sugerida no Paperclip

### Company

- Name: `SPITI Auction Growth & Product OS`
- Mission: usar texto da seção 5.2.
- Budget mensal: começar conservador e ajustar após 2 semanas.
- Require board approval for new agents: **on**.

### Agent inicial

- First agent: `SPITI Chief of Staff`
- Role: CEO/Chief of Staff.
- Adapter: idealmente `hermes_local` se Paperclip estiver no mesmo ambiente com Hermes disponível; alternativamente `codex_local`/`claude_local`.
- Heartbeat interval: off.
- Wake on demand: on.
- Can create agents: pode propor, mas hires por approval.

### Skills iniciais

- Internas SPITI:
  - `spiti-brand-voice`
  - `spiti-data-safety`
  - `spiti-hub-pr-workflow`
  - `spiti-content-factuality-check`
- Externas SEO:
  - `claude-seo` ou `codex-seo`
  - foco: `seo-plan`, `seo-audit`, `seo-content`, `seo-google`, `seo-schema`, `seo-geo`, `seo-technical`, `seo-image-gen` se disponível.

### Projects

Criar P1–P6 da seção 7.

### Routines

Criar R1–R6 da seção 8, inicialmente pausadas ou com baixa frequência. Ativar uma por vez.

---

## 17. Primeiras tasks para abrir no Paperclip

1. `Create SPITI operating guardrails skill`
   - Output: skill com regras de approval, tom, dados e PR.

2. `Audit current spiti.art SEO baseline`
   - Output: relatório técnico + oportunidades.

3. `Create 90-day SPITI SEO content calendar`
   - Output: calendário com pilares, keywords, intents e prioridade.

4. `Create Spiti Hub agent PR workflow`
   - Output: checklist e teste de PR pequeno para `dev`.

5. `Map Google Analytics/Search Console access`
   - Output: credenciais necessárias e status sem expor secrets.

6. `Draft first SPITI newsletter template`
   - Output: HTML/text draft + assunto/preheader + approval request.

7. `Create paid social creative system v1`
   - Output: formatos, prompts, estilo, naming, approval checklist.

8. `Discovery: future SPITI public website`
   - Output: perguntas respondidas, sitemap ideal, riscos de migração.

---

## 18. Riscos e mitigação

### Risco: agentes enviarem comunicação externa indevida

Mitigação:

- Approval obrigatório.
- Skills de guardrail.
- MailerLite/Meta/WhatsApp inicialmente só draft/read-only.

### Risco: dado falso sobre obra, artista, preço ou lance

Mitigação:

- Regra “silêncio > dado errado”.
- Exigir fonte explícita.
- Campos pendentes em vez de afirmação.
- Revisão humana em conteúdo externo.

### Risco: Paperclip gerar ruído/custo com muitos heartbeats

Mitigação:

- Timer off por padrão.
- Routines programadas.
- Budgets por agente.
- Começar com poucos agentes.

### Risco: alteração acidental em produção

Mitigação:

- PR para `dev`.
- `main` bloqueado por política.
- Approval para deploy/prod.
- Secret scan e build obrigatórios.

### Risco: acesso excessivo a dados pessoais

Mitigação:

- Read-only por padrão.
- Views segmentadas.
- Hash para ads.
- Logs de approval.

### Risco: site novo quebrar SEO existente

Mitigação:

- Auditoria baseline.
- Plano de redirects/canonicals.
- Migração gradual.
- Monitoramento GSC pós-migração.

---

## 19. Decisões em aberto para Lucas

1. Company única ou múltiplas Companies?
   - Recomendação inicial: **uma Company única** com múltiplos projetos, porque todos os fluxos se conectam.

2. Adapter principal:
   - Hermes Local, Codex Local, Claude Local ou mix?
   - Recomendação: Chief of Staff em Hermes Local; engenharia em Codex/Hermes; SEO em Claude/Codex com skill SEO.

3. Paperclip já está instalado onde?
   - Local, VPS, Docker, LK Sneakers? Precisamos saber para replicar/isolá-lo para SPITI.

4. SPITI deve ter Paperclip separado da LK Sneakers?
   - Recomendação: sim, separar Company/tenant e secrets; idealmente até instância separada se houver risco de mistura.

5. Site novo:
   - Substituir Artlogic totalmente ou começar com blog/landing paralelo?

6. Newsletter:
   - Frequência inicial mensal ou quinzenal?

7. Aprovação:
   - Quem além de Lucas pode aprovar conteúdo/campanhas?

---

## 20. Próxima ação recomendada agora

Na tela do Paperclip mostrada pelo Lucas, preencher:

- **Company name:** `SPITI Auction Growth & Product OS`
- **Mission / goal:** usar o texto PT-BR ou EN da seção 5.2.

Depois clicar **Next** e criar o primeiro agente:

- **Agent name:** `SPITI Chief of Staff`
- **Title:** `CEO / Chief of Staff`
- **Role:** CEO
- **Adapter:** a definir conforme ambiente disponível, preferencialmente `hermes_local` se Paperclip conseguir acessar Hermes; caso contrário `codex_local`/`claude_local`.

Assim que a Company existir, a próxima etapa é criar os projetos P1–P6 e importar/escrever as skills de guardrail da SPITI.
