# Product descriptions — audit de linguagem operacional

Status: produto informado corrigido; próximos lotes aguardam aprovação explícita por volume.

## Produto corrigido

- `tenis-air-jordan-1-mid-glitter-swoosh-azul`: `descriptionHtml` corrigido no Admin; tag `encomenda`, variantes, estoque e badge operacional não alterados.

## Achados no catálogo

- Produtos auditados: 2331
- Produtos com algum termo operacional em `body_html`: 2232
- Produtos com frase exata padrão antiga ainda remanescente, excluindo o corrigido: 898
- Principais termos encontrados: `envio em até 2 dias`, `Produtos em estoque`, `rodar`, `Pronta entrega`.

## Packet P1 proposto

- Escopo: corrigir os primeiros 100 produtos com a frase exata antiga no FAQ da descrição.
- Campo: somente `product.descriptionHtml`.
- Método: replace exato da frase antiga por copy neutra de disponibilidade/prazo.
- Fora do escopo: produto/variante/preço/estoque/tags/metafields operacionais/campo `Sujeito a encomenda`/theme/checkout/SEO.
- Guardrail: não alterar tag `encomenda`, inventoryPolicy, inventoryQuantity, variants ou badge/mensagem operacional.

Frase antiga:

> Produtos em estoque: envio em até 2 dias úteis. Produtos sob encomenda: 4 a 6 semanas. Frete grátis acima de R$ 499. Rastreamento em tempo real.

Frase nova:

> O prazo varia conforme a disponibilidade confirmada e a região de entrega. Itens sob encomenda seguem prazo estimado de 4 a 6 semanas. Frete grátis acima de R$ 499 e rastreamento em tempo real.

Arquivos:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/drafts/product-description-operational-faq-packet-p1-20260605/candidate-batch-p1-first100.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/drafts/product-description-operational-faq-packet-p1-20260605/candidate-summary-p1-first100.csv`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/drafts/product-description-operational-faq-packet-p1-20260605/exact-old-remaining-summary.json`

QA local do P1: candidatos com termos remanescentes após replace: 13.

Aprovação sugerida: **Aprovo P1 produtos**

## Padrões não exatos para tratar depois

- 576x: `etas originais.</dd> <dt>Qual o prazo de entrega?</dt> <dd>Estoque próprio: envio em até N dias úteis. Frete grátis acima de R$ N.</dd> <dt>Como escolher o tamanho?</dt> <dd>Recomendamos escolher seu tamanho habitual. `
- 211x: `etas originais.</dd> <dt>Qual o prazo de entrega?</dt> <dd>Estoque próprio: envio em até N dias úteis. Frete grátis acima de R$ N.</dd> </dl>`
- 90x: `lagem original.</dd> <dt>Qual o prazo de entrega?</dt> <dd>Estoque próprio: envio em até N dias úteis. Sob encomenda: N a N semanas. Frete grátis acima de R$ N.</dd> </dl>`
- 57x: `o habitual.</dd> <dt>Qual o prazo de entrega?</dt> <dd>Produtos em estoque: envio em até N dias úteis. Frete grátis acima de R$ N. Rastreamento em tempo real.</dd> </dl>`
- 28x: `um tamanho.</dd> <dt>Qual o prazo de entrega?</dt> <dd>Produtos em estoque: envio em até N dias úteis. Frete grátis acima de R$ N. Rastreamento em tempo real.</dd> </dl>`
- 13x: `etas originais.</dd> <dt>Qual o prazo de entrega?</dt> <dd>Estoque próprio: envio em até N dias úteis. Frete grátis acima de R$ N.</dd> <dt>Como é o ajuste?</dt> <dd>O Samba OG calça fiel ao tamanho (TTS), mas possui f`
- 12x: `l na marca.</dd> <dt>Qual o prazo de entrega?</dt> <dd>Produtos em estoque: envio em até N dias úteis. Frete grátis acima de R$ N. Rastreamento em tempo real.</dd> </dl>`
- 10x: `de costume.</dd> <dt>Qual o prazo de entrega?</dt> <dd>Produtos em estoque: envio em até N dias úteis. Frete grátis acima de R$ N. Rastreamento em tempo real.</dd> </dl>`
- 10x: `de Project.</dd> <dt>Qual o prazo de entrega?</dt> <dd>Produtos em estoque: envio em até N dias úteis. Frete grátis acima de R$ N. Rastreamento em tempo real.</dd> </dl>`
- 8x: `o ao corpo.</dd> <dt>Qual o prazo de entrega?</dt> <dd>Produtos em estoque: envio em até N dias úteis. Frete grátis acima de R$ N. Rastreamento em tempo real.</dd> </dl>`