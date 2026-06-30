# Receipt — Supabase security gate broker RLS fix

- Data/hora: 2026-06-30T10:10:30.070086+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock / Supabase security
- Responsável humano: lk-stock
- Pedido original: Corrigir cron LK Supabase public exposure security gate daily usando Integration Auth Broker
- Classificação: infra-sensitive
- Fontes usadas:
- cron output /opt/data/profiles/lk-stock/cron/output/21ee8507b7b7/2026-06-30_09-00-23.md; hermes-cli-integrations smoke supabase; Supabase pooler psql via hermes_doppler; lk_supabase_security_gate.py --verbose
- O que foi feito:
- Broker Supabase validado com status ok/method psql_pooler_select_1/values_printed=false; identificadas 5 tabelas backup public com RLS desligado; após aprovação escopada de Lucas, aplicado enable row level security nessas 5 tabelas via broker/Doppler psql; gate verbose passou; wrapper cron silent-OK executou com stdout vazio.
- Output/artefato:
- status=pass; base_tables_rls_off=0; anon/auth table grants=0; custom public functions executable by anon/auth=0; sensitive anon REST probes retornaram 401; service_role probes retornaram 200; values_printed=false.
- Aprovação: Lucas aprovou no Telegram: APROVO aplicar exatamente esse SQL agora
- Envio/publicação: Sem envio externo; apenas resposta Telegram de conclusão.
- Writes externos: Supabase LK production SQL: ALTER TABLE ... ENABLE ROW LEVEL SECURITY em cinco tabelas backup public; nenhum token/secret impresso; values_printed=false.
- Riscos/bloqueios: Alteração em produção Supabase, mitigada por escopo limitado a tabelas backup; eventual consumidor público dessas tabelas backup ficaria bloqueado por RLS, o que é desejado para security gate.
- Rollback/mitigação: Se estritamente necessário e aprovado, reverter com ALTER TABLE ... DISABLE ROW LEVEL SECURITY nas mesmas cinco tabelas; não recomendado por reabrir o gate.
- Próximos passos: Cron diário permanece ativo; próxima execução automática deve ficar silent-OK. Se aparecer nova tabela backup em public com RLS off, repetir padrão broker+approval.
- Onde foi documentado no Brain: Receipt criado via hermes_memory_os_receipt_writer.py; skill supabase-security-operations já contém referência ao padrão broker-connected remediation.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
