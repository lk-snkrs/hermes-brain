# LKGOC Collection Template v1 — contrato técnico a partir da 204L

Status: DRAFT CANÔNICO — forensic audit concluído, refactor ainda não executado
Data: 2026-06-09
Dono: LK Collection Optimizer

## 1. Objetivo

Transformar a implementação aprovada da collection **New Balance 204L** em um template LKGOC reutilizável para novas collections otimizadas, sem repetir o erro de copiar HTML/classe ou criar templates por coleção sem contrato.

Pergunta central de Lucas:

> Como transformar a 204L de uma implementação aprovada em um template LKGOC reutilizável sem perder o visual aprovado?

## 2. Descoberta principal do forensic audit

A 204L aprovada em Production **não usa um template separado**.

Dados reais Shopify:

- Collection `new-balance-204l`
  - tipo: smart collection
  - id: `455991394526`
  - `template_suffix`: `""` / default
- Template usado:
  - `templates/collection.json`
  - section principal: `sections/lk-collection.liquid`
- Production/main não possui `templates/collection.lkgoc.json`.
- DEV/unpublished possui `templates/collection.lkgoc.json`, mas esse template ainda não é o gold real da 204L.

Conclusão: a 204L hoje é uma implementação **hardcoded no template default**, não um template LKGOC limpo.

## 3. Onde a 204L renderiza hoje

Arquivos production auditados:

- `templates/collection.json`
- `sections/lk-collection.liquid`
- `snippets/lk-goc-new-balance-204l-guide-panel.liquid`
- `snippets/lk-goc-collection.liquid`
- `snippets/lk-goc-guide-contract.liquid`

### 3.1 Template JSON atual

`templates/collection.json`:

```json
{
  "sections": {
    "main": {
      "type": "lk-collection",
      "settings": {
        "products_per_page": 24
      }
    }
  },
  "order": ["main"]
}
```

### 3.2 CSS/base visual 204L

Em `sections/lk-collection.liquid`, há CSS global baseado em:

- `.lk-204l-coll-preview`
- `.lk-goc-coll-preview`
- `body:has(.lk-204l-coll-preview)`
- `#lk-guia-new-balance-204l`

Isso controla:

- fundo escuro do banner/hero;
- ocultação da descrição padrão;
- layout da galeria;
- modal de imagem;
- espaçamento do guide;
- grid editorial do guide.

### 3.3 Hero 204L

O hero da 204L aparece dentro de `sections/lk-collection.liquid` com:

```liquid
{%- if collection.handle == 'new-balance-204l' -%}
  ... HTML/CSS/JS do hero 204L ...
{%- endif -%}
```

Ou seja: não é data-driven, nem template-driven. É condicional por handle dentro da section default.

### 3.4 Descrição override

A descrição da 204L é aplicada no mesmo arquivo via:

```liquid
{%- case collection.handle -%}
  {%- when 'new-balance-204l' -%}
    {%- assign lk_desc_override = '...' -%}
```

### 3.5 Guide pós-grid

O guide da 204L é renderizado pós-grid com:

```liquid
{% render 'lk-goc-guide-contract' %}
{%- if collection.handle == 'nike-mind-001' -%}
  ...
{%- elsif collection.handle == 'new-balance-204l' -%}
  {% render 'lk-goc-new-balance-204l-guide-panel' %}
```

O conteúdo do guide fica em:

- `snippets/lk-goc-new-balance-204l-guide-panel.liquid`

## 4. Por que as tentativas anteriores deram errado

### 4.1 Erro 1 — `collection.puma-speedcat`

Criar `templates/collection.puma-speedcat.json` não replica a 204L, porque a 204L não usa esse modelo. Isso cria uma rota paralela.

### 4.2 Erro 2 — `collection.lkgoc` sem migrar a 204L

`templates/collection.lkgoc.json` existe no DEV, mas não é o gold real da 204L em Production. Usar `?view=lkgoc` validou outro caminho, não o caminho aprovado.

### 4.3 Erro 3 — trocar apenas `template_suffix`

Colocar Speedcat com o mesmo `template_suffix` da 204L significa default, mas se o default só tem hardcode para 204L, a Speedcat continua sem LKGOC.

### 4.4 Erro 4 — copiar classe/HTML

Copiar `.lk-204l-coll-preview` pode parecer certo visualmente, mas não cria contrato técnico reutilizável. Só transfere dívida técnica.

## 5. Definição correta do LKGOC Collection Template v1

O template correto precisa ser extraído da 204L e formalizado como componente reutilizável.

### 5.1 Estrutura alvo

- `templates/collection.lkgoc.json`
  - template oficial para collections otimizadas.
- `sections/lk-goc-collection-template.liquid` ou evolução segura de `sections/lk-collection.liquid`
  - renderiza hero + grid + guide em ordem canônica.
- dados por coleção em fonte controlada:
  - metafields/metaobjects preferencialmente;
  - ou snippet data-map temporário, mas sem HTML solto por coleção.

### 5.2 Ordem canônica de render

