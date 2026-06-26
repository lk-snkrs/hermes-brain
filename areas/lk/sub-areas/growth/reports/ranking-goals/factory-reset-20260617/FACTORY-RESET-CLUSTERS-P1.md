# Factory reset — clusters P1 — 2026-06-17

Status: read-only + approval packet. Nenhum write externo. values_printed=false.

## Pedido executado

Lucas pediu para fazer os passos 3, 4 e 5 do plano:

3. Rodar factories read-only para Nike/Jordan/Travis, New Balance e Onitsuka.
4. Escolher a próxima P1 com base em receita, GSC, SERP e conversão provável.
5. Gerar approval packet.

## Veredito

A próxima P1 recomendada é a collection:

`/collections/air-jordan-travis-scott`

Motivo: maior cluster de receita da LK, já aparece no topo da SERP para `nike travis scott`, tem CTR melhorável e não tem FAQ/answer block no Admin read-only.

## Ranking dos clusters

### 1. Nike/Jordan/Travis — P1 escolhido

Receita 90d:

- R$ 1.240.840,90
- 267 unidades
- 227 pedidos
- 33,8% share

GSC:

- Query: `nike travis scott`
- Página: `/collections/air-jordan-travis-scott`
- 81 cliques / 6.656 impressões / CTR 1,22% / posição 6,1

DataForSEO:

- `nike travis scott`: 8.100/mês, intenção transactional.
- `air jordan travis scott`: 1.300/mês, intenção transactional.

SERP mobile Brasil para `nike travis scott`:

- Popular Products aparece no topo.
- LK aparece orgânico rank_absolute 3 / rank_group 2.
- PAA/PAS incluem intenção de preço, originalidade e modelos Travis Scott Jordan.

Shopify read-only:

- Collection existe: `Nike x Travis Scott`.
- 25 produtos.
- SEO atual: `Air Jordan Travis Scott Original na LK Sneakers`.
- Descrição existe.
- FAQ: **não detectado**.

Projeção simples de CTR:

- Baseline: 81 cliques / 6.656 impressões / CTR 1,22%.
- CTR 1,8%: ~120 cliques, +39 cliques, +47,9%.
- CTR 2,2%: ~146 cliques, +65 cliques, +80,8%.
- CTR 2,5%: ~166 cliques, +85 cliques, +105,4%.

### 2. New Balance 204L — P1 alternativo

Receita cluster New Balance 90d:

- R$ 729.216,18
- 285 unidades
- 236 pedidos
- 19,9% share

GSC:

- Query: `new balance 204l`
- Página: `/collections/new-balance-204l`
- 12 cliques / 3.874 impressões / CTR 0,31% / posição 11,0

DataForSEO:

- `new balance 204l`: 12.100/mês; maio e abril 2026 com 40.500 buscas.
- Intenção transactional.

Shopify read-only:

- Collection existe.
- 32 produtos.
- SEO atual já bom: `New Balance 204L Original | LK Sneakers`.
- FAQ já detectado.

Diagnóstico:

- Oportunidade grande, mas provavelmente exige mais que title/meta: Merchant/Product listings, ranking orgânico fora do top 10, conteúdo/links e talvez feed quality.
- Melhor como próxima factory após Travis.

### 3. Onitsuka Tiger — segurar impacto

Receita cluster 90d:

- R$ 810.696,90
- 313 unidades
- 256 pedidos
- 22,1% share

GSC:

- `onitsuka tiger`: 102 cliques / 29.510 impressões / CTR 0,35% / posição 8,2.
- `onitsuka tiger mexico 66`: 152 cliques / 6.971 impressões / CTR 2,18% / posição 2,3.

Status:

- Collection principal e Mexico 66 foram atualizadas recentemente.
- Recomendo aguardar D+7 antes de novo write no cluster.

## Decisão

Escolher **Air Jordan Travis Scott collection** agora.

Racional:

- maior receita da LK;
- SERP já mostra LK em posição forte;
- CTR tem espaço de uplift;
- collection não tem FAQ;
- melhoria é de baixo esforço e risco controlado;
- evita continuar Nike Mind enquanto há cache misto em algumas páginas.

## Approval packet gerado

- Packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ranking-goals/factory-reset-20260617/APPROVAL-PACKET-AIR-JORDAN-TRAVIS-SCOTT-COLLECTION.md`
- Payload: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ranking-goals/factory-reset-20260617/candidate-air-jordan-travis-scott-collection-packet.json`
