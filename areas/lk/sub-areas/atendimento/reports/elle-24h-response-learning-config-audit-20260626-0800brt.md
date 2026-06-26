# Elle / Atendimento LK — audit de respostas, aprendizado e configuração

Data: 2026-06-26 08:00 BRT
Janela: últimas 24h aprox.
Modo: read-only/local; sem Chatwoot/Shopify/Tiny/WhatsApp writes; values_printed=false.

## Fontes verificadas

- Relatório observer live via VPS/container Elle.
- `/var/log/elle/events.jsonl` no container `elle-chatwoot`.
- Chatwoot read-only via runtime Elle para conversas com avaliação ruim.
- Config runtime Elle via import `app` no container, sem imprimir secrets.
- Supervised learning files:
  - `/data/supervised_learning/lessons.jsonl`
  - `/data/supervised_learning/pending_wrong_response_cases.jsonl`
- Cron local `lk-elle-customer-correction-learner`.

## Números principais

- Eventos totais no log: 2738.
- Observed: 404.
- Debounce processed: 200.
- Processed/customer replies: 33.
- Response evaluated: 33.
- Qualidade do evaluator: 18 good, 10 ok, 5 bad.
- Erros únicos avaliados: 4 conversas / 5 avaliações ruins, pois uma mensagem teve duas avaliações ruins.
- Todos os 33 `processed` tinham:
  - `ai_consulted=true`
  - `ai_provider=openrouter`
  - `decision_source` presente
- Decision source em processed:
  - `rule_guardrail_after_llm`: 30
  - `llm_final`: 3
- `valid_json=true`: 18/33.
- `valid_json=false`: 15/33.

## O que a Elle errou

1. Conv 2324 / msg 55598 — pós-venda tratado inicialmente como produto/contexto errado.
   - Cliente: compra de maio / prazo estourado.
   - Avaliações ruins: `post_sale_mishandled` e `context_missed`.
   - Risco: alto/médio.
   - Sinal: deveria ficar no trilho pós-venda humano, sem resposta de produto/catálogo.

2. Conv 2325 / msg 55634 — navegação em produto New Balance 9060 Angora Sea Salt virou handoff de pós-venda.
   - Cliente só estava navegando no produto e pediu saber mais.
   - Categoria final: `human_handoff`.
   - Issue: `misclassification`.
   - Risco: médio.
   - Erro: transbordo sensível desnecessário; a Elle soou como se houvesse problema de pedido/atraso.

3. Conv 2331 / msg 56088 — homepage/olá virou handoff de pós-venda.
   - Cliente navegava na home e disse olá.
   - Categoria final: `human_handoff`.
   - Issue: `inappropriate_handoff`.
   - Risco: baixo.
   - Erro: escalou para Larissa/Giselia sem necessidade.

4. Conv 1440 / msg 56239 — pergunta “Tem o New Balance Miu Miu?” recebeu produto/link irrelevante.
   - Categoria final: `product_clear`.
   - Issue: `irrelevant_product_suggestion`.
   - Risco: baixo, mas comercialmente ruim.
   - Erro: sugeriu Nike Vomero Premium Tangerine Tint em vez de reconhecer incerteza/ausência ou pedir validação.

## Autoaprendizado

Status: funcionando parcialmente.

Evidência positiva:

- Cron `lk-elle-customer-correction-learner` habilitado, agendado `*/15 * * * *`.
- Última execução local lida: 2026-06-26 11:00 UTC, status OK, `lessons_added=0`.
- `lessons.jsonl` existe, 8 linhas.
- `pending_wrong_response_cases.jsonl` existe, 3 linhas.
- O runtime carrega `supervised_customer_correction_lessons` no prompt (`load_recent_supervised_lessons()` em `/app/app.py`).
- Nas últimas 24h houve 5 eventos `guardrail_teaching_lesson_added`.

Limite atual:

- O aprendizado é supervisionado/por prompt, não auto-deploy de código.
- Ele registra lições e candidatos, mas não garante correção imediata de todos os padrões.
- Há exemplos em que a Elle ainda errou mesmo com OpenRouter ativo, especialmente produto/contexto e handoff indevido.

## Configuração runtime

Status: bem configurada para operar, mas não “perfeita”.

Config lida do runtime, sem secrets:

- `AI_ENABLED=true`
- `AI_PROVIDER=openrouter`
- `AI_MODEL=deepseek/deepseek-v4-pro`
- secret OpenRouter presente
- `PUBLIC_REPLY_ENABLED=true`
- `WRITE_ENABLED=true`
- `KILL_SWITCH=false`
- `DRY_RUN=false`
- `POST_RESPONSE_EVALUATOR_ENABLED=true`
- container `elle-chatwoot` up ~46h

Smokes classify-only remotos:

- Product browsing: OpenRouter consultado, JSON válido, `decision_source=llm_final`.
- Availability/stock risk: OpenRouter consultado, JSON válido, guardrail/handoff.
- Human/Larissa request: OpenRouter consultado, JSON válido, guardrail/handoff.

## Diagnóstico

Elle não está “burra” no sentido de estar sem LLM: ela está consultando OpenRouter em todas as respostas processadas da janela.

Mas ainda está com três gaps:

1. Over-guardrail/handoff: 30/33 respostas acabaram em `rule_guardrail_after_llm`; só 3 foram `llm_final`.
2. JSON/observabilidade: 15/33 `processed` registraram `valid_json=false`, mesmo com provider/decision_source presentes.
3. Contexto/produto: ainda erra quando precisa diferenciar navegação genérica, pergunta de produto e pós-venda real.

## Próximos passos recomendados

1. Hotfix de classificação: não tratar homepage/coleção/produto browsing simples como pós-venda sem palavras fortes de pedido, atraso, rastreio, troca, devolução, reembolso ou cancelamento.
2. Produto incerto: quando cliente pergunta por produto não encontrado ou collab ambígua, responder “vou verificar / me manda link/foto/tamanho” em vez de sugerir outro produto não relacionado.
3. Observabilidade: investigar por que 15/33 `processed` estão com `valid_json=false`; objetivo é manter `valid_json=true` quando OpenRouter responde JSON válido e separar fallback real de guardrail intencional.
4. Autoaprendizado: transformar os 5 erros ruins da janela em regressões/smokes, não depender só de prompt lessons.

## Reminder OS

- Reminder OS loop needed: yes.
- Owner: lk-ops + Elle maintainer.
- Next action: preparar hotfix/regression pack para os 4 erros únicos acima.
- Review trigger: próxima auditoria 24h ou novo `response_evaluated quality=bad`.
- Evidence: este relatório + `/opt/data/profiles/lk-ops/cron/output/lk-elle-atendimento/20260626T110231Z-daily.md`.
