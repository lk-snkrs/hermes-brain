# Approval Packet — Nike Mind 002 Black Hyper Crimson — 2026-06-17

Status: preparado, não executado. Nenhum write externo.

## Target

`/products/tenis-nike-mind-002-black-hyper-crimson-preto`

## Por que é o próximo

Depois de Black Chrome, Pearl Pink e hub Nike Mind, o próximo alvo mais lógico é o **Nike Mind 002 Black Hyper Crimson**:

- SERP mobile DataForSEO para `nike mind 002`: LK aparece no orgânico, rank_absolute 9 / rank_group 4.
- A query `nike mind 002` tem volume Brasil **3.600/mês** e intenção transactional.
- O produto está dentro da collection hub Nike Mind.
- Read-only Shopify mostra que o PDP ainda não tem FAQ em `descriptionHtml`.
- O snippet atual é bom, mas genérico; falta reforçar `Brasil`, comparação com 001 e resposta citável para PAA.

## Evidência SERP

Para `nike mind 002` no Google mobile Brasil:

- Nike.com.br rank 1.
- Popular Products aparece cedo na SERP.
- LK aparece organicamente com:
  - title: `Tênis Nike Mind 002 Black Hyper Crimson Preto - LK Sneakers`
  - URL: `/products/tenis-nike-mind-002-black-hyper-crimson-preto`
  - rank_absolute 9 / rank_group 4.

PAA detectado:

- “Qual é o preço do Nike Mind 002?”
- “Para que serve o Nike Mind?”
- “Quando o Nike Mind chega ao Brasil?”
- “Quanto vai custar o Nike Mind?”

## Escopo proposto

Executar somente:

- `seo.title`
- `seo.description`
- `descriptionHtml` com bloco answer-first + FAQ

Bloqueado:

- preço
- estoque/disponibilidade
- desconto
- feed/GMC
- campanhas
- theme production fora do escopo
- checkout
- Klaviyo/WhatsApp
- outros produtos

## Campos propostos

Title:
`Nike Mind 002 Black Hyper Crimson Original no Brasil | LK`

Meta:
`Nike Mind 002 Black Hyper Crimson original no Brasil: sneaker escultural Nike Mind com curadoria exclusiva LK, autenticidade e atendimento humano.`

Bloco answer-first:

> O Nike Mind 002 Black Hyper Crimson leva a linguagem sensorial da linha Nike Mind para um sneaker fechado, com construção escultural, visual técnico e contraste em preto com detalhes Hyper Crimson. Diferente do Mind 001, que tem leitura de slide/mule, o Mind 002 funciona como tênis urbano de presença forte, pensado para quem busca a estética experimental da Nike em um formato mais familiar para o dia a dia. Na LK, a curadoria prioriza Nike Mind original no Brasil, seleção premium e atendimento humano para orientar modelo, tamanho e proposta de uso.

FAQ proposta:

### O Nike Mind 002 Black Hyper Crimson é original?
Sim. A LK trabalha com curadoria de produtos originais e atendimento humano para orientar a compra com segurança em modelos Nike Mind de alta procura.

### Onde comprar Nike Mind 002 original no Brasil?
Procure uma curadoria que detalhe modelo, colorway, fotos, autenticidade e suporte para escolha de tamanho. A LK reúne seleção premium e atendimento humano para uma compra mais segura.

### Qual a diferença entre Nike Mind 001 e Nike Mind 002?
O Nike Mind 001 tem leitura de slide/mule escultural. O Nike Mind 002 é um sneaker fechado, mantendo a linguagem sensorial e futurista da linha Mind em um formato mais urbano.

### O Nike Mind 002 é confortável para uso diário?
O Mind 002 tem proposta de sneaker urbano com construção sensorial. A percepção de conforto pode variar conforme o pé, rotina e referência de uso; para uma escolha mais segura, confirme modelo e tamanho com atendimento humano.

### Como usar o Nike Mind 002 Black Hyper Crimson?
A colorway Black Hyper Crimson combina com looks pretos, denim, peças técnicas e streetwear minimalista. O modelo funciona melhor quando o tênis entra como ponto visual forte da produção.


## Risco

Baixo/médio:

- PDP já ranqueia organicamente para `nike mind 002`; mexer em title/meta pode oscilar snippet.
- Upside é alto porque a página já aparece no top 10 e o CTR pode melhorar com `Original no Brasil` + FAQ.
- Não consultar nem prometer estoque/disponibilidade.

## Rollback

Antes de qualquer write:

- backup de `seo.title`, `seo.description`, `descriptionHtml`;
- mutation limitada ao produto Black Hyper Crimson;
- readback Admin + HTML público/cache-bust;
- se QA falhar, restaurar backup.

## Aprovação sugerida

> Aprovo aplicar no PDP `/products/tenis-nike-mind-002-black-hyper-crimson-preto` somente `seo.title`, `seo.description` e descrição/FAQ do produto conforme o packet Nike Mind 002 Black Hyper Crimson 2026-06-17, sem mexer em preço, estoque, desconto, feed/GMC, campanhas, theme production fora do escopo, checkout, Klaviyo/WhatsApp ou outros produtos, com backup, QA, rollback e revisão D+7/D+14.

values_printed=false
