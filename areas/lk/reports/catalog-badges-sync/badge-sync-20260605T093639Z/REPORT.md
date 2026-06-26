# LK catalog badges sync

Data: 2026-06-05T09:36:39.275951+00:00
Modo: preview

## Evidência
- Menus: `main-menu, mega-menu-c-pia-1, mega-menu-mobile`
- Coleções alvo: `140`
- Produtos escaneados: `2329`
- Produtos com mudança planejada: `0`
- NEW 90d encontrados: `194`
- GA4: `{"available": true, "rows_total": 2413, "property": "348553567"}`

## Interpretação
- Badge `NEW` passou a ser padronizado em janela de `90` dias via tag `new`.
- Badge `BEST SELLER` passou a ser padronizado por coleção via tag `best-seller--<handle>`; tags genéricas antigas são removidas pelo sync para evitar badge fora de contexto.
- Produtos esgotados/OOS são excluídos da candidatura de `BEST SELLER`, mesmo que venceriam por score.
- O ranking usa híbrido 70% vendas Shopify + 30% GA4 page views, limitado às coleções do menu principal.

## Preview

## Risco
- Write externo em Shopify: tags de produtos e lógica de badge do tema.
- Requer readback após aplicação para confirmar tags no Admin/API.

## Bloqueio
- Nenhum bloqueio técnico identificado no preview.

## Rollback
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260605T093639Z/rollback-snapshot.json`
- Restaurar `current_tags` por product id usando o mesmo script em modo rollback, ou aplicar manualmente o snapshot.

## Próxima decisão
- Se o preview estiver ok, executar `--apply` e validar readback dos produtos alterados.