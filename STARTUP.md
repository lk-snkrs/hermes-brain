# SESSION START PROTOCOL — Hermes Brain

## Regra central

Hermes Brain é fonte versionada de contexto, decisões, rotinas, skills e governança. Ele não substitui dados vivos: para número operacional, estoque, pedido, campanha, lance, deploy ou status atual, consultar banco/API/fonte real.

## Boot recomendado

1. Identificar escopo: Lucas pessoal, LK, Zipper, SPITI, Hermes/Infra, Tecnologia, Governança ou multiempresa.
2. Ler `START-HERE.md` e `MAPA.md` quando a navegação/importância estrutural importar.
3. Ler `AGENTS.md` para guardrails globais.
4. Carregar skill relevante se existir.
5. Usar `session_search` quando o pedido depender de histórico de conversa.
6. Verificar crons reais com `cronjob list` antes de afirmar que uma rotina roda.
7. Usar Doppler `lc-keys/prd` sob demanda para credenciais; nunca imprimir valores.

## Paths atuais

- Brain: `/opt/data/hermes_bruno_ingest/hermes-brain`
- Runtime Hermes principal: `/opt/data`
- Perfis especialistas: `/opt/data/profiles/*`
- Scripts runtime comuns: `/opt/data/scripts/`

## Encerramento / handoff

Ao final de tarefa relevante:

1. Registrar decisões, receipts, approvals, riscos ou aprendizados no Brain/skill/ledger apropriado.
2. Se mexeu em docs do Brain, rodar `python3 scripts/brain_health_check.py` em `/opt/data/hermes_bruno_ingest/hermes-brain`.
3. Se for rotina recorrente, confirmar cron real via `cronjob list`; rotina documentada não prova execução.
4. Se houver alteração externa/produção, registrar evidência + rollback; ações externas exigem aprovação atual de Lucas.
5. Não usar comandos legados `/root/.hermes/scripts/brain_sync.sh`, Mem0 ou sync via `sshpass`; o fluxo atual é o fechamento/sync allowlist documentado nos relatórios `reports/brain-sync-safe-dry-run-*` e no cron `3fc45b0830c6`.
