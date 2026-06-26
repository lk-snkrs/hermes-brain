# Rotina — Hermes v0.17 Adoption Sentinel

Status: ativa como rotina local/read-only, ainda não agendada em cron.
Data: 2026-06-22
Script: `/opt/data/scripts/hermes_v017_adoption_sentinel.py`

## Objetivo

Detectar drift de adoção Hermes v0.17 no ecossistema Lucas/Cimino sem mutar runtime:

- perfis/agentes sem `delegation.max_async_children`;
- perfis com `orchestrator_enabled` mas sem toolset `delegation`;
- jobs `deliver=origin` sem contrato Telegram/noise explícito;
- scripts sem sinais de Delegated Done / Tester Receipt;
- evidência Brain/skills de adoção v0.17.

## Contrato silent-OK

- `python3 /opt/data/scripts/hermes_v017_adoption_sentinel.py --quiet`
- `rc=0` + stdout vazio = OK.
- `rc=0` + stdout JSON sanitizado = atenção/documentary gap.
- Não imprime secrets; `values_printed=false`.

## Escopo permitido

A rotina é read-only:

- lê `/opt/data/config.yaml`;
- lê `/opt/data/profiles/*/config.yaml`;
- lê `/opt/data/cron/jobs.json` e `/opt/data/profiles/*/cron/jobs.json`;
- lê `/opt/data/scripts`;
- lê Brain/skills para evidência v0.17.

## Escopo bloqueado

Sem aprovação escopada, a rotina não deve:

- alterar cron registry;
- reiniciar gateway/perfis;
- alterar Docker/VPS/Traefik;
- ativar dashboard/API público;
- ativar WhatsApp Cloud, Photon/iMessage, Raft ou SimpleX;
- instalar MCP;
- trocar modelo default;
- imprimir valores de credenciais.

## Critérios de ação

### Ação autônoma local/documental

Permitido:

- gerar relatório Brain;
- atualizar skill/reference;
- criar approval packet;
- sugerir patch de config local com backup quando não exigir restart imediato;
- registrar receipt.

### Approval packet obrigatório

Obrigatório para:

- restart de gateways/perfis para ativar toolsets/config;
- cron schedule/delivery/prompt mutation;
- dashboard/API/webhook público;
- canais externos;
- instalação MCP com OAuth/write/stdio suspeito;
- qualquer write externo/prod.

## Estado inicial 2026-06-22

Após primeira execução:

- profile delegation gaps: 0 depois do patch local de configs;
- crons `origin` sem contrato explícito: 13;
- script sentinel criado e contém Delegated Done check;
- status ainda `attention` por gaps documentais em cron metadata/prompt.

## Próximos passos

1. Criar pacote de aprovação para ativação via restart dos perfis configurados.
2. Criar pacote de aprovação para hardening metadata/prompt dos 13 jobs `origin` sem contrato explícito.
3. Se aprovado, aplicar em ondas pequenas com backup/rollback/readback.

`values_printed=false`
