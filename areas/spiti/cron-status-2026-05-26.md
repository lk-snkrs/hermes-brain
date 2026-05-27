# SPITI — Status de crons próprios

Data: 2026-05-26  
Status: registro documental local/read-only.

## Estado observado

Na auditoria de governança/organograma, não foi encontrado registry local em:

- `/opt/data/profiles/spiti/cron/jobs.json`

Isso **não é automaticamente erro**. Pode significar que SPITI tem runtime/bot ativo para atendimento sob demanda, mas ainda não possui scheduler local próprio.

## Interpretação operacional

Até decisão contrária:

- SPITI pode operar como especialista sob demanda;
- crons SPITI não devem ser inventados por simetria com LK/Amora;
- qualquer cron novo precisa ter dono, cadência, critério de silêncio, destino, rollback e aprovação explícita.

## Possíveis rituais futuros

Somente se houver volume real:

- revisão semanal de Hub/obras/lotes;
- watchdog read-only de dados críticos;
- relatório de risco/pendências SPITI;
- digest local silencioso com alerta apenas em exceção.

## Guardrail

Silêncio é melhor que dado errado. Lance/lote/cliente/bidder/financeiro/deploy/banco exigem fonte verificável e aprovação quando houver write ou contato externo.
