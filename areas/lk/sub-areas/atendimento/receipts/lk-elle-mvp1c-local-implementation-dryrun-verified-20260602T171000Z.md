# Receipt — Elle MVP 1C local implementation and dry-run verification

- Data UTC: 2026-06-02T17:10:00Z
- Produto: Elle MVP 1C
- Sistema alvo: Chatwoot `https://chat.lkskrs.online`
- Account: `LK Sneakers` / ID `1`

## Aprovação recebida

Lucas aprovou explicitamente o MVP 1C em modo sem mensagem pública, com permissão para notas privadas, labels e transbordo para `atendimento whatsapp`, mantendo proibição de mensagem pública e alterações Shopify/Tiny/WhatsApp/produtos/pedidos/estoque/preço/tema.

## Implementado localmente no Brain

Policies:

- `policies/elle_intents.yaml`
- `policies/elle_guardrails.yaml`
- `policies/elle_private_note_template.md`

Fixtures:

- `evaluation/fixtures/chatwoot_message_created_examples.jsonl`

Scripts:

- `scripts/elle_dryrun_classifier.py`
- `scripts/chatwoot_internal_actions.py`
- `scripts/chatwoot_context.py`
- `scripts/shopify_context_policy.py`
- `scripts/tiny_stock_gate.py`
- `scripts/elle_mvp1c_dryrun.py`

Tests:

- `evaluation/test_elle_classifier.py`
- `evaluation/test_elle_idempotency.py`
- `evaluation/test_chatwoot_internal_actions.py`
- `evaluation/test_chatwoot_context.py`
- `evaluation/test_shopify_context_policy.py`
- `evaluation/test_tiny_stock_gate.py`

Approval packet:

- `approval-packets/elle-mvp1c-chatwoot-webhook-approval-20260602.md`

Dry-run report:

- `evaluation/reports/elle_mvp1c_dryrun_20260602.md`

## TDD / verificação

Testes primeiro foram executados antes da implementação e falharam por módulos ausentes, como esperado.

Após implementação, verificação final:

```bash
cd /opt/data/hermes_bruno_ingest/hermes-brain && \
python3 areas/lk/sub-areas/atendimento/evaluation/test_elle_classifier.py && \
python3 areas/lk/sub-areas/atendimento/evaluation/test_elle_idempotency.py && \
python3 areas/lk/sub-areas/atendimento/evaluation/test_chatwoot_internal_actions.py && \
python3 areas/lk/sub-areas/atendimento/evaluation/test_chatwoot_context.py && \
python3 areas/lk/sub-areas/atendimento/evaluation/test_shopify_context_policy.py && \
python3 areas/lk/sub-areas/atendimento/evaluation/test_tiny_stock_gate.py && \
python3 areas/lk/sub-areas/atendimento/scripts/elle_mvp1c_dryrun.py
```

Resultado:

- `test_elle_classifier OK`
- `test_elle_idempotency OK`
- `test_chatwoot_internal_actions OK`
- `test_chatwoot_context OK`
- `test_shopify_context_policy OK`
- `test_tiny_stock_gate OK`
- Dry-run: 12 fixtures
- Intent OK: 12/12
- Labels OK: 12/12
- Risk OK: 12/12
- Handoff OK: 12/12
- Forbidden public actions: 0

YAML parse também verificado para `elle_guardrails.yaml` e `elle_intents.yaml`.

## Segurança implementada

- Adapter Chatwoot não implementa função de mensagem pública.
- Padrões runtime: dry-run/write disabled/kill switch ligado.
- Idempotência por event/message id.
- Filtro ignora outbound, nota privada e evento da própria Elle.
- Shopify policy permite apenas contexto; bloqueia writes e estoque final.
- Tiny gate exige produto/SKU/tamanho resolvido e fonte fresca para sugestão de disponibilidade.

## Não executado

- Nenhum webhook criado no Chatwoot.
- Nenhuma mensagem pública enviada.
- Nenhuma nota/label/assignment em produção executado por Hermes neste passo.
- Nenhuma alteração em Shopify, Tiny, WhatsApp, produto, pedido, estoque, preço, tema ou campanha.

## Bloqueio para produção

Para ativar de fato, ainda falta:

1. URL pública do webhook receiver da Elle.
2. Webhook secret.
3. Token Chatwoot em cofre/ambiente seguro.
4. Confirmar ID do time `atendimento whatsapp`.
5. Smoke test em `DRY_RUN=true` antes de `CHATWOOT_WRITE_ENABLED=true`.
