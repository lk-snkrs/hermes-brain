# LK catalog badges sync

Data: 2026-05-29T13:17:02.386247+00:00
Modo: preview

## Evidência
- Menu: `main-menu`
- Coleções alvo no menu: `48`
- Produtos escaneados: `2316`
- Produtos com mudança planejada: `3`
- NEW 90d encontrados: `193`
- GA4: `{"available": true, "rows_total": 2422, "property": "348553567"}`

## Interpretação
- Badge `NEW` passou a ser padronizado em janela de `90` dias via tag `new`.
- Badge `BEST SELLER` passou a ser padronizado por coleção via tag `best-seller--<handle>`; tags genéricas antigas são removidas pelo sync para evitar badge fora de contexto.
- Produtos esgotados/OOS são excluídos da candidatura de `BEST SELLER`, mesmo que venceriam por score.
- O ranking usa híbrido 70% vendas Shopify + 30% GA4 page views, limitado às coleções do menu principal.

## Preview
- Pop Mart Labubu The Monsters Coca-Cola Series Look What I Found Figure (`pop-mart-labubu-the-monsters-coca-cola-series-look-what-i-found-figure`): +[-] / -[best-seller--pop-mart]
- Pop Mart Labubu The Monsters Coca-Cola Series Special Sofa Figure (`pop-mart-labubu-the-monsters-coca-cola-series-special-sofa-figure`): +[-] / -[best-seller--collectibles]
- Pop Mart Labubu The Monsters Have a Seat ZIZI Vinyl Plush Pingente (`pop-mart-labubu-the-monsters-have-a-seat-zizi-vinyl-plush-pingente`): +[best-seller--collectibles, best-seller--labubu, best-seller--pop-mart] / -[-]

## Risco
- Write externo em Shopify: tags de produtos e lógica de badge do tema.
- Requer readback após aplicação para confirmar tags no Admin/API.

## Bloqueio
- Nenhum bloqueio técnico identificado no preview.

## Rollback
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T131702Z/rollback-snapshot.json`
- Restaurar `current_tags` por product id usando o mesmo script em modo rollback, ou aplicar manualmente o snapshot.

## Próxima decisão
- Se o preview estiver ok, executar `--apply` e validar readback dos produtos alterados.