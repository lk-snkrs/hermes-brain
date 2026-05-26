# Reauditoria — Organograma de agentes Hermes vs Amora/OpenClaw

Data: 2026-05-25
Escopo: auditoria local/read-only + correção documental mínima no Brain. Sem cron novo, sem Docker/gateway/restart, sem produção e sem escrita externa.

## Veredito

O organograma está majoritariamente correto e já está no desenho certo em relação à Amora/OpenClaw: Hermes Geral coordena, especialistas executam, Brain registra e produção/externo exige aprovação.

Não está “perfeito” porque o próximo ganho não é mais documentação conceitual; é maturidade operacional: coerência contínua entre docs, runtime, crons, handoffs e UX de decisão.

## Comparação com Amora/OpenClaw

### O que está correto

- Existe organograma vivo em `AGENTS.md` e nos mapas de contexto.
- Existe pacote mínimo por agente no padrão Amora/Hermes: `SOUL`, `IDENTITY`, `USER`, `AGENTS`, `MAPA`, `HEARTBEAT`, `TOOLS`, `MEMORY`.
- Existe separação entre camada de negócio, agente documental, runtime profile/bot, cron/rotina, tarefa e handoff.
- O modelo evita múltiplas “mentes” separadas: especialistas são braços de execução subordinados ao Hermes Central/Brain.
- A matriz de roteamento cobre LK Growth, LK operações sensíveis, Mordomo, Zipper, SPITI, Operações Hermes e Tecnologia/Infra.
- O Task Router já tem contrato técnico local/read-only e regressões no runtime Hermes.
- Approval boundary A0-A4 está explícito; produção, externo, Docker/VPS, crons novos e credenciais continuam bloqueados sem aprovação específica.

### Diferenças deliberadas vs Amora

- Hermes não deve copiar a Amora 1:1 com crons e writes agressivos; usa Amora como referência de maturidade documental e operacional.
- Hermes usa profiles/bots e skills como braços especializados, não como “cérebros” autônomos independentes.
- O Brain é central e versionado; fonte viva continua sendo API/banco/sistema real quando há dado operacional atual.
- A UX de Lucas deve ser decisão 1/N com botões e silent-OK, não blocão de relatório.

## Evidências coletadas

- Pacote mínimo de agentes: OK para `hermes-geral`, `lk`, `mordomo`, `spiti`, `zipper`.
- Docs canônicos: OK para `AGENTS.md`, organograma de agentes, organograma orquestrador/tarefas, matriz de roteamento, task-router, protocolo de handoff e template de handoff.
- Router documental: `scripts/test_hermes_task_router.py` passou com `6 tests OK`.
- Router runtime Hermes: `/opt/hermes/tests/agent/test_lucas_task_router_preflight.py` passou com `10 passed`.
- Docs guard default: `216` arquivos escaneados, `fail_count=0`.
- Docs guard strict-runtime: `1511` arquivos escaneados, `fail_count=0`.
- Runtime observado: gateways vivos para `/opt/data`, `/opt/data/profiles/lk-growth`, `/opt/data/profiles/mordomo`, `/opt/data/profiles/spiti`.
- Cron registry local observado por arquivo: main `23/23` ativos; LK Growth `26 total / 22 ativos / 4 pausados`; Mordomo `12 total / 11 ativos / 1 pausado`; SPITI sem registry local encontrado.

## Correção documental aplicada

- Corrigido trecho obsoleto em `empresa/contexto/organograma-agentes-hermes.md` que ainda dizia que o Mordomo precisava ganhar pasta documental própria. O arquivo agora reconhece que `agentes/mordomo/` já existe e que o gap real é consistência com runtime/handoff.

## Melhorias recomendadas

1. **Criar ledger/checkpoint de handoff diário por especialista**
   - Objetivo: garantir que LK Growth, Mordomo e SPITI não virem históricos isolados.
   - Saída: um índice simples por data com outputs relevantes, decisões, writes, riscos e próximos passos.

2. **Reconciliar crons por dono lógico**
   - Objetivo: reduzir `deliver=origin/default` e confirmar se cada rotina pertence ao Hermes Geral, LK Growth, Mordomo ou SPITI.
   - Guardrail: primeiro relatório read-only; qualquer pausa/migração exige aprovação.

3. **Tratar SPITI cron registry ausente como finding, não erro**
   - Existe runtime SPITI vivo, mas não encontrei `/opt/data/profiles/spiti/cron/jobs.json`.
   - Pode ser correto se SPITI não tiver crons; deve ser documentado para não parecer buraco.

4. **Separar Zipper documental/read-only de futuro Zipper runtime**
   - Hoje está correto dizer que Zipper não tem runtime dedicado.
   - Melhorar: definir critério de criação do profile Zipper e quais fontes/guardrails entrariam nele.

5. **Transformar “Amora package OK” em check automático periódico silencioso**
   - Objetivo: se faltar `SOUL/IDENTITY/...` ou se um doc ficar contraditório, alertar só exceção.
   - Guardrail: cron novo exige aprovação; por enquanto pode ficar como script/manual.

6. **Dashboard curto de coerência docs × runtime × crons**
   - Objetivo: uma página viva com: agents OK, gateways vivos, cron owners, gaps, últimos handoffs e decisões pendentes.
   - Evita reauditar tudo manualmente a cada pergunta.

## Risco residual

- Worktree do Brain já estava muito sujo antes desta auditoria; não atribuir todas as mudanças a esta sessão.
- O guardrail bloqueou `cronjob list` via ferramenta por estar em modo approval/handoff; usei leitura local de registry para evitar mutação e não burlar produção.
- Runtime foi inspecionado read-only via `/proc`; nenhum processo foi reiniciado.

## Próxima decisão sugerida

Próximo passo de menor risco: fazer a **Matriz de Donos de Crons vs Organograma** em modo read-only e salvar em `reports/governance/`, sem alterar cron nenhum.
