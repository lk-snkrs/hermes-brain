# PRD / Implementation Plan — Elle Brain v2

> **Para Hermes:** este plano deve ser executado com `superpowers` + `writing-plans` + `test-driven-development` + `verification-before-completion`. Não executar produção sem aprovação escopada de Lucas.

**Data:** 2026-06-26  
**Owner:** LK Ops / Atendimento  
**Sistema:** Elle / Chatwoot / WhatsApp LK  
**Status:** PRD/plan proposto — aguardando aprovação para implementação  
**Escopo deste documento:** especificação e plano; sem write em produção  
**Fonte base:** audit `elle-full-architecture-guardrails-audit-20260626.md` + hotfix `elle-hotfix-product-postsale-context-validjson-20260626.md`  
**values_printed:** false

---

## 1. Resumo executivo

Lucas identificou corretamente o problema central da Elle:

> Se a Elle só responde intents pré-definidas, ela fica “burra”. Ela precisa usar a inteligência do Hermes/LLM para entender perguntas novas, e os guardrails devem proteger — não substituir — o raciocínio.

A Elle atual **já consulta OpenRouter/LLM**, mas a arquitetura ainda é monolítica: a função `classify()` mistura contexto, regras, LLM, guardrails, renderização e decisão final. Isso faz com que respostas seguras às vezes sejam tratadas como handoff/regras, e respostas incertas às vezes caiam em templates fracos.

**Elle Brain v2** propõe separar a decisão em camadas:

```text
Intake → Context Builder → LLM Candidate → Policy Engine → Action Router → Evaluator → Supervised Learning
```

A meta é manter segurança operacional, mas permitir que a LLM/Hermes seja o cérebro em casos seguros.

---

## 2. Problema

### 2.1 Sintomas observados

1. Mensagens de navegação em produto/home podiam virar pós-venda/handoff por contexto antigo.
2. Produto incerto podia retornar sugestão aleatória de catálogo.
3. Perguntas abertas seguras podiam cair em regra/template em vez de resposta inteligente.
4. `rule_guardrail_after_llm` domina a maior parte dos processed logs.
5. `valid_json=false` era ambíguo antes do hotfix; agora há `parse_status`, mas falta candidate/policy observability.
6. Autoaprendizado registra lessons, mas não vira regressão/hotfix automaticamente.
7. `classify()` está grande demais e difícil de auditar.

### 2.2 Causa raiz

Não é ausência de LLM. A causa é **acoplamento de responsabilidades**:

- regras pré-LLM;
- prompt longo com regras e exceções;
- LLM candidate;
- guardrails pós-LLM;
- renderização da resposta;
- action routing;
- logging;
- supervised learning.

Tudo isso está concentrado no mesmo fluxo, especialmente `classify()`.

---

## 3. Objetivos

### 3.1 Objetivos de produto

1. Fazer a Elle **pensar** em perguntas novas usando LLM/Hermes.
2. Manter atendimento natural, curto e humano, no estilo LK/Larissa.
3. Reduzir respostas erradas causadas por match de palavra-chave isolada.
4. Aumentar `llm_final` em casos seguros.
5. Manter `stock_handoff`/`human_handoff` corretos em casos de risco.
6. Tornar cada decisão auditável: por que a LLM venceu, foi reescrita ou bloqueada.
7. Fazer aprendizado supervisionado virar regression candidate claro.

### 3.2 Objetivos técnicos

1. Separar `classify()` em camadas testáveis.
2. Criar contratos de dados para contexto, candidate, policy decision e final result.
3. Criar policy table determinística com IDs e testes.
4. Criar regression suite com casos reais/sintéticos.
5. Implementar rollout seguro em dry-run/shadow antes de produção.
6. Preservar rollback fácil para arquitetura atual.

---

## 4. Não objetivos

Este projeto **não** deve:

- consultar ou prometer estoque fora do `lk-stock`/Larissa;
- alterar Shopify/Tiny/Klaviyo/Meta/WhatsApp sem aprovação separada;
- criar respostas automáticas para reclamações sensíveis como decisão final;
- autoeditar produção a partir de aprendizado;
- remover handoff humano;
- transformar Elle em agente que faz ações externas por conta própria;
- publicar mudanças em produção sem backup, dry-run, verificação e aprovação de Lucas.

