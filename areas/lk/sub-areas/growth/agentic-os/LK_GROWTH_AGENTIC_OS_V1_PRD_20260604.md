# LK Growth Agentic OS v1 — PRD

Data: 2026-06-04
Status: **PRD aprovado conceitualmente / implementação pendente de aprovação separada**
Escopo: LK Sneakers Growth OS (`lk-growth` profile)
Modo atual: **local/read-only/documental**

## 1. Tese

O `lk-growth` deve evoluir de um agente que executa crons de Growth para um **sistema operacional agentic de Growth**: um orquestrador com subagentes internos, contexto rico, ferramentas verificadas, governança, recibos e autoaprendizagem.

A meta não é criar mais bots soltos. A meta é criar uma mini-equipe operacional dentro do perfil `lk-growth`, com autonomia máxima onde é seguro e aprovação explícita onde há risco.

## 2. Objetivos

1. Aumentar a qualidade das recomendações de SEO/CRO/GEO/GMC e dos handoffs para LKGOC quando a demanda pertencer ao agente `[LK] Otimização de Coleções`.
2. Reduzir relatórios genéricos e transformar cada execução em decisões acionáveis.
3. Separar coleta, análise, crítica, síntese e aprendizagem.
4. Garantir que cada recomendação tenha fonte, confiança, risco e follow-up.
5. Preservar o padrão Lucas: Telegram só decisões/exceções; Brain como fonte rica.
6. Criar um ciclo contínuo: `run → evidence → recommendation → approval/action → receipt → impact review → lesson → skill/context update`.

## 3. Não objetivos

- Não criar novos bots Telegram neste v1.
- Não criar novos profiles Hermes neste v1.
- Não criar novos crons sem aprovação separada.
- Não permitir writes externos automáticos.
- Não transformar subagentes em memória isolada.
- Não enviar outputs intermediários dos subagentes para Lucas.

## 4. Arquitetura proposta

Fluxo padrão:

```text
Cron / demanda / pergunta
  → LK Growth Orchestrator
  → Growth Planner
  → Specialist Workers selecionados
  → Growth Governor / Critic
  → Síntese do Orchestrator
  → Brain report + receipt
  → Telegram curto se houver decisão/alerta
  → D+7/D+14/D+30 Impact Review
  → Learning Loop: context pack / skill / template / rotina
```

## 5. Componentes

### 5.1 LK Growth Orchestrator

Dono da execução. Responsável por:

- interpretar briefing do cron ou pedido;
- carregar contexto Growth/LK;
- chamar o Planner;
- disparar apenas subagentes necessários;
- consolidar resultados;
- priorizar Top 3–5 ações;
- gerar approval packets quando necessário;
- salvar report/receipt no Brain;
- enviar Telegram apenas quando acionável.

### 5.2 Growth Planner

Responsável por planejar cada run antes dos especialistas.

Entrega obrigatória:

- objetivo da execução;
- subagentes a chamar;
- fontes necessárias;
- fontes opcionais;
- critério `decision-grade`;
- riscos de output;
- condição de abortar/rebaixar confiança.

Exemplo:

> Hoje é GMC Review. Chamar `Data Scout`, `GMC/Product Data Analyst` e `Governor`. Não chamar CRO completo. Se GMC estiver indisponível, emitir gap report e bloquear recomendações decision-grade.

### 5.3 Specialist Workers

Subagentes internos por execução. Não são bots, não têm canal Telegram, não fazem writes.

#### Growth Data Scout

Missão:
- coletar e normalizar dados;
- declarar fontes disponíveis/ausentes;
- não recomendar ação final.

Fontes/ferramentas:
- Brain/files;
- Shopify read-only;
- GA4/GSC quando disponível;
- GMC/Merchant read-only;
- DataForSEO;
- PageSpeed/CrUX;
- Klaviyo/Metricool/Meta apenas como sinais auxiliares quando existirem.

Output:
- fontes verificadas;
- fontes ausentes;
- métricas principais;
- lacunas;
- confiança.

#### SEO/GEO Analyst

Missão:
- oportunidades orgânicas, SERP, AI Search/GEO, citabilidade, schema/FAQ.

Fontes/ferramentas:
- GSC;
- DataForSEO;
- web/browser read-only;
- Brain experiment history;
- llms.txt / agents.md / schema;
- skills SEO quando disponíveis.

Output:
- finding;
- query/tema;
- URL alvo;
- evidência;
- hipótese;
- recomendação;
- confidence;
- métrica de follow-up.

#### CRO/PDP Analyst

Missão:
- funil, PDP, collection, mobile UX, conversão e experimentos.

Fontes/ferramentas:
- GA4;
- Shopify read-only;
- browser/public QA;
- PageSpeed/CrUX;
- experiment ledger.

