# Reminder OS × Mesa COO integration v1

Data: 2026-06-12  
Status: especificação local/documental ativa; sem alteração de cron Mesa nesta fase.  
Owner: Hermes Geral / Operações  
Superfície: Hermes Agent nativo — Brain, Kanban, ledger local, cron/watchdog e agents/profiles. Mission Control fica fora.

## Objetivo

Definir quando um loop Reminder OS deve virar decisão da Mesa COO, quando deve permanecer silencioso, e quando deve ser fechado/expirado localmente.

A Mesa COO é superfície de decisão executiva. Reminder OS é a camada de continuidade. A integração existe para impedir abandono sem transformar a Mesa em relatório de backlog.

## Critérios de promoção para Mesa COO

Um loop pode virar `Decisão N/M` quando tiver pelo menos um destes critérios:

- `status=waiting_lucas`;
- `severity=high`;
- risco de perda financeira, cliente, operação, reputação, prazo ou fonte viva;
- decisão humana clara com opções de ação;
- bloqueio recorrente que já passou por pelo menos uma revisão 2h;
- approval packet pronto aguardando escolha de Lucas;
- loop vencido cujo próximo passo não pode ser executado sem Lucas.

## Não promover para Mesa COO

Manter local/silent ou expirar quando for:

- card antigo sem risco atual;
- backlog baixo/sem prazo;
- rotina saudável;
- melhoria interna sem decisão humana;
- loop já coberto por Kanban/handoff ativo;
- duplicata detectada por dedupe;
- tarefa que exige primeiro evidência viva/read-only.

## Formato Telegram-safe

Quando promovido, a Mesa deve mostrar uma decisão limpa:

```md
## Mesa COO — YYYY-MM-DD

Decisão 1/N: [título humano]
- Dono: [owner]
- Por que importa: [risco/impacto]
- Se escolher Fazer: [ação segura imediata]
- Evidência: [referência curta, sem JSON bruto]
- Limite/risco: [o que não será executado sem aprovação]
```

Proibido expor:

- job ID;
- JSON bruto do ledger;
- wrapper técnico;
- stack trace;
- segredo, credencial ou preview de credencial;
- lista extensa de cards antigos.

## Semântica do botão Fazer

`Fazer` na Mesa só autoriza o escopo seguro descrito na própria decisão.

Se o próximo passo for produção, cliente/fornecedor, preço, estoque, campanha, Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail, banco, Docker/VPS/gateway/cron/runtime ou secrets, `Fazer` significa preparar/validar preview ou approval packet — não executar o write final.

## Fechamento e expiração

A Mesa pode recomendar:

- `retomar`: virar ação segura/local ou card Kanban;
- `fechar`: marcar `done` quando o resultado já existe;
- `expirar`: marcar `expired` quando perdeu relevância;
- `adiar`: atualizar `next_review_at`.

Fechamento/expiração são writes locais no ledger/Brain e precisam de evidência curta.

## Resumo executivo periódico

Daily/weekly governance pode medir:

- loops abertos por owner;
- loops `waiting_lucas`;
- loops vencidos;
- loops fechados/expirados;
- principais riscos de abandono.

Isso deve ficar local/Brain por padrão. Telegram só recebe se Lucas pedir ou se houver decisão acionável.

## Testes necessários antes de ativar automação real

- fixture com loop `waiting_lucas/high` promovido para decisão limpa;
- fixture com loop `low/stale` suprimido;
- teste de no-wrapper/no-job-id/no-JSON bruto;
- teste de `Fazer` não expandir escopo para writes externos;
- teste de dedupe para não gerar decisões repetidas;
- teste de fallback quando evidência está ausente: pedir evidência, não decidir.

## Guardrails

Esta fase não altera cron da Mesa, gateway, scheduler, delivery, botões ou runtime. Mudança real de Mesa/cron exige approval packet separado com rollback e verificação.
