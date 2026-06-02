# Reauditoria de memória — Hermes vs Bruno/OpenClaw vs docs oficiais Hermes

Data/hora: 2026-06-01T14:25:59+00:00  
Status: auditoria local/read-only + documentação; sem alteração de runtime/provider.

## Pergunta

Lucas pediu nova auditoria da memória, comparando:

1. estado atual da memória Hermes;
2. princípio Bruno/OpenClaw;
3. documentação oficial Hermes.

## Veredito curto

**A arquitetura está majoritariamente correta agora.**

Depois das correções de 2026-06-01, a separação principal está alinhada:

- **Hermes Brain** = memória rica canônica / fonte de verdade documental e operacional curada.
- **`MEMORY.md` / `USER.md`** = boot mínimo injetado.
- **daily / hot / reports / receipts** = continuidade, evidência e estado current.
- **skills** = procedimentos repetíveis.
- **`session_search`** = histórico conversacional.
- **Mem0/provider externo** = decisão atual posterior: não usar Mem0; provider externo off; Brain é fonte de verdade.

O principal ponto de atenção restante é que o `USER.md` do profile default está em **~90%** do limite. O conteúdo é relevante, mas a capacidade está alta e deveria ser compactada em próxima rodada pequena para voltar ao alvo de 40–70%.

## Fontes consultadas

### Docs oficiais Hermes

- `https://hermes-agent.nousresearch.com/docs/user-guide/features/memory`
- `https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers`
- `https://hermes-agent.nousresearch.com/docs/user-guide/features/skills`
- `https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files`
- `https://hermes-agent.nousresearch.com/docs/user-guide/profiles`
- `https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly`

### Brain / Bruno

- `areas/operacoes/base-conhecimento/bruno-openclaw-segundo-cerebro-crons-consolidacao-diaria-2026-05-19.md`
- `areas/operacoes/base-conhecimento/bruno-openclaw-organograma-agentes-e-brain-2026-05-19.md`
- `memories/politica-memoria-hermes.md`
- `memories/MAPA.md`
- `AGENTS.md`

## O que a documentação oficial Hermes confirma

### 1. Built-in memory é pequena e curada

Docs de memória confirmam:

- `MEMORY.md`: notas do agente, ambiente, convenções e aprendizados.
- Limite padrão: **2.200 chars**.
- `USER.md`: perfil, preferências e estilo do usuário.
- Limite padrão: **1.375 chars**.
- Ambas entram no system prompt como snapshot congelado no início da sessão.
- Mudanças persistem em disco imediatamente, mas só entram no prompt em nova sessão.

Conclusão: usar `MEMORY.md`/`USER.md` como Brain inteiro é contra a arquitetura Hermes.

### 2. Context files são o lugar correto para contexto de projeto/domínio

Docs de context files confirmam:

- `AGENTS.md` é contexto primário de projeto.
- `.hermes.md`/`HERMES.md`, `AGENTS.md`, `CLAUDE.md` e `.cursorrules` seguem prioridade.
- Context files são descobertos progressivamente em subdiretórios.
- Isso reduz prompt bloat e preserva cache.

Conclusão: Brain + `AGENTS.md`/MAPAs é o canal correto para contexto rico navegável.

### 3. Skills são memória procedural sob demanda

Docs de skills confirmam:

- skills são documentos carregados sob demanda;
- usam progressive disclosure;
- são melhores para procedimentos, runbooks, troubleshooting, auditorias e padrões repetíveis.

Conclusão: procedimento repetível não deve ficar no `MEMORY.md`; deve virar skill/reference.

### 4. External providers são aditivos, não substitutos

Docs de memory providers confirmam:

- provider externo roda junto com built-in memory;
- só um provider externo ativo por vez;
- built-in memory continua ativa;
- providers como Honcho/Mem0 adicionam recall/semântica/ferramentas, mas não substituem o Brain.

Conclusão posterior à decisão de Lucas: não usar Mem0; manter provider externo off, salvo novo PRD explícito.

### 5. Profiles isolam memória

Docs de profiles confirmam que cada profile tem seu próprio:

- config;
- `.env`;
- `SOUL.md`;
- memories;
- sessions;
- skills;
- cron;
- gateway state.

Conclusão: auditoria de memória deve ser per-profile; não basta olhar o default.

## Comparação com Bruno/OpenClaw

### Tese Bruno

A síntese Bruno/OpenClaw no Brain diz:

> O agente não é o cérebro. O agente opera em cima de um workspace/cérebro persistente.

E também:

> Mental notes don’t survive session restarts. Files do.

O padrão Bruno divide:

1. memória de boot;
2. memória de sessão;
3. memória semântica;
4. `hot.md` para contexto quente;
5. dailies para o dia;
6. MAPAs distribuídos para navegação;
7. skills para capacidades reutilizáveis;
8. archive/reports/receipts para histórico/evidência.

### Tradução Hermes atual

A tradução Hermes-native agora está correta:

- memória de boot Bruno → `MEMORY.md`/`USER.md` curtos + `SOUL.md`/`AGENTS.md`/MAPAs;
- memória de sessão Bruno → conversa atual + `session_search` para recuperação posterior;
- memória semântica Bruno → Brain/search/session_search; provider externo canário foi rejeitado por decisão posterior de Lucas;
- workspace/cérebro Bruno → Hermes Brain versionado;
- MAPAs Bruno → `MAPA.md` distribuídos no Brain;
- skills Bruno → Hermes skills;
- hot/daily Bruno → `memories/hot.md` e `memories/daily/YYYY-MM-DD.md`.

