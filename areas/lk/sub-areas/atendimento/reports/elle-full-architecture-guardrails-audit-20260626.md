# Elle / Atendimento LK — full architecture + guardrails audit

Data: 2026-06-26
Modo: read-only audit após hotfix; sem Chatwoot/Shopify/Tiny/WhatsApp customer writes; values_printed=false

## Pergunta do Lucas

> Temos que fazer um audit inteiro na Elle: como ela funciona e se guardrails é a maneira correta.

## Veredito

Guardrails são necessários, mas a arquitetura atual ainda tem acoplamento demais entre "entender" e "bloquear".

A direção correta é:

1. **LLM/Hermes como cérebro de interpretação e resposta candidata** para casos elegíveis.
2. **Policy/guardrails como camada pós-LLM**, clara e auditável, que permite, reescreve, bloqueia ou escala.
3. **Ferramentas/fonte viva** para dados materiais.
4. **Evaluator + supervised learner** como melhoria supervisionada, não autoedição de produção.

Hoje a Elle já tenta seguir isso, mas `app.py` ainda mistura muitos papéis em uma função grande (`classify`), com regras antes, durante e depois da LLM.

## Arquitetura atual observada

Runtime: container/VPS `elle-chatwoot`
Fonte runtime: `/app/app.py`
Fonte persistida: `/opt/elle-chatwoot/app.py`
Tamanho: ~2.990 linhas
Log: `/var/log/elle/events.jsonl`
Aprendizado: `/data/supervised_learning/`

### Fluxo de entrada

```text
Chatwoot webhook
  -> Handler.do_POST
  -> verify_hmac / path validation
  -> flatten(payload)
  -> detect_human_takeover
  -> event filters / duplicate seen
  -> enqueue_debounced_incoming
  -> _debounce_fire
  -> build_debounced_flat
  -> process_incoming_flat
```

### Fluxo de decisão

```text
process_incoming_flat
  -> human lock / assignee guard
  -> classify(flat)
      -> early deterministic guards
      -> base_rule_classify(flat)
      -> site/catalog lookup
      -> fetch_conversation_messages
      -> consult_llm_with_history
           -> build_ai_prompt
           -> call_ai_json(OpenRouter)
      -> deterministic hard overrides / finalization
      -> ai metadata: valid_json, parse_status, provider, decision_source
  -> observe_message
  -> apply_actions
  -> evaluate_response_quality
  -> processed log
```

### Fluxo de ação

```text
apply_actions
  -> if handoff: set human lock
  -> if public reply allowed: send official Chatwoot public reply
  -> if handoff: create private note + open/assign handoff
  -> conversation labels
```

### Fluxo de aprendizado

```text
response_evaluated logs
  -> supervised learner cron
  -> lessons.jsonl / candidates / pending wrong cases
  -> load_recent_supervised_lessons()
  -> injected into build_ai_prompt()
```

Também há `record_guardrail_teaching_lesson()` quando a LLM é vetada/corrigida por guardrail.

## Configuração runtime observada

| Item | Status |
|---|---|
| AI_ENABLED | true |
| AI_PROVIDER | openrouter |
| AI_MODEL | deepseek/deepseek-v4-pro |
| OpenRouter secret | presente, valor não impresso |
| PUBLIC_REPLY_ENABLED | true |
| WRITE_ENABLED | true |
| KILL_SWITCH | false |
| DRY_RUN | false |
| DEBOUNCE_ENABLED | true |
| OBSERVER_ENABLED | true |
| OBSERVER_AI_ENABLED | true |
| POST_RESPONSE_EVALUATOR_ENABLED | true |
| SUPERVISED_GUARDRAIL_TEACHING_ENABLED | true |

## Evidência recente de logs

Tail auditado: últimos 2.000 eventos.

| Status | Contagem |
|---|---:|
| ignored | 841 |
| human_lock_set | 376 |
| observed | 278 |
| debounce_queued | 202 |
| debounce_processed | 145 |
| ai_decision | 74 |
| response_evaluated | 35 |
| processed | 35 |
| guardrail_teaching_lesson_added | 8 |
| post_sale_alert_created | 4 |
| catalog_synced | 2 |

Processed breakdown relevante:

| decision_source | categoria | valid_json | provider | qtd |
|---|---|---:|---|---:|
| rule_guardrail_after_llm | human_handoff | true | openrouter | 12 |
| rule_guardrail_after_llm | human_handoff | false | openrouter | 10 |
| llm_final | greeting | true | openrouter | 3 |
| rule_guardrail_after_llm | product_clear | false | openrouter | 3 |
| rule_guardrail_after_llm | stock_handoff | false | openrouter | 2 |
| llm_final | product_clear | true | openrouter | 2 |

## O que está bom

1. **LLM existe e é chamada** para eligible inbound.
2. **Histórico Chatwoot entra no prompt** (`recent_messages`, `customer_burst`, `rule_hint`, `site_result`, `supervised lessons`).
3. **Debounce existe** para agrupar bursts e evitar responder linha isolada.
4. **Human lock existe** para não brigar com Larissa/Giselia.
5. **Pós-resposta é avaliada** (`response_evaluated`).
6. **Autoaprendizado supervisionado existe**, mas não edita produção sozinho.
7. **Observabilidade melhorou** com `parse_status` após hotfix.

## O problema estrutural

A função `classify()` faz coisas demais:

