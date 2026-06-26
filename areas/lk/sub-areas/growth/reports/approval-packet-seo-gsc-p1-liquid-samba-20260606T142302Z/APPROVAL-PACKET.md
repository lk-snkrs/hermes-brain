# Approval Packet — LK SEO/GSC P1 + Liquid error Samba Jane

Data UTC: 20260606T142302Z
Status: preparado read-only. Nenhum write externo executado.

## Decisão pedida ao Lucas

Aprovar ou não o seguinte lote pequeno:

1. Corrigir em produção o erro público da coleção Adidas Samba Jane.
2. Aplicar title/meta do lote GSC P1 em Shopify.
3. Rodar QA pós-publicação e review de impacto em ~7 dias.

## Por que agora

- GSC mostra demanda real com CTR muito baixo em páginas já posicionadas.
- A coleção Adidas Samba Jane tem erro Liquid visível em produção.
- Várias metas/titles atuais estão longas, truncadas, genéricas ou com preço no title, reduzindo clareza premium no snippet.

## Parte A — Hotfix Adidas Samba Jane

Página afetada:

`https://lksneakers.com.br/collections/adidas-samba-jane`

Erro público atual:

`Liquid error (sections/lk-collection line 951): Could not find asset snippets/lk-samba-jane-editorial-v3.liquid`

Diagnóstico local:

- O section `sections/lk-collection.liquid` chama `snippets/lk-samba-jane-editorial-v3.liquid`.
- Existe um candidate anterior no Brain com o snippet completo:
  - `areas/lk/sub-areas/growth/receipts/theme-dev/samba-jane-placeholder-hotfix-156623372510-20260603T151135Z/candidate__snippets__lk-samba-jane-editorial-v3.liquid`
- O receipt anterior indica tentativa em theme unpublished `156623372510`, mas `readback_match=false`; portanto não considerar aplicado.

Ação proposta:

- Subir o snippet faltante para o theme correto ou remover o render condicional se o bloco não for desejado.
- Preferência: primeiro dev theme/preview, QA visual, depois produção.

Risco:

- Baixo/médio: asset novo de snippet pode alterar a experiência visual da coleção.
- Mitigação: QA mobile/desktop; rollback removendo snippet ou revertendo section para estado anterior.

Rollback:

- Restaurar backup do asset `snippets/lk-samba-jane-editorial-v3.liquid` se existir.
- Ou remover o snippet criado e/ou condicional do `sections/lk-collection.liquid`.
- Validar que a página não exibe mais Liquid error.

## Parte B — Title/meta preview GSC P1

Arquivo completo:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/approval-packet-seo-gsc-p1-liquid-samba-20260606T142302Z/seo-title-meta-preview.csv`

Resumo dos itens:

### Homepage
- URL: `https://lksneakers.com.br/`
- Evidência: GSC brand query `lk`: 19/13.223, CTR 0,14%, pos 6,3; title/meta atuais longos/truncados
- Title proposto (53): LK Sneakers Jardins | Curadoria de Sneakers Originais
- Meta proposta (144): Sneaker boutique no Jardins, São Paulo. Curadoria premium de Nike, Adidas, New Balance e Onitsuka Tiger, com autenticidade e atendimento humano.

### New Balance 204L
- URL: `https://lksneakers.com.br/collections/new-balance-204l`
- Evidência: GSC `new balance 204l`: 28/10.615, CTR 0,26%, pos 9,7
- Title proposto (49): New Balance 204L Original | Curadoria LK Sneakers
- Meta proposta (143): New Balance 204L original na LK: perfil baixo, estética running retrô, colorways desejadas e atendimento humano para orientar a melhor escolha.

### Onitsuka Tiger
- URL: `https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos`
- Evidência: GSC `onitsuka tiger`: 66/25.976, CTR 0,25%, pos 8,3
- Title proposto (50): Onitsuka Tiger Original | Mexico 66 e Curadoria LK
- Meta proposta (131): Onitsuka Tiger original na LK Sneakers: Mexico 66 e modelos selecionados com curadoria premium, autenticidade e atendimento humano.

