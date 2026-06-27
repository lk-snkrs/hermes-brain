# Elle Brain v2 — structured output retry follow-up — 2026-06-26

**Escopo:** continuidade aprovada por Lucas (“seguir”) após Fase B/C local + shadow e itens 1–4.  
**Modo:** local/shadow classify-only; sem canary; sem envio a cliente; sem alteração do `app.py` produtivo.  
**values_printed:** false

## O que foi ajustado

Artefatos paralelos v2 apenas:

- `/app/elle_brain_v2.py`
- `/app/tests/elle_brain_v2_regression.py`
- cópias persistentes em `/opt/elle-chatwoot/` e `/opt/elle-chatwoot/brain-v2/`

Patch aplicado:

1. Parser JSON mais tolerante para respostas com code fence, texto antes/depois e string JSON encapsulada.
2. `response_format` estruturado com `json_schema` estrito na primeira tentativa.
3. Retry curto com `json_object` quando a primeira tentativa vem vazia/inválida.
4. `max_tokens` compatível com rota OpenRouter/OpenAI-like.
5. Observabilidade do `attempt`, sem imprimir conteúdo sensível.

## Verificação local

```json
{"ok": true, "tests": 32, "values_printed": false}
{"py_compile_ok": true, "regression_ok": true, "app_py_matches_backup": true, "values_printed": false}
```

## Shadow live pós-patch — amostra curta

Executado em `live_openrouter`, classify-only:

```json
{
  "events_tail": 10000,
  "processed_seen": 156,
  "live_openrouter_used": 40,
  "valid_json": 40,
  "invalid_json_or_error": 0,
  "valid_json_rate": "100%",
  "writes_external": 0,
  "values_printed": false
}
```

Arquivo local gerado nesta rodada:

- `/tmp/elle-brain-v2-structured-shadow-20260626T172245Z/shadow-report.json`
- `/tmp/elle-brain-v2-structured-shadow-20260626T172245Z/shadow-report.md`

## Shadow live pós-patch — rodada maior 100 chamadas

A rodada assíncrona maior terminou. O runner gerou o relatório no container, mas o pós-processamento tentou ler um caminho host incorreto e encerrou com exit code 1 depois de já imprimir o resumo. O relatório bruto foi resgatado do container e copiado para o Brain.

```json
{
  "events_tail": 10000,
  "processed_seen": 156,
  "live_openrouter_used": 100,
  "valid_json": 76,
  "invalid_json_or_error": 24,
  "valid_json_rate": "76%",
  "writes_external": 0,
  "values_printed": false
}
```

Resumo do runner na rodada 100:

```json
{
  "v2_categories": [["product_clear", 62], ["human_handoff", 43], ["stock_handoff", 24], ["greeting", 18], ["institutional", 5], ["coupon", 4]],
  "v2_policy_actions": [["allow", 77], ["handoff", 64], ["rewrite", 8], ["clarify", 7]],
  "v2_parse_status": [["valid_json", 76], ["not_consulted", 56], ["invalid_json_or_empty", 24]],
  "v2_providers": [["openrouter", 100], [null, 56]],
  "category_diff_count": 55,
  "handoff_diff_count": 41
}
```

Arquivos raw salvos:

- `areas/lk/sub-areas/atendimento/reports/elle-brain-v2/structured-output-shadow-100-raw-20260626/shadow-report.json`
- `areas/lk/sub-areas/atendimento/reports/elle-brain-v2/structured-output-shadow-100-raw-20260626/shadow-report.md`

## Leitura executiva atualizada

A amostra curta indicou melhoria, mas a rodada maior mostrou que o structured output **ainda não é estável**: `76/100 valid_json`, abaixo do critério de `>=95%`.

**Decisão técnica:** canary continua **NO-GO**.

Motivos:

1. `valid_json_rate=76%`, abaixo do alvo de 95%;
2. ainda existem 55 diferenças de categoria e 41 de handoff vs legado;
3. nenhuma mudança foi conectada ao `app.py` produtivo;
4. o policy engine segura risco, mas canary público exige parsing consistente.

## Segurança

- `customer_send_executed=false`
- `writes_external=0` para Chatwoot/WhatsApp/Shopify/Tiny
- OpenRouter usado apenas classify-only/shadow
- `app.py` produtivo preservado (`app_py_matches_backup=true`)
- sem restart/cutover/canary
- `values_printed=false`

## Próximo passo recomendado

Investigar os 24 `invalid_json_or_empty` da rodada 100 sem salvar conteúdo sensível: registrar só códigos/shape do provider, finish_reason, presença de `message.content`, `refusal`, `tool_calls`/campos alternativos e HTTP status. Depois ajustar provider/model/schema ou fallback antes de nova rodada 100.
