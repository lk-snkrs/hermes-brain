# PRD — Mission Control Hermes-native / COO Cockpit

Data: 2026-05-17  
Owner: Lucas Cimino  
Produto: Hermes Agent / Hermes Brain / Ecossistema Lucas Cimino  
Status: PRD v1 completo para construção do zero  
Decisão estratégica: abandonar Tenacity OS / TenacitOS como base de longo prazo e construir uma superfície Hermes-native, aprendendo com `outsourc-e/hermes-workspace` sem copiar sua arquitetura de alto risco.

---

## 1. Resumo executivo

O Mission Control Hermes-native será o cockpit de COO do ecossistema Lucas Cimino.

Ele não é apenas um dashboard técnico, nem apenas um chat. Ele deve ser a camada executiva acima da Grande Mente Hermes Brain, mostrando:

- o que está acontecendo em cada empresa;
- o que foi feito;
- o que falta fazer;
- o que está bloqueado;
- quais decisões Lucas precisa tomar;
- quais rotinas estão vivas;
- quais dados estão frescos ou quebrados;
- quais oportunidades comerciais existem;
- quais ações são seguras para Hermes executar sozinho;
- quais ações exigem aprovação explícita.

A hierarquia canônica é:

```text
Hermes Brain / Grande Mente / COO
├── Lucas pessoal
├── LK OS — LK Sneakers
├── Zipper OS — Zipper Galeria
├── SPITI OS — SPITI Auction
├── Professor Bruno / material adaptável
├── Operações / Tecnologia / Governança
└── Integrações transversais
```

O Mission Control deve ser o painel dessa Grande Mente, não uma coleção solta de cards por empresa.

---

## 2. Decisão de produto

### 2.1 O que foi decidido

Construir do zero a opção 1: um Mission Control próprio, Hermes-native, sob medida para Lucas.

### 2.2 O que não será mais usado como base

Tenacity OS / TenacitOS / Tenacitas não deve ser a base de evolução.

Motivo:

- foi desenhado para OpenClaw/Tenacitas;
- assume diretórios, comandos e rotas que não representam o Hermes real;
- corrigi-lo gera superfície bonita mas semanticamente falsa;
- aumenta risco de UI dizer “funciona” enquanto a operação Hermes real está em outro lugar.

### 2.3 O que será aproveitado do Hermes Workspace

O repositório `outsourc-e/hermes-workspace` foi clonado localmente em:

```text
/opt/data/research/hermes-workspace
```

Ele será usado como referência de produto, não como dependência central.

Aprendizados a aproveitar:

1. Chat com streaming e renderização de tool calls.
2. Sessões e histórico navegáveis.
3. Browser/editor de memória.
4. Browser/gestor de skills.
5. Jobs/crons em UI.
6. MCP como catálogo/configuração.
7. Files + Monaco editor.
8. Terminal web / PTY — mas no nosso caso não expor por padrão em produção.
9. Dashboard agregado de sessões/modelos/custo/atenção.
10. Operations / Conductor como missão, decomposição e despacho.
11. Agent View com estado, fila, histórico e uso.
12. Swarm Mode com workers persistentes, roster por papel, Kanban, relatórios e checkpoints.
13. Capability gates: se algo não está configurado, mostrar “precisa configurar”, não quebrar.
14. Segurança: auth em todas as rotas, CSP, proteção path traversal, fail-closed em bind remoto.
15. PWA/mobile-first.

Coisas a adaptar do nosso jeito:

- Trocar “workspace genérico para Hermes” por “COO cockpit multiempresa”.
- Priorizar Lucas Queue, decisões, dados, fontes e aprovações, não terminal.
- Criar visões por empresa e braço operacional.
- Integrar analytics reais por empresa.
- Separar fato, interpretação, recomendação e ação.
- Usar Hermes Brain como fonte de verdade operacional.
- Preservar guardrails: nada externo ou produtivo sem aprovação atual.

Coisas a evitar do Hermes Workspace em produção inicial:

- terminal web irrestrito;
- file browser amplo sobre `/opt/data`;
- escrita direta em memória/skills sem revisão;
- controle de crons/jobs com botão destrutivo;
- conexão pública direta ao API server Hermes;
- montar runtime produtivo completo antes de QA.

---

## 3. Problema

Lucas opera LK, Zipper, SPITI, rotinas pessoais, projetos de tecnologia, scripts, crons, integrações e Hermes Brain. O Brain já contém muito conhecimento, mas a operação ainda exige navegar muitos arquivos, relatórios e conversas.

O problema central não é falta de informação. É falta de uma camada de decisão.

Hoje, as perguntas executivas são difíceis de responder rapidamente:

