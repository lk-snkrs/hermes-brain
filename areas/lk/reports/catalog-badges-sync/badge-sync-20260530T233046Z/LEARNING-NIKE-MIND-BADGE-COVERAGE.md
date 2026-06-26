# Learning — Nike Mind sem Best Seller

Data: 2026-05-30

## Problema

A coleção `nike-mind-001` não exibia badges `BEST SELLER`, embora tivesse produtos elegíveis e vendidos.

## Causa raiz

O script `lk_catalog_badges_sync_20260528.py` estava mirando apenas coleções encontradas nos menus `main-menu`, `mega-menu-c-pia-1` e `mega-menu-mobile`.

Como `nike-mind-001` estava fora desse escopo, o sync global não adicionava `best-seller--nike-mind-001`. Além disso, a rotina full removia tags `best-seller--*` gerenciadas que não estivessem no escopo processado.

## Correção técnica

O script foi ajustado para que o sync default use `target_source = all_manual_collections`, alinhando badges à automação de ordenação de todas as coleções manuais. O modo `--collection-handles` continua disponível para reparos pontuais preservando tags fora do escopo.

Arquivo alterado:

- `/opt/data/hermes_bruno_ingest/scripts/lk_catalog_badges_sync_20260528.py`

## Execução aprovada

Lucas aprovou via Telegram/clarify: `Aplicar todas as coleções manuais (preview: 353 produtos)`.

Execução:

- `python3 /opt/data/hermes_bruno_ingest/scripts/lk_catalog_badges_sync_20260528.py --apply`
- Resultado: `updated = 353`
- Target: 140 coleções manuais
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260530T233046Z/receipt.json`

## Verificações

- Preview pós-apply scoped para `nike-mind-001`: `products_changed = 0`
- Nike Mind top elegível: 6 produtos com `storefront_available = True` e `best_seller_eligible = True`
- Invariantes do snapshot aplicado: `top8_oos_or_ineligible_violations = 0`

## Regra durável

Badges `BEST SELLER` por coleção devem cobrir todas as coleções manuais/visíveis relevantes, não apenas coleções do menu. Produtos esgotados continuam inelegíveis para Best Seller.
