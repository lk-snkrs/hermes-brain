# Plano de rollout — padrão Guia + Coleção LK

Data: 2026-05-29
Status: plano corrigido após alinhamento de Lucas.

## Correção importante

A coleção `new-balance-204l` **não entra no lote de aplicação**.

Ela já foi feita e é a **gold source** do padrão visual da coleção product-first e do bloco guia pós-grid.

## Fonte de verdade

- Coleção gold source: `new-balance-204l`
- Dev theme usado como referência: `155065450718`
- Padrão de coleção: `lk-collection-v2`
- Padrão do bloco pós-grid: `Guia Editorial LK` no layout 204L
- Padrão de guia standalone: Moon Shoe/Jacquemus
- Padrão de tabela comparativa em guia: Moon Shoe `compact table v3` — tabela real compacta no mobile, sem cards/lista editorial

## Sequência correta

### Fase 1 — Guias standalone faltantes

Criar guias dedicados primeiro para coleções elegíveis: marcas, linhas, modelos e collabs.

Não começar por tipo genérico de produto.

Primeiros candidatos:

1. `nike-dunk-sb`
2. `nike-air-force-1`
3. `nike-cortez`
4. `aime-leon-dore`
5. `pop-mart` / `labubu` — validar se entra como collectibles/editorial ou se precisa tratamento separado

Excluídos do primeiro lote por serem buckets genéricos:

- `camiseta-1`
- `moletom-1`
- outros tipos amplos sem ângulo editorial claro

### Fase 2 — Linkar coleções aos guias

Para guias já existentes ou recém-criados:

- garantir CTA coleção → guia;
- garantir CTA guia → coleção;
- remover FAQ duplicado;
- manter `FAQPage` único;
- validar preview desktop e mobile.

### Fase 3 — Padronizar visual das coleções pelo contrato 204L

Aplicar o padrão 204L às outras coleções, não à própria 204L.

Coleções com guia existente/parcial para validar e padronizar:

- `air-jordan`
- `air-jordan-1`
- `air-jordan-4`
- `nike-dunk`
- `onitsuka-tiger-x-astroboy`
- `pace`
- `saint-studio`
- `jacquemus`
- `kith`
- `supreme`
- `athleisure`
- `alo-yoga-1`
- `lululemon`
- `jason-markk`

## Regra operacional

- 204L = referência, não tarefa.
- Moon Shoe/Jacquemus = referência de guia standalone.
- Dev theme primeiro.
- Production apenas após aprovação explícita.
