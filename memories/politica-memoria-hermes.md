# Política de memória — Hermes Brain + Hermes Agent

Data: 2026-06-01  
Status: canônica para governança de memória curta/injetada vs memória rica.

## Tese canônica

A memória curta/injetada do Hermes (`MEMORY.md` e `USER.md`) deve ser **boot mínimo curado**: identidade, preferências, guardrails e ponteiros de navegação.

A memória rica deve existir fora do prompt fixo, em camadas consultáveis.

## Resumo canônico de camadas

- **Hermes Brain**: memória rica canônica, fonte de verdade documental/operacional curada.
- **`MEMORY.md` / `USER.md`**: boot mínimo injetado no prompt — preferências estáveis, guardrails globais e ponteiros curtos.
- **daily / hot / reports / receipts**: continuidade, evidência, estado current, auditorias e recibos de alteração.
- **skills**: procedimentos repetíveis, troubleshooting, runbooks, checklists com verificação/rollback.
- **`session_search`**: histórico conversacional e origem de decisões que ainda não foram materializadas no Brain.
- **Mem0/provider externo**: decisão atual é **não usar**; Brain é a fonte rica canônica. Só reabrir com novo PRD/spike explícito de Lucas.

Camadas consultáveis detalhadas:

- Hermes Brain (`memories/`, `areas/`, `empresa/`, `agentes/`);
- daily notes;
- `hot.md` para contexto current;
- context files (`AGENTS.md`, `.hermes.md`, `SOUL.md`, MAPAs);
- skills para procedimentos repetíveis;
- `session_search` para histórico conversacional;
- reports/archive/receipts para evidência;
- provider externo de memória: atualmente rejeitado/off; só reabrir com novo PRD/spike explícito.

## Por quê

A documentação oficial do Hermes define a memória built-in como pequena e curada:

- `MEMORY.md`: notas do agente, ambiente, convenções, aprendizados — limite padrão 2.200 chars.
- `USER.md`: perfil/preferências do usuário — limite padrão 1.375 chars.
- Ambas são injetadas no system prompt no início da sessão como snapshot congelado.
- Mudanças via memory tool persistem em disco, mas só entram no prompt em nova sessão.

Logo, `MEMORY.md`/`USER.md` não devem guardar Brain inteiro, status operacional vivo, receipts longos, PRs, logs, IDs efêmeros, rotinas completas ou histórico bruto.

## Camadas e destino correto

### 1. Built-in memory do Hermes

Use para:

- preferências estáveis de Lucas;
- guardrails globais de segurança;
- ponteiros para fontes de verdade;
- mapa mínimo de profiles/domínios;
- convenções que ajudam quase todo turno.

Não use para:

- status de job/processo/deploy;
- IDs de PR/issue/commit/cron salvo se forem ponteiros estáveis e inevitáveis;
- conclusões temporárias;
- checklists longos;
- conteúdo que pertence a especialista específico;
- dados que mudam semanalmente.

Meta operacional: manter entre 40–60% do limite, aceitando picos curtos se houver consolidação.

### 2. `hot.md`

Use para:

- prioridades atuais;
- bloqueios atuais;
- decisões recentes que ainda afetam ação;
- links quentes para rotinas/receipts.

Remover ou arquivar quando deixar de ser current.

### 3. Daily notes

Use para:

- decisões do dia;
- entregas;
- handoffs;
- aprendizados;
- não-ações e bloqueios.

Daily é a primeira camada de preservação contra perda por compactação/restart.

### 4. Brain por área/profile

Use para:

- contexto durável de LK, Zipper, SPITI, Mordomo, Hermes/Infra;
- decisões por domínio;
- rotinas, templates, reports e receipts;
- identidade e escopo dos especialistas.

### 5. Skills

Use para:

- procedimento repetível;
- runbook;
- troubleshooting;
- padrão de auditoria/relatório;
- guardrail com verificação/rollback.

Regra: se repetiu 3 vezes, causou erro caro, ou Lucas corrigiu uma abordagem, vira skill ou referência.

