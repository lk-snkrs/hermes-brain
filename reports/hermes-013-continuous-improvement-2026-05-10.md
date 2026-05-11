# Hermes 0.13 + melhoria contínua — 2026-05-10

## Decisão Lucas
Lucas aprovou seguir com atualização para Hermes 0.13 e pediu rotina diária às 02:00 BRT para manter Hermes/LK sempre atualizado, mais inteligente e mais completo.

## Guardrails
- Implementar autonomamente melhorias de baixo risco: Brain, skills, docs, scripts read-only, previews, checks, PRs documentais.
- Toda melhoria automática deve ser operacionalizada no dia a dia: virar skill, checklist, rotina, relatório, cron, dashboard local, comando reutilizável ou documentação prática.
- O que for manual deve ser ensinado ao Lucas com uso claro: comando/ação, quando usar, resultado esperado e sinais de falha.
- Mudanças de médio/alto risco devem virar pergunta objetiva para Lucas, com benefício, risco, blast radius, backup/rollback e recomendação.
- Não alterar produção/infra/secrets/banco/host/Docker/Traefik/campanhas/Shopify writes sem plano, backup/rollback e aprovação explícita.
- Nunca imprimir secrets.

## Cron criado
- Nome: Hermes/LK daily continuous improvement scan
- Job ID: f5a23dd6a1bd
- Schedule: `0 5 * * *` UTC = 02:00 BRT
- Deliver: origem/Telegram Lucas
- Skills: hermes-agent, lucas-hermes-continuous-improvement, multiempresa-routing-lucas, lucas-chief-of-staff

## Rotina diária
1. Verificar versão Hermes ativa.
2. Buscar releases em NousResearch/hermes-agent: latest e janela histórica recente/relevante, especialmente v0.10, v0.11, v0.12 e v0.13 enquanto estivermos fazendo catch-up.
3. Ler release notes e classificar impacto para LK/Hermes Brain: adotar agora, ensinar uso manual, guardar para depois, ignorar, ou pedir aprovação por risco.
4. Implementar e operacionalizar melhorias de baixo risco no fluxo real.
5. Ensinar ao Lucas o que for manual.
6. Preparar updates runtime em paralelo, com rollback.
7. Perguntar antes de qualquer médio/alto risco.
8. Reportar recomendações e aprovações necessárias.

## 0.13 preparado em paralelo
- Clone local: `/opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0`
- Tag: `v2026.5.7`
- Head: `498bfc7`
- Patch local preservado: retry de falhas transitórias de compressão/contexto antes de fallback destrutivo.
- Teste rodado: `/opt/hermes/.venv/bin/python -m pytest tests/agent/test_context_compressor.py -q -o 'addopts='`
- Resultado: `70 passed in 2.95s`

## Próximas ações recomendadas
1. Buildar imagem custom Hermes 0.13 em paralelo.
2. Rodar smoke tests de CLI/config/skills/cron/gateway em staging/local.
3. Validar Docker/user não-root e config `/opt/data/config.yaml`.
4. Planejar janela de restart com rollback para trocar gateway.
5. Após update: ativar `/goal`, Kanban LK Growth Ops, Shopify optional skill read-only, watchdogs `no_agent`, dashboard local-only.
