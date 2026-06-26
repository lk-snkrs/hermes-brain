# Receipt — LK Recovery Klaviyo webhook read-only investigation — 2026-06-21

- Data/hora: 2026-06-21T13:14:48.553069+00:00
- Agente/profile/cron: Hermes default / Mesa COO
- Empresa/área: LK / Atendimento / Recovery / Klaviyo
- Responsável humano: LK Ops/Growth + Hermes Operações
- Pedido original: Lucas aprovou Fazer para investigar por que 0 conversa Klaviyo/webhook foi criada em 24h apesar de checkouts recentes, em modo read-only/local.
- Classificação: read-only
- Fontes usadas:
- Daily consolidation 2026-06-20 linhas 70 e 106; receipt recovery-klaviyo-dedup-prod-final-20260620; skill lk-chatwoot-klaviyo-webhook-recovery-diagnostic; monitor read-only recovery-monitor-20260621T131255Z; logs read-only Rails/Sidekiq 24h; Klaviyo API GET flow-action 109063868 via Doppler-first; Chatwoot token lido apenas em memória para comparação booleana.
- O que foi feito:
- Executado monitor Recovery 7d read-only; confirmado Shopify Recovery ativo e criando conversas; confirmado Klaviyo/webhook com 0 conversas em 24h; confirmado endpoint recebendo chamadas Klaviyo nos logs; confirmado 401 Unauthorized 24h; confirmado KlaviyoCartJob 0; confirmado flow action Yp9RY5/action 109063868 live WEBHOOK por GET; comparado header X-Chatwoot-Token contra token esperado por igualdade booleana sem imprimir valores: header presente, mismatch detectado.
- Output/artefato:
- Resultado sanitizado: checkouts recentes 44, recovered recentes 10, origem criada 24h Shopify 3 e Klaviyo/webhook 0, último Klaviyo/webhook 12/06 16:38 BRT, Rails logs 24h post_klaviyo=8 controller=8 unauthorized_401=8 KlaviyoCartJob=0 duplicate_skip=0 duplicate_guard_failed=0, Klaviyo GET action HTTP 200 status live/action_type WEBHOOK, x_chatwoot_token_header_present=true, header_matches_chatwoot_token=false, header_mismatch_detected=true, values_printed=false.
- Aprovação: Aprovado por Lucas: Fazer. Escopo limitado a read-only/local; não autoriza Klaviyo/Shopify/Chatwoot writes, envio, flow/campaign activation, webhook mutation, runtime restart, Docker/VPS/Traefik/gateway mutation.
- Envio/publicação: Nenhum envio externo; Telegram apenas resumo final para Lucas.
- Writes externos: 0
- Riscos/bloqueios: Klaviyo webhook está recebendo eventos mas falhando autenticação; enquanto o header divergir, carrinhos Klaviyo não viram conversas. Guard anti-duplicação Shopify já está ativo, então corrigir autenticação é o próximo passo, mas é write externo/sensível e precisa approval packet separado.
- Rollback/mitigação: Não aplicável a sistemas externos: nenhuma alteração externa feita. Artefatos locais podem ser removidos se necessário.
- Próximos passos: Preparar approval packet separado para corrigir o header X-Chatwoot-Token da action Klaviyo 109063868 via UI Klaviyo ou endpoint alternativo validado; depois monitorar queda de 401, enfileiramento KlaviyoCartJob, conversas Klaviyo e skips por duplicidade Shopify.
- Onde foi documentado no Brain: Receipt criado em areas/lk/sub-areas/atendimento/receipts/recovery-klaviyo-readonly-investigation-20260621.md; monitor criado em areas/lk/sub-areas/atendimento/monitoring/recovery-7d/recovery-monitor-20260621T131255Z.md; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