- O que cada empresa está tentando fazer agora?
- Quais frentes já foram feitas?
- O que falta do PRD?
- O que está bloqueado por dados, aprovação, API, fornecedor, time ou decisão?
- Que analytics importam para cada braço?
- O que está acontecendo em Google Merchant Center, SEO, CRO, campanhas, CRM e estoque?
- Quais rotinas estão realmente ativas e quais são só docs?
- O que Hermes pode executar sozinho?
- O que precisa de aprovação do Lucas?
- O que aprendeu com uma correção do Lucas e virou regra permanente?

O Mission Control deve responder isso em 30 segundos.

---

## 4. Objetivo do produto

Criar um cockpit executivo Hermes-native que transforme o Hermes Brain e as integrações em gestão diária.

Objetivos principais:

1. Dar a Lucas uma visão clara de toda a operação.
2. Separar empresas, fontes, responsabilidades e riscos.
3. Mostrar progresso real: feito, em execução, falta, bloqueado.
4. Centralizar a Lucas Queue: decisões pendentes, impacto e recomendação.
5. Expor analytics por empresa e por braço operacional.
6. Mostrar saúde de dados: frescor, confiança, fonte e lacunas.
7. Tornar o Approval Manager visível e auditável.
8. Transformar PRDs em execução rastreável.
9. Permitir despacho de tarefas Hermes com segurança e evidência.
10. Evitar qualquer ação externa/produtiva sem aprovação explícita.

---

## 5. Princípios de produto

### 5.1 COO first

A interface deve pensar como COO, não como painel técnico.

Toda tela deve responder:

- qual decisão isso ajuda Lucas a tomar?
- qual risco isso reduz?
- qual receita, eficiência ou qualidade isso melhora?
- qual fonte sustenta essa recomendação?
- qual próximo passo seguro?

### 5.2 Brain as source of truth

O Mission Control não substitui o Brain. Ele lê, resume, roteia e cria evidência.

Fontes de verdade continuam em:

- `hermes-brain/areas/*`
- skills canônicas
- reports auditáveis
- scripts read-only
- crons reais
- APIs quando usadas em modo seguro

### 5.3 Separação entre camadas

Cada item precisa distinguir:

```text
Fato verificado
→ interpretação
→ recomendação
→ ação possível
→ aprovação necessária
→ evidência
```

### 5.4 Read-only primeiro

Toda integração nova entra primeiro como leitura, snapshot e relatório.

Writes só depois de:

- preview;
- escopo exato;
- backup/rollback quando aplicável;
- aprovação Lucas no turno atual;
- verificação pós-ação.

### 5.5 Mobile-first e Telegram-compatible

Lucas deve conseguir usar no celular.

Todo card deve gerar uma versão Telegram curta:

- decisão;
- impacto;
- recomendação;
- aprovação necessária;
- link/evidência.

### 5.6 Guardrails visíveis

A UI deve mostrar o que Hermes não pode fazer sozinho:

```text
Sem WhatsApp/e-mail externo, sem Shopify/Tiny/Merchant/ads, sem Docker/VPS/Traefik/DNS, sem banco produtivo e sem cron novo sem aprovação explícita, escopo, backup e rollback quando aplicável.
```

---

## 6. Usuários e papéis

### 6.1 Lucas

Decisor executivo. Vê status, aprova, bloqueia, prioriza e corrige.

### 6.2 Hermes COO

Camada de raciocínio e orquestração. Lê o Brain, interpreta dados, prepara decisões e despacha tarefas seguras.

### 6.3 Workers Hermes

Inspirado no Hermes Workspace swarm, mas adaptado ao ecossistema Lucas:

- Orchestrator / COO: decomposição, decisões, roteamento e approval gates.
- Data Steward: saúde de fontes, frescor, schema, reconciliação.
- LK Analyst: ecommerce, estoque, GMC, SEO, CRO, CRM, campanhas.
- Zipper Analyst: colecionadores, vendas, feiras, conteúdo, logística.
- SPITI Analyst: leilão, lotes, lances, hub, relatórios.
- Ops Watch: crons, runtime, health, segurança.
- Reviewer: revisão de PR/plano/risco.
- QA: verificação visual, rota, console, smoke test.

### 6.4 Times externos / internos

Aparecem como owners, não como usuários diretos no MVP:

- LK: Renan, Júlio, Danilo, Pareto, FHITS.
- Zipper: Osmar, Helo, Biz, Mie, Cibele, Panda.
- SPITI: equipe de leilão/operação.

---

## 7. Escopo V1

O V1 deve entregar uma versão executiva e segura de Mission Control em `mission.lucascimino.com`, substituindo a base Tenacity por base própria.

### 7.1 Telas V1

1. Grande Mente / Home COO
2. Lucas Queue
3. Multiempresa Map
4. LK OS Cockpit
5. Zipper OS Cockpit
6. SPITI OS Cockpit
7. Analytics Hub
8. Approval Center
9. Routines & Cron Registry
10. Data Sources & Freshness
11. Hermes Operations
12. PRD Execution Board
13. Workspace Learnings / Agent Roster

