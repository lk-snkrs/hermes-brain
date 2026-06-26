# P0 Samba Redirect Receipt

Data UTC: 2026-06-18T21:36:28Z

## Aprovação

- Aprovação recebida no Telegram: "Aprovo" em resposta ao pedido de criar o redirect Samba.

## Executado

- Shopify URL redirect criado.
- De: `/collections/samba-duplicata-backup-20260616`
- Para: `/collections/adidas-samba`
- Redirect ID: `491197071582`
- values_printed=false.

## Readback Shopify Admin

- Pre-existing redirects para path exato: 0.
- Create HTTP status: 201.
- Readback HTTP status: 200.
- Readback exato path + target: OK.

## Verificação pública

- `https://lksneakers.com.br/collections/samba-duplicata-backup-20260616` → HTTP 301 → `/collections/adidas-samba`.
- `https://lksneakers.com.br/collections/adidas-samba` → HTTP 200.
- Cadeia completa a partir de `https://www.lksneakers.com.br/collections/samba-duplicata-backup-20260616` termina em `https://lksneakers.com.br/collections/adidas-samba` com HTTP 200.

## Rollback

- Remover redirect ID `491197071582` no Shopify Admin se necessário.
