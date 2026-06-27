# Approval Packet — Elle Brain v2 Canary

**Data:** 2026-06-26  
**Sistema:** Elle / Chatwoot / WhatsApp LK  
**Solicitação:** autorização futura para canary controlado da Elle Brain v2.  
**Status recomendado:** **NÃO APROVAR CANARY AINDA**; aprovar somente a próxima rodada de shadow live/structured-output fix.  
**values_printed:** false

## Resumo executivo

A Fase B/C local + shadow foi expandida: regressões subiram para 30 casos, o runner passou a suportar `live_openrouter`, e foi executado shadow classify-only com OpenRouter real em 35 eventos processados recentes. Não houve envio a clientes nem write externo.

A arquitetura v2 está no caminho certo, mas o canary público ainda deve esperar porque o shadow live retornou `valid_json` em 27/35 chamadas live e `invalid_json_or_empty` em 8/35. A camada policy segurou os riscos, mas canary exige structured output mais estável.

## Evidência

- Regression suite container: `{"ok": true, "tests": 30, "values_printed": false}`.
- Shadow heuristic: 36 processed; category diff 19; handoff diff 14; writes_external 0.
- Shadow live OpenRouter: 36 processed; 35 live calls; 27 valid JSON; 8 invalid/empty; 1 not consulted por limite; writes_external 0.
- Backup: `/root/elle-brain-v2-do-1-4-backups/20260626T160752Z`.
- Review: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/reports/elle-brain-v2/elle-brain-v2-do-1-4-shadow-live-review-20260626.md`.

## Escopo que seria aprovado no canary futuro

Se/quando aprovado, canary deve ser limitado a:

1. pequena porcentagem ou allowlist de conversas novas;
2. somente categorias seguras: greeting, product_clear, institutional, coupon;
3. hard guardrails sempre pós-LLM:
   - estoque/disponibilidade/pronta entrega/loja física/reserva → `stock_handoff`;
   - pós-venda/troca/devolução/reembolso/cancelamento/status → `human_handoff`;
   - prazo/CEP/frete dependente de fulfilment → `human_handoff`;
   - produto/foto incerta → clarificar, não sugerir aleatório;
4. logs com candidate/policy/final decision;
5. kill-switch e rollback documentados.

## Critérios mínimos antes de aprovar canary

- ≥95% `valid_json` no shadow live OpenRouter em janela relevante.
- 0 casos de promessa proibida em regression + shadow sample.
- 0 casos de estoque/disponibilidade respondidos como disponibilidade confirmada.
- Revisão qualitativa das principais diferenças vs legado.
- `app.py` produtivo alterado somente em patch aprovado, com backup/rollback/readback.

## Decisão pedida

**Minha recomendação:** aprovar apenas a próxima etapa local/shadow:

> Corrigir structured output/retry do OpenRouter e rodar novo shadow live maior. Não ativar canary ainda.

## Rollback se algum artefato paralelo incomodar

Remover/corrigir apenas artefatos paralelos:

- `/app/elle_brain_v2.py`
- `/app/tests/elle_brain_v2_regression.py`
- `/app/scripts/elle_brain_v2_shadow_runner.py`
- `/opt/elle-chatwoot/brain-v2/`

`/app/app.py` não foi alterado por este pacote.
