# Elle Brain v2 — OpenRouter diagnostics + token budget follow-up — 2026-06-26

**Escopo:** continuidade segura após rodada 100 mostrar `76/100 valid_json`.  
**Modo:** local/shadow classify-only; sem canary; sem envio a cliente; sem alteração do `app.py` produtivo.  
**values_printed:** false

## Hipótese investigada

A rodada 100 anterior mostrou `invalid_json_or_empty` sem erro HTTP. Foi adicionada observabilidade sanitizada para entender o shape da resposta, sem raw customer text e sem raw LLM output.

Campos coletados:

- `finish_reason`
- bucket de tamanho do `message.content`
- presença/ausência de content
- parse failure class
- error class
- tentativa 1 vs retry

## Diagnóstico antes do ajuste de token budget

Amostra `live_limit=50`, após instrumentação:

```json
{
  "live_used": 50,
  "valid_json": 42,
  "invalid_or_error": 8,
  "valid_json_rate": "84%",
  "finish_reason": [["stop", 28], ["length", 22]],
  "content_len_bucket": [["101-500", 37], ["0", 8], ["501+", 5]],
  "parse_failure": [["none", 42], ["json_parse_none", 8]],
  "error_class": [["", 50]],
  "attempt": [[1, 42], [2, 8]],
  "writes_external": 0,
  "values_printed": false
}
```

**Leitura:** falha concentrada em `finish_reason=length` + conteúdo vazio no retry. Não havia erro HTTP/provider. A causa provável era orçamento de tokens insuficiente para structured output/retry no modelo atual.

## Ajuste aplicado

Somente no artefato paralelo `/app/elle_brain_v2.py`:

- primeira tentativa: `max_tokens` de 500 para 900;
- retry: `max_tokens` de 350 para 700.

Nenhuma mudança em `app.py` produtivo.

## Verificação local pós-ajuste

```json
{"ok": true, "tests": 34, "values_printed": false}
{"py_compile_ok": true, "regression_ok": true, "app_py_matches_backup": true, "values_printed": false}
```

## Shadow live pós-ajuste de token budget

Amostra `live_limit=50`:

```json
{
  "live_used": 50,
  "valid_json": 49,
  "invalid_or_error": 1,
  "valid_json_rate": "98%",
  "finish_reason": [["stop", 49], ["length", 1]],
  "content_len_bucket": [["101-500", 39], ["501+", 10], ["0", 1]],
  "parse_failure": [["none", 49], ["json_parse_none", 1]],
  "error_class": [["", 50]],
  "attempt": [[1, 49], [2, 1]],
  "writes_external": 0,
  "values_printed": false
}
```

## Leitura executiva

O diagnóstico confirmou que o problema principal era `finish_reason=length` por token budget baixo. O ajuste subiu a estabilidade da amostra de 50 chamadas de `84%` para `98% valid_json`.

**Canary ainda não está aprovado.** O gate oficial continua sendo rodada de 100 chamadas com `>=95% valid_json` + revisão qualitativa dos diffs.

## Próximo passo

Rodar a rodada-gate com `live_limit=100` usando o token budget novo. Se bater `>=95%`, ainda assim revisar qualitativamente diffs antes de qualquer canary.

## Segurança

- `customer_send_executed=false`
- `writes_external=0` para Chatwoot/WhatsApp/Shopify/Tiny
- OpenRouter usado apenas classify-only/shadow
- `app.py` produtivo preservado
- sem restart/cutover/canary
- `values_printed=false`
