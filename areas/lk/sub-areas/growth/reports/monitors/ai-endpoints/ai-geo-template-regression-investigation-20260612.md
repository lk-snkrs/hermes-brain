# LK Growth — investigação de regressão AI/GEO templates — 2026-06-12

Gerado em UTC: 2026-06-12T18:00:06.425413+00:00

## Veredito

- Regressão confirmada entre `2026-06-12T14:58:39Z` e `2026-06-12T17:10:26Z`.
- O `/llms.txt` saiu do estado estratégico curto (~5k chars, source map presente) para snapshot longo (~47k chars, source map ausente) com termos operacionais proibidos.
- O `/llms-full.txt` também perdeu `LK_GEO_SOURCE_MAP_START` e voltou a conter termos operacionais.
- Não encontrei evidência, nos crons LK Growth, de rotina recorrente que tenha executado Shopify write nesse intervalo.
- Como o Shopify Asset API não entrega histórico de versões/autor do asset, não é possível atribuir 100% o autor apenas por Shopify read-only depois do fato.

## Linha do tempo verificada

- `2026-06-09T18:18Z`: pacote `llms-fix-all` aplicou estado estratégico em produção. `/llms.txt` ficou ~5k chars, com `LK_GEO_SOURCE_MAP_START` e termos proibidos zerados.
- `2026-06-10T09:10Z`, `2026-06-10T17:10Z`, `2026-06-11T09:10Z`, `2026-06-11T17:10Z`, `2026-06-12T09:10Z`: monitor público OK.
- `2026-06-12T14:58:39Z`: monitor manual após ajuste de stdout ainda OK; `/llms.txt` len ~5030, `/llms-full.txt` len ~122351.
- `2026-06-12T17:10:26Z`: cron detectou regressão; `/llms.txt` len ~47848, source map ausente e termos proibidos presentes; `/llms-full.txt` len ~119141, source map ausente e termos proibidos presentes.
- `2026-06-12T17:20–17:22Z`: correção aprovada por Lucas e aplicada em production theme `155065417950`.
- `2026-06-12T17:22:58Z`: monitor final OK.

## O que foi checado

- `jobs.json` LK Growth: nenhum cron ativo com write Shopify nesse intervalo; monitor AI/GEO é `no_agent`/read-only.
- Outputs de cron LK Growth e LK Content entre 14:59–17:10 UTC.
- State DB/mensagens de perfis Hermes entre 14:59–17:10 UTC buscando `llms`, `templates/llms`, `assets.json`, `155065417950`, `theme`, `Shopify`.
- Shopify Admin API read-only:
  - assets atuais `templates/llms.txt.liquid` e `templates/llms-full.txt.liquid` existem e após nossa correção ficaram com `updated_at=2026-06-12T14:22:18-03:00`.
  - endpoint `events.json` não retornou eventos de theme/asset úteis para atribuição.
- Receipts e workdirs de 2026-06-09 para comparar hashes/lengths.

## Hipótese mais provável

- Alguma ação fora do cron LK Growth — manual, app/admin Shopify, rotina de sync/deploy não registrada em receipts Growth, ou agente fora do intervalo auditável — regravou os dois assets com uma versão longa derivada do snapshot antigo, removendo os markers `LK_GEO_SOURCE_MAP_START/END` e reintroduzindo trechos operacionais.
- O padrão sugere overwrite integral de template, não edição pontual: ambos os arquivos mudaram de tamanho e perderam markers no mesmo intervalo.

## Prevenção aplicada agora

- Monitor `lk_ai_endpoints_monitor.py` foi endurecido localmente:
  - passa a falhar se `/llms.txt` ou `/llms-full.txt` perderem `LK_GEO_SOURCE_MAP_START`;
  - passa a comparar hash público contra baseline aprovada;
  - se houver alteração de conteúdo sem atualizar baseline aprovada, alerta `content_hash_drift`;
  - continua falhando com termos proibidos.
- Baseline aprovada salva em:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/monitors/ai-endpoints/ai-endpoints-approved-baseline.json`
- Backup do script antes do hardening:
  - `/opt/data/profiles/lk-growth/scripts/lk_ai_endpoints_monitor.py.bak_20260612_drift_guard`
- Rerun pós-hardening:
  - `Veredito: OK`
  - `Falhas: 0`
  - relatório: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/monitors/ai-endpoints/ai-endpoints-monitor-20260612T175935Z.json`

## Recomendações pendentes

1. Approval separado para restaurar `/llms.txt` ao formato estratégico curto (~5k chars) do pacote `llms-fix-all-20260609`; hoje ele está seguro, mas ainda longo.
2. Antes de qualquer futuro pacote AI/GEO, atualizar baseline apenas junto do receipt aprovado.
3. Se a regressão repetir, investigar apps/theme deploys externos e usuários/admins Shopify com acesso a theme edit, porque o histórico local não aponta cron LK Growth.

## Segurança

- Secrets não foram impressos.
- A investigação foi read-only em Shopify.
- Writes realizados nesta etapa foram locais: script do monitor, baseline e relatório.
