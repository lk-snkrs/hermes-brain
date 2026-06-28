# Receipt — LK Supabase security gate auth resolved

- Data/hora: 2026-06-27T10:00:59Z
- Agente/profile/cron: lk-stock
- Empresa/área: LK/Stock/Supabase security
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas forneceu nova senha Postgres do Supabase LK e exigiu correção com Supabase MCP.
- Classificação: external-write
- Fontes usadas:
- Supabase MCP test/discovery; Doppler lc-keys/prd secret write; psql connectivity probes; cron wrapper execution; cronjob readback
- O que foi feito:
- Validado Supabase MCP configurado e conectado com 11 tools; testada nova senha sem imprimir valor; atualizado Doppler secret SUPABASE_LK_POSTGRES_PASSWORD; rerodado gate com psql e REST; cron forçado e readback mostrou last_status=ok.
- Output/artefato:
- Doppler set status ok; psql session_pooler_5432 ok e transaction_pooler_6543 ok; gate verbose status=pass, base_tables_total=123, base_tables_rls_off=0, anon_select_granted=0, anon_write_granted=0, auth_select_granted=0, auth_write_granted=0, api_policy_count=0, broad_api_true_count=0, custom_functions_executable_by_anon=0, custom_functions_executable_by_auth=0, oauth_tokens_nonempty_sensitive=0, anon_200_count=0, service_200_count=6; cron 21ee8507b7b7 last_status=ok; values_printed=false.
- Aprovação: Aprovação explícita de Lucas no Telegram: 'Usa essa senha por favor ... De qualquer maneira vc deve corrigir, deve usar o Mcp do supabase'. Escopo executado: atualizar apenas SUPABASE_LK_POSTGRES_PASSWORD no Doppler e verificar gate; nenhum SQL/schema/data write.
- Envio/publicação: Telegram final report only
- Writes externos: 1 Doppler secret update: SUPABASE_LK_POSTGRES_PASSWORD; DB writes 0; SQL writes 0; Shopify/Tiny writes 0.
- Riscos/bloqueios: A senha foi enviada em chat; recomendar rotação futura por canal seguro quando conveniente. Gate ficou OK com a senha atual.
- Rollback/mitigação: Se necessário, reverter SUPABASE_LK_POSTGRES_PASSWORD no Doppler para valor anterior conhecido/rotacionado e restaurar backups locais de /opt/data/profiles/lk-stock/backups/supabase-gate-fix-20260627T093802Z/.
- Próximos passos: Nenhum loop aberto para o gate; próxima execução diária deve ser silent-OK se postura continuar segura.
- Onde foi documentado no Brain: Receipt criado via Memory OS receipt writer; skill doppler-secrets-operations atualizada com nuance lk-stock Supabase; valores sensíveis impressos=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
