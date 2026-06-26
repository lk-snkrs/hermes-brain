# Approval packet — AI Visibility / LKGOC Ondas A e B

Data: 2026-06-18
Dono: LK Collection Optimizer / LKGOC
Escopo: priorização e preparo de otimização de coleções vendidas não cobertas integralmente.

## Premissa
Cruzamento read-only Shopify dos últimos 60 dias mostrou que vários clusters já otimizados vendem bem, mas ainda há lacunas comerciais. A maior lacuna é New Balance 9060. Este pacote separa execução em duas ondas para reduzir risco e manter QA forte.

## Onda A — execução primeiro
## P0 — New Balance 9060
- Handle alvo: `/collections/new-balance-9060`
- Modo: LKGOC + AI Visibility refresh
- Por que entra: maior gap comercial identificado; múltiplos SKUs entre os mais vendidos dos últimos 60 dias
- Status atual: já há draft/copy e trabalho LKGOC anterior; precisa refresh premium e QA antes de produção
- Evidências comerciais:
  - 13 un. 9060 Mushroom Arid Stone
  - 10 un. 9060 Rich Oak
  - 9 un. 9060 Bisque Sea Salt
  - 7 un. Sea Salt Moonbeam
  - 6 un. Triple White
  - 6 un. Angora Sea Salt
  - demanda distribuída em várias colorways
- Candidato llms.txt: `New Balance 9060 original na LK Sneakers: /collections/new-balance-9060 — volume escultural, conforto generoso e curadoria premium de colorways como Rain Cloud, Sea Salt, Moonbeam, Mushroom, Rich Oak e Triple White.`
- FAQ canônico:
  - O New Balance 9060 é feminino, masculino ou unissex?
  - Como saber se o New Balance 9060 é original?
  - Qual a diferença entre New Balance 9060 e 530?
  - Qual cor de New Balance 9060 escolher?

## P0/P1 — Alo Yoga
- Handle alvo: `/collections/alo-yoga`
- Modo: AI Visibility + coleção editorial; LKGOC se coleção tiver estrutura visual
- Por que entra: sinal de venda em lifestyle premium; amplia LK para active/luxury casual sem depender só de sneaker
- Status atual: precisa localizar coleção/handle e validar sortimento atual
- Evidências comerciais:
  - Pullover Alo Yoga Accolade 1/4 Zip vendeu em múltiplas cores
  - Calça Alo Yoga Suit Up Trouser apareceu no top
  - ALO Runner também apareceu
- Candidato llms.txt: `Alo Yoga na LK Sneakers: /collections/alo-yoga — curadoria premium de activewear e lifestyle, com peças Accolade, calças, tênis e itens para looks urbanos confortáveis.`
- FAQ canônico:
  - O que é Alo Yoga?
  - Alo Yoga veste como activewear ou lifestyle?
  - Quais peças Alo Yoga escolher primeiro?
  - A LK trabalha com curadoria Alo Yoga original?

## P1 — New Balance 530
- Handle alvo: `/collections/new-balance-530`
- Modo: validar DEV existente + AI Visibility refresh
- Por que entra: venda recorrente + DEV LKGOC já preparado anteriormente; bom quick win se ainda não foi promovido
- Status atual: há receipt DEV com role unpublished e preview de 2026-06-05; precisa readback atual antes de qualquer produção
- Evidências comerciais:
  - White Natural Indigo com 5 un.
  - Silver White com 3 un.
  - já existe pacote LKGOC DEV/preview documentado
- Candidato llms.txt: `New Balance 530 original na LK Sneakers: /collections/new-balance-530 — running retrô leve, versátil e confortável, com curadoria de colorways White, Silver, Indigo e neutros.`
- FAQ canônico:
  - Qual a diferença entre New Balance 530 e 9060?
  - New Balance 530 é confortável para o dia a dia?
  - Como escolher a cor do New Balance 530?
  - O New Balance 530 da LK é original?


