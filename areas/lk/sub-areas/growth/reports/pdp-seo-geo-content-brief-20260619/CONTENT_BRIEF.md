# LK PDP SEO/GEO/AI Visibility — Content brief — Pacote B revisado

Criado: `2026-06-19T20:09:07.241467+00:00`

**Modo:** read-only / brief de conteúdo. Nenhum write Shopify executado.

## Fontes usadas

- **claude_seo_skill:** seo-content + seo-ecommerce + seo-page lens from Claude-SEO upstream mapping
- **shopify_admin:** shopify-admin-current-pdp-content.json
- **semrush:** source-ahrefs-semrush-snapshot.json; crawl finished; content/schema issues still broad, so avoid adding body FAQ duplication
- **ahrefs:** local Ahrefs top organic keywords file; only Light Smoke Grey row had no keywords, other Package B handles not in available top50 final snapshot; issues show schema.org validation noise sitewide
- **dataforseo:** Google keyword overview, intent, mobile SERP/PAA, AI keyword volume
- **ai_mentions:** DataForSEO AI mentions endpoint returned 402 access denied; not used as decision-grade

## Regras globais Claude-SEO aplicadas

- Description body_html = editorial/commercial, not FAQ container.
- FAQ = custom.faq JSON / theme FAQ source; maintain parity with FAQPage schema after propagation.
- Use exact entity in first sentence; repeat naturally, not stuffing.
- No stock/availability/pronta entrega/prazo promises; no medical/therapeutic claims.
- Answers should be citation-ready: direct first sentence, then LK context.
- Avoid price in FAQ/body; price/availability belong to product UI/chat.

## Direção estratégica

- **Descrição:** editorial, curta, premium e citável; não usar como container de perguntas.
- **FAQ:** no `custom.faq` / estrutura do tema; perguntas diretas com respostas úteis para PAA/AI.
- **Schema:** validar depois que o tema renderizar o `custom.faq`; evitar duplicidade com FAQ antiga no body.

## Cluster: nike_mind_slide_001

- Demanda/intenção: `{'google_volume_nike_mind_001': 27100, 'google_volume_nike_mind_002': 3600, 'intent': 'transactional with informational secondary', 'ai_volume_nike_mind_001': 26, 'ai_volume_nike_mind_slide_001': 1}`
- Estratégia de entidade: Use Nike Mind Slide 001 in LK copy for clarity, but include Mule/slide once to match official/SERP vocabulary. Keep Nike Mind 001 in FAQ/question phrasing for demand.
- SERP/PAA:
  - Official BR result names it Mule Nike Mind 001; SERP also shows slide/mule language.
  - PAA asks what it does, price, anxiety, launch in Brazil; answer must avoid health promises.
  - Related searches include onde comprar, brasil, original, preço, para que serve, feminino.

## Cluster: vomero_premium

- Demanda/intenção: `{'google_volume_nike_vomero_premium': 27100, 'intent': 'informational/commercial', 'ai_volume': 10}`
- Estratégia de entidade: Use full model/color in body, but FAQ should answer generic Nike Vomero Premium questions to capture informational SERP.
- SERP/PAA:
  - Official snippet emphasizes amortecimento máximo and Air Zoom duplas.
  - PAA asks what it is, what Vomero line is, what it is for, Premium vs Plus, and whether it serves for running.
  - SERP has strong image/video/review layer; copy must answer performance + lifestyle without overclaiming.

## Cluster: dunk_cacao_wow

- Demanda/intenção: `{'google_volume_dunk_cacao_wow': 260, 'google_volume_nike_dunk_cacao_wow': 140, 'intent': 'informational/transactional mix', 'ai_volume': 6}`
- Estratégia de entidade: Use Nike Dunk Low Cacao Wow; mention feminino/grade only as model identity if factual, not availability; avoid gendered exclusion.
- SERP/PAA:
  - Official title: Tênis Nike Dunk Low Cacao Wow Feminino.
  - SERP and products emphasize Sail/Cacao Wow/Coconut Milk, marrom/branco, leather and Dunk 80s basketball heritage.
  - Related searches include feminino, masculino, 36, infantil, original.

## PDP: `slide-nike-mind-001-light-smoke-grey-cinza`

### Descrição recomendada

