# Feedback Ledger — LK Growth OS

Data de criação: 2026-06-05
Status: operacional local/read-only.

## Função

Registrar aprendizado operacional do LK Growth depois de briefs, packets, approvals, execuções e impact reviews. O objetivo é transformar repetição em padrão canônico, skill ou rotina.

## Quando registrar

Registrar quando houver:

- feedback de Lucas;
- aprovação/rejeição de packet;
- write aprovado executado por LK Shopify ou outro agente;
- impacto D+7/D+14/D+30;
- erro de diagnóstico;
- oportunidade que virou padrão repetível;
- correção arquitetural ou de linguagem.

## Template

```yaml
id: GROWTH-FEEDBACK-YYYYMMDD-001
created_at: YYYY-MM-DDTHH:MM:SSZ
source: Lucas | impact_review | receipt | qa | agent_governance | other
related_ids:
  inbox: null
  opportunity: null
  packet: null
  receipt: null
  shopify_preview: null
feedback_type: correction | approval | rejection | impact_learning | risk_learning | style_learning | process_learning
summary: "aprendizado curto"
what_changed: "o que deve mudar no processo"
action_required: none | update_template | update_skill | update_routine | update_mapa | create_packet | block_pattern
owner: lk-growth
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
