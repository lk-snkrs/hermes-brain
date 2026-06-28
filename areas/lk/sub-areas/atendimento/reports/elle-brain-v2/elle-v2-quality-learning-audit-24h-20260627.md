# Elle v2 — auditoria qualitativa 24h pós-implementação

Data: 2026-06-27
Janela: últimas 24h a partir dos logs/runtime atuais
Escopo: Chatwoot LK WhatsApp + logs Elle + learner/autonomy gate
Modo: read-only para sistemas externos; análise local sanitizada
values_printed=false

## Resumo executivo

A Elle v2 está ativa e atendendo casos elegíveis, mas a qualidade ainda não permite autonomia ampla.

- Eventos Elle 24h: 3011
- Debounces processados: 200
- Decisões IA: 100
- Casos processados/respostas avaliadas: 46
- Conversas elegíveis nos logs: 34
- Conversas com readback real no Chatwoot: 28
- Conversas/eventos sintéticos, probe ou sem readback real: 6
- v2 canary usado: 10
- v2 canary skipped: 13
- v2 errors: 0
- Provider errors: 0
- Handoff violations: 0
- Autonomy gate: HOLD

## Distribuição por decision_source

| Origem | Eventos |
|---|---:|
| rule_guardrail_after_llm | 110 |
| llm_final | 26 |
| elle_brain_v2_canary | 10 |

Interpretação: a LLM está sendo consultada, mas o guardrail/policy ainda domina a decisão final. Isso está correto para risco, mas indica que a autonomia ampla ainda não deve subir.

## Distribuição por categoria

| Categoria | Eventos |
|---|---:|
| product_clear | 63 |
| human_handoff | 51 |
| stock_handoff | 24 |
| greeting | 10 |
| coupon | 4 |
| institutional | 4 |

## Veredito individual sanitizado

IDs abaixo são IDs técnicos internos; relatório não contém telefone/e-mail/secret. Conteúdo está resumido/parafraseado.

| Caso | Tema | Elle/fluxo | Veredito | Observação |
|---|---|---|---|---|
| conv 2353 | Produto/preço NB | respondeu produto incorreto | ERRO | Cliente perguntou preço de New Balance; resposta citou produto Lululemon não relacionado. Avaliador marcou bad/high. |
| conv 2362 | Navegação produto / Onitsuka | fez handoff como pós-venda antes da dúvida real | ERRO | Mensagem inicial era navegação site; Elle respondeu como se fosse pós-venda/problema. Depois humano assumiu. |
| conv 2389 | Espanhol/localização/foto | v2/guardrail + humano | MELHORAR | Cliente em espanhol perguntou localização/visita e depois mandou foto; fluxo terminou em handoff, mas a primeira resposta não respondeu bem localização/idioma. |
| conv 2381 | Objeção de preço/originalidade | v2/guardrail + humano | MELHORAR | Cliente questionou preço vs outros sites/oficial. Resposta inicial foi genérica; melhor seria playbook de objeção de preço + originalidade + curadoria/handoff. |
| conv 2369 | Disponibilidade + foto + tamanho | handoff estoque/humano | OK | Pergunta de disponibilidade/tamanho; Elle não prometeu estoque e transferiu. |
| conv 2360 | Foto/tamanho/disponibilidade | handoff/humano | OK | Tema de disponibilidade; humano respondeu. Não vi promessa indevida da Elle. |
| 21 outros casos reais | saudação/produto/cupom/estoque/pós-venda | tratado ou transbordado | OK | Sem violação de estoque/prazo/reserva; casos seguros tiveram IA/LLM ou humano conforme lock. |
| 6 eventos sem readback Chatwoot | probes/sintéticos/shadow | logs Elle apenas | EXCLUÍDO da qualidade cliente | IDs técnicos 9001/904xxx/990001 não apareceram como conversas reais no readback; não usar como prova de atendimento ao cliente. |

## Qualidade final

Entre as 28 conversas reais com readback:

| Status | Quantidade | Leitura |
|---|---:|---|
| OK | 24 | comportamento seguro ou humano assumiu corretamente |
| Melhorar | 2 | resposta funcional, mas abaixo do padrão LK |
| Erro | 2 | resposta/contexto incorreto |

Taxa qualitativa operacional aproximada: 24/28 OK = 85,7%.

Atenção: esse número é qualitativo, não métrica estatística perfeita. O ponto importante é que ainda existem erros concretos de contexto/produto.

## Erros principais encontrados

### 1. Produto incorreto em pergunta de preço

Padrão: cliente pergunta sobre produto A e a Elle retorna link/produto B não relacionado.

Risco:
- perde confiança;
- parece resposta inventada;
- pode causar reclamação.

Correção recomendada:
- regression test: pergunta de preço sobre produto em contexto deve manter o mesmo produto;
- se confiança de lookup for baixa, responder sem sugerir produto não relacionado;
- para objeção de preço, usar resposta segura: originalidade, curadoria, importação/encomenda/pronta-entrega sem promessa, e chamar humano se necessário.

