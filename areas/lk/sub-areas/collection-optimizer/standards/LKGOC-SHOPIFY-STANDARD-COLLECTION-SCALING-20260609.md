# LKGOC — Padrão Shopify para coleções escaláveis

Status: **CANÔNICO / EM DEFINIÇÃO APÓS ERRO 530**  
Data: 2026-06-09  
Dono: `[LK] Otimização de Coleções` / LKGOC  
Escopo: coleções Shopify LK com padrão visual/editorial derivado do gold source 204L.

---

## 1. Por que este documento existe

Lucas identificou corretamente que as tentativas anteriores estavam erradas porque:

- criavam HERO duplicado;
- tentavam resolver por CSS incremental;
- aceitavam algo “parecido” em vez de **exatamente o padrão aprovado**;
- não definiam uma arquitetura Shopify escalável;
- misturavam padrão visual, conteúdo, guide e overrides por `collection.handle` dentro da mesma section.

A regra correta é:

> Para novas coleções LKGOC, a LK precisa de um **template Shopify padrão e escalável**, onde a estrutura visual é fixa e aprovada, e cada coleção muda apenas texto, imagens, links e blocos de conteúdo.

---

## 2. Referências oficiais Shopify consultadas

### JSON templates

Fonte: Shopify Dev — JSON templates.

Pontos relevantes:

- JSON templates controlam layout usando sections.
- Um JSON template armazena lista de sections, settings e ordem.
- Sections são renderizadas na ordem do atributo `order`, sem markup entre elas.
- JSON templates suportam alternate templates.
- Cada JSON template pode ter até 25 sections.
- Cada section pode ter até 50 blocks.
- Section IDs precisam ser únicos dentro do template.
- Sections sem `presets` podem ser incluídas manualmente no JSON, mas não aparecem para adição livre no Theme Editor.

Implicação LKGOC:

- O padrão correto não é hardcodear uma coleção dentro de `lk-collection.liquid`.
- O padrão correto é um `templates/collection.lkgoc.json` com sections LKGOC fixas e settings/blocks por instância.

### Sections

Fonte: Shopify Dev — Sections.

Pontos relevantes:

- Sections são módulos Liquid reutilizáveis e customizáveis.
- Sections podem ser usadas via JSON templates.
- Shopify recomenda JSON templates para renderizar sections dentro de templates, por serem mais customizáveis e performáticos no Theme Editor.
- Statically rendered sections devem ser evitadas quando possível.
- Sections em JSON templates podem ter settings e blocks próprios.

Implicação LKGOC:

- LKGOC deve ser composto por sections reutilizáveis.
- O conteúdo de cada coleção deve vir de settings/blocks/metafields, não de if/elsif por handle.

### Collection template

Fonte: Shopify Dev — Collection template.

Pontos relevantes:

- O template `collection` renderiza uma página que lista produtos da coleção.
- O template ou uma section dentro dele deve incluir o objeto `collection`.
- Produtos da coleção devem ser paginados; `collection.products` tem limite de 50 por página.
- Filtros/sort devem continuar respeitando o fluxo storefront.

Implicação LKGOC:

- O grid nativo da collection não pode ser quebrado.
- A section de grid deve continuar usando o objeto `collection`, paginação, filtro e sort existentes.
- LKGOC deve envolver/acompanhar o grid, não substituir o funcionamento comercial da coleção.

### Alternate templates

Fonte: Shopify Dev — Alternate templates.

Pontos relevantes:

- É possível criar templates alternativos para o mesmo tipo de recurso.
- O formato é `collection.<suffix>.json`.
- Um alternate template pode ser aplicado ao recurso no admin ou renderizado via `?view=<suffix>`.
- Exemplo: `collection.lkgoc.json` pode ser renderizado com `?view=lkgoc`.

Implicação LKGOC:

- DEV/QA deve usar `?view=lkgoc` antes de alterar assignment de template.
- Production só deve receber assignment/publicação após approval Lucas.

---

## 3. O erro que fica proibido

Fica proibido como padrão LKGOC:

- criar hero separado acima do topo existente e causar duplicação;
- ajustar collection por “remendo visual” de CSS por handle;
- colocar múltiplos branches `if collection.handle == ...` dentro de `lk-collection.liquid` como arquitetura de escala;
- considerar “clone” válido apenas porque tem classes parecidas;
- aceitar medidas “quase iguais” ao gold source;
- alterar Production para testar;
- criar layout novo sem referência aprovada.

