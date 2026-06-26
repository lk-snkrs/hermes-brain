# CRO Brief P1 para LKGOC — LK Growth → Collection Optimizer

Data UTC: 2026-06-06T16:43:20.310889+00:00
Owner do diagnóstico: LK Growth
Owner da implementação visual/layout: LKGOC / Collection Optimizer
Status: **Brief read-only. Nenhum write Shopify/theme.**

## 1. Contexto e ownership

Lucas corrigiu o fluxo: LK Growth deve melhorar CRO por diagnóstico, hipótese, priorização, copy e mensuração — **não alterando tema/layout diretamente** quando a superfície pertence ao LKGOC.

Regra aplicada neste brief:

- Growth entrega evidência, hipótese, copy sugerida, métrica e critérios de aceite.
- LKGOC decide arquitetura visual, aplica no DEV correto e faz QA visual.
- Shopify/theme production só com aprovação explícita de Lucas.

Tema DEV correto para LKGOC, conforme Brain e validação recente:

- Theme ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role atual validado: `unpublished`
- Fonte: `areas/lk/sub-areas/growth/LKGOC-THEME-TARGET-CONTEXT.md`

## 2. Objetivo do CRO P1

Melhorar conversão e qualidade de decisão das páginas com demanda orgânica relevante, sem transformar coleção/PDP em blog e mantendo o padrão canônico LK:

1. Produto primeiro.
2. Orientação editorial curta e premium.
3. Guia pós-grid quando for coleção.
4. Guia dedicado quando a demanda justificar.
5. FAQ único, sem duplicar FAQ legado.
6. Autenticidade, curadoria e atendimento humano como prova de confiança.

## 3. Evidência Growth usada

### GSC — janela 2026-05-07 a 2026-06-03

- `nike mind 001`
  - PDP Black Chrome: 5 cliques / 30.305 impressões / CTR 0,02% / posição 9,0.
  - PDP Pearl Pink: 9 cliques / 25.038 impressões / CTR 0,04% / posição 8,9.
- `onitsuka tiger`
  - Collection Onitsuka: 66 cliques / 25.976 impressões / CTR 0,25% / posição 8,3.
- `lululemon`
  - Collection Lululemon: 124 cliques / 17.661 impressões / CTR 0,70% / posição 5,5.
- `new balance 204l`
  - Collection: 28 cliques / 10.615 impressões / CTR 0,26% / posição 9,7.

### DataForSEO Brasil

- `lululemon`: ~40.500 buscas/mês.
- `onitsuka tiger`: ~33.100 buscas/mês.
- `nike mind 001`: ~18.100 buscas/mês.
- `new balance 204l`: ~9.900 buscas/mês, com pico recente de 40.500–49.500.
- `adidas samba jane`: ~2.400 buscas/mês, com pico recente de 8.100.

### QA técnico Growth

- Páginas mobile seguem pesadas: ~263–295 requests e ~86–91 scripts por página em Playwright.
- Erros/sinais de atenção: CORS em endpoints internos, `[ET] tracker not configured`, Judge.me missing key em alguns contextos.
- Isso é frente técnica paralela de mensuração/performance; não deve bloquear o brief visual LKGOC, mas deve entrar no QA de impacto.

## 4. Priorização P1

### P1-A — Nike Mind 001 PDPs

URLs:

- `/products/slide-nike-mind-001-black-chrome-preto`
- `/products/slide-nike-mind-001-pearl-pink-rosa`

Classificação LKGOC sugerida: **Correção/otimização PDP + ponte para Guia**, não coleção full.

Hipótese CRO:

- A busca por `nike mind 001` tem alta intenção e curiosidade sobre um produto novo/diferente.
- A página precisa ajudar o usuário a entender rapidamente o que é o Nike Mind, diferença 001 vs 002 e como escolher tamanho/cor, sem empurrar o CTA para baixo.
- Melhorar clareza e confiança deve aumentar engajamento com CTA/chat/guia e reduzir abandono de PDP.

Recomendação de arquitetura:

