# LKGOC Contract Lock — Salomon XT-6

Criado em: 2026-06-15T14:47:45Z
Status: DEV_BUILD_ALLOWED / PRODUCTION_BLOCKED

## Gold source collection
- New Balance 204L LKGOC — padrão aprovado por Lucas.
- DEV theme validado historicamente: `lk-new-theme/dev`, id `155065450718`, role `unpublished`.
- Copiar: hierarquia, densidade editorial, shell escuro premium, kicker, hero editorial, product-first mobile, grid antes do guia, guide panel pós-grid.
- Não mudar: arquitetura visual, FAQ única, comportamento mobile/desktop, ordem hero → grid → guia.
- Pode mudar: texto, imagens, links, produtos, nuances comerciais da Salomon XT-6.

## Gold source guia
- Guia LK em `/pages`, usando `sections/lk-goc-guide-v1.liquid` e templates existentes de guia LKGOC como padrão.
- Não criar artigo simples ou bloco longo dentro da collection.

## Media manifest — status inicial
- Necessário: imagem editorial/lifestyle/on-foot para hero da collection e guia.
- Packshot/GOAT/PDP só pode apoiar produto, não hero LKGOC.
- Status agora: `PENDING_RESEARCH`; DEV pode usar placeholder explícito, Production bloqueado até asset aprovado.

## Acceptance tests
- API readback collection/page/theme DEV.
- Preview DEV/unpublished da collection e guia.
- Screenshot mobile/desktop da 204L e Salomon lado a lado.
- Provar: hero não packshot em Production, grid antes do guia, guia pós-grid, FAQ única, sem Liquid error, links collection↔guia funcionando.

## Escopo de write permitido agora
- DEV/unpublished theme: permitido pelo fluxo LKGOC.
- Shopify production/main/customer-facing: proibido sem approval.
- Publicar collection/page/produtos: proibido sem approval.
