# Handoff — LK Growth → LKGOC / Collection Optimizer

Data UTC: 2026-06-06T16:46:40.781412+00:00
Origem: LK Growth
Destino: LK Collection Optimizer / LKGOC
Tipo: CRO Brief P1 — execução visual/layout sob ownership LKGOC
Status: **handoff criado; sem write Shopify/theme nesta etapa**

## Pedido de Lucas

Lucas pediu `CRO Brief P1 para LKGOC` e depois `seguir`.

Correção operacional incorporada:

- LK Growth melhora CRO por diagnóstico, priorização, hipóteses, copy e mensuração.
- LK Growth **não altera tema/layout/PDP/collection visual** quando a superfície pertence ao LKGOC.
- Implementação visual deve ser feita pelo LKGOC/Collection Optimizer no fluxo canônico.

## Fonte Growth

Brief completo:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/briefs/cro-brief-p1-para-lkgoc-20260606T164320Z/CRO-BRIEF-P1-PARA-LKGOC.md`

## Escopo solicitado ao LKGOC

Classificar e preparar execução para as oportunidades P1:

1. Nike Mind 001 PDPs
   - `/products/slide-nike-mind-001-black-chrome-preto`
   - `/products/slide-nike-mind-001-pearl-pink-rosa`
   - Classificação sugerida Growth: Correção PDP + ponte para guia.

2. Onitsuka Tiger Collection
   - `/collections/onitsuka-tiger-todos-os-modelos`
   - Classificação sugerida Growth: Lite ou Full conforme densidade/asset.

3. Lululemon Collection
   - `/collections/lululemon`
   - Classificação sugerida Growth: Lite cuidadoso.

4. New Balance 204L
   - `/collections/new-balance-204l`
   - Classificação sugerida Growth: gold source; apenas refinamento leve se necessário.

## DEV correto

- Theme ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role atual validado em execução recente: `unpublished`
- Fonte: `areas/lk/sub-areas/growth/LKGOC-THEME-TARGET-CONTEXT.md`

## Guardrails obrigatórios

- Não usar `[Check] - Homologação`.
- Não usar sandbox aleatório.
- Não escrever em produção.
- Não inserir bloco global no `layout/theme.liquid` para CRO visual.
- Não inserir módulo antes do breadcrumb.
- Não empurrar grid/produto/CTA para baixo.
- Collections seguem padrão canônico: produto primeiro, guia pós-grid.
- FAQ único, sem duplicação.
- Imagens editoriais só com asset aprovado/licenciado LK.
- Sem falar publicamente em pronta entrega/encomenda/estoque como taxonomia.

## Workers mínimos sugeridos

1. Collection Intake Classifier
2. LKGOC Experience Architect
3. Guia LK Editorial Writer, se houver guia/copy editorial
4. SEO/GEO Validator
5. Visual QA Mobile/Desktop Worker
6. Rollback & Receipt Verifier

## Output esperado do LKGOC

- Classificação Full / Lite / Correção / Não-LKGOC por URL.
- Plano visual por superfície, usando padrão 204L/Moon Shoe.
- Preview packet antes de theme write, ou DEV preview com approval específico.
- QA mobile/desktop.
- Rollback/readback/receipt.
- Handoff de volta para LK Growth para mensuração D+7/D+14/D+30.

## Métricas Growth a medir depois

- GSC: cliques, impressões, CTR, posição por query/page.
- GA4: sessões orgânicas, engaged sessions, PDP views, add_to_cart, begin_checkout, purchase.
- Shopify: pedidos/receita por landing page quando disponível.
- Eventos de guia/chat/WhatsApp se tracking estiver confiável.

## Status atual

Handoff criado. Nenhuma alteração visual/theme foi feita por Growth nesta etapa.