- Não inserir bloco antes do breadcrumb.
- Não inserir bloco global no layout.
- Se aplicável ao padrão visual do PDP, inserir módulo curto **após a área principal do produto** ou próximo a trust/descrição, sem competir com galeria/CTA.
- Criar/ajustar link para guia dedicado: `/pages/guia-nike-mind-001-002`.

Copy sugerida, para LKGOC adaptar:

```text
Nike Mind 001: design sensorial, presença e escolha assistida

O Nike Mind 001 é um slide de leitura futurista, criado para uma experiência tátil diferente no caminhar. Na LK, a curadoria prioriza autenticidade, acabamento e atendimento humano para orientar tamanho e melhor opção de cor.

• Perfil escultural e confortável para uso lifestyle.
• Orientação humana para tamanho e escolha entre cores.
• Compra segura com curadoria premium no Jardins e online.

CTA secundário: Ver guia Nike Mind 001 vs 002
```

Critérios de aceite:

- CTA principal permanece acima da dobra ou não perde destaque.
- Breadcrumb e estrutura do PDP preservados.
- Módulo não aparece em produtos não-Nike Mind.
- Sem Liquid error.
- Mobile sem overflow e sem empurrar conteúdo crítico excessivamente.
- Link para guia funcionando.

Métricas de sucesso:

- PDP organic sessions.
- Add-to-cart rate.
- Click para guia.
- Click WhatsApp/chat quando rastreável.
- Conversão assistida PDP → checkout.
- GSC CTR e posição como métrica secundária.

### P1-B — New Balance 204L Collection

URL:

- `/collections/new-balance-204l`

Classificação LKGOC sugerida: **manter como gold source / refinamento leve**, não reconstruir.

Hipótese CRO:

- A 204L já é padrão aprovado. O ganho está em orientar busca por cor/gênero/tamanho sem tirar produto do foco.
- Como há demanda alta e picos recentes, a página deve deixar claro rapidamente as variações desejadas e caminho para escolha.

Recomendação de arquitetura:

- Preservar padrão canônico atual da 204L.
- Evitar novo bloco visual fora do padrão.
- Se houver ajuste, fazer dentro do bloco editorial/guia existente, pós-grid ou copy curta aprovada.

Copy sugerida, se LKGOC julgar necessário:

```text
O New Balance 204L combina perfil baixo, estética running retrô e proporções discretas. A curadoria LK organiza as principais leituras — bege, branco, cinza e opções femininas — para facilitar a escolha com autenticidade e atendimento humano.
```

Critérios de aceite:

- Grid permanece antes do guia.
- Guia pós-grid preservado.
- FAQ único, sem duplicação.
- Nenhuma regressão no padrão gold source.

Métricas:

- Organic sessions collection.
- Product click-through da collection para PDP.
- Add-to-cart originado da collection.
- CTR GSC para `new balance 204l`.

### P1-C — Onitsuka Tiger Collection

URL:

- `/collections/onitsuka-tiger-todos-os-modelos`

Classificação LKGOC sugerida: **Lite → possível Full se houver densidade de produtos/imagens editoriais reais**.

Hipótese CRO:

- Onitsuka tem alta demanda e intenção ampla. Usuário precisa diferenciar estética vintage, perfil baixo, modelos e autenticidade.
- Um tratamento LKGOC leve pode aumentar confiança e cliques para PDP sem parecer marketplace genérico.

Recomendação de arquitetura:

- Collection product-first.
- Banner/header no padrão `lk-collection-v2` se ainda não estiver no padrão.
- Guia pós-grid curto: “como escolher Onitsuka Tiger na LK”.
- Não criar FAQ solta antes do grid.

Copy sugerida:

```text
Onitsuka Tiger original com leitura vintage e acabamento premium

Modelos Onitsuka Tiger têm perfil baixo, construção leve e estética retrô. A LK seleciona pares autênticos e oferece atendimento humano para orientar modelo, tamanho e combinação — da leitura clássica ao uso urbano contemporâneo.
```

FAQ sugerido, se virar guia:

- Onitsuka Tiger é confortável para uso diário?
- Como escolher tamanho em Onitsuka Tiger?
- Qual a diferença entre Onitsuka Tiger e sneakers de corrida retrô?
- Como confirmar autenticidade na LK?

Métricas:

- CTR GSC para `onitsuka tiger`.
- Click collection → PDP.
- Add-to-cart por sessão orgânica.
- Conversão por landing page.

### P1-D — Lululemon Collection

URL:

- `/collections/lululemon`

Classificação LKGOC sugerida: **Lite, com cuidado de taxonomia**.

Hipótese CRO:

- A busca por Lululemon é muito forte, mas a intenção pode ser marca ampla. A página precisa posicionar a LK como curadoria premium/athleisure, sem prometer disponibilidade/tamanho publicamente.
- Orientação de uso/caimento ajuda a transformar busca de marca em interesse comercial.

Recomendação de arquitetura:

- Bloco curto de curadoria, não guia longo se não houver densidade de sortimento/conteúdo.
- Evitar linguagem operacional de estoque.
- Reforçar autenticidade, atendimento humano e seleção.

Copy sugerida:

```text
Lululemon na curadoria LK: performance, conforto e lifestyle

Peças Lululemon selecionadas para uma rotina entre treino, viagem e cidade. A LK combina curadoria premium, autenticidade e atendimento humano para orientar escolha, caimento e composição.
```

Métricas:

- CTR GSC para `lululemon`.
- Engagement/click para produtos.
- Add-to-cart e compra assistida.
- Eventos de chat/WhatsApp quando confiáveis.

## 5. O que NÃO fazer

- Não inserir módulo visual global no `layout/theme.liquid`.
- Não colocar bloco antes do breadcrumb.
- Não empurrar produto/CTA para baixo.
- Não criar variações soltas fora do padrão 204L/Moon Shoe.
- Não duplicar FAQ.
- Não publicar direto em produção.
- Não usar imagem editorial externa sem asset aprovado/licenciado LK.
- Não falar publicamente em pronta entrega/encomenda/estoque como taxonomia.

## 6. Handoff para LKGOC — input contract

Pedido para LKGOC:

1. Classificar cada URL: Full / Lite / Correção / Não-LKGOC.
2. Usar o padrão `lk-collection-v2` / gold source 204L quando for coleção.
3. Para Nike Mind, decidir se é ajuste de PDP + guia dedicado ou se precisa de coleção/guia adicional.
4. Produzir preview no DEV correto `155065450718` somente após approval do escopo LKGOC.
5. QA mobile/desktop com screenshots.
6. Readback de assets e rollback.
7. Retornar para LK Growth medir impacto.

## 7. Critérios de aceite globais

- Sem Liquid error.
- Sem overflow mobile.
- Produto/CTA não perde prioridade.
- Grid antes do guia em collections.
- Copy premium, curta, humana e comercial.
- Autenticidade e atendimento humano claros.
- FAQ/schema apenas quando há guia/estrutura apropriada.
- Canonical/title/meta preservados.
- Produção intocada até aprovação explícita.

## 8. Plano de mensuração Growth pós-implementação

Janela sugerida:

- D+7: sanity check e HTML/QA/GSC early signs.
- D+14: GSC CTR/cliques/posição e GA4/Shopify landing-page engagement.
- D+30: impacto comercial mais confiável.

Métricas:

- GSC: clicks, impressions, CTR, avg position por query/page.
- GA4: organic sessions, engaged sessions, PDP views, add_to_cart, begin_checkout, purchase quando confiável.
- Shopify: pedidos/receita por landing page quando disponível.
- CRO events: guide clicks, product clicks collection → PDP, chat/WhatsApp se tracking estiver confiável.

## 9. Dependências/riscos

- Dados comerciais finais ainda precisam cruzar GA4/Shopify/receita/margem para priorização decision-grade completa.
- Tracking atual tem sinais de falha/ruído; Growth deve auditar mensuração em paralelo.
- LKGOC precisa respeitar assets aprovados/licenciados para qualquer mídia editorial.

## 10. Recomendação executiva

Prioridade de implementação LKGOC:

1. Nike Mind 001 PDPs — correção de clareza/guia, maior gargalo de CTR e intenção nova.
2. Onitsuka — alta demanda, CTR baixo, bom candidato Lite/Full.
3. Lululemon — alta demanda, exige copy cuidadosa e premium.
4. New Balance 204L — apenas refinamento leve, pois já é gold source.
