# Receipt — LK Variante client-side footer hotfix attempt

Data: 2026-06-03T00:55:24.772843+00:00

## Ação aprovada

Lucas aprovou aplicar direto em Production como hotfix com backup/readback/rollback.

## O que foi feito

- Tema Production confirmado: `lk-new-theme/production` / `155065417950` / role `main`.
- Asset alterado via Shopify Admin API: `assets/lk-footer.js`.
- Backup salvo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/client-side-correction-plan-20260603/production-footer-hotfix-20260603T005234Z/assets__lk-footer.before.js`.
- Readback Admin passou: `True`.
- Marker no readback Admin: `True`.

## Evidência técnica

- SHA antes: `e5032b9a599bcb0aa0fc5ff2f50fb82ee9147588ce27377650429eaa216ce7a1`
- SHA proposto/readback: `06a3bb965b9c44d1fc94605bce4152e5ff1207313caab48de379676c16ac4f12`
- Bytes adicionados no source Admin: `3223`

## QA público

O hotfix **não chegou no asset público carregado pelo HTML stale**:

- `https://lksneakers.com.br/cdn/shop/t/91/assets/lk-footer.js?v=64977926636341263331780325147`: len `3085`, marker `False`
- `https://lksneakers.com.br/cdn/shop/t/91/assets/lk-footer.js`: len `3053`, marker `False`

Revalidação adicional:

- `air-jordan-1-high-85-college-navy` carrega `https://lksneakers.com.br/cdn/shop/t/91/assets/lk-footer.js?v=64977926636341263331780325147`: len `3085`, marker `False`
- `new-balance-530-white-natural-indigo-1` carrega `https://lksneakers.com.br/cdn/shop/t/99/assets/lk-footer.js?v=64977926636341263331780446162`: len `3085`, marker `False`

## Interpretação

O write no source do tema funcionou por Admin API, mas o storefront continua servindo URLs/version hashes públicos antigos de `lk-footer.js`. Portanto a estratégia “corrigir via asset global já carregado pelo HTML stale” não é suficiente para as PDPs stale atuais.

## Risco atual

Baixo: a alteração está no source Admin do tema Production, mas não aparece no asset público carregado pelas PDPs testadas. Se o HTML/asset re-renderizar futuramente, o JS é restrito a `.lk-variante` e só troca label por handle conhecido.

## Rollback disponível

Restaurar `{report['backup_path']}` em `assets/lk-footer.js` no tema `{report['theme']['id']}`.

## Próximo passo recomendado

Adicionar esta evidência ao pacote Shopify Support: até o asset global alterado por Admin API não atualiza/atinge as URLs públicas versionadas servidas pelo rendered HTML stale. Não fazer mais hotfixes de cache-bust no mesmo tema sem suporte/purge Shopify.
