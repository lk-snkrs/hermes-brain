# LK Content Klaviyo operational map — receipt — 2026-06-07

## Timestamp

- BRT: 2026-06-07T13:53:41-03:00
- Auditoria executada: 2026-06-07T16:57:23Z

## Escopo executado

Lucas pediu para seguir após o smoke Klaviyo read-only corrigido. Foi criada e executada uma auditoria read-only sanitizada para mapear campanhas, listas, segmentos, flows e métricas do Klaviyo para operação do LK Content.

## Arquivos criados/atualizados

- `/opt/data/profiles/lk-content/scripts/klaviyo_readonly_audit.py`
- `/opt/data/profiles/lk-content/performance/klaviyo-operational-map-20260607.md`

## Resultado real

Status: `ok`
Revision: `2026-04-15`

Endpoints read-only:

- Campaigns email: HTTP 200, 20 retornadas
- Lists: HTTP 200, 10 retornadas
- Segments: HTTP 200, 10 retornados
- Flows: HTTP 200, 20 retornados
- Metrics: HTTP 200, 135 retornadas

Mapa operacional identificado:

- Newsletter candidata: `LK News` (`S3VM4Y`)
- Teste newsletter: `LK Newsletter Test` (`Sjzi3r`)
- VIP/high-ticket: `LK VIP (>R$5k)`, `CK - Clientes High Ticket (10k)`, `CK - Clientes High Ticket (5k)`, `LK | Alto Valor (VIP)`
- Reativação: `LK Reativacao 60d+`, `LK Winback — Cant Lose`, `LK | Perdidos`, `Desengajados - 3 meses`, flows Win-back
- Abandono/intenção: flows Checkout Abandonment, Abandoned Cart, Abandono de coleção, Wishlist
- Welcome/onboarding: Welcome Series e Agradecimento ao cliente

## Segurança

- `writes_performed`: 0
- `external_write_performed`: false
- `send_schedule_flow_activation_performed`: false
- `pii_returned`: false
- Nenhum envio, agendamento, criação de campanha/template, alteração de segmento/lista/flow ou deleção foi executado.
- Nenhum token/header/secret foi registrado.

## Próximo gate

Próximo passo seguro: montar pacote editorial de calendário/newsletter usando esse mapa + playbook LK. Qualquer draft Klaviyo é write externo e exige aprovação explícita atual. Envio/agendamento/flow activation exige dupla confirmação sequencial no Telegram.
