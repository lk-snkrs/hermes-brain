# LK Growth — Ahrefs Wave 2 recheck 12h

- Data UTC: `20260619T115152Z`
- Escopo: read-only; writes externos = 0; estoque consultado = false; values_printed=false
- Diretório: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-wave-facets-orphans-external-20260618/recheck-12h-20260619T115152Z`

## Status dos conectores
- Ahrefs API: indisponível; project_id=None; issues_live=0
- SEMrush API smoke: HTTP 200; usable=True; SemrushBot bloqueado no robots.txt=True.

## Veredito por bloco
1. Page has links to broken page — Ahrefs live indisponível; baseline 7829; validação pública/read-only usada. Public check de collections/facets: 12 URLs, product hrefs com `_pos/_fid/_ss/variant` = 0.
2. More than three parameters in URL — Ahrefs live indisponível; baseline 976; validação pública/read-only usada. Validação pública confirma causa raiz do card corrigida: bad param product hrefs = 0.
3. Orphan pages — Ahrefs live indisponível; baseline 219; validação pública/read-only usada. Shopify read-only amostra PDP: found=20/20, ACTIVE=20, publicadas=20, com collections=20.
4. Canonical URL has no incoming internal links — Ahrefs live indisponível; baseline 98; validação pública/read-only usada. Na amostra, links canônicos encontrados em collection pública para 0/20; restante tende a depender de paginação/lazy grid/recrawl ou collections não amostradas.
5. External 4XX / 3XX — 4XX: Ahrefs live indisponível; baseline 15; validação pública/read-only usada. 3XX: Ahrefs live indisponível; baseline 6; validação pública/read-only usada. Origins públicos rechecados=11; href exato problemático restante=3.

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
- Confirmado corrigido publicamente: product-card canonical hrefs em collections/filtros; external href exato problemático removido dos origins rechecados.
- Ainda em cache/recrawl: Ahrefs issue counts se o crawl/date atual ainda é o mesmo ou se os counts não caíram.
- Pendente real: PDPs da amostra sem link canônico encontrado nas collections públicas checadas precisam de recrawl/paginação/collection membership mais profunda antes de qualquer write.
- Falso positivo/limitação: SEMrush pode acusar crawler bloqueado por `robots.txt`; isso não prova erro de storefront.

## Próximo passo
- Rodar novo Ahrefs Site Audit/crawl ou aguardar recrawl; se os mesmos 5 issues persistirem com crawl pós-fix, gerar pacote P1 com URLs remanescentes reais. Sem write executado neste job.
