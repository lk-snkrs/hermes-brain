# Receipt — Shopify LK broker smoke OK — stale reauth packet archived

- Data/hora: 2026-06-28T18:04:43.794853+00:00
- Agente/profile/cron: Hermes default / integration auth broker control-plane
- Empresa/área: Operações Hermes / Shopify LK auth broker
- Responsável humano: Hermes Agent
- Pedido original: Lucas repassou mensagem do LK Stock dizendo que shopify_lk smoke falhou e que criou approval packet de reauth.
- Classificação: local-write
- Fontes usadas:
- Live smoke default; live smoke com HERMES_HOME=/opt/data/profiles/lk-stock; hermes-cli-run --audit-json; approval-packet path.
- O que foi feito:
- Revalidei shopify_lk via broker no default e no ambiente LK Stock; ambos OK. Revalidei audit-json com exit_code 0/status ok. Arquivei o approval packet como stale/no-action.
- Output/artefato:
- shopify_lk status OK; reauth não necessária agora; active approval packet removido para archived/stale-smoke-ok; values_printed=false.
- Aprovação: Correção local/read-only/documental decorrente de inconsistência apontada por Lucas; sem writes externos e sem secrets.
- Envio/publicação: Telegram: resumo final nesta conversa.
- Writes externos: 0
- Riscos/bloqueios: Se LK Stock usou cache de contexto antigo, pode precisar nova mensagem/novo turno; runtime e fonte viva já estão OK.
- Rollback/mitigação: Mover archived/shopify-lk-reauth-central-auth-broker-20260628.stale-smoke-ok.md de volta para approval-packets se smoke fresco voltar a falhar.
- Próximos passos: LK Stock pode fazer readback read-only de webhookSubscriptions pelo broker se a tarefa ainda for necessária.
- Onde foi documentado no Brain: Receipt atual e archived approval packet com nota stale.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
