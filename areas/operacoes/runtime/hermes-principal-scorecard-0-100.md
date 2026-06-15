# Hermes Principal Scorecard 0–100

Status: ativo desde 2026-06-15.
Owner: Hermes Geral / Operações.
Fonte viva: `reports/nightly-ops-audit/latest.json` → campo `scorecard`.
Executor: `/opt/data/scripts/hermes_nightly_ops_audit.py` espelhado em `areas/operacoes/scripts/hermes_nightly_ops_audit.py`.
Digest consumidor: cron 03h `Relatório Hermes diário ... + Score 0–100`.

## Objetivo

Dar uma nota executiva de 0 a 100 no digest das 03h para os sistemas principais do Hermes, sem transformar o relatório em log técnico.

A nota mede confiança operacional, não valor de negócio. Ela usa evidência local/sanitizada da auditoria 02h50: registry de crons, perfis Hermes vivos, achados `critical/attention/watch`, contratos silent-OK e presença de jobs obrigatórios.

## Escala

- 90–100: excelente.
- 80–89: bom.
- 70–79: atenção leve.
- 50–69: atenção.
- 0–49: ação necessária.

Regra de segurança: qualquer `critical` limita a nota geral a no máximo 69; qualquer `attention` limita a no máximo 84. `watch` desconta pouco, pois é observação/maturação, não incidente.

## Áreas principais pontuadas

- Runtime/Gateways — gateways, latência, profiles e watchdogs de runtime.
- Crons/Scheduler — integridade de scripts, status dos crons ativos e contratos de entrega.
- Brain OS — Fechamento/Brain Sync, Brain OS 02h25 e governança do Brain.
- Memory OS — higiene de memória, Memory OS e alertas de saturação/contexto.
- Nightly Ops Audit — auditoria transversal 02h50 e artifact local para o digest.
- Reminder OS — continuidade/open loops; Telegram/origin é exceção aprovada por Lucas.
- Daily Learning/Digest — 02h Daily Intelligence e 03h digest executivo.
- Segurança/Secrets — evidência sanitizada, `values_printed=false`, Doppler/secret hygiene.

## Contrato do digest 03h

O digest deve incluir uma linha `Nota Hermes` com:

- nota geral `X/100`;
- notas por área principal;
- explicação curta do que puxou a nota para baixo;
- status humano: OK, Atenção controlada ou Ação necessária.

Não deve imprimir JSON bruto, IDs técnicos, wrappers, tokens, previews, connection strings ou valores sensíveis.

## Guardrails

- Scorecard é read-only/local; não autoriza mutação de cron, Docker/VPS/Traefik/gateway, secrets, integrações externas, clientes/fornecedores, Shopify/Tiny/Supabase/GMC/Klaviyo ou ações destrutivas.
- Correções A0/A1 continuam limitadas ao contrato do Nightly Ops Audit.
- Reminder OS permanece autorizado a alertar no Telegram quando houver loop aberto acionável.
- Outros watchdogs devem continuar silent-OK/local salvo exceção aprovada.

## Cron/Scheduler hardening — 2026-06-15

Lucas aprovou as fases A/B/C para melhorar o componente `Crons/Scheduler`.

Executado:

- Fase A: `enabled_cron_no_success_yet` ganhou grace period antes da primeira janela `next_run_at`; crons novos/mensais/futuros não reduzem a nota antes do primeiro vencimento.
- Fase B: entregas `origin/telegram` não-obrigatórias foram contidas para `local`, mantendo como superfícies Lucas-facing obrigatórias o digest 03h, Reminder OS, Mesa COO e alertas realmente acionáveis.
- Fase C: smoke seguro feito por sintaxe/compilação para scripts pendentes; scripts com possível envio externo/WhatsApp/cliente não foram executados live.

Jobs alterados para `deliver=local` nesta onda:

- default: `c1ce34b4449a`, `b78ae7ac81d0`, `7b7ae67655c5`, `bc96bb03d2b0`.
- `lk-ops`: `lk-pos-postpurchase-canary`, `3f044d9c6f99`, `45a6cd07c138`.
- `lk-shopify`: `198d5fa71996`.
- `lk-content`: `d4d4bf090aa7`.
- `lk-stock`: `c45da7bb0fcb`, `2fd03de2c8b8`.
- `mordomo`: `c358f8f56a26`, `7e7995f01070`, `b47c29d8ad2b`, `289a4019872d`.

Rollback: restaurar os cron registries em `/opt/data/backups/cron-scheduler-score-improvement-20260615T013006Z/` ou reverter apenas `deliver` desses jobs para `origin` se Lucas quiser voltar a receber algum deles no Telegram.

## Verificação

Smoke atual em 2026-06-15 após A/B/C:

- `python3 -m py_compile /opt/data/scripts/hermes_nightly_ops_audit.py`: OK.
- `python3 /opt/data/scripts/hermes_nightly_ops_audit.py --autoheal --json-only`: OK.
- Safe syntax smoke dos scripts pendentes: OK.
- Artifact: `reports/nightly-ops-audit/latest.json` com `scorecard.overall_score=100`, `Crons/Scheduler=100`, `overall_status=excelente`, `critical=0`, `attention=0`, `watch=0`, `values_printed=false`.
