# Correção de padrão — guias de coleção LK

## Problema identificado

As páginas recém-criadas para Adidas Samba e Onitsuka Tiger Mexico 66 ficaram com estrutura genérica/textual. Isso viola o padrão já provado pela LK no guia Nike x Jacquemus Moon Shoe.

## Referência canônica verificada

URL: https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk

Elementos detectados no HTML público:

- layout source-page editorial (`lk-source-page--moon-shoe`);
- hero editorial em 2 colunas com imagem contextual;
- H1 serif editorial (`Cormorant Garamond` no CSS da página);
- introdução longa e curada;
- blocos citáveis LK;
- tabela comparativa (`lk-source-table`) para colorways/leitura visual/importância;
- seção de sinais de moda (`lk-source-media`) com cards externos;
- links de referência como Vogue, Hypebeast e Hypebae;
- imagens/contexto visual;
- FAQ em `details/summary`;
- CTA comercial discreto.

## Diferença dos guias atuais

### Guia Adidas Samba

URL: https://lksneakers.com.br/pages/guia-adidas-samba

Verificação pública:

- tabelas: 0;
- fontes/cards de moda: ausentes;
- Vogue/GQ/Hypebeast: ausentes;
- estrutura visual: genérica `lk-editorial-guide`, não padrão Moon Shoe.

### Guia Onitsuka Tiger Mexico 66

URL: https://lksneakers.com.br/pages/guia-onitsuka-tiger-mexico-66

Verificação pública:

- tabelas: 0;
- fontes/cards de moda: ausentes;
- Vogue/GQ/Hypebeast: ausentes;
- estrutura visual: genérica `lk-editorial-guide`, não padrão Moon Shoe.

## Fontes editoriais levantadas para correção

### Adidas Samba

- Vogue: `https://www.vogue.com/article/adidas-sambas-history`
- Vogue: `https://www.vogue.com/article/best-adidas-sneakers`
- GQ: `https://www.gq.com/story/best-adidas-sambas-ranking`
- Adidas: `https://www.adidas.com/us/blog/1060276-we-gave-the-world-a-samba-a-legendary-shoe-with-a-rich-history`

### Onitsuka Tiger Mexico 66

- Vogue: `https://www.vogue.com/article/kill-bill-sneakers-onitsuka-tiger-mexico-66-celebrities`
- Vogue HK runway/contexto Onitsuka: `https://www.voguehk.com/en/article/runway/onitsuka-tiger-fall-2026`
- Hypebeast tag/contexto Mexico 66 SD: `https://hypebeast.com/tags/onitsuka-tiger-mexico-66-sd`

## Novo padrão obrigatório

Para cada guia:

1. Clonar estrutura visual do guia Moon Shoe/Jacquemus, adaptando classes para `lk-source-page--samba` e `lk-source-page--mexico-66`.
2. Hero com imagem editorial/contextual.
3. H1 serif editorial.
4. Intro premium, sem linguagem operacional ou taxonomia de estoque.
5. Pelo menos 1 tabela comparativa.
6. Seção de sinais de moda com cards externos.
7. Blocos citáveis LK.
8. FAQ em details/summary.
9. CTA comercial discreto para a coleção.
10. Manter produto/coleção como curadoria premium, não vitrine genérica de preço.

## Status

Este arquivo é auditoria/preparação local. Nenhuma nova alteração externa foi feita nesta etapa.