---

## 5. Princípios de design

### 5.1 LLM-first em casos seguros

Se o caso é seguro, a LLM deve poder responder.

Exemplos:

- saudação;
- home/produto/coleção browsing;
- dúvida comercial sem disponibilidade;
- fit/guia de tamanho com regra aprovada;
- carrinho/checkout simples;
- cupom/pagamento dentro do copy aprovado;
- produto incerto pedindo esclarecimento.

### 5.2 Guardrails como policy layer

Guardrail não deve ser “menu de respostas”. Deve ser uma camada pós-candidate:

| Ação | Significado |
|---|---|
| `allow` | usar resposta da LLM |
| `rewrite` | substituir por template seguro |
| `clarify` | pedir dado mínimo |
| `handoff` | transferir para Larissa/lk-stock |
| `block` | não responder publicamente |

### 5.3 Fonte viva para dado material

Se a resposta depende de estoque, disponibilidade, prazo, pedido, status, reserva, troca, reembolso ou financeiro, a Elle não deve inventar. Deve usar fonte viva oficial ou handoff.

### 5.4 Observabilidade antes de autonomia

Toda decisão deve registrar:

- candidate;
- policy;
- final;
- motivo;
- owner;
- se houve LLM;
- se houve tool/fonte;
- se houve write externo.

### 5.5 Aprendizado supervisionado

Autoaprendizado pode criar lessons e regression candidates. Não pode editar código/produção sozinho.

---

## 6. Arquitetura proposta

```text
1. Intake
   Chatwoot webhook, HMAC, duplicate filter, debounce, human takeover event.

2. Context Builder
   Monta um objeto Context com mensagem atual, burst, histórico, site_result, human_lock, lessons e flags.

3. LLM Candidate
   OpenRouter/Hermes interpreta a intenção e retorna JSON estruturado.

4. Policy Engine
   Aplica guardrails determinísticos e decide allow/rewrite/clarify/handoff/block.

5. Renderer
   Produz a resposta final, nota privada e labels com base na policy decision.

6. Action Router
   Envia public reply, private note, assignment e labels, respeitando dry-run/kill switch/write_enabled.

7. Evaluator
   Audita a resposta enviada/decidida.

8. Supervised Learning
   Cria lessons/regression candidates. Não edita produção sozinho.
```

---

## 7. Contratos de dados

### 7.1 `ElleContext`

```json
{
  "conversation_id": "string",
  "message_id": "string",
  "sender_name": "string",
  "current_message": "string_sanitized",
  "customer_burst": "string_sanitized",
  "recent_messages": [],
  "site_result": null,
  "human_lock": null,
  "assignee_present": false,
  "supervised_lessons": [],
  "flags": {
    "current_safe_product_browse": false,
    "current_post_sale": false,
    "stock_signal": false,
    "availability_signal": false,
    "delivery_deadline_signal": false,
    "photo_uncertain": false,
    "business_contact": false,
    "explicit_human_request": false
  }
}
```

### 7.2 `LLMCandidate`

```json
{
  "intent": "product_browse | stock_availability | post_sale | greeting | checkout | coupon | fit | unknown",
  "category": "greeting | institutional | coupon | competitor_safe | product_clear | stock_handoff | human_handoff",
  "reply_candidate": "string",
  "handoff": false,
  "handoff_target": "none | larissa | lk-stock",
  "risk_flags": [],
  "needs_tool": "none | catalog | order_status | stock | human",
  "missing_info": [],
  "reasoning_short": "string"
}
```

### 7.3 `PolicyDecision`

```json
{
  "policy_action": "allow | rewrite | clarify | handoff | block",
  "policy_ids_applied": [],
  "final_category": "string",
  "handoff": false,
  "handoff_target": "none | larissa | lk-stock",
  "safe_template_id": null,
  "forbidden_terms_removed": [],
  "reason": "string"
}
```

### 7.4 `ElleResult`

