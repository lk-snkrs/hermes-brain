# Template canônico proposto — Coleção LK produto-first

Data de criação: 2026-05-28  
Status: **proposto / approval-packet read-only**  
Dono lógico: LK Shopify  
Co-dono: LK Growth  
Origem: padrão validado na coleção New Balance 204L e consolidado no Fechamento Ágil 2026-05-27.

## 1. Objetivo

Padronizar páginas de coleção LK em um formato **produto-first**: o cliente vê rapidamente os produtos e consegue comprar/consultar antes de encontrar blocos editoriais longos.

A coleção deve vender primeiro e educar depois.

## 2. Quando usar

Usar este template quando a coleção for:

- coleção comercial de produto, marca, collab, modelo ou curadoria com intenção de compra;
- coleção com tráfego orgânico/pago/social esperado;
- página onde excesso de texto/hero/editorial acima do grid atrapalha descoberta de produto;
- coleção derivada de guia/editorial, mas com objetivo principal de conversão;
- coleção que precise equilibrar SEO/GEO com UX de e-commerce.

Não usar como padrão único quando a página for:

- source page/editorial puro sem grade de produtos;
- guia institucional ou conteúdo de marca sem objetivo imediato de compra;
- landing campaign específica com aprovação visual/CRO própria;
- página experimental em dev theme ainda sem validação.

## 3. Estrutura canônica

### 3.1 Topo minimalista

Ordem recomendada:

1. Kicker curto, se necessário: `CURADORIA LK`, marca ou linha.
2. H1 direto com o nome da coleção.
3. Descrição curta, preferencialmente 1–2 frases.
4. CTA discreto quando fizer sentido: chat/curadoria/atendimento.
5. Sem bloco editorial pesado antes do grid.

Critérios:

- H1 legível, sem ocupar a primeira dobra inteira.
- Texto introdutório não deve empurrar produtos para baixo sem necessidade.
- Evitar storytelling longo antes do grid.
- Evitar termos públicos de disponibilidade como “pronta entrega”, “sob encomenda” ou “consultar estoque”; usar linguagem de curadoria e atendimento.

### 3.2 Produtos primeiro

O grid de produtos deve aparecer cedo.

Critérios:

- Produtos visíveis rapidamente no mobile e desktop.
- Ordenação comercial disponível quando aplicável: relevância/destaque, mais vendidos, data, preço e A–Z quando a theme suportar.
- Não sacrificar a compra para acomodar texto SEO acima do grid.
- Quantidade por página deve equilibrar velocidade e exploração; referência recente da 204L: 20 produtos por página funcionou melhor que grid excessivamente longo.

### 3.3 Blocos de confiança e atalhos

Se usados, devem ser leves:

- curadoria exclusiva;
- autenticidade;
- atendimento humano;
- loja física/Jardins quando pertinente;
- CTA `Falar no chat` discreto.

Não usar bloco que pareça banner agressivo ou atrapalhe a decisão de compra.

### 3.4 Guia / editorial depois do grid

Conteúdo editorial entra **depois** dos produtos.

Blocos possíveis:

- guia rápido do modelo/coleção;
- como usar / styling;
- comparação entre versões/modelos;
- origem da collab ou contexto cultural;
- links para source page/editorial completo quando existir.

Reutilizar os padrões de LK Growth:

- `areas/lk/sub-areas/growth/PADRAO-GUIAS-EDITORIAIS-LK.md`;
- `areas/lk/sub-areas/growth/templates/brief-guia-editorial-colecao-lk.md`;
- padrão visual/editorial aprovado no Moon Shoe quando for guia/source page.

### 3.5 FAQ e schema no final

FAQ deve vir depois do conteúdo e do grid, com função de SEO/GEO e suporte a dúvidas reais.

FAQ recomendado:

- perguntas sobre modelo, forma, estilo, autenticidade, curadoria e atendimento;
- evitar promessa rígida de disponibilidade/estoque/prazo;
- quando falar de disponibilidade, usar “confirme disponibilidade e prazo no chat/atendimento”.

Schema recomendado:

- `CollectionPage` / `BreadcrumbList` quando aplicável;
- `FAQPage` apenas se FAQ estiver visível e aprovado;
- Product schema deve continuar vindo dos produtos/PDP/theme, não ser inventado manualmente na coleção.

## 4. Critérios de qualidade

Uma coleção produto-first está pronta quando:

- a primeira dobra mostra intenção comercial clara;
- o grid aparece cedo, especialmente no mobile;
- a descrição acima do grid é curta e útil;
- guia/FAQ/schema enriquecem sem bloquear compra;
- linguagem pública não promete estoque/prazo por tamanho;
- Shopify/LK Growth conseguem medir impacto por tráfego, CTR, conversão e receita;
- há rollback claro se o layout performar pior.

## 5. Responsabilidades

### LK Shopify

- transformar o padrão em preview Shopify quando houver coleção-alvo;
- validar objeto Shopify, handle, theme/dev theme quando necessário;
- preparar snapshot, readback, receipt e rollback antes de qualquer write;
- não publicar/alterar produção sem aprovação escopada.

### LK Growth

- validar SEO/GEO/CRO, conteúdo editorial, FAQ e schema;
- garantir que o conteúdo pós-grid siga o padrão de guias/editoriais;
- priorizar páginas por impacto comercial, não por HTML isolado;
- acompanhar impacto depois da aplicação.

### LK Ops/Tiny

- não é dono deste template;
- entra apenas quando houver afirmação de estoque/preço/disponibilidade, que deve seguir Tiny como fonte de verdade.

## 6. Rollback padrão

Para qualquer aplicação futura em Shopify:

1. Capturar snapshot do estado atual da coleção/theme/asset/template antes.
2. Salvar backup local restrito com timestamp.
3. Aplicar primeiro em dev/unpublished theme quando for alteração visual/theme.
4. Verificar readback API/hash/DOM/screenshot.
5. Se aprovado para produção, executar alteração escopada.
6. Rollback: re-aplicar snapshot anterior do asset/template/campo alterado.

Para alteração apenas de documentação/template local:

- rollback é remover ou reverter este arquivo e o approval packet correspondente via git diff/backup.

## 7. Limites explícitos

Este template **não aprova**:

- alterar Shopify production;
- editar tema, Liquid, JSON template ou asset;
- alterar preço, estoque, status, produto, SKU, coleção viva ou SEO field;
- publicar guia/source page;
- criar campanha, Klaviyo, WhatsApp, Meta/GMC ou qualquer envio externo;
- prometer disponibilidade, prazo, reserva ou compra.

Cada aplicação real exige preview/aprovação no template `preview-aprovacao-shopify.md`.

## 8. Texto-base para aplicação futura

Quando uma coleção específica for candidata, o pedido deve virar um preview assim:

> Aplicar padrão LK coleção produto-first em `[handle da coleção]`: topo minimalista, produtos antes de guia/FAQ/schema, CTA discreto, sem alterar preço/estoque/produtos. Escopo inicial: dev/read-only preview. Produção só após aprovação separada com snapshot/readback/rollback.
