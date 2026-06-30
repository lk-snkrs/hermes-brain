# Skill Surface Diet — fechamento all profiles

Data: 2026-06-29

## Resultado

Todos os profiles em `/opt/data/profiles` foram cobertos por Skill Surface Diet e migrados para config v30. O profile default `/opt/data` também está v30 e com Skill Surface Diet ativa.

## Escopo final

- Profiles ativos mantidos ativos e validados por PID/HERMES_HOME/Telegram/API-webhook.
- Profiles dormentes/read-only finais (`brain-process`, `hermes-ops-readonly`, `lk-analyst-readonly`, `lk-content-reviewer`) permaneceram parados; não foi iniciada nova superfície/bot.
- `lk-collection-optimizer` foi migrado v24→v30 e reiniciado scoped; PID final validado: `130730`.
- Heavy local skill copies nos quatro profiles dormentes foram compactadas com conteúdo completo preservado em `references/full-skill-before-surface-diet-20260629.md`.

## Guardrails preservados

- Writes externos: 0.
- Docker/VPS/Traefik: não tocados.
- Main/default não foi reiniciado nesta etapa final; já estava v30/ativo.
- Secrets: valores não impressos; `values_printed=false`.

## Caveats

- Default PID 1 mantém portas locais de API/health conforme runtime Main; isso é esperado para o default e não foi alterado.
- Alguns profiles usam token via fonte não exposta diretamente no env; validação Telegram foi por logs/gateway_state quando `getMe` direto não era aplicável.
