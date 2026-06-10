# LKGOC Golden Source — Guia LK em `/pages` — New Balance 204L

Status: GOLDEN SOURCE CANDIDATE / OPERACIONAL  
Owner: `[LK] Otimização de Coleções`  
Data: 2026-06-09

## URL de referência

`https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk`

## Decisão

Esta página deve ser corrigida e elevada a **Golden Source do Guia LK em `/pages`**. Ela será a referência para novos Guias LK editoriais ligados às collections LKGOC.

## Papel no sistema

- Collection LKGOC: vitrine comercial e conversão.
- Guia LK em `/pages`: conteúdo editorial, SEO, GEO/AI Search, FAQ, comparação, prova de curadoria e retorno comercial para a collection.

## Componentes obrigatórios do Guia Golden

1. Hero editorial premium:
   - eyebrow `Guia LK`;
   - H1 único;
   - intro curta com intenção comercial;
   - CTA primário para collection;
   - CTA secundário para FAQ/comparação;
   - imagem editorial/lifestyle validada no media manifest.

2. Bloco `O que é`:
   - definição objetiva;
   - leitura cultural/comercial;
   - sem claims inventados.

3. Bloco citável LK:
   - resposta curta, factual e citável por IA/AI Overviews.

4. Comparação/tabela:
   - colorways, modelos ou variações;
   - leitura visual;
   - indicado para quem.

5. Styling/uso:
   - cards curtos, premium e aplicáveis.

6. Sinais editoriais:
   - fontes externas confiáveis quando disponíveis;
   - não usar como claim sem evidência.

7. Compra orientada:
   - autenticidade;
   - curadoria LK;
   - atendimento humano;
   - link claro para collection.

8. FAQ:
   - perguntas reais de busca/cliente;
   - respostas curtas;
   - FAQPage schema válido.

9. SEO/GEO:
   - title/meta humanos;
   - canonical correto;
   - H1 único;
   - headings limpos;
   - FAQPage schema;
   - WebPage/Breadcrumb schema recomendado;
   - bloco citável e entidades claras.

## Correções identificadas na URL atual

Verificação read-only em 2026-06-09:

- PASS: URL pública existe em `/pages`.
- PASS: usa `template_suffix = nb204l-guide`.
- PASS: H1 único.
- PASS: seção `lk-goc-guide` renderiza.
- PASS: há FAQPage schema.
- PASS: há CTA para `/collections/new-balance-204l`.
- ATENÇÃO: `og:image` atual cai no logo LK, não na imagem editorial do guia.
- ATENÇÃO: não foi encontrado WebPage/Article schema específico além de Organization e FAQPage.
- ATENÇÃO: `body_html` da Shopify Page ainda contém HTML/CSS legado do guia; o padrão Golden deve preferir conteúdo controlado por template/section/settings, não body inline.

## Regra de replicação

Para novos guias:

- criar `templates/page.guia-[colecao]-lkgoc.json` usando `sections/lk-goc-guide-v1.liquid` ou sucessor;
- preencher settings/blocos no template ou, idealmente, via metaobjects/metafields;
- não colar HTML longo no body da Page como padrão;
- manter body da Page mínimo/neutro quando o conteúdo vier do template;
- criar page handle em `/pages/guia-[colecao]` ou slug aprovado;
- linkar collection ↔ guia;
- QA desktop/mobile + schema + SEO before approval.

## Production guardrail

A página atual está em Production. Qualquer correção customer-facing exige aprovação explícita atual de Lucas.
