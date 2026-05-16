# LK GMC source governance investigation — 2026-05-14

Generated: `2026-05-14T21:52:54.913308+00:00`

Status: `approved_read_only_investigation_complete`

## Escopo aprovado
- Opção 1 escolhida por Lucas: investigar governança de fontes sem write/settings change.
- Nenhuma alteração em Merchant, Shopify, Tiny, feed, campanhas ou mensagens.

## Achados principais
- DataSources list status: `200`; count: `4`.
- Content API datafeeds list status: `200`.
- Automatic price updates effective: `True`.
- Shopify app installations exposed by token: `0`; Google/feed-like candidates: `[]`.
- Shopify publications exposed: `['Online Store', 'Facebook & Instagram', 'Google & YouTube', 'Point of Sale', 'Linktree', 'Pinterest', 'TikTok', 'Attentive']`.

## Shopify Google & YouTube sample evidence

Sample read-only by SKU:
- `01424-002-2`: Shopify price `8999.99`, compare-at `None`, status `ACTIVE`, Google & YouTube published `True`.
- `553558140-7`: Shopify price `1799.99`, compare-at `1599.99`, status `ACTIVE`, Google & YouTube published `True`.
- `AQ9129-170-5`: Shopify price `2749.99`, compare-at `2449.90`, status `ACTIVE`, Google & YouTube published `True`.
- `AQ9129-170-7`: Shopify price `3349.99`, compare-at `2449.90`, status `ACTIVE`, Google & YouTube published `True`.
- `AQ9129-170-9`: Shopify price `3349.99`, compare-at `2449.90`, status `ACTIVE`, Google & YouTube published `True`.
- `GW3773-39`: Shopify price `3799.99`, compare-at `1699.99`, status `ACTIVE`, Google & YouTube published `True`.

Interpretation: sampled stale-price/landing SKUs are active and published to Google & YouTube with current Shopify commercial values. This points the next check to the Google & YouTube channel/feed sync that generates or refreshes Merchant DS `10636492695`, not to repeating Merchant price PATCH.

## Interpretação
- Primary online DS 10636492695 is the intended API ProductInputs owner, but final product readbacks remain stale after price PATCH; investigate the upstream app/job/channel that writes this data source, not the PATCH endpoint alone.
- Automatic price updates are effective and should remain enabled until upstream ownership is fixed; they are a safety net, not the primary source of truth.
- Shopify app installation query did not expose a confirmed Google/feed app with the current token/scope; Merchant UI / Shopify apps UI remains needed for final ownership confirmation.

## Próximo gate recomendado
- Preparar **packet de UI/source ownership**: screenshots/export read-only no Merchant Center e Shopify Apps/Google channel para confirmar quem regenera DS `10636492695`.
- Depois disso, escolher: (A) corrigir/upstream resync da fonte API; (B) limitar/autofeed com rollback; (C) experimento temporário de settings em coorte minúscula. Nenhuma opção executada agora.

## Not performed
- Merchant/ProductInputs/Content API write
- data source update/delete
- automatic item update setting change
- feed upload/fetchNow
- Shopify write/app config change
- Tiny write
- campaign/send/contact