1. Banner/crumbs/título da collection.
2. Hero editorial LKGOC.
3. Grid nativo de produtos Shopify.
4. Guide editorial pós-grid.
5. FAQ/schema quando aplicável.

### 5.3 Contrato visual

O LKGOC v1 deve preservar o gold 204L:

- shell escuro premium;
- kicker “CURADORIA LK”;
- headline editorial curta;
- copy humana e comercial;
- galeria/collage à direita no desktop;
- comportamento mobile sem quebra;
- guide pós-grid com card amplo + FAQ lateral no desktop;
- CTA para guia completo quando existir;
- sem linguagem pública de estoque/pronta entrega.

### 5.4 Contrato de dados por collection

Cada collection otimizada precisa fornecer:

- `handle`
- `hero_aria_label`
- `kicker`
- `headline`
- `hero_body`
- `hero_cards[]`
  - image URL / asset
  - alt
  - label
- `desc_override`
- `guide_anchor`
- `guide_title`
- `guide_intro`
- `guide_bullets[]`
- `faq[]`
- `guide_page_url`
- `schema_faq` boolean

## 6. Refactor seguro recomendado

### Fase 1 — DEV read-only/diff

- Congelar Speedcat.
- Usar 204L Production como snapshot de gold.
- Criar screenshot baseline 204L mobile/desktop.
- Criar mapa DOM baseline:
  - hero;
  - grid;
  - guide;
  - schema;
  - product links.

### Fase 2 — extrair sem mudar visual

No DEV/unpublished:

1. Criar novo snippet/component:
   - `snippets/lk-goc-collection-hero.liquid`
   - recebe dados prontos.
2. Criar novo snippet/component:
   - `snippets/lk-goc-collection-guide.liquid`
   - recebe dados prontos.
3. Criar data-map inicial:
   - `snippets/lk-goc-collection-data.liquid`
   - primeiro só com `new-balance-204l`.
4. Alterar `sections/lk-collection.liquid` no DEV para renderizar 204L via componentes novos.
5. QA 204L DEV vs 204L Production:
   - visual side-by-side;
   - DOM contract;
   - Liquid error 0;
   - grid e guide na mesma posição relativa;
   - sem regressão de product links.

Critério: 204L em DEV precisa ficar indistinguível da 204L Production.

### Fase 3 — criar template oficial

Depois que a 204L estiver idêntica via componentes:

- criar/ajustar `templates/collection.lkgoc.json` para usar a mesma section/componentes;
- decidir se `collection.lkgoc` será o template futuro ou se o default seguirá roteando collections otimizadas.

Recomendação: `collection.lkgoc` deve virar o template oficial, mas só depois de provar equivalência com 204L.

### Fase 4 — aplicar Speedcat

Só depois:

- adicionar dados Speedcat no data-map;
- atribuir Speedcat ao template oficial em DEV;
- QA mobile/desktop;
- approval Lucas;
- só então production.

## 7. Critérios de QA obrigatórios

Para qualquer collection LKGOC:

- Theme DEV role: `unpublished` antes de qualquer teste.
- `Liquid error`: 0.
- Hero existe.
- Grid existe.
- Guide existe pós-grid.
- Product links preservados.
- Não há texto herdado da collection gold.
- Não há “pronta entrega”, “estoque imediato” ou linguagem pública de estoque.
- Mobile e desktop renderizam sem overlay/corte.
- 204L não sofre regressão.

## 8. Decisão operacional

Não fazer mais Speedcat direto.

A próxima execução correta é:

1. Refactor 204L no DEV para componentes/data-map.
2. Provar equivalência 204L DEV vs 204L Production.
3. Só então criar Speedcat como segunda instância do template.

## 9. Artefatos do forensic audit

Diretório local:

`/opt/data/profiles/lk-collection-optimizer/output/lkgoc-204l-forensic-20260609/`

Arquivos principais:

- `collection-new-balance-204l.json`
- `themes.json`
- `main/templates__collection.json`
- `main/sections__lk-collection.liquid`
- `main/snippets__lk-goc-new-balance-204l-guide-panel.liquid`
- `prod_204l.html`
- `dev_204l.html`
- `204l-render-map.json`

## 10. Regra final

A 204L é o gold visual. O LKGOC v1 só existe quando a 204L puder ser renderizada por um contrato reutilizável sem mudar visualmente.

Até lá, copiar para Speedcat é implementação manual, não template LKGOC.


---

## 11. Correção após consulta Shopify.dev — padrão escalável correto

Fonte consultada em 2026-06-09:

- Shopify JSON templates: `https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates`
- Shopify sections: `https://shopify.dev/docs/storefronts/themes/architecture/sections`
- Shopify metafields: `https://shopify.dev/docs/apps/build/custom-data/metafields`
- Shopify metaobjects: `https://shopify.dev/docs/apps/build/custom-data/metaobjects`

### 11.1 O que a Shopify recomenda

Para padronizar e escalar páginas/collections em tema Shopify, a arquitetura correta é:

1. **JSON template** controla quais sections entram e em qual ordem.
   - Ex.: `templates/collection.lkgoc.json`.
   - O template armazena lista de sections e settings.
   - Merchant pode adicionar/remover/reordenar sections no Theme Editor quando a section tem schema/presets.

2. **Sections reutilizáveis** são módulos Liquid customizáveis.
   - Devem conter schema.
   - Devem ser referenciadas por JSON templates sempre que possível.
   - Shopify recomenda JSON templates para renderizar sections em templates, em vez de static render/hardcode.

3. **Metafields** servem para dados específicos de um recurso Shopify.
   - Para collection: campos como headline, intro, CTA, flag de otimização, referência ao guia.

4. **Metaobjects** servem para estruturas complexas e reutilizáveis.
   - Ideal para blocos LKGOC com múltiplos campos: hero cards, FAQs, bullets, media manifest, guide blocks.

### 11.2 Implicação para LKGOC

O LKGOC correto não deve ficar hardcoded em `sections/lk-collection.liquid` por `collection.handle`.

A arquitetura escalável deve ser:

- `templates/collection.lkgoc.json`
  - template oficial das coleções otimizadas.
- `sections/lk-goc-collection.liquid`
  - section única de LKGOC Collection.
  - contém a ordem interna canônica: hero → grid wrapper/slot → guide/FAQ.
  - ou, se o grid precisa continuar na section base, usar um wrapper claro com sections separadas em JSON: hero section, main collection grid section, guide section.
- `metafields` na collection para dados simples:
  - `custom.lkgoc_enabled`
  - `custom.lkgoc_profile`
  - `custom.lkgoc_hero_title`
  - `custom.lkgoc_hero_intro`
  - `custom.lkgoc_guide_title`
  - `custom.lkgoc_guide_url`
- `metaobjects` para dados compostos:
  - `lkgoc_collection_profile`
  - hero cards;
  - guide bullets;
  - FAQ;
  - media usage/manifest.

### 11.3 Decisão técnica revisada

A 204L atual continua sendo gold visual, mas **não deve ser copiada como arquitetura**.

O próximo passo correto é criar um LKGOC v1 Shopify-native:

1. Criar uma nova section Shopify-native:
   - `sections/lk-goc-collection.liquid` ou `sections/lk-goc-collection-v1.liquid`.
2. Criar `templates/collection.lkgoc.json` apontando para essa section e/ou para sections modulares.
3. Alimentar a section por metafields/metaobjects, não por múltiplos `if collection.handle`.
4. Migrar a 204L em DEV para esse template e validar equivalência visual contra Production.
5. Só depois aplicar Puma Speedcat como segunda collection usando o mesmo template.

### 11.4 Melhor arquitetura para LK

Opção recomendada: **JSON template com 3 sections**.

```json
{
  "sections": {
    "lkgoc_hero": {
      "type": "lk-goc-collection-hero",
      "settings": {}
    },
    "main": {
      "type": "lk-collection",
      "settings": {
        "products_per_page": 24,
        "lkgoc_template_mode": true
      }
    },
    "lkgoc_guide": {
      "type": "lk-goc-collection-guide",
      "settings": {}
    }
  },
  "order": ["lkgoc_hero", "main", "lkgoc_guide"]
}
```

Vantagens:

- segue Shopify JSON template;
- mantém o grid Shopify existente (`lk-collection`) sem reescrever tudo;
- hero e guide viram sections próprias e editáveis;
- evita `if collection.handle` espalhado;
- permite aplicar `template_suffix = lkgoc` em novas collections;
- escala para Speedcat, 9060, 530 etc.

### 11.5 O que não fazer mais

- Não criar `collection.puma-speedcat.json` como template permanente.
- Não usar `?view=lkgoc` como prova final.
- Não resolver com classe `--speedcat` ou clone visual solto.
- Não adicionar novos blocos hardcoded em `sections/lk-collection.liquid` por handle, exceto transição controlada.
- Não mexer em Production antes de provar que 204L DEV no novo template é visualmente equivalente à 204L Production.

### 11.6 Próxima execução aprovada pelo contrato

Fase DEV:

1. Criar branch limpa para `lkgoc-shopify-native-v1`.
2. Criar sections:
   - `lk-goc-collection-hero.liquid`
   - `lk-goc-collection-guide.liquid`
3. Criar/ajustar template:
   - `templates/collection.lkgoc.json`
4. Primeiro preencher dados 204L via settings do próprio JSON template para equivalência visual.
5. Em fase 2, migrar dados para metafields/metaobjects para escala operacional.
6. Aplicar 204L no DEV com `template_suffix = lkgoc` apenas no ambiente/collection de teste ou usando preview seguro.
7. QA visual 204L novo template vs 204L production.
8. Só depois Speedcat.

### 11.7 Observação importante sobre dados

Shopify JSON templates não compartilham section data entre templates. Por isso, para escala real, o conteúdo não deve viver duplicado em cada JSON template. Deve vir de metafields/metaobjects por collection.

Para o MVP, settings no JSON são aceitáveis para provar equivalência com 204L. Para escala, metafields/metaobjects são obrigatórios.