Output:
- gargalo;
- hipótese CRO;
- impacto/esforço/risco;
- preview necessário;
- rollback esperado;
- métrica D+7/D+14.

#### GMC/Product Data Analyst

Missão:
- Merchant Center, feed, atributos, LIA/local inventory, product data.

Fontes/ferramentas:
- GMC/Merchant read-only;
- Shopify read-only;
- product feeds/readbacks;
- Brain packets anteriores;
- DataForSEO quando impactar Shopping/SERP.

Output:
- issue;
- offers/SKUs afetados;
- evidência;
- fonte provável;
- risco de overwrite;
- micro-piloto sugerido;
- approval packet requerido.

#### Content/SEO Analyst — não-LKGOC

Missão:
- conteúdo Growth não-LKGOC, source pages não-LKGOC, copy comercial, citability blocks e handoff para `[LK] Otimização de Coleções` quando a demanda virar LKGOC.

Fontes/ferramentas:
- GSC/DataForSEO;
- public SERP;
- Brain Growth;
- Shopify read-only;
- templates editoriais não-LKGOC.

Bloqueio:
- LKGOC, otimização de coleção, guia de coleção e página/guia de produto-modelo não são executados por este worker; devem ser roteados ao agente `[LK] Otimização de Coleções`.

Output:
- evidence packet;
- estrutura recomendada não-LKGOC;
- sinal/handoff para Collection Optimizer quando aplicável;
- riscos;
- preview/local artifact.

#### Experiment Reviewer

Missão:
- fechar aprendizagem D+7/D+14/D+30.

Fontes/ferramentas:
- receipts;
- Shopify/GA4/GSC read-only;
- Brain experiment ledger.

Output:
- hipótese original;
- métrica esperada;
- resultado observado;
- verdict: improved / neutral / worsened / inconclusive / insufficient data;
- lesson;
- proposta de atualizar skill/contexto/template.

### 5.4 Growth Governor / Critic

Responsável por segurança, qualidade e anti-alucinação.

Checagens obrigatórias:

- recomendação tem evidência?
- fonte usada é a fonte correta?
- há dado ausente que rebaixa confiança?
- já existe experimento parecido?
- há write externo implícito?
- precisa de approval packet?
- há risco de ruído no Telegram?
- o output diferencia evidência, hipótese, opinião e decisão?

Pode bloquear ou rebaixar qualquer recomendação.

### 5.5 Growth Learning Loop

Responsável por transformar execuções em aprendizado.

Artifacts:

- Run Receipt;
- Hypothesis Ledger;
- Impact Review;
- Context Pack Update;
- Skill Promotion Candidate;
- Kill Criteria Register.

## 6. Context Packs

Cada subagente deve receber contexto explícito. Formato base:

```yaml
name: <subagent>
mission: <o que faz>
non_goals: <o que não faz>
lk_context:
  - LK é curadoria/sob encomenda; não usar estoque como prioridade SEO/CRO.
  - Tiny é estoque; Shopify é superfície/event trigger.
  - Brain é fonte rica; memória global é boot/index.
source_hierarchy:
  - <fonte 1>
  - <fonte 2>
allowed_tools:
  - <tool read-only>
blocked_tools:
  - external writes
  - WhatsApp/direct sends
  - campaigns/bulk
  - infra/runtime
required_output_schema:
  - evidence
  - interpretation
  - confidence
  - recommendation
  - approval_needed
  - follow_up_metric
decision_grade:
  required:
    - <evidência mínima>
escalation_rules:
  - if source missing: mark non-decision-grade
learning_hook:
  - register hypothesis
  - trigger D+7/D+14 review
```

## 7. Matriz de autonomia

### A0 — Ler e diagnosticar

Livre.

Inclui:
- ler Brain;
- ler reports/receipts;
- auditar público;
- consultar integrações read-only;
- rodar scripts locais read-only.

### A1 — Criar preview/local packet

Livre.

Inclui:
- criar approval packet local;
- gerar scorecard;
- gerar proposed title/meta/schema/content;
- criar plano de teste.

### A2 — Recomendar decisão

Livre se tiver evidência e confiança declarada.

Inclui:
- priorizar Top 5;
- recomendar fazer/não fazer;
- definir próximo follow-up.

### A3 — Write externo pequeno

Requer aprovação explícita e escopada.

Inclui:
- Shopify SEO fields;
- GMC/Product API ou supplemental feed;
- Klaviyo envio;
- theme dev upload;
- alteração em collection/product/page.

### A4 — Produção/bulk/campanha/infra

Requer aprovação forte + backup + rollback + verificação.

