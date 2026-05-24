# Backlog de ruído e jobs pausados — Brain Runtime — 2026-05-22

Status: **parcialmente corrigido**, com uma limpeza segura de cron one-shot vencido. Sem alteração de delivery, schedule, scripts, Docker, gateway ou runtime.

## Por que existe

No padrão Bruno/OpenClaw adaptado ao Hermes, sucesso normal deve ser silencioso/local. Telegram/origin deve ficar para decisão, exceção, falha, risco crítico ou pedido explícito de Lucas.

A reconciliação runtime de 2026-05-22 mostrou que o sistema está saudável, mas ainda há pendências de governança de ruído e de limpeza de one-shots antigos.

## Watchdogs/jobs ativos com delivery `origin` que merecem revisão de ruído

Não alterar automaticamente. Antes de mudar delivery, validar se o script realmente é silent-OK e se stdout só aparece em ação/falha.

- `Hermes runtime + cron watchdog no_agent` (`edd06fe19397`) — ativo, `origin`.
- `Hermes compression failure self-heal watchdog` (`4bb4e2223fd3`) — ativo, `origin`.
- `Mordomo Telegram gateway watchdog` (`ac0b440e2643`) — ativo, `origin`.
- `LK Growth Telegram gateway watchdog` (`876d54c62ccd`) — ativo, `origin`.
- `SPITI Telegram gateway watchdog` (`663e3e6a148c`) — ativo, `origin`.
- `Hermes Brain Operating Layer structural watchdog` (`d03fa04e1188`) — ativo, `origin`, mas no_agent/silent-OK.
- `LK WhatsApp Hermes responder regression watchdog` (`a5d7a392eed9`) — ativo, `origin`.

## Jobs pausados/one-shot que merecem reconciliação documental

Não remover automaticamente sem escopo explícito.

- `Mordomo: confirmar entrega com Seda Embalagens` (`527ee57b3a6b`) — **removido em 2026-05-22** por estar vencido (`once at 2026-05-19 12:00`), pausado e sem `last_run_at`.
- `LK SEO/CRO impact review — SEO title/meta P1 packets` (`a7e883edd200`) — one-shot futuro/pausado sem execução registrada; mantido porque envolve avaliação operacional futura e não estava vencido na mesma categoria.
- Crons pausados de SEO/CRO/influencer/Mordomo devem ser mantidos ou arquivados com decisão explícita do contexto operacional.

## Critério seguro para futura alteração

Para cada job candidato:

1. Ler script/prompt.
2. Confirmar contrato: `rc=0 + stdout vazio = OK`, `rc=0 + stdout = alerta/auto-heal`, `rc!=0 = falha`.
3. Confirmar canal esperado: local, origin ou externo.
4. Se for apenas redução de ruído sem mudar execução externa, preparar patch/brief com rollback.
5. Se envolver gateway, Docker, host, externo, mensagem ou fonte de verdade, pedir aprovação explícita.

## Decisão desta rodada

- Cron one-shot vencido `527ee57b3a6b` removido.
- Demais jobs pausados/ativos preservados sem alteração por exigirem contexto operacional ou aprovação específica.
- Redução de ruído de delivery `origin → local` fica para rodada própria, sem misturar com correção documental/segurança.
