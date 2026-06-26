# LK Shopify — propagação de Golden Patterns

Data: 2026-05-27 01:23 UTC  
Pedido: Lucas apontou que LK Shopify faltou na propagação da lógica de organograma/Amora/Golden Patterns e aprovou seguir.

## Escopo executado

Sem tocar Shopify/Tiny real, produção, runtime, gateway, token ou cron.

Foram atualizados documentos locais do Brain e skills para deixar LK Shopify explícito na lógica:

- `areas/lk/sub-areas/shopify/AGENTS.md`
- `areas/lk/sub-areas/shopify/MAPA.md`
- `areas/lk/sub-areas/shopify/templates/preview-aprovacao-shopify.md`
- `areas/lk/MAPA.md`
- `AGENTS.md`
- `empresa/contexto/organograma-agentes-hermes.md`
- `empresa/contexto/matriz-roteamento-tarefas-hermes.md`
- `empresa/contexto/task-router-hermes.md`
- `skills/lk-shopify-readonly/SKILL.md`
- `skills/lk-shopify-product-upload/SKILL.md`
- runtime skills `lk-shopify-readonly` e `lk-shopify-product-upload` via skill_manage

## Decisão aplicada

LK Shopify agora tem rota explícita `lk-shopify-surface` e template obrigatório para preview/aprovação.

A regra é:

- LK Growth define/mede SEO/GEO/CRO/conteúdo.
- LK Shopify executa/previewa superfície Shopify quando for produto, coleção, página, menu, tag, SEO field, theme/dev theme, readback/receipt.
- LK Ops/Tiny continuam fonte de verdade para estoque/preço/disponibilidade.
- LK Trends informa oportunidade, mas não aprova publicação/compra.

## Golden Pattern aplicado

LK Shopify deve reutilizar padrões aprovados:

- produto/upload: `lk-shopify-product-upload`;
- leitura/catálogo/pedido/cliente/menu/tag/SEO/SKU/theme: `lk-shopify-readonly`;
- guia/source page/editorial publicado via Shopify: padrão Moon Shoe do LK Growth;
- estoque/SKU: Tiny como verdade, Shopify como superfície/evento.

## Guardrails preservados

- Nenhum write em Shopify/Tiny foi executado.
- Nenhum deploy/theme publish foi executado.
- Nenhum contato externo/campanha/envio foi feito.
- Aprovação genérica para documentação não vira aprovação permanente de produção.
- Writes futuros seguem snapshot → preview → aprovação escopada → execução → readback → receipt → rollback.

## Verificação mínima

- Arquivos escritos/patchados localmente.
- Próximo passo recomendado: rodar Brain health/diff check para validar docs após o conjunto de mudanças de governança em andamento.
