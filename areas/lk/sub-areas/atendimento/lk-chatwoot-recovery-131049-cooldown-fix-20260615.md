# LK Chatwoot Recovery — 131049 cooldown/cadência production fix 2026-06-15

> **Documento histórico / DO NOT RUN:** comandos e caminhos citados são evidência/registro; não executar sem aprovação escopada, backup, rollback e readback.


## Contexto

Lucas pediu seguir ações 1–5 após pesquisa do erro Meta WhatsApp `131049` em carrinho abandonado.

Pesquisa oficial Meta: `131049` = mensagem não entregue para manter engajamento saudável; quando ligado a limite de template marketing por usuário, aguardar pelo menos 24h antes de reenviar. Retry imediato tende a falhar novamente.

## Mudanças aplicadas

Ambiente: Chatwoot LK produção.

Imagem final em Rails/Sidekiq: `lk-chatwoot:v2-recovery23-131049-cooldown-fix-20260615`.

Arquivos alterados na fonte `/opt/data/lk-chatwoot-v2`:

- `app/jobs/shopify/abandoned_checkout_job.rb`
  - Antes de claimar/enviar toque 2+:
    - bloqueia novo toque se houver falha Meta `131049` recente para o checkout/conversa.
    - bloqueia follow-up se a última mensagem pública de recovery falhou.
    - permite seguir se último status foi `delivered` ou `read`.
  - Usa `messages.content_attributes ->> 'external_error'`, porque `external_error` não é coluna física em `messages`.
- `app/services/recovery/settings_resolver.rb`
  - Adicionada setting `SHOPIFY_RECOVERY_131049_COOLDOWN_HOURS`.
- `app/services/shopify/checkout_tracking_service.rb`
  - Default fallback de delays reduzido de `[60, 1440, 2880]` para `[60, 2880]`.

Config live `Account(1).recovery_settings` atualizada:

- `SHOPIFY_RECOVERY_DELAYS`: de `60,1440,4320` para `60,2880`.
- `SHOPIFY_RECOVERY_131049_COOLDOWN_HOURS`: `24`.

## Backup / rollback

Backup antes da mudança:

- `/root/chatwoot-rollbacks/recovery-131049-cooldown-20260615T102140Z/`

Rollback:

1. Restaurar image tag anterior no `/opt/chatwoot/docker-compose.yaml`:
   - `lk-chatwoot:v2-recovery21-template-param-coercion-20260614`
2. Rodar em `/opt/chatwoot`:
   - `docker compose up -d rails sidekiq`
3. Se necessário, restaurar arquivos fonte do backup.
4. Restaurar settings antigas se quiser voltar cadência:
   - `SHOPIFY_RECOVERY_DELAYS=60,1440,4320`
   - remover/ignorar `SHOPIFY_RECOVERY_131049_COOLDOWN_HOURS`.

## Verificação executada

- Syntax Ruby via Docker: OK para arquivos alterados.
- Build Docker: OK.
- Compose recreate: Rails e Sidekiq iniciaram na imagem nova.
- Health local HTTP: OK após boot.
- Readback imagem Rails/Sidekiq: `lk-chatwoot:v2-recovery23-131049-cooldown-fix-20260615`.
- Readback settings via Rails runner:
  - delays `[60, 2880]`.
  - cooldown `24`.
- Smoke Rails runner de método de cooldown: executou sem erro e sem imprimir PII.
- Logs recentes Rails/Sidekiq: 0 ocorrências de `131049 cooldown check failed`, `prior delivery check failed`, `NoMethodError`, `PG::UndefinedColumn`.

## Observações

- Nenhum retry/reenvio manual foi feito.
- Nenhuma PII, checkout URL ou token foi impresso.
- A mudança reduz pressão futura; não transforma mensagens já falhadas em entregues.
- Próximo monitoramento deve comparar `failed 131049` antes/depois por template e status (`delivered`/`read`/`failed`).
