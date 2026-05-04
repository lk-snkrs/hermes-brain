# Integração — Telegram

## Escopo

Telegram é a interface operacional principal de Lucas com Hermes e canal de entrega de relatórios/cronjobs.

## Secrets Doppler

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_ALLOWED_USERS` quando aplicável

## Read-only

- Conferir configuração, gateway, logs e destino de entrega sem expor tokens.
- Listar cronjobs Hermes e destinos conhecidos.

## Write

- Criar mensagens/respostas no chat atual conforme pedido de Lucas.
- Agendar cronjobs informativos quando aprovados ou claramente internos ao fluxo.

## External-send

- Enviar mensagens para canais/grupos/pessoas fora do chat atual exige cuidado; se o destino for específico, listar targets antes.
- Mensagens comerciais para clientes não devem usar Telegram sem aprovação explícita.

## Admin/destructive

- Trocar bot token, allowed users, gateway, containers ou integrações exige aprovação e rollback.

## Escala de permissões

- Read-only: consultar metadados, status, listas, métricas e registros sem alterar dados.
- Write: criar/atualizar dados internos, tags, notas, segmentos ou configurações não destrutivas.
- External-send: enviar mensagem, email, campanha, notificação ou contato com cliente/lead/parceiro. Exige preview e aprovação de Lucas.
- Admin/destructive: apagar dados, alterar credenciais, webhooks, domínios, billing, permissões, deploys, containers, produção ou integrações críticas. Exige aprovação explícita, plano de backup e rollback.

Regra de secrets: este arquivo lista apenas nomes de secrets no Doppler `lc-keys/prd`; valores reais nunca entram no GitHub.
