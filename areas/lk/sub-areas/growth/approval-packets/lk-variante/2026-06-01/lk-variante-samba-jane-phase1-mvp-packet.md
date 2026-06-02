# LK Variante — Fase 1 + MVP Samba Jane

Data UTC: 2026-06-01
Escopo: read-only + desenho de MVP. Nenhum write Shopify/app/theme executado neste pacote.

## Definição aprovada em conversa

**LK Variante** é um sistema próprio para mostrar variações lógicas de produtos irmãos, não um filtro por cor.

Exemplo: cliente entra em uma PDP de New Balance 9060 ou Adidas Samba Jane e vê miniaturas dos produtos irmãos/variações mais relevantes daquele grupo, ordenadas por performance comercial/best-seller.

Regras do Lucas:

- O grupo lógico (`variant_group`) é a parte central.
- Filtro por cor não é o objetivo.
- Preferência inicial: usar **tag** para unir produtos do grupo.
- Também pode haver inteligência automática para sugerir grupos/ordem.
- Ordenação deve usar best-seller e pode ser atualizada semanalmente ou quinzenalmente.
- MVP de teste: **Adidas Samba Jane**.

## O que o Variant King/StarApps faz hoje na LK

PDP auditada:

`/products/tenis-adidas-samba-jane-white-black-branco`

Achados:

- HTML da PDP: 1,243,359 bytes
- `window.vkcl_data`: presente 1 vez
- `window.vkcl_data`: ~460,328 bytes inline
- CSS Variant King `app="vsk"`: ~188,112 bytes inline
- Ocorrências `variant-king-combined-listing`: 1,174
- Ocorrências `swatch-preset`: 1,169
- Scripts externos StarApps/Variant King também presentes via CDN/extension.

Interpretação:

- O app é o maior alvo de payload atual.
- O custo não é só download: é parse/execute/render no mobile.
- Um substituto próprio pode economizar centenas de KB se no futuro o app puder ser removido/desligado para grupos migrados.

## Produtos candidatos — grupo Samba Jane

Fonte pública: `/collections/adidas-samba-jane/products.json?limit=250`

A coleção pública retorna 10 produtos, mas contém 3 produtos `Adidas Tokyo Mary Jane` que não parecem ser Samba Jane. Portanto, para o MVP, **não usar a coleção como fonte única do grupo**. Usar tag/canonical group e/ou regra por handle/título.

Produtos Samba Jane encontrados na coleção pública:

1. `tenis-adidas-samba-jane-white-blue-gum-branco`
2. `tenis-adidas-samba-jane-white-black-branco`
3. `tenis-adidas-samba-jane-scarlet-gum-vermelho`
4. `tenis-adidas-samba-jane-cream-black-gum-bege`
5. `tenis-adidas-samba-jane-green-white-gum-verde`
6. `tenis-adidas-samba-jane-black-white-gum-preto`
7. `tenis-adidas-samba-jane-chalk-white-wonder-quartz-branco`
8. `tenis-adidas-samba-jane-white-red-gum-branco` — aparece no SQL local, mas não apareceu na resposta pública da coleção atual.

Produtos que apareceram na coleção mas devem ficar fora do variant_group Samba Jane:

- `tenis-adidas-tokyo-mary-jane-sandy-pink-earth-strata-rosa`
- `tenis-adidas-tokyo-mary-jane-crystal-sky-cream-white-azul`
- `tenis-adidas-tokyo-mary-jane-cream-white-red-gold-metallic-creme`

## Ordem comercial inicial por vendas locais

Fonte: SQLite local `lk_os_phase5.sqlite`, tabelas `lk_products`, `lk_order_items`, `lk_orders`.

Observação: Data Spine pode estar defasado; para produção final, validar com Shopify orders/read-only catch-up se necessário.

Ranking por `units_180`, desempate `units_all`:

1. White Black — 5 unidades/180d, 16 all-time
2. Cream Black Gum — 3 unidades/180d, 12 all-time
3. White Blue Gum — 3 unidades/180d, 7 all-time
4. Black White Gum — 2 unidades/180d, 16 all-time
5. Scarlet Gum — 2 unidades/180d, 13 all-time
6. Green White Gum — 2 unidades/180d, 6 all-time
7. Chalk White Wonder Quartz — 0 unidades
8. White Red Gum — 0 unidades

Proposta para exibir na PDP:

