# Check — Organograma Hermes vs lógica Bruno/Amora

Data: 2026-05-30
Escopo: auditoria local/read-only da documentação do organograma, matriz de roteamento, pacotes de identidade dos agentes e alinhamento com a lógica Bruno/Amora.

## Veredito curto

O organograma está bem documentado e segue corretamente a lógica Bruno/Amora: `AGENTS.md`/organograma vivo define quem é cada agente, quem chama quem, onde vive, permissões, fronteiras, handoff e governança.

O Hermes/Cimino está estruturalmente correto para multiempresa: uma Grande Mente central/COO, especialistas como braços de execução, Brain como fonte de verdade e approval gates para produção/externo.

## Evidências verificadas

Documentos canônicos lidos/verificados:

- `empresa/contexto/organograma-agentes-hermes.md`
- `empresa/contexto/organograma-orquestrador-tarefas-hermes.md`
- `empresa/contexto/matriz-roteamento-tarefas-hermes.md`
- `empresa/contexto/matriz-agentes-profiles-bots-crons-status-2026-05-26.md`
- `empresa/contexto/task-router-hermes.md`
- referências anteriores de auditoria Hermes vs Amora em `reports/governance/`

Pacotes mínimos de identidade verificados com cobertura 8/8 para:

- `agentes/hermes-geral/`
- `agentes/mordomo/`
- `agentes/lk/`
- `areas/lk/sub-areas/growth/`
- `areas/lk/sub-areas/atendimento/`
- `areas/lk/sub-areas/shopify/`
- `areas/lk/sub-areas/trends/`
- `agentes/spiti/`
- `agentes/zipper/`

Arquivos mínimos considerados:

- `SOUL.md`
- `IDENTITY.md`
- `USER.md`
- `AGENTS.md`
- `MAPA.md`
- `HEARTBEAT.md`
- `TOOLS.md`
- `MEMORY.md`

## Runtime / profiles verificados

Profiles ativos/documentados:

- Main Hermes: `/opt/data`
- Mordomo: `/opt/data/profiles/mordomo`
- LK Growth: `/opt/data/profiles/lk-growth`
- LK Ops/Atendimento: `/opt/data/profiles/lk-ops`
- LK Shopify: `/opt/data/profiles/lk-shopify`
- LK Trends: `/opt/data/profiles/lk-trends`
- SPITI: `/opt/data/profiles/spiti`

Profiles auxiliares/preparados com token, mas não promovidos automaticamente a agentes operacionais:

- `brain-process`
- `hermes-ops-readonly`
- `lk-analyst-readonly`
- `lk-content-reviewer`

Decisão correta mantida: não autoativar esses perfis só porque têm token; eles precisam de decisão explícita para virar agente Telegram operacional.

## Atualização feita nesta auditoria

Foram atualizados os documentos locais:

- `empresa/contexto/organograma-agentes-hermes.md`
- `empresa/contexto/matriz-agentes-profiles-bots-crons-status-2026-05-26.md`

A atualização registrou:

- pacote documental mínimo agora completo para especialistas ativos;
- watchdog global canônico `b78ae7ac81d0`;
- cobertura do watchdog: Main check-only + Mordomo + LK Growth + SPITI + LK Ops + LK Shopify + LK Trends;
- regra de não auto-start para profiles prepared/read-only com token.

## Lacunas restantes

1. **Rotinas antigas ainda hospedadas em Main/Mordomo**
   - LK Ops e Zipper ainda têm algumas rotinas executadas fora do dono lógico por histórico.
   - Isto está documentado; migração exige aprovação escopada e classificação linha a linha.

2. **Crons próprios ausentes em alguns especialistas**
   - LK Ops, LK Shopify, LK Trends e SPITI não têm registry próprio consolidado observado.
   - Isso não é erro por si só; precisa ser declarado como escolha ou pendência antes de criar/migrar cron.

3. **Zipper segue documental/read-only**
   - Correto neste momento.
   - Runtime/bot dedicado só deve existir com gatilho objetivo de volume, risco ou canal.

4. **Ritual vivo ainda é o principal ponto de maturidade**
   - A estrutura documental está boa.
   - O próximo nível estilo Amora é consistência diária do ciclo: pedido → executor certo → preview/ação segura → receipt → handoff → Brain → skill/rotina.

## Nota executiva

- Documentação estrutural: 9/10.
- Aderência à lógica Bruno/Amora: 8.7/10.
- Maturidade ritual viva: 8/10.
- Risco principal: drift entre dono lógico, runtime atual e cron registry se não houver revisão periódica.

## Recomendação

Não criar novos agentes agora. O próximo ganho é manter a governança viva:

1. revisar mensalmente a matriz agente → profile → bot → cron → dono lógico;
2. padronizar receipts/handoffs de outputs materiais;
3. classificar profiles auxiliares como ativo, experimento, arquivo ou candidato a pausa;
4. só migrar crons ou criar novos runtimes com aprovação explícita e rollback.
