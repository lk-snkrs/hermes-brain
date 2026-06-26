# LK Growth — External broken links audit — 2026-06-19

- Pedido: seguir com auditoria dos broken external links do SEMrush.
- Modo: read-only; nenhum write em Shopify production foi executado.
- values_printed=false.

## Resumo

- Páginas auditadas: 177
- Pares source→external link: 409
- Targets externos únicos: 48
- Candidatos quebrados por crawler: 20 pares / 18 targets
- Quebrados confirmados 404: 3 pares / 3 targets
- Bot/manual verify: 16 pares
- Timeout/manual verify: 1 pares

## Quebrados confirmados e ação proposta

- Source: `https://lksneakers.com.br/products/tenis-nike-x-skims-rift-mesh-light-bone-bege`
  - Target 404: `https://www.aimeleondore.com/products/unisphere-label-hat`
  - Anchor: `Aimé Leon Dore`
  - Status: `404`
- Source: `https://lksneakers.com.br/products/tenis-nike-x-skims-rift-mesh-light-bone-bege`
  - Target 404: `https://poshmark.com/listing/Aime-Leon-Dore-ALD-Unisphere-Baseball-Cap-Snapback-Hat-Faded-68d6de3ca7e260bc2765236a`
  - Anchor: `Poshmark`
  - Status: `404`
- Source: `https://lksneakers.com.br/blogs/novidades/feid-x-salomon-xt-4-og-ferxxocalipsis-o-drop-latino-que-mudou-o-jogo-em-2026`
  - Target 404: `https://www.salomon.com`
  - Anchor: `Salomon Technical Specs`
  - Status: `404`

Ação proposta no único PDP afetado:
- Produto: `Tênis Nike x Skims Rift Mesh "Light Bone" Bege` (`tenis-nike-x-skims-rift-mesh-light-bone-bege`)
- Trocar `https://www.aimeleondore.com/products/unisphere-label-hat` por `https://www.aimeleondore.com/products/unisphere-hat`.
- Remover a citação/link morto do Poshmark do body do produto.

## Itens classificados como falso positivo / manual verify

- Instagram: retornou `429` por rate-limit/login/anti-bot. Não tratar como broken sem validação manual; links parecem normais.
- StockX, adidas.com.br e Reclame Aqui: retornaram `403`, típico de bloqueio anti-bot. Não remover automaticamente.
- Salomon: HEAD/crawler marcou problema, mas fetch em browser retornou conteúdo OK. Não corrigir.
- McKinsey: timeout na validação automática. Classificar como manual verify, não write automático.

## Approval necessário para write

Para aplicar o patch visível no PDP, precisa aprovação explícita de Lucas:

`APROVADO aplicar patch broken external links no produto Nike x Skims Rift Mesh Light Bone`

## Arquivos

- Raw JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/external-broken-links-20260619/external-link-audit-raw.json`
- Raw CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/external-broken-links-20260619/external-link-audit-raw.csv`
- Shopify location: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/external-broken-links-20260619/shopify-location-true-404.json`
- Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/external-broken-links-20260619/approval-packet-product-broken-links.json`
- Diff preview: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/external-broken-links-20260619/proposed-product-body.diff`
