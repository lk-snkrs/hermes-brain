# Rotina — Hermes Release Watch

## O que faz

Verifica novidades do Hermes Agent e avalia como elas podem melhorar o Hermes Brain, skills, memória, gateway, crons e operação do Lucas.

## Fonte

GitHub releases do repositório `NousResearch/hermes-agent`.

## Última release consultada nesta fase

- Data da consulta inicial: 2026-05-04.
- Atualização operacional: 2026-05-10.
- Tag upstream revisada: `v2026.5.7`.
- Nome upstream: Hermes Agent v0.13.0 (2026.5.7), “The Tenacity Release”.
- Versão observada após deploy aprovado: Hermes Agent v0.13.0 em containers Docker Hostinger.
- Interpretação atual: produção já está em v0.13; release watch deve focar em novas releases/latest e operacionalização pendente da v0.13, não em repetir update de runtime.
- Qualquer futura troca de runtime/Docker/image/compose/restart continua exigindo aprovação Lucas + backup/rollback.

## Novidades relevantes para Lucas/Hermes Brain

### v0.13 — operacionalizar primeiro

- `/goal`: padrão para missões longas que antes dependiam de “seguir”.
- Multi-Agent Kanban: base para `lk-growth-ops`/Mission Control, começando como checklist/board documentado antes de workers reais.
- `no_agent` cron: watchdogs baratos e silenciosos para health checks read-only.
- `[[as_document]]`: relatórios grandes entregues como documento no Telegram.
- Segurança: redaction, allowlists, prompt-injection scan de cron/skills e logs redigidos.
- Gateway auto-resume: útil para janelas futuras de restart, mas não elimina necessidade de aprovação.
- Dashboard: útil local-only/SSH; exposição pública exige hardening aprovado.

### v0.12 e anteriores ainda úteis

- Autonomous Curator: manutenção autônoma de skills.
- Self-improvement loop melhorado: melhor decisão sobre memória/skills.
- `hermes skills check/update`: atualização de skills.
- `hermes update --check`: só como preflight; em Docker/custom image pode não servir como mecanismo de update.
- Gateway plugins e media parity: mais robustez para plataformas/mídia.
- Cron/gateway melhorias: útil para release watch, health checks, `context_from`, `workdir` e toolsets enxutos.
- Webhook/direct-delivery: útil para integrações event-driven após desenho seguro.

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
- Atualizar `areas/operacoes/rotinas/hermes-v013-operacionalizacao.md` quando uma novidade v0.13 virar uso diário.
- Atualizar `areas/operacoes/rotinas/hermes-v013-watchdogs-no-agent.md` quando um watchdog read-only for proposto/testado.
- Atualizar `areas/operacoes/rotinas/hermes-v013-kanban-lk-growth-ops.md` quando o Mission Control LK evoluir.
- Atualizar skills internas se o procedimento mudar.
- Para update do runtime Hostinger, usar `areas/operacoes/rotinas/hermes-runtime-update-plan.md`.
- Não rodar `hermes update`, `docker compose pull`, restart ou recriação em produção sem plano e aprovação.

## Post-check operacional

Após a primeira execução esperada em 2026-05-11 09:00 UTC, há um job one-shot `Hermes release watch post-check` (`1f60e374d0ba`) agendado para 09:15 UTC. Ele deve verificar somente em modo read-only se o release watch executou/entregou. Se não houver execução, registrar evidência e pedir aprovação antes de qualquer correção em gateway/cron/Docker.
