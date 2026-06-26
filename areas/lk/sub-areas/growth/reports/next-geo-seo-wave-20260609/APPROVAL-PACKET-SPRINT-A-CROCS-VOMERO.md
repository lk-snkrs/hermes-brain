# Approval Packet — Sprint A Crocs McQueen + Nike Vomero Premium

Data: 2026-06-09T18:45:29.820819+00:00
Escopo: SEO/GEO read-only + propostas para Shopify SEO/content.
Status: **aguardando aprovação antes de qualquer write em produção**.

## Resumo executivo

Priorizar dois clusters:

1. **Crocs Relâmpago McQueen**
   - Melhor oportunidade imediata: 33.100 buscas/mês, intenção transacional.
   - Cluster pequeno e fácil de consolidar.
   - Ajuste principal: fortalecer termo brasileiro `Relâmpago McQueen`, reduzir fragmentação entre `/crocs-mcqueen` e `/crocs-relampago-mcqueen`, e criar bloco FAQ/citável.

2. **Nike Vomero Premium**
   - 22.200 buscas/mês, intenção transacional e tendência anual muito forte.
   - Cluster já tem coleção, guia, blogs e PDPs.
   - Ajuste principal: encurtar metas longas, reforçar links internos e padronizar narrativa `ZoomX + Air Zoom + lifestyle premium`.

## O que foi verificado

Arquivos gerados:

- `NEXT-WAVE-PACKET.md`
- `site-discovery.json`
- `sprint-a-crocs-vomero-audit.json`

Verificação pública:

- Todas as URLs auditadas retornaram **200**.
- Product/Collection/FAQ/Blog schema aparecem onde esperado em várias páginas.
- O erro transitório visto no PDP `nike-vomero-premium-alabaster-amarelo` foi revalidado: a página carregou corretamente.

## Aprovação solicitada — pacote P1

Aprovar ajustes de conteúdo/SEO em Shopify para as URLs abaixo, com snapshot antes/depois e rollback.

### Crocs Relâmpago McQueen

#### 1. Collection principal

URL: `https://lksneakers.com.br/collections/crocs-relampago-mcqueen`

Estado atual:

- Title: `Crocs Relâmpago McQueen: 1 modelos | LK Sneakers`
- Meta description: `Crocs Relâmpago McQueen para fãs do filme Carros da Pixar. Todos os modelos disponíveis com autenticidade garantida. Parcele em 10x, frete grátis acima de R$ 500. Loja física Jardins SP.`
- H1: `Crocs Relâmpago McQueen`

Proposta:

- Title: `Crocs Relâmpago McQueen Original | LK Sneakers`
- Meta: `Crocs Relâmpago McQueen original na curadoria LK: design Cars, autenticidade e atendimento humano para escolher com segurança.`

Motivo:

- Remove contagem `1 modelos`, que envelhece mal e pode conflitar com estoque/grade.
- Mantém linguagem premium e evita promessa de disponibilidade.

#### 2. Collection alternativa

URL: `https://lksneakers.com.br/collections/crocs-mcqueen`

Estado atual:

- Title: `Crocs McQueen: 1 modelos | LK Sneakers`
- H1: `Crocs McQueen`

Proposta:

- Manter como apoio/sinônimo, mas linkar de forma clara para a collection principal `crocs-relampago-mcqueen`.
- Se possível via Shopify SEO: title `Crocs McQueen Original | Relâmpago McQueen LK`.
- Evitar transformar em segunda landing principal.

Motivo:

- A busca brasileira é majoritariamente `crocs relampago mcqueen`, não `crocs lightning mcqueen`.
- Reduz risco de canibalização.

#### 3. Guia Crocs

URL: `https://lksneakers.com.br/pages/crocs-relampago-mcqueen-guia`

Estado atual:

- Title: `Crocs Relâmpago McQueen | Guia LK`
- Meta: `Guia LK do Crocs Relâmpago McQueen: versões, detalhes, autenticidade e como escolher com atendimento humano.`

Proposta:

- Title: `Crocs Relâmpago McQueen Original | Guia LK`
- Meta: `Guia LK do Crocs Relâmpago McQueen original: detalhes, autenticidade, numeração e como escolher com curadoria premium.`

