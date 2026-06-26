# LKGOC Full — New Balance 9060 — pacote inicial

Criado: 2026-06-05T09:24:34Z
Status: **preflight/evidence inicial** — sem write Shopify/produção.

## Input contract

- Nome da coleção/modelo: New Balance 9060
- Handle existente identificado publicamente: `/collections/new-balance-9060`
- URL pública: https://lksneakers.com.br/collections/new-balance-9060
- Nível: **Full LKGOC**
- Tipo: refactor/otimização de coleção existente
- Referência visual coleção: New Balance 204L gold source
- Referência guia dedicado: NB204L/Moon Shoe guide padrão LKGOC
- Produtos incluídos: página pública indica **51 itens**
- Produto âncora sugerido: New Balance 9060 Rain Cloud / Sea Salt / Grey-Beige conforme disponibilidade comercial
- Objetivo comercial: capturar demanda transacional alta + reforçar curadoria/autenticidade + melhorar conversão do grid 9060
- Evidência DataForSEO: coletada
- Evidência SERP/PAA: coletada
- Evidência pública LK: coletada via fetch da collection
- Evidência Shopify/GA4/GSC/GMC: **pendente**; relatório ainda não decision-grade para priorização fina por receita/conversão

## Evidência de demanda — Google Brasil / DataForSEO

- `new balance 9060`: 246.000 buscas/mês; tendência anual +82%; intenção transacional; competição HIGH.
- `tênis new balance 9060`: 22.200 buscas/mês; tendência anual +50%; intenção transacional.
- `new balance 9060 feminino`: 18.100 buscas/mês; tendência anual +83%; intenção transacional.
- `new balance 9060 original`: 4.400 buscas/mês; intenção transacional.
- `new balance 9060 masculino`: 3.600 buscas/mês; intenção transacional.
- `new balance 9060 brasil`: 170 buscas/mês; tendência anual +136%.

## Evidência GEO/AI Search

- `new balance 9060`: AI search volume 559 em 2026-05, com crescimento vs meses anteriores.
- `new balance 9060 original`: AI search volume 19 em 2026-05.
- Perguntas de autenticidade aparecem tanto em IA quanto PAA; oportunidade clara para bloco citável e FAQ/schema.

## SERP — concorrência e intenção

Top organic/PAA observado para `new balance 9060`:

- #1 New Balance oficial — título enfatiza cores exclusivas, feminino/masculino e conforto.
- #2 Netshoes — snippet: estilo chunky, conforto, uso fora do universo performance.
- Popular products com sellers: Droper, HypeWalk, Artwalk, Amazon, Track&Field, Maze, New Balance.
- PAA relevante:
  - Qual é melhor, New Balance 530 ou 9060?
  - Quanto custa o 9060 nos EUA?
  - Qual o valor do New Balance 9060 original?
  - Como saber se o NB-9060 é original?
  - Qual o New Balance 9060 mais vendido?
  - Qual a diferença do New Balance 9060 original e falso?
- Related searches: New Balance 530, 9060 feminino, Sea Salt, Black, preto, branco.

## Diagnóstico público LK atual

Página atual existe e já tem boa base editorial:

- H2 atual: “Volume escultural, presença imediata.”
- Texto atual posiciona 9060 como leitura expressiva, conforto, proporção ampla e visual contemporâneo.
- Página mostra 51 itens.
- FAQ atual contém 4 perguntas.

Gaps/riscos:

- FAQ público atual menciona “produtos em estoque” e prazo de entrega — desalinhado ao guardrail LK de não usar estoque/pronta entrega/prazo como taxonomia pública.
- Falta pacote Full LKGOC auditável: guia dedicado, CTA cruzado, blocos citáveis mais fortes, evidence packet completo, scorecard e QA visual DEV.
- A página pública ainda precisa ser tratada como insumo, não como base final; regra Lucas = rewrite/refactor canônico.

## Direção CLAUDE-SEO / LKGOC

Entidades principais:

- New Balance 9060
- ABZORB / SBS / entressola escultural / inspiração running anos 2000
- colorways: Rain Cloud, Sea Salt, Moonbeam, Triple White, Black/preto, Grey Beige
- intenção: compra, autenticidade, comparação com 530/1906R/2002R, styling, conforto, numeração

Estrutura recomendada:

1. Coleção produto-first no padrão 204L.
2. Hero/copy curta premium: volume escultural, conforto e curadoria autenticada.
3. Grid de produtos antes de conteúdo longo.
4. Guia pós-grid com styling, colorways e comparação 9060 vs 530/2002R/1906R.
5. FAQ sem promessas operacionais públicas.
6. Guia dedicado `/pages/new-balance-9060-original-brasil-guia-lk` ou `/pages/guia-new-balance-9060-original-brasil`.
7. Blocos citáveis para GEO/AI: “O que é”, “como veste”, “como escolher cor”, “como verificar autenticidade”, “9060 vs 530”.

## Copy draft — direção, não publicar ainda

H1 sugerido: New Balance 9060

Meta title sugerido: New Balance 9060 Original | Curadoria LK Sneakers

Meta description sugerida: New Balance 9060 original em curadoria premium da LK Sneakers. Explore versões femininas, masculinas e unissex, com autenticidade verificada e atendimento humano.

Primeiro bloco sugerido:

> O New Balance 9060 combina volume escultural, conforto generoso e estética retrô-futurista em uma das silhuetas mais desejadas da marca. Na LK Sneakers, a curadoria reúne versões originais do 9060 — de neutros como Rain Cloud, Sea Salt e Moonbeam a colorways de maior presença — com seleção pensada para quem busca autenticidade, proporção e acabamento premium.

FAQ proposta:

1. O New Balance 9060 é feminino, masculino ou unissex?
2. Como saber se o New Balance 9060 é original?
3. Qual a diferença entre New Balance 9060 e New Balance 530?
4. O New Balance 9060 é confortável para uso diário?
5. Como escolher a melhor cor do New Balance 9060?
6. O New Balance 9060 veste grande ou pequeno?

## Plano DEV/preview

- Criar pacote Full LKGOC em ambiente DEV/unpublished verificado por API antes de qualquer write.
- Se o tema alvo `155065450718` estiver `role: main`, abortar write e exigir cópia/tema unpublished ou aprovação explícita de produção; padrão seguro é DEV/unpublished.
- Produção só depois de preview, QA visual desktop/mobile, scorecard >=85 e aprovação Lucas.

## Approval packet esperado depois do DEV

- Link preview coleção com `preview_theme_id`.
- Link preview guia dedicado.
- Screenshots desktop/mobile.
- Score LKGOC.
- Readback Asset API/HTML.
- Rollback snapshot.
- Decisão pedida: aprovar merge DEV → Production.