### 7.2 Funcionalidade V1

- Dashboard estático/dinâmico híbrido: começa com dados do Brain e artefatos versionados.
- Cards com status: `feito`, `em execução`, `falta`, `bloqueado`, `aguarda Lucas`, `monitorar`.
- Lucas Queue com prioridade, impacto, recomendação e gate.
- Mapa de fontes por empresa.
- Matriz de analytics por braço operacional.
- Registro de rotinas ativas vs documentadas.
- Registro de aprovações e ações bloqueadas.
- Version marker obrigatório no HTML para verificação.
- Sem terminal web produtivo no V1.
- Sem writes em plataformas no V1.

---

## 8. Fora de escopo V1

O V1 não deve:

- enviar e-mail, WhatsApp, campanha, proposta ou mensagem externa;
- alterar Shopify, Tiny, Merchant Center, Google Ads, Meta, Klaviyo, Supabase, Notion ou banco produtivo;
- criar/reiniciar crons;
- reiniciar Docker/gateway/VPS/Traefik;
- expor terminal web irrestrito;
- expor file browser amplo de `/opt/data`;
- conectar diretamente API Server Hermes público;
- substituir Telegram como canal de aprovação;
- automatizar compra, sourcing, fornecedor ou cliente;
- tomar decisão de preço, desconto, lance, proposta ou publicação sem aprovação.

---

## 9. Estrutura de informação

### 9.1 Home — Grande Mente / COO Inbox

Objetivo: visão geral em uma tela.

Blocos:

- Status geral do ecossistema.
- Lucas Queue top 5.
- Alertas críticos.
- Rotinas rodando hoje.
- Empresas com mudança relevante.
- Próximo bloco recomendado.
- Guardrails visíveis.

### 9.2 Lucas Queue

Cada decisão deve ter:

- título;
- empresa/área;
- impacto;
- urgência;
- contexto curto;
- recomendação Hermes;
- opções de decisão;
- aprovação necessária;
- fonte/evidência;
- risco se adiar.

Tipos de decisão:

- aprovar execução;
- pedir mais dados;
- rejeitar;
- deixar em monitoramento;
- transformar em rotina;
- transformar em PR/issue;
- delegar a time externo.

### 9.3 Multiempresa Map

Cada empresa terá linhas:

- Feito
- Em execução
- Falta
- Bloqueado
- Próxima ação segura
- Dono humano / dono Hermes

### 9.4 PRD Execution Board

Cada PRD vira board com:

- objetivos;
- fases;
- status;
- entregáveis;
- lacunas;
- evidência;
- próximo passo;
- dependências;
- ações bloqueadas.

PRDs iniciais:

- LK OS PRD;
- Zipper OS PRD;
- SPITI OS / Spiti Hub;
- Mordomo pessoal;
- Mission Control Hermes-native;
- Company Decision Memory.

---

## 10. Analytics por empresa e braço operacional

### 10.1 Analytics globais da Grande Mente

Métricas:

- decisões abertas por empresa;
- decisões vencidas;
- ações bloqueadas por aprovação;
- rotinas ativas;
- rotinas documentadas sem execução confirmada;
- fontes stale;
- incidentes de dados;
- PRDs com lacuna crítica;
- tarefas read-only prontas para executar;
- tarefas que exigem Lucas.

### 10.2 LK OS — Analytics

Fontes canônicas:

- Shopify: vendas, pedidos, clientes, catálogo, tags, source context.
- Tiny `LK | CONTROLE ESTOQUE`: verdade de estoque.
- GA4 `348553567`: tráfego, funil, CRO, PDP/landing.
- Search Console: SEO orgânico.
- Google Merchant Center / Content API: feed, product status, GMC issues.
- Google Ads / Metricool: sinais pagos e social/ads.
- Meta Ads `act_1242062509867163`: plataforma de mídia, criativos, ad_name/ad_id.
- Pareto: paid traffic / tráfego pago.
- FHITS: influencers.
- Klaviyo: CRM/e-mail/drafts.
- Judge.me/Rivo/Frenet: reviews, loyalty, logística quando retomado.
- Notion / Júlio: compras/sourcing manual.

Braços LK e analytics:

#### Ecommerce / Shopify

- Receita por período.
- Pedidos por canal.
- Ticket médio.
- Produtos mais vendidos.
- Produtos com tráfego alto e baixa venda.
- PDPs com baixa conversão.
- Coleções com oportunidade.
- SKUs sem padrão.
- Produtos sem SEO adequado.
- Produtos sem imagem/descrição/tag correta.

#### Estoque / Tiny / Sourcing

- Ruptura por SKU/tamanho.
- Baixo estoque.
- Estoque físico vs livre vs reservado/encomenda.
- Shopify SKU ↔ Tiny code match.
- Fila Júlio: produto, tamanho, demanda, preço site LK, custo alvo, fonte Droper/StockX/GOAT.
- Lead time real por fonte quando disponível.
- Oportunidade de recompra/reposição.

