# LK GMC — Execução 1, 2 e 3: link_template, color, landing

Gerado em: `2026-06-04T18:32:10.982969+00:00`  
Modo: `local/read-only`  
Writes externos: `0`  
Store code confirmado: `LK001`

## Veredito executivo
Rodei os três pacotes em modo seguro. Resultado: temos **material suficiente para um A3 approval packet de micro-piloto**, mas **ainda não é seguro escrever** porque falta confirmar o surface dono/mutation exata e fazer snapshot/readback/rollback.

## 1. link_template / LIA — micro-piloto final
- Candidatos comerciais avaliados: `10`.
- Micro-piloto final conservador: `10` ofertas.
- URL preview usa `store_code=LK001`.
- Status: pronto para snapshot + confirmação de surface; write segue bloqueado.

| # | offer_id | título | URL LK001 |
|---|---|---|---|
| 1 | `LIA_01424-002-1` | Tênis Born Raised x Nike SB Dunk Low One Block At A Time Azul | `https://lksneakers.com.br/products/born-x-raised-x-nike-sb-dunk-low-one-block-at-a-time?variant=44413386424542&country=BR&store_code=LK001` |
| 2 | `LIA_01424-002-2` | Tênis Born Raised x Nike SB Dunk Low One Block At A Time Azul | `https://lksneakers.com.br/products/born-x-raised-x-nike-sb-dunk-low-one-block-at-a-time?variant=44413386457310&country=BR&store_code=LK001` |
| 3 | `LIA_1023851-1A17746_2NM8J-1` | Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom | `https://lksneakers.com.br/products/tenis-onitsuka-tiger-x-versace-sakura-leather-loafers-brown-white-marrom?variant=48054524543198&country=BR&store_code=LK001` |
| 4 | `LIA_1023851-1A17746_2NM8J-10` | Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom | `https://lksneakers.com.br/products/tenis-onitsuka-tiger-x-versace-sakura-leather-loafers-brown-white-marrom?variant=48054524608734&country=BR&store_code=LK001` |
| 5 | `LIA_1025116-1A17741_2NM5J-1` | Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Brown Bege | `https://lksneakers.com.br/products/tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-brown-bege?variant=48054312730846&country=BR&store_code=LK001` |
| 6 | `LIA_1025116-1A17741_2NM5J-10` | Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Brown Bege | `https://lksneakers.com.br/products/tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-brown-bege?variant=48054313025758&country=BR&store_code=LK001` |
| 7 | `LIA_001010841` | Tênis Autry Medalist Low LS75 Branco | `https://lksneakers.com.br/products/tenis-autry-medalist-low-ls75-branco?variant=47543139041502&country=BR&store_code=LK001` |
| 8 | `LIA_001010842` | Tênis Autry Medalist Low LS75 Branco | `https://lksneakers.com.br/products/tenis-autry-medalist-low-ls75-branco?variant=47543139074270&country=BR&store_code=LK001` |
| 9 | `LIA_002010759` | Tênis Autry Medalist Low LL15 Branco | `https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco?variant=47543143792862&country=BR&store_code=LK001` |
| 10 | `LIA_002010760` | Tênis Autry Medalist Low LL15 Branco | `https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco?variant=47543143825630&country=BR&store_code=LK001` |

### Gate antes de write A3
- [ ] Confirmar surface dono: Simprosys Local Feed / Merchant local product API / Shopify POS-local inventory.
- [ ] Tirar snapshot dos 10 product resources/status atuais.
- [ ] Definir mutation exata no mesmo surface dono.
- [ ] Fazer readback e checar productstatuses após processamento.
- [ ] Ter rollback no mesmo surface.

## 2. missing color — fila revisada
- Linhas comerciais high-confidence priorizadas: `120`.
- Grupos/títulos distintos: `24`.
- Status: fila de revisão; não aplicar em massa sem approval/surface.

