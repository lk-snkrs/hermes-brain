# Capabilities Adoption Matrix — Hermes/LK produção

Gerado em: 2026-05-30T21:41:19+00:00  
Status: **canônico v0.1**  
Escopo: comparação documental/read-only entre features oficiais do Hermes e uso atual local. **Não autoriza ativação de plugin, MCP, Kanban dispatcher, hooks, dashboard público, API, cron ou qualquer write externo.**

## 1. Tese executiva

A pergunta correta não é “temos muitos documentos?” nem “LK Shopify está offline?”. A pergunta correta é:

> Estamos usando o Hermes como plataforma operacional completa, com as features certas nos lugares certos, sem aumentar risco?

Resposta curta:

- **Estamos usando bem:** profiles, Telegram gateways, skills, memória, session_search, cron/script-only, delegation, toolsets por plataforma, checkpoints, voice/TTS/vision/image/web/terminal/file/code em vários perfis.
- **Estamos usando parcialmente:** Kanban, MCP, dashboard/API, plugins, context files/SOUL/Brain, deliverable mode, provider fallback, hooks.
- **Estamos subutilizando ou sem piloto controlado:** Kanban como board real de trabalho, plugins próprios, hooks de eventos, Goals, batch processing, MCPs de negócio além de DataForSEO, dashboard como cockpit local seguro, profile distributions.
- **Não devemos ativar tudo:** algumas features aumentam muito o blast radius. Adoção deve ser por piloto pequeno, read-only ou local, com rollback.

## 2. Correção de termos

Pelo áudio, interpretei:

- “Esquio” como **Skills**.
- “Camba” como **Kanban**.

Se você quis dizer outra coisa, atualizar este arquivo.

## 3. Matriz por capability

### Skills

- Estado atual: **alto uso**.
- Evidência: dezenas de skills instaladas; uso obrigatório por tarefa; skills específicas de Hermes, LK, Shopify, SEO, devops, MCP, GitHub, etc.
- Valor: alto. É a memória procedural do Hermes.
- Gap: evitar virar depósito de relatório; manter skills enxutas e reutilizáveis.
- Próximo passo: manter; criar/patchar skills só quando um workflow se provar reutilizável.
- Risco: prompt bloat se tudo virar skill.
- Prioridade: **P0 manter bem, não expandir sem curadoria**.

### Memory / User Profile

- Estado atual: **alto uso**.
- Evidência: memória persistente ativa e cheia; profile de usuário ativo.
- Valor: alto para preferências, guardrails e ambiente.
- Gap: memória quase cheia; evitar fatos stale.
- Próximo passo: higiene periódica; mover procedimentos para skills e relatórios para Brain.
- Risco: memória imperativa ou stale causar comportamento errado.
- Prioridade: **P0 higiene**.

### Profiles / Multi-profile gateways

- Estado atual: **alto uso**.
- Evidência: default, lk-shopify, lk-ops, lk-growth, lk-trends, mordomo, spiti e outros perfis preparados/live.
- Valor: muito alto; permite isolamento por função/empresa.
- Gap: contratos de cada profile e estado live precisam continuar canônicos.
- Próximo passo: manter `PROFILE_STATUS_MATRIX.md` como fonte curta e revalidar antes de ações.
- Risco: profile configurado ser tratado como ativo; token/API/webhook herdado indevidamente.
- Prioridade: **P0**.

### Toolsets por plataforma

- Estado atual: **alto uso, mas precisa governança**.
- Evidência: toolsets diferentes entre Telegram e CLI em vários perfis; especialistas com toolsets mais estreitos.
- Valor: alto; controla blast radius.
- Gap: alguns perfis ainda têm terminal/code no Telegram por necessidade, mas isso deve ser intencional.
- Próximo passo: revisar por outcome, não por paranoia: atendimento rápido precisa pouco; manutenção precisa mais.
- Risco: toolset amplo demais em Telegram; toolset estreito demais quebrando WACLI/Tiny/Shopify.
- Prioridade: **P0 governança contínua**.