### 2. Navegação de produto classificada como pós-venda

Padrão: mensagem automática “estava navegando...” herdou/ativou fluxo de pós-venda/handoff indevido.

Risco:
- cliente recebe “sinto muito”/transferência sem ter reclamado;
- over-handoff;
- baixa conversão.

Correção recomendada:
- regra: mensagem atual de navegação/produto não deve herdar contexto antigo de pedido/reembolso/rastreio salvo se a mensagem atual contiver termos de pós-venda;
- regression test para landing/home/product browsing.

### 3. Espanhol/localização e foto

Padrão: cliente em espanhol pergunta localização/visita e depois manda foto. Fluxo transbordou, mas não respondeu com boa orientação inicial.

Correção recomendada:
- se idioma espanhol detectado, responder em espanhol simples ou português claro;
- localização/visita pode usar endereço aprovado, sem prometer disponibilidade;
- foto + “tem?” deve transbordar para Larissa/lk-stock, como já ocorreu.

### 4. Objeção de preço

Padrão: cliente compara preço LK com site oficial/outros sites.

Correção recomendada:
- criar playbook de objeção de preço/originalidade/curadoria;
- não discutir preço como negociação automática;
- se sensível, handoff para humano.

## Guardrails

Pontos bons:

- Não encontrei promessa automática de estoque/pronta entrega/reserva feita pela Elle nos casos auditados.
- Casos de disponibilidade/tamanho/foto foram para humano/stock guardrail.
- Pós-venda/prazo/pagamento sensível foi tratado com handoff/guardrail.
- `handoff_violations=0` no gate.

Pontos de atenção:

- Em alguns casos seguros de produto, o guardrail ainda domina demais e o humano acaba respondendo o que a Elle poderia conduzir melhor.
- Em caso de produto/preço, a Elle pode inventar/selecionar item errado se o lookup de catálogo tiver baixa confiança.

## Autoaprendizado / cérebro

Learner executado após a análise:

```json
{
  "status": "ok",
  "lessons_total": 15,
  "evaluations_total": 11,
  "v2_lessons_loaded": 8,
  "v2_context_probe_ok": true,
  "regression_candidates_total": 16,
  "eval_risk_seen": 4,
  "eval_risk_candidates_total": 4,
  "customer_send_executed": false,
  "writes_external": 0,
  "values_printed": false
}
```

Arquivos supervisionados:

| Arquivo | Count | Status |
|---|---:|---|
| lessons.jsonl | 15 | existe |
| evaluations.jsonl | 11 | existe |
| regression_candidates.jsonl | 16 | existe |
| eval_risk_regression_candidates.jsonl | 4 | existe |

Eval risk candidates recentes:

| Categoria | Decision source | Quality | Risk | Status |
|---|---|---|---|---|
| product_clear | rule_guardrail_after_llm | bad | low | candidate_pending_review |
| product_clear | rule_guardrail_after_llm | bad | high | candidate_pending_review |
| human_handoff | rule_guardrail_after_llm | bad | low | candidate_pending_review |
| greeting | elle_brain_v2_canary | bad | low | candidate_pending_review |

Conclusão: o autoaprendizado está funcionando como aprendizado supervisionado. Ele registra lessons/evaluations/candidates e v2 consome parte das lessons. Ele não se auto-corrige em produção sozinho — correto e seguro. O gargalo agora é revisar/aprovar/aplicar candidates como regressões/policy fixes.

## Autonomy gate

```json
{
  "status": "hold",
  "processed": 46,
  "v2_canary_used": 10,
  "v2_canary_skipped": 13,
  "v2_canary_error": 0,
  "ai_provider_error": 0,
  "eval_bad": 4,
  "eval_medium_high": 1,
  "handoff_violations": 0,
  "recommendation": "do_not_expand_autonomy",
  "writes_external": 0,
  "values_printed": false
}
```

## Conclusão

A Elle v2 está operacional, segura e aprendendo, mas não está com qualidade suficiente para autonomia maior.

Veredito:
- Manter v2 em 100% safe-only.
- Não expandir autonomia.
- Corrigir P0/P1 antes: produto errado, navegação tratada como pós-venda, espanhol/localização, objeção de preço.

## Próximos passos recomendados

P0 — corrigir antes de expandir:
1. Regression test para “produto A não pode responder produto B”.
2. Policy: se catalog match confidence baixo, pedir confirmação/link/foto em vez de sugerir item não relacionado.
3. Regression test para “estava navegando em produto/coleção/home” não virar pós-venda sem termo atual de pedido/rastreio/reembolso.

P1:
1. Playbook de objeção de preço/originalidade/curadoria.
2. Idioma espanhol/localização básica com endereço aprovado, sem promessa de disponibilidade.
3. Converter os 4 eval_risk_candidates em testes revisáveis.

## Limites

- Não consultei estoque/Tiny.
- Não fiz WhatsApp/backfill/envio.
- Não alterei Shopify/Chatwoot/cliente.
- Sem PII/raw customer dump no relatório final.
