# Handoff Growth -> Shopify: Otimização de LCP (PageSpeed)

**Data:** 2026-06-30
**Origem:** [LK] Growth OS (Hermes Specialist)
**Destino:** [LK] Shopify Técnico
**Status:** READY / PENDENTE EXECUÇÃO

## Objetivo
Implementar a tag `fetchpriority="high"` e o atributo `preload: true` nas imagens principais (Above the fold) para reduzir o LCP em mobile e blindar o ranking orgânico da LK Sneakers.

## Ações Necessárias
1. **PDP (Páginas de Produto):** No snippet de imagem principal (ex: `product-media.liquid`), adicionar `fetchpriority: 'high', preload: true` ao filtro `image_tag`.
2. **Home:** Na primeira imagem do slideshow/banner principal, realizar a mesma implementação de prioridade.

## Justificativa
Aprovado por Lucas Cimino após auditoria de Core Web Vitals. Redução estimada de ~800ms de atraso no carregamento visual.

## Contexto de Segurança
A alteração deve ser feita primeiro em um tema de desenvolvimento (preview) e validada via Lighthouse antes de subir para o tema principal.

---
*Este documento serve como Card de Tarefa rastreável para o ecossistema Hermes.*