#### GMC / Merchant Center

- Produtos aprovados/reprovados por destino.
- Issues por severidade.
- `price_updated`, `strikethrough_price_updated`, landing/crawl, identifiers, attributes.
- Distinção online vs local/LIA.
- ProductInput vs Shopify visible title.
- Feed/source ownership.
- Último pacote aplicado, rollback e verificação.
- Próximos candidates com approval packet.

Regra crítica: GMC title/attributes não autorizam alterar Shopify visível. Separar `GMC ProductInput` de `Shopify title/SEO`.

#### SEO orgânico / Search Console

- Queries por posição, CTR e cliques.
- Páginas com impressão alta e CTR baixa.
- PDP/collection/blog opportunities.
- Marca/modelo com oportunidade.
- Interlinking e schema pendentes.
- Backlog de conteúdo ligado a produto comprável.
- Separação SEO orgânico vs GMC/feed.

#### CRO

Meta ativa: 0,13% → 0,20%.

Métricas:

- sessões → PDP view → add to cart → checkout → purchase;
- PDPs de alto tráfego/baixa venda;
- add-to-cart sem compra;
- mobile issues;
- confiança/PDP/preço/estoque;
- experimentos aprováveis;
- impacto pós-mudança.

#### Paid Traffic / Pareto

- Investimento por campanha/adset/ad.
- Sinais de ROAS de plataforma, sempre rotulados como `platform_signal`.
- Criativos com desempenho.
- Landing pages.
- Produtos impactados.
- Lacunas UTM/ad_name/ad_id.
- Próxima pergunta para Pareto.

#### Influencers / FHITS

- Influencer, cupom, handle, campanha.
- Ponte com Shopify quando verificável.
- Maicon: influencer em Meta `ad_name`; somar todos os `ad_id`; separar Marias.
- Vendas atribuíveis por evidência textual/cupom/referrer.
- Estoque afetado por influencer.
- Criativos candidatos que precisam aprovação visual.

#### CRM / Klaviyo / WhatsApp

- Segmentos RFM.
- Clientes em risco.
- Cross-sell por compra anterior.
- Drafts Klaviyo em aberto.
- WhatsApp concierge preview-only.
- Campanhas aprovadas vs bloqueadas.
- Nunca enviar sem aprovação atual.

#### Conteúdo / Campaign Production Engine

- Backlog de conteúdo por sinal real.
- Produtos/tendências com fit LK.
- PDP copy, blog, newsletter, Instagram, Reels, WhatsApp.
- Status: ideia, draft, aguardando aprovação, publicado, aprendido.

#### Loyalty / Trust

Status: `pending_future`.

- Rivo tiers/marcos.
- Judge.me reviews.
- Review request audit.
- Birthday/profile capture.
- Não retomar sem Lucas pedir.

### 10.3 Zipper OS — Analytics

Fontes canônicas:

- Supabase Zipper Vendas `pcstqxpdzibheuopjkas`, tabela `vendas_tango`.
- Supabase CRM/Main `rmdugdkantdydivgnimb`: `contacts`, `conversations`, `secretary_log`, `followups`, `contents`, `content_metrics`, `content_tags`, `artists`, `exhibitions`, `exhibition_artists`.
- Não usar tabelas `spiti_*` como evidência de vendas reais Zipper.
- Calendário `lucas@zippergaleria.com.br` para logística de obra.

Braços Zipper e analytics:

#### Vendas de obras

- Vendas por período.
- Valor total e ticket médio.
- Artistas vendidos.
- Origem/canal/evento.
- Colecionadores recorrentes.
- Obras/artistas com demanda.
- Histórico antes de rascunho comercial.

#### Colecionadores / relacionamento

- Pendências em `secretary_log`.
- Follow-ups abertos.
- Urgências.
- Contatos por artista/interesse.
- Próximas respostas sugeridas.
- Rascunhos no tom Zipper, nunca envio automático.

#### Feiras / eventos

- Leads que mencionaram ARPA/feira.
- Convites/lembretes pendentes.
- Checklist por fase.
- Produção/comercial/logística.
- Pergunta ao Lucas antes de agendar/enviar convite externo.

#### Comunicação / conteúdo

- Conteúdos publicados.
- Métricas: alcance, impressões, likes, saves, comentários, opens, clicks.
- Conteúdo por artista/exposição.
- Performance por narrativa.
- Backlog de post/newsletter.
- Tom: culto, leve, sofisticado, sem hard sell.

#### Logística de obras

- Conversas com retirada/coleta/entrega/movimentação.
- Data, hora, local de retirada/entrega extraídos do texto.
- Evento em calendário Zipper quando claro e dentro de escopo; produção e entregas como convidados.
- Não assumir local pela etiqueta “Zipper”.

