# LK catalog badges sync

Data: 2026-05-30T20:47:54.789408+00:00
Modo: preview

## Evidência
- Menus: `main-menu, mega-menu-c-pia-1, mega-menu-mobile`
- Coleções alvo: `81`
- Produtos escaneados: `2326`
- Produtos com mudança planejada: `2`
- NEW 90d encontrados: `199`
- GA4: `{"available": true, "rows_total": 2425, "property": "348553567"}`

## Interpretação
- Badge `NEW` passou a ser padronizado em janela de `90` dias via tag `new`.
- Badge `BEST SELLER` passou a ser padronizado por coleção via tag `best-seller--<handle>`; tags genéricas antigas são removidas pelo sync para evitar badge fora de contexto.
- Produtos esgotados/OOS são excluídos da candidatura de `BEST SELLER`, mesmo que venceriam por score.
- O ranking usa híbrido 70% vendas Shopify + 30% GA4 page views, limitado às coleções do menu principal.

## Preview
- Moletom Represent Clo Owners Club Zip Ash Grey Cinza (`moletom-represent-clo-owners-club-zip-ash-grey-cinza`): +[best-seller--moletom-1] / -[-]
- Moletom Slyce Off Court Off White (`moletom-slyce-off-court-off-white`): +[-] / -[best-seller--moletom-1]

## Risco
- Write externo em Shopify: tags de produtos e lógica de badge do tema.
- Requer readback após aplicação para confirmar tags no Admin/API.

## Bloqueio
- Nenhum bloqueio técnico identificado no preview.

## Rollback
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260530T204754Z/rollback-snapshot.json`
- Restaurar `current_tags` por product id usando o mesmo script em modo rollback, ou aplicar manualmente o snapshot.

## Próxima decisão
- Se o preview estiver ok, executar `--apply` e validar readback dos produtos alterados.