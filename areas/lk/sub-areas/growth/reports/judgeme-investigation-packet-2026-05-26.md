# Judge.me / LK PDP — investigação e pacote de correção

Data: 2026-05-26T16:31:34+00:00  
Escopo: read-only/public storefront + inspeção local de tema.  
URL testada: `https://lksneakers.com.br/products/tenis-nike-sb-zoom-air-paul-rodriguez-1-habanero-red-all-star-vermelho`

## Veredito

Status: **bug confirmado, sem write executado**.

O Judge.me está carregando scripts e settings no PDP, mas o widget de review de produto renderiza vazio (`#judgeme_product_reviews` com altura 0 e `<div></div>` interno). Como consequência, o link de rating perto do H1 fica invisível/0x0 quando o produto tem 0 reviews. O fallback de reputação Google existe no modal em produção, mas depende do clique em um elemento invisível em alguns PDPs.

## Evidências verificadas

### Storefront público

- `window.jdgm` existe como objeto.
- `window.jdgmSettings` existe, `widget_version: "3.0"`.
- Scripts detectados:
  - `https://cdn.judge.me/widget_preloader.js`
  - Shopify app extension `judgeme-535/assets/loader.js`
- Preview badge renderizado no DOM:
  - classe: `.jdgm-widget.jdgm-preview-badge`
  - `data-average-rating="0.00"`
  - `data-number-of-reviews="0"`
  - texto interno: `No reviews`
  - bloco interno vem com `style="display:none"`.
- Link `.pi-rating-link` medido no browser:
  - `display: inline-block`
  - `width: 0`
  - `height: 0`
  - `innerText: ""`
- Review widget no modal:
  - id: `#judgeme_product_reviews`
  - classe: `.jdgm-widget.jdgm-review-widget`
  - `height: 0`
  - HTML interno: `<div></div>`
- Seção de app block no fim do PDP está vazia:
  - `#shopify-section-template--20761716326622__judgeme-reviews`
  - conteúdo: `<div class="page-width"></div>`.

### Schema / SEO

- `Product` JSON-LD está presente, mas **não contém** `aggregateRating` nem `review`.
- `Organization/ShoeStore/ClothingStore` tem `aggregateRating` com rating de loja (`4.89`, `433` reviews), o que é separado de reviews de produto.
- Não recomendo inserir `Product.aggregateRating` sem review real por produto.

### Histórico/Brain

- Brain confirma regra operacional: Judge.me auto-publica reviews; Lucas deleta reviews ruins manualmente; Lucas responde negativas pessoalmente; review request deveria sair por Klaviyo, mas precisa auditoria.
- Relatório anterior de QA (`pdp-cro-hotfix-qa-2026-05-26.md`) já marcava warning de Judge.me/missing key e dependência do fallback.

### Código local

Arquivo inspecionado: `/opt/data/hermes_bruno_ingest/lk-new-theme/sections/lk-pdp.liquid`

- O template local ainda renderiza o preview badge assim:
  - `<a href="#judgeme_product_reviews" class="pi-rating-link">{% render 'judgeme_widgets', widget_type: 'judgeme_preview_badge' %}</a>`
- O template local renderiza o review widget dentro do modal:
  - `{% render 'judgeme_widgets', widget_type: 'judgeme_review_widget', concierge_product: product %}`
- A produção parece ter hotfixes adicionais que não estão totalmente refletidos no arquivo local lido, especialmente fallback dentro do modal. Isso exige cuidado para não sobrescrever produção com arquivo local antigo.

## Diagnóstico provável

1. **Produto sem review específica:** o badge do Judge.me vem como `0.00 / 0 reviews` e o HTML interno começa oculto.
2. **Trigger invisível:** o tema envolve o badge em `.pi-rating-link`, mas quando Judge.me oculta o badge, o link fica 0x0 e deixa de ser uma CTA útil.
3. **Widget dentro de modal oculto:** o review widget é renderizado dentro de `.pdp-reviews-modal`, que começa com `display:none`; o Judge.me frequentemente falha ou não hidrata corretamente widgets escondidos no load.
4. **App block vazio:** há uma seção Judge.me no fim do template, mas ela não entrega conteúdo visível.
5. **Dependência excessiva de fallback:** o fallback para Google Reviews é bom para confiança, mas hoje cobre uma falha de renderização em vez de ser um estado UX intencional.

## Correção recomendada

### Opção A — hotfix seguro de UX, sem mexer na app Judge.me

Objetivo: garantir que sempre exista uma CTA visível para avaliações, mesmo quando Judge.me retorna 0 reviews.

Escopo técnico:

- Manter o preview badge quando ele tiver conteúdo visível.
- Adicionar uma CTA fallback visível ao lado/abaixo do H1 quando `.jdgm-prev-badge` estiver oculto ou com `data-number-of-reviews="0"`.
- CTA sugerida: `Avaliações da loja` ou `Ver avaliações` abrindo o modal Google/reviews já existente.
- Não declarar avaliação do produto quando não há review do produto.

Risco: baixo.  
Rollback: remover CSS/JS/markup fallback adicionado no `sections/lk-pdp.liquid`.

### Opção B — correção estrutural do Judge.me

Objetivo: dar ao Judge.me um container visível e inicializável.

Escopo técnico:

- Não renderizar o review widget principal dentro de um modal `display:none` no carregamento.
- Renderizar uma seção visível de reviews abaixo do PDP ou usar o app block oficial corretamente configurado.
- O modal pode apontar/ancorar para essa seção ou clonar conteúdo depois de inicializado, mas não deve ser o único local de hidratação.
- Investigar/admin Judge.me: key/config/app block, porque histórico apontou warning `Cannot load Judge.me widget contents due to missing jdgm key` e possível falha de assets de media gallery.

Risco: médio, porque toca integração app/theme e pode afetar todos os PDPs.  
Rollback: restaurar asset `sections/lk-pdp.liquid` anterior + remover bloco/app section se alterado.

### Opção C — investigação autenticada Judge.me/Klaviyo

Objetivo: entender se existem reviews de produto, se o app tem key/config válida e se review request está configurado.

Escopo:

- Judge.me admin/API: status de loja, produto, reviews publicadas, moderation, review request.
- Klaviyo: confirmar se review request existe/está ativo ou se está duplicando com Judge.me.

Risco: read-only baixo; writes/envios/moderação seguem bloqueados.  
Bloqueio: precisa credencial/API/app access se não existir no ambiente.

## O que eu não executei

- Nenhum write em Shopify/theme/produção.
- Nenhuma alteração no Judge.me admin.
- Nenhuma moderação/resposta de review.
- Nenhum envio Klaviyo/WhatsApp/email.
- Nenhuma alteração de schema/SEO visível.

## Aprovação necessária

Para eu corrigir em produção, aprovar explicitamente uma destas opções:

- `Aprovo hotfix Judge.me Opção A no PDP produção: CTA/fallback visível sem alterar reviews reais.`
- `Aprovo correção Judge.me Opção B em dev theme primeiro, com preview e sem publicar.`
- `Aprovo investigação autenticada Judge.me/Klaviyo read-only, sem writes/envios/moderação.`
