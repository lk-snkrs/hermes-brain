---
name: lk-shopify-product-upload
description: "Use when Lucas asks to subir/cadastrar produto da LK Sneakers no Shopify, especially from GOAT/market trend intake. Creates a safe product upload workflow: GOAT photo/order reference, SKU creation, product data assembly, Google/model history research, SEO/Claude-style description, preview, approval, and Shopify write guardrails."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [lk-sneakers, shopify, product-upload, goat, seo, market-trends, sku]
    related_skills: [lk-shopify-readonly, lk-market-trends, seo-ecommerce, seo-content, seo-page]
---

# LK Shopify Product Upload

## Overview

Use this skill when Lucas asks Hermes to **subir produto no Shopify da LK Sneakers** or when a Market Trends/LC WhatsApp `!subir` item should become a product-registration workflow.

This skill captures Lucas's product upload logic:

1. Use **GOAT** as the product reference whenever applicable because GOAT tends to have the correct product photos and the correct image order.
2. Create the LK product structure carefully: title, vendor/brand, model, colorway, category, SKU/variant sizing, tags, SEO fields, and source references.
3. Research the model history/context on Google/web before writing copy.
4. Draft the description with LK's premium editorial tone and then run a stronger **Claude SEO / SEO-content** pass, using the available specialist skills (`seo-content`, `seo-ecommerce`, `seo-page`, or blog/SEO tools as appropriate). Treat “Claude SEO” as the refinement layer for entity clarity, E-E-A-T, product-page SEO, AI readability and non-generic LK copy.
5. Produce a complete preview for Lucas.
6. Only write to Shopify after explicit approval. Product creation/update is not covered by the read-only Shopify skill.

## When to Use

Use when Lucas says or implies:

- “subir produto no Shopify”
- “cadastrar produto”
- “produto novo LK”
- “usar GOAT para fotos”
- “criar SKU”
- “descrição SEO do produto”
- “pega esse do market trends e sobe”
- LC WhatsApp command/intake: `!subir <produto/modelo/link/print>`

Do not use for:

- order/customer analysis only → use `lk-shopify-readonly`.
- stock truth/availability → Tiny `LK | CONTROLE ESTOQUE` remains the source of truth.
- campaign/email/WhatsApp send → separate approval flow.
- automatic sourcing/purchase → requires preview + Lucas approval.

## Critical Guardrails

Product upload is a Shopify write and therefore requires explicit Lucas approval before execution.

Free without approval:

- Research product/model history.
- Gather candidate references and photos.
- Build SKU plan.
- Draft SEO title/meta/description/tags.
- Create a product-upload preview.
- Prepare rollback/cleanup plan.

Requires explicit Lucas approval:

- Create product in Shopify.
- Upload images to Shopify.
- Create/update variants/SKUs.
- Publish product.
- Change price, stock, collections, tags/metafields, status, SEO fields.
- Any Tiny write, stock movement, supplier contact, campaign, Klaviyo/WhatsApp send.

Before any Shopify write, produce a preview containing every field that will be written and a rollback/cleanup plan.

## Source Hierarchy

### Product reference and photos

1. **GOAT** — preferred reference for sneaker/product photos and image order when the product exists there.
2. Official brand/product page — use for model name, materials, colorway, story and official naming.
3. StockX / Stadium Goods / Flight Club / retailer pages — secondary validation, not the sole source.
4. LK historical Shopify/Tiny entries — use to keep naming, tags, SKU pattern and variants consistent.

### Stock and SKU truth

- Tiny `LK | CONTROLE ESTOQUE` is the stock truth.
- Shopify is catalog/sales truth, not final stock truth.
- If creating SKUs before Tiny exists, mark them as **proposed LK SKU** and do not claim stock truth until Tiny confirms/cadastra.

## Product Upload Workflow

### 1. Intake

Capture:

- product/model name;
- brand;
- colorway;
- gender/line when relevant;
- GOAT URL or search query;
- target sizes;
- price if Lucas supplied it;
- whether this came from Market Trends/`!subir`;
- urgency/reason: trend, sourcing, influencer signal, customer demand, collection gap.

If the input is too thin, continue with best-effort research and mark assumptions instead of asking unless the missing field blocks the task.

### 2. Research and validation

Research web/Google for:

- model history and cultural context;
- release year/season/collaboration;
- official name and colorway;
- materials/silhouette;
- common aliases and spelling;
- marketplace references and demand signals.

Separate facts from interpretation. Do not invent release details.

### 3. GOAT image plan

Use GOAT as the primary visual reference when available.

Capture in preview:

- GOAT product URL;
- expected photo order;
- cover/hero image candidate;
- side/detail/back/sole/order notes;
- any uncertainty such as missing GOAT page, duplicate listing, or colorway mismatch.

Do not scrape/upload images if terms/access are uncertain or if no explicit upload approval exists. For preview, describe image slots and source URLs where safe.

Recommended image order for sneakers:

1. Main lateral/profile image.
2. Alternate angle/medial.
3. Front/top.
4. Heel/back.
5. Sole/outsole.
6. Detail/material/box if useful.

### 4. Naming standard

Use LK style: product-first, brand/model/color/material/color in Portuguese when appropriate.

Recommended pattern:

`Tênis <Brand> <Model> <Collab/Edition> <Colorway> <Cor PT-BR>`

Examples:

- `Tênis Adidas Taekwondo Mei Ballet Preto e Branco`
- `Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo`
- `Tênis Nike Air Jordan 4 Retro Metallic Gold Branco`