### Cron / Script-only watchdogs

- Estado atual: **alto uso**.
- Evidência: muitos crons; padrão `no_agent`/silent-OK usado; relatórios e watchdogs locais.
- Valor: alto para monitoramento e rotinas.
- Gap: delivery precisa ficar coerente: Telegram só quando for alerta/decisão/relatório desejado.
- Próximo passo: manter silent-OK; não criar cron novo sem owner, delivery e rollback.
- Risco: spam no Telegram ou jobs com prompt pesado/desatualizado.
- Prioridade: **P0 manter disciplina**.

### Delegation / Subagents

- Estado atual: **uso bom em sessão**, não necessariamente produto operacional.
- Evidência: toolset `delegation` habilitado em perfis; usado para pesquisas/tarefas paralelas.
- Valor: alto para raciocínio paralelo e auditorias.
- Gap: para trabalhos duráveis, Kanban pode ser melhor que delegation.
- Próximo passo: usar delegation para subtarefas rápidas; Kanban para workflows que precisam sobreviver restart/audit trail.
- Risco: subagent não verifica side-effects; precisa validar handles.
- Prioridade: **P1 melhorar critério delegation vs Kanban**.

### Kanban / “Camba”

- Estado atual: **configurado parcialmente, subutilizado como board real**.
- Evidência read-only: `kanban.dispatch_in_gateway=true` aparece em default/lk-ops/lk-growth; docs oficiais cobrem board, dispatcher, worker lanes, dashboard e audit trail.
- Valor: muito alto para trabalho durável multi-agente: fan-out/fan-in, filas, revisão, execução por especialistas e trilha persistente.
- Gap principal: falta um piloto operacional simples e seguro com board real, assignees claros e workers restritos.
- Melhor uso para nós:
  - fila de melhorias Hermes/LK;
  - triagem de documentos e rotinas;
  - SEO/Growth research → análise → plano;
  - tarefas longas que hoje ficam em conversa Telegram;
  - revisão de alterações locais antes de runtime.
- Não usar para:
  - atendimento imediato;
  - ações externas sem approval;
  - tarefas pequenas de uma resposta.
- Piloto recomendado:
  - board `hermes-lk-improvements`;
  - tarefas **unassigned** primeiro;
  - 3 cards: MCP evaluation, plugin evaluation, dashboard/local cockpit evaluation;
  - sem dispatcher automático para writes externos;
  - só depois testar um worker local/read-only.
- Risco: `dispatch_in_gateway` pode tornar assignment executável; não atribuir tarefas produtivas sem lane/worker seguro.
- Prioridade: **P1 alto — fazer piloto controlado**.

### MCP

- Estado atual: **parcial**.
- Evidência read-only: `mcp_servers` ausente na maioria dos perfis; `dataforseo` configurado em `lk-shopify` e `lk-trends`; skill `native-mcp` confirma SDK/HTTP disponíveis neste ambiente.
- Valor: alto quando conecta ferramentas externas com schemas precisos.
- Gap principal: falta política de quais MCPs valem e em qual profile.
- Bons candidatos para piloto:
  - DataForSEO: já existe em LK Shopify/Trends; validar uso real e tool whitelist.
  - Banco/Open Finance MCP: só read-only e com autenticação explícita do usuário.
  - Crisp/Hugo MCP: futuro atendimento, mas melhor via Marketplace Plugin + fila idempotente.
  - GitHub MCP: só se trouxer algo melhor que `gh`/skills atuais.
- Não instalar MCP remoto só porque existe.
- Regra de segurança:
  - começar read-only/list/get;
  - token em Doppler/secret manager, nunca em chat/config impresso;
  - sampling desativado para servidores não confiáveis;
  - whitelisting de tools antes de Telegram.
- Prioridade: **P1 alto — piloto MCP controlado, não expansão geral**.

