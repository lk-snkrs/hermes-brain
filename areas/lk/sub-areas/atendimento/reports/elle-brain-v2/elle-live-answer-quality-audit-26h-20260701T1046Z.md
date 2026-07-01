# Elle — auditoria de respostas nas últimas 26h

Gerado: 2026-07-01T10:46Z  
Janela auditada: 2026-06-30T08:45Z → 2026-07-01T10:45Z  
Escopo: read-only em runtime/log vivo `/var/log/elle/events.jsonl`, health público, Chatwoot read-only via Doppler e gates locais. Nenhum envio, nenhum write externo, nenhum segredo impresso. `values_printed=false`.

## Prompt operacional melhorado

> Audite a qualidade das respostas públicas da Elle nas últimas 26 horas usando logs vivos e Chatwoot read-only. Responda: (1) ela respondeu tudo correto? (2) quais respostas foram erradas/frágeis e por quê? (3) houve autoavaliação/autocorreção/aprendizado supervisionado? (4) os erros já estavam antes ou depois das correções aplicadas? Separar `self-evaluation`, `production self-correction/guardrail`, `supervised drafts/lessons` e `auto-edit code/policy`. Verificar health, contadores de `processed`, `response_evaluated`, `eval_bad`, `risk medium/high`, `provider_error`, `v2_error`, `handoff_violations`, `autonomy_gate`, `autofix_loop`, e ler mensagens representativas no Chatwoot. Não usar Tiny/estoque direto; não prometer disponibilidade. Salvar relatório sanitizado com `values_printed=false`.

## Veredito curto

**Não respondeu tudo correto na janela bruta de 26h.** Houve **5 `eval_bad`** e **5 riscos médio/alto** dentro da janela total.

Mas há uma distinção importante: **os erros materiais mais graves aconteceram antes das correções de ontem** (`quality-fixes` e regra de cupom `ELLE5`). Depois da correção `ELLE5` às 2026-06-30T18:24:53Z, a janela pós-fix teve **12 respostas processadas, 0 `eval_bad` e 1 risco médio**, sem erro de provider/v2.

## Evidência operacional — janela 26h

Health público:

- `ok=true`
- `write_enabled=true`
- `kill_switch=false`
- `public_reply_enabled=true`
- `ai_enabled=true`
- `ai_provider=openrouter`
- `elle_brain_v2_canary_enabled=true`
- `elle_brain_v2_canary_percent=100`
- `catalog_stock_included=false`

Contadores do log vivo `/var/log/elle/events.jsonl`:

| Métrica | Valor |
|---|---:|
| eventos totais | 2480 |
| conversas com evento | 165 |
| respostas processadas | 42 |
| `response_evaluated` | 42 |
| `eval_good / ok / bad` | 26 / 11 / 5 |
| risco `high / medium / low / none` | 4 / 1 / 4 / 33 |
| `v2 used / skipped / error` | 7 / 35 / 0 |
| `provider_error` | 0 |
| `handoff_violations` | 0 |
| categorias `product_clear / coupon / greeting / human_handoff / stock_handoff` | 10 / 1 / 2 / 23 / 6 |
| decision source `v2 / guardrail / llm_final` | 7 / 34 / 1 |

Autonomy gate 26h:

```json
{
  "status": "hold",
  "processed": 42,
  "v2_canary_used": 7,
  "v2_canary_skipped": 35,
  "v2_canary_error": 0,
  "ai_provider_error": 0,
  "eval_bad": 5,
  "eval_medium_high": 5,
  "handoff_violations": 0,
  "recommendation": "do_not_expand_autonomy",
  "customer_send_executed": false,
  "writes_external": 0,
  "values_printed": false
}
```

## Separação antes/depois das correções

Correções materiais aplicadas ontem:

- `elle-quality-errors-fix-20260630.md`: correções de estoque/handoff, pós-venda, medidas, desconto genérico conservador.
- `elle-coupon-elle5-fix-20260630.md`: regra de Lucas: cupom de desconto é sempre `ELLE5`; corrigido runtime para responder cupom/primeira compra/desconto com `ELLE5` sem inventar porcentagem/condição.

Pós-correção `ELLE5` — desde 2026-06-30T18:24:53Z:

