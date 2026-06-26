# PRD — Mostrar coleção New Balance 9060 na busca por “9060”

Data UTC: 20260603T203113Z
Status: PRD / approval packet — sem write executado
Responsável sugerido: LK Shopify / Theme CRO
Superfície: Shopify Theme Search Page (`/search`) + opcional Search & Discovery/predictive search

---

## 1. Problema

Ao buscar `9060` em:

`https://lksneakers.com.br/search?q=9060`

A página mostra uma grade de produtos encontrados, mas não destaca a coleção canônica:

`/collections/new-balance-9060`

Isso cria fricção porque o cliente que pesquisa apenas o modelo provavelmente quer chegar na coleção completa, com filtros, copy de coleção, ordenação/merchandising e SEO da família New Balance 9060 — não apenas ver uma lista de produtos soltos da busca.

---

## 2. Evidência read-only coletada

### Busca live

URL testada:

`https://lksneakers.com.br/search?q=9060&cb=prd9060`

Resultado observado:

- Página respondeu OK.
- Busca mostra aproximadamente `55 resultado(s)`.
- A página renderiza produtos New Balance 9060 na grade.
- A coleção `new-balance-9060` não aparece como resultado destacado no corpo da busca; ocorrência encontrada no HTML era do menu/header, não de um card de resultado de coleção.

### Coleção existe e está populada

URL:

`https://lksneakers.com.br/collections/new-balance-9060`

Resultado observado:

- Título live: `New Balance 9060`.
- Collection JSON:
  - handle: `new-balance-9060`
  - title: `New Balance 9060`
  - products_count público: `51`
- Amostras de produtos:
  - `Tênis New Balance 9060 Bisque Sea Salt Bege`
  - `Tênis New Balance 9060 Mushroom Arid Stone Bege`
  - `Tênis New Balance 9060 Sea Salt Moonbeam Branco`
  - `Tênis New Balance 9060 Rich Oak Marrom`
  - `Tênis New Balance 9060 Triple White Branco`

### Predictive/Search Suggest já encontra a coleção

Endpoint público testado:

`/search/suggest.json?q=9060&resources[type]=product,collection`

Resultado:

- `collections` inclui `New Balance 9060`.
- Ou seja: o dado existe e o Shopify consegue associar `9060` à coleção; o problema é de UX/renderização da página `/search` e/ou configuração do tipo de recurso buscado.

### Estado do tema live

Asset live consultado via Admin read-only:

`sections/lk-search.liquid`

Trechos relevantes observados:

```liquid
<form action="/search" method="get" class="search-banner__form">
  <input type="text" name="q" ...>
  <input type="hidden" name="type" value="product">
</form>
```

E na grade:

```liquid
{%- for item in search.results -%}
  {%- if item.object_type == 'product' -%}
    {% render 'lk-product-card', product: item %}
  {%- endif -%}
{%- endfor -%}
```

Interpretação:

- O formulário força `type=product` nas novas buscas.
- O template ignora qualquer resultado que não seja produto.
- Mesmo se `collection` entrar em `search.results`, a seção atual não renderiza card de coleção.

---

## 3. Objetivo

Quando o usuário pesquisar `9060`, a busca deve mostrar claramente a coleção canônica `New Balance 9060` antes da grade de produtos.

Objetivo prático:

- O usuário vê um bloco/card/banner “Coleção encontrada: New Balance 9060”.
- Clicar leva para `/collections/new-balance-9060`.
- A grade de produtos continua aparecendo abaixo.
- A solução deve ser escalável para outros modelos futuramente, mas o MVP pode começar com `9060`.

---

## 4. Métrica de sucesso

### UX

- Em `/search?q=9060`, acima da grade de produtos, aparece um módulo de coleção com:
  - título: `New Balance 9060`
  - texto curto: `Ver todos os modelos New Balance 9060`
  - link/CTA para `/collections/new-balance-9060`
  - contagem, se possível: `51 produtos`

### Técnica

- Busca por `9060` continua carregando produtos normalmente.
- Nenhum produto some da busca por causa da correção.
- Filtros/sort existentes continuam funcionando.
- Mobile e desktop exibem o módulo sem quebrar layout.

### Segurança operacional

- Primeiro aplicar no tema Dev/unpublished.
- Validar preview.
- Só depois promover para production com aprovação explícita.

---

## 5. Escopo do MVP recomendado

### Incluir

1. Alterar `sections/lk-search.liquid` no tema Dev.
2. Adicionar um módulo “Coleção encontrada” acima da toolbar ou acima da grid.
3. Para o MVP, usar um mapa controlado no Liquid para queries de alto valor:
   - `9060` → `/collections/new-balance-9060`
   - título: `New Balance 9060`
   - subtítulo: `51 produtos disponíveis` ou texto sem contagem dinâmica se a contagem não estiver disponível com segurança no Liquid.
