# Approval Packet — SEMrush Position Tracking alert — 2026-06-26

Status: **diagnóstico read-only concluído; nenhum write externo executado**.

Fonte do alerta enviado por Lucas:
- Project: `lksneakers.com.br`
- Device/location: mobile, Brazil, Google, PT-BR
- Regra: mudança > 5 posições
- Keywords: `nike vomero premium valor`, `adidas samba marrom`, `alo yoga roupa`, `lululemon define jacket`, `alo yoga brasil`.

Evidências locais:
- DataForSEO SERP mobile BR/PT consultado para os 5 termos.
- Shopify Admin read-only: `work/semrush-alert-20260626/shopify-readonly.json`.
- Public readback: páginas públicas LK consultadas para Samba, Alo Yoga, Vomero Premium e Lululemon Define.

## Resumo executivo

Prioridade de ação: **Adidas Samba marrom**.

Motivo:
- Maior volume do alerta: 3.600.
- Queda SEMrush: -81 posições / sem posição reportada.
- SERP tem intenção transacional forte, com Adidas oficial, Authentic Feet, Netshoes, Popular Products, Dafiti, Enjoei e NewSkull.
- A LK possui produtos Samba marrom ativos, mas **não possui collection canônica real `adidas-samba-marrom` no Admin**. A URL pública `/collections/adidas-samba-marrom` renderiza conteúdo da coleção geral Adidas Samba, sem collection própria detectada.

## Ranking de resposta

| Prioridade | Keyword | Alerta | Diagnóstico | Próxima ação |
|---|---:|---|---|---|
| P1 | `adidas samba marrom` | queda -81 / vol 3.600 | Não há collection canônica real; há produtos ativos marrom; SERP favorece PDPs + categoria específica | Handoff LK Shopify para validar/criar superfície `adidas-samba-marrom`; depois Growth guia/FAQ/schema em dev |
| P2 | `lululemon define jacket` | pos 25 / queda -6 / vol 260 | LK aparece em Popular Products, mas não há collection Define; há 3 PDPs ativos | Handoff LK Shopify ou PDP SEO cleanup; menor impacto que Samba |
| P3 | `alo yoga roupa` | pos 18 / queda -10 / vol 0 no alerta | Collection Alo existe e tem guia, mas copy parece duplicada/longa; Google oficial domina | Fazer higiene/compactação em dev depois; não urgente |
| P4 | `alo yoga brasil` | pos 15 / alta +5 / vol 2.400 | Movimento positivo; SERP dominada por Alo oficial/notícias/Instagram | Monitorar, não mexer agora |
| P5 | `nike vomero premium valor` | pos 10 / alta +90 / vol 40 | Forte melhora; LK aparece em Popular Products; guia já robusto | Não mexer agora; só monitorar e talvez futuro FAQ de preço sem fixar valores |

## P1 — Adidas Samba marrom

### SERP atual

- Adidas oficial ocupa posições orgânicas e Popular Products.
- Authentic Feet e Netshoes ranqueiam com páginas de categoria/busca específicas.
- Popular Products mostra vários itens “Samba marrom”.
- PAA: `Tem Adidas Samba marrom?`, `Porque o Adidas Samba é tão caro?`, `Qual a cor do Adidas Samba mais vendido?`, `Quanto custa o Adidas Samba original?`.

### LK readback

Admin read-only encontrou produtos ativos:
- `tenis-adidas-samba-og-shadow-brown-powder-yellow-marrom` — ACTIVE.
- `tenis-adidas-samba-lt-cow-print-brown-white-marrom` — ACTIVE.
- `tenis-adidas-samba-62-wild-brown-marrom` — ACTIVE.

Também encontrou produtos Samba marrom ARCHIVED, então a superfície precisa filtrar só ativos.

Collection:
- `collectionByHandle(adidas-samba-marrom)` = null.
- `collectionByHandle(adidas-samba)` existe, 95 produtos.
- URL pública `/collections/adidas-samba-marrom` renderiza a coleção geral Samba; isso não é uma superfície canônica real no Admin.

### Recomendação

Abrir handoff para LK Shopify validar/criar/ativar collection canônica:
- handle preferido: `adidas-samba-marrom`
- title sugerido: `Adidas Samba Marrom`
- inclusão: apenas produtos Adidas Samba marrom ativos já existentes, sem consultar/alterar estoque.

Depois da superfície 200 OK, Growth prepara em dev:
- guia/FAQ/schema focado em `Adidas Samba marrom`;
- OG / XLG / Jane / variações marrom;
- feminino/masculino;
- autenticidade;
- diferença Samba marrom vs branco/preto;
- styling com tons terrosos.

## Atenções

- Não mexer em estoque/disponibilidade sem LK Stock.
- Não publicar preço fixo em guia editorial; preço deve permanecer dinâmico na PDP/checkout.
- Não alterar GMC/campanhas/Klaviyo/checkout.
- Qualquer criação/ativação de collection é LK Shopify, não Growth direto.

## Aprovação recomendada

`Aprovo abrir handoff para LK Shopify validar/criar/ativar a collection canônica Adidas Samba Marrom, preferencialmente /collections/adidas-samba-marrom, usando apenas produtos Adidas Samba marrom ativos já existentes, sem consultar ou alterar estoque, preço, campanhas, GMC, Klaviyo ou checkout, com preview/readback público; após a superfície 200 OK, Growth prepara guia/FAQ/schema em dev antes de qualquer produção.`