### Plugins

- Estado atual: **quase não usado**.
- Evidência read-only: `plugins.enabled: []` na maioria dos configs; docs oficiais citam plugins, built-ins, model provider plugins, memory provider plugins, context engine plugins, platform adapter plugins.
- Valor: alto para empacotar capacidade própria de forma limpa.
- Melhor uso para nós:
  - plugin LK read-only capability cards;
  - plugin de observabilidade local/cockpit;
  - plugin de guardrails/receipts;
  - eventualmente platform adapter/integration shell para Crisp.
- Não usar plugin para tudo; skill/script pode bastar.
- Piloto recomendado:
  - primeiro plugin local/read-only que exponha “status dos profiles” ou “capability cards” sem writes externos.
- Risco: plugin pode adicionar tools/surfaces de alto privilégio; precisa opt-in e testes.
- Prioridade: **P1 médio/alto — piloto local read-only**.

### Event Hooks

- Estado atual: **não usado**.
- Evidência read-only: `hooks: {}` e `hooks_auto_accept: false` nos configs inspecionados.
- Valor: médio/alto para eventos internos: agente longo, falhas, receipts, métricas.
- Melhor uso para nós:
  - hook local para registrar long-running agent em arquivo/Brain, não Telegram;
  - hook de receipt quando ação runtime aprovada termina;
  - hook de métrica para dashboard.
- Não usar para alertar Telegram em todo evento; isso vira ruído.
- Risco: hooks podem executar código automaticamente.
- Prioridade: **P2 — depois de Kanban/MCP/plugin piloto**.

### Web Dashboard / API Server

- Estado atual: **API ativa no default; dashboard conceitualmente útil, mas exposição exige cuidado**.
- Evidência: inventário viu `0.0.0.0:8642` e `0.0.0.0:8644` no default; config tem dashboard settings.
- Valor: alto como cockpit de observabilidade e sessões/logs/config/crons/kanban.
- Gap: confirmar exposição real/proteções antes de usar como interface central.
- Melhor uso para nós:
  - local/loopback/Tailscale primeiro;
  - cockpit para status, crons, sessions, logs, Kanban e receipts;
  - Mission Control continua camada executiva, dashboard é runtime observability.
- Risco: API/dashboard dá acesso poderoso; não expor público sem auth/proxy/rollback.
- Prioridade: **P0 classificar exposição; P1 cockpit local**.

### Webhooks / Subscription proxy

- Estado atual: **webhook ativo no default; uso de negócio deve ser restrito**.
- Valor: alto para eventos Shopify/GitHub/Crisp etc.
- Gap: cada webhook precisa assinatura/HMAC, owner, event filter, idempotência e rollback.
- Melhor uso para nós:
  - Shopify/Tiny restock via proxy com HMAC correto;
  - Crisp plugin hooks no futuro;
  - GitHub/PR review se houver necessidade.
- Risco: writes/side effects externos.
- Prioridade: **P1 por integração específica, não genérico**.

### Goals

- Estado atual: **configurado, pouco explorado**.
- Evidência: `goals.max_turns: 20` em configs; docs oficiais cobrem Persistent Goals.
- Valor: médio para loops persistentes com critérios de sucesso.
- Melhor uso para nós:
  - tarefas locais com critério claro, ex: “consolidar docs até passar healthcheck”.
- Não usar para ações produtivas externas ou loops vagos.
- Risco: loop autônomo indo longe demais se critério ruim.
- Prioridade: **P2 piloto local/documental**.

### Batch processing / trajectories

- Estado atual: **não operacionalizado como rotina canônica**.
- Valor: alto para processar muitos prompts/itens com output auditável.
- Melhor uso para nós:
  - avaliação de prompts/skills;
  - classificação de documentos antigos;
  - geração de cards Kanban a partir de backlog;
  - testes de qualidade de respostas dos especialistas.
- Risco: custo e geração massiva de artefatos.
- Prioridade: **P2**.

