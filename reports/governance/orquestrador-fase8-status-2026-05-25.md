# Orquestrador Hermes — Fase 8 status e lacunas

Data/hora de auditoria: 2026-05-25T00:28Z  
Owner: Hermes Geral / COO  
Escopo: local/read-only, Brain docs, cron registry e testes locais.  
Writes externos: não.

## Resumo

Status da Fase 8: **parcialmente completa / operacional como base v2, ainda em observação**.

A orquestração já tem Task Router, contratos de handoff, Zipper documental/read-only, ledger central e Mesa COO v2 configurada. O que ainda falta para chamar de fase madura é observar a próxima execução real da Mesa no Telegram limpo, transformar mais outputs reais de especialistas em handoffs consistentes e corrigir falsos positivos/negativos de roteamento conforme surgirem casos reais.

## Checklist Fase 8

### 1. Contratos mínimos de handoff por especialista

Status: **feito com ajuste em 2026-05-25**.

Evidências:

- `empresa/contexto/contratos-handoff-especialistas.md`
- `templates/handoff-especialista.md`
- `agentes/hermes-geral/AGENTS.md`
- `agentes/lk/AGENTS.md`
- `areas/lk/sub-areas/growth/AGENTS.md`
- `areas/lk/sub-areas/growth/HEARTBEAT.md`
- `agentes/mordomo/AGENTS.md`
- `agentes/spiti/AGENTS.md`
- `agentes/zipper/AGENTS.md`
- `agentes/zipper/HEARTBEAT.md`

Ajuste aplicado nesta rodada:

- `areas/lk/sub-areas/growth/HEARTBEAT.md` agora declara handoff obrigatório, ledger, template, `Writes externos: não` para execução read-only/local e bloqueios sem aprovação.
- `empresa/contexto/contratos-handoff-especialistas.md` agora inclui seção específica para Operações Hermes / Brain / runtime governance.

### 2. Zipper v1 documental/read-only

Status: **feito como contrato documental; runtime dedicado continua fora de escopo**.

Evidências:

- `areas/zipper/contrato-operacional-readonly.md`
- `agentes/zipper/AGENTS.md`
- `agentes/zipper/HEARTBEAT.md`
- `empresa/contexto/matriz-roteamento-tarefas-hermes.md`, rota `zipper-os-readonly-comm-crm`
- `empresa/contexto/task-router-hermes.md`, caso especial “Zipper sem profile dedicado”

Limite:

- Sem bot/profile Zipper dedicado nesta fase.
- Sem WhatsApp/e-mail/CRM/banco/site/cron/runtime write.
- Proposta, preço, disponibilidade, contato externo e logística sensível seguem approval-gated.

### 3. Handoff ledger

Status: **feito como estrutura; maturidade depende de uso contínuo**.

Evidências:

- `empresa/contexto/handoff-ledger.md`
- `empresa/contexto/handoffs/`
- `templates/handoff-especialista.md`

Lacuna restante:

- Garantir que os próximos outputs materiais de LK Growth, Mordomo, SPITI e Zipper realmente registrem handoff, não apenas produzam relatório local.

### 4. Mesa COO v2

Status: **configurada e testada; falta observar próxima entrega real pós-ajuste**.

Evidências:

- Cron vivo “Mesa COO diária Telegram” ativo, com entrega para Telegram.
- Skill `mesa` com contrato v2: uma decisão por vez, máximo quatro, sem metadata técnica, sem tabela, com botões nativos via scheduler quando cron.
- Testes de scheduler cobrem supressão de wrappers técnicos e marker de botões.

Lacuna restante:

- Validar visualmente a próxima execução real no Telegram: mensagem curta, sem wrapper, sem job id, sem JSON, sem marcador HTML visível.

### 5. Task Router cobre lacunas secundárias

Status: **feito para as lacunas principais identificadas**.

Evidências:

- `empresa/contexto/matriz-roteamento-tarefas-hermes.md` cobre LK Growth conteúdo, LK Growth analytics, LK Ops sensível, Mordomo, Zipper read-only, SPITI, Hermes Ops, Tech/Infra e pesquisa geral.
- `empresa/contexto/task-router-hermes.md` documenta Fase 7 e Fase 7B, incluindo runtime preflight, hard block e handoff packets.

Lacuna restante:

- Monitorar casos reais para detectar rotas genéricas indevidas ou especialistas errados. Isso é maturidade operacional, não bloqueio documental.

### 6. Silent-OK / proatividade supervisionada

Status: **contrato estabelecido; execução recorrente deve continuar com baixa emissão**.

Evidências:

- `agentes/hermes-geral/HEARTBEAT.md`
- `agentes/*/HEARTBEAT.md`
- Cron registry mostra watchdogs críticos com delivery local/silent-OK e relatórios obrigatórios separados de alertas.

Limite:

- Não criar novo cron nem mudar delivery/cadência sem aprovação explícita.

## Riscos atuais

1. **UX da Mesa real ainda precisa de observação:** testes passam, mas a prova final é a próxima entrega Telegram limpa.
2. **Ledger pode virar documento morto:** mitigação é registrar apenas outputs materiais/decisões e não saúde normal.
3. **Zipper ainda não tem runtime dedicado:** isso é deliberado; hoje o comportamento seguro é documental/read-only.
4. **Brain repo tem muitos arquivos modificados/untracked de outras frentes:** não tratar como problema da Fase 8 sem auditoria específica; evitar commits amplos ou sync manual fora do escopo.

## Próximo passo recomendado

1. Observar a próxima Mesa COO no Telegram.
2. Se vier limpa, marcar P8.3 como operacionalmente validado.
3. Se vazar wrapper/metadata, tratar como regressão de scheduler/gateway e corrigir com teste antes de qualquer novo prompt tweak.
4. Nas próximas execuções de especialistas, exigir handoff no ledger usando o template.

## Verificações executadas nesta rodada

- Data/hora: `date -Is`.
- Cron registry: `hermes cron list --all`, com nomes de jobs e status vivos.
- Git status do Brain: auditado; árvore contém múltiplas mudanças de outras frentes, portanto esta rodada não deve tentar commit/sync amplo.
- Busca/readback de contratos: AGENTS/HEARTBEAT, matriz de roteamento, Task Router, Zipper contract, ledger e template.
- Testes focados Hermes: `/opt/hermes/.venv/bin/python -m pytest tests/cron/test_scheduler.py tests/agent/test_lucas_task_router_preflight.py -q` → `134 passed`, 1 warning de permissão do pytest cache.
- Brain health check: `python3 scripts/brain_health_check.py --json /tmp/brain_health_fase8.json` → `fail_count=0`, `warn_count=0`.
- Secret scan focado nos 4 arquivos alterados/criados nesta rodada → OK.

## Ações executadas nesta rodada

- Patch local/read-only em `areas/lk/sub-areas/growth/HEARTBEAT.md`.
- Patch local/read-only em `empresa/contexto/contratos-handoff-especialistas.md`.
- Criação deste relatório de status.

Nenhuma ação externa, produção, Docker/VPS/gateway, cron, Shopify/GMC/Klaviyo/Meta/WhatsApp/e-mail ou cliente foi executada.
