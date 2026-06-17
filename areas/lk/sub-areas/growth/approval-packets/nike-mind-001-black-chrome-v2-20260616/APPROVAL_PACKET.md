# Approval Packet v2 — Nike Mind 001 Black Chrome — 2026-06-16

Status: **preview / precisa aprovação explícita para produção**  
Modo: read-only + proposta local  
Writes externos executados: **0**  
values_printed: false  
Owner: LK Growth

## Decisão recomendada

Aplicar uma melhoria pontual no PDP `slide-nike-mind-001-black-chrome-preto` para capturar a demanda de `nike mind 001`, reforçando `original`, `Brasil`, `Black Chrome`, curadoria LK e respostas citáveis.

Não mexer em preço, estoque, desconto, campanhas, GMC/feed, Klaviyo/WhatsApp ou theme production fora do escopo.

## Evidência

### GSC / demanda própria LK

Fonte: GSC read-only router, janela `2026-05-17 → 2026-06-13`.

- `nike mind 001` → PDP Black Chrome: **37.488 impressões / 5 cliques / CTR 0,01% / posição 9,1**.
- `chinelo nike mind 001` → PDP Black Chrome: **10.308 impressões / 6 cliques / CTR 0,06% / posição 6,0**.
- Collection `/collections/nike-mind-001`: **199 cliques / 15.922 impressões / CTR 1,25% / posição 7,5**.

### Comercial / Shopify read-only

Fonte: revenue cluster 90d registrado no Brain.

- Cluster Nike Mind: **R$ 231.199,30 / 70 unidades / 49 pedidos / share 6,3%**.

### SERP / demanda externa

Fonte: DataForSEO Brasil/pt, mobile, 2026-06-16.

- `nike mind 001`: **27.100 buscas/mês**; maio/2026 com **110.000 buscas**; intenção principal **transacional**.
- SERP mobile: Nike.com.br domina orgânico #1/#2; Instagram aparece forte; LK aparece em **Popular Products** como seller para Black Chrome, mas não no Top 10 textual.
- PAA detectadas:
  - `O que o Nike Mind 001 faz?`
  - `Quanto custa o Nike Mind 001?`
  - `Qual a função do Nike Mind?`
  - `Quando o Nike Mind chega ao Brasil?`
  - `O Nike Mind 001 pode ajudar com a ansiedade?`

## Problema

A página já tem conteúdo e estrutura técnica razoáveis, mas o snippet e a hierarquia não capturam bem a busca ampla. O usuário pesquisa `Nike Mind 001`; o H1 atual abre com `Chinelo Slide...`, e a meta não reforça suficientemente `no Brasil` e `original`.

Além disso, o PDP público contém FAQ/blocos operacionais genéricos e repetidos. A melhoria deve ser cirúrgica: mais intenção de busca, menos ruído, sem prometer disponibilidade/prazo e sem transformar disponibilidade em taxonomia pública.

## Escopo aprovado se Lucas confirmar

### A) SEO title

Atual:

`Nike Mind 001 Black Chrome Original | LK Sneakers`

Proposto:

`Nike Mind 001 Black Chrome Original no Brasil | LK`

Motivo: mantém colorway e originalidade, adiciona `Brasil`, remove redundância de marca no final.

### B) Meta description

Atual:

`Nike Mind 001 Black Chrome original na LK: slide escultural com conforto sensorial, curadoria premium e atendimento humano para confirmar o par.`

Proposto:

`Nike Mind 001 Black Chrome original no Brasil: slide escultural da linha Nike Mind com curadoria exclusiva LK, autenticidade e atendimento humano.`

Motivo: mais alinhada a intenção `original no Brasil`, sem prometer disponibilidade/estoque/prazo.

### C) H1 visível

Atual:

`Chinelo Slide Nike Mind 001 Black Chrome Preto`

Proposto:

`Nike Mind 001 Black Chrome original`

Motivo: aproxima H1 da query principal; mantém legibilidade premium.

### D) Bloco answer-first / GEO no PDP

Proposto:

> O Nike Mind 001 Black Chrome é o slide escultural da linha Nike Mind, reconhecido pelo formato anatômico, visual futurista e acabamento preto com efeito cromado. A busca pelo modelo cresceu porque ele mistura conforto sensorial, design de objeto e presença de moda — não é um chinelo básico, mas uma peça de styling para quem procura um Nike Mind original no Brasil. Na LK, a curadoria prioriza pares autênticos, seleção premium e atendimento humano para orientar modelo, tamanho e prazo pelo chat quando necessário. Para quem está comparando versões, o Black Chrome tende a ser a opção mais versátil: funciona com alfaiataria casual, denim, looks minimalistas e produções streetwear, mantendo a leitura experimental da linha Mind sem perder usabilidade.

