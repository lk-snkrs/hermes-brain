# Public cache recheck — ASICS GT-2160 + Wales Bonner

Data UTC: 20260608T143603Z

## Escopo
- Modo: read-only public PDP cache QA.
- Writes externos: `0`.
- Fonte esperada: `areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-asics-gt2160-walesbonner-github-merge-20260608T0125Z/receipt.md`.
- Markers esperados: `top30-asics-gt-2160-regular` e `top30-adidas-wales-bonner-samba`.

## Resultado por PDP
- ASICS White Putty: OK
  - URL: https://lksneakers.com.br/products/tenis-asics-gt-2160-white-putty-branco
  - HTTP 200: 5/5
  - marker `top30-asics-gt-2160-regular` presente: 5/5 counts=[1, 1, 1, 1, 1]
  - classes canônicas presentes: 5/5
  - Cloudflare/challenge-like: 0/5
- ASICS JJJJound: OK
  - URL: https://lksneakers.com.br/products/tenis-asics-gt-2160-x-jjjound-white-branco
  - HTTP 200: 5/5
  - marker `top30-asics-gt-2160-regular` presente: 5/5 counts=[1, 1, 1, 1, 1]
  - classes canônicas presentes: 5/5
  - Cloudflare/challenge-like: 0/5
- Adidas Wales Bonner Wonder White: OK
  - URL: https://lksneakers.com.br/products/tenis-adidas-samba-x-wales-bonner-wonder-white-marrom
  - HTTP 200: 5/5
  - marker `top30-adidas-wales-bonner-samba` presente: 5/5 counts=[1, 1, 1, 1, 1]
  - classes canônicas presentes: 5/5
  - Cloudflare/challenge-like: 0/5
- Adidas Wales Bonner Wonder Clay Royal: OK
  - URL: https://lksneakers.com.br/products/tenis-adidas-samba-x-wales-bonner-wonder-clay-royal-bege
  - HTTP 200: 5/5
  - marker `top30-adidas-wales-bonner-samba` presente: 5/5 counts=[1, 1, 1, 1, 1]
  - classes canônicas presentes: 5/5
  - Cloudflare/challenge-like: 0/5

## Veredito
- Geral: `OK`.
- Nenhum Shopify/theme/Admin/GitHub write foi executado.

JSON: `qa.json`