```html
<p><strong>Nike Mind Slide 001 Light Smoke Grey original</strong> na curadoria LK.</p>
<p>O Nike Mind Slide 001 Light Smoke Grey combina construção escultural, leitura futurista e tom cinza claro em uma proposta de mule/slide com presença de moda.</p>
<p>A silhueta aberta entrega uma experiência diferente de um sneaker tradicional: mais visual, sensorial e voltada a styling do que a performance esportiva.</p>
<h2>Por que escolher este modelo?</h2>
<ul>
<li>Design escultural da linha Nike Mind em formato mule/slide.</li>
<li>Cor Light Smoke Grey com estética futurista, mas fácil de combinar.</li>
<li>Curadoria LK com foco em autenticidade, seleção premium e atendimento humano para orientar a escolha.</li>
</ul>
```

### FAQ recomendada

- **O que é o Nike Mind 001?**
  - O Nike Mind 001 é um mule/slide experimental da Nike com construção escultural e proposta sensorial para o contato com o pé. Ele é mais indicado para lifestyle, descanso e styling do que para corrida ou treino técnico.
- **O Nike Mind Slide 001 Light Smoke Grey é original?**
  - Sim. A curadoria LK trabalha com produtos originais e seleção premium, com atendimento humano para orientar autenticidade, modelo e melhor escolha.
- **Nike Mind 001 ajuda com ansiedade?**
  - A LK não trata o Nike Mind 001 como produto médico nem promete efeito terapêutico. A proposta do modelo é sensorial e de bem-estar no uso, com design pensado para uma experiência diferente de calce.
- **Qual tamanho escolher no Nike Mind Slide 001?**
  - A recomendação é partir da sua numeração habitual em Nike. Se você estiver entre dois tamanhos ou tiver dúvida de calce, fale com o atendimento LK antes da compra.
- **Como combinar o Light Smoke Grey?**
  - O tom cinza claro funciona bem com peças neutras, calças amplas, shorts e looks minimalistas, mantendo a presença futurista do modelo sem pesar a composição.

## PDP: `slide-nike-mind-001-pearl-pink-rosa`

### Descrição recomendada

```html
<p><strong>Nike Mind Slide 001 Pearl Pink original</strong> na curadoria LK.</p>
<p>O Nike Mind Slide 001 Pearl Pink leva a construção escultural da linha Nike Mind para uma leitura rosa clara, futurista e mais expressiva.</p>
<p>É uma peça de impacto para quem busca um slide/mule com presença fashion, visual sensorial e proposta diferente de um sneaker fechado.</p>
<h2>Por que escolher este modelo?</h2>
<ul>
<li>Silhueta experimental Nike Mind em formato aberto.</li>
<li>Colorway Pearl Pink com leitura statement, mas suave.</li>
<li>Curadoria LK com autenticidade, seleção premium e orientação humana para tamanho e estilo.</li>
</ul>
```

### FAQ recomendada

- **O que diferencia o Nike Mind Slide 001 Pearl Pink?**
  - O Pearl Pink combina a silhueta escultural do Nike Mind 001 com uma cor rosa clara de presença fashion. É uma escolha mais expressiva que versões neutras, sem perder leitura minimalista.
- **O Nike Mind Slide 001 Pearl Pink é original?**
  - Sim. A curadoria LK trabalha com produtos originais e seleção premium, com atendimento humano para apoiar a escolha.
- **Nike Mind 001 é tênis de corrida?**
  - Não. O Nike Mind 001 funciona melhor como mule/slide de lifestyle, conforto e styling. Para corrida ou treino técnico, a proposta do produto não é a mesma de um tênis de performance.
- **Qual tamanho escolher no Nike Mind Slide 001?**
  - Use sua numeração habitual em Nike como referência. Em caso de dúvida entre dois tamanhos, o atendimento LK pode orientar antes da compra.
- **Como usar o Nike Mind Slide 001 rosa?**
  - O Pearl Pink funciona como ponto de cor em looks neutros, peças claras, jeans, alfaiataria casual e produções com estética mais fashion.

## PDP: `tenis-nike-vomero-premium-white-bright-crimson-branco`

### Descrição recomendada