### 10.4 SPITI OS — Analytics

Fontes canônicas:

- Email/fonte de verdade de lances.
- Supabase/SPITI CRM `rmdugdkantdydivgnimb`.
- `spiti_lotes`, lotes, clientes, cobranças, vendas, pagamentos, todos.
- Spiti Hub repo `spiti-auction/spiti-hub`: branch `dev` para staging, `main` produção.

Regra crítica: silêncio é melhor que dado errado.

Braços SPITI e analytics:

#### Leilão / lances

- Lotes ativos.
- Lance atual por fonte verificada.
- Tipo de lance quando disponível: A automático, O normal.
- Divergências entre site, email e base.
- Alertas de lote.
- Última verificação.

#### Operação pós-leilão

- Vendas/cobranças.
- Pagamentos consignante.
- Pendências por cliente/lote.
- Relatórios internos com matriz de evidência.

#### Spiti Hub / produto

- PRs abertos.
- Branch dev vs main.
- Deploy staging/produção.
- SEO/conteúdo do Hub.
- Issues críticas.
- Nunca push direto em main.

#### Marketing / SEO / Conteúdo SPITI

- Páginas de leilão/lote com tráfego.
- Conteúdo/newsletter.
- Search visibility.
- Conversões/lances quando verificável.
- Não inferir bid por meta tag.

### 10.5 Lucas pessoal / Mordomo

Fontes:

- WhatsApp pessoal via wacli quando aprovado/escopado.
- Calendário.
- Telegram como aprovação.

Analytics:

- pendências pessoais;
- eventos claros extraídos;
- follow-ups futuros;
- mensagens que precisam rascunho;
- contatos externos aguardando Lucas.

Guardrail: nunca enviar externo; rascunhar no Telegram/local.

### 10.6 Operações / Tecnologia / Governança

Fontes:

- Hermes runtime.
- Cron registry.
- Gateway/API health.
- Brain health check.
- GitHub PRs.
- Vercel deployments.
- Docker/VPS read-only observability.

Analytics:

- crons ativos;
- crons documentados vs reais;
- falhas recentes;
- jobs silent-OK;
- watchdogs;
- version marker de `mission.lucascimino.com`;
- deploy status;
- secrets missing sem imprimir valores;
- skills drift;
- PRDs sem execução;
- decisões duráveis não salvas na área correta.

---

## 11. Roteamento de risco / Autonomy ladder

### A0 — Livre

- leitura de docs;
- leitura de Brain;
- análise local;
- relatório;
- preview;
- plano;
- secret scan sem valores;
- health check read-only.

### A1 — Livre com registro

- escrever/atualizar doc no Brain;
- criar PRD;
- criar plano;
- criar script read-only;
- gerar artefato local;
- clonar referência pública para pesquisa.

### A2 — Requer cuidado, mas pode preparar

- criar branch/PR documental;
- rodar build/test local;
- consultar APIs read-only com Doppler;
- gerar snapshot privado com PII minimizada;
- preparar cron preview.

### A3 — Requer aprovação Lucas

- criar cron real;
- alterar dashboard em produção;
- alterar banco não crítico;
- alterar Shopify SEO/produto/coleção;
- atualizar Merchant feed/ProductInput;
- criar Klaviyo draft externo;
- usar leitura recorrente de WhatsApp/e-mail sensível.

### A4 — Requer aprovação explícita atual com conteúdo e destinatário/escopo

- enviar WhatsApp/e-mail/cliente/fornecedor/coletor/artista;
- campanha Klaviyo/Meta/Google;
- compra/reposição/sourcing real;
- Shopify/Tiny/Merchant write produtivo;
- Supabase produtivo write;
- deploy com impacto externo;
- Docker/VPS/Traefik/DNS/volumes/redes;
- apagar/deletar/suprimir dados;
- qualquer ação com dinheiro, estoque, cliente ou reputação.

---

## 12. Requisitos funcionais

### RF1 — Home COO

Mostrar visão geral do ecossistema com status, riscos, decisões e próximos passos.

### RF2 — Lucas Queue

Fila única de decisões, com filtros por empresa, risco, impacto e vencimento.

### RF3 — Company cockpits

Cada empresa terá cockpit próprio com:

- status;
- analytics;
- feito/em execução/falta/bloqueado;
- fontes;
- recomendações;
- aprovações.

### RF4 — Analytics Hub

Tela transversal de métricas por empresa/braço, com fonte e frescor.

### RF5 — Data Freshness

Mostrar para cada fonte:

- última leitura;
- método;
- status;
- confiança;
- próximos checks;
- bloqueios.

### RF6 — Approval Center

Centralizar previews e decisões:

- ação proposta;
- payload;
- escopo;
- rollback;
- risco;
- status;
- evidência pós-execução quando houver.

