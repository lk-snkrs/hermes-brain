# Receipt — LK Supabase security hardening 1-5 pós-contenção

- Data/hora: 2026-06-16T19:16:03.613334+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Supabase / Security
- Responsável humano: Hermes lk-stock
- Pedido original: Executar próximos passos 1-5 pós-contenção Supabase LK: policies mínimas, views/RPC sanitizadas, rotação/invalidação de tokens, revisão de logs e gate diário.
- Classificação: infra-sensitive
- Fontes usadas:
- PostgreSQL Supabase LK via Doppler/psql; REST Supabase anon/service probes; cron registry Hermes; sem impressão de secrets/PII.
- O que foi feito:
- Removidas policies public/anon/authenticated restantes; revogado EXECUTE de RPCs customizadas para anon/authenticated; oauth_tokens verificado vazio; logs inventariados por contagem/range; gate diário silent-OK criado e testado.
- Output/artefato:
- Report areas/lk/sub-areas/stock/reports/lk-supabase-security-hardening-20260616.md; gate areas/lk/sub-areas/stock/scripts/lk_supabase_security_gate.py; cron 21ee8507b7b7; verificação gate pass/failures=0.
- Aprovação: Lucas aprovou executar os próximos passos 1-5. Rotação de chaves Supabase ficou bloqueada por Management API 403 e exige dashboard/token Management válido.
- Envio/publicação: Telegram final; cron silent-OK origin apenas em falha.
- Writes externos: Supabase grants/policies/function privileges alterados; cron Hermes criado; nenhum dado de tabela alterado; nenhum token impresso.
- Riscos/bloqueios: Possível quebra de frontend/automação que dependia de anon/authenticated direto; service_role validado 200. Rotação de keys ainda pendente se houver suspeita de vazamento fora da DB.
- Rollback/mitigação: Recriar grants/policies/RPCs mínimos a partir de migrations/necessidade explícita; pausar/remover cron 21ee8507b7b7 se gerar falso positivo.
- Próximos passos: Se Lucas quiser rotação total, abrir dashboard Supabase ou fornecer Management token válido; depois atualizar Doppler e rerodar gate.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/reports/lk-supabase-security-hardening-20260616.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