- Mostrar até 6 miniaturas.
- Produto atual sempre aparece selecionado.
- Os demais aparecem por ordem best-seller do grupo.
- Se o produto atual não estiver no top 6, incluir produto atual + top 5.

## Estratégia de tag recomendada

Tag canônica para grupo:

`lk_variant_group:samba-jane`

Tags opcionais futuras:

- `lk_variant_label:White Black`
- `lk_variant_label:Black White Gum`
- `lk_variant_label:Cream Black Gum`
- `lk_variant_order:<n>` se quiser override manual.

Observação: hoje os produtos não têm uma tag padronizada comum. Alguns têm `Samba Jane`, outros só best-seller tags, outros tags vazias no SQL local. Portanto, qualquer uso por tag exigirá correção/aplicação de tags em Shopify, que é write de produto e precisa aprovação separada.

## MVP técnico proposto

### Arquivos de tema

- `snippets/lk-variant-swatches.liquid`
- `assets/lk-variante.css`
- `assets/lk-variante.js`
- opcional para piloto sem tag write: `assets/lk-variante-groups.json`

### Modo MVP sem mexer em tags ainda

Para reduzir risco, o primeiro preview dev pode usar um JSON estático de piloto Samba Jane no tema dev, sem alterar produtos:

- agrupa os 7/8 handles Samba Jane;
- renderiza apenas quando `product.handle` pertence ao grupo;
- mostra thumbnail, label curta, preço/availability pública quando disponível;
- clica para navegar para a PDP irmã;
- mantém Variant King ativo como fallback, inicialmente sem removê-lo.

Depois, se o visual e comportamento forem aprovados, migrar a fonte para tags/metafields.

### Modo final por tag

Quando aprovado, Shopify product tags alimentam o group:

- todos os produtos do grupo recebem `lk_variant_group:samba-jane`;
- script/rotina quinzenal calcula ordem best-seller;
- Liquid lê ou recebe group data pré-gerado;
- miniaturas aparecem em PDP/cards.

## Algoritmo de ordenação

Score recomendado:

`score = units_180 * 4 + units_90 * 3 + units_all * 0.5 + availability_bonus + newness_soft_bonus`

Regras:

- excluir produtos draft/unpublished;
- produto sem disponibilidade pode aparecer depois dos disponíveis ou ficar com badge `sob encomenda`, dependendo regra comercial;
- produto atual sempre visível;
- atualizar semanalmente ou quinzenalmente;
- gerar receipt com ranking antes de qualquer write.

## Riscos

- Agrupar errado produtos semelhantes, especialmente `Samba`, `Sambae`, `Samba Jane`, `Tokyo Mary Jane`.
- Duplicar UI com Variant King se ambos aparecerem no mesmo bloco.
- Se depender só de collection, entra produto errado no grupo.
- Se depender só de título/handle, pode falhar em exceções futuras.
- Tag write é produto/admin write e precisa aprovação separada.
- Remover/desligar Variant King é mudança de app/tema com risco alto; não fazer no MVP inicial.

## Próxima fase recomendada

Fase 2A — Preview dev sem product-tag write:

1. Criar `lk-variante` em tema dev `155065450718` usando JSON piloto Samba Jane.
2. Inserir snippet na PDP de forma guardada: só aparece para handles do grupo piloto.
3. Não remover Variant King ainda.
4. Validar mobile/desktop, clique, visual e peso.
5. Se aprovado, decidir se o bloco substitui/oculta visualmente o app em Samba Jane.

Fase 2B — Tag canonical:

1. Preparar preview de tags a aplicar nos produtos Samba Jane.
2. Lucas aprova product-tag write separadamente.
3. Aplicar tags com backup/readback.
4. Trocar fonte do MVP para tags/dados gerados.

## Aprovação necessária para execução dev

Para subir o MVP no tema dev, aprovação sugerida:

**“Aprovado criar preview LK Variante Samba Jane no tema dev 155065450718, sem production, sem remover Variant King e sem alterar tags/produtos.”**

Para aplicar tags em produto depois, seria outra aprovação:

**“Aprovado aplicar tag `lk_variant_group:samba-jane` nos produtos Samba Jane listados no packet, com backup e readback.”**

## Não realizado

- Nenhum upload para Shopify.
- Nenhuma alteração de tema dev/production.
- Nenhuma tag/metafield/produto alterado.
- Nenhum app removido/desativado.
- Nenhum preço/estoque/checkout/campanha alterado.
