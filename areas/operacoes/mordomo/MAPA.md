# Mordomo / Lucas pessoal — MAPA canônico mínimo

Status: **ponte canônica criada em 2026-05-22**.

Objetivo: dar ao Mordomo/Lucas pessoal um ponto de navegação claro sem mover arquivos históricos nem criar um agente/runtime novo.

## Fonte de verdade

- Brain atual: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Runtime/profile conhecido: `/opt/data/profiles/mordomo` quando usado por bots/scripts do Mordomo.
- Documentação ativa permanece, por enquanto, em `areas/operacoes/`.

## Escopo

Mordomo cobre a camada pessoal/assistente de Lucas:

- follow-ups pessoais;
- lembretes;
- triagem de mensagens;
- drafts internos;
- CRM local/Mordomo;
- WhatsApp/Telegram pessoal quando habilitado por rotina aprovada.

## Guardrails

- Pode fazer leitura, organização local, draft e receipt interno.
- Pode enviar follow-up simples conhecido/verificado conforme autonomia já aprovada por Lucas, respeitando os bloqueios de preço, disponibilidade, reserva, negociação, reclamação, fornecedor, bulk e campanhas.
- Não enviar WhatsApp/e-mail/mensagem externa quando houver dúvida de conteúdo, destinatário, preço, disponibilidade, promessa, reclamação ou negociação.
- Não alterar Docker/VPS/gateway/cron/profile sem aprovação explícita com rollback.
- Não guardar segredos; documentar apenas nomes de secrets quando necessário.

## Arquivos principais atuais

- `areas/operacoes/crm/mordomo-crm-local-status.md` — status do CRM local.
- `areas/operacoes/mordomo-whatsapp-manual.md` — operação manual/segura de WhatsApp.
- `areas/operacoes/prds/mordomo-global-intake-followup-prd-2026-05-18.md` — PRD global de intake/follow-up.
- `areas/operacoes/prds/mordomo-hermes-v2-inteligencia-autonomia-crm-global-2026-05-21.md` — visão v2 de inteligência/autonomia.
- `areas/operacoes/prds/mordomo-whatsapp-autonomy-phase-2-2026-05-20.md` — autonomia WhatsApp fase 2.
- `areas/operacoes/base-conhecimento/mordomo-email-intake-kb-2026-05-18.md` — base de conhecimento para intake por e-mail.
- `areas/operacoes/base-conhecimento/mordomo-strategy-executor-split-2026-05-20.md` — separação estratégia/executor.
- `areas/operacoes/rotinas/mordomo-global-followup-engine-2026-05-18.md` — rotina do motor de follow-up.

## Crons/runtime relacionados — verificar sempre ao afirmar execução

A documentação não prova execução. Antes de dizer que algo do Mordomo está ativo, verificar `cronjob list` ou runtime equivalente.

Evidência de 2026-05-22:

- `Mordomo Telegram gateway watchdog` — ativo, script-only, último status ok.
- `Mordomo WhatsApp pessoal resumo 17h BRT` — pausado.
- `Mordomo WhatsApp pessoal realtime scan` — pausado.
- `Mordomo: confirmar entrega com Seda Embalagens` — one-shot pausado/antigo; candidato a arquivamento.

## Decisão de estrutura

Por enquanto, este MAPA é uma **ponte canônica**. Não cria novo agente nem muda runtime.

Critério para virar pasta maior `agentes/mordomo/` ou `areas/lucas-pessoal/`:

- volume recorrente alto;
- múltiplos scripts/rotinas ativos;
- decisões pessoais frequentes que precisam ficar separadas de Operações Hermes;
- necessidade de perfil/bot próprio com AGENTS/SOUL/HEARTBEAT.

Até lá, manter em `areas/operacoes/mordomo/MAPA.md` e indexar documentos relevantes daqui.

## Projetos Brain OS

- `../projetos/mordomo-os/` — hub canônico Onda 2 do Mordomo OS, preservando esta ponte canônica e indexando PRDs, SOUL, registry, rotinas, guardrails e reports.
