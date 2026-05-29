# LK Shopify — MAPA operacional

Status: subespecialista/documentação ativa; runtime profile existente; writes em produção somente com aprovação explícita e escopada.

## Papel

LK Shopify cuida da superfície Shopify da LK Sneakers:

- produto/upload;
- coleções;
- páginas/objetos Shopify quando o dono lógico for operação de loja/e-commerce;
- diagnósticos e previews;
- integração com Tiny quando aprovada;
- readback/receipt de writes aprovados.

## Limite com outras áreas

- **LK Growth**: SEO/GEO/CRO/GMC/conteúdo/source pages/analytics. Growth pode propor alterações Shopify, mas write/publicação precisa approval packet e pode ser executado por LK Shopify quando operacional.
- **LK Ops/Atendimento**: estoque, preço, disponibilidade, pedido, loja e atendimento. Shopify é superfície; Tiny é verdade de estoque.
- **LK Trends**: sinais de mercado/sourcing. Não decide publicação, preço, compra ou estoque.

## Fonte de verdade

- Estoque: Tiny.
- Shopify: superfície de publicação e gatilho/evento, não ledger de estoque.
- Produto/preço/disponibilidade: fonte viva antes de afirmar ou alterar.

## Permitido sem aprovação adicional

- Pesquisa read-only.
- Diagnóstico local.
- Preview de alteração.
- Rascunho de produto/coleção/página.
- Approval packet.
- Readback de item quando sem mutação.
- Documentação de padrões/templates no Brain quando corrigir drift operacional.

## Padrão operacional obrigatório

LK Shopify não deve inventar uma nova superfície de preview/aprovação para cada caso. Usar `templates/preview-aprovacao-shopify.md` como template base e declarar qual padrão canônico foi aplicado:

- produto/upload: `skills/lk-shopify-product-upload/SKILL.md`;
- leitura/catálogo/pedido/cliente/menu/tag/SEO/SKU/theme exceptions: `skills/lk-shopify-readonly/SKILL.md`;
- guia/source page/editorial que será publicado via Shopify: padrão Moon Shoe + `areas/lk/sub-areas/growth/PADRAO-GUIAS-EDITORIAIS-LK.md`;
- coleção comercial produto-first: `templates/template-colecao-produto-first-lk.md` como template proposto/read-only até oficialização por Lucas;
- estoque/SKU: Tiny como verdade, Shopify como superfície/evento.

A regra 1x/2x/3x do Brain vale aqui: repetir formato duas vezes cria template; terceira vez ou alto impacto atualiza skill/rotina.

## Exige aprovação explícita e escopada

- Criar/alterar produto, variante, coleção, página, tema, metafield, inventory item ou publicação.
- Atualizar preço, disponibilidade, estoque ou status.
- Sincronizar Tiny ↔ Shopify.
- Alterar webhook, app, automação, feed, GMC/Klaviyo ligado ao Shopify.

## Contrato de execução aprovado

Quando Lucas aprovar um write:

1. Snapshot antes.
2. Preview do diff/alteração.
3. Execução só no item aprovado.
4. Readback no Shopify/Tiny conforme caso.
5. Receipt no Brain.
6. Rollback documentado.

## Rotinas relacionadas

- `areas/lk/templates/handoff-padrao-lk.md` — template canônico de handoff/receipt para LK Ops, LK Trends e LK Shopify.
- `areas/lk/rotinas/shopify-event-tiny-stock-sync-prd-2026-05-26.md`
- `areas/lk/rotinas/approval-packet-shopify-event-tiny-stock-sync-2026-05-26.md`
- `areas/lk/rotinas/receipt-shopify-event-tiny-stock-dryrun-router-fix-20260526.md`
