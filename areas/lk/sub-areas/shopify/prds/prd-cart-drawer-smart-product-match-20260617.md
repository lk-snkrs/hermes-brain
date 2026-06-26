# PRD — Cart Drawer Smart Product Match

Data: 2026-06-17
Owner: LK Shopify
Status: PRD / aguardando decisão de produto
Escopo: LK Sneakers Shopify cart drawer — bloco de recomendação/upsell

## 1. Problema

O bloco atual de recomendação no cart drawer está apresentando produtos semanticamente errados para o contexto do carrinho.

Exemplo observado por Lucas no preview:

- Título: `MAIS VENDIDOS LK`
- Produtos exibidos: calça Accolade, Adidas Taekwondo, camiseta Basic Pack.
- Contexto: dentro do cart drawer, após o usuário já demonstrar intenção por um item específico.

Isso quebra a expectativa do usuário porque o cart drawer é um momento de confirmação/fechamento, não de navegação genérica. Uma recomendação aleatória ou ampla demais parece ruído, reduz confiança e disputa atenção com o checkout.

## 2. Diagnóstico técnico atual

No snippet `snippets/lk-cart-drawer.liquid`, a lógica atual é:

1. Detectar alguns modelos via `LK_MODEL_COLLECTIONS`.
2. Se detectar, buscar `/collections/{modelo}/products.json?limit=16&sort_by=best-selling`.
3. Se não detectar ou se a coleção falhar/retornar vazia, cair para `/collections/all/products.json?limit=16&sort_by=best-selling`.
4. Renderizar fallback com título `Mais vendidos LK`.

Falha principal: o fallback `collections/all + best-selling` mistura categorias e pode sugerir peças sem relação com o item do carrinho. Mesmo o rótulo `Você também pode gostar` seria fraco se a lógica continuar ampla demais.

## 3. Objetivo

Substituir a recomendação genérica por uma lógica de match contextual, com alta precisão e baixo risco visual/comercial.

A recomendação deve responder à pergunta:

> “Qual produto faz sentido mostrar agora para alguém que está prestes a comprar ESTE item?”

Não deve responder:

> “Quais são os produtos mais vendidos da loja inteira?”

## 4. Princípio de produto

No cart drawer, **precisão > quantidade**.

Se o sistema não tiver confiança suficiente para recomendar algo coerente, é melhor esconder o bloco do que mostrar produtos desconexos.

Regra central:

- Mostrar até 4 recomendações somente quando houver match confiável.
- Não usar fallback genérico de loja inteira para carrinho com sneaker.
- Nunca mostrar categorias aleatórias como apparel se o item principal for sneaker, exceto em uma regra explícita de complemento aprovada.

## 5. Definição de “match correto”

### 5.1 Hierarquia de recomendação

#### Nível A — Mesmo modelo / mesma silhueta
Prioridade máxima. Exemplo:

- Carrinho: New Balance 530
- Recomendar: outros New Balance 530, preferencialmente cores/tamanhos disponíveis.

Copy sugerida:

- `Mais cores do seu modelo`
- Alternativa: `Também no seu modelo`

#### Nível B — Silhueta adjacente dentro da mesma intenção
Quando não há produtos suficientes no mesmo modelo.

Exemplos:

- Adidas Samba → Gazelle / Handball Spezial / SL 72 / Campus
- Nike Dunk Low → Air Jordan 1 Low / Nike Cortez apenas se a curadoria aprovar; não misturar com calça/camiseta.
- Onitsuka Mexico 66 → Adidas Samba/Gazelle/Spezial como proposta terrace/retro low-profile.

Copy sugerida:

- `Na mesma estética`
- `Modelos parecidos`

#### Nível C — Complemento explícito, só para categorias compatíveis
Usar somente quando a categoria permite cross-sell claro.

Exemplos:

- Sneaker → meia premium / lace / cuidado, se existirem e forem uma estratégia aprovada.
- Apparel → apparel da mesma cápsula/marca/cor.
- Pack/camiseta → outro pack/camiseta; não sneaker aleatório.

Copy sugerida:

- `Completa o pedido`

#### Nível D — Sem recomendação
Se nenhum dos níveis acima gerar pelo menos 2 itens confiáveis, esconder o bloco.

Não renderizar:

- `Mais vendidos LK`
- `Você também pode gostar`
- `/collections/all` como fallback amplo
- produtos de categoria incompatível

## 6. Seleção do item principal do carrinho

Quando houver mais de um item, definir o “anchor item” para gerar as sugestões.

Ordem proposta:

1. Item de maior valor total de linha.
2. Se empate, item adicionado mais recentemente se essa informação estiver disponível no front; se não, primeiro item do cart JSON.
3. Se o carrinho tiver sneaker + apparel, o sneaker vira anchor por padrão.
4. Se o carrinho tiver múltiplos sneakers de modelos diferentes, usar o item de maior valor; não misturar recomendações de vários modelos no mesmo bloco.

