# Auditoria — Workers/subagentes temporários nos 3 agentes LK

Data: 2026-06-06T12:57Z UTC
Escopo: LK Growth, LK Shopify, LK Collection Optimizer / LKGOC
Modo: read-only/local; nenhuma ação externa; nenhuma credencial preservada.

## Pergunta auditada

Lucas perguntou se os três agentes LK que foram criados/ensinados estão realmente chamando subagentes/workers automaticamente quando iniciam uma tarefa, ou se apenas estão documentados.

## Veredito executivo

Lucas está majoritariamente certo na suspeita.

Os três agentes têm a regra documentada: classificar a demanda, escolher o playbook canônico e acionar automaticamente o subconjunto mínimo de workers/subagentes temporários.

Mas a evidência runtime é desigual:

- LK Growth: documentado; runtime tem capacidade e uso antigo de `delegate_task`, mas sem prova forte pós-2026-06-05 do novo fluxo automático por conversa.
- LK Shopify: documentado; há evidência parcial de sessões/background/sibling subagent, mas sem receipt limpo por turno dizendo quais workers foram acionados.
- LK Collection Optimizer/LKGOC: documentado e sabe responder em smoke test, mas não há chamadas `delegate_task` nem execução nomeada de workers no runtime auditado.

Portanto: documentação existe; mecanismo operacional/observabilidade ainda não está fechado. A correção correta não é criar mais agentes permanentes; é reforçar nos três profiles o contrato local de execução + receipt: demanda classificada → playbook escolhido → workers selecionados/omitidos → execução → consolidação pelo agente dono.

## LK Growth

### Documentação

Status: OK.

Evidências:
- `profiles/lk-growth/skills/productivity/lk-growth-operations/SKILL.md` define LK Growth como agente permanente, workers temporários internos por execução e seleção automática do subconjunto mínimo.
- `profiles/lk-growth/skills/productivity/lk-growth-operations/references/lk-growth-agent-worker-playbooks-20260605.md` define subconjuntos por playbook.
- `areas/lk/sub-areas/growth/templates/index-playbooks-lk-growth-20260605.md` registra a regra canônica.
- `areas/lk/sub-areas/growth/agentic-os/FASE-1B-LK-GROWTH-OS-20260605.md` repete a regra.

### Runtime

Status: parcial/não conclusivo.

Evidências:
- Delegation configurado no profile: `orchestrator_enabled=True`, `max_concurrent_children=3`, `max_spawn_depth=1`, `subagent_auto_approve=False`.
- Há uso real antigo de `delegate_task` nos logs/sessions.
- Busca no state local mostrou ocorrências textuais de `delegate_task` e `subagent`.

Lacuna:
- Não foi encontrada evidência forte pós-2026-06-05 de execução automática do novo padrão `classificar → playbook → subconjunto mínimo` em conversas recentes.
- Algumas rotinas com toolsets restritos podem não ter `delegation` habilitado.
- Boot memory local não reforça a regra.

## LK Shopify

### Documentação

Status: OK.

Evidências:
- `profiles/lk-shopify/skills/productivity/lk-shopify-readonly/SKILL.md` define LK Shopify como agente permanente e workers temporários internos por execução.
- `profiles/lk-shopify/skills/productivity/lk-shopify-readonly/references/lk-shopify-agent-worker-playbooks-20260605.md` exige classificação, playbook canônico e subconjunto mínimo automático.
- `areas/lk/sub-areas/shopify/agentic-os/LK-SHOPIFY-WORKER-OS-20260605.md` registra worker OS e ativação automática.
- `areas/lk/sub-areas/shopify/agentic-os/FASE-1B-LK-SHOPIFY-OS-20260605.md` registra workers temporários selecionados automaticamente.
- `areas/lk/sub-areas/shopify/MAPA.md` aponta para o OS operacional.

### Runtime

Status: parcial.

Evidências:
- Delegation configurado no profile: `orchestrator_enabled=True`, `max_concurrent_children=3`, `max_spawn_depth=1`, `subagent_auto_approve=False`.
- Há sessões `bg_*`, background tasks e warning de sibling subagent no runtime.
- Há conversa em que o agente diz que pretende usar workers mínimos.

