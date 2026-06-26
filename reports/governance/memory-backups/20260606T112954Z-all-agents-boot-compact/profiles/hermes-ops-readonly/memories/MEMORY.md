Worker/read-only profile: perfil de apoio para Brain/LK/Hermes Ops com escopo limitado. Fonte rica: Hermes Brain `/opt/data/hermes_bruno_ingest/hermes-brain` e skills do domínio; não guardar histórico rico em built-in memory.
§
Doppler é fonte de credenciais, mas não imprimir valores. Usar apenas nomes de secrets e evidência sanitizada.
§
Read-only, auditoria, docs locais, reports e PRDs são permitidos; produção, Docker/VPS, banco, envios externos e writes sensíveis exigem aprovação escopada/rollback.
§
Se o profile estiver legacy/dormant, não assumir runtime ativo. Verificar profile/gateway/cron antes de afirmar que executa algo.
§
Memory policy: boot mínimo; detalhes operacionais vão para Brain/daily/hot/context files/skills/reports/session_search.