## 7. Taxonomia necessária

A lógica precisa de uma taxonomia explícita, não só busca textual solta.

### 7.1 Campos mínimos por regra

Cada grupo de recomendação deve conter:

- `id`: chave interna.
- `label`: nome humano do grupo.
- `category`: sneaker, apparel, accessory, care, etc.
- `patterns`: padrões de handle/title para detecção.
- `primary_collection`: collection canônica para Nível A.
- `adjacent_collections`: collections permitidas para Nível B.
- `excluded_categories`: categorias bloqueadas.
- `title_primary`: copy quando Nível A acionar.
- `title_adjacent`: copy quando Nível B acionar.

### 7.2 Mapa inicial sugerido

Sneakers:

- New Balance 530 → `new-balance-530`
- New Balance 9060 → `new-balance-9060`
- Adidas Samba → `adidas-samba`; adjacentes: `adidas-gazelle`, `adidas-spezial`, `adidas-campus`
- Adidas Gazelle → `adidas-gazelle`; adjacentes: `adidas-samba`, `adidas-spezial`, `adidas-campus`
- Adidas Campus → `adidas-campus`; adjacentes: `adidas-samba`, `adidas-gazelle`, `adidas-spezial`
- Adidas Spezial / Handball Spezial → `adidas-spezial`; adjacentes: `adidas-samba`, `adidas-gazelle`, `adidas-campus`
- Onitsuka Tiger Mexico 66 → `onitsuka-tiger-mexico-66`; adjacentes: `adidas-samba`, `adidas-gazelle`, `adidas-spezial`
- Nike Dunk Low → `nike-dunk-low`; adjacentes: a validar com Lucas
- Air Jordan 1 Low → `air-jordan-1-low`; adjacentes: a validar com Lucas
- Nike Cortez → `nike-cortez`; adjacentes: `adidas-samba`, `onitsuka-tiger-mexico-66` se a curadoria aprovar
- ASICS Gel-Kayano 14 → `asics-gel-kayano-14`; adjacentes: a validar com Lucas

Apparel/acessórios:

- Não misturar com sneaker por fallback.
- Só entra como complemento se houver regra explícita e copy própria.

## 8. Filtros obrigatórios

Antes de renderizar qualquer card:

1. Excluir produtos já no carrinho.
2. Excluir produto atual/anchor.
3. Excluir produto sem imagem válida.
4. Excluir produto indisponível conforme disponibilidade exposta no storefront JSON.
5. Preferir variante com mesmo tamanho do item anchor quando existir.
6. Não renderizar botão `Adicionar` sem `variant_id` confiável.
7. Limitar a 4 cards.
8. Se restarem menos de 2 cards, esconder bloco ou cair para Nível B; não cair para loja inteira.

Nota de governança: disponibilidade operacional/estoque real continua sendo domínio do LK Stock. O cart drawer pode usar apenas a disponibilidade pública exposta pelo storefront para não renderizar item impossível de adicionar; decisões de estoque/reposição devem ser validadas com LK Stock.

## 9. Copy e nomenclatura

Evitar:

- `Mais vendidos LK`
- `Você também pode gostar`
- `Recomendados para você` quando a lógica não for personalizada de verdade.

Preferir copy específica ao motivo da recomendação:

- Nível A: `Mais cores do seu modelo`
- Nível A alternativo: `Também no seu modelo`
- Nível B: `Modelos parecidos`
- Nível B alternativo: `Na mesma estética`
- Nível C: `Completa o pedido`

## 10. UX / Layout

O bloco deve continuar compacto e secundário ao checkout.

Requisitos:

- Não empurrar o CTA de checkout para fora da área visível em mobile.
- Não ocupar mais atenção visual que o item do carrinho + checkout.
- Manter cards compactos atuais, mas garantir imagem limpa e nome legível.
- Se não houver recomendação coerente, remover o bloco sem deixar espaço vazio.

## 11. Comportamento esperado por cenário

### Cenário 1 — Carrinho com New Balance 530

Esperado:

- Título: `Mais cores do seu modelo`
- Produtos: outros NB 530.
- Excluir o NB 530 já no carrinho.

### Cenário 2 — Carrinho com Adidas Samba

Esperado:

1. Primeiro tentar `adidas-samba`.
2. Se houver menos de 2 itens, buscar adjacentes terrace/low-profile aprovados: Gazelle, Spezial, Campus.
3. Nunca mostrar calça/camiseta via fallback.

### Cenário 3 — Carrinho com sneaker sem mapa

Esperado:

- Não mostrar `Mais vendidos LK`.
- Se houver categoria/silhueta inferida com alta confiança, usar adjacentes aprovados.
- Se não houver confiança: esconder bloco.

