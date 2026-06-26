# Approval packet — Salomon XT-6 next improvements

Data UTC: 20260626T093722Z

## Contexto verificado

Histórico recente consultado:
- receipts LKGOC/Salomon XT-6 em `collection-optimizer/work/salomon-xt6-lkgoc-20260615/`;
- report SEMrush/Growth em `growth/reports/semrush-ideas-execution-status-20260626.md`;
- readback público de collection, guia e 4 PDPs;
- SERP DataForSEO mobile BR para `salomon xt 6` e `tenis salomon xt 6`;
- GA4/GSC read-only snapshot salvo em `growth/reports/salomon-xt6/`;
- GMC read-only router.

## Fatos atuais

### Search/SERP
- Para `salomon xt 6`, LK aparece com PDP GORE-TEX na posição orgânica aproximada 6 / rank absoluto 9; collection ainda não aparece no top 20.
- Para `tenis salomon xt 6`, SERP tem bloco Shopping/popular products forte; LK não apareceu no top orgânico capturado.
- Concorrentes principais: Sunika, Droper, Farfetch, Salomon, Enjoei, Netshoes.

### GA4/GSC
- GSC 28 dias: 387 impressões / 4 cliques em queries Salomon.
- GA4 item-level 28 dias: 185 item views, 8 add-to-cart, 2 compras, R$ 4.799,98 item revenue.

### Público/SEO técnico
- Collection `/collections/salomon-xt-6`: indexável, canonical OK, meta description OK.
- Guia `/pages/guia-salomon-xt-6`: indexável, mas public title/description ainda não usam SEO metafields; description pública mostra texto ruim com `DEV`.
- PDPs: indexáveis e com Product schema; alguns shards de footer hub ainda propagando.
- Merchant: issue `image_link_internal_error` em Cloudburst `L49154600` ainda aparece no snapshot read-only, apesar de imagens antigas já terem sido restauradas HTTP 200; precisa próximo ciclo/propagação.

## Pacote proposto — executar em production com rollback

### A. Corrigir SEO title/meta do Guia Salomon XT-6 no theme layout
- Problema: `layout/theme.liquid` usa `page.metafields.global.description_tag` para description, mas não usa `page.metafields.global.title_tag` no `<title>`; em readback público o guia saiu como `Guia Salomon XT-6 | LK Sneakers` e description com `DEV`.
- Ação: patch escopado em `layout/theme.liquid` para páginas com `page.metafields.global.title_tag` usarem esse title antes de fallback.
- Ação específica para `guia-salomon-xt-6`: garantir description limpa pelos metafields já existentes.
- Impacto: CTR/qualidade SERP/GEO; remove risco reputacional de `DEV` público.
- Risco: baixo/médio por ser layout global; patch será condicional e backup será salvo.
- Rollback: restaurar `layout/theme.liquid` backup.

### B. Reforçar ligação PDP → Collection + Guia
- Problema: PDPs Salomon têm pouco/zero link para o guia; collection links aparecem, mas guia não.
- Ação: adicionar bloco escopado aos PDPs Salomon: `Ver coleção Salomon XT-6` + `Guia LK do Salomon XT-6`.
- Impacto: internal linking, crawl path, UX de decisão.
- Risco: médio por mexer em template PDP; preferir snippet escopado a `product.handle contains 'salomon-xt-6'`.
- Rollback: remover snippet/inclusão.

### C. Criar/ajustar FAQ schema do Guia
- Problema: PAA tem perguntas sobre preço, origem, fabricação, marca e GORE-TEX; o guia tem FAQ, mas precisamos validar JSON-LD limpo para AI/Search.
- Ação: FAQPage JSON-LD escopado ao guia, baseado no conteúdo visível; sem claims de disponibilidade/estoque.
- Impacto: AI visibility/PAA/GEO.
- Risco: baixo se refletir conteúdo visível.
- Rollback: remover snippet.

### D. GMC follow-up Cloudburst
- Problema: Merchant ainda aponta `image_link_internal_error` para Cloudburst `L49154600`.
- Ação agora: read-only e aguardar recrawl; se persistir, preparar packet de feed/Simprosys/Shopify product media. Nenhum feed write sem aprovação separada.

## Aprovação necessária

Aprovar execução production do pacote A+B+C:
- theme/layout write;
- PDP template/snippet write;
- FAQ schema write;
- backups + readback + receipt.

Sem tocar preço, estoque, desconto, campanhas, feed/GMC ou disponibilidade.

Reminder OS loop needed: yes
Reminder OS owner: lk-growth + lk-shopify if theme/PDP template execution proceeds
Reminder OS next action: with approval, apply scoped theme/snippet/schema patch and verify public readback.
Reminder OS review trigger: Lucas approves packet or 24h cache/GMC follow-up.
Reminder OS evidence: this packet + read-only snapshots listed above.
