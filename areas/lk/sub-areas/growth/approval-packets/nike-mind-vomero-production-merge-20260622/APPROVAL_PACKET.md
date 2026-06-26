# Production Merge Approval Packet — Nike Mind/Vomero schema dedupe — 2026-06-22

**Status:** packet preparado; **produção ainda não foi alterada**.  
**Gerado em:** 2026-06-22T16:55:42.925992+00:00  
**Origem:** Lucas respondeu “Aprovo” após DEV preview OK. Interpretação segura: preparar merge packet; não executar produção sem aprovação escopada explícita.  
**values_printed:** false.

## 1. O que já foi validado no DEV

Theme DEV: `lk-new-theme/dev` — `155065450718`.

Preview QA:

| Página | HTTP | H1 | FAQPage | Legacy duplicado | Liquid error |
|---|---:|---:|---:|---|---|
| `/collections/nike-mind-001?preview_theme_id=155065450718` | 200 | 1 | 1 | removido | False |
| `/pages/guia-nike-mind-001-002?preview_theme_id=155065450718` | 200 | 1 | 1 | removido | False |
| `/collections/nike-vomero-premium?preview_theme_id=155065450718` | 200 | 1 | 1 | removido | False |

## 2. Assets propostos para merge production

Aplicar no production theme `lk-new-theme/production` somente os mesmos 4 snippets validados no DEV:

1. `snippets/lk-growth-nike-mind-seo-geo-preview.liquid`
   - Desativar bloco legado Nike Mind que duplicava visual/schema.
2. `snippets/lk-growth-geo-faq-schema.liquid`
   - Desativar apenas o branch de FAQ schema duplicado do Vomero collection.
   - Preservar os demais branches de GEO FAQ schema.
3. `snippets/lk-nike-mind-guide-panel.liquid`
   - Remover painel visual duplicado; manter 1 FAQPage canônico para collection Nike Mind.
4. `snippets/lk-goc-nike-vomero-premium-guide-panel.liquid`
   - Remover painel visual duplicado; manter 1 FAQPage canônico para collection Vomero.

## 3. Fora do escopo

Não alterar:

- produtos;
- collection sort/ordenação;
- preço;
- estoque/disponibilidade;
- desconto;
- PDPs Mind 001;
- PDP Vomero;
- checkout;
- GMC/feed;
- Google/Meta Ads;
- Klaviyo/WhatsApp;
- theme publish;
- qualquer asset fora dos 4 snippets listados.

## 4. Risco

- **Baixo/médio**: altera snippets production, mas o comportamento foi validado em DEV.
- **Risco visual controlado**: remove blocos duplicados e deixa o conteúdo de collection body como fonte visual canônica.
- **Risco schema controlado**: objetivo é reduzir múltiplos FAQPage para 1 por página.
- **Rollback simples**: restaurar os 4 snippets de backup production.

## 5. Plano de execução se aprovado

1. Backup production dos 4 snippets.
2. Aplicar exatamente o conteúdo validado no DEV aos 4 snippets production.
3. Readback asset-by-asset.
4. QA público production:
   - `/collections/nike-mind-001`: HTTP 200, H1 1, FAQPage 1, sem legacy duplicado, sem Liquid error.
   - `/pages/guia-nike-mind-001-002`: HTTP 200, H1 1, FAQPage 1, sem legacy duplicado, sem Liquid error.
   - `/collections/nike-vomero-premium`: HTTP 200, H1 1, FAQPage 1, sem legacy duplicado, sem Liquid error.
5. Criar receipt e manter rollback script.
6. Impact review D+7/D+14 já registrado junto ao cleanup.

## 6. Rollback

- Backup DEV já existe em:  
  `growth/work/nike-mind-vomero-theme-dedupe-dev-20260622/dev-theme-backup-before/`
- Para production merge, antes de executar será criado backup production em:  
  `growth/work/nike-mind-vomero-production-merge-20260622/production-backup-before/`
- Rollback production será scriptado para restaurar os 4 snippets originais.

## 7. Aprovação necessária para executar produção

Para aplicar em production, preciso da aprovação escopada abaixo:

> Aprovo aplicar no **Shopify production theme `155065417950`** somente o merge dos 4 snippets validados no DEV para deduplicar schema/blocos de Nike Mind e Vomero, sem mexer em produtos, preço, estoque, ordenação, descontos, PDPs, GMC/feed, campanhas, Klaviyo/WhatsApp, checkout, theme publish ou qualquer asset fora dos 4 listados, com backup, readback, QA público e rollback.

