# Elle MVP 1C — Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task after Lucas explicitly approves the production Chatwoot write scope.

**Goal:** Build Elle MVP 1C for Chatwoot: classify incoming customer conversations, create private notes, apply labels, and route/transbord to humans without sending public customer messages.

**Architecture:** A small webhook receiver ingests Chatwoot events, validates the webhook secret, deduplicates event/message IDs, fetches conversation/contact context, classifies intent/risk with LK policies, then performs only approved Chatwoot internal writes: private note, labels, and optional assignment to `atendimento whatsapp`. The system must include dry-run mode and kill switch before any production writes.

**Tech Stack:** Chatwoot API/webhooks, Python or Node service, local config/secrets via Doppler or environment, Hermes Brain policy files, Tiny/Shopify read-only context adapters, audit logs.

---

## Preconditions

- Chatwoot URL: `https://chat.lkskrs.online`
- Account ID: `1`
- Existing labels: `pedido`, `estoque`, `troca`, `devolucao`, `prazo`, `reclamacao`, `vip`, `financeiro`, `humano`, `whatsapp-api`
- Existing team: `atendimento whatsapp`
- Shopify connected and enabled.
- WhatsApp Business API inbox may still be pending; MVP can be tested against any Chatwoot incoming conversation/inbox, but production WhatsApp activation requires separate approval.

## Production approval required before implementation writes

Lucas must approve this exact scope before creating production webhooks or running write mode:

```text
Aprovo o MVP 1C da Elle no Chatwoot em modo sem mensagem pública:
- criar notas privadas
- aplicar labels operacionais
- transbordar para o time atendimento whatsapp
- não enviar mensagens públicas ao cliente
- não alterar Shopify/Tiny/WhatsApp/produtos/pedidos/estoque/preço/tema
- usar Shopify só como contexto e Tiny como fonte de estoque
```

Until then, only documentation, local dry-run code, and read-only checks are allowed.

---

## Task 1: Create policy source files

**Objective:** Create machine-readable policy files from the operational matrix.

**Files:**
- Create: `areas/lk/sub-areas/atendimento/policies/elle_intents.yaml`
- Create: `areas/lk/sub-areas/atendimento/policies/elle_guardrails.yaml`
- Create: `areas/lk/sub-areas/atendimento/policies/elle_private_note_template.md`

**Steps:**

1. Convert each intent from `elle-mvp1-c-operational-matrix-20260602.md` into YAML:
   - name
   - labels
   - default_risk
   - handoff_required conditions
   - allowed_actions
   - prohibited_actions
   - required_sources
2. Add global guardrails:
   - no_public_reply in MVP 1C
   - Tiny stock truth
   - Shopify context only
   - sensitive intents force human
3. Add the private note template exactly as defined in the matrix.
4. Verify YAML parse with a local parser.

**Verification command:**

```bash
python - <<'PY'
import yaml, pathlib
for p in pathlib.Path('areas/lk/sub-areas/atendimento/policies').glob('elle_*.yaml'):
    yaml.safe_load(p.read_text())
    print('OK', p)
PY
```

Expected: every policy YAML prints `OK`.

---

## Task 2: Define dry-run event fixture format

**Objective:** Create fixtures that simulate Chatwoot events without touching production.

**Files:**
- Create: `areas/lk/sub-areas/atendimento/evaluation/fixtures/chatwoot_message_created_examples.jsonl`

**Steps:**

1. Add at least 12 anonymized fixture events:
   - greeting
   - order status
   - delayed order complaint
   - stock/size clear
   - stock/size ambiguous
   - exchange
   - return
   - financial/payment
   - VIP order
   - preorder/encomenda
   - unrelated/ambiguous
   - angry customer
2. Each fixture should include:
   - event_id
   - conversation_id
   - message_id
   - message_type: incoming
   - content
   - contact: name/email/phone redacted or synthetic
   - expected_intents
   - expected_labels
   - expected_risk
   - expected_handoff

**Verification:**

Run a JSONL parser and assert every line has required fields.

---

## Task 3: Build classifier dry-run script

**Objective:** Implement a local dry-run classifier that maps message text to intent/risk/labels using policy files.

**Files:**
- Create: `areas/lk/sub-areas/atendimento/scripts/elle_dryrun_classifier.py`
- Test/Create: `areas/lk/sub-areas/atendimento/evaluation/test_elle_classifier.py`

**Steps:**

1. Write tests for the 12 fixtures.
2. Implement deterministic baseline rules first:
   - keywords for pedido/prazo/estoque/troca/devolucao/reclamacao/financeiro/vip/encomenda
   - risk escalation rules
   - `humano` label on high-risk cases
3. Ensure no public response action is ever produced.
4. Produce output shape:

```json
{
  "intent": ["estoque"],
  "labels": ["estoque", "whatsapp-api"],
  "risk": "medio",
  "handoff": false,
  "sources_needed": ["tiny"],
  "private_note": "..."
}
```

**Verification command:**

```bash
python areas/lk/sub-areas/atendimento/evaluation/test_elle_classifier.py
```

Expected: all fixtures pass.

---

## Task 4: Add idempotency and event filtering logic

**Objective:** Ensure duplicate events and bot/outbound messages do not create repeated actions.

**Files:**
- Modify/Create: `areas/lk/sub-areas/atendimento/scripts/elle_dryrun_classifier.py`
- Test/Create: `areas/lk/sub-areas/atendimento/evaluation/test_elle_idempotency.py`

**Steps:**

1. Add event filter:
   - accept only `message_created` / incoming customer messages
   - ignore private notes
   - ignore outbound messages
   - ignore events from Elle itself
