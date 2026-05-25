# Task Router Hermes — Algoritmo Operacional

Data: 2026-05-24  
Status: aprovado para Fase 1 documental  
Matriz: `empresa/contexto/matriz-roteamento-tarefas-hermes.md`

## Objetivo

Transformar pedidos de Lucas em rotas de execução seguras, sem misturar empresas, sem usar o profile errado e sem executar produção/externo sem aprovação explícita.

## Contrato operacional

Hermes Geral deve decidir uma destas ações:

- `executar_aqui`
- `delegar_especialista`
- `preparar_approval_packet`
- `bloquear_por_aprovacao`
- `perguntar_clarificacao`
- `registrar_handoff`

Perguntar só quando a ambiguidade muda materialmente a rota ou o risco.

## Algoritmo

### Passo 1 — Classificar contexto

Escolha um contexto principal:

- `lucas_pessoal`
- `lk`
- `lk_growth`
- `zipper`
- `spiti`
- `operacoes_hermes`
- `tecnologia_infra`
- `governanca_segurança`
- `multiempresa`
- `desconhecido`

Se houver mais de uma empresa, separar fontes e outputs.

### Passo 2 — Classificar tipo de tarefa

Tipos principais:

- decisão/priorização;
- pergunta/análise;
- conteúdo/blog/source page/copy;
- SEO/CRO/GEO/GMC/analytics;
- atendimento/cliente/WhatsApp/e-mail;
- rotina/cron/watchdog;
- código/deploy/infra;
- banco/API/write;
- publicação/campanha/envio;
- documentação/PRD/governança.

### Passo 3 — Consultar matriz

Usar `empresa/contexto/matriz-roteamento-tarefas-hermes.md` para mapear:

```yaml
contexto: ...
tipo: ...
orquestrador: ...
executor: ...
runtime_profile: ...
output_path: ...
allowed_without_approval: ...
requires_approval: ...
handoff_required: ...
```

### Passo 4 — Determinar risco

Use níveis:

- **A0 — leitura/local:** pesquisa, leitura, documentação, draft local.
- **A1 — preview/packet:** proposta, approval packet, preview local/dev sem publicação.
- **A2 — write reversível interno:** arquivo no Brain, branch, PR, rollback local.
- **A3 — write externo controlado:** Shopify, GMC, Klaviyo, Supabase, Calendar, GitHub remoto, Vercel preview.
- **A4 — produção/sensível/destrutivo:** produção, cliente, dinheiro, preço, lance, Docker/VPS/root/Traefik/secrets, bulk/campanha.

Regra:

- A0/A1 geralmente podem avançar se dentro do escopo.
- A2 depende de escopo e segurança.
- A3/A4 exigem aprovação explícita atual com escopo.

### Passo 5 — Decidir ação

#### Executar aqui

Use quando:

- é governança central;
- é PRD/plano/documentação central;
- não há especialista dono;
- é pergunta simples com fonte clara;
- é verificação local/read-only.

#### Delegar especialista

Use quando:

- matriz define profile/bot dono;
- tarefa é operacional do domínio;
- qualidade depende do contexto especializado;
- exemplo obrigatório: conteúdo/blog/source page da LK → `lk-growth`.

Resposta esperada:

```text
Entendi. Isso é [especialista], não Hermes Geral.
Vou rotear para [profile/bot] e volto com o output/preview.
Sem write externo/produção até aprovação.
```

#### Preparar approval packet

Use quando:

- ação final exige aprovação;
- ainda é possível montar plano, evidência, rollback e preview sem write externo.

#### Bloquear por aprovação

Use quando o próximo passo executaria:

- produção;
- contato externo;
- preço/disponibilidade/reserva/negociação;
- cliente/colecionador/artista/bidder;
- Shopify/GMC/Klaviyo/Meta/Supabase write;
- Docker/VPS/root/SSH/Traefik/volumes/networks;
- cron novo sem cadência/kill criteria.

#### Perguntar clarificação

Use só quando:

- não dá para classificar empresa;
- o executor muda dependendo da resposta;
- o risco muda de A0/A1 para A3/A4;
- faltam destinatário/canal/conteúdo para ação externa.

### Passo 6 — Executar e verificar

Antes de responder “feito”:

- verificar arquivo/output existe;
- verificar guardrails básicos;
- confirmar que não houve write externo quando bloqueado;
- coletar path/link/receipt;
- registrar handoff se necessário.

### Passo 7 — Handoff

Se especialista executou trabalho relevante, exigir ou criar handoff mínimo:

- data/hora;
- agente/profile;
- empresa/área;
- pedido original;
- o que foi feito;
- fontes;
- output;
- aprovação;
- writes externos;
- riscos;
- próximos passos;
- onde foi documentado.

Template: `templates/handoff-especialista.md`.

## Pseudocódigo

```python
def route_task(request):
    context = classify_context(request)
    task_type = classify_task_type(request)
    route = lookup_matrix(context, task_type)
    risk = classify_risk(request, route)

    if risk in ["A3", "A4"] and not has_explicit_current_approval(request):
        return prepare_packet_or_block(route, risk)

    if route.executor and route.executor != "Hermes Geral":
        result = delegate_to_specialist(route, request)
        verify(result)
        handoff = ensure_handoff(result, route)
        return summarize_to_lucas(result, handoff)

    result = execute_here(request, route)
    verify(result)
    if route.handoff_required:
        record_handoff(result, route)
    return summarize_to_lucas(result)
```

## Implementação técnica v1 — local/read-only

A Fase 5 iniciou com um router técnico local em:

- `scripts/hermes_task_router.py`
- regressão: `scripts/test_hermes_task_router.py`

Contrato:

```bash
python3 scripts/hermes_task_router.py "faz uma source page da LK para New Balance 530"
```

Retorna JSON com:

- `route_id`
- `context`
- `task_type`
- `orchestrator`
- `executor`
- `runtime_profile`
- `action`
- `output_path`
- `allowed_without_approval`
- `requires_approval`
- `handoff_required`
- `rationale`

Escopo aprovado desta implementação:

- local/read-only;
- sem envio externo;
- sem alteração de crons;
- sem restart/gateway/Docker;
- sem Shopify/GMC/Klaviyo/Meta/Supabase/WhatsApp/e-mail writes;
- serve como camada de classificação/guardrail antes de enforcement em runtime.

Gatilhos cobertos por teste:

- LK source page/SEO/GEO/CRO → `lk-growth-content` / executor `lk-growth`.
- WhatsApp/preço/disponibilidade/reserva → `mordomo-personal-intake` com bloqueio por aprovação.
- SPITI/lote/lance/bidder → `spiti-os` com packet/aprovação.
- Zipper/proposta/preço/colecionador → `zipper-os-readonly-comm-crm` com bloqueio.
- Brain/crons/governança → `hermes-ops-brain-governance` / executar aqui quando documental.

Fase 6A/6B — runtime preflight metadata:

- Módulo runtime: `/opt/hermes/agent/lucas_task_router.py`.
- Integração: `/opt/hermes/run_agent.py` prepende metadata interna `HERMES TASK ROUTER PREFLIGHT` ao turno do modelo.
- Escopo: metadata-only/read-only, fail-open, sem writes externos e sem bloqueio hard no dispatcher de ferramentas.
- Relatório de implementação: `reports/governance/task-router-runtime-preflight-fase6a-2026-05-24.md`.
- Relatório de ativação: `reports/governance/task-router-runtime-preflight-fase6b-activation-2026-05-24.md`.
- Status: ativado no gateway principal após restart controlado aprovado; API, webhook e Telegram voltaram saudáveis.

Fase 6C — reply context + dispatcher hard block:

- Correção de roteamento em replies Telegram: o preflight classifica somente a instrução atual do Lucas, removendo o envelope `[Replying to: ...]` antes de chamar o router. Relatório: `reports/governance/task-router-reply-context-fix-fase6c-2026-05-24.md`.
- Bloqueio hard no dispatcher quando a rota exige approval/handoff: `send_message`, `cronjob`, interações browser mutantes, terminal/execute_code com padrões externos/produção e `delegate_task` são bloqueados antes de execução.
- Ferramentas read-only continuam permitidas para pesquisa, evidência, preview e approval packet local.
- Relatórios: `reports/governance/task-router-dispatcher-hard-block-fase6c-2026-05-24.md` e `reports/governance/task-router-dispatcher-guardrail-fase6c-2026-05-24.md`.
- Status: implementado e ativo no runtime atual; processo principal foi iniciado depois dos arquivos de guardrail e health checks API/webhook estão OK.

Fase 6D — UX limpa de decisão/approval packet Telegram:

- Correção em `/opt/hermes/cron/scheduler.py`: mensagens de decisão com `HERMES_INLINE_BUTTONS` têm o marcador extraído antes de qualquer wrapping legado; se houver metadata válida de botões, o scheduler suprime `Cronjob Response`, `job_id` e boilerplate de gestão mesmo quando `cron.wrap_response` estiver ligado.
- Regressão em `/opt/hermes/tests/cron/test_scheduler.py`: `test_inline_button_decision_delivery_suppresses_wrapper_even_when_enabled` garante Telegram limpo com botões nativos.
- Verificação: teste novo `1 passed`, classe `TestDeliverResultWrapping` `13 passed`, `py_compile` de scheduler/Telegram OK.
- Relatório: `reports/governance/task-router-telegram-clean-decision-ux-fase6d-2026-05-24.md`.
- Status: implementado, testado e ativo no runtime vivo; processos principais iniciaram depois do patch e health checks API/webhook estão OK.