```json
{
  "category": "string",
  "handoff": false,
  "reply": "string",
  "private_note": "string",
  "labels": [],
  "blocked_reasons": [],
  "ai": {
    "consulted": true,
    "provider": "openrouter",
    "model": "deepseek/deepseek-v4-pro",
    "valid_json": true,
    "parse_status": "valid_json",
    "candidate_category": "string",
    "policy_action": "allow",
    "policy_ids_applied": [],
    "decision_source": "llm_final | policy_rewrite_after_llm | policy_handoff_after_llm | rule_guardrail_no_llm"
  }
}
```

---

## 8. Policy table inicial

| ID | Trigger | Ação | Owner | Observação |
|---|---|---|---|---|
| `P-STOCK-001` | estoque, disponibilidade, tamanho disponível, pronta entrega, retirada, reserva | `handoff` | lk-stock/Larissa | Nunca prometer disponibilidade |
| `P-DELIVERY-001` | prazo/CEP/frete com data específica ou dependente de pronta entrega | `handoff` | Larissa | Não prometer prazo |
| `P-POSTSALE-001` | pedido, rastreio, atraso, não recebi, troca, devolução, reembolso, cancelamento | `handoff` | Larissa | Não misturar catálogo |
| `P-PHOTO-001` | foto/print sem produto claro | `clarify` ou `handoff` | Larissa | Nunca adivinhar modelo |
| `P-UNKNOWN-PRODUCT-001` | produto não encontrado ou baixa confiança | `clarify` | Elle | Pedir link/foto/modelo, não sugerir aleatório |
| `P-AUTH-001` | pergunta explícita de originalidade | `rewrite` | Elle | “Sim, trabalhamos apenas com produtos originais.” |
| `P-COUPON-001` | desconto/Pix/cupom | `rewrite` | Elle | Copy aprovado: ELLE5 5% |
| `P-FIT-001` | calce/tamanho/guia seguro | `allow` ou `rewrite` | Elle | Mind/Yeezy +1; 204L/Onitsuka normal |
| `P-COMPARE-001` | comparação/curadoria entre modelos | `handoff` | Larissa | Não inventar comparação |
| `P-BROWSE-001` | browsing produto/home sem risco atual | `allow` | Elle | LLM-first |
| `P-CHECKOUT-001` | carrinho/checkout/pagamento simples | `allow` | Elle | Sem handoff silencioso |
| `P-HUMAN-001` | cliente pede Larissa/humano | `handoff` | Larissa | Ack curto |
| `P-FORBIDDEN-001` | resposta promete estoque/prazo/reserva/reembolso/desconto indevido | `block`/`rewrite` | Policy | Última barreira |

---

## 9. Regression suite — casos mínimos

### 9.1 Casos safe LLM-first

| Caso | Entrada | Esperado |
|---|---|---|
| `safe_greeting` | “Olá” | `greeting`, `handoff=false`, LLM allowed |
| `safe_home_browse` | “Estava navegando em LK Sneakers Jardins...” | `product_clear`, `handoff=false`, `policy_action=allow` |
| `safe_product_browse` | “Estava navegando em New Balance 9060...” | `product_clear`, `handoff=false` |
| `safe_collection_browse` | “Estava navegando em coleção Adidas” | `product_clear`, `handoff=false` |
| `safe_fit_204l` | “204L calça normal?” | `product_clear`, sem estoque |
| `safe_mind_size` | “Mind 001 precisa pegar maior?” | `product_clear`, regra +1 |
| `safe_coupon` | “tem desconto no pix?” | `coupon`, copy aprovado |
| `safe_checkout` | “como finalizo no cartão?” | `product_clear`/`institutional`, sem handoff |
| `unknown_product` | “Tem New Balance Miu Miu?” | não sugerir aleatório; pedir link/foto/modelo/verificação |

### 9.2 Casos hard guardrail

