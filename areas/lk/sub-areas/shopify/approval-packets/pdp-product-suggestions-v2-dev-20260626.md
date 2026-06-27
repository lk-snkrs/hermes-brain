# Approval packet — PDP Sugestões de Produto v2 — DEV

Data: 2026-06-26  
Agente: lk-shopify  
Superfície: Shopify theme DEV/unpublished / PDP recomendações abaixo do produto

## Pedido

Lucas corrigiu a direção: o problema não é só filtrar a primeira coleção. O campo inteiro **Relacionados** está conceitualmente errado e precisa melhorar a sugestão de produtos.

## Diagnóstico read-only

### Problema atual

O bloco atual `Relacionados` é alimentado por `product.collections.first`, o que mistura produtos por acidente de coleção/termo e não por intenção comercial/editorial.

Mesmo após o patch DEV tático por `type/vendor`, ainda é uma solução limitada, porque:

- depende da coleção acidental;
- não usa sinais melhores de recomendação;
- pode competir com a Curadoria LK;
- não separa “mesma variação/silhueta” de “complementares/descoberta”.

### Evidência de fonte melhor

Audit público read-only comparou 3 fontes:

1. `Relacionados` atual por coleção;
2. `Curadoria LK` (`lk-variante`), quando existe;
3. Shopify `/recommendations/products.json?intent=related`.

#### PDP boné Saint George

- Relacionados por coleção atual: inclui `tenis-new-balance-9060-bone-sparrow-marrom` — ruim.
- Curadoria LK: retorna bonés ALD coerentes.
- Shopify Recommendations API: retorna vários ALD coerentes; precisa filtrar type `Boné` para não trazer camisetas.

#### PDP Air Jordan 1 Low Panda

- Curadoria LK: variações específicas do grupo AJ1 Low.
- Recommendations API: retorna Air Jordan 1 Low relevantes.

#### PDP Onitsuka Mexico 66 Triple Black

- Relacionados por coleção atual: mistura NB204L/NB9060/Samba — ruim.
- Curadoria LK: Mexico 66 coerentes.
- Recommendations API: majoritariamente Onitsuka/Mexico 66, mas ainda precisa filtro para remover cross-brand residual.

## Modelo recomendado — PDP Product Suggestions v2

Substituir o bloco visual **Relacionados** por uma nova lógica de sugestões em 2 papéis claros:

### 1. `Curadoria LK` continua sendo “mesma família / variações”

- `lk-variante` permanece acima/na área atual.
- É o bloco mais editorial e controlado.
- Não deve ser duplicado por `Relacionados`.

### 2. Novo bloco abaixo: `Você também pode gostar`

Fonte primária:

- Shopify Recommendations API `intent=related`, porque ela já retorna sinais melhores que `product.collections.first`.

Filtro obrigatório:

1. excluir produto atual;
2. excluir handles já exibidos em Curadoria LK quando detectáveis no DOM;
3. priorizar mesmo `type` + mesmo `vendor`;
4. depois mesmo `type`;
5. depois mesmo `vendor`, se fizer sentido;
6. bloquear cross-type ruim em acessórios — exemplo: boné não deve puxar tênis por conter “bone” no título;
7. renderizar até 4 cards;
8. se não houver pelo menos 2 bons candidatos, esconder bloco.

### Fallback

Se a Recommendations API falhar ou vier fraca:

- manter o fallback por coleção apenas com filtro estrito já aprovado em DEV;
- nunca voltar ao `product.collections.first limit:4` sem filtro.

## Implementação DEV proposta

Escopo:

- `sections/lk-pdp.liquid`

Mudanças:

1. manter o fallback Liquid filtrado atual;
2. adicionar wrapper com dados do produto:
   - product id;
   - handle;
   - vendor;
   - type;
   - handles já presentes em Curadoria LK quando renderizados no DOM;
3. adicionar JS leve para buscar `/recommendations/products.json?product_id={{ product.id }}&intent=related&limit=12`;
4. filtrar/ordenar candidatos client-side;
5. renderizar cards simples no padrão visual `lk-product-card`/grade atual ou, se a estrutura exata ficar arriscada, manter Liquid fallback e só substituir quando houver card seguro;
6. registrar marker `data-lk-related-v2="recommendations-filtered-20260626"`.

## Critérios de aceite DEV

### Boné Saint George

- Não aparece `tenis-new-balance-9060-bone-sparrow-marrom`.
- Sugestões são bonés/ALD coerentes.
- Não duplica o mesmo handle já na Curadoria LK, quando detectável.

### Air Jordan 1 Low Panda

- Sugestões são Air Jordan/Jordan/tênis coerentes.
- Não aparecem acessórios/apparel.

### Onitsuka Mexico 66 Triple Black

- Sugestões priorizam Onitsuka/Mexico 66/tênis similares.
- Não puxa NB/Samba se houver candidatos Onitsuka suficientes.

### Geral

- HTTP `200`.
- Liquid errors `0`.
- JS exceptions `0`.
- Mobile continua 2 colunas.
- Production não alterado.

## Risco

Médio:

- envolve JS/render client-side no PDP;
- precisa QA visual para não quebrar card/price/image;
- melhora relevância, mas não substitui curadoria editorial humana para famílias importantes.

## Rollback

Restaurar `sections/lk-pdp.liquid` do backup DEV anterior:

`/opt/data/profiles/lk-shopify/workdirs/pdp-relacionados-relevance-20260626/dev_before_sections__lk-pdp.liquid`

ou remover o bloco JS/marker `data-lk-related-v2` e voltar ao fallback Liquid filtrado.

## Fora de escopo

- Sem produto/preço/estoque/Tiny/checkout/GMC/Klaviyo/ads/WhatsApp.
- Sem Production merge.
- Sem promessa de disponibilidade.
- Sem alterar Curadoria LK já publicada, exceto leitura de handles para evitar duplicidade.

## Aprovação necessária

Para aplicar essa versão melhor em DEV:

> Aprovo DEV Product Suggestions v2 no PDP usando Recommendations API filtrada + fallback Liquid, sem Production merge.

## Reminder OS

- loop needed: yes
- owner: lk-shopify
- next action: aguardar aprovação DEV; se aprovada, aplicar em DEV, readback e QA visual/público.
- review trigger: resposta de Lucas aprovando ou ajustando o modelo.
- evidence: audit público em `/opt/data/profiles/lk-shopify/workdirs/pdp-relacionados-relevance-20260626/suggestion_sources_audit.json`.
