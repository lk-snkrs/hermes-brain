# Receipt — Elle LLM-primary playbook hotfix — IA decide casos seguros

- Data/hora: 2026-06-24T10:49:32.313547+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Atendimento / Elle
- Responsável humano: Lucas Cimino
- Pedido original: Lucas pediu corrigir arquitetura para ensinar a IA a responder e não transformar guardrail em atendente.
- Classificação: infra-sensitive
- Fontes usadas:
- Runtime /opt/elle-chatwoot; testes locais; smokes live OpenRouter sanitizados; docker/check_drift.
- O que foi feito:
- Prompt/playbook reforçado para IA ser decisora principal em casos comerciais seguros; fit/guide-size deixou de cair como estoque; safe cart/checkout e fit guidance deixam de ser sobrescritos por template quando LLM retorna JSON válido; guardrails de risco duro preservados.
- Output/artefato:
- Deploy via /opt/elle-chatwoot/scripts/recreate_elle.sh; container elle-chatwoot ativo na imagem elle-chatwoot:canonical-20260623; py_compile OK; smoke 8/8; regressão 9/9; drift OK; safe_product_browse/safe_fit/safe_cart com decision_source=llm_final; risk_availability/risk_deadline com rule_guardrail_after_llm.
- Aprovação: Aprovação explícita em Telegram: 'então corrigir'.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: Runtime/container Elle recriado localmente; sem Shopify/Tiny/estoque/Klaviyo/Meta/cliente direto.
- Riscos/bloqueios: Mudança em produção do bot Elle; mitigada com backup, regressões, smoke live, drift check e rollback.
- Rollback/mitigação: Backups: /opt/elle-chatwoot/rollbacks/20260624T104722Z/ e /opt/elle-chatwoot/rollbacks/20260624T094245Z/. Reverter arquivos e recriar container com helper se necessário.
- Próximos passos: Auditar próximas 24h: aumentar proporção llm_final em casos comerciais seguros; confirmar guardrail só em risco real; monitorar valid_json=false no caso de prazo.
- Onde foi documentado no Brain: Sim, receipt Brain e testes /opt/elle-chatwoot/tests/elle_behavior_regression_20260624.py.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
