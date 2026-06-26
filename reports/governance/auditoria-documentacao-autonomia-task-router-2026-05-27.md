# Auditoria da documentação Hermes — autonomia, organograma e Task Router

Data: 2026-05-27

## Escopo

Auditoria local/read-only da documentação de governança criada/alterada na frente Organograma Hermes vs Amora, com foco em:

- organograma de agentes;
- matriz de roteamento;
- Task Router;
- regra de autonomia em 3 níveis;
- UX anti-loop de aprovação;
- interpretação de `seguir`.

Nenhuma ação de runtime, Docker, VPS, gateway, cron ativo, produção ou write externo foi executada.

## Veredito

A arquitetura está correta, mas a documentação tinha risco de drift por repetir a política de autonomia em vários arquivos e manter status antigo de “Fase 1 documental” em documentos que já descrevem runtime/dispatcher/guardrails ativos.

## Correções aplicadas

1. Criada fonte canônica:
   - `empresa/contexto/politica-autonomia-aprovacao-hermes.md`

2. Atualizados os documentos principais para apontarem para a fonte canônica:
   - `AGENTS.md`
   - `empresa/contexto/organograma-agentes-hermes.md`
   - `empresa/contexto/matriz-roteamento-tarefas-hermes.md`
   - `empresa/contexto/task-router-hermes.md`
   - `empresa/contexto/organograma-orquestrador-tarefas-hermes.md`

3. Atualizados headers/status de matriz/router/orquestrador:
   - de “Fase 1 documental” para documentos operacionais vivos, com runtime/guardrails em evolução.

4. Reforçada regra de linguagem:
   - `seguir` sozinho é continuidade local/read-only/documental;
   - `seguir` sozinho não aprova A3/A4, write externo, produção, contato externo, Docker/VPS/Traefik/root/SSH, secrets ou ação fora do escopo aprovado.

## Validação

- `scripts/test_hermes_task_router.py`: 9 passed.
- `scripts/brain_health_check.py --json reports/brain-health-check-2026-05-27-autonomia-docs.json`: 0 FAIL.
- Secret scan do Brain health check: 0 FAIL / 0 WARN.
- Link check do Brain health check: 0 FAIL / 0 WARN.

Warnings remanescentes do health check são pré-existentes/fora do escopo desta auditoria:

- `areas/hermes` sem `MAPA.md`;
- 9 rotinas não indexadas em `empresa/rotinas/_index.md`.

## Próximo ajuste recomendado

Fazer uma passada separada só de higiene do Brain:

1. indexar rotinas legítimas no `_index.md`;
2. decidir se `areas/hermes/MAPA.md` deve existir ou se `areas/hermes/` deve ser arquivada;
3. separar histórico de implementação de política canônica nos docs longos do Task Router.
