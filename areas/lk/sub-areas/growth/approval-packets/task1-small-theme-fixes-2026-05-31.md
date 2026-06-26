# Approval packet — LK tarefa 1 small theme fixes

Data: 2026-05-31
Escopo: correções pequenas derivadas da tarefa 1, sem produto/preço/estoque/checkout/campanhas.

## Decisão recebida

Lucas respondeu: `Aprovado`.

Interpretação segura deste packet: aprovação para preparar o pacote com preview exato. Aplicação em Shopify/theme ainda deve declarar explicitamente o destino se houver dúvida: dev only, dev → produção, ou apenas relatório.

## Itens propostos

### 1. Alinhar Twitter Card da home com OG aprovado

Arquivo provável: `layout/theme.liquid`.

Estado atual público:

- `twitter:title`: `LK Sneakers | Tênis Nike Dunk, adidas Samba, New Balance 530 Originais`
- `twitter:description`: `Na LK Sneakers & Apparels você encontra produtos originais de marcas como Nike, Adidas, Onitsuka e New Balance. Modelos como Air Force, Jordan, Dunk e Yeezy. Envio imediato e troca grátis.`

Target:

- `twitter:title`: `LK Sneakers | Jardins SP, Originalidade Garantida, Curadoria Premium`
- `twitter:description`: `Sneaker boutique premium no Jardins, São Paulo. Nike, Adidas Samba, New Balance e Onitsuka Tiger originais. Até 10x sem juros, frete grátis acima de R$499 e loja física na Rua Melo Alves.`

Critério de sucesso:

- Storefront público e DataForSEO leem Twitter Card alinhado ao OG.

Rollback:

- Reenviar backup anterior de `layout/theme.liquid`.

### 2. Corrigir alt do hero com fallback robusto

Arquivo provável: `sections/lk-hero.liquid`.

Estado atual:

```liquid
{%- assign hero_alt = block.settings.image_alt | default: block.settings.title | escape -%}
```

Problema:

- Primeiro slide tem `image_alt` vazio e `title` vazio, então o `<img>` sai com `alt=""`.
- Slide: `Onitsuka Tiger x Versace` no `kicker`.

Target:

```liquid
{%- assign hero_alt_source = block.settings.image_alt | default: block.settings.title | default: block.settings.kicker | default: shop.name -%}
{%- assign hero_alt = hero_alt_source | escape -%}
```

Resultado esperado:

- Banner principal deixa de sair com `alt=""`.
- Alt renderizado provável: `Onitsuka Tiger x Versace`.

Rollback:

- Restaurar linha anterior de `sections/lk-hero.liquid`.

### 3. Trocar H2 do carrinho vazio para H1

Arquivo: `sections/lk-cart.liquid`.

Estado atual:

```liquid
<h2 class="cart-empty__title">{{ section.settings.empty_title }}</h2>
```

Target:

```liquid
<h1 class="cart-empty__title">{{ section.settings.empty_title }}</h1>
```

Risco:

- Baixo: CSS é por classe `.cart-empty__title`; visual deve permanecer igual.
- Benefício principal: semântica/acessibilidade.
- SEO direto baixo porque `/cart` é bloqueado/noindex.

Rollback:

- Reverter para `h2`.

### 4. Diagnóstico headless do erro DataForSEO

Escopo: read-only.

Objetivo:

- Capturar DOM pós-JS via headless e tentar mapear o erro `The closing tag and the currently open tag do not match.` para trecho renderizado/snippet global.

Critério:

- Não aplicar correção de HTML global sem origem confirmada.

## Risco geral

Baixo nos itens 1–3, mas ainda é theme write.

## Não incluído

- Produto, preço, estoque, SKU, collection order, tags de produto.
- Checkout, descontos, fulfillment.
- Apps, Klaviyo, ads, WhatsApp/email/campanhas.
- GMC/feed.
- Publish de tema ou alteração de tema ativo além dos assets acima.

## Sequência segura se for aplicar

1. Backup/readback dos assets em dev e produção conforme destino aprovado.
2. Aplicar em `lk-new-theme/dev` primeiro.
3. Readback exato dos assets.
4. Validar preview/público conforme destino.
5. Aplicar produção apenas se o escopo aprovado mencionar produção.
6. Storefront/DataForSEO read-only para verificar:
   - Twitter Card home;
   - ausência de imagem sem alt na home;
   - H1 no carrinho vazio.

## Decisão pendente para execução

Escolher destino:

- A — preparar só patch/local, sem Shopify write.
- B — aplicar apenas no dev theme `lk-new-theme/dev`.
- C — aplicar em dev e depois produção, com backups e readback.