### Deliverable mode / artifacts

- Estado atual: **usado parcialmente via arquivos locais/MEDIA quando necessário**.
- Valor: alto para entregar PDFs, imagens, relatórios, HTMLs e receipts.
- Gap: padronizar quando entregar `MEDIA:` vs só caminho local.
- Prioridade: **P1 padronizar nos relatórios executivos**.

### Context files / SOUL / AGENTS / Brain

- Estado atual: **alto uso, mas precisa síntese**.
- Evidência: Brain com MAPA/AGENTS/rotinas; manual canônico recém-criado.
- Valor: muito alto para identidade e continuidade.
- Gap: evitar excesso de docs conflitantes; manter fonte curta.
- Próximo passo: este manual e matriz devem ser preferidos sobre receipts antigos.
- Prioridade: **P0**.

### Checkpoints / rollback

- Estado atual: **habilitado**.
- Evidência: `checkpoints.enabled=true` nos configs inspecionados.
- Valor: alto para edição local.
- Gap: garantir que mudanças runtime também tenham backup explícito além de checkpoint.
- Prioridade: **P0 manter**.

### Voice / TTS / Vision / Image generation / Browser

- Estado atual: **habilitado em toolsets relevantes**.
- Valor: alto para Telegram multimodal, análise visual e geração de artefatos.
- Gap: usar sob demanda, não como prioridade de plataforma.
- Prioridade: **P2 melhoria oportunista**.

### Profile distributions

- Estado atual: **não usado como produto interno**.
- Valor: médio/alto se quisermos empacotar especialistas replicáveis.
- Melhor uso para nós:
  - empacotar “LK Shopify specialist” ou “SPITI specialist” no futuro.
- Risco: congelar prematuramente padrões ainda em maturação.
- Prioridade: **P3 futuro**.

## 4. Prioridades recomendadas

### P0 — Não é novidade, é segurança operacional

1. Classificar exposição real do API/webhook default.
2. Manter manual canônico curto e atualizado.
3. Higienizar memória/skills para evitar bloat e conflito.
4. Confirmar por profile: toolsets, API/webhook off, round-trip quando necessário.

### P1 — Features Hermes que mais valem agora

1. **Kanban piloto controlado** para melhorias Hermes/LK, com tarefas unassigned e workers read-only.
2. **MCP piloto controlado**: validar DataForSEO existente e definir política para MCPs de negócio.
3. **Plugin local read-only**: status/capability cards do ecossistema, sem writes externos.
4. **Dashboard/API local seguro**: cockpit de observabilidade, não exposição pública.
5. **Deliverable mode padronizado** para relatórios/artifacts.

### P2 — Depois que P1 estiver estável

1. Event hooks locais/silent-OK.
2. Goals para loops documentais com critério claro.
3. Batch processing para classificar docs/backlog/skills.
4. Profile distributions para empacotar especialistas maduros.

## 5. Próximo pacote de trabalho sugerido

Nome: **Fase 2 — Adoção controlada de features Hermes**

Escopo read-only/local:

1. Criar `HERMES_FEATURE_BACKLOG.md` com cards de adoção.
2. Criar design de board Kanban `hermes-lk-improvements` sem executar dispatcher produtivo.
3. Auditar MCP `dataforseo` nos perfis onde já existe: está carregando? quais tools? sampling off? tool whitelist?
4. Definir primeiro plugin local/read-only: “Hermes/LK capability status”.
5. Especificar dashboard local/cockpit: loopback/Tailscale, auth, sem exposição pública.

Saída esperada:

- backlog claro;
- nenhum runtime alterado;
- approval packets separados para qualquer ativação real.

## 6. Regra final

Não perseguir “usar todas as features”. Perseguir:

> usar cada feature onde ela reduz risco, aumenta clareza operacional ou cria capacidade real que hoje não temos.

Features que aumentam superfície sem benefício imediato devem ficar documentadas, não ativadas.
