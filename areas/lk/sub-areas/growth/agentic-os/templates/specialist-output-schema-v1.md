# LK Growth Agentic OS — Specialist Output Schema v1

Status: template operacional
Escopo: schema obrigatório para qualquer subagente interno do `lk-growth`

## Universal Specialist Output

```yaml
subagent: <Growth Data Scout | SEO/GEO Analyst | CRO/PDP Analyst | GMC/Product Data Analyst | Content/SEO Analyst — não-LKGOC | Experiment Reviewer>
run_id: <run id>
run_scope: <short scope>
called_by: Growth Planner
mode: read_only | preview | review

sources_checked:
  - source: <source name>
    status: verified | unavailable | stale | partial | not_needed
    used_for: <what this source supports>
    limitation: <none or limitation>

findings:
  - id: F-01
    finding: <plain-language finding>
    evidence:
      - <specific evidence, source, metric, URL, SKU, or citation>
    interpretation: <what it means>
    confidence: high | medium | low
    decision_grade: yes | no
    non_decision_grade_reasons:
      - <reason if no>
    recommendation: <safe recommendation>
    approval_needed: none | A3 | A4
    autonomy_level: A0 | A1 | A2 | A3-needed | A4-needed
    follow_up_metric: <metric and window>
    risks:
      - <risk>
    learning_hook:
      - <hypothesis or context update candidate>

blocked_items:
  - item: <what cannot proceed>
    reason: <why>
    required_source_or_approval: <source/approval needed>

summary_for_governor:
  strongest_evidence:
    - <item>
  weakest_or_riskiest_claims:
    - <item>
  recommended_top_actions:
    - <item>
  telegram_worthy: yes | no
  telegram_reason: <why>
```

## Specialist-specific minimums

### Growth Data Scout

Must include:

- source matrix;
- verified/unavailable/stale/partial classification;
- gaps that block decision-grade;
- no final business recommendation.

### SEO/GEO Analyst

Must include:

- query/topic;
- target URL or missing URL gap;
- source: GSC/DataForSEO/SERP/public HTML/Brain;
- intent;
- confidence;
- follow-up: impressions, clicks, CTR, position, AI/citation signal where available.

### CRO/PDP Analyst

Must include:

- URL/template/PDP/collection;
- funnel or UX gap;
- baseline source: GA4/Shopify/browser/PageSpeed/CrUX;
- impact/effort/risk;
- preview/rollback requirement;
- follow-up: conversion, add-to-cart, revenue, engagement, mobile split.

### GMC/Product Data Analyst

Must include:

- issue;
- offer IDs/SKUs or explicit missing-SKU gap;
- GMC/Merchant status;
- Shopify/feed/readback cross-check;
- source of overwrite risk;
- approval class for any correction.

### Content/SEO Analyst — não-LKGOC

Must include:

- confirmation that the task is not LKGOC/collection optimization, or a handoff to `[LK] Otimização de Coleções`;
- source page/content target when non-LKGOC;
- demand/intent evidence;
- proposed content structure;
- schema/FAQ/citability status;
- gap list and follow-up metric.

### Experiment Reviewer

Must include:

- original hypothesis;
- original baseline;
- observed D+7/D+14/D+30 metric;
- verdict;
- lesson;
- update recommendation for context pack/skill/template.

## Failure Conditions

The output is invalid if:

- it recommends a write without approval class;
- it hides missing essential sources;
- it treats hypothesis as fact;
- it has no follow-up metric;
- it lacks source status;
- it creates Telegram-worthy noise without decision/alert.