- filtro de risco;
- classificação determinística;
- lookup de catálogo;
- busca de histórico;
- chamada LLM;
- decisão final;
- override por guardrail;
- registro de lesson;
- montagem de metadata.

Isso cria o comportamento que Lucas chamou de “burro”: não porque não existe LLM, mas porque o raciocínio da LLM às vezes é atravessado por regra/template antes de virar resposta.

## Guardrails: são a maneira correta?

**Sim, mas não do jeito monolítico atual.**

Guardrails devem existir como uma **policy layer auditável**, não como um monte de branches que competem com a LLM.

### O que deve continuar como hard guardrail

- estoque/disponibilidade/pronta entrega/loja física/reserva → `stock_handoff` / lk-stock/Larissa;
- prazo/CEP/frete dependente de pronta entrega/encomenda → humano;
- pós-venda real: pedido, entrega, rastreio, atraso, troca, devolução, reembolso, cancelamento → humano;
- comparação/curadoria sensível → humano;
- produto por foto/print incerto → pedir link/nome legível ou humano;
- pagamento/desconto/preço negociado → resposta aprovada ou humano;
- reclamação sensível → humano.

### O que não deve ser hard guardrail

- saudação;
- browsing de produto/home;
- dúvida comercial aberta;
- fit/guia de tamanho seguro;
- carrinho/checkout simples;
- pergunta sobre marca/produto sem disponibilidade.

Esses casos devem ser `llm_final` quando o JSON é válido e a resposta passa no policy check.

## Arquitetura recomendada

```text
1. Intake
   - webhook, HMAC, flatten, debounce, duplicate guard

2. Context Builder
   - current message
   - burst
   - recent history
   - product/site context
   - human lock/assignee
   - supervised lessons

3. Intent/Response Candidate — LLM-first
   - LLM retorna JSON estruturado:
     category, intent, risk_flags, needs_tool, reply_candidate, handoff_target, reasoning_short

4. Policy Engine — deterministic guardrails
   - ALLOW: manda reply_candidate
   - REWRITE: troca por template seguro
   - BLOCK/HANDOFF: Larissa/lk-stock
   - ASK_CLARIFY: pede dado mínimo

5. Action Router
   - public reply
   - private note
   - assignment/labels
   - no customer write in dry-run/test

6. Evaluator
   - classifica qualidade/risco depois da decisão
   - gera regression candidate

7. Supervised Learning
   - lessons entram no prompt
   - mudanças de código só com teste + aprovação/receipt
```

## Gaps atuais

1. **Monólito em `classify()`**: difícil prever quando LLM vence ou perde.
2. **Prompt longo demais**: mistura playbook, hard rules, exceções, lessons e dados. Isso aumenta risco de JSON inválido e inconsistência.
3. **Regras duplicadas**: algumas decisões aparecem em `base_rule_classify`, depois em `classify` antes da LLM, depois em overrides pós-LLM.
4. **`rule_guardrail_after_llm` alto**: bom para segurança, mas indica que a policy layer está dominando a resposta final.
5. **Autoaprendizado ainda é passivo**: registra lessons, mas não transforma automaticamente em regressões/hotfix com dono.
6. **Sem tool router formal**: para perguntas novas, a LLM não tem uma interface clara de ferramentas; ela responde dentro do prompt + guardrail.

## Recomendação prática

### Fase 1 — sem mudar produção agora

Criar uma especificação + regression suite “Elle Brain v2”:

- 30 casos representativos reais/sintéticos:
  - saudação;
  - browsing home/produto;
  - produto incerto;
  - disponibilidade;
  - loja física/pronta entrega;
  - prazo/CEP;
  - pós-venda;
  - troca/devolução;
  - reclamação;
  - cupom/pagamento;
  - fit/tamanho;
  - foto/print;
  - comparação;
  - cliente oferecendo produto;
  - humano/Larissa.
- cada caso com expected: `category`, `handoff`, `decision_source`, `policy_action`, resposta proibida/permitida.

### Fase 2 — separar camadas no código

Extrair de `classify()`:

- `build_context(flat) -> Context`
- `llm_candidate(context) -> Candidate`
- `policy_evaluate(context, candidate) -> PolicyDecision`
- `render_response(context, decision) -> Result`
- `action_router(result)`

### Fase 3 — transformar guardrails em policy table

Cada guardrail deve ter:

- id;
- trigger;
- severity;
- action: allow/rewrite/block/handoff/clarify;
- owner: Elle/Larissa/lk-stock;
- template seguro;
- teste.

### Fase 4 — melhorar observabilidade

Logar por processed:

- `candidate_category`;
- `candidate_reply_preview` sanitizado;
- `policy_action`;
- `policy_ids_applied`;
- `final_category`;
- `decision_source`;
- `parse_status`;
- `tool_needed/tool_used`.

## Próximo passo recomendado

Não recomendo fazer mais hotfix solto agora. Recomendo criar um **PRD/plan de refatoração Elle Brain v2** com:

- contrato de arquitetura;
- casos de regressão;
- plano de rollout em dry-run/shadow;
- rollback;
- critérios de aceite.

Esse plano deve ser aprovado antes de mexer de novo em produção, porque agora é mudança estrutural, não só bugfix.

## Status

- Audit inicial completo: sim.
- Writes externos: nenhum neste audit.
- Secrets: não impressos.
- values_printed=false.
