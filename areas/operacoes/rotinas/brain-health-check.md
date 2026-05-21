# Rotina — Brain Health Check

## O que roda

Validação local do Hermes Brain para prevenir regressões estruturais antes de commits, PRs e merges documentais.

Script:

```bash
python3 scripts/brain_health_check.py
```

Relatório JSON opcional:

```bash
python3 scripts/brain_health_check.py --json reports/brain-health-check-YYYY-MM-DD.json
```

## Checks atuais

- Token-shaped secrets versionados, incluindo Doppler, Shopify, Supabase PAT, GitHub classic/fine-grained, OpenAI, Mem0, Telegram, FAL, W&B, Tinker e Google OAuth/refresh-token.
- Links markdown relativos quebrados.
- Anchors markdown internos quebrados quando o link aponta para `#secao` em arquivo `.md`.
- Arquivos estruturais obrigatórios do Brain: README, START-HERE, STARTUP, PROTOCOLS, TOOLS, ARCHITECTURE, changelog, roadmap, índices, memória, `memories/MAPA.md`, `memories/hot.md` e segurança.
- Arquivos obrigatórios por agente: `SOUL.md`, `AGENTS.md`, `TOOLS.md`, `USER.md`, `MEMORY.md`, `HEARTBEAT.md`.
- `MAPA.md` obrigatório em cada área e subárea.
- Pastas `areas/**/decisions/*.md` precisam estar navegáveis a partir do `MAPA.md` local da área/subárea.
- Rotinas em `areas/**/rotinas/*.md` ausentes de `empresa/rotinas/_index.md`.
- Skills canônicas ausentes de `empresa/skills/_index.md`.
- Skills de navegação por área que apontam para skill canônica inexistente.

## Quando rodar

- Antes de cada commit relevante.
- Após mudanças em docs/scripts.
- Antes de abrir PR no `hermes-brain`.
- Antes de squash merge autônomo de PR documental de baixo risco.
- Antes de encerrar uma fase do fluxo Bruno/OpenClaw → Hermes.
- Como base para futura rotina cron.

## Critério de aprovação

- `FAIL=0` em todos os checks.
- `WARN=0` é o alvo operacional para merges documentais autônomos.
- Se existir `WARN`, avaliar e resolver quando simples; se for exceção legítima, documentar no PR/relatório.
- Scan de secrets precisa estar limpo.

## Comando de verificação completa

```bash
python3 scripts/brain_health_check.py --json reports/brain-health-check-$(date -u +%F).json
```

## O que não prova

- Não prova que cron real está ativo.
- Não prova que VPS/Docker/gateway estão saudáveis.
- Não prova que dados vivos em Supabase/Shopify/APIs estão corretos.
- Não substitui `security-checkup.md` para nova integração/canal/agente/cron.

## Próximos incrementos possíveis

- Coluna/status real das rotinas no índice executivo.
- Relatório histórico consolidado por mês.
- Cron read-only para rodar o check e entregar resumo no Telegram, se Lucas aprovar cadência.
- Integração com checks de dados vivos por negócio apenas em rotinas específicas e aprovadas.
