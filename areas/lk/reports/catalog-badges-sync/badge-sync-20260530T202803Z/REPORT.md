# LK catalog badges sync

Data: 2026-05-30T20:28:03.922537+00:00
Modo: apply

## Evidência
- Menus: `escopo manual`
- Coleções alvo: `1`
- Produtos escaneados: `2326`
- Produtos com mudança planejada: `8`
- NEW 90d encontrados: `199`
- GA4: `{"available": true, "rows_total": 2425, "property": "348553567"}`

## Interpretação
- Badge `NEW` passou a ser padronizado em janela de `90` dias via tag `new`.
- Badge `BEST SELLER` passou a ser padronizado por coleção via tag `best-seller--<handle>`; tags genéricas antigas são removidas pelo sync para evitar badge fora de contexto.
- Produtos esgotados/OOS são excluídos da candidatura de `BEST SELLER`, mesmo que venceriam por score.
- O ranking usa híbrido 70% vendas Shopify + 30% GA4 page views, limitado às coleções do menu principal.

## Preview
- Tênis On Running Cloudsolo Loewe Black Eggshell Preto (`tenis-on-running-cloudsolo-loewe-black-eggshell-preto`): +[best-seller--loewe-x-on-running] / -[-]
- Tênis On Running Cloudsolo Loewe Dark Brown Black Marrom (`tenis-on-running-cloudsolo-loewe-dark-brown-black-marrom`): +[best-seller--loewe-x-on-running] / -[-]
- Tênis On Running Cloudsolo Loewe Dark Sand Cream Bege (`tenis-on-running-cloudsolo-loewe-dark-sand-cream-bege`): +[best-seller--loewe-x-on-running] / -[-]
- Tênis On Running Cloudsolo Loewe Khaki Green Sand Verde (`tenis-on-running-cloudsolo-loewe-khaki-green-sand-verde`): +[best-seller--loewe-x-on-running] / -[-]
- Tênis On Running Cloudsolo Loewe Sand Turquoise Bege (`tenis-on-running-cloudsolo-loewe-sand-turquoise-bege`): +[best-seller--loewe-x-on-running] / -[-]
- Tênis On Running Cloudsolo Loewe White Light Grey Cinza (`tenis-on-running-cloudsolo-loewe-white-light-grey-cinza`): +[best-seller--loewe-x-on-running] / -[-]
- Tênis On Running Cloudtilt Loewe Denim Blue Azul (`tenis-on-running-cloudtilt-loewe-denim-blue-azul`): +[best-seller--loewe-x-on-running] / -[-]
- Tênis On Running Cloudtilt Loewe Denim Grey Cinza (`tenis-on-running-cloudtilt-loewe-denim-grey-cinza`): +[best-seller--loewe-x-on-running] / -[-]

## Risco
- Write externo em Shopify: tags de produtos e lógica de badge do tema.
- Requer readback após aplicação para confirmar tags no Admin/API.

## Bloqueio
- Nenhum bloqueio técnico identificado no preview.

## Rollback
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260530T202803Z/rollback-snapshot.json`
- Restaurar `current_tags` por product id usando o mesmo script em modo rollback, ou aplicar manualmente o snapshot.

## Próxima decisão
- Se o preview estiver ok, executar `--apply` e validar readback dos produtos alterados.