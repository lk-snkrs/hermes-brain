# Mission Control — ponte de reconciliação

Data: 2026-05-19  
Escopo desta rodada: apenas ponte documental.  
Fora de escopo: auditoria detalhada de repositório/UI/runtime Mission Control, Docker/VPS, deploy, workers, crons ou integrações.

## Por que este arquivo existe

A auditoria BRUNO-ATUAL marcou Mission Control como P0 para reconciliação, mas a tarefa atual separou o trabalho detalhado para outro agente. Este ponteiro evita perder o vínculo com os novos documentos P0 seguros.

## Insumos criados nesta rodada

- `memories/current.md` — camada quente/current para boot e prioridades.
- `areas/operacoes/rotinas/runtime-profile-channel-inventory-2026-05-19.md` — matriz de profiles, bots, canais, cadência, status e kill criteria.
- `empresa/skills/skill-audit-2026-05-19.md` — matriz de skills canônicas.
- `agentes/mordomo/` — documentação inicial do agente/profile Mordomo.

## Requisitos para a reconciliação futura

Um documento único de Mission Control deve dizer:

- o que está ativo em produção;
- o que é histórico/legado;
- o que é benchmark Bruno/OpenClaw/TenacitOS;
- quais módulos são próximos;
- quais invariantes de segurança não podem ser quebradas;
- quais dados vêm do Brain e quais exigem fonte viva;
- quais ações exigem aprovação antes de runtime/write/envio externo.

## Guardrails

- Não assumir que relatório, PRD ou mock significa runtime ativo.
- Não acionar Docker/VPS/root/SSH/Traefik/volumes/networks sem aprovação explícita.
- Não criar cron, worker, webhook, canal ou envio externo por causa deste documento.
- Não copiar material bruto de terceiros para o Brain.
