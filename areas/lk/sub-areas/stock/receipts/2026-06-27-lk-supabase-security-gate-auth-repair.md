# Receipt — LK Supabase security gate auth repair

- Data/hora: 2026-06-27T09:41:18Z
- Agente/profile/cron: lk-stock
- Empresa/área: LK/Stock/Supabase security
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas respondeu Corrigir ao alerta do cron LK Supabase public exposure security gate daily
- Classificação: local-write
- Fontes usadas:
- cronjob list + hermes cron list --all + execução manual do wrapper + Doppler lc-keys/prd presence checks
- O que foi feito:
- Identificado que o erro real era autenticação psql com SUPABASE_LK_POSTGRES_PASSWORD, não falha de LLM/provider; ajustado hermes_doppler PROFILE_SECRET_MAP de lk-stock para incluir secrets Supabase LK; ajustado wrapper do cron para usar hermes_doppler.py run --profile lk-stock; ajustado gate para emitir diagnóstico acionável db_auth_error com probe REST parcial sanitizado.
- Output/artefato:
- py_compile OK; lk-stock Doppler profile expected_count=11 present_count=11 missing_count=0; wrapper executa com values_printed=false e agora retorna lk_supabase_security_gate_db_auth_error com anon_200_count=0, service_200_count=6; gate completo ainda bloqueado porque senha Postgres no Doppler falha no pooler.
- Aprovação: Lucas pediu corrigir; nenhuma ação externa/prod/secret rotation executada.
- Envio/publicação: Telegram final report only
- Writes externos: 0
- Riscos/bloqueios: Gate completo continua fail até atualizar/rotacionar SUPABASE_LK_POSTGRES_PASSWORD; REST parcial não substitui auditoria de grants/RLS via psql.
- Rollback/mitigação: Restaurar backups em /opt/data/profiles/lk-stock/backups/supabase-gate-fix-20260627T093802Z/ e reverter diff do Brain se necessário.
- Próximos passos: Atualizar SUPABASE_LK_POSTGRES_PASSWORD em Doppler lc-keys/prd com a senha atual do banco LK ou aprovar rotação/reset no Supabase Dashboard; rerodar python3 /opt/data/profiles/lk-stock/scripts/lk_supabase_security_gate_daily.py até rc=0/silent-OK.
- Onde foi documentado no Brain: Receipt criado via Memory OS receipt writer; valores sensíveis impressos=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
