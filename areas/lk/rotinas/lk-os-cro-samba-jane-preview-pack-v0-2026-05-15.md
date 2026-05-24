# LK OS — CRO Preview Pack v0: Adidas Samba Jane

Gerado em: `2026-05-15T10:20:00Z`
Status: `preview_only_needs_lucas_approval_before_theme_write`
Escopo: coleção Adidas Samba Jane + PDP `Black White Gum` como primeira página/produto de teste.

## Regra Lucas

Toda modificação de tema deve acontecer primeiro na **branch dev** / ambiente dev. Nenhuma alteração deve ir para produção sem aprovação e validação visual de Lucas.

## Páginas escolhidas

### Collection

- URL: https://lksneakers.com.br/collections/adidas-samba-jane
- Evidência anterior GA4/GSC: 199 sessões, 0 compras, 19.402 impressões GSC, CTR 1,12%, posição 6,9.
- Fonte: `fact_ga4`, `fact_gsc`, `public_live_snapshot`.

### Produto piloto

- URL: https://lksneakers.com.br/products/tenis-adidas-samba-jane-black-white-gum-preto
- Motivo: primeiro produto da collection, preço promocional visível, grade 34–40 e página com bloco de compra completo.
- Fonte: `public_live_snapshot` + collection products JSON público.

## Diagnóstico rápido

### Collection

- O conteúdo SEO/intro é bom, mas longo; pode empurrar a decisão de compra.
- A collection já mostra tamanhos nos cards, preço, desconto e parcelamento.
- Falta uma faixa de confiança/benefícios mais escaneável antes do grid.
- Filtros e ordenação existem, mas tamanho deveria virar atalho principal para tênis.
- Modal/newsletter aparece como atrito visual em testes de navegação e pode bloquear a primeira decisão.

### PDP

- Bloco de compra é forte: preço, tamanhos, CTA, avaliações Google, autenticidade, 10x, frete, troca, loja física.
- O maior atrito observado é o popup/newsletter bloqueando a intenção de compra.
- O segundo atrito é que confiança e prazo/encomenda precisam ficar ainda mais próximos do CTA em forma de mensagem curta.

## Recomendação de primeiro teste em dev

Começar por **Adidas Samba Jane — collection + PDP piloto**, mas com escopo pequeno:

### Teste A — Popup menos agressivo em páginas de compra

Objetivo: reduzir bloqueio acima da dobra antes de escolher produto/tamanho.

- PDP: não exibir popup inicial, ou atrasar para 20–30s/scroll/exit intent.
- Collection: atrasar popup ou trocar por barra discreta não-bloqueante.
- Manter captura de e-mail, mas não competir com add-to-cart.

Copy alternativa se mantiver newsletter:

> Receba acesso antecipado a drops e benefícios exclusivos da LK.

CTA:

> Quero receber benefícios

### Teste B — Trust strip compacto acima do grid/CTA

Collection, acima do grid:

> Adidas Samba Jane originais, curados pela LK. Envio para todo o Brasil, até 10x sem juros, troca fácil e atendimento humano.

Chips:

- Original garantido
- Loja física Jardins
- Até 10x sem juros
- Troca fácil
- Frete grátis +R$499

PDP, perto do botão:

> Produto original com curadoria LK. Escolha seu tamanho e compre com até 10x sem juros, troca fácil e atendimento humano.

### Teste C — Atalho de tamanho na collection

Antes do grid:

> Escolha seu tamanho

Chips: `34 · 35 · 36 · 37 · 38 · 39 · 40`

Regra: usar os filtros/links existentes, sem mexer em estoque real e sem inferir disponibilidade Tiny.

## O que deve ir para branch dev primeiro

1. Identificar onde o tema controla newsletter/modal.
2. Criar condição dev para PDP/collection Samba Jane:
   - atrasar/remover modal apenas nesse escopo de teste;
   - não alterar globalmente o site inteiro sem aprovação.
3. Adicionar trust strip reaproveitável, limitado a collection/PDP piloto.
4. Validar visual desktop/mobile.
5. Enviar preview/screenshot para Lucas aprovar antes de produção.

## O que não autorizei/não foi feito

- Nenhum Shopify/theme write.
- Nenhuma alteração em produção.
- Nenhum deploy.
- Nenhuma campanha/newsletter/Klaviyo.
- Nenhum preço/estoque/produto/SEO field alterado.

## Approval surface para Telegram

Aprovação sugerida para a próxima etapa técnica:

> Aprovo preparar na branch dev o CRO Preview Pack v0 para Adidas Samba Jane, limitado a: popup atrasado/removido só na collection/PDP piloto, trust strip compacto e atalho de tamanho na collection. Sem produção, sem Shopify produto/preço/estoque, sem campanha e sem publish até eu revisar.
