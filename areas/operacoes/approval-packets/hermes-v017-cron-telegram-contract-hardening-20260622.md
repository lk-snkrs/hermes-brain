# Approval Packet — Hardening v0.17 de contratos Telegram nos crons `origin`

Data: 2026-06-22
Status: preparado; nenhum cron foi alterado.

## Decisão solicitada

Aprovar ou não uma onda de metadata/prompt hardening em crons que entregam no Telegram (`deliver=origin`) e não têm contrato explícito de ruído/rich-message/actionability no registro/prompt.

## Evidência

Sentinel local read-only:

`/opt/data/scripts/hermes_v017_adoption_sentinel.py --json`

Resultado pós-auditoria:

- status: `attention`
- crons `origin` sem contrato explícito: 13
- profile delegation gaps: 0 após patch local de configs
- `values_printed=false`

## Risco atual

Não prova spam. Mas é drift de governança: jobs podem estar corretos pelo script, porém o registro não deixa explícito:

- silent-OK quando saudável;
- sem JSON bruto;
- sem wrapper técnico;
- sem IDs técnicos desnecessários;
- mensagem humana curta;
- rich Telegram só para decisão/falha/ação.

## O que a aprovação permite

Se aprovado:

1. backup dos cron registries;
2. patch apenas de metadata/prompt contract dos 13 jobs;
3. preservar schedule/delivery/enabled/state/script;
4. não executar jobs;
5. validar JSON do registry;
6. rerun do sentinel;
7. receipt.

## O que a aprovação NÃO permite

- Não muda schedule.
- Não muda delivery.
- Não pausa/remove jobs.
- Não executa jobs.
- Não reinicia gateway.
- Não envia mensagens externas.
- Não toca Docker/VPS/Traefik.

## Opções

1. **Aprovar hardening metadata/prompt dos 13 crons `origin`**.
2. **Aprovar só listar os 13 jobs para revisão humana**.
3. **Bloquear por enquanto; manter só sentinel/report**.

## Rollback

Restaurar `/opt/data/cron/jobs.json` e `/opt/data/profiles/*/cron/jobs.json` dos backups da onda antes do patch.

`values_printed=false`
