# Product Upload Global Routing — 2026-06-15

## Decisão Lucas

Subir/listar produto novo no site da LK não é uma regra exclusiva do LC WhatsApp nem do comando `!subir`. É uma regra operacional global para todos os agentes da LK.

Se qualquer agente estiver em conversa de conteúdo, anúncios, SEO, campanha, sourcing, coleções, atendimento, estoque ou operações e perceber que um produto precisa existir no site, deve acionar/handoff para `[LK] Shopify` (`lk-shopify`) com a skill `lk-shopify-product-upload`.

## Dono

- Dono final: `[LK] Shopify` / `lk-shopify`.
- Skill: `lk-shopify-product-upload`.
- Apoio: `lk-growth`/Claude SEO para descrição, SEO, entidade e GMC quando necessário.
- Apoio: `lk-stock` somente quando houver estoque real/pronta-entrega/disponibilidade/Tiny.

## Contrato de handoff

O agente de origem deve enviar para `lk-shopify`:

- motivo da criação/listagem;
- contexto de conteúdo/anúncio/SEO/campanha/sourcing;
- referência GOAT, SKU, URL, modelo ou imagem;
- preço e tamanhos, se Lucas já informou;
- urgência;
- restrições e dúvidas.

O `lk-shopify` deve devolver draft/preview com:

- produto encontrado na GOAT/KicksDB/StockX quando aplicável;
- imagens GOAT na ordem correta, filtrando sufixos legados `_02`, `_05`, `_07`, `_10`, `_11`;
- título padronizado LK;
- descrição premium com Brain/Claude SEO quando necessário;
- tag `encomenda`;
- variantes/tamanhos confirmados;
- campos GMC/categoria/fabricante/marca;
- link draft/admin preview para Lucas aprovar;
- readback/evidência.

## Guardrail

Não publicar ativo, alterar Tiny/estoque, enviar anúncio/campanha, contactar fornecedor ou fazer outro write externo sem aprovação explícita de Lucas.
