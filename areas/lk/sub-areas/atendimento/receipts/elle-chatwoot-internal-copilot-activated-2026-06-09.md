# Elle / Chatwoot — copiloto interno ativado

Data: 2026-06-09
Área: LK / Atendimento / Elle / Chatwoot
Modo: produção controlada, writes internos apenas

## Aprovação

Lucas respondeu “Aprovo” após o approval packet que solicitava ativar:

- nota privada;
- labels;
- assignment para `atendimento whatsapp`;
- sem resposta pública.

## Escopo executado

Ativada Elle como copiloto interno real no Chatwoot self-hosted `https://chat.lkskrs.online`.

Permitido pelo runtime:

- Criar nota privada com `private=true`.
- Aplicar labels operacionais.
- Atribuir ao time `atendimento whatsapp` quando a classificação exigir handoff.

Continuam proibidos por escopo:

- Mensagem pública ao cliente.
- WhatsApp send.
- Promessa de estoque/preço/prazo/reserva/desconto.
- Alterações em Shopify, Tiny, produtos, pedidos, estoque, preço, tema, campanhas, inbox, webhook ou automação pública.

## Backup / rollback

Backup criado no VPS antes da alteração:

- Diretório: `/opt/elle-chatwoot/backups/activation-20260609T133859Z`
- Arquivo: `.env.pre-activation`
- Permissão: `600`

Flags pré-ativação:

- `ELLE_DRY_RUN=true`
- `CHATWOOT_WRITE_ENABLED=false`
- `ELLE_KILL_SWITCH=true`
- `CHATWOOT_TEAM_ID=2`

Rollback operacional:

1. Restaurar flags no Doppler e no `/opt/elle-chatwoot/.env`:
   - `ELLE_DRY_RUN=true`
   - `CHATWOOT_WRITE_ENABLED=false`
   - `ELLE_KILL_SWITCH=true`
2. Recriar/reiniciar somente o container `elle-chatwoot`.
3. Verificar `https://elle.lkskrs.online/healthz`.

## Alterações feitas

Doppler `lc-keys/prd` atualizado:

- `ELLE_DRY_RUN=false`
- `CHATWOOT_WRITE_ENABLED=true`
- `ELLE_KILL_SWITCH=false`

VPS `/opt/elle-chatwoot/.env` atualizado com os mesmos flags.

Container recriado:

- `elle-chatwoot`
- imagem observada: `elle-chatwoot-elle-chatwoot`

## Verificação pós-ativação

Health Elle:

- HTTP `200`
- `dry_run=False`
- `write_enabled=True`
- `kill_switch=False`

Health Chatwoot:

- HTTP `200`
- `queue_services=ok`
- `data_services=ok`

Container:

- `elle-chatwoot`: `Up`

Código/adapter:

- Método de resposta pública no adapter local: `0` encontrado.
- Código remoto `app.py` inspecionado: ações permitidas são private note, labels e assignment; private note usa `private: True`.

## Smoke pós-ativação

Foi enviado um evento sintético ao receiver Elle com conversa inexistente `990001` para evitar tocar cliente real.

Resposta Elle:

- HTTP `200`
- `status=processed`
- `dry_run=false`
- `write_enabled=true`
- `kill_switch=false`
- labels: `pedido`, `whatsapp-api`
- handoff: `false`

Log Elle:

- Entrada do smoke encontrada: `1`
- `status=processed`
- `dry_run=False`
- `write_enabled=True`
- `kill_switch=False`
- `action_status.error=HTTPError`

Interpretação: erro esperado porque a conversa sintética não existe. Isso evitou write em conversa real.

Probe Chatwoot read-only:

- Conversa sintética `990001`: HTTP `404`
- `synthetic_conversation_exists=False`

## O que não foi feito

- Nenhuma mensagem pública enviada.
- Nenhum WhatsApp enviado.
- Nenhuma conversa real criada.
- Nenhuma nota/label/assignment aplicado em cliente real durante o smoke.
- Nenhum webhook/inbox alterado.
- Nenhuma alteração em Chatwoot Rails/Sidekiq, Postgres, Redis, Traefik ou outros containers.
- Nenhuma alteração em Shopify/Tiny/estoque/preço/pedido.

## Status final

Elle está **ativa como copiloto interno**.

Próxima mensagem real `message_created` inbound no Chatwoot deve acionar:

- nota privada;
- labels;
- assignment se houver risco/handoff.

Sem resposta pública automática.

`values_printed=false`.
