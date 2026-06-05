# LK GMC — Next Gate Read-only Packet: link_template + color + landing

Gerado em: `2026-06-04T16:07:39.747946+00:00`  
Modo: `local/read-only / approval-prep`  
Writes externos: `0`

## Veredito

O próximo pacote seguro está pronto para decisão: **não é para escrever em massa**. O melhor avanço é um micro-piloto controlado de `link_template` em ofertas LIA, mas só depois de confirmar o contrato exato `store_code`/Simprosys/GBP. Em paralelo, há uma fila high-confidence de cor com prioridade comercial e uma classificação inicial de landing errors.

## 1. Shortlist nominal — micro-piloto link_template

- Base: `reports/lk-gmc-local-link-template-preview-2026-06-04.csv`.
- Seleção: 20 ofertas, evitando concentrar tudo no mesmo handle.
- Estado atual: `link_template`/`mobile_link_template` ausente; source `api`; canal local/LIA.
- Ação ainda bloqueada: qualquer ProductInput/API/feed/Simprosys/POS write.

| # | product_id | offer_id | título | proposta preview |
|---|---|---|---|---|
| 1 | `local:pt:BR:LIA_001010841` | `LIA_001010841` | Tênis Autry Medalist Low LS75 Branco | `https://lksneakers.com.br/products/tenis-autry-medalist-low-ls75-branco?variant=47543139041502&country=BR&store_code={store_code}` |
| 2 | `local:pt:BR:LIA_001010842` | `LIA_001010842` | Tênis Autry Medalist Low LS75 Branco | `https://lksneakers.com.br/products/tenis-autry-medalist-low-ls75-branco?variant=47543139074270&country=BR&store_code={store_code}` |
| 3 | `local:pt:BR:LIA_002010759` | `LIA_002010759` | Tênis Autry Medalist Low LL15 Branco | `https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco?variant=47543143792862&country=BR&store_code={store_code}` |
| 4 | `local:pt:BR:LIA_002010760` | `LIA_002010760` | Tênis Autry Medalist Low LL15 Branco | `https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco?variant=47543143825630&country=BR&store_code={store_code}` |
| 5 | `local:pt:BR:LIA_01424-002-1` | `LIA_01424-002-1` | Tênis Born Raised x Nike SB Dunk Low One Block At A Time Azul | `https://lksneakers.com.br/products/born-x-raised-x-nike-sb-dunk-low-one-block-at-a-time?variant=44413386424542&country=BR&store_code={store_code}` |
| 6 | `local:pt:BR:LIA_01424-002-2` | `LIA_01424-002-2` | Tênis Born Raised x Nike SB Dunk Low One Block At A Time Azul | `https://lksneakers.com.br/products/born-x-raised-x-nike-sb-dunk-low-one-block-at-a-time?variant=44413386457310&country=BR&store_code={store_code}` |
| 7 | `local:pt:BR:LIA_10017` | `LIA_10017` | Boné Aphase Basic Project - Used Black Preto | `https://lksneakers.com.br/products/bone-aphase-basic-project-used-black-preto?variant=47007181209822&country=BR&store_code={store_code}` |
| 8 | `local:pt:BR:LIA_100286` | `LIA_100286` | Boné Carhartt Canvas Mesh-Back Bege | `https://lksneakers.com.br/products/bone-carhartt-canvas-mesh-back-bege?variant=46599128613086&country=BR&store_code={store_code}` |
| 9 | `local:pt:BR:LIA_1002861` | `LIA_1002861` | Boné Carhartt Canvas Mesh-Back Preto | `https://lksneakers.com.br/products/bone-carhartt-canvas-mesh-back-preto?variant=46599128580318&country=BR&store_code={store_code}` |
| 10 | `local:pt:BR:LIA_100289` | `LIA_100289` | Boné Carhartt Canvas Marrom | `https://lksneakers.com.br/products/bone-carhartt-canvas-marrom?variant=46599128744158&country=BR&store_code={store_code}` |
| 11 | `local:pt:BR:LIA_1002891` | `LIA_1002891` | Boné Carhartt Canvas Preto | `https://lksneakers.com.br/products/bone-carhartt-canvas-preto?variant=46599128711390&country=BR&store_code={store_code}` |
| 12 | `local:pt:BR:LIA_102291-1` | `LIA_102291-1` | Calça Carhartt Men's Work - Relaxed Fit - Rugged Flex - Canvas Preto | `https://lksneakers.com.br/products/calca-carhartt-mens-work-relaxed-fit-rugged-flex%C2%AE-canvas-preto?variant=46599128449246&country=BR&store_code={store_code}` |
| 13 | `local:pt:BR:LIA_102291-2` | `LIA_102291-2` | Calça Carhartt Men's Work - Relaxed Fit - Rugged Flex - Canvas Preto | `https://lksneakers.com.br/products/calca-carhartt-mens-work-relaxed-fit-rugged-flex%C2%AE-canvas-preto?variant=46599128482014&country=BR&store_code={store_code}` |
| 14 | `local:pt:BR:LIA_1022913-1` | `LIA_1022913-1` | Calça Carhartt Men's Work - Relaxed Fit - Rugged Flex - Canvas Bege | `https://lksneakers.com.br/products/calca-carhartt-mens-work-relaxed-fit-rugged-flex%C2%AE-canvas-bege?variant=46599128187102&country=BR&store_code={store_code}` |
| 15 | `local:pt:BR:LIA_1022913-2` | `LIA_1022913-2` | Calça Carhartt Men's Work - Relaxed Fit - Rugged Flex - Canvas Bege | `https://lksneakers.com.br/products/calca-carhartt-mens-work-relaxed-fit-rugged-flex%C2%AE-canvas-bege?variant=46599128219870&country=BR&store_code={store_code}` |
| 16 | `local:pt:BR:LIA_1023851-1A17746_2NM8J-1` | `LIA_1023851-1A17746_2NM8J-1` | Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom | `https://lksneakers.com.br/products/tenis-onitsuka-tiger-x-versace-sakura-leather-loafers-brown-white-marrom?variant=48054524543198&country=BR&store_code={store_code}` |
| 17 | `local:pt:BR:LIA_1023851-1A17746_2NM8J-10` | `LIA_1023851-1A17746_2NM8J-10` | Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom | `https://lksneakers.com.br/products/tenis-onitsuka-tiger-x-versace-sakura-leather-loafers-brown-white-marrom?variant=48054524608734&country=BR&store_code={store_code}` |
| 18 | `local:pt:BR:LIA_1025116-1A17741_2NM5J-1` | `LIA_1025116-1A17741_2NM5J-1` | Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Brown Bege | `https://lksneakers.com.br/products/tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-brown-bege?variant=48054312730846&country=BR&store_code={store_code}` |
| 19 | `local:pt:BR:LIA_1025116-1A17741_2NM5J-10` | `LIA_1025116-1A17741_2NM5J-10` | Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Brown Bege | `https://lksneakers.com.br/products/tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-brown-bege?variant=48054313025758&country=BR&store_code={store_code}` |
| 20 | `local:pt:BR:LIA_1032792-1` | `LIA_1032792-1` | Calça Carhartt Men's Work - Relaxed Fit - Rugged Flex - Canvas Marrom | `https://lksneakers.com.br/products/calca-carhartt-mens-work-relaxed-fit-rugged-flex%C2%AE-canvas-marrom?variant=46599128318174&country=BR&store_code={store_code}` |

