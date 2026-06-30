# Handoff Growth -> Shopify: Ajuste de Schema.org (Rich Snippets)

**Data:** 2026-06-30
**Origem:** [LK] Growth OS (Hermes Specialist)
**Destino:** [LK] Shopify Técnico
**Status:** READY / PENDENTE EXECUÇÃO

## Objetivo
Corrigir a falha de sincronização onde o SKU no Liquid Schema está retornando `null`, impedindo a exibição de estrelas e preço real nos Rich Snippets do Google. Superar o visual dos concorrentes (Juicy Sneakers) na SERP.

## Ações Necessárias
1. **Mapeamento de SKU:** No arquivo de Schema do produto (geralmente `snippets/seo-schema.liquid` ou similar), substituir a lógica do campo `sku` para ler o `current_variant.sku` de forma dinâmica.
2. **Review Integration:** Garantir que o objeto `aggregateRating` do Judge.me esteja corretamente aninhado dentro do objeto `@type: Product`. Atualmente o Schema de Organization está correto, mas o de Produto individual carece do Rating dinâmico.

## Justificativa Growth
Aumento direto de CTR (Taxa de Clique) através de resultados visualmente mais premium e confiáveis no Google Search.

---
*Este documento serve como Card de Tarefa rastreável para o ecossistema Hermes.*
