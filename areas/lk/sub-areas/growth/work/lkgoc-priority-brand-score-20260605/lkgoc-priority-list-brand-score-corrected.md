# LKGOC — priorização corrigida por score de marcas/modelos

Gerado: 2026-06-05T19:54:22.816558+00:00

## Fontes consultadas

- Brain LK Growth: Brand Mix Intelligence e source hierarchy (`lk-os-prd-decisions-20260509.md`, `lk-growth-source-priority-20260603.md`).
- Shopify Admin read-only: pedidos/line items 30d e 90d, sem PII.
- DataForSEO: volume/intenção Brasil para modelos candidatos.
- Storefront público: existência de collection/handle e presença de LKGOC renderizado.

## Correção de lógica

A lista anterior foi errada porque partiu de volume SEO genérico e não do score LK.
Para LKGOC, prioridade deve começar por:

1. score de marca por venda real Shopify;
2. score de modelo/família dentro da marca;
3. fit premium/curadoria LK;
4. demanda Google/DataForSEO como complemento;
5. readiness da coleção existente;
6. lacuna LKGOC atual.

## Score de marcas — Shopify 90d

- Nike: R$ 1.579.985 / 365 un. / 290 pedidos — #1.
- Onitsuka Tiger: R$ 814.397 / 314 un. / 259 pedidos — #2.
- New Balance: R$ 752.996 / 293 un. / 246 pedidos — #3.
- Adidas: R$ 192.078 / 95 un. / 85 pedidos — distante das três líderes.
- Puma/Asics: baixo sinal interno no período; não priorizar como LKGOC Full agora.

## Score de modelos — Shopify 90d

- Nike Moon Shoe / Jacquemus: R$ 890.998 / 164 un. / 147 pedidos.
- Onitsuka Mexico 66: R$ 633.297 / 262 un. / 219 pedidos — já otimizada no pacote atual.
- New Balance 9060: R$ 340.399 / 135 un. / 110 pedidos — já otimizada.
- New Balance 204L: R$ 317.999 / 112 un. / 98 pedidos — já otimizada/gold source.
- Nike Mind: R$ 239.199 / 72 un. / 52 pedidos.
- Nike Vomero Premium: R$ 183.500 / 42 un. / 31 pedidos.
- Air Jordan 1: R$ 140.579 / 39 un. / 31 pedidos.
- Adidas Samba: R$ 66.500 / 33 un. / 31 pedidos — já otimizada família principal.
- New Balance 530: R$ 62.000 / 33 un. / 31 pedidos — já otimizada.
- Adidas SL 72: R$ 27.600 / 17 un. / 16 pedidos.

## DataForSEO — sinais complementares

- Nike Vomero Premium: 22.200 buscas/mês, transacional, tendência anual forte.
- Nike Mind 001: 18.100 buscas/mês, transacional.
- Adidas SL 72: 22.200 buscas/mês, transacional, mas Adidas tem score de marca menor no Shopify.
- Adidas Tokyo: 9.900 buscas/mês, intenção navegacional; não entra antes de Nike.
- Adidas Samba Jane: 2.400 buscas/mês, transacional e tendência forte; candidata de correção/reforço, não nova prioridade maior.
- Nike Moon Shoe: volume explícito baixo, mas é o maior modelo real da LK em receita/unidades — prioridade vem de Shopify, não de volume genérico.

## Ordem corrigida de prioridade LKGOC

### P0 — fazer agora

1. `nike-x-jacquemus-moon-shoe-sp` — Full/refactor LKGOC
   - Maior receita e unidades entre modelos mapeados.
   - Marca #1 no score LK.
   - Collection existe e ainda não renderiza LKGOC de coleção.
   - Fit máximo: collab, premium, fashion, alta margem percebida, forte storytelling.

2. `nike-mind-001` + avaliar criação/agrupamento `nike-mind`
   - Nike continua #1.
   - Modelo/família com 72 unidades em 90d e R$ 239k.
   - Demanda DataForSEO alta para Nike Mind 001/002.
   - Recomendação: auditar se vale collection guarda-chuva `nike-mind` ou otimizar `nike-mind-001` com links para 002/slide.

3. `nike-vomero-premium`
   - 42 unidades / R$ 183k em 90d.
   - Demanda Google forte e transacional.
   - Bom potencial de guia: corrida premium, design exagerado, trend performance/lifestyle.

### P1 — próxima leva

4. `air-jordan-1`
   - Bom faturamento, marca Nike/Jordan, collection existe.
   - Conteúdo precisa ser muito bom para competir; não é tão urgente quanto Moon Shoe/Mind/Vomero.

5. `adidas-sl-72`
   - Bom volume Google, mas score interno menor.
   - Entraria depois da sequência Nike porque Adidas está muito abaixo em venda real.

6. `adidas-samba-jane` / `adidas-sambae` — correção/reforço, não prioridade nova
   - Já têm histórico LKGOC parcial/legado.
   - Fazer como correção de consistência, schema/FAQ/guia e possível migração para componente único, não como próxima coleção principal.

### P2 — segurar por enquanto

7. `adidas-tokyo`
   - Busca existe, mas intenção navegacional e venda interna menor.

8. `adidas-ballerina-bad-bunny`
   - Baixa unidade; pode ser micro landing se campanha/influencer empurrar.

9. `puma-speedcat` e `asics-gel-kayano-14`
   - Não priorizar agora: sinal interno baixo no Shopify, apesar de tendência externa.

## Decisão operacional recomendada

Próximo pacote DEV: `nike-x-jacquemus-moon-shoe-sp`.
Depois: `nike-mind-001`/`nike-mind` conforme auditoria de handle/produtos.
Depois: `nike-vomero-premium`.

## Arquivos de dados

- `shopify-brand-score-readonly.json`
- `model-family-score-readonly.json`