### 6. Session search

Use para:

- recuperar conversa passada;
- localizar origem de decisão;
- evitar pedir para Lucas repetir contexto.

Não transformar todo histórico em memória injetada.

### 7. Reports/archive/receipts

Use para:

- evidência detalhada;
- auditorias;
- outputs longos;
- recibos de alteração;
- verificações.

O prompt fixo deve conter ponteiro para o report, não o report inteiro.

### 8. Provider externo de memória

**Decisão atual de Lucas: não usar Mem0/provider externo para memória Hermes.** Hermes Brain continua como memória rica canônica; `memory.provider` deve ficar vazio/off. Artefatos de canário/PRD anteriores são históricos/rejeitados, não backlog ativo. Só reabrir se Lucas pedir novo PRD/spike explícito, sem dados reais sensíveis e sem ativação automática.

## Índice operacional: onde procurar/salvar cada memória

Use este roteador antes de gravar informação nova:

- Preferência estável de Lucas, guardrail global, convenção que vale quase todo turno → `USER.md`/`MEMORY.md` built-in, em forma curta.
- Prioridade, bloqueio ou decisão que afeta a semana atual → `memories/hot.md`.
- Fato/decisão/entrega do dia → `memories/daily/YYYY-MM-DD.md`.
- Contexto durável por negócio/domínio → `areas/<domínio>/`, `agentes/<especialista>/`, `empresa/contexto/` ou `memories/*.md` curado.
- Procedimento repetível, troubleshooting, checklist com verificação/rollback → skill ou referência dentro de skill.
- Evidência detalhada, auditoria, receipt, rollback, readback, diff ou output longo → `reports/`, `receipts/` ou `archive/`, linkado a partir do MAPA/daily/hot quando necessário.
- Histórico de conversa ou origem de uma decisão que não foi materializada → `session_search` primeiro; só promover se virar regra/decisão.
- Dado vivo/operacional atual — estoque, pedido, métrica, status de gateway/cron/deploy/campanha → fonte real/API/CLI no momento; Brain guarda apenas ponteiro/receipt.
- Credenciais, tokens, senhas, refresh tokens, connection strings → nunca no Brain nem na memória injetada; consultar fonte segura autorizada e não imprimir valor.
- Conhecimento semântico amplo que exigiria recall automático → hoje permanece em Brain/session_search; provider externo está rejeitado/off até novo PRD explícito.

## Política de promoção/rebaixamento

Fluxo recomendado:

1. Conversa/execução acontece na sessão.
2. Se relevante, registrar no daily do dia.
3. Se afeta ação atual, adicionar/resumir em `hot.md`.
4. Se durável por domínio, mover para área/profile do Brain.
5. Se procedimento, criar/atualizar skill.
6. Se evidência longa, salvar em report/receipt e linkar.
7. Só promover para built-in memory se for estável, alto sinal e útil em quase todo turno.
8. Rebaixar/remover da built-in memory quando virar detalhe de domínio, ficar velho ou existir fonte melhor no Brain.

## Critérios rápidos

Perguntas antes de salvar em `MEMORY.md`/`USER.md`:

- Vai continuar verdadeiro em 30–90 dias?
- Ajuda quase todo turno?
- Não existe fonte melhor no Brain/skill/context file?
- É curto o suficiente para ser ponteiro, não conteúdo?
- Não é segredo, payload, log, status atual ou receipt?

Se qualquer resposta for “não”, não salvar na memória injetada.

## Estado local após correção 2026-06-01

Memória built-in do profile default foi compactada para boot mínimo:

- `MEMORY.md`: cerca de 1.092 chars de 2.200.
- `USER.md`: cerca de 1084 chars de 1.375 após P1 sem provider externo de memória.

A sessão atual pode continuar mostrando snapshot antigo até `/new` ou nova sessão, porque Hermes congela memória no início da sessão para preservar cache.

## Referência de validação

Relatório web salvo em:

`/opt/data/reports/hermes-memory-best-practices-web-validation-20260601.md`