### Top grupos
- `11`× — Tenis Nike SB Dunk Low Pro Bluetile Skateboards Azul — cor(es): Azul:11 — exemplos: IQ1323-001-41, IQ1323-001-38, IQ1323-001-39, IQ1323-001-36, IQ1323-001-43
- `8`× — Tênis New Balance 1906L Black Suede Preto — cor(es): Preto:8 — exemplos: U1906LNT-10, U1906LNT-11, U1906LNT-9, U1906LNT-1, U1906LNT-8
- `8`× — Tênis Nike Shox TL Black Cave Stone Preto — cor(es): Preto:8 — exemplos: HM9612-010-34, HM9612-010-40, HM9612-010-41, HM9612-010-44, HM9612-010-36
- `7`× — Tênis New Balance 204L Sea Salt Linen Bege — cor(es): Bege:7 — exemplos: U204L2SZ-36, U204L2SZ-44, U204L2SZ-42, U204L2SZ-38, U204L2SZ-40
- `7`× — Tênis Nike Vomero Premium x Melitta Baumeister Total Orange Laranja — cor(es): Laranja:7 — exemplos: IQ7166-800-34, IQ7166-800-35, IQ7166-800-45, IQ7166-800-38, IQ7166-800-42
- `6`× — Tênis Nike Vomero Premium x Renegade x Cinnamon Marrom — cor(es): Marrom:6 — exemplos: IQ7314-200-38, IQ7314-200-44, IQ7314-200-41, IQ7314-200-40, IQ7314-200-42
- `6`× — Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Shy Pink Bege — cor(es): Bege:6 — exemplos: IQ7604-109, IQ7604-101, IQ7604-100, IQ7604-108, IQ7604-107
- `6`× — Tênis Adidas Ballerina Bad Bunny Black Chalk Preto — cor(es): Preto:6 — exemplos: JQ9231-6, JQ9231-3, JQ9231-9, JQ9231-2, JQ9231-8
- `6`× — Tênis New Balance 1906L Silver Shadow Grey Slip-on Prata — cor(es): Prata:6 — exemplos: U1906LAE-36, U1906LAE-38, U1906LAE-35, U1906LAE-43, U1906LAE-40
- `6`× — Tênis Nike Vomero Premium Barely Green Verde — cor(es): Verde:6 — exemplos: HM5973-300-38, HM5973-300-37, HM5973-300-42, HM5973-300-34, HM5973-300-36
- `5`× — Tênis New Balance 204L Lone Star Grey Cinza — cor(es): Cinza:5 — exemplos: U204L5AV-41, U204L5AV-38, U204L5AV-42, U204L5AV-36, U204L5AV-40
- `5`× — Tênis Nike Air Jordan 1 Retro Low OG Howard University Vermelho — cor(es): Vermelho:5 — exemplos: HQ2993-105, HQ2993-110, HQ2993-106, HQ2993-103, HQ2993-108

## 3. landing errors — retry público
- URLs rechecadas: `44`.
- `public_ok_likely_not_404`: `44`

Não apareceu 404 confirmado neste retry. O bloqueio principal segue sendo limitação pública/edge/Cloudflare em parte das URLs, não prova de PDP quebrada.

## Artefatos
- `areas/lk/sub-areas/growth/reports/lk-gmc-run-123-link-template-final-pilot-LK001-20260604.csv`
- `areas/lk/sub-areas/growth/reports/lk-gmc-run-123-missing-color-priority-review-20260604.csv`
- `areas/lk/sub-areas/growth/reports/lk-gmc-run-123-landing-retry-20260604.csv`
- `areas/lk/sub-areas/growth/reports/lk-gmc-run-123-link-color-landing-20260604.json`

## Bloqueios preservados
- Bloqueado: ProductInput/Merchant API write
- Bloqueado: Simprosys/POS/app config
- Bloqueado: supplemental/feed upload
- Bloqueado: fetchNow/reprocess
- Bloqueado: bulk nos 10.441
- Bloqueado: cor em massa
- Bloqueado: Shopify/theme/PDP/campanhas