4. Manter a grade de produtos abaixo.
5. Ajustar o formulário de busca para não forçar somente produto quando for seguro:
   - opção A: manter `type=product` e renderizar o módulo por mapa próprio; menor risco.
   - opção B: mudar para `type=product,collection` e renderizar `item.object_type == 'collection'`; mais nativo, mas exige QA de contagem/filtros.
6. QA em desktop e mobile.

### Não incluir no MVP

- Não mexer em produtos, estoque, preço, checkout ou apps.
- Não alterar coleção, SEO fields ou descrição da coleção.
- Não mudar Search & Discovery settings sem aprovação separada.
- Não generalizar para todos os modelos automaticamente sem lista aprovada.
- Não remover a grade de produtos.

---

## 6. Solução recomendada

### Recomendação: Opção A — Módulo curado de coleção por query/modelo

Criar um bloco no `lk-search.liquid` que detecta a query normalizada e, quando ela bate com um modelo de coleção importante, renderiza um “collection hit” antes dos produtos.

Por que esta opção é melhor para começar:

- Resolve exatamente o problema do `9060`.
- Baixo risco para a página de busca inteira.
- Não depende de comportamento incerto do `search.results` para collections no tema atual.
- Não altera o motor de busca; só adiciona um atalho UX para coleção canônica.
- Pode ser expandido depois para `204L`, `530`, `Samba`, `Campus`, `Dunk`, etc.

### Comportamento esperado

Para `/search?q=9060`:

- Banner atual continua: `Resultados para "9060"`.
- Abaixo do banner ou entre banner e toolbar, exibir:

```text
Coleção encontrada
New Balance 9060
Explore todos os modelos, cores e tamanhos disponíveis.
[Ver coleção]
```

Link:

`/collections/new-balance-9060`

Grade abaixo:

- Continua exibindo os produtos buscados.

---

## 7. Design/UX sugerido

### Desktop

Posição:

- Logo abaixo do banner preto da busca e acima da toolbar “Filtros / X resultados / Ordenar”.

Layout:

- Card horizontal clean, similar a faixa editorial/collection promo.
- Fundo off-white ou branco com borda leve.
- Título em serif/estilo LK:
  - `New Balance 9060`
- Label pequeno uppercase:
  - `Coleção encontrada`
- CTA à direita:
  - `Ver coleção`

### Mobile

Posição:

- Logo abaixo do banner.
- Card vertical compacto.
- CTA full-width ou alinhado à esquerda.

### Copy recomendada

Label:

`Coleção encontrada`

Título:

`New Balance 9060`

Texto:

`Veja todos os modelos, cores e tamanhos disponíveis na curadoria LK.`

CTA:

`Ver coleção 9060`

---

## 8. Requisitos funcionais

1. Dado que o usuário acessa `/search?q=9060`, então o módulo de coleção deve aparecer.
2. Dado que o usuário acessa `/search?q=new%20balance%209060`, então o módulo também deve aparecer.
3. Dado que o usuário acessa `/search?q=nb%209060`, então o módulo deve aparecer se incluirmos alias no MVP.
4. Dado que o usuário clica no CTA, então deve ir para `/collections/new-balance-9060`.
5. Dado que o usuário pesquisa outro termo sem mapeamento, então a busca deve funcionar exatamente como hoje.
6. A grade de produtos deve continuar sendo renderizada normalmente.
7. Filtros, sort e load-more devem continuar funcionando.

---

## 9. Requisitos técnicos

### Arquivo principal

`sections/lk-search.liquid`

### Alteração mínima sugerida

1. Normalizar termo de busca:

```liquid
{%- assign lk_search_terms_normalized = search.terms | downcase | strip -%}
```

2. Detectar query 9060:

```liquid
{%- assign lk_collection_hit_handle = blank -%}
{%- assign lk_collection_hit_title = blank -%}

{%- if lk_search_terms_normalized == '9060'
  or lk_search_terms_normalized contains 'new balance 9060'
  or lk_search_terms_normalized == 'nb 9060' -%}
  {%- assign lk_collection_hit_handle = 'new-balance-9060' -%}
  {%- assign lk_collection_hit_title = 'New Balance 9060' -%}
{%- endif -%}
```

3. Renderizar módulo se houver match:

```liquid
{%- if lk_collection_hit_handle != blank -%}
  <section class="lk-search-collection-hit" aria-label="Coleção encontrada">
    <div class="lk-search-collection-hit__eyebrow">Coleção encontrada</div>
    <div class="lk-search-collection-hit__content">
      <h2 class="lk-search-collection-hit__title">{{ lk_collection_hit_title }}</h2>
      <p class="lk-search-collection-hit__text">Veja todos os modelos, cores e tamanhos disponíveis na curadoria LK.</p>
    </div>
    <a class="lk-search-collection-hit__cta" href="/collections/{{ lk_collection_hit_handle }}">Ver coleção 9060</a>
  </section>
{%- endif -%}
```

