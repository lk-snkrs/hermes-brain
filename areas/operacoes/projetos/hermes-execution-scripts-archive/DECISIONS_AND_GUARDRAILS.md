# Decisions and Guardrails — Hermes Execution Scripts Archive

## Decisões

- Onda 12 cria hub para arquivo de scripts de execução sem mover scripts nem promover execução runtime.

## Guardrails

- Script no repositório não é rotina ativa; verificar cron/runtime antes de afirmar que roda.
- Não executar scripts antigos com efeito externo sem revisão, Doppler-first e aprovação escopada.
- Procedimento recorrente deve virar rotina/skill validada antes de automação.
- Sem chmod, cron, gateway ou execução produtiva nesta onda.
