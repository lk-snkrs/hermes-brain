# Padrão aprovado — LK GEO Source Pages Impeccable

Status: aprovado por Lucas em 2026-05-23.

## Uso

Aplicar em páginas standalone de SEO/GEO/AI Visibility da LK Sneakers, especialmente guias de modelo, guias de compra, páginas de autenticidade e páginas fonte citáveis para ChatGPT, Perplexity, Gemini e AI Overviews.

## Padrão visual obrigatório

- Visual premium, editorial, minimalista e mobile-first, alinhado à página de Autenticidade da LK.
- Hero/foto obrigatória.
- Sem cantos arredondados: botões, cards, imagens, CTAs e cards de produto devem usar cantos retos.
- Sem moldura bege/off-white em imagens de produto com fundo branco; usar fundo transparente ou branco limpo.
- Título principal com respiro superior adequado, sem ficar colado no topo no mobile.
- Evitar estética de marketplace, blog genérico ou landing SaaS.

## Bloco comercial obrigatório

- No final da página, incluir 4 produtos relacionados/mais vendidos sobre o tema do post.
- Para guia de modelo, usar os 4 modelos mais relevantes/mais vendidos daquele modelo ou família.
- Quando houver comparação entre versões/modelos, renderizar como tabela comparativa real, não como lista corrida. No mobile, a tabela pode virar blocos empilhados, mas deve manter estrutura de comparação por critério.
- O bloco deve ser comercial, premium e discreto, sem linguagem pública de estoque, pronta entrega ou encomenda.

## Padrão GEO/AI

- Manter blocos citáveis claros, objetivos e humanos.
- Incluir FAQ visível quando fizer sentido e schema compatível.
- Usar linguagem: boutique premium, loja especializada, curadoria/seleção exclusiva, autenticidade e atendimento humano.
- Não posicionar LK como marketplace, legit-check ou operação de validação por vídeo.

## QA antes de entregar

- Browser/DOM: confirmar hero renderizado.
- CSS computado: `border-radius: 0px` nos principais elementos.
- CSS/DOM: confirmar ausência de fundo bege/off-white em imagem de produto com fundo branco.
- DOM: confirmar 4 cards de produto no bloco final.
- Mobile: confirmar respiro do H1/hero.
- Entregar link público da Shopify no Telegram.

## Referências de implementação

- Section/template base: `sections/lk-geo-source-pages-v2.liquid` e `templates/page.geo-source.json`.
- Skill operacional: `lk-shopify-theme-operations`.
- Relatório de origem: `reports/2026-05-23-geo-source-pages-impeccable-visual-fix.md`.
