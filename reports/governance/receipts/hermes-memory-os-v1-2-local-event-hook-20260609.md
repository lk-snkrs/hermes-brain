# Receipt — Hermes Memory OS v1.2 hook local por evento

Data: 2026-06-09T13:56:36Z  
Owner: LC Hermes / Hermes Agent central  
Escopo: melhoria local/silent-OK; sem runtime sensível.

## Objetivo

Sair do scan puramente periódico e criar um hook local explícito para ser chamado assim que um artefato material do Brain for criado/atualizado.

## Mudanças executadas

- Criado `/opt/data/scripts/hermes_memory_os_event_hook.py`.
- O hook aceita `path`, `--event-type`, `--since-minutes`, `--dry-run`, `--json`.
- Infere tipo do artefato: `receipt`, `handoff`, `approval_packet`, `routine`, `prd`, `daily`, `hot` ou `unknown`.
- Sugere camadas de memória sem ler/despejar conteúdo do arquivo.
- Chama `/opt/data/scripts/hermes_memory_os_daytime_checker.py` com janela curta para atualizar scorecard/eventos imediatamente.
- Gera `reports/memory-hygiene/hook-latest.json` e append em `reports/memory-hygiene/hook-events.jsonl`.
- Preserva silent-OK: sem `--json`, stdout vazio quando verde.

## Evidência de execução

- Teste do hook em receipt real: `status=ok`, `event_type=receipt`, `checker=ok`.
- Execução silent-OK: `rc=0`, `stdout_bytes=0`.
- Scorecard após hook: `status=ok`, `score=100`.

## Guardrails preservados

- Nenhum Docker/VPS/Traefik/gateway/container/restart.
- Nenhum provider externo/Mem0/Honcho ativado.
- Nenhum write em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco/campanha.
- Nenhum secret impresso ou copiado.
- Telegram permanece silent-OK; sucesso rotineiro fica local.

## Rollback

- Remover ou ignorar `/opt/data/scripts/hermes_memory_os_event_hook.py`.
- Remover/ignorar `reports/memory-hygiene/hook-latest.json` e `hook-events.jsonl`.
- Checker diurno v1.1 e cron local/no_agent continuam operando sem depender do hook.

## Próximo passo seguro

Após observar alguns ciclos, integrar chamada padrão do hook nas rotinas/skills que criam receipts/handoffs, ainda sem provider externo, gateway, Docker/VPS ou produção.