### RF7 — Routines & Cron Registry

Mostrar:

- rotina documentada;
- cron real;
- schedule;
- delivery;
- status;
- último output;
- silent-OK ou obrigatório;
- owner;
- rollback/pause path.

### RF8 — PRD Execution Board

Cada PRD deve virar execução rastreável:

- fases;
- checkboxes;
- lacunas;
- entregáveis;
- evidências;
- próximo bloco seguro.

### RF9 — Workspace-inspired Agent Roster

Mostrar workers possíveis e limites:

- Orchestrator;
- Builder;
- Reviewer;
- QA;
- Data Steward;
- LK/Zipper/SPITI analysts;
- Ops Watch.

No V1, isso é informacional/despacho via Hermes, não swarm web irrestrito.

### RF10 — Capability gates

Se uma integração não estiver pronta, mostrar:

- “precisa configurar”;
- o que falta;
- risco;
- próximo passo seguro;
- não quebrar a tela.

### RF11 — Evidence links

Todo card deve apontar para:

- arquivo Brain;
- report;
- script;
- cron ID quando seguro;
- PR/commit;
- timestamp.

### RF12 — Version verification

Toda build deve ter marcador:

```html
data-mission-control-version="hermes-native-v1-YYYY-MM-DD"
```

Verificação de produção deve checar marker/copy, não apenas HTTP 200.

---

## 13. Requisitos não funcionais

- Português por padrão.
- Mobile-first.
- Carregamento rápido.
- Sem secrets no client bundle.
- Sem PII bruta em HTML/Telegram.
- Auth em todas as rotas internas.
- CSP.
- Fail-closed em integração ausente.
- Separar server-only de client.
- Sem terminal produtivo no V1.
- Logs sanitizados.
- Build e lint obrigatórios antes de deploy.
- Screenshot/browser QA obrigatório antes de afirmar pronto.

---

## 14. Arquitetura proposta

### 14.1 Stack sugerida

- Next.js ou React/Vite próprio, escolhendo o caminho mais simples para Vercel atual.
- TypeScript.
- Tailwind/design system próprio premium minimal.
- Server-side adapters para ler Brain e snapshots.
- JSON artifacts versionados para V1.
- Futuro: API interna para jobs, crons, sessions e approvals.

### 14.2 Camadas

```text
UI Mission Control
├── server adapters
│   ├── Brain reader
│   ├── reports reader
│   ├── cron registry adapter
│   ├── analytics snapshot adapter
│   ├── approvals adapter
│   └── Hermes API adapter futuro
├── data contracts
│   ├── company_status.json
│   ├── analytics_snapshot.json
│   ├── decisions_queue.json
│   ├── routines_registry.json
│   └── prd_execution.json
└── source of truth
    ├── Hermes Brain
    ├── reports
    ├── scripts read-only
    ├── cronjob list
    └── APIs read-only quando aprovadas/necessárias
```

### 14.3 Contratos de dados V1

#### CompanyStatus

Campos:

- company_id
- company_name
- status
- summary
- done
- in_progress
- missing
- blocked
- next_safe_action
- owner_human
- owner_hermes
- risk_level
- evidence
- updated_at

#### DecisionItem

Campos:

- decision_id
- title
- company_id
- area
- impact
- urgency
- recommendation
- options
- required_approval_level
- blocked_reason
- evidence
- expires_at
- status

#### AnalyticsCard

Campos:

- metric_id
- company_id
- arm
- title
- value
- comparison
- source
- freshness
- confidence
- interpretation
- recommended_action
- approval_needed

#### RoutineCard

Campos:

- routine_id
- title
- company_id
- documented_path
- cron_id
- schedule
- delivery
- status
- last_run
- output_contract
- owner
- risk

#### PRDPhase

Campos:

- prd_id
- phase_id
- title
- status
- completed_items
- pending_items
- blocked_items
- evidence
- next_step

---

## 15. Design / UX

### 15.1 Tom visual

Premium minimal, executivo, sem excesso de cards genéricos.

Direção:

- preto/off-white/cinza quente;
- acentos por empresa;
- tipografia limpa;
- densidade alta, mas legível no mobile;
- status chips claros;
- sem visual “SaaS genérico”.

### 15.2 Cores por área

- Grande Mente: neutro premium.
- LK: verde/graphite comercial.
- Zipper: vinho/areia/cultural.
- SPITI: azul/ink/auction.
- Operações: cinza/amber.
- Bloqueado/risco: vermelho controlado.
- Aguardando Lucas: dourado/âmbar.

### 15.3 Cada card deve responder

- O que é?
- Por que importa?
- Qual fonte?
- Qual próximo passo?
- Hermes pode fazer sozinho?
- Precisa Lucas?

---

## 16. Roadmap de implementação

### Fase 0 — Reset seguro da base

Objetivo: parar dependência Tenacity e preparar repositório/estrutura limpa.