2. Add idempotency key: `event_id` if present, else `message_id`.
3. In dry-run, store processed IDs in a local temp file or in-memory set for tests.
4. Write tests for duplicate event handling.

**Verification:**

Expected duplicate fixture produces zero second action.

---

## Task 5: Define Chatwoot API write adapter in disabled mode

**Objective:** Prepare Chatwoot write adapter with public-message sends impossible by construction.

**Files:**
- Create: `areas/lk/sub-areas/atendimento/scripts/chatwoot_internal_actions.py`
- Test/Create: `areas/lk/sub-areas/atendimento/evaluation/test_chatwoot_internal_actions.py`

**Steps:**

1. Implement functions:
   - `create_private_note(conversation_id, content)`
   - `apply_labels(conversation_id, labels)`
   - `assign_team(conversation_id, team_id)`
2. Do not implement public message send function in MVP 1C.
3. Add runtime mode:
   - `DRY_RUN=true` default
   - `CHATWOOT_WRITE_ENABLED=false` default
   - `ELLE_KILL_SWITCH=true` default blocks writes
4. Tests must assert no function exists/can call public reply endpoint.
5. Tests must assert dry-run prints intended actions without HTTP.

**Verification:**

Run tests and grep code for forbidden public endpoint usage.

---

## Task 6: Add read-only Chatwoot context adapter

**Objective:** Fetch conversation/contact/team/label context read-only.

**Files:**
- Create: `areas/lk/sub-areas/atendimento/scripts/chatwoot_context.py`
- Test/Create: `areas/lk/sub-areas/atendimento/evaluation/test_chatwoot_context.py`

**Steps:**

1. Implement safe GET wrappers for:
   - account
   - conversation
   - messages
   - contact
   - labels
   - teams
2. Require token via environment; never print token.
3. Add redaction for PII in logs.
4. Mock HTTP in tests.

**Verification:**

Unit tests pass and no token appears in captured logs.

---

## Task 7: Add Shopify context usage boundary

**Objective:** Encode that Shopify is context only.

**Files:**
- Create: `areas/lk/sub-areas/atendimento/scripts/shopify_context_policy.py`
- Test/Create: `areas/lk/sub-areas/atendimento/evaluation/test_shopify_context_policy.py`

**Steps:**

1. Implement a policy function that allows Shopify use for:
   - customer lookup
   - order summary
   - fulfillment/financial status display
2. Block any Shopify write/action categories.
3. Ensure stock answers never use Shopify inventory as final truth.
4. Tests verify blocked operations.

---

## Task 8: Add Tiny stock requirement gate

**Objective:** Ensure stock/availability notes require Tiny/fresh snapshot or produce a block/handoff.

**Files:**
- Create: `areas/lk/sub-areas/atendimento/scripts/tiny_stock_gate.py`
- Test/Create: `areas/lk/sub-areas/atendimento/evaluation/test_tiny_stock_gate.py`

**Steps:**

1. Define stock request resolver fields:
   - product
   - SKU
   - size
   - confidence
2. If product/SKU/size ambiguous, require handoff.
3. If Tiny source is missing/stale, require handoff.
4. If Tiny source fresh, allow private suggestion with explicit size.
5. Tests cover clear, ambiguous, stale, missing cases.

---

## Task 9: End-to-end dry-run report

**Objective:** Run fixtures through the full dry-run pipeline and produce an audit report.

**Files:**
- Create: `areas/lk/sub-areas/atendimento/scripts/elle_mvp1c_dryrun.py`
- Output: `areas/lk/sub-areas/atendimento/evaluation/reports/elle_mvp1c_dryrun_YYYYMMDD.md`

**Steps:**

1. Load fixtures.
2. Run filter, classifier, policy, note formatter, routing decision.
3. Print intended Chatwoot actions only.
4. Produce report with:
   - fixture count
   - intent accuracy
   - label accuracy
   - handoff accuracy
   - any forbidden action attempted
5. Expected forbidden action count must be zero.

---

## Task 10: Production webhook approval packet

**Objective:** Prepare but do not execute the production Chatwoot webhook configuration.

**Files:**
- Create: `areas/lk/sub-areas/atendimento/approval-packets/elle-mvp1c-chatwoot-webhook-approval-YYYYMMDD.md`

**Steps:**

1. Document webhook URL target.
2. Document events subscribed.
3. Document secret/signature validation.
4. Document exact Chatwoot writes:
   - private note
   - labels
   - team assignment
5. Document explicit non-actions:
   - no public reply
   - no Shopify/Tiny writes
   - no WhatsApp sends
6. Include rollback:
   - disable webhook
   - set kill switch
   - revoke token if needed

---

## Task 11: Controlled production activation after approval

**Objective:** Activate only after Lucas approves the packet.

**Files:**
- Create receipt in `areas/lk/sub-areas/atendimento/receipts/`

**Steps:**

1. Confirm current approval text in chat.
2. Verify Chatwoot health read-only.
3. Create/configure webhook with narrow events.
4. Keep `CHATWOOT_WRITE_ENABLED=false` for first smoke test.
5. Send/receive controlled test event.
6. Verify no public message sent.
7. Enable internal writes only if smoke test passes and Lucas approves.
8. Test one controlled conversation.
9. Write receipt with evidence.

---

## Verification-before-completion checklist

Before claiming MVP 1C operational:

- [ ] Policies parse.
- [ ] Fixture tests pass.
- [ ] Idempotency tests pass.
- [ ] No public message endpoint is implemented/called.
- [ ] Kill switch tested.
- [ ] Token redaction tested.
- [ ] Dry-run report generated.
- [ ] Chatwoot webhook approved explicitly.
- [ ] Controlled production test verified.
- [ ] No Shopify/Tiny/WhatsApp external write occurred.
- [ ] Brain receipt written.