Se houver divergência visual, a correção correta é no **padrão/componentização**, não em patch isolado.

---

## 4. Gold source visual obrigatório

Gold source atual: **New Balance 204L**.

Para uma coleção ser considerada LKGOC compatível, ela deve reproduzir a mesma estrutura visual da 204L:

1. topo/banner da collection sem duplicação de H1;
2. bloco editorial/curadoria com a mesma hierarquia;
3. collage/galeria com mesma proporção e comportamento;
4. grid comercial preservado;
5. guide pós-grid com mesma estrutura;
6. FAQ/schema quando aplicável;
7. mobile e desktop com o mesmo contrato visual medido.

O conteúdo muda. A estrutura não muda.

---

## 5. Arquitetura Shopify correta para escalar

### 5.1 Template padrão

Arquivo alvo:

```text
templates/collection.lkgoc.json
```

Função:

- ser o template padrão reutilizável de coleções LKGOC;
- conter a ordem canônica das sections;
- permitir preview por `?view=lkgoc`;
- depois permitir assignment em cada collection aprovada.

Estrutura recomendada:

```json
{
  "sections": {
    "lkgoc_hero": {
      "type": "lk-goc-collection-hero",
      "settings": {}
    },
    "main_grid": {
      "type": "lk-collection",
      "settings": {
        "lkgoc_grid_only": true
      }
    },
    "lkgoc_guide": {
      "type": "lk-goc-collection-guide",
      "settings": {}
    }
  },
  "order": [
    "lkgoc_hero",
    "main_grid",
    "lkgoc_guide"
  ]
}
```

Observação crítica:

- Isso **não** significa criar um segundo hero se `lk-collection` já renderiza hero.
- Para essa arquitetura funcionar, `lk-collection` precisa ter modo `grid_only`, sem banner/hero/guide interno.
- Se o tema atual usa `lk-collection` para banner + grid + guide, é preciso separar responsabilidades antes de escalar.

### 5.2 Section hero LKGOC

Arquivo alvo:

```text
sections/lk-goc-collection-hero.liquid
```

Responsabilidade:

- renderizar o padrão visual aprovado da 204L;
- conter o markup fixo do hero/editorial;
- receber conteúdo por settings/blocks/metafields;
- nunca depender de branch por handle.

Não pode:

- inventar novo layout;
- ter CSS específico por coleção;
- duplicar H1 se o template já tem H1 em outro lugar;
- carregar guide ou grid.

### 5.3 Section grid

Arquivo existente:

```text
sections/lk-collection.liquid
```

Responsabilidade em LKGOC:

- renderizar apenas grid, filtros, sort, paginação, produtos e load more;
- preservar `collection` object;
- não renderizar hero/editorial/guide quando chamado pelo template LKGOC.

Setting recomendado:

```json
{
  "type": "checkbox",
  "id": "lkgoc_grid_only",
  "label": "LKGOC grid only",
  "default": false
}
```

Regra:

- se `lkgoc_grid_only == true`: não renderizar banner, descrição, trust strip nem guide hardcoded.
- se `false`: comportamento legado preservado.

### 5.4 Section guide LKGOC

Arquivo alvo:

```text
sections/lk-goc-collection-guide.liquid
```

Responsabilidade:

- renderizar guide pós-grid no padrão 204L;
- receber título, intro, blocos, FAQs e CTAs por settings/blocks/metafields;
- manter schema/FAQ quando aplicável;
- não depender de handle hardcoded.

---

## 6. Fonte de conteúdo por coleção

A escala correta deve seguir uma destas opções, nesta ordem de maturidade:

### Opção A — JSON template com blocks/settings

Boa para DEV e primeiras coleções.

- cada collection usa `collection.lkgoc.json` ou alternate específico;
- conteúdo fica em section settings/blocks;
- bom para testar o padrão sem criar infraestrutura de metafields.

Limite:

- se o mesmo `collection.lkgoc.json` for usado por várias coleções com settings fixos, o conteúdo não pode ser diferente por coleção.
- para conteúdo diferente por coleção, precisa de alternate template por coleção ou fonte dinâmica.

### Opção B — Collection metafields

Mais escalável.

Exemplos de metafields:

```text
collection.metafields.lkgoc.kicker
collection.metafields.lkgoc.headline
collection.metafields.lkgoc.intro
collection.metafields.lkgoc.hero_image_1
collection.metafields.lkgoc.hero_image_2
collection.metafields.lkgoc.hero_image_3
collection.metafields.lkgoc.guide_title
collection.metafields.lkgoc.guide_intro
collection.metafields.lkgoc.faq_json
```

