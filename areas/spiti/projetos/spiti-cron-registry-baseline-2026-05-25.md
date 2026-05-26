# SPITI — baseline de cron registry

Status: baseline documental  
Owner: SPITI OS  
Supervisor: Hermes Geral / COO  
Data: 2026-05-25  
Writes externos/runtime: não

## Decisão atual

SPITI não possui registry local de crons em:

`/opt/data/profiles/spiti/cron/jobs.json`

Este estado é considerado intencional/aceitável por enquanto: SPITI pode ter profile/gateway observado e documentação operacional, mas não há crons locais registrados no scheduler do profile SPITI.

## O que existe hoje

- Agente/documentação SPITI em `agentes/spiti/`.
- Área SPITI em `areas/spiti/`.
- Watchdog central no Main para observar o gateway SPITI.
- Rotas e guardrails SPITI documentados para Hub, CRM, obras, lotes, leilões, Financial/Growth e IA interna.

## O que não existe hoje

- Registry runtime local de crons SPITI.
- Scheduler próprio com jobs SPITI locais.
- Crons SPITI migrados para `/opt/data/profiles/spiti/cron/jobs.json`.

## Como interpretar em auditorias

Quando uma auditoria procurar `/opt/data/profiles/spiti/cron/jobs.json` e não encontrar:

- Não tratar automaticamente como falha.
- Registrar como “SPITI sem crons locais”.
- Confirmar se existe decisão posterior mudando esse baseline antes de criar arquivo ou migrar jobs.

## Quando criar registry SPITI no futuro

Só criar registry/runtime se houver aprovação explícita e um destes motivos:

- Rotina SPITI recorrente com dono claro.
- Necessidade de separar crons SPITI do Main/COO.
- Canal/bot SPITI com entregas próprias.
- Risco de misturar SPITI com Zipper/LK/Mordomo.
- Necessidade de auditoria operacional mais granular.

## Antes de criar registry/runtime

Preparar pacote com:

1. Jobs exatos a criar/migrar.
2. Backups de registries afetados.
3. Plano de rollback.
4. Script/path compatibility.
5. Contrato de entrega: local/silent-OK por padrão; Telegram apenas decisão/exceção/falha.
6. Verificação sem secrets.
7. Handoff para Hermes Central.

## Bloqueios

Sem aprovação explícita, não:

- Criar `/opt/data/profiles/spiti/cron/jobs.json`.
- Mover jobs para SPITI.
- Criar cron SPITI.
- Reiniciar gateway ou scheduler.
- Alterar Docker/VPS/Traefik.
- Enviar mensagens externas.

## Veredito atual

Manter SPITI sem crons locais e documentar o baseline para evitar falso positivo em auditorias futuras.