### Checklist antes de aprovar qualquer piloto A3

- [ ] Confirmar o placeholder exato aceito (`{store_code}` ou outro contrato).
- [ ] Confirmar se a URL com store_code deve manter `variant` e `country=BR`.
- [ ] Confirmar surface dono: Simprosys Local Feed / Merchant API / Shopify POS-local inventory.
- [ ] Snapshot dos 5–20 product resources/config antes do write.
- [ ] Readback após write + productstatuses após processamento.
- [ ] Rollback no mesmo surface se o issue trocar ou aumentar.

## 2. Missing color — prioridade comercial high-confidence

- High-confidence total no preview: `393`.
- Subfila com termos comerciais prioritários: `80` linhas neste packet.
- Status: preview-only; não aplicar atributo `color` sem revisão/aprovação.

| # | offer_id | cor | título | sinal |
|---|---|---|---|---|
| 1 | `U204L6A6-34` | Bege | Tênis New Balance 204L Reflection Bege | 204l |
| 2 | `U204L2SZ-36` | Bege | Tênis New Balance 204L Sea Salt Linen Bege | 204l |
| 3 | `IQ7604-104` | Rosa | Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Sail Tropical Pink Rosa | travis, jordan |
| 4 | `U204L5AV-41` | Cinza | Tênis New Balance 204L Lone Star Grey Cinza | 204l |
| 5 | `IQ1323-001-41` | Azul | Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul | dunk |
| 6 | `KI6669-39` | Branco | Tênis adidas Samba OG Crystal Linen Ivory Gum Branco | samba |
| 7 | `IQ1323-001-38` | Azul | Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul | dunk |
| 8 | `U204L5AV-38` | Cinza | Tênis New Balance 204L Lone Star Grey Cinza | 204l |
| 9 | `HQ2993-105` | Vermelho | Tênis Nike Air Jordan 1 Retro Low OG Howard University Vermelho | jordan |
| 10 | `IQ1323-001-39` | Azul | Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul | dunk |
| 11 | `U204L2SZ-44` | Bege | Tênis New Balance 204L Sea Salt Linen Bege | 204l |
| 12 | `IQ7604-109` | Bege | Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Shy Pink Bege | travis, jordan |
| 13 | `KI6669-36` | Branco | Tênis adidas Samba OG Crystal Linen Ivory Gum Branco | samba |
| 14 | `IQ7604-101` | Bege | Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Shy Pink Bege | travis, jordan |
| 15 | `IQ7604-100` | Bege | Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Shy Pink Bege | travis, jordan |
| 16 | `HQ2993-110` | Vermelho | Tênis Nike Air Jordan 1 Retro Low OG Howard University Vermelho | jordan |
| 17 | `U204L6A6-42` | Bege | Tênis New Balance 204L Reflection Bege | 204l |
| 18 | `HQ2993-106` | Vermelho | Tênis Nike Air Jordan 1 Retro Low OG Howard University Vermelho | jordan |
| 19 | `IQ1323-001-36` | Azul | Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul | dunk |
| 20 | `U204L2SZ-42` | Bege | Tênis New Balance 204L Sea Salt Linen Bege | 204l |
| 21 | `JRD-0696926-OS` | Vermelho | Tênis Nike Air Jordan 1 Low Cardinal Vermelho | jordan |
| 22 | `IQ1323-001-43` | Azul | Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul | dunk |
| 23 | `IQ1323-001-34` | Azul | Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul | dunk |
| 24 | `IQ7604-108` | Bege | Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Shy Pink Bege | travis, jordan |
| 25 | `HQ2993-103` | Vermelho | Tênis Nike Air Jordan 1 Retro Low OG Howard University Vermelho | jordan |
| 26 | `U204L5AV-42` | Cinza | Tênis New Balance 204L Lone Star Grey Cinza | 204l |
| 27 | `IQ7604-107` | Bege | Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Shy Pink Bege | travis, jordan |
| 28 | `IQ1323-001-40` | Azul | Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul | dunk |
| 29 | `JS3931-8` | Marrom | Tênis Adidas Samba LT Cow Print Brown White Marrom | samba |
| 30 | `U204L5AV-36` | Cinza | Tênis New Balance 204L Lone Star Grey Cinza | 204l |
| 31 | `U204L2SZ-38` | Bege | Tênis New Balance 204L Sea Salt Linen Bege | 204l |
| 32 | `IQ1323-001-37` | Azul | Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul | dunk |
| 33 | `JS3931-4` | Marrom | Tênis Adidas Samba LT Cow Print Brown White Marrom | samba |
| 34 | `U204L2SZ-40` | Bege | Tênis New Balance 204L Sea Salt Linen Bege | 204l |
| 35 | `IQ1323-001-35` | Azul | Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul | dunk |
| 36 | `IQ7604-102` | Bege | Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Shy Pink Bege | travis, jordan |
| 37 | `KI6669-40` | Branco | Tênis adidas Samba OG Crystal Linen Ivory Gum Branco | samba |
| 38 | `KI6669-35` | Branco | Tênis adidas Samba OG Crystal Linen Ivory Gum Branco | samba |
| 39 | `U204L6A6-44` | Bege | Tênis New Balance 204L Reflection Bege | 204l |
| 40 | `IQ1323-001-42` | Azul | Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul | dunk |

