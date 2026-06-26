# Approval Packet — Adidas Samba Canonical Consolidation

Gerado: 2026-06-16T20:17:03.526951+00:00

## Problema
Existem duas coleções Shopify públicas e indexáveis para o mesmo cluster Adidas Samba:

- `https://lksneakers.com.br/collections/samba`
- `https://lksneakers.com.br/collections/adidas-samba`

As duas retornam HTTP 200, têm canonical próprio e têm os mesmos 95 produtos. Isso dilui sinais de SEO/GEO em uma query transacional de alto volume.

## Evidência read-only
### Público / HTML
- `samba`: status=200; canonical=`https://lksneakers.com.br/collections/samba`; title=`Adidas Samba original | LK Sneakers`; products_raw=58; FAQ novo=False.
- `adidas-samba`: status=200; canonical=`https://lksneakers.com.br/collections/adidas-samba`; title=`Adidas Samba Original | LK Sneakers`; products_raw=58; FAQ novo=True.

### Shopify Admin
- `samba`: id=`gid://shopify/Collection/424590213342`; produtos=95; updatedAt=2026-06-15T14:44:33Z; SEO title=`Adidas Samba original | LK Sneakers`.
- `adidas-samba`: id=`gid://shopify/Collection/468244332766`; produtos=95; updatedAt=2026-06-16T20:04:43Z; SEO title=`Adidas Samba Original | LK Sneakers`.

### Sitemap / linkagem
- Sitemap de coleções contém as duas URLs.
- Homepage contém link para `/collections/samba`.
- Matching locs:
  - https://lksneakers.com.br/collections/samba
  - https://lksneakers.com.br/collections/adidas-sambae
  - https://lksneakers.com.br/collections/adidas-samba-jane
  - https://lksneakers.com.br/collections/adidas-samba

## Demanda / SERP
- `adidas samba`: 246.000 buscas/mês no Brasil; intenção transacional.
- `tenis adidas samba`: 90.500 buscas/mês.
- `samba adidas`: 74.000 buscas/mês.
- `adidas samba feminino`: 60.500 buscas/mês.
- SERP tem PAA e shopping/popular products; precisa de uma URL forte, não duas competindo.

## Recomendação
Escolher `https://lksneakers.com.br/collections/samba` como URL principal.

Motivos:
- é a URL já linkada pela homepage/menu público;
- é mais curta e limpa;
- já parece ser a coleção histórica/mais antiga;
- tem os mesmos 95 produtos;
- evita mudar a linkagem principal já existente.

A URL `/collections/adidas-samba` deve deixar de competir e apontar para `/collections/samba`.

## Plano proposto — fase segura
1. Backup completo das duas coleções.
2. Copiar o conteúdo SEO/GEO otimizado de `/collections/adidas-samba` para `/collections/samba`, ajustando qualquer termo operacional residual.
3. Criar/validar redirect 301 de `/collections/adidas-samba` para `/collections/samba` se a rota puder ser liberada com segurança.
4. Se o redirect não puder sobrescrever rota ativa, preparar fallback: despublicar/arquivar a coleção duplicada e então criar redirect.
5. QA: HTTP, canonical, sitemap, meta title/description, conteúdo/FAQ, ausência de termos proibidos nos campos editados.

## Risco
- Médio: envolve URL/canonical de coleção de alto volume.
- Redirect de coleção ativa pode exigir despublicar/arquivar a duplicata; isso é write estrutural em Shopify.
- Não mexe em produtos, preço, estoque, feed, campanhas ou theme.

## Rollback
- Restaurar campos SEO/descrição das duas coleções pelo backup.
- Remover redirect criado.
- Republicar/restaurar handle da coleção duplicada se necessário.

## Aprovação necessária
Para executar a consolidação, preciso da aprovação explícita:

`Aprovo consolidar Adidas Samba em /collections/samba: copiar o SEO/GEO otimizado para /samba, tentar redirect 301 de /adidas-samba para /samba, com backup e rollback. Se precisar despublicar/arquivar a duplicata para liberar o redirect, parar e pedir nova confirmação antes.`

## Alternativa conservadora
Se preferir evitar mexer em redirect agora:

`Aprovo apenas copiar o SEO/GEO otimizado para /collections/samba, sem redirect e sem despublicar a duplicata.`