Bloco citável sugerido:

```text
O Crocs Relâmpago McQueen original é a versão Classic Clog inspirada no personagem de Cars, reconhecida pelo vermelho intenso, olhos no cabedal e acabamento temático. Na LK, a curadoria prioriza autenticidade, atendimento humano e orientação para escolher o tamanho com segurança.
```

FAQ sugerido:

- `O Crocs Relâmpago McQueen é o mesmo Lightning McQueen?`
  - `Sim. No Brasil, a busca costuma usar Relâmpago McQueen; internacionalmente, o personagem aparece como Lightning McQueen.`
- `Como escolher o tamanho do Crocs Relâmpago McQueen?`
  - `A recomendação é confirmar a numeração com atendimento humano, considerando o caimento amplo do Classic Clog e a preferência de uso.`
- `Como saber se o Crocs Relâmpago McQueen é original?`
  - `Observe acabamento, proporção, marcações, material e procedência. A LK trabalha com curadoria e autenticidade como premissas de compra.`

Atenção:

- Não inserir promessa de estoque, pronta entrega, tamanho disponível ou reposição. Se precisar falar disponibilidade, acionar `lk-stock`.

### Nike Vomero Premium

#### 4. Collection principal

URL: `https://lksneakers.com.br/collections/nike-vomero-premium`

Estado atual:

- Title: `Nike Vomero Premium — Comprar | LK Sneakers`
- Meta: `Nike Vomero Premium: running heritage com amortecimento Zoom Air e design contemporâneo. 15 modelos na LK Sneakers, Jardins SP. Frete grátis, 10x sem juros.`
- H1: `Nike Vomero Premium`

Proposta:

- Title: `Nike Vomero Premium Original | LK Sneakers`
- Meta: `Nike Vomero Premium original na curadoria LK: ZoomX, Air Zoom, design running lifestyle e atendimento humano para escolher.`

Motivo:

- Remove contagem `15 modelos`, que pode ficar incorreta.
- Fortalece tecnologia e uso lifestyle sem parecer marketplace genérico.

#### 5. Guia Nike Vomero Premium

URL: `https://lksneakers.com.br/pages/nike-vomero-premium-guia`

Estado atual:

- Title: `Nike Vomero Premium | Guia LK`
- Meta: `Guia LK do Nike Vomero Premium: tecnologia, conforto, design e como escolher modelos desejados com segurança.`

Proposta:

- Title: `Nike Vomero Premium Original | Guia LK`
- Meta: `Guia LK do Nike Vomero Premium: ZoomX, Air Zoom, conforto máximo, estética running e como escolher com curadoria.`

Bloco citável sugerido:

```text
O Nike Vomero Premium combina espuma ZoomX, unidades Air Zoom e proporção maximalista para criar um running de conforto extremo com leitura lifestyle. É uma escolha para quem busca presença visual, tecnologia Nike e uma silhueta contemporânea fora do óbvio.
```

FAQ sugerido:

- `O Nike Vomero Premium é confortável?`
  - `Sim. O modelo combina espuma ZoomX e unidades Air Zoom, criando uma sensação de amortecimento alto e macio.`
- `Nike Vomero Premium é para corrida ou lifestyle?`
  - `A origem é running, mas a leitura atual também é lifestyle: volume, tecnologia e presença visual para uso urbano.`
- `Qual a diferença entre Vomero Premium e Air Max?`
  - `O Vomero Premium enfatiza espuma ZoomX e Air Zoom com estética running maximalista; Air Max costuma destacar a cápsula Air visível como assinatura visual.`

#### 6. Blog Vomero principal

URL: `https://lksneakers.com.br/blogs/novidades/nike-vomero-premium-o-running-que-virou-lifestyle`

Achado:

- Meta description atual tem **320 caracteres**, longa demais para snippet.

Proposta:

- Meta: `Nike Vomero Premium une ZoomX, Air Zoom e estética running maximalista. Entenda por que virou peça lifestyle em 2026.`

#### 7. PDPs Nike Vomero Premium

URLs auditadas:

- `tenis-nike-vomero-premium-alabaster-amarelo`
- `tenis-nike-vomero-premium-barely-green-verde`
- `tenis-nike-vomero-premium-barely-volt-cinza`

