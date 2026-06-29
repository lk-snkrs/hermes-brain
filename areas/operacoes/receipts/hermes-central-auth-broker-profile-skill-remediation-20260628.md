# Receipt — Hermes Central Auth Broker — profile skill/SOUL remediation after LK Stock stale reply

- Data/hora: 2026-06-28T18:01:48.018519+00:00
- Agente/profile/cron: Hermes default / operações runtime
- Empresa/área: Operações Hermes / Governança de integrações
- Responsável humano: Hermes Agent
- Pedido original: Lucas mostrou que LK Stock ainda sugeriu pendência OAuth Shopify/readback webhooks, indicando que não tinha absorvido o Central Integration Auth Broker.
- Classificação: local-write
- Fontes usadas:
- Mensagem Lucas; busca em /opt/data/profiles/lk-stock; AGENTS/SOUL/skills locais; watchdog reload; broker smoke.
- O que foi feito:
- Copiei a skill hermes-central-integration-auth-broker para skills/devops de 16 profiles; corrigi linhas stale 2026-06-11 em AGENTS/SOUL; adicionei regra viva nos SOUL de todos os profiles; reloaded 12 gateways managed.
- Output/artefato:
- 16/16 profiles com skill local; 16/16 SOUL com regra viva; AGENTS verificados com bloco obrigatório; LK Stock recarregado; managed roster 12/12 OK; broker smoke shopify/supabase/google/klaviyo OK.
- Aprovação: Correção local/procedural decorrente de falha apontada por Lucas; sem writes externos, sem Docker/VPS/Traefik e sem alteração de secrets.
- Envio/publicação: Telegram: resumo final nesta conversa.
- Writes externos: 0
- Riscos/bloqueios: Interrupção breve dos especialistas durante reload; nenhum secret alterado.
- Rollback/mitigação: Backups em /opt/data/backups/central-auth-broker-profile-skill-propagation-20260628T175653Z, central-auth-broker-stale-validation-line-fix-20260628T175736Z, central-auth-broker-soul-rule-all-profiles-20260628T180020Z.
- Próximos passos: Se algum bot ainda responder com contexto antigo, tratar como sessão antiga/compaction residual e reiniciar só o profile afetado; opcional auditar prompts de cron/sessions históricas sem reescrever histórico.
- Onde foi documentado no Brain: Receipt atual; skill hermes-central-integration-auth-broker em cada profile.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
