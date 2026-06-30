# Hermes Task OS Minimalista — Onda 0

Data: 2026-06-29  
Status: aprovado por Lucas para escopo **local/read-only/documental**.  
Fonte: auditoria `reports/governance/hermes-power-user-gap-audit-reddit-2026-06-29.md` e aprovação Telegram de Lucas.

## Objetivo

Reduzir burocracia e aumentar fechamento operacional. Toda frente não-trivial precisa deixar rastro simples: **dono, status, risco, evidência e próximo passo**.

Isto não cria cron, não muda Kanban runtime, não muda gateway e não autoriza dispatch automático.

## Quando usar

Use para trabalho operacional não-trivial:

- múltiplos passos;
- handoff entre agentes/perfis;
- risco A2+;
- approval packet;
- auditoria;
- rotina ou melhoria que precisa ser retomada depois;
- qualquer entrega que mereça receipt.

Não use para resposta simples, pergunta factual curta ou leitura local trivial.

## Unidade mínima

```yaml
id: local ou card_id quando existir
owner: perfil/agente dono
status: ready | running | blocked | done | archived/stale
risk: A0 | A1 | A2 | A3 | A4
scope: read-only | local-write | runtime | external-write
next_action: ação única, verificável
source_evidence: path/comando/fonte viva
receipt_or_handoff: path quando fechado
```

## Estados

| Status | Uso |
|---|---|
| `ready` | Pode ser executado dentro do escopo aprovado. |
| `running` | Existe execução em andamento; deve ter owner e evidência. |
| `blocked` | Precisa de fonte, aprovação, humano ou ação sensível. |
| `done` | Fechado com evidência e receipt/handoff quando material. |
| `archived/stale` | Não é mais atual; preservar motivo para evitar retrabalho. |

## Regras Telegram/Mesa COO

- Mesa COO não recebe backlog bruto.
- Telegram recebe apenas decisão real, bloqueio concreto, falha atual, aprovação necessária ou alerta acionável.
- Silent-OK fica local/Brain.
- Se o status é `done`, a resposta a Lucas deve mostrar resultado executivo antes de paths.

## Approval boundaries

Permitido nesta Onda 0/Onda 1:

- docs locais;
- reports locais;
- receipts locais;
- inventários read-only;
- QA local/read-only;
- piloto documental.

Bloqueado sem nova aprovação escopada:

- cron novo ou alteração de cron;
- gateway/restart/Docker/VPS/Traefik;
- dashboard/API/webhook;
- credenciais;
- writes externos;
- mutação em produção;
- auto-routing/dispatch automático persistente.

## Gate de sucesso

Uma frente está bem fechada quando:

1. o escopo está claro;
2. a evidência foi verificada;
3. o risco foi classificado;
4. o próximo passo é único e acionável;
5. há receipt/handoff quando material;
6. nenhum ruído técnico foi enviado ao Telegram sem necessidade.
