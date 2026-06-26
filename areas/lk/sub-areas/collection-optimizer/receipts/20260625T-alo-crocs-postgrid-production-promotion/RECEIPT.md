# Receipt — Production promotion LKGOC pós-grid Alo Yoga + Crocs McQueen

Data: 2026-06-25  
Agente: `[LK] Otimização de Coleções` / LKGOC  
Aprovação: Lucas aprovou explicitamente a promoção para production/main no Telegram.  
Resultado: **PASS**  
Rollback executado: **não**  
values_printed: false

## Escopo aprovado

Promover para production/main a correção LKGOC pós-grid validada no DEV `lk-new-theme/dev` (`theme_id=155065450718`), limitada a:

- `sections/lk-collection.liquid`
- `snippets/lk-goc-collection.liquid`

Fora do escopo e não alterado:

- preço;
- estoque;
- produtos/variantes;
- ordenação;
- GMC;
- Klaviyo;
- campanhas;
- checkout.

## Temas verificados

| Tema | ID | Nome | Role |
|---|---:|---|---|
| DEV fonte | 155065450718 | `lk-new-theme/dev` | `unpublished` |
| Production alvo | 155065417950 | `lk-new-theme/production` | `main` |

## Writes externos realizados

Shopify Theme Assets — production/main:

| Asset | Backup | Fonte DEV | Upload | Readback |
|---|---:|---:|---:|---|
| `sections/lk-collection.liquid` | 262049 bytes | 261457 bytes | HTTP 200 | match DEV |
| `snippets/lk-goc-collection.liquid` | 174144 bytes | 176644 bytes | HTTP 200 | match DEV |

## QA público após promoção

| Handle | HTTP | H1 | FAQPage | Guia | Bloco citável | Liquid error | Pós-grid |
|---|---:|---:|---:|---:|---:|---:|---|
| `alo-yoga-1` | 200 | 1 | 1 | 1 | 1 | não | PASS |
| `crocs-mcqueen` | 200 | 1 | 1 | 1 | 1 | não | PASS |
| `new-balance-204l` benchmark | 200 | 1 | 1 | 2 | 1 | não | PASS basic |

### Posições públicas verificadas

- Alo Yoga: `Ordenar:` 2953 → `Mostrando 24 de` 7856 → `Guia editorial LK` 7890
- Crocs McQueen: `1 itens` 2944 → `Ordenar:` 2952 → `Guia editorial LK` 3419

## Screenshots mobile

- `prod-after-alo-mobile.png`
- `prod-after-crocs-mobile.png`
- `prod-after-204l-mobile.png`

## Rollback

Rollback pronto, mas **não executado** porque QA passou:

`rollback_prod_theme_assets.py`

Backups production antes da promoção:

- `backup-prod-before-sections__lk-collection.liquid`
- `backup-prod-before-snippets__lk-goc-collection.liquid`

## Observação

A correção definitiva foi feita no tema/section pós-grid, não em `collection.descriptionHtml`, porque a tentativa anterior via descriptionHtml quebrava a hierarquia produto-first.
