# Approval Packet — Air Jordan / Nike x Travis Scott Collection — 2026-06-17

Status: preparado, não executado. Nenhum write externo.

## Target

`/collections/air-jordan-travis-scott`

## Por que é P1

É o próximo movimento mais forte depois do lote Nike Mind:

- Maior cluster de receita da LK: **R$ 1.240.840,90 / 267 unidades / 227 pedidos / 33,8% share** em 90d.
- GSC para `nike travis scott`: **81 cliques / 6.656 impressões / CTR 1,22% / posição 6,1**.
- SERP mobile Brasil para `nike travis scott`: LK aparece orgânico **rank_absolute 3 / rank_group 2**.
- DataForSEO: `nike travis scott` com **8.100 buscas/mês**, intenção transactional.
- Shopify read-only: collection tem descrição, 25 produtos, mas **FAQ não detectado**.

## Escopo proposto

Executar somente:

- `seo.title`
- `seo.description`
- `descriptionHtml` da collection com bloco answer-first + FAQ

Bloqueado:

- produtos da coleção
- preço
- estoque/disponibilidade
- desconto
- feed/GMC
- campanhas
- theme production
- checkout
- Klaviyo/WhatsApp
- outras coleções/produtos

## Campos propostos

Title:
`Nike x Travis Scott Original no Brasil | Air Jordan LK`

Meta:
`Nike x Travis Scott original no Brasil: Air Jordan, Dunk e colaborações Cactus Jack com curadoria LK, autenticidade e atendimento humano.`

Bloco answer-first:

> A coleção Nike x Travis Scott reúne alguns dos sneakers mais desejados da cultura streetwear: Air Jordan 1 Low, Air Jordan 1 High, Dunk, Mac Attack e colaborações Cactus Jack. São modelos de alta procura, com colorways limitadas, leitura premium e forte valor de coleção. Na LK, a curadoria prioriza pares originais, seleção criteriosa e atendimento humano para orientar modelo, tamanho e proposta de uso. Para quem busca Nike Travis Scott original no Brasil, esta página organiza os principais modelos da collab em um só lugar, com linguagem clara para comparar silhuetas, cores e estilos.

FAQ proposta:

### O Nike x Travis Scott vendido na LK é original?
Sim. A LK trabalha com curadoria de produtos originais e atendimento humano para orientar a compra com segurança em modelos Nike, Air Jordan e Travis Scott de alta procura.

### Onde comprar Nike Travis Scott original no Brasil?
Procure uma curadoria que detalhe modelo, colorway, fotos, autenticidade e suporte para escolha de tamanho. A LK reúne seleção premium de Nike x Travis Scott e atendimento humano para uma compra mais segura.

### Qual a diferença entre Air Jordan Travis Scott Low, High e Dunk?
O Air Jordan 1 Low Travis Scott tem perfil mais baixo e versátil. O Air Jordan 1 High tem presença mais clássica e robusta. O Nike SB Dunk Travis Scott tem construção e linguagem ligadas ao skate e ao universo Cactus Jack.

### Por que os tênis Travis Scott x Nike são tão procurados?
A procura vem da combinação entre colaboração limitada, assinatura Cactus Jack, colorways reconhecíveis e relevância cultural do Travis Scott no streetwear e na música.

### Como escolher um Nike Travis Scott para usar no dia a dia?
Para uso mais versátil, comece por cores neutras e silhuetas como Air Jordan 1 Low. Para uma peça de maior impacto, modelos High, Dunk ou colorways raras tendem a ter presença mais forte no styling.


## Impacto esperado

Baseline GSC:

- 81 cliques / 6.656 impressões / CTR 1,22% / posição 6,1.

Uplift simples se a posição se mantiver:

- CTR 1,8%: ~120 cliques, +39 cliques, +47,9%.
- CTR 2,2%: ~146 cliques, +65 cliques, +80,8%.
- CTR 2,5%: ~166 cliques, +85 cliques, +105,4%.

## Risco

Baixo/médio:

- A collection já ranqueia bem; title/meta podem oscilar snippet.
- FAQ/answer block aumenta relevância sem mexer em produtos ou theme.
- Não falar em disponibilidade/estoque como promessa pública.
- Se o storefront repetir cache misto, manter Admin readback + QA público e não escalar outros writes até estabilizar.

## Rollback

Antes de qualquer write:

- backup de `seo.title`, `seo.description`, `descriptionHtml`;
- mutation limitada à collection `air-jordan-travis-scott`;
- readback Admin + QA público/cache-bust;
- se QA falhar, restaurar backup.

## Revisão de impacto

D+7 e D+14:

- GSC page `/collections/air-jordan-travis-scott`;
- queries `nike travis scott`, `air jordan travis scott`, `travis scott jordan`, `nike travis scott original`;
- cliques, impressões, CTR, posição;
- GA4/Shopify organic landing/collection/product click/add-to-cart/receita se disponível.

## Aprovação sugerida

> Aprovo aplicar na coleção `/collections/air-jordan-travis-scott` somente `seo.title`, `seo.description` e descrição/FAQ da coleção conforme o packet Air Jordan Travis Scott 2026-06-17, sem mexer em produtos, preço, estoque, desconto, feed/GMC, campanhas, theme production, checkout, Klaviyo/WhatsApp ou outras coleções/produtos, com backup, QA, rollback e revisão D+7/D+14.

values_printed=false