### E) FAQ canônico proposto

Substituir/organizar a FAQ do PDP para ficar em paridade com FAQPage JSON-LD:

1. **O Nike Mind 001 Black Chrome é original?**  
   Sim. A LK trabalha com curadoria de pares originais, verificação de autenticidade e atendimento humano para orientar a compra com segurança.

2. **Onde comprar Nike Mind 001 original no Brasil?**  
   A LK Sneakers reúne curadoria premium de Nike Mind 001 original no Brasil, com seleção especializada e orientação pelo chat para confirmar modelo, tamanho e detalhes antes da compra.

3. **O Nike Mind 001 tem forma grande ou pequena?**  
   O Mind 001 costuma seguir a numeração Nike. Por ser um slide/mule, o ajuste pode variar conforme formato do pé e preferência de uso; em caso de dúvida, a equipe LK orienta a escolha pelo chat.

4. **Qual a diferença entre Nike Mind 001 e Nike Mind 002?**  
   O Mind 001 tem leitura de slide/mule com visual mais aberto e escultural. O Mind 002 se aproxima mais de uma estrutura fechada. A escolha depende de uso, styling e preferência de calce.

5. **Como usar o Nike Mind 001 Black Chrome no dia a dia?**  
   O Black Chrome funciona com denim, alfaiataria casual, peças minimalistas e composições streetwear. A cor preta com acabamento cromado deixa o modelo versátil sem perder o caráter experimental da linha Mind.

### F) Links internos

- No PDP Black Chrome → `/collections/nike-mind-001` com anchor: `ver curadoria Nike Mind 001 e 002`.
- Da collection Nike Mind → PDP Black Chrome como colorway-chave, se o template/área permitir sem mexer em tema production fora do escopo.

## Métrica de sucesso

- D+7/D+14 GSC por query+URL:
  - `nike mind 001`: CTR sair de **0,01%** para pelo menos **0,3–0,5%** mantendo posição Top 10.
  - `chinelo nike mind 001`: CTR sair de **0,06%** para pelo menos **0,5%**.
- Monitorar cliques orgânicos, posição média, sessões orgânicas no PDP e pedidos influenciados.

## Risco

- Risco SEO: baixo/médio. Pode alterar snippet e CTR; monitorar D+7/D+14.
- Risco comercial: baixo. Não altera preço, estoque, desconto ou promessa pública de disponibilidade.
- Risco de conteúdo: médio se FAQ duplicar com blocos genéricos existentes; execução deve limpar/paralelizar FAQ visível + JSON-LD, não adicionar outra FAQ duplicada.

## Rollback

Antes de qualquer write aprovado:

1. Reconsultar Shopify Admin read-only e salvar `seo.title`, `seo.description`, body/description/H1/FAQ atuais e identificadores.
2. Salvar snapshot rollback em `receipts/`.
3. Aplicar somente campos/textos aprovados.
4. Fazer readback Admin + fetch público com cache-bust.
5. Agendar impact review D+7/D+14.

## Aprovação necessária

Para executar, preciso de aprovação explícita atual, por exemplo:

`Aprovo aplicar o packet v2 Nike Mind 001 Black Chrome de 2026-06-16 somente nos campos/textos listados, com rollback/readback, sem alterar preço, estoque, desconto, campanhas, GMC/feed, Klaviyo/WhatsApp ou theme production fora do escopo.`

## Não executado

- Não alterei Shopify, theme, GMC/feed, GA4/GSC config, Ads, Klaviyo, WhatsApp, preço, estoque ou desconto.
- Não consultei estoque/disponibilidade operacional.
- Não publiquei copy, FAQ, schema ou links internos.

Reminder OS loop needed: yes.  
Reminder OS owner: LK Growth.  
Reminder OS next action: aguardar aprovação explícita de Lucas; se aprovado, executar somente o escopo acima com rollback/readback.  
Reminder OS review trigger: resposta de Lucas ou D+7/D+14 após eventual execução.  
Reminder OS evidence: este approval packet v2 + GSC/Shopify/DataForSEO registrados.  
Status: pending Lucas approval.
