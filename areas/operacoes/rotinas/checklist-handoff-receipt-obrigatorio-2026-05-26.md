# Checklist — Handoff e receipt obrigatório

Data: 2026-05-26  
Owner: Hermes Geral / Governança  
Status: regra documental ativa para especialistas.

## Quando registrar handoff/receipt

Registrar no Brain quando houver qualquer um destes casos:

- decisão durável de Lucas;
- aprovação de write;
- execução de write local relevante;
- execução de write externo/produção;
- risco, bloqueio ou exceção;
- migração/pausa/alteração de cron;
- restart/alteração de gateway/profile/launcher;
- output material de especialista;
- mudança em escopo, dono lógico, guardrail ou rotina;
- aprendizado que deve virar skill/rotina.

## Campos mínimos

- Data/hora.
- Dono lógico.
- Executor/profile.
- Pedido limpo.
- Evidência usada.
- Ação feita ou bloqueada.
- Escopo da aprovação, se houve.
- Sistemas afetados.
- Preview/snapshot quando aplicável.
- Readback/verificação.
- Rollback.
- Próximo passo.

## Regra por risco

### A0/A1 — leitura, análise, preview

- Handoff só se gerar decisão, risco, output durável ou nova rotina.

### A2 — write local/Brain/PR/branch

- Receipt local com diff/arquivo, verificação e motivo.

### A3 — write externo controlado

- Receipt obrigatório com snapshot, preview, execução, readback e rollback.

### A4 — produção/sensível/destrutivo

- Approval packet antes.
- Receipt após.
- Se falhar, registrar falha e rollback/estado final.

## Ledger diário

Usar também `areas/operacoes/rotinas/ledger-handoff-especialistas-diario.md` como índice operacional por especialista. O ledger não é cron ativo por si só; é a rotina documental para consolidar outputs materiais sem transformar todo silent-OK em ruído no Telegram.

## Anti-padrões

- “Feito” sem readback.
- “Aprovado” sem escopo.
- Migrar cron sem backup.
- Restart sem prova de gateway saudável depois.
- Write externo sem receipt.
- Relatório no Telegram com job id, JSON, wrapper ou metadado técnico.
