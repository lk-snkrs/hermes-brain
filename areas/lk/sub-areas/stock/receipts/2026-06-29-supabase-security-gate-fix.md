# Receipt — Supabase LK security gate conectado ao broker e correção aplicada

- Data/hora: 2026-06-29T09:14:31.543493+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock OS / Supabase security
- Responsável humano: lk-stock
- Pedido original: Lucas aprovou aplicar a correção do Supabase LK security gate após conexão pelo Integration Auth Broker.
- Classificação: external-write
- Fontes usadas:
- Integration Auth Broker smoke supabase: status ok method psql_pooler_select_1 rc 0; Supabase MCP readback; lk_supabase_security_gate.py --verbose; cron job 21ee8507b7b7.
- O que foi feito:
- Aplicado em produção Supabase LK: ENABLE ROW LEVEL SECURITY nas tabelas public.lk_stock_items_backup_20260628_dedupe e public.lk_stock_snapshots_backup_20260628_dedupe; REVOKE EXECUTE da função public.lk_compras_next_seq() para public, anon e authenticated. Wrapper do cron valida broker Supabase antes do gate.
- Output/artefato:
- Gate passou após correção: status=pass, base_tables_rls_off=0, anon_select_granted=0, anon_write_granted=0, auth_select_granted=0, auth_write_granted=0, api_policy_count=0, broad_api_true_count=0, custom_functions_executable_by_anon=0, custom_functions_executable_by_auth=0, anon_200_count=0, service probes 6/6 HTTP 200, cron run 2026-06-29_09-13-19 silent empty output, values_printed=false.
- Aprovação: Aprovação explícita de Lucas no Telegram: APROVO aplicar a correção do Supabase LK security gate agora.
- Envio/publicação: Sem envio externo/customer-facing. Telegram usado apenas para reportar execução e bloqueios.
- Writes externos: 1 write de segurança no Supabase produção LK via psql/Doppler: alteração de RLS e grants; secrets não impressos.
- Riscos/bloqueios: RLS nas tabelas backup sem políticas bloqueia acesso direto por anon/authenticated, esperado para backups; revoke da função lk_compras_next_seq para anon/authenticated pode bloquear uso client-side, mas função deve ser backend-only.
- Rollback/mitigação: Rollback possível mediante aprovação: ALTER TABLE ... DISABLE ROW LEVEL SECURITY nas duas tabelas backup e GRANT EXECUTE ON FUNCTION public.lk_compras_next_seq() TO public, anon, authenticated; não recomendado sem novo motivo de exposição controlado.
- Próximos passos: Manter daily gate silent-OK; investigar separadamente o cron LK Shopify Sales OS nightly full reconcile que segue em erro.
- Onde foi documentado no Brain: Receipt Memory OS criado via writer no Brain canônico; skill hermes-central-integration-auth-broker atualizada para Supabase pooler smoke.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