Fase 7 — cobertura de rotas especialistas na matriz:

- Ampliação em `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/hermes_task_router.py` para cobrir rotas documentadas que antes caíam em genérico ou no dono errado.
- Novas rotas ativas: `lk-growth-analytics-readonly`, `lk-ops-commerce-sensitive` e `tech-infra-mission-control`.
- Regressões em `/opt/hermes/tests/agent/test_lucas_task_router_preflight.py` garantem executor/profile/approval boundary para analytics LK, operações LK sensíveis e tech/infra produção.
- Status: código-fonte e Brain router implementados/testados com `11 passed`; ativação plena no gateway vivo requer restart controlado porque `/opt/hermes/agent/lucas_task_router.py` mudou.
- Relatório: `reports/governance/task-router-specialist-routing-fase7-2026-05-24.md`.

Fase 7B — handoff packets limpos e anti-bypass:

- Módulo runtime: `/opt/hermes/agent/lucas_task_router.py` agora expõe `build_specialist_handoff_packet()` para gerar packet Lucas-facing sem `decision_json`, `route_id`, metadata preflight, `job_id` ou boilerplate técnico.
- O preflight injeta contrato interno de packet quando há `handoff_required`, executor especialista ou approval action, orientando o modelo a responder com `Destino`, `Pedido limpo`, `Evidências`, `Preview`, `Risco`, `Bloqueios`, `Rollback` e uma próxima decisão.
- O dispatcher continua bloqueando `delegate_task` em modo approval/handoff; o resultado sintético agora inclui um `handoff_packet` limpo para guiar a resposta, em vez de permitir delegação como bypass de aprovação.
- Verificação: `pytest tests/agent/test_lucas_task_router_preflight.py ...` + regressões do dispatcher = `13 passed`; `py_compile` OK; API/webhook health OK.
- Relatório: `reports/governance/task-router-specialist-handoff-fase7b-2026-05-24.md`.
- Ativação runtime: processos Main e perfis especialistas reiniciaram após o patch (`Main` iniciou `2026-05-24T23:23:02Z`, patch mtime `2026-05-24 22:02:38 +0000`), health checks API/webhook OK e logs pós-restart sem erros. Relatório: `reports/governance/task-router-fase7b-runtime-activation-2026-05-24.md`.

Próximo degrau: monitorar as próximas decisões/rotas reais no Telegram e corrigir falsos positivos/negativos da matriz se aparecerem.

## Casos especiais

### LK conteúdo/blog/source page

Sempre:

- classificar como `lk-growth-content`;
- delegar para LK Growth;
- output em `areas/lk/sub-areas/growth/`;
- proibir publicação/Shopify/theme sem aprovação;
- devolver arquivo/preview para Lucas.

### Zipper sem profile dedicado

Enquanto não houver runtime dedicado:

- Hermes Geral pode fazer read-only/documentação;
- não deve fingir que existe bot/profile operacional;
- contato externo/proposta/preço exige aprovação;
- outputs relevantes devem ir para `areas/zipper/`.

### SPITI

- silêncio > dado errado;
- lance/lote só com fonte verificável;
- Hub/Financial/code via profile/repo correto;
- writes/deploys com PR/approval/rollback.

### Mordomo

- follow-up simples conhecido/verificado pode ser automático conforme guardrails existentes;
- bloquear preço, disponibilidade, reserva, negociação, reclamação, fornecedor, bulk/campanha;
- registrar aprendizados de tom/cliente quando duráveis.

## Resposta curta padrão

### Ao rotear

```text
Contexto: [empresa/área]
Executor: [profile/bot]
Ação: [read-only/draft/packet]
Risco: [baixo/médio/alto]
Produção/externo: não executado
```

### Ao concluir

```text
Feito por [executor].
Arquivo/receipt: [path/link]
Status: [draft/local/read-only/etc]
Próxima decisão: [aprovar preview/revisar/bloquear]
```

## Verificação de qualidade

- O executor escolhido bate com a matriz?
- O output foi salvo no path correto?
- Há link/arquivo/receipt real?
- Havia aprovação explícita se houve A3/A4?
- Especialista gerou handoff?
- O Brain foi atualizado quando a decisão é durável?
