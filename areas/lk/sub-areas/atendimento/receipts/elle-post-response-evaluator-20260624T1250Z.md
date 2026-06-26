# Receipt — Elle post-response evaluator — cada resposta gera evidência

- Data/hora: 2026-06-24T12:50:49.695851+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Atendimento / Elle
- Responsável humano: Lucas Cimino
- Pedido original: Lucas aprovou adicionar um avaliador pós-resposta para a Elle ficar mais inteligente sem autoaprendizado solto.
- Classificação: infra-sensitive
- Fontes usadas:
- Runtime /opt/elle-chatwoot; testes locais; smoke dentro do container; docker/check_drift.
- O que foi feito:
- Adicionado avaliador pós-resposta: após processar/decidir uma resposta, a Elle avalia qualidade/risco, registra evento response_evaluated e cria candidato em /data/supervised_learning/evaluations.jsonl quando há erro/risco/oportunidade clara. O avaliador nunca escreve lesson automática; should_auto_learn=false.
- Output/artefato:
- Deploy via recreate_elle.sh; container elle-chatwoot ativo; py_compile OK; smoke 8/8; regressão 11/11; drift OK; smoke container confirmou quality=bad risk_level=high candidate_added=true source=post_response_evaluator should_auto_learn=false values_printed=false.
- Aprovação: Aprovação explícita em Telegram: 'Achei ótimo vamos adicionar um avaliador'.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: Runtime/container Elle recriado localmente; gravação futura local em /data/supervised_learning/evaluations.jsonl e logs; sem Shopify/Tiny/estoque/Klaviyo/Meta/cliente direto.
- Riscos/bloqueios: Mudança em produção do bot Elle e mais chamadas de IA por resposta; mitigada com sample rate configurável ELLE_POST_RESPONSE_EVALUATOR_SAMPLE_RATE, testes, smoke no container, drift check e rollback.
- Rollback/mitigação: Rollback: restaurar /opt/elle-chatwoot/rollbacks/20260624T124937Z/app.py e teste se necessário, depois recriar container com /opt/elle-chatwoot/scripts/recreate_elle.sh.
- Próximos passos: Auditar custo/latência e qualidade dos candidatos; se houver volume alto, reduzir ELLE_POST_RESPONSE_EVALUATOR_SAMPLE_RATE ou filtrar por categorias.
- Onde foi documentado no Brain: Sim, receipt Brain e teste /opt/elle-chatwoot/tests/elle_behavior_regression_20260624.py::test_post_response_evaluator_logs_evidence_and_candidate_without_auto_lesson.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
