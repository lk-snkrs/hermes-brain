# Auditoria — Adidas Sambae DEV não está em paridade 204L

Data: 2026-06-02
Tema DEV: 155065450718
Escopo: read-only/local; sem write em produção.

## Evidências verificadas

- Asset section candidato: `receipts/dev/sambae-from-zero-clean-204l-dev-20260602T222505Z/section.after.liquid`
- Snippets candidatos:
  - `snippet.hero.liquid`
  - `snippet.guide.liquid`
- QA anterior:
  - `QA.asset.json`: render count no asset = 1 hero / 1 guide
  - `QA.render.json`: URL normal/sections = 0 hero / 0 guide; cookie-preview = markers presentes

## Causa raiz

1. O QA que passou era principalmente de asset/readback, não de render real estável para o link compartilhável.
   - `QA.asset.json`: hero_render_count=1 e guide_render_count=1 só provam que o Liquid contém os renders.
   - `QA.render.json`: sem cookie de preview, `/collections/adidas-sambae?preview_theme_id=155065450718` retornou hero=0 e guide=0.
   - Com cookie de preview Shopify, os marcadores aparecem. Portanto parte da confusão vem de preview/cookie/cache, não de produção.

2. A implementação não copiou literalmente o padrão 204L; criou snippets novos e só reutilizou classes 204L.
   - Hero Sambae usa `.lk-204l-*`, mas é um snippet próprio: `lk-sambae-204l-hero`.
   - Guia Sambae usa `#lk-guia-adidas-sambae`, mas o CSS fino do 204L está preso ao ID `#lk-guia-new-balance-204l`.
   - Resultado: o guia não herda a mesma geometria/typografia/microspacing do 204L.

3. A section continua com muito legado de `adidas-samba-jane` e regras específicas antigas.
   - No asset candidato: `adidas-samba-jane` aparece 38 vezes; `adidas-sambae` aparece só nos dois renders.
   - Isso aumenta colisão de CSS/branch e não é uma cópia limpa do contrato 204L.

4. A lógica de interação do hero Sambae diverge da 204L.
   - 204L: botão “Ler mais” abre o bloco/reveal padrão (`root.is-open` + collage).
   - Sambae: botão expande apenas a cópia; o collage só alterna clicando na imagem principal.
   - Visualmente isso “parece outro componente”.

## Diagnóstico curto

O problema não é falta de produto nem handle: o handle correto é `adidas-sambae` e os renders estão no asset candidato. O problema é execução de paridade: foi feito um wrapper/snippet novo com classes parecidas, mas sem transplantar o contrato completo do 204L e sem QA final em render acessível ao usuário sem cookie de preview.

## Correção recomendada

- Rebuild DEV de Sambae como clone literal do branch 204L:
  - duplicar o bloco `new-balance-204l` e trocar somente copy/imagens/labels/handle;
  - duplicar o guia pós-grid 204L e trocar somente ID/copy/FAQ/page URL;
  - copiar também CSS ID-specific de `#lk-guia-new-balance-204l` para `#lk-guia-adidas-sambae`;
  - remover/desativar o snippet híbrido atual para evitar cascata ambígua;
  - QA obrigatório: asset + sections API + full page com cookie + screenshot desktop/mobile + comparação de classes/marcadores.

## Aprovação

Pode corrigir em DEV sem tocar produção. Publicar em produção exige aprovação explícita do Lucas.