Lacuna:
- Não foi encontrada chamada explícita limpa de `delegate_task` no fluxo recente LK Shopify.
- Não há receipt estruturado por demanda com workers selecionados e omitidos.
- Boot memory local não resume a regra dos workers.
- Termos runtime (`bg_*`, worker, sibling subagent) não casam com os nomes semânticos dos workers LK Shopify, o que dificulta auditoria.

## LK Collection Optimizer / LKGOC

### Documentação

Status: OK.

Evidências:
- `areas/lk/sub-areas/collection-optimizer/AGENTS.md` define o agente permanente e lista 8 workers temporários:
  1. Collection Intake Classifier
  2. Evidence & SERP Researcher
  3. LKGOC Experience Architect
  4. Guia LK Editorial Writer
  5. Shopify DEV Preview Builder
  6. Visual QA Mobile/Desktop Worker
  7. SEO/GEO Validator
  8. Rollback & Receipt Verifier
- `areas/lk/sub-areas/collection-optimizer/MEMORY.md` registra workers temporários/on-demand e nunca todos por padrão.
- `profiles/lk-collection-optimizer/skills/lk-superpowers-collection-optimizer/SKILL.md` exige escolher automaticamente o subconjunto mínimo de workers por demanda.
- `references/ownership-and-handoff-20260606.md` separa agentes permanentes de subagents/child tasks temporárias.
- `agentic-os/FASE-1B-LK-COLLECTION-OPTIMIZER-OS-20260606.md` registra worker pool temporário nomeado e também admite que runtime/channel round-trip ainda precisa ser validado.

### Runtime

Status: insuficiente.

Evidências:
- Delegation configurado no profile: `orchestrator_enabled=True`, `max_concurrent_children=3`, `max_spawn_depth=1`, `subagent_auto_approve=False`.
- Smoke test mostrou que o profile sabe responder corretamente sobre dono, pares Growth/Shopify, workers e guardrail de production.

Lacuna:
- `delegate_task`: 0 ocorrências no state auditado.
- Nenhuma execução nomeada dos workers LKGOC encontrada.
- Logs com `kanban dispatcher` não provam workers LKGOC semânticos.
- Falta receipt de workers selecionados/omitidos.

## Diagnóstico sistêmico

1. A documentação ensinou o comportamento.
2. A configuração permite delegação nos três profiles.
3. Porém `subagent_auto_approve=False` e a ausência de receipts tornam impossível afirmar que todo início de tarefa aciona workers automaticamente.
4. O padrão atual parece depender do agente lembrar/decidir usar workers durante a conversa, não de um contrato obrigatório e observável.
5. Para Lucas, a suspeita é correta: em especial no LKGOC, provavelmente ele não está chamando subagentes reais de forma automática quando conversa com o profile.

## Correção recomendada

Sem criar novos agentes permanentes:

1. Patchar as skills locais dos três profiles para incluir um bloco obrigatório `Worker Invocation Contract`:
   - classificar demanda;
   - escolher playbook;
   - listar workers selecionados;
   - listar workers omitidos e motivo;
   - acionar `delegate_task` quando a tarefa tiver 2+ trilhas independentes ou investigação/execução paralelizável;
   - consolidar resposta no agente dono;
   - registrar receipt local.
2. Patchar boot memory dos três profiles com uma linha curta sobre seleção automática de workers mínimos.
3. Criar template de receipt comum:
   - `workers_selected`
   - `workers_skipped`
   - `delegation_tool_used: yes/no`
   - `reason_if_no_delegation`
   - `owner_agent_final_decision`
4. Rodar smoke test em cada profile com uma tarefa simulada e exigir prova no receipt.
5. Só depois afirmar maturidade operacional completa.

## Segurança

- Nenhuma ação externa executada.
- Nenhum write em Shopify/Tiny/GMC/GitHub/prod.
- Nenhuma credencial preservada.