| Métrica pós-fix | Valor |
|---|---:|
| eventos | 947 |
| conversas com evento | 86 |
| respostas processadas | 12 |
| `eval_good / ok / bad` | 8 / 4 / 0 |
| risco médio/alto | 1 |
| `v2 used / skipped / error` | 1 / 11 / 0 |
| `provider_error` | 0 |
| categorias `human_handoff / stock_handoff / product_clear` | 7 / 3 / 2 |
| decision source `guardrail / v2` | 11 / 1 |

Leitura: **houve melhora após as correções**. O gate de 26h ainda fica `hold` porque a janela inclui erros pré-fix; a janela pós-fix não mostra `eval_bad`.

## Casos materiais auditados

| Conversa | Momento | Sinal | Leitura |
|---:|---|---|---|
| 2448 | pré-fix | `bad/high`, `product_clear` e depois `coupon` | Cliente perguntou cupom; Elle tinha resposta/contexto ruim e cupom frágil. Depois Lucas corrigiu: cupom é sempre `ELLE5`; runtime foi ajustado. |
| 1673 | pré-fix | `bad/high`, pós-venda/pedido | Handoff ocorreu, mas a resposta/copy era frágil para pedido já identificado. Humano assumiu e respondeu que conferiria status. |
| 2451 | pré-fix | `bad/low` + `bad/high` | Conversa com produto/sourcing/disponibilidade; houve perda de contexto e resposta que deveria ter sido handoff/stock antes. Humano assumiu e tratou disponibilidade/encomenda. |
| 1481 | pós-fix | `ok/medium`, `human_handoff` | Guardrail não prometeu estoque: fez handoff para Larissa/lk-stock. Risco médio vem de contexto incompleto/reativação de conversa antiga; não é `eval_bad`. |
| 2468 | pós-fix | `good/ok`, mas copy a melhorar | Primeira resposta de carrinho foi boa; depois cliente perguntou “loja física/SP” e a Elle classificou como `stock_handoff`, sem prometer disponibilidade. Seguro, porém over-conservative: pergunta institucional de loja física deveria responder endereço/atendimento se não houver pedido de disponibilidade/retirada/reserva. |

## Autoavaliação / auto-melhoria

| Camada | Funcionou? | Evidência |
|---|---|---|
| Autoavaliação | **Sim** | 42/42 respostas processadas tiveram avaliação na janela. |
| Guardrail/autocorreção de produção | **Parcialmente sim** | Gate ficou `hold`, recomendação `do_not_expand_autonomy`, 0 `handoff_violations`, e pós-fix não houve `eval_bad`. |
| Aprendizado supervisionado | **Sim, sem auto-write externo** | `guardrail_teaching_lesson_added=3` na janela 26h; autofix loop: `evaluations_seen=20`, `patch_suggestions_total=20`, `regression_drafts_total=20`, `auto_apply=false`, `writes_external=0`. |
| Auto-edição de código/política | **Não** | Correções produtivas foram feitas por Hermes com aprovação/ordem de Lucas; o loop não autoaplicou patch. |

## O que ainda melhorar

1. **Loja física vs disponibilidade**: separar melhor pergunta institucional (“vocês ficam em SP? tem loja física?”) de intenção de retirada/pronta entrega/reserva. A resposta da conv 2468 foi segura, mas desnecessariamente transbordou para estoque.
2. **Janela de gate pós-fix**: o gate 26h/24h ainda fica `hold` por carregar erros pré-correção. A leitura operacional deve considerar também um gate pós-fix/desde-deploy para não confundir histórico com degradação atual.
3. **Revisar conversas antigas reativadas**: caso 1481 mostrou `ok/medium` por contexto incompleto. Melhorar resumo de contexto quando cliente volta em conversa antiga.
4. **Manter cupom `ELLE5` como regra fixa**: não inventar porcentagem, validade ou condição; se cliente relatar erro no checkout, pedir print/etapa e handoff Larissa.

## Status

- Auditoria: concluída read-only.
- Writes externos: nenhum.
- Secrets/tokens: não impressos.
- Resultado: **não 100% na janela total; melhorou após as correções; ainda há melhoria de copy/roteamento em loja física e contexto antigo**.
