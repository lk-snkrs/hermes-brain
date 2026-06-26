# Feedback Ledger — LK Shopify OS

Data de criação: 2026-06-05
Status: operacional local/read-only.

## Função

Registrar aprendizado operacional do LK Shopify depois de previews, QA, approvals, execuções, readbacks, receipts e rollbacks. O objetivo é melhorar segurança, reduzir variações e transformar padrões repetidos em templates/skills.

## Quando registrar

Registrar quando houver:

- feedback de Lucas sobre preview/execução;
- aprovação/rejeição de write;
- QA visual/técnico com falha ou correção;
- readback divergente;
- rollback usado ou insuficiente;
- padrão repetido de produto/coleção/page/theme;
- correção de fronteira entre Shopify, Growth, Ops e Tiny.

## Template

```yaml
id: SHOPIFY-FEEDBACK-YYYYMMDD-001
created_at: YYYY-MM-DDTHH:MM:SSZ
source: Lucas | qa | readback | receipt | rollback | agent_governance | other
related_ids:
  inbox: null
  preview: null
  packet: null
  receipt: null
  growth_opportunity: null
feedback_type: correction | approval | rejection | qa_learning | readback_learning | rollback_learning | process_learning
summary: "aprendizado curto"
what_changed: "o que deve mudar no processo"
action_required: none | update_preview_template | update_skill | update_routine | update_mapa | create_packet | block_pattern
owner: lk-shopify
status: open | applied | deferred
links:
  evidence: null
  changed_file: null
notes: []
```

## Regra 1x/2x/3x

- 1 vez: registrar se for relevante.
- 2 vezes: criar/ajustar template ou fonte canônica.
- 3 vezes ou impacto alto: atualizar skill/rotina.

## Entradas atuais

Sem entradas novas nesta criação.
