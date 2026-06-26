# Curadoria LK — Sales Signal Read-only
Generated at: `2026-06-02T12:42:00.263100+00:00`
## Escopo
- Read-only: Shopify Admin Orders API + public product JS.
- Nenhum write externo, nenhum upload de tema, nenhum segredo impresso.
- Janela live: 180 dias.
## Freshness
- Shopify live orders lidos: `2762` pedidos em `12` páginas.
- SQLite local existe, mas está stale para vendas atuais: max order `2026-04-16T20:13:58+00:00`.
## Ranking live por grupo

### samba_jane
1. Tênis Adidas Samba Jane 'White Black' Branco — qty `7`, orders `6`, last `2026-05-31T16:12:07-03:00`
2. Tênis Adidas Samba Jane White Blue Gum Branco — qty `5`, orders `5`, last `2026-05-23T15:33:20-03:00`
3. Tênis Adidas Samba Jane 'Scarlet Gum' Vermelho — qty `3`, orders `3`, last `2026-04-28T15:48:08-03:00`
4. Tênis Adidas Samba Jane 'Black White Gum' Preto — qty `3`, orders `3`, last `2026-05-23T15:33:20-03:00`
5. Tênis Adidas Samba Jane Green White Gum Verde — qty `2`, orders `2`, last `2026-02-17T09:45:55-03:00`
6. adidas-samba-jane-cream-black-gum — `missing_public_js`

### aj1_low_regular
1. Tênis Nike Air Jordan 1 Low Vintage Grey Cinza — qty `3`, orders `3`, last `2026-04-30T17:25:56-03:00`
2. Tênis Nike Air Jordan 1 Low Midnight Navy Wolf Grey Azul Marinho — qty `2`, orders `2`, last `2026-03-30T05:47:11-03:00`
3. Tênis Nike Air Jordan 1 Low Jade Smoke Multicolor — qty `2`, orders `2`, last `2026-01-31T11:03:15-03:00`
4. Tênis Nike Air Jordan 1 Low Black Medium Grey Cinza — qty `1`, orders `1`, last `2025-12-18T17:48:29-03:00`
5. Tênis Nike Air Jordan 1 Low Taxi Amarelo — qty `1`, orders `1`, last `2026-01-21T17:10:57-03:00`
6. Tênis Nike Air Jordan 1 Low Light Smoke Grey Cinza — qty `0`, orders `0`, last `None`

### aj1_low_travis
1. Tênis Nike Air Jordan 1 Low Og Sp x Travis Scott Medium Olive Verde — qty `4`, orders `4`, last `2026-05-29T14:04:16-03:00`
2. Tênis Nike Air Jordan 1 Low Og Sp x Travis Scott Velvet Brown Marrom — qty `2`, orders `2`, last `2026-05-21T11:38:28-03:00`
3. Tênis Nike Travis Scott x Air Jordan 1 Low OG SP 'Black Phantom' Preto — qty `1`, orders `1`, last `2025-12-11T15:35:33-03:00`
4. Tênis Nike Travis Scott x Air Jordan 1 Low OG Reverse Mocha Bege — qty `0`, orders `0`, last `None`
5. Tênis Nike Air Jordan 1 Low Og Sp x Travis Scott Mocha — qty `0`, orders `0`, last `None`
6. Tênis Nike Travis Scott x Air Jordan 1 Low Og Canary Amarelo — qty `0`, orders `0`, last `None`

## Interpretação
- Para produção, usar filtro semântico/cápsula primeiro e ranking comercial dentro do grupo depois.
- Para produto atual, remover o próprio handle e pegar os próximos 5.
- Se o grupo tiver menos de 5 com venda recente, completar por curadoria/proximidade e marcar internamente como fallback, sem texto “best seller” no storefront.

## Próxima decisão
- Aprovar ou não upload no tema dev para reordenar previews existentes com base no ranking live 180d.