| Caso | Entrada | Esperado |
|---|---|---|
| `stock_size_available` | “tem tamanho 36?” | `stock_handoff`, lk-stock/Larissa |
| `store_pickup` | “tem na loja física?” | `stock_handoff` |
| `ready_delivery` | “pronta entrega?” | `stock_handoff` |
| `reserve` | “reserva pra mim?” | `stock_handoff`/humano, sem prometer reserva |
| `delivery_cep` | “chega até sexta?” | `human_handoff` |
| `post_sale_late` | “comprei em maio e não recebi” | `human_handoff` |
| `refund` | “quero reembolso” | `human_handoff` |
| `exchange` | “quero trocar/devolver” | `human_handoff`, pedir pedido/motivo |
| `address_change` | “preciso alterar endereço” | `human_handoff`, pedir pedido, sem prometer alteração |
| `photo_unknown` | imagem/print sem texto | pedir link/nome ou humano, não chutar |
| `comparison` | “qual a diferença entre X e Y?” | `human_handoff` |
| `human_request` | “quero falar com Larissa” | `human_handoff` |

### 9.3 Casos contextuais

| Caso | Contexto | Entrada | Esperado |
|---|---|---|---|
| `browse_after_old_post_sale` | histórico antigo de reembolso | browsing produto atual | `product_clear`, não herdar pós-venda velho |
| `post_sale_current_wins` | histórico de produto | “não recebi meu pedido” | `human_handoff` |
| `bare_size_after_product` | cliente viu produto | “36” | `stock_handoff` se pergunta disponibilidade |
| `color_followup` | produto recente | “tem nessa cor?” | `stock_handoff`/clarify seguro |
| `short_chaser_after_post_sale` | pós-venda ativo | “e aí?” | humano/lock, não catálogo |

### 9.4 Observabilidade

| Caso | Esperado |
|---|---|
| OpenRouter JSON válido | `parse_status=valid_json` |
| OpenRouter inválido | `parse_status=invalid_json_or_empty` |
| provider exception | `parse_status=provider_error` |
| hard rule sem LLM por inelegibilidade | `decision_source=rule_guardrail_no_llm`, motivo claro |
| LLM candidate vetado | `candidate_category`, `policy_action`, `policy_ids_applied` presentes |

---

## 10. Acceptance criteria

### 10.1 Funcional

- [ ] 100% dos casos da regression suite passam em dry-run.
- [ ] Safe cases usam `llm_final` ou `policy_action=allow` quando OpenRouter retorna JSON válido.
- [ ] Hard guardrail cases nunca prometem estoque, prazo, reserva, reembolso, cancelamento, desconto indevido ou disponibilidade.
- [ ] Produto incerto nunca retorna produto aleatório.
- [ ] Navegação atual de produto/home não herda pós-venda antigo.
- [ ] Pós-venda atual sempre vence catálogo/produto.
- [ ] Human lock impede Elle de brigar com humano.

### 10.2 Observabilidade

- [ ] Todo `processed` contém `ai_consulted`, `provider`, `model`, `valid_json`, `parse_status`, `decision_source`.
- [ ] Todo `processed` com LLM contém candidate/policy fields.
- [ ] Todo policy override registra `policy_ids_applied`.
- [ ] Response evaluator roda e registra `quality`/`risk_level`.
- [ ] Lessons/candidates são sanitizados e não contêm secrets.

### 10.3 Operacional

- [ ] Rollout começa em dry-run/shadow.
- [ ] Nenhum envio real ao cliente durante testes.
- [ ] Produção só com aprovação explícita de Lucas.
- [ ] Backup e rollback testados antes do cutover.
- [ ] Receipt Brain criado com evidência.

---

## 11. Rollout seguro

### Fase A — PRD aprovado

- Lucas aprova este PRD/plan.
- Nenhum código produtivo alterado ainda.

### Fase B — branch/snapshot + testes

- Criar backup de `/opt/elle-chatwoot/app.py` e container `/app/app.py`.
- Criar `tests/elle_brain_v2_regression.py`.
- Rodar RED contra arquitetura atual.

### Fase C — refatoração local/dry-run

- Implementar camadas em arquivo novo ou módulo local:
  - `context_builder`
  - `llm_candidate`
  - `policy_engine`
  - `renderer`
  - `action_router`
- Manter compatibilidade com `process_incoming_flat`.
- `WRITE_ENABLED=false`, `KILL_SWITCH=true` nos smokes.

### Fase D — shadow mode

