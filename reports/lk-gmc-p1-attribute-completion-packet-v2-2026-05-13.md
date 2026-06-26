# LK GMC — P1 Attribute Completion Packet v2, 2026-05-13
Status: `gmc_p1_attribute_completion_packet_v2_ready_no_write`
Modo: no-write / approval packet prep. Nenhum Merchant/feed/Shopify/Tiny/DB/envio executado.
## Veredito
Há um pacote P1 possível para corrigir atributos Merchant em **1.583 online product IDs**, mas ainda não é execução. O pacote deve ser dividido em duas ondas: 60 high-confidence e 1.523 medium-confidence/review.
## Contagens
- Produtos com issues revisados: 2100
- Candidatos futuros totais: 1583
- High-confidence: 60
- Medium-confidence / needs review: 1523
- Bloqueados sem match Shopify exato: 469
- Ambíguos por valor fonte ausente: 48
- Atributos faltantes nos candidatos:
  - size: 1532
  - age group: 1478
  - gender: 1478
  - color: 45

## Onda 1 — high-confidence, size-only/default variants
Recomendação: só preparar apply depois de aprovação específica. Exemplos:
- `online:pt:BR:105247` — Boné Carhartt Canvas Script Graphic Preto — missing: size — sugestão: `{"sizes": ["Default Title"]}`
- `online:pt:BR:11700328-1` — Boné Lululemon Classic Ball Wordmark — missing: size — sugestão: `{"sizes": ["Bone/White"]}`
- `online:pt:BR:11700328-2` — Boné Lululemon Classic Ball Wordmark — missing: size — sugestão: `{"sizes": ["Butter Cream/Light Ivory"]}`
- `online:pt:BR:11700328-3` — Boné Lululemon Classic Ball Wordmark — missing: size — sugestão: `{"sizes": ["Lavender Lux/Goodnight Plum"]}`
- `online:pt:BR:11700328-4` — Boné Lululemon Classic Ball Wordmark — missing: size — sugestão: `{"sizes": ["Passionate"]}`
- `online:pt:BR:11700328-5` — Boné Lululemon Classic Ball Wordmark — missing: size — sugestão: `{"sizes": ["Black/White"]}`
- `online:pt:BR:11700328-6` — Boné Lululemon Classic Ball Wordmark — missing: size — sugestão: `{"sizes": ["White/Black"]}`
- `online:pt:BR:11750230-1` — Bolsa Lululemon Slouchy Sling 6L — missing: size — sugestão: `{"sizes": ["Lava Cake"]}`

## Onda 2 — medium-confidence, adult/unisex + size por Shopify
Recomendação: revisar amostra/critério antes de apply em lote. Exemplos:
- `online:pt:BR:1023851-1A17746_2NM8J-1` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom — missing: age group, gender, size — sugestão: `{"sizes": ["43"], "ageGroup": "adult", "gender": "unisex"}`
- `online:pt:BR:1023851-1A17746_2NM8J-10` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom — missing: age group, gender, size — sugestão: `{"sizes": ["44"], "ageGroup": "adult", "gender": "unisex"}`
- `online:pt:BR:1023851-1A17746_2NM8J-2` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom — missing: age group, gender, size — sugestão: `{"sizes": ["39"], "ageGroup": "adult", "gender": "unisex"}`
- `online:pt:BR:1023851-1A17746_2NM8J-3` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom — missing: age group, gender, size — sugestão: `{"sizes": ["40"], "ageGroup": "adult", "gender": "unisex"}`
- `online:pt:BR:1023851-1A17746_2NM8J-4` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom — missing: age group, gender, size — sugestão: `{"sizes": ["40.5"], "ageGroup": "adult", "gender": "unisex"}`
- `online:pt:BR:1023851-1A17746_2NM8J-5` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom — missing: age group, gender, size — sugestão: `{"sizes": ["41"], "ageGroup": "adult", "gender": "unisex"}`
- `online:pt:BR:1023851-1A17746_2NM8J-7` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom — missing: age group, gender, size — sugestão: `{"sizes": ["42"], "ageGroup": "adult", "gender": "unisex"}`
- `online:pt:BR:1023851-1A17746_2NM8J-8` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom — missing: age group, gender, size — sugestão: `{"sizes": ["42.5"], "ageGroup": "adult", "gender": "unisex"}`

## Bloqueados — não aplicar
Motivo principal: sem match Shopify exato por SKU/offer_id. Exemplos:
- `online:pt:BR:10310578515087778063` — 40 — missing: age group, gender, size — sugestão: `{}`
- `online:pt:BR:10695397335246538087` — 42 — missing: age group, color, gender, size — sugestão: `{}`
- `online:pt:BR:12196644472973744396` — 36/37 — missing: age group, gender, size — sugestão: `{}`
- `online:pt:BR:12475328072847087695` — 42 — missing: age group, gender, size — sugestão: `{}`
- `online:pt:BR:12820359859699264559` — Camiseta Fear Of God Essentials Jersey Crewneck Heather Bege — missing: age group, color, gender, price, size — sugestão: `{}`

## Ambíguos — não aplicar
Motivo principal: atributo fonte ausente, especialmente cor em itens default/acessórios. Exemplos:
- `online:pt:BR:2183-USA` — Jason Markk Travel Shoe Cleaning Kit — missing: color, size — sugestão: `{"sizes": ["Default Title"], "color": ""}`
- `online:pt:BR:300110` — Jason Markk Essential Kit de Limpeza — missing: color, size — sugestão: `{"sizes": ["Default Title"], "color": ""}`
- `online:pt:BR:9780847866694` — Livro Rizzoli Nike SB: The Dunk Book — missing: color, size — sugestão: `{"sizes": ["Default Title"], "color": ""}`
- `online:pt:BR:9780847872657` — Livro Rizzoli From Soul to Sole: The Adidas Sneakers of Jacques Chassaing — missing: color, size — sugestão: `{"sizes": ["Default Title"], "color": ""}`
- `online:pt:BR:9783836571968` — Livro Taschen The Adidas Archive: The Footwear Collection — missing: color, size — sugestão: `{"sizes": ["Default Title"], "color": ""}`

## Guardrails para eventual apply
- Do not apply blocked_no_shopify_exact_sku_match rows.
- Do not apply ambiguous_missing_source_value rows.
- High-confidence 60 rows are mostly size-only accessories/default variants; still require Lucas approval before apply.
- Medium-confidence 1523 rows use adult/unisex + Shopify size evidence; require review/approval before apply.
- Any future apply must snapshot current Merchant product resources privately before update and verify exact product IDs after delay.
- Do not touch local channel/POS, Shopify, Tiny, Klaviyo, Notion, Rivo, Judge.me, n8n, or external sends.

## Próximo passo seguro
Se for seguir GMC, preparar o executor dry-run apenas para a Onda 1 de 60 high-confidence ou gerar amostra revisável da Onda 2. Qualquer apply exige aprovação inline separada.

## Não executado
- Merchant write/update/custombatch/feed/fetchNow.
- Shopify/Tiny/DB/POS write.
- Klaviyo/WhatsApp/envio externo.
- Compra/fornecedor/Notion/n8n.
