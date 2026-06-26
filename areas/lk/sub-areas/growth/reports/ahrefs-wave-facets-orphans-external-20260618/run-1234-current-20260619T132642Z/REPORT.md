# LK Growth — Recheck Ahrefs + storefront atual

- Data UTC: `2026-06-19T13:26:59.333685+00:00`
- Escopo: read-only; values_printed=false

## Ahrefs issues
- Page has links to broken page: crawled=7829, new=7829, change=7829, added=0, removed=0, missing=0
- More than three parameters in URL: crawled=976, new=976, change=976, added=0, removed=0, missing=0
- Orphan page (has no incoming internal links): crawled=0, new=0, change=0, added=0, removed=0, missing=0
- Canonical URL has no incoming internal links: crawled=98, new=98, change=98, added=0, removed=0, missing=0
- External 4XX: crawled=15, new=15, change=15, added=0, removed=0, missing=0
- External 3XX redirect: crawled=6, new=6, change=6, added=0, removed=0, missing=0

## Storefront público — product href params
- https://lksneakers.com.br/collections/nike-dunk?filter.v.option.tamanho=44: status=200; product_hrefs=58; bad_param_hrefs=0
- https://lksneakers.com.br/collections/adidas-samba: status=200; product_hrefs=51; bad_param_hrefs=0
- https://lksneakers.com.br/collections/sneakers: erro <HTTPError 503: 'Service Unavailable'>
- https://lksneakers.com.br/collections/new-balance-204l: status=200; product_hrefs=27; bad_param_hrefs=0
- https://lksneakers.com.br/collections/onitsuka-tiger: status=200; product_hrefs=56; bad_param_hrefs=0
- https://lksneakers.com.br/collections/asics: status=200; product_hrefs=37; bad_param_hrefs=0

## Interpretação preliminar
- Se Ahrefs manteve contagens e storefront segue com bad_param_hrefs=0, tratar como recrawl/cache até novo crawl completo.
- External links serão validados/corrigidos em etapa separada.