Entregáveis:

- backup/tag da implementação atual;
- documentação do que será descartado;
- diretório/projeto novo Hermes-native;
- marker claro de versão;
- decisão registrada no Brain.

Não fazer:

- deletar produção sem rollback;
- deploy sem build/QA;
- conectar APIs sensíveis.

### Fase 1 — PRD + contratos + dados estáticos

Objetivo: transformar este PRD em contratos de dados e conteúdo inicial.

Entregáveis:

- `company_status.json` inicial;
- `decisions_queue.json` inicial;
- `analytics_snapshot.json` inicial;
- `routines_registry.json` inicial;
- `prd_execution.json` inicial;
- parser simples de Brain/reports ou export manual versionado.

### Fase 2 — UI v1 estática com dados reais do Brain

Objetivo: substituir a tela atual por cockpit executivo confiável.

Telas:

- Home COO;
- Lucas Queue;
- Multiempresa;
- LK;
- Zipper;
- SPITI;
- Analytics;
- Approvals;
- Routines;
- PRDs.

Critério de pronto:

- build OK;
- marker OK;
- mobile OK;
- conteúdo não genérico;
- guardrails visíveis;
- sem JS errors.

### Fase 3 — Analytics snapshots read-only

Objetivo: ligar dados vivos de forma segura, começando por snapshots, não live writes.

Prioridade:

1. LK Data Spine: Shopify/Tiny/GA4/GSC/GMC/Metricool/Meta/Klaviyo snapshots.
2. Zipper Supabase snapshots: vendas, contatos, pendências, conteúdo.
3. SPITI read-only: lances/lotes/Hub status, com fonte verificada.
4. Ops: crons/runtime/Brain health.

### Fase 4 — Approval Center real

Objetivo: centralizar previews e histórico de aprovações.

Entregáveis:

- aprovação pendente;
- aprovação concedida;
- rejeitado;
- needs_data;
- executed_verified;
- pending_future;
- rollback link.

No V1/V2, a aprovação continua via Telegram. UI mostra estado e prepara payload.

### Fase 5 — Hermes dispatch seguro

Objetivo: inspirado no Conductor/Swarm do Hermes Workspace, permitir despachar tarefas seguras.

Escopo inicial:

- gerar plano;
- rodar análise read-only;
- atualizar doc Brain;
- preparar PR;
- pedir QA/review.

Fora de escopo:

- botão que executa ação externa/produtiva;
- terminal web irrestrito;
- restart/deploy direto.

### Fase 6 — PWA e uso diário

Objetivo: Lucas usar como app no celular.

Entregáveis:

- PWA;
- home screen;
- versão Telegram de cards;
- deep links para decisões;
- briefing diário a partir do Mission Control.

### Fase 7 — Integrações avançadas

Somente depois de V1 estável:

- sessions browser;
- skills browser;
- memory browser read-only;
- cron manager com approval gates;
- MCP catalog;
- cost/usage ledger;
- agent roster vivo;
- QA screenshots automáticos.

---

## 17. Backlog inicial por prioridade

### P0 — Fundação

- Criar app do zero ou limpar repo atual com rollback.
- Criar design system base.
- Criar contratos JSON.
- Criar Home COO.
- Criar Lucas Queue.
- Criar Multiempresa Map.
- Criar guardrails visíveis.
- Criar version marker.

### P1 — LK OS profundo

- LK PRD execution board.
- Data Quality / stock / SKU / Tiny status.
- GMC status e approval packets.
- SEO/GSC/CRO pipeline.
- Paid vs Influencer split: Pareto vs FHITS.
- CRM/Klaviyo drafts.
- Sourcing/Júlio queue.
- Rotinas Daily/Weekly/Pulso.

### P1 — Zipper OS

- Zipper vendas reais.
- Colecionadores/follow-ups.
- Feiras/ARPA.
- Comunicação/conteúdo.
- Logística de obras.
- Separação forte Zipper vs SPITI.

### P1 — SPITI OS

- Fonte de lances.
- Lotes/alertas.
- Divergências.
- Spiti Hub PR/deploy status.
- Pós-leilão.

### P1 — Operações

- Cron registry.
- Brain health.
- Mission Control deploy verification.
- Watchdogs.
- Skills drift.
- PRD execution status.

### P2 — Hermes Workspace-inspired advanced

- Sessions browser.
- Skills browser.
- Memory browser read-only.
- MCP view.
- Agent roster.
- Swarm reports.
- Conductor-like mission decomposition.
- Terminal disabled by default, gated for local/admin only.

---

## 18. Critérios de sucesso

### Produto

- Lucas entende status global em menos de 30 segundos.
- Lucas sabe exatamente o que aprovar ou bloquear.
- Cada empresa tem próximos passos claros.
- Nenhum card genérico sem fonte.
- Nenhuma ação perigosa fica implícita.