- Processar eventos recentes em paralelo sem responder clientes.
- Comparar v1 vs v2:
  - categoria;
  - handoff;
  - candidate;
  - policy;
  - resposta final;
  - evaluator.

### Fase E — canary controlado

- Ativar v2 só em um subconjunto seguro ou por feature flag.
- Monitorar `bad`, `risk_level`, `policy_action`, `handoff`.

### Fase F — produção

- Só após aprovação de Lucas.
- Backup + deploy/restart controlado.
- Readback `/health`.
- Smoke classify-only.
- Monitor 1h/24h.

---

## 12. Rollback

Rollback obrigatório:

1. Restaurar backup de `/opt/elle-chatwoot/app.py`.
2. Copiar para container `/app/app.py`.
3. `python3 -m py_compile /app/app.py`.
4. `docker restart elle-chatwoot`.
5. Verificar `/health`.
6. Confirmar logs sem `processed` com erro.
7. Registrar receipt.

---

## 13. Implementation plan detalhado

### Task 1 — Criar regression suite base

**Objetivo:** transformar os casos acima em teste executável antes de refatorar.

**Arquivos:**
- Criar: `/opt/elle-chatwoot/tests/elle_brain_v2_regression.py`

**Passos:**
1. Criar fixtures de `flat(content, history=[], site_result=None)`.
2. Monkeypatch `fetch_conversation_messages`.
3. Monkeypatch `call_ai_json` para respostas válidas/inválidas.
4. Adicionar casos safe/hard/context/observability.
5. Rodar:

```bash
PYTHONPATH=/app python3 /opt/elle-chatwoot/tests/elle_brain_v2_regression.py
```

**Esperado em RED:** falhas nos campos novos de candidate/policy e possivelmente algumas decisões.

---

### Task 2 — Introduzir contratos sem trocar comportamento

**Objetivo:** criar estruturas auxiliares sem mudar resultado final.

**Arquivos:**
- Modificar: `/opt/elle-chatwoot/app.py`

**Passos:**
1. Adicionar builders simples:
   - `build_elle_context(flat) -> dict`
   - `build_candidate_from_legacy_ai(ai) -> dict`
   - `build_policy_decision_legacy(final, ai) -> dict`
2. Anexar metadata nova sem alterar `reply/category`.
3. Rodar regressão.

**Critério:** comportamento final igual; logs mais ricos.

---

### Task 3 — Extrair Context Builder

**Objetivo:** mover coleta de histórico, burst, site_result, locks e flags para função própria.

**Arquivos:**
- Modificar: `/opt/elle-chatwoot/app.py`

**Passos:**
1. Criar `build_context(flat)`.
2. Substituir trechos duplicados de `classify()` por `ctx`.
3. Garantir que `base_rule_classify` use somente sinais necessários.
4. Rodar regressões.

---

### Task 4 — Extrair LLM Candidate

**Objetivo:** fazer a chamada LLM retornar candidate estruturado.

**Passos:**
1. Criar `llm_candidate(ctx, base_hint)`.
2. Atualizar prompt para pedir `intent`, `risk_flags`, `needs_tool`, `missing_info`.
3. Validar JSON mínimo.
4. Se JSON inválido, retornar candidate com `parse_status` e sem resposta final.

---

### Task 5 — Criar Policy Engine

**Objetivo:** centralizar hard guardrails numa tabela.

**Passos:**
1. Criar `POLICIES = [...]` com IDs da seção 8.
2. Criar `policy_evaluate(ctx, candidate) -> PolicyDecision`.
3. Garantir precedência:
   - hard risk > candidate;
   - forbidden terms > allow;
   - low-confidence product > clarify;
   - safe browse > allow.
4. Testar cada policy ID.

---

### Task 6 — Criar Renderer

**Objetivo:** transformar candidate/policy em resposta final segura.

**Passos:**
1. Criar `render_result(ctx, candidate, policy)`.
2. Templates seguros por policy.
3. Sem emoji.
4. Sem “atendente virtual”; se necessário, “IA de atendimento em treinamento”.
5. Larissa nos handoffs públicos.

---

### Task 7 — Action Router compatível

