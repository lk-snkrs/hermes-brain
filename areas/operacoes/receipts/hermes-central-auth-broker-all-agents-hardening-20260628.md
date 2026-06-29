# Receipt — Hermes Central Auth Broker — all-agent hardening after LK Stock false Shopify failure

- Data/hora: 2026-06-28T18:12:33.006365+00:00
- Agente/profile/cron: Hermes default / integration auth broker control-plane
- Empresa/área: Operações Hermes / Governança de integrações
- Responsável humano: Hermes Agent
- Pedido original: Lucas pediu “arrume em todos os agentes” após LK Stock gerar status falso de OAuth Shopify pendente apesar do broker.
- Classificação: local-write
- Fontes usadas:
- Mensagem Lucas; hermes_cli_run.py; hermes_cli_integrations.py; profile AGENTS/SOUL/skills; live smoke/audit; watchdog roster.
- O que foi feito:
- Endureci o broker: hermes-cli-run força HOME/XDG central; smoke_shopify agora usa hermes-cli-run e method broker_shopify_store_execute; adicionei gate anti-falso-failure/reauth em skill, AGENTS e SOUL; recopiada skill para 16 profiles; recarregados managed gateways; adicionei notas superseded em artefatos históricos que diziam auth Shopify pendente.
- Output/artefato:
- 16/16 profiles com skill/gate; 13/13 gateways esperados vivos; smoke shopify_lk/supabase/google/klaviyo OK; teste com HOME/XDG falsos em LK Stock retorna Shopify audit exit_code=0/status=ok; active approval packet stale removido; secret scan 0.
- Aprovação: Correção local/procedural solicitada diretamente por Lucas; sem writes externos, sem alteração de secrets, sem Docker/VPS/Traefik.
- Envio/publicação: Telegram: resumo final nesta conversa.
- Writes externos: 0
- Riscos/bloqueios: Histórico antigo em logs/sessions pode continuar citando falhas passadas; artefatos markdown principais receberam nota superseded. Se algum agente citar logs históricos, deve usar a regra atual do broker e smoke fresco.
- Rollback/mitigação: Backups em central-auth-broker-hardening-all-agents-20260628T180548Z, central-auth-broker-force-xdg-20260628T180833Z, central-auth-broker-false-failure-rule-agents-soul-20260628T180623Z e shopify-auth-stale-status-supersede-notes-20260628T181139Z.
- Próximos passos: Nenhum obrigatório; LK Stock pode seguir readback webhookSubscriptions pelo broker se necessário.
- Onde foi documentado no Brain: Receipt atual; skill hermes-central-integration-auth-broker; superseded notes em artefatos históricos.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
