# Approval Packet — Adidas Samba LKGOC Full DEV

Data UTC: 2026-06-02T23:50:05Z
Status: NÃO PUBLICADO / NÃO APLICADO EM PRODUÇÃO

## Nível LKGOC
Full — refactor/rewrite-from-zero de coleção estratégica com guia dedicado, pesquisa, DEV preview e scorecard.

## Input Contract
- Nome/modelo: Adidas Samba
- Handle coleção: adidas-samba
- Refactor: sim, REWRITE-FROM-ZERO; página atual usada apenas como inventário/evidência
- Referência visual coleção: New Balance 204L
- Referência guia dedicado: Nike x Jacquemus Moon Shoe
- Produtos incluídos: coleção Shopify com 96 produtos confirmados por GraphQL
- Produto âncora/famílias: Samba OG, Samba Jane, Sambae, Samba XLG + colorways/collabs detectadas no inventário
- URL coleção: /collections/adidas-samba
- Guia dedicado DEV: /pages/guia-adidas-samba?view=samba-guide-lkgoc-dev
- Tema DEV: 155065450718 — lk-new-theme/dev — role unpublished
- Dados ausentes: GSC/GA4/Shopify receita e Ahrefs não consultados nesta rodada; decisão comercial final não é decision-grade sem eles

## Evidence Packet resumido
- Inventário LK: 96 produtos na coleção adidas-samba; primeiros produtos incluem Samba OG Crochet Pack, Samba Jane Chalk White, Samba Disney 101 Dalmatians, Samba OG White Floral, Samba Jane White Blue Gum etc.
- DataForSEO: consultado keyword overview, search intent, SERP BR/pt e AI search volume para adidas samba, samba og, adidas samba feminino, sambae, samba jane e samba xlg.
- SERP: consultas BR/pt para adidas samba e adidas samba feminino; intenção mista comercial/informacional, com necessidade de comparação de versões e styling.
- Fontes oficiais/editoriais: adidas history/Samba hub + Vogue/GQ/Elle como contexto de história, tendência e styling. Guia V2 inclui bloco de fontes com links externos no padrão.
- Limitações: GSC, GA4, Ahrefs e dados de receita/conversão não foram integrados; isso reduz priorização, não invalida o DEV visual/copy.

## Shopify DEV / assets
- Tema: 155065450718 — lk-new-theme/dev — unpublished, previewable true, processing false.
- sections/lk-collection.liquid: atualizado no DEV; readback Admin API OK; sha b75740d901640102648509382f52038e742e9e84a004b1e65606d51255de3e48; bytes 253300.
- sections/lk-adidas-samba-source-page-v1.liquid: criado/atualizado no DEV; sha 59bb3eb9aeb2169ea8e141fba9522dcd79be7e8e7c356e557474f9d382e1a666; bytes 12025.
- templates/page.samba-guide-lkgoc-dev.json: criado no DEV; sha 18f4bd94687dca45a6a774ce215a81926c7ffd815eb08b7efbcb9e4e64decca3; bytes 142.
- templates/collection.samba-lkgoc-dev.json: criado no DEV para tentativa de preview; sha 8fff4599a884561323a9cfaca740546986707c7a71acc4d95b54e656bdb53286; bytes 163.
- Backup: receipts/shopify-dev-backups/samba-lkgoc-20260602T234452Z.

## Preview / QA
- Guia DEV renderizando: https://lksneakers.com.br/pages/guia-adidas-samba?view=samba-guide-lkgoc-dev
- Coleção DEV: asset confirmado via Admin API, mas preview público ainda cai/renderiza sem markers novos. URLs com preview_theme_id e view foram testadas e não exibiram a copy nova.
- Screenshots QA:
  - qa/2026-06-02-samba-lkgoc/204l-desktop.png
  - qa/2026-06-02-samba-lkgoc/204l-mobile.png
  - qa/2026-06-02-samba-lkgoc/samba-guide-dev-desktop-v2.png
  - qa/2026-06-02-samba-lkgoc/samba-guide-dev-mobile-v2.png

## Comparação visual com 204L
- Intenção implementada no Liquid: produto-first, grid antes do guia, bloco Guia Editorial LK pós-grid e CTA para guia completo.
- QA aprovado parcialmente: referência 204L desktop/mobile capturada; guia dedicado desktop/mobile capturado.
- Bloqueio: coleção Adidas Samba DEV ainda não pôde ser validada visualmente no storefront; por regra LKGOC, isso é drift/preview blocker, não pronto para production.

## Scorecard LKGOC
Score atual: 78/100 — não pronto para aprovação de produção.
- Visual coleção / padrão 204L: 12/20 — Liquid DEV patchado, mas preview público não validado.
- Guia dedicado / Moon Shoe: 13/15 — renderiza e V2 tem tabela/fontes; precisa QA final visual humano.
- Pesquisa/evidence: 11/15 — DataForSEO/SERP/fontes/inventário OK; falta GSC/GA4/Ahrefs.
- SEO/GEO/ecommerce: 13/15 — copy, FAQ, tabela, citabilidade e entidades fortes; schema precisa validar no HTML final da coleção.
- CRO/produto readiness: 8/10 — 96 produtos e variantes mapeadas; falta ordem/receita/conversão.
- FAQ/schema/citabilidade: 8/10 — FAQ e blocos citáveis criados; schema final depende do preview da coleção.
- QA visual desktop/mobile: 4/10 — guia capturado; coleção DEV bloqueada.
- Operação/rollback/approval: 6/10 — DEV/backup/readback OK; precisa resolver preview antes de pedir produção.

## Limitações / bloqueios
- O preview público da coleção /collections/adidas-samba não mostra o patch do tema DEV, embora o Admin API confirme o asset alterado.
- Possíveis causas: mecanismo/cookie de preview Shopify, cache/roteamento, template efetivo no storefront, ou restrição de preview para coleção.
- Sem validação visual da coleção no padrão 204L, não considerar pronto.

## Aprovação necessária
- Nenhuma aprovação pedida para produção agora.
- Próxima aprovação só depois de resolver preview e refazer QA coleção desktop/mobile comparando com 204L.
- Se Lucas aprovar depois: aplicar/copyar assets para produção ou publicar alteração correspondente, com rollback explícito e revisão de impacto em ~7 dias.
