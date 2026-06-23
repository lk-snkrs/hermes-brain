# LK Growth — Follow 1→5 com trava anti-retrabalho

- Criado UTC: 2026-06-22T17:09:51.280260+00:00
- Pedido Lucas: seguir itens 1 a 5, garantindo que não vamos agir em páginas já trabalhadas.
- Modo desta etapa: read-only/local report. Writes externos: 0. values_printed=false.

## Trava anti-retrabalho aplicada

Antes de priorizar qualquer ação, foi criado inventário de intervenções recentes 2026-06-19→2026-06-22.

Fonte principal criada:
- `/opt/data/lk_recent_interventions_inventory_20260619_20260622.md`

### Páginas/URLs em quarentena operacional

Não propor novo write/copy/schema/SEO nelas agora; apenas impact review, QA ou readback.

#### Nike Mind / Vomero
- `/collections/nike-mind-001`
- `/pages/guia-nike-mind-001-002`
- `/collections/nike-vomero-premium`
- `/products/slide-nike-mind-001-black-chrome-preto`
- `/products/slide-nike-mind-001-light-smoke-grey-cinza`
- `/products/slide-nike-mind-001-pearl-pink-rosa`
- `/products/tenis-nike-vomero-premium-white-bright-crimson-branco`

#### Onda C1+C2 LKGOC / AI Visibility
- `/collections/adidas-handball-spezial`
- `/collections/new-balance-204l`
- `/collections/onitsuka-tiger-mexico-66`
- `/collections/new-balance-1906l`
- `/collections/alo-yoga-1`
- `/collections/air-jordan-1-low`

#### Growth Package A/B e ajustes recentes
- `/products/crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho`
- `/collections/onitsuka-tiger-todos-os-modelos`
- `/products/tenis-nike-dunk-low-cacao-wow-marrom`
- `/llms.txt`
- `/llms-full.txt`
- `/agents.md`
- `/collections/sneakers`
- `/collections/adidas-campus`
- `/collections/adidas-japan`
- `/pages/guia-salomon-xt6-lkgoc`

## Status dos itens 1→5

### 1. Impact review Nike Mind / Vomero

Status: **agendável / não mexer de novo agora**.

- Correção production de dedupe FAQPage já aplicada e QA final OK:
  - Nike Mind: HTTP 200, H1=1, FAQPage=1.
  - Vomero: HTTP 200, H1=1, FAQPage=1.
- Próxima ação permitida: impact review D+7/D+14, sem write.
- Métricas: GSC CTR/posição/cliques, GA4 sessões/ATC, Shopify pedidos/receita, QA público schema.

### 2. Auditoria schema top páginas comerciais

Status: **executada read-only**.

Relatório criado:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ranking-goals/schema-h1-faqpage-public-audit-20260622.md`

Achados principais sem retrabalho:
- P0: nenhum erro crítico confirmado.
- P1 novo elegível: `/collections/alo-yoga` redireciona para home; investigar relação com `/collections/alo-yoga-1` antes de qualquer write.
- P1 elegível com cautela: `/collections/crocs-relampago-mcqueen` tem CollectionPage/Breadcrumb/H1 OK, mas `FAQPage=0`; não confundir com PDP Crocs McQueen já trabalhado.
- Gaps em Onda C existem em algumas páginas sem FAQPage, mas ficam bloqueados por anti-retrabalho até impact review/QA D+7.

### 3. Pacote CTR P0 sem repetir páginas

Status: **não aplicar em Nike Mind/Vomero agora**.

Critério atualizado:
- Nike Mind/Vomero entram só em medição de impacto.
- Próximos candidates precisam excluir inventário recente.
- Candidatos iniciais para packet novo:
  1. `/collections/alo-yoga` → resolver/explicar redirect para home vs coleção canônica `/collections/alo-yoga-1`.
  2. `/collections/crocs-relampago-mcqueen` → avaliar se merece FAQ/schema/intro citável, considerando baixa profundidade de catálogo e PDP já trabalhado.
  3. Revisar queries novas em GSC excluindo todos os handles em quarentena.

### 4. QA visual LKGOC Onda C1+C2

Status: **não escalar nem mexer em copy agora; fazer QA/readback e D+7**.

- Collections Onda C1+C2 publicadas e em quarentena de retrabalho.
- Próxima ação permitida: QA visual/readback e impact review em ~2026-06-26.
- Onitsuka Mexico 66 tinha pendência de readback público/cache no receipt; tratar como verificação, não novo rewrite.

### 5. GMC product data packet

Status: **read-only packet pronto; writes exigem aprovação e dono correto**.

Relatório de base:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/gmc/lk-gmc-product-data-ranking-review-2026-06-18.md`

Prioridades:
1. `mhlsf_full_missing_valid_link_template` — 11.267 local/LIA offers; provável surface feed/Simprosys/API, não PDP.
2. `missing_item_attribute_for_product_type` — 2.530 produtos; aplicar só por micro-piloto e priorização comercial.
3. Residual: inventory/local stores/price/GTIN/images, sem consultar estoque direto.

## Próximo bloco recomendado, sem repetir páginas

1. Rodar GSC/GA4 atual filtrando fora da quarentena operacional.
2. Criar packet novo apenas para páginas **não trabalhadas**:
   - `/collections/alo-yoga` redirect/canonização.
   - `/collections/crocs-relampago-mcqueen` schema/FAQ citável se houver demanda e sentido comercial.
3. Preparar checklist D+7 para Nike Mind/Vomero e Onda C1+C2.
4. Preparar GMC micro-piloto sem executar write.

## Regra operacional deste sprint

Qualquer nova sugestão deve passar primeiro pela lista de quarentena. Se a URL/handle estiver listada, só pode ser: impact review, QA, readback ou rollback — não otimização nova.