**Objetivo:** manter `apply_actions` seguro e compatível.

**Passos:**
1. Não alterar writes reais ainda.
2. Garantir que `dry_run`, `kill_switch`, `write_enabled` continuam mandando.
3. Garantir duplicate public reply guard.
4. Garantir private note antes de assignment em handoff.

---

### Task 8 — Observability v2

**Objetivo:** enriquecer logs sem PII.

Adicionar a `processed`:

- `candidate_intent`
- `candidate_category`
- `candidate_reply_preview` sanitizado
- `policy_action`
- `policy_ids_applied`
- `final_category`
- `tool_needed`
- `tool_used`

---

### Task 9 — Shadow runner

**Objetivo:** comparar v1 vs v2 sem enviar cliente.

**Arquivos:**
- Criar: `/opt/elle-chatwoot/scripts/elle_brain_v2_shadow_runner.py`

**Passos:**
1. Ler eventos recentes sanitizados.
2. Rodar v1 e v2 em dry-run.
3. Gerar JSON/MD com diferenças.
4. Não chamar Chatwoot writes.

---

### Task 10 — Canary flag

**Objetivo:** permitir rollout controlado.

Adicionar env/flag:

- `ELLE_BRAIN_V2_ENABLED=false`
- `ELLE_BRAIN_V2_SHADOW=true`
- `ELLE_BRAIN_V2_CANARY_CONVERSATIONS=` opcional

---

### Task 11 — Deploy controlado

**Pré-condição:** aprovação explícita de Lucas.

1. Backup.
2. `py_compile`.
3. regressões.
4. shadow report.
5. aplicar runtime.
6. restart controlado.
7. health/readback.
8. monitor 1h.
9. receipt.

---

## 14. Métricas de sucesso

| Métrica | Meta inicial |
|---|---:|
| regressões passando | 100% |
| safe cases com `llm_final`/allow | >80% quando JSON válido |
| hard guardrails corretos | 100% |
| bad response_evaluated | tendência ↓ |
| produto incerto sugerindo aleatório | 0 |
| estoque prometido pela Elle | 0 |
| pós-venda misturado com catálogo | 0 |
| processed sem `decision_source` | 0 |
| processed sem `parse_status` | 0 |

---

## 15. Riscos

| Risco | Mitigação |
|---|---|
| LLM responde demais | hard policies + forbidden terms |
| guardrail continua dominando | medir `policy_action` e `llm_final` safe cases |
| JSON inválido | fallback observável + prompt menor |
| regressão em pós-venda | regression suite + Larissa handoff tests |
| estoque prometido | policy hard + forbidden terms |
| produção instável | shadow + canary + rollback |
| logs com PII | redaction e previews truncados |

---

## 16. Decisão necessária

Para implementar, Lucas precisa aprovar uma das opções:

1. **Aprovar só Fase B/C local + shadow**  
   Sem envio real; cria teste/refatoração e roda em paralelo.

2. **Aprovar implementação completa até canary**  
   Inclui feature flag e canary, mas produção final ainda requer aprovação antes de ligar geral.

3. **Segurar implementação e só revisar PRD**  
   Ajustamos o documento antes de qualquer código.

Minha recomendação: **opção 1** primeiro.

---

## 17. Definition of Done para a primeira entrega

A primeira entrega de Elle Brain v2 estará pronta quando:

- regression suite existir;
- context/candidate/policy/result estiverem separados ou compatibilizados;
- shadow runner comparar v1 vs v2;
- nenhum write real for feito durante teste;
- relatório de shadow mostrar onde v2 melhora/piora;
- Lucas receber approval packet para canary.

---

## 18. Evidência e auditoria

- Audit base: `areas/lk/sub-areas/atendimento/reports/elle-full-architecture-guardrails-audit-20260626.md`
- Hotfix prévio: `areas/lk/sub-areas/atendimento/receipts/elle-hotfix-product-postsale-context-validjson-20260626.md`
- Este PRD/plan: `areas/lk/sub-areas/atendimento/prds/elle-brain-v2-prd-plan-20260626.md`

**Writes externos deste documento:** nenhum.  
**Secrets:** não impressos.  
**values_printed:** false
