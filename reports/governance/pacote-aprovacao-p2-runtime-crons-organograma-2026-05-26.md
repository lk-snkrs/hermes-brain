# Pacote de aprovação — P2 runtime/crons pós-organograma

Data: 2026-05-26  
Owner: Hermes Geral / COO  
Status: preparado; não executado.

## O que já foi feito sem produção

- Matriz agente → dono lógico → runtime → status → gap.
- Correção explícita do LK Shopify como nó próprio do LK OS.
- Classificação de profiles ativos/dormentes.
- Reforço documental de LK Shopify e LK Trends.
- Ledger/checklist de handoff/receipt.

## O que P2 significa

P2 só deve mexer em runtime/crons depois de aprovação escopada por lote.

### Lote A — validação runtime read-only
- Verificar processos por `HERMES_HOME`.
- Verificar logs dos gateways ativos.
- Verificar API/webhook off em profiles secundários.
- Sem restart.

### Lote B — ativação/restart de profiles preparados
- Escopo: um profile por vez (`lk-ops`, `lk-shopify`, `lk-trends` se aprovado).
- Pré-requisito: token correto, `.env` saneado, API/webhook off, backup.
- Execução: start/restart controlado do profile específico.
- Verificação: PID por `HERMES_HOME`, log conectado, round-trip Telegram.
- Rollback: parar apenas o profile afetado e restaurar backup.

### Lote C — crons/delivery
- Escopo: jobs listados nominalmente.
- Pré-requisito: backup registry, classificação owner, decisão de delivery.
- Execução: migrar/pausar/alterar delivery só dos jobs aprovados.
- Verificação: registry readback + próxima execução ou dry-run quando seguro.
- Rollback: restaurar registry anterior.

### Lote D — Zipper runtime futuro
- Gatilho objetivo: volume semanal recorrente de enquiries/e-mails/CRM ou necessidade de canal próprio.
- Pré-requisito: fontes, guardrails, aprovador humano e handoff definidos.
- Não criar por simetria.

## Ações explicitamente não executadas agora

- Nenhum cron criado, pausado, migrado ou removido.
- Nenhum gateway reiniciado.
- Nenhum Docker/VPS/Traefik alterado.
- Nenhum write externo em Shopify/Tiny/Klaviyo/CRM/WhatsApp/e-mail.
- Nenhum token ou secret lido/imprimido.

## Aprovação necessária para executar P2 real

Aprovar por lote e com escopo, por exemplo:

> Aprovo Lote A read-only runtime.

ou

> Aprovo Lote B apenas para LK Shopify, sem API/webhook, com backup e round-trip Telegram.

Aprovação genérica de estratégia não deve ser interpretada como autorização para restart, cron migration ou produção.
