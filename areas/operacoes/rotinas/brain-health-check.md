# Rotina — Brain Health Check

## O que roda

Validação local do Hermes Brain para prevenir regressões estruturais.

Script:

```bash
python3 scripts/brain_health_check.py
```

## Checks atuais

- Token-shaped secrets versionados.
- Links markdown relativos quebrados.
- Arquivos obrigatórios por agente.
- Rotinas de área ausentes de `empresa/rotinas/_index.md`.
- Skills canônicas ausentes de `empresa/skills/_index.md` ou referências quebradas.

## Quando rodar

- Antes de cada commit relevante.
- Após mudanças em docs/scripts.
- Antes de encerrar uma fase do fluxo Bruno/OpenClaw → Hermes.
- Como base para futura rotina cron.

## Critério de aprovação

- `FAIL=0` em todos os checks.
- Warnings podem existir, mas devem ser avaliados e resolvidos quando simples.
- Scan de secrets deve estar limpo.

## Próximos incrementos

- Validar anchors markdown.
- Validar status real de crons na VPS.
- Verificar divergência entre skills canônicas e navegação por área.
- Gerar relatório JSON para histórico.
