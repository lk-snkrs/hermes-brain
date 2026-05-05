# Rotina — Hermes Release Watch

## O que faz

Verifica novidades do Hermes Agent e avalia como elas podem melhorar o Hermes Brain, skills, memória, gateway, crons e operação do Lucas.

## Fonte

GitHub releases do repositório `NousResearch/hermes-agent`.

## Última release consultada nesta fase

- Data da consulta: 2026-05-04.
- Tag upstream: `v2026.4.30`
- Nome upstream: Hermes Agent v0.12.0 (2026.4.30)
- Tema: “The Curator release”
- Versão observada no runtime Docker Hostinger: Hermes Agent v0.9.0 (2026.4.13)
- Interpretação: há gap entre produção e upstream; update de runtime é ação de produção e exige aprovação Lucas + backup/rollback.

## Novidades relevantes para Lucas/Hermes Brain

- Autonomous Curator: manutenção autônoma de skills.
- Self-improvement loop melhorado: melhor decisão sobre memória/skills.
- `hermes skills check/update`: atualização de skills.
- `hermes update --check`: preflight antes de update.
- Gateway plugins e media parity: mais robustez para plataformas/mídia.
- Secret redaction off by default: aumenta importância do nosso scan próprio.
- Observability/Langfuse plugin: potencial para monitorar sessões e custos.
- Cron/gateway melhorias: útil para rotinas de release watch/health checks.

## Como avaliar cada release

Para cada novidade:

1. O que mudou no Hermes?
2. Isso melhora o Brain, skills, memória, crons, Telegram ou segurança?
3. Existe risco operacional?
4. Dá para aplicar agora ou só documentar?
5. Qual arquivo/skill/rotina deve ser atualizado?

## Resultado esperado

- Atualizar `empresa/gestao/memory-system.md` se envolver memória/skills.
- Atualizar `ROADMAP-30-DIAS-HERMES.md` se virar próxima rodada.
- Atualizar skills internas se o procedimento mudar.
- Para update do runtime Hostinger, usar `areas/operacoes/rotinas/hermes-runtime-update-plan.md`.
- Não rodar `hermes update`, `docker compose pull`, restart ou recriação em produção sem plano e aprovação.

## Post-check operacional

Após a primeira execução esperada em 2026-05-11 09:00 UTC, há um job one-shot `Hermes release watch post-check` (`1f60e374d0ba`) agendado para 09:15 UTC. Ele deve verificar somente em modo read-only se o release watch executou/entregou. Se não houver execução, registrar evidência e pedir aprovação antes de qualquer correção em gateway/cron/Docker.
