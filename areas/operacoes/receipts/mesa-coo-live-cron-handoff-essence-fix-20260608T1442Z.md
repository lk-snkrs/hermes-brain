# Receipt — Mesa COO live cron handoff essence fix

Data UTC: 2026-06-08T14:42Z

## Pedido/correção

Lucas perguntou se a correção havia sido feita “na essência do MESA”. A verificação mostrou que o handoff e a skill `mesa` já tinham sido corrigidos, mas o prompt vivo do cron `Mesa COO diária Telegram` ainda não continha explicitamente a regra essencial de handoff para agentes/especialistas.

## Ação executada

Atualizado somente o prompt do cron vivo:

- Job ID: `749ee30b51eb`
- Nome: `Mesa COO diária Telegram`
- Schedule preservado: `0 9 * * *`
- Deliver preservado: `origin`
- Skills preservadas: `mesa`, `lucas-chief-of-staff`, `multiempresa-routing-lucas`
- Workdir preservado: `/opt/data/hermes_bruno_ingest/hermes-brain`
- Toolsets preservados: `terminal`, `file`, `cronjob`, `skills`, `session_search`

## Regra adicionada ao prompt vivo

- Quando uma decisão da Mesa for executada e gerar estado operacional reutilizável — approval packet, receipt, validação pública, bloqueio, próximo gate, rollback/snapshot ou decisão pendente — a Mesa só está fechada depois de registrar um handoff curto no Brain para os agentes/especialistas afetados.
- O handoff deve dizer destinatários, artefatos, writes executados, aprovações pendentes, bloqueios, próximos gates e onde ficou documentado.
- Não depender apenas do relatório consolidado diário; reconciliar sessão recente, receipts e handoffs antes de apresentar próxima decisão.
- Não incluir nem priorizar IMBOX/Inbox em rotinas/decisões de COO, salvo pedido explícito de Lucas.

## Verificação

Readback local de `/opt/data/cron/jobs.json` confirmou:

- `has_handoff_essential_rule=true`
- `has_mesa_closed_after_handoff=true`
- `has_imbox_filter=true`

## Limites

- Nenhuma agenda foi alterada.
- Nenhum destino de entrega foi alterado.
- Nenhum write externo foi executado.
- Nenhum secret foi impresso ou registrado.