## Medição atual da memória injetada

Config atual em `/opt/data/config.yaml`:

- `memory.memory_char_limit`: **2200**
- `memory.user_char_limit`: **1375**
- `memory.provider`: **vazio** — sem external provider ativo.

### Profile default

- `MEMORY.md`: **1.092 / 2.200 chars** = **49,6%**. Saudável.
- `USER.md`: **1.234 / 1.375 chars** = **89,7%**. Alto.

Leitura:

- `MEMORY.md` default está excelente: boot mínimo com ponteiros para Brain, profiles, safety e fontes de verdade.
- `USER.md` default está semanticamente correto, mas perto do limite. É o único item acima de 80%.

### Specialist profiles auditados

Todos os `MEMORY.md` especialistas principais estão abaixo de 50%:

- `lk-growth`: 899 / 2200 = 40,9%.
- `lk-ops`: 825 / 2200 = 37,5%.
- `lk-shopify`: 1052 / 2200 = 47,8%.
- `lk-trends`: 962 / 2200 = 43,7%.
- `mordomo`: 818 / 2200 = 37,2%.
- `spiti`: 716 / 2200 = 32,5%.
- worker/read-only profiles: 760 / 2200 = 34,5%.

`USER.md` especialistas ficam em geral abaixo de 72%, exceto default que está em 89,7%.

## Achados

### Achado A — Arquitetura está alinhada

Status: OK.

A política canônica está documentada em:

- `memories/politica-memoria-hermes.md`;
- `memories/MAPA.md`;
- `AGENTS.md`.

A frase central está correta: Brain é fonte rica; memória injetada é boot mínimo; Mem0 não é fonte de verdade.

### Achado B — Default `USER.md` está alto

Status: atenção.

`USER.md` default contém preferências importantes, mas está em **89,7%**. Isso não está quebrado, mas reduz margem para novas preferências.

Recomendação: próxima rodada pequena de compactação do `USER.md`, com backup, para alvo de **900–1.050 chars**.

Candidatos de compactação:

- fundir preferências de alerta Telegram + entrega de reports;
- fundir safety externa + autonomia local;
- reduzir frase de Mem0, pois a política completa já está no Brain/PRD.

### Achado C — Duplicação proposital em profiles worker/read-only

Status: aceitável, mas monitorar.

Há blocos iguais em quatro profiles read-only/worker:

- `brain-process`;
- `hermes-ops-readonly`;
- `lk-analyst-readonly`;
- `lk-content-reviewer`.

Como cada profile tem memória isolada, alguma duplicação de guardrails é aceitável. Mas se crescer, deve virar ponteiro para Brain/skill e não texto completo.

### Achado D — External provider ainda desligado

Status: OK.

`memory.provider` está vazio. Isso está alinhado com a decisão atual:

- não ativar Mem0 em produção;
- não preparar canário/approval packet ativo; artefatos anteriores ficam históricos/rejeitados;
- se testado, usar canário sintético.

### Achado E — Brain como memória rica está documentado

Status: OK.

O Brain contém:

- política de memória;
- daily/hot;
- PRD Mem0 histórico/rejeitado;
- queries/approval packet históricos/rejeitados;
- receipts de compactação;
- relatório de validação web;
- MAPAs e AGENTS atualizados.

Isso segue Bruno: não deixar decisão só no chat.

## Scorecard

- Alinhamento com docs oficiais Hermes: **9/10**.
- Alinhamento com Bruno/OpenClaw: **9/10**.
- Higiene do `MEMORY.md` default: **10/10**.
- Higiene do `USER.md` default: **7/10** por saturação, não por conteúdo errado.
- Specialist profiles: **8,5/10** — bons tamanhos; duplicação em workers é aceitável mas deve ser monitorada.
- Provider externo: **10/10** — corretamente não ativado.

Nota geral: **8,8/10**.

## Recomendações

### P0 — Não mexer em provider externo agora

Mem0 continua fora de produção e fora do backlog ativo por decisão de Lucas.

### P1 — Compactar `USER.md` default em rodada pequena

Fazer backup e reduzir de ~1.234 chars para ~950–1.050 chars, sem perder:

- alertas acionáveis;
- safety VPS/Docker/app;
- preferência por docs concisos/skills;
- autonomia local vs writes externos;
- guardrail Mordomo;
- reports silenciosos/local por padrão;
- Mem0 apenas como índice auxiliar.

### P2 — Monitor mensal de saturação

Criar ou manter rotina local/silent-OK para alertar só se:

- algum `MEMORY.md`/`USER.md` passar de 80%;
- aparecer cron/job/PID/commit/PR/status current em memória injetada;
- provider externo for ativado sem PRD/canário.

### P3 — Manter Bruno como benchmark, não runtime

Não copiar OpenClaw literalmente. Usar o princípio:

- files > mental notes;
- Brain > chat;
- MAPAs distribuídos;
- daily/hot/receipts;
- skill para procedimento.

## Não-ações

Não foi feito:

- alteração de runtime;
- restart de gateway/profile;
- Docker/VPS/Traefik;
- cron;
- provider externo;
- edição de `MEMORY.md`/`USER.md` nesta auditoria;
- gravação de credenciais.

## Conclusão

A análise anterior estava correta e agora está melhor materializada no Brain. O sistema está alinhado com Hermes oficial e com Bruno/OpenClaw.

O único ajuste recomendado é **compactar o `USER.md` default**, não porque esteja conceitualmente errado, mas porque está alto demais para uma camada que deve ser boot mínimo.
