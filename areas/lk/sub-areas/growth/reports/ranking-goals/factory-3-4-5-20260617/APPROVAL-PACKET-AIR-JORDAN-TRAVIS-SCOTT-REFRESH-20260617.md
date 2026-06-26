# Approval Packet — Air Jordan / Nike x Travis Scott Refresh — 2026-06-17

Status: preparado, não executado. Nenhum write externo. values_printed=false.

## Target

`/collections/air-jordan-travis-scott`

## Contexto atualizado

O storefront público já mostra FAQ na collection Travis. Portanto, o refresh proposto não é "adicionar FAQ do zero"; é refinar a página para:

- capturar melhor `Nike x Travis Scott`, `Air Jordan Travis Scott`, `Brasil`, `Cactus Jack` e originalidade;
- reduzir dependência do snippet atual focado só em `Air Jordan Travis Scott`;
- melhorar resposta citável para AI Overview/PAA;
- manter tom premium sem prometer disponibilidade.

## Evidência

- Receita cluster Nike/Jordan/Travis 90d: R$ 1.240.840,90; 267 unidades; 227 pedidos; 33,8% share.
- GSC baseline do Brain para `nike travis scott`: 81 cliques / 6.656 impressões / CTR 1,22% / posição 6,1.
- DataForSEO: `nike travis scott` 8.100/mês; `air jordan travis scott` 1.300/mês; ambos transactional.
- SERP mobile atual: Popular Products acima do orgânico; LK orgânico rank_absolute 4 / rank_group 2; LK citada no AI Overview.
- Public title atual: `Air Jordan Travis Scott Original na LK Sneakers`.
- Public meta atual: `Compre Air Jordan Travis Scott original na LK Sneakers. Alta procura, curadoria premium, autenticidade garantida e opções em até 10x.`

## Escopo aprovado sugerido

Executar somente na collection:

- `seo.title`;
- `seo.description`;
- ajuste do bloco `descriptionHtml`/FAQ answer-first.

Não executar:

- produtos;
- preço;
- estoque/disponibilidade;
- desconto;
- feed/GMC;
- campanhas;
- theme production;
- checkout;
- Klaviyo/WhatsApp;
- outras coleções/produtos.

## Campos propostos

Title:

`Nike x Travis Scott Original no Brasil | Air Jordan LK`

Meta:

`Nike x Travis Scott original no Brasil: Air Jordan, Dunk e colaborações Cactus Jack com curadoria LK, autenticidade e atendimento humano.`

## Bloco answer-first proposto

A coleção Nike x Travis Scott reúne alguns dos sneakers mais desejados da cultura streetwear: Air Jordan 1 Low, Air Jordan 1 High, Dunk, Mac Attack e colaborações Cactus Jack. São modelos de alta procura, com colorways limitadas, leitura premium e forte valor de coleção. Na LK, a curadoria prioriza pares originais, seleção criteriosa e atendimento humano para orientar modelo, tamanho e proposta de uso. Para quem busca Nike Travis Scott original no Brasil, esta página organiza os principais modelos da collab em um só lugar, com linguagem clara para comparar silhuetas, cores e estilos.

## FAQ proposta

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

Cenários simples se a posição se mantiver:

- CTR 1,8%: ~120 cliques, +39 cliques.
- CTR 2,2%: ~146 cliques, +65 cliques.
- CTR 2,5%: ~166 cliques, +85 cliques.

## Risco

Baixo/médio:

- A página já aparece bem e já é citada por AI Overview; qualquer title/meta pode oscilar snippet.
- A alteração deve preservar entidades já reconhecidas: Nike, Travis Scott, Air Jordan, Cactus Jack, LK Sneakers.
- Não usar linguagem pública de estoque/disponibilidade.

## Backup e rollback

Antes de write:

- capturar backup Admin de `seo.title`, `seo.description`, `descriptionHtml`;
- aplicar mutation limitada à collection;
- readback Admin;
- QA público com cache-bust;
- se falhar, restaurar backup.

## Revisão

- D+7 e D+14 em GSC: queries `nike travis scott`, `air jordan travis scott`, `nike travis scott original`, `travis scott jordan`.
- Medir cliques, impressões, CTR, posição.
- Cruzar com GA4/Shopify landing page revenue se disponível.

## Aprovação sugerida

> Aprovo aplicar na coleção `/collections/air-jordan-travis-scott` somente o refresh de `seo.title`, `seo.description` e descrição/FAQ answer-first conforme o packet `APPROVAL-PACKET-AIR-JORDAN-TRAVIS-SCOTT-REFRESH-20260617.md`, sem mexer em produtos, preço, estoque, desconto, feed/GMC, campanhas, theme production, checkout, Klaviyo/WhatsApp ou outras coleções/produtos, com backup, QA, rollback e revisão D+7/D+14.