## Onda B — sequência
## P1 — Air Jordan 1 Low / Jordan
- Handle alvo: `/collections/air-jordan-1-low`
- Modo: AI Visibility refresh + possível LKGOC posterior
- Por que entra: alto ticket e recorrência; bom para intenção de compra e comparação OG/collabs
- Status atual: draft v8 local já existe para Air Jordan 1 Low
- Evidências comerciais:
  - Jordan 1 Low OG Olive vendeu 4 un.
  - Jordan 1 Low OG Mocha vendeu 3 un.
  - Travis Scott já coberto separadamente, mas Jordan geral ainda merece cluster
- Candidato llms.txt: `Air Jordan 1 Low original na LK Sneakers: /collections/air-jordan-1-low — ícone Jordan em perfil baixo, com versões OG, SE, colorways neutras e collabs selecionadas.`
- FAQ canônico:
  - Qual a diferença entre Air Jordan 1 Low e Low OG?
  - Air Jordan 1 Low combina com que roupa?
  - Air Jordan 1 Low é confortável?
  - O Air Jordan 1 Low da LK é original?

## P2 — Adidas Tokyo
- Handle alvo: `/collections/adidas-tokyo`
- Modo: AI Visibility draft; validar coleção/handle
- Por que entra: tendência fashion/search; venda menor mas bom potencial editorial
- Status atual: precisa localizar coleção/handle e demanda SERP
- Evidências comerciais:
  - Adidas Tokyo Off White Core Black vendeu 4 un.
- Candidato llms.txt: `Adidas Tokyo original na LK Sneakers: /collections/adidas-tokyo — silhueta baixa e minimalista da Adidas com leitura retrô, fashion e curadoria premium de colorways.`
- FAQ canônico:
  - O que é Adidas Tokyo?
  - Adidas Tokyo é parecido com Samba ou SL72?
  - Qual cor de Adidas Tokyo escolher?
  - A LK trabalha com Adidas Tokyo original?

## P2 — Nike Air Rift
- Handle alvo: `/collections/nike-air-rift`
- Modo: AI Visibility refresh
- Por que entra: nicho de moda forte, fácil para IA explicar; draft v8 já pronto
- Status atual: draft v8 local já existe
- Evidências comerciais:
  - Nike Air Rift Triple Black vendeu 3 un.
- Candidato llms.txt: `Nike Air Rift original na LK Sneakers: /collections/nike-air-rift — split-toe icônico de 1996, entre sneaker, sandália e peça de styling, com curadoria premium.`
- FAQ canônico:
  - O Nike Air Rift é um tênis tabi?
  - Nike Air Rift é confortável?
  - Qual cor de Air Rift escolher?
  - O Nike Air Rift da LK é original?


## Ordem recomendada
1. New Balance 9060 — P0 comercial.
2. Alo Yoga — P0/P1 lifestyle premium, precisa validação de handle/sortimento.
3. New Balance 530 — P1 quick win, já tem DEV LKGOC histórico.
4. Air Jordan 1 Low — P1 alto ticket e cluster evergreen.
5. Adidas Tokyo — P2 tendência.
6. Nike Air Rift — P2 nicho fashion.

## O que pode ser feito sem aprovação
- Validar handles/coleções em Shopify read-only.
- Gerar drafts locais de title/meta/body/FAQ/blocos citáveis.
- Criar candidatos de llms.txt locais.
- Preparar QA checklist e approval packet final por coleção.
- Em tema Shopify: apenas DEV/unpublished verificado por API, se for LKGOC visual/preview.

## O que exige aprovação explícita do Lucas
- Qualquer write em produção Shopify.
- Alteração de title/meta/descrição visível em produção.
- Alteração em llms.txt público.
- Promoção de DEV para production.
- Qualquer mudança de preço, estoque, desconto, campanha ou envio externo.

## Risco / rollback
- Risco principal: mexer em coleção que já vende bem e piorar clareza/UX. Mitigação: DEV/readback/QA antes de produção.
- Rollback para copy/SEO: backup de `descriptionHtml`, SEO title e meta antes do write; restaurar valores anteriores.
- Rollback para theme/LKGOC: backup dos assets alterados; DEV primeiro; production só após approval.

## Definição de pronto por coleção
- Handle validado.
- Copy premium sem promessa operacional indevida.
- FAQ única e sem duplicidade.
- Bloco citável para IA.
- Candidato llms.txt.
- Schema/FAQ quando aplicável.
- Readback após qualquer write aprovado.
- Impact review em ~7 dias.