### Operacional

- PRDs viram execução rastreável.
- Rotinas ativas não se confundem com docs.
- Correções do Lucas viram Brain/skill/regra.
- Analytics por empresa deixam de ser relatórios soltos.
- Mission Control mostra lacunas reais, não só cards bonitos.

### Técnico

- Build passa.
- Marker verificado em produção.
- Browser console limpo.
- Mobile sem overflow.
- Sem secrets/PII bruta no bundle.
- Sem dependência de Tenacity/OpenClaw.

---

## 19. Riscos e mitigação

### Risco: virar dashboard bonito mas inútil

Mitigação: cada card precisa ter decisão, fonte, próximo passo e guardrail.

### Risco: misturar empresas

Mitigação: roteamento obrigatório por Grande Mente → empresa → braço; fontes separadas.

### Risco: expor terminal/files/secrets

Mitigação: não incluir terminal no V1; server-only adapters; secret scan; auth.

### Risco: dados vivos quebrados

Mitigação: capability gates e freshness labels.

### Risco: ação externa acidental

Mitigação: Approval Center, A0-A4, Telegram approval e sem botões A4.

### Risco: copiar Hermes Workspace demais

Mitigação: usar como repertório de produto, não base direta; adaptar para COO multiempresa.

### Risco: Tenacity residual continuar no repo

Mitigação: reset documentado, rollback tag, remoção explícita de rotas/acoplamentos OpenClaw.

---

## 20. Plano de execução bite-sized

### Bloco 1 — Preparação segura

1. Confirmar repo/path atual de `mission.lucascimino.com`.
2. Criar branch/tag rollback.
3. Registrar arquivos Tenacity a descartar.
4. Criar diretório/app Hermes-native.
5. Criar `README.md` com decisão de abandono Tenacity.
6. Rodar secret scan antes de commit.

### Bloco 2 — Contratos

1. Criar `src/data/contracts.ts`.
2. Criar fixtures JSON iniciais.
3. Criar `company_status` para LK/Zipper/SPITI/Ops/Lucas.
4. Criar `decisions_queue` inicial.
5. Criar `analytics_snapshot` inicial.
6. Criar `routines_registry` inicial.
7. Criar `prd_execution` inicial.
8. Testar schema/parse.

### Bloco 3 — Layout base

1. Criar design tokens.
2. Criar shell mobile-first.
3. Criar navigation.
4. Criar status chips.
5. Criar evidence link component.
6. Criar guardrail banner.

### Bloco 4 — Home COO

1. Hero Grande Mente.
2. Ecosystem health strip.
3. Lucas Queue preview.
4. Empresas status grid.
5. Próxima ação segura.
6. Rotinas de hoje.
7. Version marker.

### Bloco 5 — Company cockpits

1. LK cockpit.
2. Zipper cockpit.
3. SPITI cockpit.
4. Ops cockpit.
5. Lucas pessoal cockpit.
6. Separar fontes/guardrails por empresa.

### Bloco 6 — Analytics Hub

1. Metric cards por empresa.
2. Fonte/freshness/confidence.
3. LK: GMC/SEO/CRO/Paid/Influencer/Stock/CRM.
4. Zipper: vendas/colecionadores/feiras/conteúdo/logística.
5. SPITI: lances/lotes/hub/pós-leilão/SEO.
6. Ops: crons/health/deploys/skills.

### Bloco 7 — Approval Center

1. Listar decisões pendentes.
2. Exibir payload preview.
3. Exibir risco A0-A4.
4. Exibir rollback/evidência.
5. CTA: “pedir aprovação no Telegram” ou “preparar plano”, sem executar A4.

### Bloco 8 — Routines & PRD Board

1. Cron registry.
2. Rotinas documentadas vs ativas.
3. PRD phases.
4. Próximo checkbox seguro.
5. Bloqueios por aprovação/dados.

### Bloco 9 — Build, QA, deploy controlado

1. `npm run build`.
2. `git diff --check`.
3. Secret scan.
4. Browser local/preview.
5. Mobile screenshot.
6. Console sem erros.
7. Deploy Vercel.
8. Verificar `mission.lucascimino.com` por marker/copy.
9. Validar rollback.

---

## 21. Entregáveis desta fase de PRD

Este PRD fecha a etapa de desenho.

Entregáveis prontos:

- decisão de abandonar Tenacity como base;
- referência local do Hermes Workspace clonada;
- lista de funcionalidades a aprender/adaptar;
- escopo V1;
- escopo fora V1;
- analytics por empresa/braço;
- guardrails A0-A4;
- arquitetura proposta;
- roadmap;
- plano bite-sized de execução.

Próximo passo recomendado:

```text
Executar Bloco 1 — Preparação segura do Mission Control Hermes-native
```

Esse próximo passo deve ser feito com rollback e sem mexer em produção até build/QA estarem limpos.
