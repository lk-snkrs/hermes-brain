# Hermes v0.14 — Guia rápido para Lucas

Data: 2026-05-16 08:40 BRT  
Fonte: GitHub release `NousResearch/hermes-agent` tag `v2026.5.16` + runtime local confirmado em `Hermes Agent v0.14.0 (2026.5.16)`.  
Objetivo: fechar o ciclo pós-update: não apenas confirmar que voltou, mas ensinar o que muda no uso diário e o que entra no mecanismo do Hermes.

## Como pensar o v0.14

A v0.14 é uma release de fundação. Para Lucas, o principal não é “tem Windows/PyPI”, mas sim que o Hermes ganhou mais mecanismos para virar cérebro operacional:

- sessões transferíveis (`/handoff`);
- subobjetivos (`/subgoal`);
- watchers mais limpos/silenciosos;
- botões de clarificação/aprovação;
- verificação de mutação de arquivos;
- diagnósticos LSP em `write_file`/`patch`;
- browser/CDP muito mais rápido;
- prompt caching cross-session;
- proxy local OpenAI-compatible;
- mais base para webhooks/Microsoft Graph/Teams.

## O que Lucas deve usar manualmente

### 1. `/subgoal`

Use quando uma missão longa já existe, mas aparece uma prioridade nova dentro dela.

Exemplo:

```text
/subgoal dentro do Zipper OS, priorizar follow-ups parados de colecionadores e criar rascunhos draft-only
```

Quando usar:

- Zipper OS já está em andamento e você quer adicionar foco;
- LK ou SPITI precisa entrar sem trocar completamente o objetivo;
- você sente que eu estou fazendo uma parte, mas faltou uma subfrente.

Sinal de uso errado:

- usar `/subgoal` para tarefa solta de 1 passo. Nesse caso, mande uma mensagem normal.

### 2. `/handoff`

Use quando quiser transferir o trabalho para outro modo/modelo/persona sem perder o contexto.

Exemplo conceitual:

```text
/handoff para modo mais técnico para revisar esse PRD do Zipper OS
```

Quando usar:

- tarefa ficou técnica demais para o modo COO;
- quer passar de estratégia para execução/código;
- quer review mais crítico sem começar do zero.

Regra: ainda preciso respeitar guardrails de produção/cliente/externo.

### 3. Botões/clarify

A v0.14 melhora aprovações com botões em Telegram/Discord. O uso ideal é eu passar a perguntar decisões como:

- Aprovar;
- Ajustar;
- Bloquear;
- Ver rollback.

Isso deve reduzir texto e ambiguidade em A2/A3/A4.

### 4. Watchers silenciosos

O padrão bom é:

- OK = silêncio;
- problema real = Telegram;
- falso positivo = corrigir expectativa e documentar.

Aplicado hoje: o watchdog estava certo em alertar drift, mas depois do upgrade aprovado precisava atualizar expectativa de v0.13 para v0.14.

### 5. Webhooks / eventos

Ainda não é para abrir nada público sem plano, mas a direção é Hermes reagir a eventos:

- novo lead;
- novo e-mail importante;
- erro de cron;
- release nova;
- webhook de app interno.

Guardrail: qualquer endpoint público ou API Server exposto é infra/security A3/A4.

## O que Hermes deve adotar automaticamente

### A. Pós-update completo

Depois de qualquer update, não basta responder “voltou”. O ciclo correto é:

1. verificar runtime;
2. verificar gateway/API/Telegram;
3. reconciliar watchdogs/helpers;
4. atualizar prompt do cron principal;
5. atualizar skill/memória/Brain;
6. criar guia de uso para Lucas;
7. rodar de novo o `Lucas Brain daily intelligence loop`;
8. reportar o que foi implementado e o que Lucas deve aprender.

### B. Release-to-operations matrix

Toda novidade do Hermes precisa cair em uma das categorias:

- implementar agora;
- ensinar Lucas;
- usar como padrão interno;
- propor com aprovação;
- ignorar por enquanto.

### C. Menos relatório técnico, mais briefing COO

O relatório deve dizer:

- o que mudou;
- o que foi aplicado;
- o que eu aprendi;
- como isso muda seu uso diário;
- qual decisão precisa de você.

## Novidades v0.14 classificadas para Lucas

### Implementar agora / padrão interno

- Reconciliar watchdogs após update.
- Usar verifier/LSP como base de confiança para arquivos/código.
- Usar browser/CDP mais agressivamente em QA quando necessário.
- Preferir watchers silenciosos para monitoramento.
- Atualizar cron das 02h para pensar no mecanismo do próprio Hermes.

### Ensinar Lucas

- `/subgoal` para subprioridades dentro de missões longas.
- `/handoff` para transferir sessão/contexto para outro modo.
- Aprovações com botões quando disponíveis na conversa.

### Propor com aprovação antes de mexer

- Proxy local OpenAI-compatible para conectar Codex/Aider/Cline a provedores OAuth.
- API Server/webhooks públicos.
- Microsoft Graph/Teams pipeline em produção.
- Exposição de qualquer endpoint ou mudança Docker/Traefik.

### Irrelevante ou baixo impacto imediato

- Native Windows e PyPI são bons para portabilidade, mas não mudam o runtime Docker atual do Lucas.
- LINE/SimpleX só entram se houver canal de negócio real.

## Correção de comportamento aplicada

Lucas corrigiu: eu parei cedo demais ao dizer apenas que Hermes voltou. A resposta correta pós-update é fechar o ciclo operacional.

Nova regra operacional: depois de atualização/runtime novo, Hermes deve completar o ciclo de adoção e ensino, não apenas saúde/uptime.
