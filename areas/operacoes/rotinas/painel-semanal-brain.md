# Rotina — Painel Semanal do Brain

Status: v0.1 documentado / execução manual sob demanda
Área: Operações / Hermes Brain

## Objetivo

Gerar uma visão semanal de governança do Hermes Brain:

1. o que entrou no Brain e foi versionado;
2. o que ficou bloqueado pelo Brain Sync seguro;
3. quais rotinas/MAPAs precisam promoção, indexação, limpeza ou arquivamento.

## Quando usar

- Após a ativação do Brain Sync seguro.
- Semanalmente, antes de revisão executiva da Grande Mente.
- Quando Lucas perguntar “o que entrou no cérebro?”, “o que ficou bloqueado?” ou “o que precisamos limpar?”.

## Fontes

- `git log --since=<janela>` no repo `hermes-brain`.
- `reports/daily-consolidation/`.
- `reports/brain-health-check-*.json`.
- `/opt/data/scripts/brain_sync_safe.py --dry-run --verbose`.
- `empresa/rotinas/_index.md`.
- `scripts/brain_health_check.py`.

## Saída

Relatório em Markdown:

```text
reports/brain-weekly-panel/brain-weekly-panel-YYYY-MM-DD.md
```

## Template

1. Resumo executivo.
2. Entrou no Brain.
3. Bloqueado pelo Brain Sync.
4. Saúde do Brain.
5. Rotinas/MAPAs a promover ou limpar.
6. Guardrails e não-ações.
7. Próxima semana.

## Guardrails

- Não incluir segredo, token, payload bruto, mensagem completa de cliente ou HTML.
- Não tratar arquivo bloqueado como erro automaticamente; muitos bloqueios são o comportamento correto.
- Não fazer writes externos além de documentação/GitHub via Brain Sync seguro.
- Telegram só para exceção crítica; relatório normal fica no Brain/local.

## Critério de sucesso

- Relatório semanal criado.
- Health check com `FAIL=0`.
- Brain Sync dry-run explica bloqueados e não encontra allowed changes pendentes após push.
