# LK Content Klaviyo smoke corrigido — 2026-06-07

## Timestamp

- BRT: 2026-06-07T13:27:13-03:00
- Execução do smoke corrigido: 2026-06-07T16:28:23Z

## Escopo

Lucas escolheu seguir com o ajuste do smoke Klaviyo para corrigir os endpoints que haviam falhado parcialmente.

## Arquivos atualizados

- `/opt/data/profiles/lk-content/scripts/klaviyo_readonly_smoke.py`
- `/opt/data/profiles/lk-content/integrations/klaviyo.md`
- Skill `specialist-profile-activation` atualizada com gotcha Klaviyo de campaigns/metrics.

## Correções aplicadas

- Campaigns: adicionado filtro obrigatório de canal `equals(messages.channel,'email')`.
- Metrics: removido `page[size]`, pois o endpoint havia rejeitado esse parâmetro no account/revision ativo.

## Resultado real do smoke read-only

- Status geral: `ok`
- Credencial Klaviyo: disponível no runtime do perfil.
- Base URL: `https://a.klaviyo.com/api`
- Revision: `2026-04-15`

Endpoints lidos com HTTP 200:

- Campaigns: 5 retornadas
- Lists: 5 retornadas
- Segments: 5 retornados
- Flows: 5 retornados
- Metrics: 135 retornadas

## Segurança

- `writes_performed`: 0
- `send_schedule_flow_activation_performed`: false
- Nenhum envio realizado.
- Nenhum agendamento realizado.
- Nenhuma ativação de flow realizada.
- Nenhum template, campanha, segmento, lista ou asset criado/editado/deletado.
- Nenhum token/header/secret foi registrado neste receipt.

## Próximo gate

Klaviyo está pronto para operações read-only e pesquisa de CRM. Qualquer draft/template/campaign write exige aprovação explícita atual. Envio/agendamento/ativação de flow exige dupla confirmação sequencial via Telegram.