### Cenário 4 — Carrinho com apparel

Esperado:

- Não sugerir sneaker aleatório.
- Usar mesma categoria/cápsula/marca se houver regra.
- Caso contrário, esconder bloco.

### Cenário 5 — Carrinho misto: sneaker + apparel

Esperado:

- Sneaker vira anchor.
- Recomendações seguem lógica do sneaker.

## 12. Requisitos técnicos

### 12.1 Arquivo provável

- `snippets/lk-cart-drawer.liquid`

### 12.2 Mudanças esperadas

- Remover fallback amplo `loadCuratedBestSellersFallback` baseado em `/collections/all`.
- Introduzir função de scoring/decisão:
  - `getAnchorItem(cart)`
  - `classifyCartItem(item)`
  - `buildRecommendationPlan(anchor)`
  - `fetchCollectionProducts(handle)`
  - `rankCandidates(candidates, anchor, strategy)`
  - `renderUpsell(container, products, title, strategy)`
- Guardar reason/strategy no DOM para QA:
  - `data-lk-upsell-strategy="same-model|adjacent|complement|hidden"`
  - `data-lk-upsell-anchor="new-balance-530"`

### 12.3 Fallback correto

Substituir:

- fallback de loja inteira

Por:

1. same-model
2. adjacent approved model group
3. approved complement group
4. hidden

## 13. Critérios de aceite

### Funcional

- Produto sneaker conhecido no carrinho gera recomendações do mesmo modelo quando existirem.
- Produto sneaker conhecido nunca cai em `collections/all` genérico.
- Produto sem match confiável não mostra bloco.
- Produto já no carrinho nunca aparece como recomendação.
- Cards sem variant ID não exibem botão adicionar.
- Mesmo tamanho é preferido quando disponível no product JSON.

### Visual

- O bloco não deixa espaço vazio quando oculto.
- O CTA de checkout continua visível/acessível no mobile.
- Cards permanecem compactos.

### QA

Testar pelo menos:

- New Balance 530.
- Adidas Samba.
- Nike Dunk Low.
- Produto sem mapa.
- Apparel.
- Carrinho misto.
- Carrinho com 4+ itens para validar scroll.

### Métrica / observabilidade

Eventos opcionais para etapa futura, sem bloquear v1:

- `lk_cart_upsell_view` com `strategy`, `anchor`, `count`.
- `lk_cart_upsell_add` com `strategy`, `anchor`, `product_handle`.
- `lk_cart_upsell_hidden` com `reason`.

## 14. Riscos

- Coleções canônicas podem estar incompletas ou mal ordenadas.
- Detecção por texto/handle pode falhar em produtos com nomes inconsistentes.
- Product JSON público pode ter limitação de campos para categoria/tags.
- Sugestão por tamanho depende de variante exposta corretamente.
- Se tentarmos ser amplos demais, voltamos ao problema original.

Mitigação:

- Começar com taxonomia explícita pequena e expandir por batches.
- QA por modelos prioritários.
- Preferir esconder o bloco quando a confiança for baixa.

## 15. Fora de escopo nesta fase

- Alterar preço, estoque, disponibilidade operacional ou checkout.
- Criar campanha, Klaviyo, ads, WhatsApp ou email.
- Escrever produto/metafield/tag em Shopify sem aprovação específica.
- Production publish/merge sem aprovação separada.
- Sistema de recomendação ML/personalização por usuário.

## 16. Plano de rollout seguro

1. Implementar em branch/local ou worktree isolado.
2. Criar diff apenas em `snippets/lk-cart-drawer.liquid`, salvo necessidade comprovada.
3. Fazer preview packet com lógica, arquivos, QA e rollback.
4. Subir para Dev/unpublished somente após aprovação explícita.
5. Readback Admin + QA público com carrinho real.
6. Só depois pedir aprovação separada para production.

## 17. Decisões pendentes para Lucas

1. Confirmar se o bloco deve sumir quando não houver match bom. Recomendação: sim.
2. Confirmar copy preferida:
   - `Mais cores do seu modelo`
   - `Modelos parecidos`
   - `Completa o pedido`
3. Confirmar grupos adjacentes para Nike Dunk Low, Air Jordan 1 Low, ASICS Gel-Kayano 14 e Nike Cortez.
4. Decidir se acessórios/apparel podem aparecer como complemento de sneaker ou se ficam totalmente bloqueados nesta v1.

## 18. Recomendação de decisão

Para v1, aprovar:

- Bloquear completamente o fallback `Mais vendidos LK` no cart drawer.
- Usar somente same-model + adjacent approved.
- Esconder o bloco quando não houver match confiável.
- Não misturar apparel/acessórios com sneaker nesta primeira versão.

Isso resolve a falha mais visível sem introduzir uma lógica ampla demais.
