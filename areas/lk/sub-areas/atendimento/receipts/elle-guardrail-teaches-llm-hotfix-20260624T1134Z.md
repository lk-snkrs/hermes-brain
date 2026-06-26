# Receipt — Elle guardrail override teaching loop — veto corrige e ensina IA

- Data/hora: 2026-06-24T11:33:21.612364+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Atendimento / Elle
- Responsável humano: Lucas Cimino
- Pedido original: Lucas pediu que quando o guardrail vetar a IA, o sistema corrija e ensine a IA como deveria responder.
- Classificação: infra-sensitive
- Fontes usadas:
- Runtime /opt/elle-chatwoot; testes locais; smoke dentro do container; docker/check_drift.
- O que foi feito:
- Adicionado loop supervisionado: quando decision_source=rule_guardrail_after_llm e a saída da IA era JSON válido, Elle registra lesson sanitizada em supervised_learning/lessons.jsonl com wrong_pattern, corrected_rule, expected_category e forbidden_terms. O prompt já carrega essas lessons em chamadas futuras, então o veto vira ensino para a IA.
- Output/artefato:
- Deploy via /opt/elle-chatwoot/scripts/recreate_elle.sh; container elle-chatwoot ativo; py_compile OK; smoke 8/8; regressão 10/10; drift OK; smoke container confirmou lesson_added=true, lesson_source=guardrail_override, expected_category=stock_handoff, values_printed=false.
- Aprovação: Aprovação explícita em Telegram: 'Mas ao vetar ela e corriga e depois ela ensina de novo a ela e como tem que responder.'
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: Runtime/container Elle recriado localmente; gravação futura apenas em /data/supervised_learning/lessons.jsonl; sem Shopify/Tiny/estoque/Klaviyo/Meta/cliente direto.
- Riscos/bloqueios: Mudança em produção do bot Elle; mitigada com teste RED/GREEN, regressões, smoke no container, drift check e rollback anterior /opt/elle-chatwoot/rollbacks/20260624T104722Z/.
- Rollback/mitigação: Rollback: restaurar /opt/elle-chatwoot/rollbacks/20260624T104722Z/app.py para /opt/elle-chatwoot/app/app.py e recriar container com /opt/elle-chatwoot/scripts/recreate_elle.sh.
- Próximos passos: Auditar próximas 24h: verificar lessons guardrail_override adicionadas, redução de overrides repetidos e aumento de llm_final em casos seguros.
- Onde foi documentado no Brain: Sim, receipt Brain e teste /opt/elle-chatwoot/tests/elle_behavior_regression_20260624.py::test_guardrail_override_writes_supervised_teaching_lesson.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