Avoid overstuffed titles and avoid invented color translations. Keep exact model/colorway in SEO fields/tags if title needs to stay readable.

### 5. SKU plan

Before writing, build a SKU table by variant/size.

Rules:

- If the item already exists in Tiny, use Tiny `codigo` exactly.
- If it exists in Shopify/Tiny with another variant, follow the established pattern for that product/model.
- If new and no Tiny code exists, propose SKU(s) but label them as proposed, not canonical.
- Always show: product name + SKU + tamanho.
- Never reuse an SKU without checking Shopify/Tiny read-only first.
- Preserve punctuation/spaces exactly once canonicalized by Tiny.

Preview table fields:

- Size/tamanho;
- Proposed or Tiny SKU;
- Source of SKU decision;
- Confidence;
- Notes/risks.

### 6. Description workflow

The description should not be generic. It should combine:

- short model/story context from research;
- materials/silhouette/fit where known;
- why it matters for the LK customer;
- concise premium editorial voice;
- SEO-friendly entity naming without keyword stuffing.

Process:

1. Research the model history on Google/web.
2. Draft a factual base description.
3. Run a **Claude SEO / SEO-content refinement pass** using the available specialist skill (`seo-content`, `seo-ecommerce`, `seo-page`, or equivalent). In Lucas's shorthand, this is the “Claude SEO” step:
   - entity clarity;
   - title/meta description;
   - product schema considerations;
   - Google/AI readability;
   - avoiding duplicate/manufacturer copy.
4. Final copy must sound LK premium, not marketplace spam.

Recommended output blocks:

- Product description HTML/body.
- SEO title.
- Meta description.
- Tags.
- Alt text pattern for images.

### 7. Shopify preview

Before any write, send Lucas a preview with:

- Product title.
- Vendor/brand.
- Product type/category.
- Status: draft or active recommendation.
- Description.
- SEO title/meta.
- Tags/collections proposed.
- Variants: size + SKU + price if known.
- Image source/order plan.
- Source references.
- Risks/uncertainties.
- Exact fields that would be written.
- Rollback/cleanup plan.

Ask for explicit approval before execution. Approval must be scoped, e.g. “aprovo criar como draft com esses campos”.

### 8. Execution after approval

If approved, use Doppler secrets without printing them.

Write sequence should be conservative:

1. Create as `draft` unless Lucas explicitly approves `active`.
2. Upload images in the approved order.
3. Create variants/SKUs exactly as approved.
4. Set SEO fields/tags/metafields/collections only if included in approval.
5. Read back the product and variants from Shopify.
6. Compare live fields to approved preview.
7. Write an audit report with Shopify product ID, handle, variant IDs, SKU list, image count/order, and rollback steps.

Do not touch inventory quantities unless separately approved and reconciled with Tiny.

## `!subir` / Market Trends Integration

`!subir` is an intake trigger, not an execution approval.

If Lucas sends `!subir` via LC WhatsApp or asks to use it for Market Trends:

1. Treat it as a candidate product registration request.
2. Create a Market Trends item with source/context.
3. Run this Shopify product upload workflow up to preview.
4. Do not create/publish/update Shopify until Lucas approves the exact preview.

Recommended mapping:

- `!subir <GOAT URL>` → parse GOAT reference and create upload preview.
- `!subir <model name>` → research GOAT + official/market references, then preview.
- `!subir trend <model>` → include trend evidence and LK commercial rationale.

## Output Format for Lucas

Use Portuguese and be direct.

Recommended preview format:

- Veredito curto.
- Fonte principal: GOAT / oficial / web / LK Shopify / Tiny.
- Produto proposto.
- SKUs/tamanhos.
- Fotos: ordem e origem.
- Descrição final.
- SEO title/meta/tags.
- Riscos/incertezas.
- O que será escrito no Shopify se aprovado.
- O que não será feito.
- Pedido de aprovação.

## Common Pitfalls

1. **Confundir `!subir` com autorização.** `!subir` inicia triagem/preview; não autoriza publicação.
2. **Usar foto fora de ordem.** Para produtos da GOAT, respeitar a lógica de imagem principal + ângulos corretos.
3. **Inventar história do modelo.** Pesquisar e citar fonte/contexto; se não houver fonte confiável, manter texto neutro.
4. **Criar SKU sem checar Tiny/Shopify.** Sempre buscar duplicidade e padrão existente antes.
5. **Publicar ativo por padrão.** Criar como draft salvo aprovação explícita para active.
6. **Tratar Shopify como estoque.** Estoque continua Tiny.
7. **Descrição genérica.** LK precisa texto premium, produto-first, com contexto real e SEO limpo.
8. **Misturar produto com campanha.** Subir produto não autoriza anúncio, Klaviyo, WhatsApp ou fornecedor.

## Verification Checklist

Before saying the product upload is ready:

- [ ] GOAT/reference checked or absence clearly stated.
- [ ] Model history researched; no invented claims.
- [ ] Shopify duplicate check completed.
- [ ] Tiny/SKU duplicate check completed or marked as pending if no access.
- [ ] SKU table includes product + SKU + tamanho.
- [ ] Description passed SEO/content refinement.
- [ ] Image order/source plan is explicit.
- [ ] Preview lists every Shopify field to be written.
- [ ] Lucas gave explicit approval before any write.
- [ ] Post-write Shopify readback verified product/variants/images.
- [ ] Audit/rollback report saved.