```html
<p><strong>Nike Vomero Premium White Bright Crimson original</strong> na curadoria LK.</p>
<p>O Nike Vomero Premium eleva a linha Vomero com visual maximalista, amortecimento generoso e uma combinação White Bright Crimson de alta presença.</p>
<p>A proposta une conforto, tecnologia Nike e estética contemporânea, funcionando tanto para quem busca sensação macia quanto para quem quer um sneaker de impacto visual.</p>
<h2>Por que escolher este modelo?</h2>
<ul>
<li>Silhueta premium da família Nike Vomero, com foco em amortecimento máximo.</li>
<li>Colorway White Bright Crimson com contraste esportivo e leitura fashion.</li>
<li>Curadoria LK com autenticidade, seleção premium e atendimento humano para orientar tamanho e uso.</li>
</ul>
```

### FAQ recomendada

- **O que é o Nike Vomero Premium?**
  - O Nike Vomero Premium é uma versão de alta presença da família Vomero, com foco em amortecimento máximo, conforto e visual robusto. Ele combina tecnologia Nike com uma estética mais premium e contemporânea.
- **O Nike Vomero Premium serve para corrida?**
  - O Vomero Premium nasce da linguagem de corrida da Nike e prioriza conforto e amortecimento. Para uso técnico ou escolha de treino, vale considerar seu tipo de pisada, rotina e expectativa; para a LK, ele também tem forte leitura lifestyle.
- **Qual a diferença entre Vomero Premium e outros Vomero?**
  - O Premium tem proposta mais maximalista, com maior presença visual e foco em sensação macia. Outros Vomero podem ser mais discretos ou mais voltados ao uso diário tradicional.
- **O Nike Vomero Premium White Bright Crimson é original?**
  - Sim. A curadoria LK trabalha com produtos originais e seleção premium, com atendimento humano para orientar autenticidade, tamanho e melhor contexto de uso.
- **Como escolher o tamanho no Nike Vomero Premium?**
  - A referência inicial é sua numeração habitual em Nike. Se você estiver entre dois tamanhos ou busca um ajuste específico, fale com a equipe LK antes da compra.

## PDP: `tenis-nike-dunk-low-cacao-wow-marrom`

### Descrição recomendada

```html
<p><strong>Nike Dunk Low Cacao Wow original</strong> na curadoria LK.</p>
<p>O Nike Dunk Low Cacao Wow combina a silhueta clássica do Dunk com uma paleta marrom, Sail e Coconut Milk, criando uma leitura quente, versátil e fácil de usar.</p>
<p>Com estética inspirada no basquete dos anos 80 e presença urbana, o modelo funciona bem em produções casuais, neutras e vintage.</p>
<h2>Por que escolher este modelo?</h2>
<ul>
<li>Colorway Cacao Wow com tons marrom e off-white de alta versatilidade.</li>
<li>Silhueta Nike Dunk Low clássica, com presença casual e urbana.</li>
<li>Curadoria LK com autenticidade, seleção premium e atendimento humano para orientar tamanho e estilo.</li>
</ul>
```

### FAQ recomendada

- **O Nike Dunk Low Cacao Wow é original?**
  - Sim. A curadoria LK trabalha com produtos originais e seleção premium, com atendimento humano para orientar autenticidade, tamanho e escolha do modelo.
- **Quais são as cores do Dunk Cacao Wow?**
  - O Nike Dunk Low Cacao Wow é conhecido pela combinação de marrom Cacao Wow com tons claros como Sail e Coconut Milk, criando uma leitura neutra, quente e fácil de combinar.
- **O Dunk Cacao Wow é feminino ou masculino?**
  - O modelo aparece frequentemente associado à linha feminina, mas o mais importante é conferir a equivalência de tamanho. A equipe LK pode orientar a melhor escolha de numeração antes da compra.
- **Como combinar o Nike Dunk Low Cacao Wow?**
  - Ele combina bem com jeans, alfaiataria casual, peças bege, branco, marrom, preto e looks de estética vintage. A paleta neutra facilita o uso no dia a dia.
- **Qual tamanho escolher no Nike Dunk Low Cacao Wow?**
  - Use sua numeração habitual em Nike Dunk como referência. Se estiver entre dois tamanhos, fale com o atendimento LK para uma orientação humana antes da compra.

## Próximo passo recomendado

1. Aguardar propagação da amostra Light Smoke Grey.
2. Validar público: descrição limpa + FAQ do tema + FAQPage JSON-LD atualizado.
3. Se OK, preparar approval packet para aplicar este brief nos 4 PDPs com backup/rollback.
