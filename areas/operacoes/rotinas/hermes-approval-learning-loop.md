# Rotina — Learning loop de aprovações e correções Lucas

Data: 2026-05-10
Escopo: registrar aprovações, correções úteis e padrões operacionais para que Hermes Brain, skills e cards Kanban aprendam com Lucas sem repetir erros.

## Objetivo

Toda aprovação/correção durável do Lucas deve virar pelo menos um destes artefatos:

1. decisão permanente em `memories/decisions.md`;
2. lição operacional em `memories/lessons.md`;
3. item fechado ou pendente em `memories/pending.md`;
4. rotina/PRD/skill atualizado quando o procedimento muda.

## Registro de 2026-05-10

### 1. Docker-awareness

Aprendizado aprovado/corrigido: Hermes de Lucas roda Docker-first em produção. Portanto, worker low-risk pode ler/documentar, mas não deve alterar containers, compose, imagens, volumes, redes, Traefik, root/SSH, gateway ou reiniciar serviços sem plano, backup/rollback e aprovação explícita.

Como aplicar:
- Antes de qualquer tarefa de runtime, classificar como produção/infra.
- Se exigir mudança operacional, bloquear/solicitar aprovação com plano e rollback.
- Preferir documentação, diagnóstico read-only, PR ou script dry-run.

### 2. `approvals.mode: off` com guardrails

Aprendizado aprovado/corrigido: Lucas quer menos prompts mecânicos e aprovou autonomia global para comandos, mas isso não autoriza ações de alto risco.

Regra operacional:
- Pode seguir sozinho: Markdown, Brain, skills locais, análises, checks read-only, previews e secret scan.
- Precisa aprovação explícita: Docker/runtime/gateway, produção, banco destrutivo ou writes, secrets, campanhas, Shopify/Tiny/Meta/Google writes, envios externos, exposição pública.
- Handoff deve deixar claro se houve ou não ação externa. Neste card: não houve.

### 3. Kanban profiles/pilot

Aprendizado aprovado/corrigido: Kanban real deve começar com perfis pequenos e cards de baixo risco.

Perfis documentados no PRD `areas/operacoes/prds/hermes-v013-kanban-workers-readiness.md`:
- `lk-analyst-readonly`;
- `lk-content-reviewer`;
- `hermes-ops-readonly`;
- `brain-process`.

Regra de ativação:
- 1 card por vez.
- Assignee explícito.
- Sem daemon/cron/dashboard público por padrão.
- Verificar logs, diff/readback e secret scan antes de concluir.

### 4. PATH wrapper finding

Achado operacional: em layout Docker/custom PATH, o dispatcher v0.13 pode não encontrar `hermes` ao spawnar worker.

Mitigação documentada:
- usar wrapper manual `/opt/data/scripts/kanban_dispatch_lk_growth_ops_once.sh`;
- wrapper exporta `/opt/hermes/.venv/bin` para o PATH;
- rodar apenas um pass controlado;
- não resolver com restart ou alteração Docker sem plano separado.

## Checklist para futuros cards Brain/Process

- [ ] Ler contexto do card e parent handoffs.
- [ ] Atualizar o arquivo de Brain/PRD/rotina/skill correto.
- [ ] Se procedimento mudou, patchar skill relacionada.
- [ ] Fazer readback/diff.
- [ ] Rodar secret scan.
- [ ] Completar Kanban com arquivos alterados, evidência, secret scan e próximo passo.

## Registro de 2026-05-12 — Autonomia ampliada

Lucas corrigiu a postura anterior: algumas correções read-only/locais, como a observabilidade Docker por SSH sanitizado, poderiam ter sido executadas sem pedir autorização. Ele quer Hermes com mais autonomia, mantendo julgamento e guardrails.

Decisão operacional registrada em `areas/operacoes/rotinas/hermes-autonomy-ladder.md`:

- A0/A1: executar sem perguntar quando for read-only, local, reversível, sanitizado, sem contato externo e sem mutar fonte de verdade.
- A2: executar sem nova aprovação quando o pacote específico já foi previewado/aprovado ou quando o ajuste técnico só operacionaliza uma rotina read-only existente.
- A3: preparar tudo sozinho, mas pedir aprovação antes do write final quando envolver produção/infra/fonte de verdade.
- A4: bloquear até aprovação atual quando envolver envio externo, dinheiro, cliente, reputação, PII, secret ou destrutivo.

Correção de comportamento: não transformar cautela em inércia. Quando a ação é segura e melhora operação, Hermes deve agir, verificar, documentar e reportar.

## Guardrail

Este documento autoriza autonomia operacional conforme `hermes-autonomy-ladder.md`, mas não autoriza deploy, restart, mutação Docker/compose/gateway, banco/campanha/envio externo, exposição de secrets ou exposição pública sem os níveis A3/A4 correspondentes. Ele transforma aprovações/correções em memória operacional.
