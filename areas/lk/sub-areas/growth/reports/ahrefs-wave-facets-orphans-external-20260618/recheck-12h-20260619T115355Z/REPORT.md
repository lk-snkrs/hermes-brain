# LK Growth — Ahrefs Wave 2 recheck 12h

- Data UTC: `20260619T115355Z`
- Escopo: read-only; writes externos = 0; estoque consultado = false; values_printed=false
- Diretório: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-wave-facets-orphans-external-20260618/recheck-12h-20260619T115355Z`

## Status dos conectores
- Ahrefs API: OK; project_id=9609836; issues_live=6
- Ahrefs project snapshot sanitizado: `{"project_id": "9609836", "status": "Completed"}`
- SEMrush API smoke: HTTP 200; usable=True; SemrushBot bloqueado no robots.txt=True.

## Veredito por bloco
1. Page has links to broken page — Ahrefs ainda mostra 7829 (baseline 7829); provável sem recrawl útil pós-fix se crawl/date não avançou. Public check de collections/facets: 12 URLs, product hrefs com `_pos/_fid/_ss/variant` = 0.
2. More than three parameters in URL — Ahrefs ainda mostra 976 (baseline 976); provável sem recrawl útil pós-fix se crawl/date não avançou. Validação pública confirma causa raiz do card corrigida: bad param product hrefs = 0.
3. Orphan pages — Ahrefs ainda mostra 219 (baseline 219); provável sem recrawl útil pós-fix se crawl/date não avançou. Shopify read-only amostra PDP: found=20/20, ACTIVE=20, publicadas=20, com collections=20.
4. Canonical URL has no incoming internal links — Ahrefs ainda mostra 98 (baseline 98); provável sem recrawl útil pós-fix se crawl/date não avançou. Na amostra, links canônicos encontrados em collection pública para 0/20; restante tende a depender de paginação/lazy grid/recrawl ou collections não amostradas.
5. External 4XX / 3XX — 4XX: Ahrefs ainda mostra 15 (baseline 15); provável sem recrawl útil pós-fix se crawl/date não avançou. 3XX: Ahrefs ainda mostra 6 (baseline 6); provável sem recrawl útil pós-fix se crawl/date não avançou. Origins públicos rechecados=11; href exato problemático restante=2.

## SEMrush/CNRUSH + robots
- SEMrush API key está presente/injetada neste processo e smoke read-only retornou status sem imprimir valores.
- Não há export Site Audit/CNRUSH disponível neste run; portanto insights SEMrush ficam limitados a smoke + validação pública.
- `robots.txt` ainda bloqueia `SemrushBot`; qualquer erro SEMrush de crawl deve ser separado de erro real de HTML/canonical/link.

## EAN/GTIN — trilha separada Merchant/Product Data
- Shopify barcode read-only: produtos ativos checados=1000; variantes=7493; barcode válido por comprimento=4596; sem barcode=2897; inválido por comprimento=0; missing_rate=38.66%
- Interpretação: não é issue Ahrefs/SEMrush de crawl; é fila separada GMC/Product Data. Não preencher GTIN/EAN em massa sem fonte confiável.

## Evidências públicas
| URL | status | product hrefs | bad param hrefs |
|---|---:|---:|---:|
| https://lksneakers.com.br/collections/nike-dunk?filter.v.option.tamanho=44 | 200 | 58 | 0 |
| https://lksneakers.com.br/collections/adidas-samba | 200 | 51 | 0 |
| https://lksneakers.com.br/collections/sneakers | 200 | 59 | 0 |
| https://lksneakers.com.br/collections/sneakers?filter.v.option.tamanho=42%2F3 | 200 | 5 | 0 |
| https://lksneakers.com.br/collections/comme-des-garcons?filter.v.option.tamanho=37 | 200 | 7 | 0 |
| https://lksneakers.com.br/collections/nike-todos-os-modelos?filter.v.option.tamanho=40%2F40.5 | 200 | 9 | 0 |
| https://lksneakers.com.br/collections/new-balance-204l | 200 | 27 | 0 |
| https://lksneakers.com.br/collections/onitsuka-tiger | 200 | 56 | 0 |
| https://lksneakers.com.br/collections/asics | 200 | 37 | 0 |
| https://lksneakers.com.br/collections/nike-air-jordan | 404 | 11 | 0 |
| https://lksneakers.com.br/collections/adidas-originals | 404 | 11 | 0 |
| https://lksneakers.com.br/collections/salomon | 404 | 11 | 0 |

## Classificação
- Confirmado corrigido publicamente: product-card canonical hrefs em collections/filtros — 12 URLs checadas, 0 hrefs de produto com `_pos/_fid/_ss/variant`.
- Ainda em cache/recrawl: Ahrefs issue counts seguem iguais ao baseline, com crawl do projeto ainda pós-fix não comprovado; precisa novo crawl/recrawl para limpar histórico.
- Pendente real externo: restaram 2 hrefs exatos problemáticos no origin `https://lksneakers.com.br/pages/guia-salomon-xt-6` (`hypebeast.com/search?s=salomon%20xt-6` e `https://www.salomon.com/`).
- Pendente/limitação orphan-canonical: PDPs da amostra existem, estão ACTIVE/publicados e têm collections no Shopify; a presença do link canônico não apareceu na primeira página HTML das collections amostradas, então depende de paginação/lazy grid/recrawl ou investigação mais profunda antes de qualquer write.
- Falso positivo/limitação: SEMrush pode acusar crawler bloqueado por `robots.txt`; isso não prova erro de storefront.

## Próximo passo
- Rodar novo Ahrefs Site Audit/crawl ou aguardar recrawl; se os mesmos 5 issues persistirem com crawl pós-fix, gerar pacote P1 com URLs remanescentes reais. Sem write executado neste job.
