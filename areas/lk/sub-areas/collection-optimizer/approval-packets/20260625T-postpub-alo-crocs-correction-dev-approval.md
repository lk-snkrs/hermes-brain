# Approval packet — Correção DEV LKGOC Lite Alo Yoga + Crocs McQueen

Data: 2026-06-25  
Origem: QA pós-publicação `qa/20260625T-postpub-alo-crocs-qa/QA-REPORT.md`  
Writes externos nesta preparação: 0

## Decisão solicitada

Autorizar **preparar em DEV/branch** uma correção LKGOC Lite para Alo Yoga e Crocs McQueen, sem tocar Production/main, para resolver os achados do QA pós-publicação.

## Escopo proposto

### Alo Yoga

Objetivo: reduzir duplicidade/overlap editorial.

- Consolidar em um único bloco pós-grid:
  - resumo editorial;
  - “Como escolher”;
  - FAQ única;
  - bloco citável LK;
  - `FAQPage` único.
- Manter tom premium/wellness/curadoria humana.
- Remover repetição entre “Como escolher Alo Yoga” e “Como escolher peças Alo Yoga”.

### Crocs McQueen

Objetivo: garantir que o conteúdo pareça efetivamente pós-grid e não pré-grid.

- Validar visualmente o rótulo `Guia editorial LK`.
- Se o rótulo aparecer antes do produto/grid, ajustar no DEV para que o bloco inteiro fique pós-grid.
- Manter FAQ e bloco citável enxutos.
- Não prometer estoque, pronta entrega, prazo, tamanho disponível ou preço.

## Fora do escopo

- Preço, estoque, variante, ordem de produto, campanha, GMC, Klaviyo, checkout.
- Novo layout visual ou design system.
- Production/main.
- Shopify Admin write direto como default; seguir GitHub/DEV/branch quando aplicável.

## Impacto esperado

- Menos ruído editorial em Alo Yoga.
- Melhor aderência ao padrão Lite e Gold Source 204L.
- Menor risco de IA/Google interpretar blocos repetidos como baixa qualidade.
- Menor risco visual de Crocs parecer guia antes do grid.

## Risco

Baixo/médio em DEV. Risco principal é mexer em conteúdo que já está público e voltar a ter cache/propagação se promovido. Por isso a correção deve ser preparada e validada antes de qualquer production.

## QA obrigatório antes de production

- Screenshot mobile/desktop das duas coleções.
- Readback público/preview.
- Contagem: H1 único, FAQPage único, bloco citável único, sem Liquid error.
- Comparação com 204L como padrão de hierarquia.
- Checagem de texto: sem estoque/pronta entrega/prazo/tamanho disponível como promessa pública.

## Rollback

Usar backups do production receipt de 2026-06-23 e snapshots novos antes de qualquer promoção.

## Frase de aprovação para Lucas

> Aprovo preparar em DEV/branch a correção LKGOC Lite de Alo Yoga e Crocs McQueen, limitada a consolidar o bloco editorial/FAQ de Alo Yoga e ajustar o posicionamento/ruído visual do Guia em Crocs McQueen, sem write em Production/main, sem preço, estoque, produtos, ordem, GMC, Klaviyo ou campanhas, com QA mobile/desktop, readback e rollback antes de qualquer promoção.