Achados:

- Titles de PDP com preço podem passar de 80 caracteres.
- Algumas metas têm 320 caracteres e parecem puxar texto do corpo.
- O PDP Barely Volt tem `Verde` no title/H1 apesar do slug terminar em `cinza`; precisa revisão de product data antes de qualquer ajuste.

Proposta geral:

- Padronizar title sem preço quando possível:
  - `Tênis Nike Vomero Premium [Colorway] | LK Sneakers`
- Meta curta:
  - `Nike Vomero Premium [Colorway] original: ZoomX, Air Zoom e curadoria LK com atendimento humano para escolher.`

Atenção:

- Divergência de cor/slug é catálogo/product data quality; revisar antes de publicar.
- Se houver implicação de disponibilidade/grade, acionar `lk-stock`.

## Mapa de links internos recomendado

### Crocs

- Collection principal deve linkar para:
  - Guia Crocs Relâmpago McQueen
  - Blog "onde comprar"
  - PDP Crocs Lightning/Relâmpago McQueen
- Guia deve linkar para:
  - Collection principal
  - PDP
  - Blog de compra/autenticidade
- Blog deve linkar para:
  - Collection principal no primeiro terço do texto
  - Guia como fonte evergreen

Anchor texts sugeridos:

- `Crocs Relâmpago McQueen original`
- `guia do Crocs Relâmpago McQueen`
- `Crocs Lightning McQueen na curadoria LK`

### Nike Vomero Premium

- Collection deve linkar para:
  - Guia Nike Vomero Premium
  - Blog running/lifestyle
  - Comparativo Vomero Premium vs Air Max
- Guia deve linkar para:
  - Collection
  - Blog principal
  - Comparativo
- PDPs devem linkar para:
  - Collection Nike Vomero Premium
  - Guia Nike Vomero Premium

Anchor texts sugeridos:

- `Nike Vomero Premium original`
- `guia Nike Vomero Premium`
- `Vomero Premium vs Air Max`
- `running lifestyle premium`

## Checklist dos 18 tópicos canônicos

- GA4: faltam dados autenticados atuais; não decision-grade para receita/CVR.
- GSC: faltam clicks/impressions/CTR/posição atuais por URL/query.
- GMC: não auditado nesta Sprint; necessário antes de campanhas de produto.
- Shopify SEO: auditado publicamente; ajustes propostos para title/meta/H1/copy.
- Shopify CRO/theme: não alterado; apenas recomendações de links/blocos.
- GEO/AI Search: incluído com blocos citáveis e FAQ.
- PageSpeed/CrUX/CWV: não auditado nesta Sprint.
- Schema: schema público detectado; FAQ/Product/Collection/Blog aparecem em URLs relevantes.
- Reviews/prova social: schema AggregateRating detectado; não auditado fonte/reviews.
- Paid media: não alterado; demanda pode informar campanhas futuras.
- Influencer/social demand: não auditado nesta Sprint.
- Concorrência/SERP: demanda e SERP pública parcialmente usadas; falta SERP individual aprofundada.
- Google Business/local: apenas menções Jardins detectadas; não auditado GBP.
- Klaviyo/CRM signals: não auditado.
- Catálogo/product data quality: achado potencial em Nike Vomero Barely Volt `verde` vs slug `cinza`; revisar.
- Conteúdo/taxonomia comercial: auditado; recomendar consolidação Crocs.
- Mensuração/QA eventos: não auditado.
- Impact review/experimentation: sugerir revisão em D+7/D+14 após publicação.

## Aprovação necessária

Preciso de aprovação explícita para qualquer uma das ações abaixo:

- Editar title/meta/descrição em Shopify production.
- Editar páginas, collections, blogs ou PDPs em production.
- Ajustar links internos em production.
- Corrigir product data visível ao cliente.

## Rollback

Antes de publicar:

1. Salvar snapshot de title/meta/body atual por URL.
2. Aplicar mudanças em lote pequeno.
3. Validar URLs 200 + snippets/schema após publicação.
4. Reverter pelo snapshot se houver queda técnica, erro visual ou desalinhamento comercial.
5. Revisar impacto em GSC/GA4 aproximadamente D+7/D+14.