Mais `40` linhas no JSON: `areas/lk/sub-areas/growth/reports/lk-gmc-next-gate-readonly-packet-20260604.json`.


## 3. Landing page errors — classificação atual

- URLs checadas: `44`.
- `public_qa_rate_limited_429_retry_later`: `27`
- `public_html_ok_js_rate_limited_likely_not_404`: `5`
- `public_ok_status_lag_or_googlebot_specific`: `12`

Leitura: parte relevante bateu em 429/Cloudflare public QA. Isso não prova 404. As 12 URLs OK indicam que uma fatia é provável lag/status Googlebot-specific. Próximo safe step é retry mais lento ou leitura autenticada read-only; qualquer correção de feed/handle/variant continua bloqueada.

### Amostras OK

- `online:pt:BR:20046-3` — Jaqueta Aphase Relaxed Denim- Black Preto — https://lksneakers.com.br/products/jaqueta-aphase-relaxed-denim-black-preto?currency=BRL&country=BR&variant=47007281283294&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:7866599083713103688` — 38 — https://lksneakers.com.br/products/tenis-adidas-samba-og-cream-white-cardboard-creme
- `online:pt:BR:DD1873102-11` — Tênis Nike Dunk Low Next Nature Black White Preto — https://lksneakers.com.br/products/nike-dunk-low-next-nature-black-white?currency=BRL&country=BR&variant=44265093464286&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:DD1873102-5` — Tênis Nike Dunk Low Next Nature Black White Preto — https://lksneakers.com.br/products/nike-dunk-low-next-nature-black-white?currency=BRL&country=BR&variant=44265093267678&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:DH4401100-40` — Tênis Nike Dunk Low Black Paisley Preto — https://lksneakers.com.br/products/nike-dunk-low-black-paisley?currency=BRL&country=BR&variant=44265080586462&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:DH7577001-44` — Tênis Nike Dunk Low Fossil Rose Azul/Rosa — https://lksneakers.com.br/products/nike-dunk-low-fossil-rose?currency=BRL&country=BR&variant=44265073148126&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:DH9764001-2` — Tênis Nike Dunk Low GS Black/White Metallic Preto — https://lksneakers.com.br/products/nike-dunk-low-gs-black-white-metallic?currency=BRL&country=BR&variant=45739470323934&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e
- `online:pt:BR:DH9764001-4` — Tênis Nike Dunk Low GS Black/White Metallic Preto — https://lksneakers.com.br/products/nike-dunk-low-gs-black-white-metallic?currency=BRL&country=BR&variant=45739470258398&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e

## Decisão recomendada para Lucas

Aprovar **somente** uma próxima etapa A1/A3-prep: confirmar contrato `store_code`/Simprosys e preparar micro-piloto nominal de 5–20 ofertas. Ainda não aprovar bulk nos 10.441.

## Bloqueios

- Bloqueado: Bulk link_template nos 10.441
- Bloqueado: ProductInput/Merchant API write
- Bloqueado: Supplemental/feed upload
- Bloqueado: fetchNow/reprocess
- Bloqueado: Shopify/POS/app config
- Bloqueado: cor/atributo em massa
- Bloqueado: campanhas ou mudanças customer-facing

## Arquivo JSON

`areas/lk/sub-areas/growth/reports/lk-gmc-next-gate-readonly-packet-20260604.json`
