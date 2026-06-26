# LK GMC approved next-wave final report — 2026-05-21

Gerado em: `2026-05-21T21:17:03.933592+00:00`

## Veredito

- Packet A: aplicado no tema `lk-new-theme/dev` (unpublished) e verificado por readback de assets + DOM renderizado em browser. Não publicado em produção.
- Packet B residual: `73/73` cores com sugestão/evidência foram aplicadas e verificadas no Content/Merchant readback; `25` continuam bloqueadas sem evidência suficiente.
- Packet D: micro-piloto top 10 foi tentado por Content API e Merchant API v1 com snapshots, mas os 10 preços continuam em mismatch/lag no processed readback; não foi feito retry/bulk. Evidência aponta para Automatic Item Updates / sinais de landing page, não simples campo de feed.
- GTIN: `12` itens mantidos bloqueados; não inventei GTIN nem removi identificadores sem fonte oficial.
- Cron: `LK GMC Review read-only mandatory delivery` (`d4c26da4cd48`) reativado para quinta 09h BRT / `0 12 * * 4`, próximo `2026-05-28T12:00:00+00:00`.

## Packet A — dev theme
- Status upload: `uploaded_verified_by_sha_or_markers`
- Theme: `lk-new-theme/dev` / `155065450718` / `unpublished`
- Rollback privado: `/opt/data/hermes_bruno_ingest/local_sql/lk_theme_rollback_snapshots/lk-packet-a-dev-theme-rollback-155065450718-20260521T211447Z.json`
- Assets verificados:
  - `layout/theme.liquid` sha_match=`True` markers=`True`
  - `sections/lk-pdp.liquid` sha_match=`True` markers=`True`
- Browser/DOM renderizado:
  - `IF9737` variant `45906859589854`: title/price renderizados em `R$ 2.199,99`
  - `IF9735-9` variant `45906859622622`: title/price renderizados em `R$ 2.199,99`

## Packet B residual — colors
- Merchant API recovery execution: `{'patched_v1': 83}`
- Merchant API recovery verify: `{'readback_mismatch_or_processing_lag': 10, 'verified': 73}`
- Colors sem evidência suficiente: `25`

## Packet D — price micro-pilot top 10
- Content API attempt: `{'inserted': 83}`; mismatch_count=`85`
- Merchant API v1 attempt: `{'patched_v1': 83}`; verify=`{'readback_mismatch_or_processing_lag': 10, 'verified': 73}`
- Resultado: os `10/10` preços do micro-piloto seguem sem match no processed readback imediato. Parado por segurança para evitar loop/bulk; próxima correção deve focar sinais de landing page/theme para cada handle, como ocorreu no Packet A.

## Rollbacks privados
- Content API next-wave: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-approved-next-wave-rollback-20260521T205115Z.json`
- Merchant API next-wave: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-approved-next-wave-merchantapi-rollback-20260521T205803Z.json`
- Dev theme Packet A: `/opt/data/hermes_bruno_ingest/local_sql/lk_theme_rollback_snapshots/lk-packet-a-dev-theme-rollback-155065450718-20260521T211447Z.json`

## Não executado
- Produção Shopify não foi publicada/alterada.
- Não mexi em preço/estoque/produto no Shopify Admin.
- Não fiz bulk de Packet D.
- Não alterei GTIN sem fonte oficial.
- Não fiz feed upload/fetchNow nem campanhas/envios.

## Próximo gate recomendado
- Se quiser levar Packet A para produção: aprovar explicitamente publish/upload dos mesmos assets para o tema main, com backup live imediatamente antes e validação live sem `preview_theme_id`.
- Para Packet D: fazer diagnóstico de landing page/theme por handle dos top 10 antes de novo patch de feed; os campos de Merchant isolados não venceram os sinais automáticos.