4. CSS no próprio section ou asset existente, seguindo o padrão visual da LK.

### Futuro melhorado

Depois do MVP, trocar mapa hardcoded por section blocks no schema:

- block type: `collection_search_alias`
- settings:
  - query aliases: `9060,new balance 9060,nb 9060`
  - collection: `new-balance-9060`
  - title override
  - text override

Isso permite Lucas/equipe editar aliases via Theme Editor sem novo deploy.

---

## 10. Plano de implementação seguro

### Fase 0 — Precheck read-only

- Confirmar tema Dev:
  - `lk-new-theme/dev`
  - `role = unpublished`
- Confirmar production:
  - `lk-new-theme/production`
  - `role = main`
- Fazer backup/readback de `sections/lk-search.liquid` do Dev e Production.

### Fase 1 — Branch/Git

- Criar branch a partir de `origin/dev`:

```bash
git checkout dev
git pull origin dev
git checkout -b fix/search-collection-hit-9060
```

- Materializar `sections/lk-search.liquid` no repo se o arquivo local estiver ausente/desatualizado, usando readback do Dev/Production como base correta.

### Fase 2 — Implementar no Dev theme

- Patch somente em `sections/lk-search.liquid`.
- Adicionar CSS + markup do módulo.
- Não mexer em `lk-collection.liquid`, produto, coleção, preço ou estoque.

### Fase 3 — QA Dev preview

Validar:

- `/search?q=9060` mostra módulo `Coleção encontrada`.
- CTA aponta para `/collections/new-balance-9060`.
- `/search?q=new%20balance%209060` também mostra.
- `/search?q=adidas` não mostra módulo 9060.
- Produtos continuam aparecendo.
- Filtros e sort continuam clicáveis.
- Mobile não quebra layout.

### Fase 4 — PR e merge em dev

- Commit no branch.
- PR contra `dev`.
- Merge em `dev` após QA/aprovação.

### Fase 5 — Production somente com aprovação explícita

Após Lucas aprovar:

- Backup do production asset.
- Upload só de `sections/lk-search.liquid` aprovado.
- Readback SHA.
- QA live em `/search?q=9060&cb=...`.
- Receipt/rollback.

---

## 11. Critérios de aceite

### Dev

- [ ] Em preview Dev, `/search?q=9060` mostra `Coleção encontrada`.
- [ ] O card contém `New Balance 9060`.
- [ ] CTA abre `/collections/new-balance-9060`.
- [ ] Produtos continuam aparecendo abaixo.
- [ ] Busca por termo não mapeado não mostra card incorreto.
- [ ] Mobile OK.
- [ ] Readback do asset Dev bate com SHA local.

### Production

- [ ] Após aprovação explícita, live `/search?q=9060` mostra o módulo.
- [ ] CTA live funciona.
- [ ] Production readback bate com asset aprovado.
- [ ] Nenhuma alteração fora do escopo foi feita.
- [ ] Receipt salvo com backup e rollback.

---

## 12. Riscos e mitigação

### Risco: hardcode virar manutenção manual

Mitigação:

- MVP hardcoded só para `9060`.
- Próxima versão com blocks/configuração editável.

### Risco: alterar comportamento dos filtros da busca

Mitigação:

- Não mudar `type=product` no MVP.
- Apenas adicionar módulo acima da busca.

### Risco: collection hit aparecer para termo errado

Mitigação:

- Usar match conservador:
  - `9060`
  - `new balance 9060`
  - `nb 9060`
- Não usar `contains '90'` ou regex ampla.

### Risco: Production theme com asset remoto diferente do repo

Mitigação:

- Usar readback live como base antes do patch.
- Backup antes de qualquer upload.
- Upload apenas do asset aprovado.

---

## 13. Rollback

### Dev

- Reverter commit do branch ou restaurar backup do Dev asset.

### Production

- Re-subir o backup anterior de `sections/lk-search.liquid`.
- Alternativamente, `git revert` do commit se a promoção for via branch/PR e o production branch estiver sincronizado.

---

## 14. Decisão necessária

Para executar o MVP no tema Dev/unpublished, Lucas precisa aprovar explicitamente:

`aprovo aplicar no tema dev o módulo de coleção encontrada para busca 9060`

Isso autoriza apenas:

- patch em `sections/lk-search.liquid` no tema Dev/unpublished;
- QA de preview;
- PR contra `dev`.

Não autoriza:

- production;
- produto/coleção/metafield;
- preço/estoque;
- Search & Discovery settings;
- campanhas/apps.
