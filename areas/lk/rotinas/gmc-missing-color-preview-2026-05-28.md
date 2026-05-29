# LK GMC — Missing color preview packet — 2026-05-28

Modo: `preview/read-only`; nenhum feed/ProductInput/Shopify write executado.

Total com `missing_item_attribute_for_product_type`: `1105`

| Confiança | Linhas |
|---|---:|
| high | 795 |
| medium | 0 |
| needs_human_review | 310 |

## Amostra high-confidence

| offerId | cor sugerida | título | evidência |
|---|---|---|---|
| `1201A789-020-41` | `Preto` | Tênis ASICS Gel-NYC Graphite Grey Black Preto | color term in title: Preto |
| `PERI049-1007` | `Preto` | Óculos de Sol Palm Angels PERI049-1007 Preto | color term in title: Preto |
| `DD0587-002-43` | `Cinza` | Tênis Jordan 5 Retro Wolf Grey (2026) Cinza | color term in title: Cinza |
| `1201A789-020-39` | `Preto` | Tênis ASICS Gel-NYC Graphite Grey Black Preto | color term in title: Preto |
| `IQ8055 100-35` | `Branco` | Tênis Nike Air Jordan 4 OG SP x Nigel Sylvester Brick After Brick Branco | color term in title: Branco |
| `ALO-2441950-39` | `Rosa` | Tênis Alo Yoga Alo Runner Pink Rosa | color term in title: Rosa |
| `3MG10844970-40` | `Verde` | Tênis On Running x Kith ON K-Tech 2 Spirulina Barley Verde | color term in title: Verde |
| `YZY-2566238-43` | `Marrom` | Tênis Adidas Yeezy Boost 350 V2 Earth Marrom | color term in title: Marrom |
| `FZ5042-041-44` | `Azul` | Tênis Nike Air Jordan 1 Low SE Repaired Denim Swoosh Azul | color term in title: Azul |
| `OXV-3513694-405` | `Azul` | Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Blue Azul | color term in title: Azul |
| `ALO-2441950-43` | `Rosa` | Tênis Alo Yoga Alo Runner Pink Rosa | color term in title: Rosa |
| `U204L4HH-42` | `Cinza` | Tênis New Balance 204L Raincloud Ash Wood Cinza | color term in title: Cinza |

## Approval packet

- Ação proposta: aplicar `color` apenas em linhas `high` após revisão humana do CSV.
- Superfície sugerida: supplemental feed/ProductInput, escolhendo a menor superfície reversível ativa para LK.
- Risco: cor inferida errada pode degradar Shopping; linhas `medium` e `needs_human_review` ficam bloqueadas até curadoria.
- Rollback: snapshot dos valores anteriores e remoção/sobrescrita do atributo no mesmo surface.
- Validação: Merchant itemLevelIssue deve cair após reprocessamento; revisão D+7.

CSV: `reports/lk-gmc-missing-color-preview-2026-05-28.csv`
