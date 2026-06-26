# Approval Packet — Nike Mind Hub Collection — 2026-06-17

Status: preparado, não executado. Nenhum write externo.

## Target

`/collections/nike-mind-001`

Coleção existente: **Nike Mind 001 e 002**.

## Por que agora

Depois dos PDPs Black Chrome e Pearl Pink, o próximo passo lógico é reforçar a página hub que pode capturar intenção ampla:

- `nike mind`
- `nike mind 001`
- `nike mind 002`
- `nike mind original`
- `nike mind brasil`
- comparação 001 vs 002

## Evidência read-only

### Shopify/Admin

- Coleção existe: `nike-mind-001`.
- Título atual: `Nike Mind 001 e 002`.
- Produtos na coleção: 18.
- SEO atual:
  - Title: `Nike Mind 001 e 002 Original | LK Sneakers`
  - Meta: `Nike Mind 001 e 002 original na curadoria LK: colorways desejadas, autenticidade e atendimento humano para escolher tamanho, estilo e melhor modelo.`
- Descrição existe.

### HTML público

- HTTP 200.
- Title atual: `Nike Mind 001 e 002 Original | LK Sneakers`.
- H1: `Nike Mind 001/002`.
- FAQ detectado.
- Bloco 001 vs 002 detectado.
- `application/ld+json`: 5 blocos.

### Demanda DataForSEO Brasil

- `nike mind 001`: 27.100/mês; maio 2026: 110.000; intenção transactional.
- `nike mind 002`: 3.600/mês; intenção transactional.
- `nike mind brasil`: 140/mês; intenção transactional/informational.
- `nike mind 001 original`: 70/mês; maio 2026: 720; intenção transactional.

### SERP mobile Brasil — `nike mind 001`

- Nike.com.br domina orgânico 1–2.
- PAA inclui:
  - “O que o Nike Mind 001 faz?”
  - “Quanto custa o Nike Mind 001?”
  - “O Nike Mind 001 pode ajudar com a ansiedade?”
  - “Qual a função do Nike Mind?”
- Popular Products mostra LK para Black Chrome, mas orgânico LK não apareceu no top 20 DataForSEO.

## Diagnóstico

A collection já está boa e não precisa reconstrução. O ganho incremental é:

- colocar `Brasil` no title/meta;
- tornar a resposta 001 vs 002 mais explícita e citável;
- capturar perguntas PAA sem prometer função médica/ansiedade;
- fortalecer a página hub para internal linking dos PDPs otimizados.

## Escopo proposto

Executar somente:

- `seo.title`
- `seo.description`
- `descriptionHtml` com bloco answer-first + FAQ refinado, se aprovado

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

## Campos propostos

Title:
`Nike Mind 001 e 002 Original no Brasil | LK`

Meta:
`Nike Mind 001 e 002 original no Brasil: compare slides e sneakers Nike Mind com curadoria LK, autenticidade e atendimento humano para escolher modelo.`

Bloco answer-first:

> Nike Mind 001 e Nike Mind 002 reúnem a proposta mais sensorial e experimental da Nike: formas esculturais, construção voltada ao contato com o pé e presença visual forte. O Mind 001 tem leitura de slide/mule, mais aberto e fácil de inserir em looks casuais; o Mind 002 leva a mesma linguagem para um sneaker fechado, com uso mais próximo de tênis urbano. Na LK, a curadoria reúne modelos Nike Mind originais no Brasil com seleção premium e atendimento humano para orientar modelo, tamanho e proposta de uso.

FAQ proposta:

### Qual a diferença entre Nike Mind 001 e Nike Mind 002?
O Nike Mind 001 tem leitura de slide/mule escultural, mais aberto. O Nike Mind 002 é um sneaker fechado, mantendo a linguagem sensorial e futurista da linha Mind.

### Onde comprar Nike Mind original no Brasil?
Procure uma curadoria que reúna modelos, colorways, fotos, autenticidade e atendimento humano. A LK organiza a seleção Nike Mind para uma compra mais segura e orientada.

### O Nike Mind 001 é chinelo ou tênis?
O Nike Mind 001 funciona como slide/mule de design escultural. Ele não é um chinelo básico; é uma peça de styling com proposta sensorial e visual futurista.

### O Nike Mind 002 é mais fácil de usar no dia a dia?
Para quem prefere sneaker fechado, o Nike Mind 002 tende a ser mais familiar no uso urbano. O Mind 001 é mais aberto e mais marcante visualmente.

### Como escolher entre Nike Mind 001 e 002?
Escolha o Mind 001 se quiser uma peça aberta, expressiva e de styling. Escolha o Mind 002 se preferir a linguagem Nike Mind em formato de tênis fechado.


## Risco

Baixo/médio:

- É collection visível, então muda copy pública.
- A coleção já tem conteúdo e schema; alteração deve ser incremental.
- Não tocar em theme reduz risco.
- Black Chrome ainda mostra propagação/cache mista; Pearl Pink já passou 6/6.

## Rollback

Antes de qualquer write:

- backup de `seo.title`, `seo.description`, `descriptionHtml`;
- mutation limitada à collection `nike-mind-001`;
- readback Admin + QA público;
- se QA falhar, restaurar backup.

## Aprovação sugerida

> Aprovo aplicar na coleção `/collections/nike-mind-001` somente `seo.title`, `seo.description` e descrição/FAQ da coleção conforme o packet Nike Mind Hub Collection 2026-06-17, sem mexer em produtos, preço, estoque, desconto, feed/GMC, campanhas, theme production, checkout, Klaviyo/WhatsApp ou outras coleções/produtos, com backup, QA, rollback e revisão D+7/D+14.

values_printed=false
