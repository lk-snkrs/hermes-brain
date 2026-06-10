# Runbook — Operação do lk-chatwoot

## Acesso
- VPS: `ssh root@72.60.150.124` (senha com Lucas — ele cola; NUNCA digitar/registrar credenciais).
- Containers: `chatwoot-rails-1`, `chatwoot-sidekiq-1`, `chatwoot-postgres-1` (db `chatwoot_production`, user postgres), `chatwoot-redis-1`. Compose: `/opt/chatwoot/docker-compose.yaml` (backups em `/opt/data/backups/`).
- Fonte: `/opt/data/lk-chatwoot-v2` (git local — commitar toda mudança).

## Build & deploy (mudança de Vue ou migração)
```
cd /opt/data/lk-chatwoot-v2
docker build -f docker/Dockerfile -t lk-chatwoot:vN .   # ~6 min (recompila Vue)
cp /opt/chatwoot/docker-compose.yaml /opt/data/backups/docker-compose.yaml.$(date +%Y%m%d-%H%M%S)
sed -i 's|lk-chatwoot:vANTIGA|lk-chatwoot:vN|g' /opt/chatwoot/docker-compose.yaml
cd /opt/chatwoot && docker compose up -d
docker exec chatwoot-rails-1 bundle exec rails db:migrate   # se houver migração
```
Rollback = sed de volta pra imagem anterior + `up -d`.

## Hot-patch (só Ruby/backend, sem rebuild)
```
docker cp ARQ chatwoot-rails-1:/app/ARQ
docker cp ARQ chatwoot-sidekiq-1:/app/ARQ    # OBRIGATÓRIO: jobs rodam no sidekiq!
docker restart chatwoot-rails-1 chatwoot-sidekiq-1
```
Validar sintaxe antes: `docker cp ARQ chatwoot-rails-1:/tmp/chk.rb && docker exec chatwoot-rails-1 ruby -c /tmp/chk.rb`.

## Diagnóstico rápido
```
# settings da conta
docker exec chatwoot-postgres-1 psql -U postgres -d chatwoot_production -t -A -c "SELECT jsonb_pretty(recovery_settings) FROM accounts WHERE id=1;"
# envios recentes / erros
docker logs chatwoot-sidekiq-1 --since 1h 2>&1 | grep -E 'EvolutionSender|Recovery|AbandonedCheckout'
# mensagens falhadas inbox 3
... -c "SELECT status, count(*) FROM messages WHERE inbox_id=3 AND message_type=1 AND created_at > now()-interval '1 hour' GROUP BY 1;"
# instâncias Evolution (apikey está em recovery_settings)
curl -s -H "apikey: $KEY" https://evolution-api-production-fa87.up.railway.app/instance/fetchInstances
```

## Ligar os fluxos (quando Lucas autorizar)
```
UPDATE accounts SET recovery_settings = recovery_settings || jsonb_build_object(
  'SHOPIFY_RECOVERY_ENABLED','true',
  'SHOPIFY_RECOVERY_DELAYS','60,1440,2880',
  'SHOPIFY_NOTIFY_ENABLED','true',
  'SHOPIFY_FOLLOWUP_DELAY_MINUTES','4320'
) WHERE id=1;
```
(sem restart — settings são lidas a cada job)

## Gotchas
- **Screenshot trava na tela do Chatwoot** (websockets) → ler DOM via JS/get_page_text.
- **1Password trava digitação** em campos do browser → navegar com Tab.
- **PWA cacheia** → hard-refresh/incognito pra ver UI nova.
- Jobs agendados (delays) EXECUTAM mesmo se a flag for desligada depois — o job re-checa `enabled?`? NÃO para toques já agendados; flag off impede novos agendamentos. Toque agendado re-checa recovered/compra, mas não a flag.
- Webhook Shopify responde 200 SEMPRE (erro = evento perdido, sem retry).
- Build em background: `nohup docker build ... > /tmp/build.log 2>&1 &` e acompanhar o log (sessões de shell têm timeout).
- Templates: identificador (sem espaço) que não existir na biblioteca NÃO é enviado (guard pós-incidente). Texto com espaços é enviado literal (com interpolação).
