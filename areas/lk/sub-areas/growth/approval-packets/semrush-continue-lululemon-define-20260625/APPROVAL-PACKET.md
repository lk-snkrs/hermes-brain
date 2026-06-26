# Approval Packet — SEMrush continuation — Lululemon Define Jacket

Data: 2026-06-25
Status: diagnóstico read-only concluído; nenhum write executado.

## Contexto

Após Adidas Samba Marrom, o próximo item acionável do alerta SEMrush é `lululemon define jacket`.

## Evidências read-only

SERP DataForSEO mobile BR/PT:
- Lululemon oficial domina posições 1, 3 e 9.
- Popular Products aparece logo acima dos orgânicos e inclui itens da LK:
  - `Jaqueta Lululemon Define Nulu` — seller LK Sneakers Apparels.
  - `Define Jacket Nulu Rose/Gold` — seller LK Sneakers Apparels.
- PAA/intenções: worth it, cost, tight/fit, what does it do.
- Conteúdo review/social/video aparece forte, além de Enjoei.

Shopify Admin read-only:
- `collectionByHandle(lululemon-define-jacket)` = null.
- `collectionByHandle(lululemon-define)` = null.
- `collectionByHandle(lululemon)` existe, 41 produtos.
- Produtos Define ativos detectados:
  - `jaqueta-lululemon-define-nulu`
  - `define-cropped-jacket-nulu`
  - `define-jacket-nulu-rose-gold`
  - `jaqueta-lululemon-define-luon-white-branco`
  - `jaqueta-lululemon-define-nulu-black-gold-preto`
  - e possivelmente outros Define no conjunto Admin.

Public readback de um PDP (`define-cropped-jacket-nulu`) retornou conteúdo pobre/ruído de troca/devolução no fetch simplificado, indicando necessidade de QA público antes de mexer em copy.

## Diagnóstico

A LK já tem presença em Popular Products, mas falta uma superfície orgânica canônica para capturar a busca `lululemon define jacket`.

Isso é parecido com o caso Samba Marrom:
- produtos existem;
- demanda/alerta existe;
- collection específica não existe;
- Growth não deve criar collection diretamente se depender de membership/Shopify object.

## Recomendação

P1 próximo: abrir handoff para LK Shopify validar/criar/ativar collection canônica:

- handle preferido: `/collections/lululemon-define-jacket`
- title sugerido: `Lululemon Define Jacket`
- incluir apenas produtos Lululemon Define ativos já existentes;
- sem consultar/alterar estoque;
- sem alterar preço, campanhas, GMC, Klaviyo ou checkout;
- readback público 200 OK.

Depois da superfície 200 OK, Growth prepara em dev:
- guia/FAQ/schema focado em Define Jacket;
- diferenças Nulu vs Luon;
- cropped vs regular;
- fit/modelagem;
- autenticidade e curadoria LK;
- evitar preço fixo e promessas de disponibilidade.

## Não recomendado agora

- Não mexer em `alo yoga brasil`: o alerta era positivo e a LK já aparece em `alo yoga roupa` na posição orgânica 8.
- Não mexer em `nike vomero premium valor`: alerta era ganho forte.
- Não publicar copy/SEO diretamente em PDP sem novo readback completo.

## Aprovação sugerida

Aprovo abrir handoff para LK Shopify validar/criar/ativar a collection canônica Lululemon Define Jacket, preferencialmente `/collections/lululemon-define-jacket`, usando apenas produtos Lululemon Define ativos já existentes, sem consultar ou alterar estoque, preço, campanhas, GMC, Klaviyo ou checkout, com preview/readback público; após a superfície 200 OK, Growth prepara guia/FAQ/schema em dev antes de qualquer produção.
