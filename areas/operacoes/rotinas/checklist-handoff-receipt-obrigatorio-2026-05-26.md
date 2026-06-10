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

## Memory OS v1.12 — receipt writer obrigatório para receipt novo

Para receipt operacional novo, usar o wrapper local `receipt_writer`; ele salva no Brain, valida campos mínimos e chama o hook em uma única operação. Hook-only em receipt novo é `drift_receipt_hook_only` e não fecha o trabalho.

```bash
python3 /opt/data/scripts/hermes_memory_os_receipt_writer.py --path <caminho-do-receipt> --title '<título>' --empresa-area '<área>' --pedido '<pedido>' --fonte '<fonte>' --feito '<ação>' --output '<artefato>' --aprovacao '<escopo/aprovação>' --rollback '<rollback>' --documentado '<onde>'
```

O hook abaixo é fallback para handoff, approval packet, artefato legado já escrito ou receipt excepcional criado por outro meio com motivo registrado:

```bash
python3 /opt/data/scripts/hermes_memory_os_event_hook.py <caminho-do-artefato>
```

Wrapper/hook devem ficar silenciosos quando verdes. Se houver saída, tratar como alerta local/actionable antes de encerrar; Telegram só se houver decisão, falha atual não recuperada ou risco acionável.

## Checklist canônico — onde registrar memória/contexto

- Preferência durável do usuário/Lucas → `USER.md`.
- Guardrail global/regra de segurança/política de boot → `MEMORY.md`.
- Prioridade ou bloqueio current → `memories/hot.md`.
- Decisão, entrega ou pendência do dia → `memories/daily/YYYY-MM-DD.md`.
- Evidência, relatório, auditoria, receipt ou output material → Brain receipt/report/área dona.
- Procedimento reutilizável ou rotina repetível → skill, referência de skill ou rotina canônica.
- Dado vivo → fonte real primeiro; Brain guarda ponteiro/receipt/report e data da consulta.
- Conversa antiga → `session_search`; promover só se virar preferência estável, decisão durável, guardrail ou procedimento.

Critério de fechamento: se o registro criado for receipt operacional novo, deve haver evidência de `receipt_writer`; se já existia, deve ser regularizado com `receipt_writer --register-existing`; se for handoff/approval-packet/legado, deve haver evidência de hook.

## Ledger diário

Usar também `areas/operacoes/rotinas/ledger-handoff-especialistas-diario.md` como índice operacional por especialista. O ledger não é cron ativo por si só; é a rotina documental para consolidar outputs materiais sem transformar todo silent-OK em ruído no Telegram.

## Anti-padrões

- “Feito” sem readback.
- “Aprovado” sem escopo.
- Migrar cron sem backup.
- Restart sem prova de gateway saudável depois.
- Write externo sem receipt.
- Receipt operacional novo escrito manualmente sem `receipt_writer`, salvo exceção registrada e hook executado.
- Relatório no Telegram com job id, JSON, wrapper ou metadado técnico.
