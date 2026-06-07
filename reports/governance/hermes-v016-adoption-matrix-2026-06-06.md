# Hermes v0.16.0 — adoption matrix inicial — 2026-06-06

Fonte: GitHub Releases API, tag `v2026.6.5`, publicada em `2026-06-06T00:55:58Z`.
Runtime remoto atual revalidado posteriormente: `Hermes Agent v0.16.0 (2026.6.5)`, config version `27 ✓`.

> Status: esta matriz inicial foi **supersedida** pelo RD/PRD de adoção contínua `hermes-v016-continuous-adoption-rd-2026-06-06.md`, porque o upgrade/cutover e os Tracks 1/2 já foram executados e verificados.

## Recomendação

Manter o v0.16 como runtime atual e continuar a adoção por hábitos/processos seguros, não por novo upgrade.

v0.16 é uma release grande de superfície/admin/desktop e segurança. Para Lucas, ela é relevante para UX, observabilidade e controle. O deployment atual é Docker-first com Telegram/gateway/crons sensíveis; portanto, novas ativações de superfície/admin/remote-desktop continuam exigindo backup, smoke tests e rollback quando envolverem Docker/Traefik/gateway/secrets.

## Matriz

| Item v0.16 | Valor para Lucas | Classificação | Próxima ação segura |
|---|---:|---|---|
| Desktop nativo macOS/Linux/Windows | Alto para uso humano e multi-profile | P1 avaliar | Testar isolado/local ou contra backend seguro; não apontar direto para produção sem plano. |
| Remote Hermes / OAuth / username-password | Alto, mas sensível | A3 | Revisar modelo de auth, API/gateway e exposição antes de conectar. Preferir túnel/local primeiro. |
| Web dashboard admin panel | Alto para observabilidade/config | A3 | Comparar com Mission Control: dashboard = admin/runtime; Mission Control = decisão/receipts. Não misturar writes. |
| MCP catalog / channels / credentials / webhooks via browser | Útil, alto risco se mal exposto | A3/A4 conforme permissão | Começar read-only/capability-card; writes/credenciais exigem approval packet. |
| Fuzzy model picker / setup UX | Médio | P1 processo | Ensinar Lucas quando runtime for atualizado; sem impacto agora. |
| `/undo` N turns | Útil para chat/CLI | P1 hábito após upgrade | Incluir na micro-aula pós-upgrade. |
| Default skills trimmed / skills hub taps | Médio | P1 auditoria | Antes do upgrade, comparar skills essenciais locais para não perder comportamento. |
| Security fixes: Starlette/CVE, SSRF hardening, subprocess credential stripping | Alto | P0 avaliar | Ler diffs/release completa e mapear risco local; pode justificar janela de upgrade planejada. |

## Checklist de pacote A3 antes de qualquer swap

1. Backup de config, `.env` sem imprimir valores, skills, sessions, cron registry e scripts locais.
2. Inventário de patches locais críticos: Telegram clean delivery/inline buttons, context compression retry, model fallback/latency watchdogs, specialist profile checks, memory hygiene, runtime watchdogs.
3. Instalação paralela ou imagem nova, não mutação cega do runtime vivo.
4. `hermes config check/migrate` em staging/paralelo.
5. Smoke tests: `hermes --version`, `hermes doctor/config check`, cron list/status, API `/health`, gateway Telegram readiness, targeted tests para cron/Telegram UX e watchdogs.
6. Rollback documentado para runtime v0.15.2.
7. Aprovação explícita de Lucas antes de restart/swap Docker/gateway.

## Não executar automaticamente

- Docker/container/compose/image swap.
- Gateway restart.
- Exposição pública de dashboard/API/desktop backend.
- Alteração de secrets/credentials.
- Writes externos ou sistemas de negócio.