### Lululemon
- URL: `https://lksneakers.com.br/collections/lululemon`
- Evidência: GSC `lululemon`: 124/17.661, CTR 0,70%, pos 5,5
- Title proposto (44): Lululemon Original | Curadoria Athleisure LK
- Meta proposta (138): Lululemon original na curadoria LK: peças athleisure selecionadas, autenticidade, atendimento humano e compra segura no Jardins ou online.

### Nike Mind 001 Black Chrome
- URL: `https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto`
- Evidência: GSC `nike mind 001`: 5/30.305, CTR 0,02%, pos 9,0; title atual pesado com preço
- Title proposto (49): Nike Mind 001 Black Chrome Original | LK Sneakers
- Meta proposta (144): Nike Mind 001 Black Chrome original na LK: slide escultural com conforto sensorial, curadoria premium e atendimento humano para confirmar o par.

### Nike Mind 001 Pearl Pink
- URL: `https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa`
- Evidência: GSC `nike mind 001`: 9/25.038, CTR 0,04%, pos 8,9; meta atual longa/descritiva demais
- Title proposto (47): Nike Mind 001 Pearl Pink Original | LK Sneakers
- Meta proposta (137): Nike Mind 001 Pearl Pink original na LK: slide de design sensorial, leitura fashion e atendimento humano para orientar tamanho e escolha.

### Crocs McQueen
- URL: `https://lksneakers.com.br/products/crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho`
- Evidência: GSC `crocs mcqueen` + variações: múltiplas queries com CTR 0,12%–0,25%
- Title proposto (46): Crocs Relâmpago McQueen Original | LK Sneakers
- Meta proposta (144): Crocs Relâmpago McQueen original na LK: Classic Clog The Cars com curadoria premium, autenticidade e atendimento humano para confirmar detalhes.

### Yeezy
- URL: `https://lksneakers.com.br/collections/yeezy`
- Evidência: GSC `yeezy`: 25/9.537, CTR 0,26%, pos 8,9
- Title proposto (51): Yeezy Original | Slides, Foam Runner e 350 V2 na LK
- Meta proposta (122): Yeezy original na curadoria LK: Slides, Foam Runner, 350 V2 e modelos selecionados com autenticidade e atendimento humano.

### Nike Vomero Premium
- URL: `https://lksneakers.com.br/products/tenis-nike-vomero-premium-white-bright-crimson-branco`
- Evidência: GSC `nike vomero premium`: 6/8.912, CTR 0,07%, pos 9,3
- Title proposto (42): Nike Vomero Premium Original | LK Sneakers
- Meta proposta (142): Nike Vomero Premium original na LK: amortecimento máximo, presença fashion e curadoria premium com atendimento humano para orientar a escolha.

### Nike Mind guide
- URL: `https://lksneakers.com.br/pages/guia-nike-mind-001-002`
- Evidência: Meta atual 320 chars e duplicada; apoio para queries Nike Mind
- Title proposto (39): Nike Mind 001 e 002: Guia LK de Escolha
- Meta proposta (133): Entenda Nike Mind 001 e 002: diferenças, conforto sensorial, design e como escolher o modelo original com curadoria e atendimento LK.

## QA obrigatório se aprovado

Antes/depois:

- Capturar title/meta via Playwright para cada URL.
- Validar canonical preservado.
- Verificar mobile render e ausência de Liquid error.
- Verificar que não houve alteração de preço, estoque, prazo, desconto ou checkout.
- Registrar receipt com before/readback/rollback.

## Métrica de impacto em 7 dias

- GSC: cliques, impressões, CTR e posição por query/page.
- GA4/Shopify: sessões orgânicas, add_to_cart, checkout, receita por landing page quando disponível.
- Analisar especialmente: Nike Mind 001, Onitsuka Tiger, Lululemon, Home, NB 204L, Crocs McQueen, Yeezy, Vomero Premium.

## Aprovação necessária

Este pacote requer aprovação explícita para qualquer produção/write Shopify/theme:

`Aprovo aplicar o pacote SEO GSC P1 + hotfix Samba Jane em dev/produção conforme QA e rollback.`

Sem essa frase ou equivalente, manter somente documentação/read-only.