Inclui:
- publish production theme;
- bulk updates;
- campanhas pagas;
- WhatsApp bulk;
- Docker/VPS/Traefik/API/gateway/secrets.

## 8. Integrações e status operacional

Cada ferramenta/integracão deve ser classificada antes de uso:

- `unavailable`
- `documented_only`
- `configured`
- `discovered`
- `read_only_verified`
- `write_capable_but_blocked`
- `approved_for_scope`

Regra: uma ferramenta só pode sustentar recomendação decision-grade se estiver `read_only_verified` ou se a limitação for explicitamente declarada.

Integrações esperadas por domínio:

- Brain/file: obrigatório para todos.
- Shopify read-only: produto, collection, comercial, receipts.
- GA4/GSC: decisão comercial SEO/CRO.
- GMC/Merchant: GMC/product data/local inventory.
- DataForSEO: SERP, keyword, competitor, AI/LLM mentions.
- PageSpeed/CrUX: performance/CWV.
- Klaviyo/Metricool/Meta: sinais auxiliares; writes bloqueados.
- Browser/web: QA público e SERP pública.

## 9. Output final para Lucas

Padrão Telegram:

- Veredito curto.
- Top 3–5 ações.
- O que exige aprovação.
- O que ficou non-decision-grade.
- Próximo passo recomendado.

Nunca enviar:
- output bruto de subagente;
- logs técnicos;
- job IDs internos sem necessidade;
- relatório longo quando não há decisão.

## 10. Piloto v1 recomendado

Primeiro piloto: `LK Growth Weekly Command Center` de segunda.

Por quê:
- é o cron mais abrangente;
- sofre mais com mistura de responsabilidades;
- permite testar Planner, especialistas, Governor e síntese sem criar runtime novo.

Subagentes do piloto:

1. Growth Planner
2. Growth Data Scout
3. SEO/GEO Analyst
4. CRO/PDP Analyst
5. GMC/Product Data Analyst
6. Growth Governor / Critic
7. Growth Orchestrator Summary

Output esperado:

- relatório Brain detalhado;
- Run Receipt;
- Top 5 prioridades;
- até 3 approval packets;
- lista de fontes ausentes;
- hipóteses registradas para D+7/D+14;
- Telegram curto se houver decisão.

## 11. Critérios de sucesso do piloto

O piloto passa se:

- cada subagente segue seu schema;
- o Planner chama apenas os especialistas necessários;
- o Governor bloqueia/rebaixa recomendações sem evidência;
- o relatório final é mais claro que o formato atual;
- há menos ruído para Lucas;
- pelo menos uma hipótese vira follow-up mensurável;
- nenhuma ação externa é feita sem aprovação;
- tudo fica rastreável no Brain.

## 12. Kill criteria

Parar ou rebaixar a implementação se:

- subagentes duplicarem trabalho sem ganho claro;
- output ficar mais longo e menos acionável;
- recomendações começarem a aparecer sem fonte;
- Telegram ficar mais ruidoso;
- execução ficar lenta demais para o cron;
- subagentes tentarem assumir write externo;
- aprendizado não gerar melhoria de contexto/skill/template.

## 13. Plano de implementação em fases

### Fase 0 — Documental/read-only

- PRD aprovado.
- Context packs rascunhados.
- Tool matrix rascunhada.
- Nenhum runtime alterado.

### Fase 1 — Simulação local

- Rodar uma simulação manual a partir de output recente do cron.
- Sem `cronjob update`.
- Sem restart/gateway.
- Salvar relatório comparativo: antes/depois.

### Fase 2 — Piloto em uma execução manual

- Executar o modelo agentic para o `Weekly Command Center` sob supervisão.
- Entrega local + resumo Telegram se acionável.
- Sem writes externos.

### Fase 3 — Embutir no cron existente

- Apenas após aprovação separada.
- Alterar prompt/script do cron existente, não criar novos crons.
- Backup/rollback do job anterior.
- Verificar primeira execução.

### Fase 4 — Promoção para padrão Growth OS

- Atualizar skills/context packs.
- Documentar rotina oficial.
- Criar monitoramento silent-OK.
- Avaliar se algum subagente merece profile/bot próprio no futuro.

## 14. Approval gates

Este PRD **não autoriza**:

- alteração de cron runtime;
- criação de profile/bot;
- restart de gateway;
- writes em Shopify/GMC/Klaviyo/Meta;
- envio externo;
- mudança de ferramenta/MCP.

Próxima aprovação necessária:

> Aprovar Fase 1 — simulação local/read-only do LK Growth Agentic OS usando um output recente do cron, sem mexer no runtime.

## 15. Decisão recomendada

Seguir com Fase 1.

Motivo: valida inteligência, autonomia e qualidade do desenho antes de qualquer alteração em cron ou runtime.
