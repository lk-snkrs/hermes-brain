# LK Growth — Auditoria SEO/GEO pós-preview dev: Onitsuka Mexico 66 + Adidas Samba

Data: 2026-05-26
Tema: `lk-new-theme/dev` (`155065450718`, unpublished)
Escopo: read-only público + alteração em tema dev aprovada no turno por Lucas (“Seguir”). Sem produção.

## URLs de preview

- Onitsuka Tiger Mexico 66: https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66?preview_theme_id=155065450718&_ab=0&_fd=0&_sc=1&cb=20260526-013141
- Adidas Samba: https://lksneakers.com.br/collections/adidas-samba?preview_theme_id=155065450718&_ab=0&_fd=0&_sc=1&cb=20260526-013141

## Padrão aplicado

- Produtos continuam primeiro.
- Guia editorial entra depois do grid/carregar mais.
- Uma FAQ visível por coleção dentro do guia editorial.
- FAQPage JSON-LD específico por coleção.
- Sem CTA “ver produtos”.
- Sem linguagem operacional pública de pronta entrega/encomenda/estoque como taxonomia.
- Copy com posicionamento premium: curadoria, originalidade, orientação humana e comparação de modelo/material/tamanho.

## Evidência técnica

Receipt: `areas/lk/sub-areas/growth/receipts/theme-dev/dev-phase1-onitsuka-samba-guides-20260526-013141/receipt.json`

- Theme verificado: `lk-new-theme/dev`, role `unpublished`.
- Asset alterado: `sections/lk-collection.liquid`.
- Readback Shopify OK.
- Rollback: re-upload de `sections__lk-collection.before.liquid` no mesmo receipt.

## Auditoria por coleção

### 1. Onitsuka Tiger Mexico 66

**Status:** aprovado para preview dev.

**O que foi verificado**

- Guia renderizado: `#lk-guia-onitsuka-tiger-mexico-66`.
- Guia aparece depois do bloco de produtos/carregar mais.
- FAQ visível: 1 heading “Perguntas frequentes”.
- Perguntas no guia: 5.
- `coll-enrichment .coll-faq`: 0, evitando FAQ duplicada.
- FAQPage JSON-LD detectado: 1.
- Produto/grid presente: 54 links de produto detectados no DOM de QA.

**Perguntas frequentes repensadas**

- Quanto custa um Onitsuka Tiger no Brasil?
- Qual a diferença entre ASICS e Onitsuka Tiger?
- O Onitsuka Tiger Mexico 66 é da ASICS?
- Como escolher entre Mexico 66, SD, Sabot e Slip-on?
- O Mexico 66 tem a forma grande ou pequena?

**Leitura SEO/GEO**

- Forte para AI Overview/ChatGPT porque responde entidades e desambiguação: Onitsuka vs ASICS, Mexico 66 vs SD/Sabot/Slip-on.
- Evita conteúdo decorativo: perguntas refletem busca real, comparação e intenção de compra.
- Blocos citáveis bons: “linha de herança japonesa ligada à origem da ASICS”, “Mexico 66 é a escolha mais clássica”, “SD tem acabamento mais premium”.

**Risco**

- Baixo em dev. Risco principal antes de produção: excesso de texto em mobile se o guia ficar muito próximo do loadmore; precisa QA visual final.

### 2. Adidas Samba

**Status:** aprovado para preview dev.

**O que foi verificado**

- Guia renderizado: `#lk-guia-adidas-samba`.
- Guia aparece depois do bloco de produtos/carregar mais.
- FAQ visível: 1 heading “Perguntas frequentes”.
- Perguntas no guia: 5.
- `coll-enrichment .coll-faq`: 0, evitando FAQ duplicada.
- FAQPage JSON-LD detectado: 1.
- Produto/grid presente: 48 links de produto detectados no DOM de QA.
- Banner recebeu descrição editorial específica para Adidas Samba.

**Perguntas frequentes repensadas**

- Como saber se o Adidas Samba é original?
- Qual a diferença entre Samba OG, Sambae, Samba Jane e Samba XLG?
- Quanto custa um Adidas Samba original?
- O Adidas Samba feminino muda forma/tamanho?
- Qual Samba escolher para rotina: couro, camurça ou versões plataforma?

**Leitura SEO/GEO**

- Forte para intenção comparativa: OG vs Sambae vs Jane vs XLG.
- Bom para resposta direta em IA: explica autenticidade, preço, forma e material sem prometer disponibilidade.
- Melhor que FAQ decorativa porque captura perguntas reais de compra e diferenciação.

**Risco**

- Baixo em dev. Antes de produção, validar se o termo “feminino” em pergunta específica não estreita demais a coleção inteira; hoje ele aparece apenas como intenção de busca/ajuste.

## Veredito

- Padrão das próximas coleções estabelecido e aplicado no lote 1.
- Onitsuka Mexico 66 e Adidas Samba estão prontos para revisão visual em preview dev.
- Não houve alteração em produção.

## Próximo passo recomendado

1. QA mobile visual dos dois previews.
2. Se Lucas aprovar visual/copy, preparar pacote de produção com rollback e janela de impacto.
3. Próximo lote sugerido depois: Onitsuka Tiger hub, NB 9060, NB 530 — mantendo o mesmo padrão e limpando linguagem operacional antes de promover.