Vantagem:

- um único `collection.lkgoc.json` serve para várias coleções;
- muda conteúdo por coleção sem duplicar template;
- facilita escala e manutenção.

### Opção C — Metaobject LKGOC

Mais organizada para operação premium.

Criar metaobject `lkgoc_collection_content` com campos:

- handle interno;
- collection reference;
- hero kicker;
- hero headline;
- hero body;
- image 1/2/3;
- image alt 1/2/3;
- guide title;
- guide intro;
- guide cards;
- FAQ;
- related collections;
- schema flags.

A collection referencia um metaobject:

```text
collection.metafields.lkgoc.content_ref
```

Vantagem:

- conteúdo editorial separado do código;
- reutilizável;
- melhor para gestão por equipe.

---

## 7. Contrato visual: “igual ao 204L”

Antes de implementar nova coleção, registrar o contrato visual do gold source 204L.

Mínimo obrigatório:

### Desktop

- posição do hero/editorial;
- altura do bloco;
- altura da collage;
- grid-template-columns;
- gap;
- transform/margem se houver overlap;
- posição inicial do grid;
- largura e margem do guide;
- H1 único.

### Mobile

- ordem do conteúdo;
- altura do bloco;
- comportamento da collage;
- se imagens secundárias aparecem ou são ocultadas;
- espaçamento antes do grid;
- guide pós-grid;
- legibilidade do headline.

QA não pode aprovar apenas DOM presente. Precisa aprovar **medida + screenshot + comparação visual**.

---

## 8. Fluxo canônico de nova coleção LKGOC

### Passo 1 — escolher gold source

- Gold atual: 204L.
- Se o gold mudar, documentar antes.

### Passo 2 — criar pacote de conteúdo

Para cada coleção:

- handle;
- título;
- intenção comercial;
- produtos relevantes;
- imagens internas/Shopify ou mídia aprovada;
- headline curto no mesmo ritmo visual;
- intro;
- guide;
- FAQs;
- links relacionados.

### Passo 3 — preencher fonte dinâmica

Preferência futura:

- metafields ou metaobject.

Enquanto isso:

- template/section settings em DEV, mas sem hardcode por handle como padrão final.

### Passo 4 — preview DEV

Usar:

```text
/collections/<handle>?preview_theme_id=<DEV_THEME_ID>&view=lkgoc
```

Ou se o template já estiver atribuído no DEV:

```text
/collections/<handle>?preview_theme_id=<DEV_THEME_ID>
```

### Passo 5 — QA obrigatório

- theme role = `unpublished`;
- Liquid error = 0;
- H1 único;
- sem hero duplicado;
- grid preservado;
- filtros/sort/paginação preservados;
- guide pós-grid;
- medidas comparadas com 204L;
- screenshot mobile e desktop;
- conteúdo sem linguagem proibida de estoque/pronta entrega;
- imagens com direito de uso/media manifest.

### Passo 6 — approval Lucas

Antes de qualquer production:

- enviar preview;
- enviar screenshots;
- explicar divergências, se houver;
- rollback plan;
- pedir approval explícito.

### Passo 7 — Production

Só após approval:

- aplicar template/assignment ou merge;
- validar live;
- salvar receipt;
- agendar impact review.

---

## 9. O que fazer agora com 530

A 530 não deve ser usada como prova de arquitetura enquanto ainda depender de:

- snippet específico `lk-goc-new-balance-530-hero-204l-clone`;
- CSS final de compensação;
- guide específico por handle dentro de `lk-collection`.

Ela pode servir como evidência de problemas, mas não como padrão escalável.

O próximo trabalho correto é:

1. congelar visual 204L como gold source;
2. criar `lk-goc-collection-hero` copiando exatamente o markup/CSS do gold;
3. criar `lk-goc-collection-guide` copiando exatamente o guide gold;
4. adaptar `lk-collection` para modo `grid_only` limpo;
5. criar `collection.lkgoc.json` com hero + grid + guide;
6. preencher uma coleção teste mudando só texto/imagens;
7. comparar com 204L antes de chamar de pronto.

---

## 10. Regra de ouro

> Se para uma nova coleção for necessário escrever CSS específico para “parecer com a 204L”, a arquitetura ainda está errada.

O padrão certo é:

- uma estrutura visual única;
- dados por coleção;
- QA comparativo;
- sem branches por handle;
- sem hero duplicado;
- sem Production sem approval.
