# LKGOC — Padronização Shopify Collections

Registrado em: 20260606T212139Z

## Objetivo
Evitar erro estrutural em coleções Shopify, especialmente confundir `pós-grid` com uma posição visual aproximada. No LKGOC, coleção padronizada é uma composição controlada de template JSON + seções Liquid + QA DOM/visual.

## Fontes pesquisadas
- Shopify Dev Docs — `collection` template: a página de coleção lista produtos da coleção, deve usar o objeto `collection`, filtros/sort podem ser usados e produtos via `collection.products` têm limite de 50 por página, exigindo paginação.
- Shopify Dev Docs — JSON templates: templates JSON renderizam seções na ordem definida em `order`, sem markup entre seções; aceitam `sections` + `order`; até 25 seções por template e até 50 blocos por seção.
- Shopify Dev Docs — templates, sections and blocks best practices: conteúdo padrão do template deve estar em uma seção principal; seções/blocos devem ser modulares, reordenáveis e com fluxo lógico; evitar granularidade excessiva e layouts frágeis por ordem arbitrária de blocos.
- Shopify Dev Docs — section schema: seção deve ter schema válido, settings únicos, blocks com IDs/settings próprios, `presets` para adicionabilidade no theme editor e `enabled_on`/`disabled_on` para restringir uso.
- Shopify Dawn reference — `templates/collection.json`: estrutura base `banner` → `product-grid`.
- Shopify Dawn reference — `sections/main-collection-product-grid.liquid`: grid real fica dentro de `paginate collection.products`; produtos são renderizados no loop `{% for product in collection.products %}` dentro de `<ul id="product-grid">`; paginação vem depois do `</ul>` quando `paginate.pages > 1`.

## Princípio canônico LK
A coleção LKGOC deve preservar a hierarquia Shopify nativa:

1. **Hero / banner editorial**
2. **Grid de produtos completo**
3. **Pós-grid editorial** — somente após o último produto/card renderizado
4. **FAQ / Schema / blocos auxiliares** — também depois do grid completo, salvo exceção aprovada

## Regra crítica: pós-grid
`Pós-grid` significa **depois de todos os produtos renderizados na página atual da coleção** e, quando houver paginação/load more/infinite scroll, depois do mecanismo oficial de continuação do grid.

É proibido considerar pós-grid:
- depois do início do `ProductGridContainer`;
- depois de filtros/sort;
- depois de uma linha parcial de produtos;
- depois de uma imagem/screenshot sem contagem de cards;
- dentro do `<ul id="product-grid">`;
- antes da paginação/load-more quando esse elemento representa continuação da listagem.

Erro bloqueante: `FAIL_POS_GRID_NOT_AFTER_ALL_PRODUCTS`.

## Arquitetura recomendada para LK

### Template JSON
Usar um template de coleção LKGOC com ordem explícita e estável. Exemplo conceitual:

```json
{
  "sections": {
    "main_collection_banner": { "type": "main-collection-banner" },
    "main_collection_product_grid": { "type": "main-collection-product-grid" },
    "lk_goc_after_grid": { "type": "lk-goc-after-grid" }
  },
  "order": [
    "main_collection_banner",
    "main_collection_product_grid",
    "lk_goc_after_grid"
  ]
}
```

Observação: o LKGOC pode adaptar nomes ao tema real, mas a ordem semântica é obrigatória.

### Seção pós-grid dedicada
Criar/manter seção própria para conteúdo pós-grid, por exemplo:
- `sections/lk-goc-after-grid.liquid`
- namespace CSS: `lk-goc-*`
- `enabled_on.templates`: collection
- sem app blocks por padrão se isso fragilizar layout
- settings/blocos suficientes para conteúdo editorial/FAQ sem granularidade excessiva

### Não acoplar pós-grid ao grid
O conteúdo editorial não deve ser injetado dentro do loop:

```liquid
{% for product in collection.products %}
  ... card produto ...
{% endfor %}
```

Nem dentro do `<ul id="product-grid">`.

O correto é que o pós-grid seja uma seção posterior no `order` do JSON, ou markup depois do fechamento inequívoco do grid e da paginação, quando tecnicamente necessário.

## QA obrigatório antes de PASS

### 1. QA de template
- Verificar que o tema é DEV/unpublished antes de qualquer write.
- Verificar arquivo de template JSON aplicado à collection alvo.
- Confirmar `order`: banner/hero antes, `product-grid` antes de `lk-goc-after-grid`.
- Confirmar que a seção pós-grid não está dentro do grid principal.

### 2. QA de Liquid/DOM
- Localizar `<ul id="product-grid">` ou seletor equivalente real do tema.
- Contar os cards renderizados no grid na página atual.
- Identificar o último card/produto.
- Confirmar que o primeiro nó LKGOC pós-grid aparece depois do fechamento do grid e depois da paginação/load-more, se existir.
- Se usar infinite scroll, o pós-grid não pode interromper a listagem; precisa ficar depois do componente de continuação ou ser condicionado a fim real.

### 3. QA visual/mobile
- Screenshot mobile deve mostrar fim do grid/produto final e início do pós-grid na sequência.
- Screenshot desktop deve confirmar mesma sequência.
- Não aprovar com screenshot que só mostra hero + primeiros produtos.

### 4. QA editorial/GEO
- O pós-grid deve ter blocos citáveis e escaneáveis.
- FAQ/schema só se o conteúdo está visível e coerente com a collection.
- Tom LK: curadoria exclusiva, autenticidade, atendimento humano, confirmação via chat quando necessário.
- Não usar taxonomia pública de pronta entrega/encomenda/estoque.

## Checklist rápido de implementação LKGOC
1. Carregar padrão gold source aprovado, não inventar layout novo.
2. Verificar DEV theme `role: unpublished` por API.
3. Mapear collection template real e seções existentes.
4. Inserir/adaptar seção pós-grid como seção posterior ao grid no JSON.
5. Garantir que o grid permanece nativo, paginado, filtrável e ordenável.
6. Rodar QA DOM: último card → paginação/load-more, se houver → pós-grid.
7. Rodar QA visual mobile/desktop.
8. Criar approval packet para Lucas.
9. Só promover para production após aprovação explícita.
10. Registrar rollback e revisão de impacto em ~7 dias.

## Decisão operacional
Para evitar repetir o erro: **nenhum relatório LKGOC pode chamar algo de pós-grid sem prova DOM/visual do último produto antes do bloco.**
