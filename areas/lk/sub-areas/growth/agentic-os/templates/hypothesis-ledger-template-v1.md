# LK Growth Agentic OS — Hypothesis Ledger Template v1

Status: template operacional
Escopo: registrar hipóteses mensuráveis geradas por execuções agentic do `lk-growth`

## Ledger Metadata

- ledger_owner: `lk-growth`
- created_at: `<YYYY-MM-DD>`
- last_updated: `<YYYY-MM-DD>`
- related_run_receipt: `<path>`
- related_approval_packet: `<path or none>`

## Hypothesis Entry

```yaml
hypothesis_id: HYP-<YYYYMMDD>-<short-slug>
created_at: <YYYY-MM-DD>
created_by_run: <run_id>
domain: SEO_GEO | CRO_PDP | GMC_PRODUCT | CONTENT_COLLECTION | PAID_RECON | LOCAL | CRM | TECHNICAL
status: proposed | preview_created | approved | implemented | reviewing_D7 | reviewing_D14 | reviewing_D30 | closed
confidence_at_creation: high | medium | low
autonomy_level: A0 | A1 | A2 | A3-needed | A4-needed

hypothesis: >
  If <change/intervention> then <expected measurable result> because <evidence/reasoning>.

source_evidence:
  - source: <Brain/GSC/GA4/Shopify/GMC/DataForSEO/PageSpeed/etc>
    status: verified | unavailable | stale | partial
    evidence: <short fact>

scope:
  urls:
    - <url or handle>
  products_or_skus:
    - <sku/offer id if relevant>
  collections:
    - <collection handle if relevant>
  audience_or_segment: <if relevant>

expected_metric:
  primary: <metric>
  secondary:
    - <metric>
  measurement_window: D+7 | D+14 | D+30 | custom
  baseline_required: yes | no
  baseline_value: <value or pending>

risk:
  level: low | medium | high
  notes:
    - <risk>
  rollback: <rollback approach if implemented>

approval:
  required: none | A3 | A4
  approval_id: <if approved>
  approved_scope: <exact scope>

implementation:
  implemented: no | yes
  implemented_at: <date or pending>
  receipt_path: <path or none>
  external_writes: no | yes

review:
  D7:
    date: <date>
    observed_metric: <value>
    verdict: improved | neutral | worsened | inconclusive | insufficient_data | pending
    notes: <notes>
  D14:
    date: <date>
    observed_metric: <value>
    verdict: improved | neutral | worsened | inconclusive | insufficient_data | pending
    notes: <notes>
  D30:
    date: <date>
    observed_metric: <value>
    verdict: improved | neutral | worsened | inconclusive | insufficient_data | pending
    notes: <notes>

learning:
  lesson: <what the system learned>
  update_context_pack: yes | no
  update_skill_or_template: yes | no
  kill_or_repeat: kill | repeat | refine | monitor
```

## Decision Rules

- Uma hipótese sem fonte essencial verificada pode existir, mas deve começar como `confidence_at_creation: low` ou `medium` e `status: proposed`.
- Hipótese A3/A4 não pode virar `implemented` sem approval packet.
- Toda hipótese implementada precisa de D+7/D+14 ou justificativa para janela diferente.
- Hipóteses repetidas sem aprendizado devem ser marcadas `kill` ou `refine`, não reiniciadas indefinidamente.

## Compact Table View

| ID | Domain | Hypothesis | Status | Confidence | Approval | Primary Metric | Next Review | Verdict |
|---|---|---|---|---|---|---|---|---|
| HYP-YYYYMMDD-slug | SEO_GEO | If...then... | proposed | medium | A3-needed | CTR | D+14 | pending |
