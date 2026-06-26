# Approval Packet — Migração cron Pixel AI Hub para Hermes Agent

Data: 2026-05-25
Contexto: Operações Hermes / Hermes Agent
Pedido de Lucas: fazer itens 1 e 2 no agente Hermes, não no Mordomo, e transferir o cron para ele.

## Destino

Hermes Agent central / Operações Hermes.

## Pedido limpo

1. Promover os aprendizados 1 e 2 do digest Pixel AI Hub para rotina do Hermes Agent:
   - auditoria de cron com fonte primária e múltiplas superfícies;
   - diagnóstico de performance por camadas antes de limpeza/restart.
2. Migrar o cron `Pixel AI Hub / Brainzinho daily learning scan` para ownership/runtime do Hermes Agent central, removendo identidade Mordomo do prompt.

## Evidências read-only

- O output do cron em `profiles/mordomo/cron/output/c358f8f56a26/2026-05-25_23-32-21.md` recomenda adaptar os itens 1 e 2.
- O registro persistido do scheduler mostra o job histórico `Pixel AI Hub / Brainzinho daily learning scan` no profile Mordomo.
- O prompt atual começa com `Você é o Mordomo Hermes de Lucas Cimino`, o que conflita com a correção de Lucas.
- A rotina documental nova foi criada em `areas/operacoes/rotinas/hermes-agent-cron-e-performance-diagnostico.md`.
- O PRD Hermes Agent do loop foi criado em `areas/operacoes/prds/pixel-ai-hub-learning-loop-hermes-agent-2026-05-25.md`.

## Preview da migração real

A migração deve ser feita por ferramenta de cron/CLI, não por edição manual de `jobs.json`:

1. Backup antes:
   - copiar `/opt/data/profiles/mordomo/cron/jobs.json` para `reports/governance/cron-registry-backups/<timestamp>/mordomo-jobs.before.json`;
   - listar cron do runtime Hermes central.
2. Criar/atualizar job no Hermes Agent central:
   - nome: `Pixel AI Hub / Brainzinho daily learning scan — Hermes Agent`;
   - schedule: `30 23 * * *`;
   - delivery: `origin` só para achado relevante; ideal silent-OK em no-op;
   - skills: `pixel-ai-hub-learning-digest`, `wacli-whatsapp-cli`, `bruno-openclaw-hermes-brain-adaptation`, `hermes-agent`;
   - toolsets: `terminal,file`;
   - prompt corrigido: identidade Hermes Agent / Operações, sem “Mordomo”.
3. Pausar ou remover o job legado do Mordomo depois que o novo estiver validado.
4. Backup depois e receipt.
5. Rodar uma execução manual read-only/safe, sem WhatsApp send/reply/react.

## Risco

Baixo para documentação já feita. Médio para migração real porque altera scheduler/profile e pode gerar ruído Telegram ou duplicidade se o job legado não for pausado.

## Bloqueios

- Criação/alteração/pausa de cron real é mutação de runtime.
- Não executar por edição manual de `jobs.json`.
- Não mexer em gateway/Docker/VPS.

## Rollback

1. Pausar o novo job Hermes Agent.
2. Reativar o job legado do Mordomo temporariamente, com prompt corrigido se necessário.
3. Restaurar backup de cron apenas via ferramenta apropriada ou plano controlado.
4. Registrar receipt com antes/depois.

## Decisão necessária

Aprovar explicitamente a migração real do cron agora, com backup antes/depois e pausa do legado após validação.
