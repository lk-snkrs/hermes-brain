# LK — SEO/CRO Weekly Improvement Loop

Status: operacionalizado como processo read-only + cron semanal; writes externos continuam bloqueados até aprovação explícita do Lucas.

## Objetivo

Criar um módulo semanal de SEO/CRO para a LK Sneakers que use a família **Claude SEO** (`AgriciDaniel/claude-seo`, instalada no Hermes como `seo-audit`, `seo-page`, `seo-content`, `seo-ecommerce`, etc.) para dar nota, comparar evolução e transformar diagnóstico em fila fixa de melhoria de páginas/PDPs.

Este módulo responde à regra do Lucas: SEO não pode ser relatório solto; precisa virar metas e melhorias recorrentes de página.

## Cadência

- Frequência: semanal.
- Janela padrão: segunda-feira de manhã BRT.
- Entrega: resumo no Telegram + artefato detalhado no Brain quando aplicável.
- Modo: read-only por padrão.

## Score semanal

Cada rodada deve gerar uma nota 0–100 com quebra por categoria:

1. Técnica/indexabilidade.
2. On-page: title, meta, H1, headings e URL.
3. Conteúdo: E-E-A-T, helpfulness, clareza e não-genericidade.
4. E-commerce/Product SEO: schema, PDP, Merchant/feed quando disponível.
5. AI Search/GEO: citabilidade, estrutura, entidades.
6. Imagens: alt text, peso e riscos de performance.
7. Search Console: impressões, CTR, posição e oportunidades.
8. Merchant Center/feed: reprovações e qualidade de dados quando disponível.

## Seleção de páginas

Prioridade semanal:

1. PDPs com impressão/tráfego e CTR/conversão fracos.
2. Produtos importantes por venda/estoque/LK OS.
3. Produtos recém-criados pela skill `lk-shopify-product-upload`.
4. Categorias/collections com oportunidade orgânica.
5. Páginas com problema no Merchant Center/feed.

## Saída obrigatória

Cada relatório semanal deve incluir:

- Nota atual: X/100.
- Nota anterior, se existir.
- Meta da próxima semana.
- Top 5 melhorias priorizadas.
- Páginas/PDPs afetadas.
- Impacto esperado.
- Esforço/risco.
- Campo exato a alterar, se houver.
- Status de aprovação: `read_only`, `needs_preview`, `approved`, `rejected`, `done`.

## Guardrails

Livre sem aprovação:

- Auditar site/PDPs publicamente.
- Ler Search Console/Merchant/Shopify em modo read-only.
- Preparar títulos, metas, descrições, schema, alt text e recomendações.
- Criar fila de melhoria.

Requer aprovação explícita do Lucas:

- Alterar título/meta/descrição/alt/schema no Shopify.
- Alterar tema, Liquid, app, collection, página institucional ou feed.
- Publicar conteúdo, campanha ou disparo.
- Rodar automação que escreve externamente.

## Relação com LK OS

Este é o braço operacional da Fase 6 do LK OS: **SEO, Search Console e Merchant Center**. O critério de sucesso é transformar SEO em fila de melhoria de PDP/conteúdo/produto, não apenas entregar auditoria.

## Skill canônica

Usar: `skills/lk-seo-weekly-improvement/SKILL.md`.

Skills relacionadas:

- `seo-audit`
- `seo-page`
- `seo-content`
- `seo-ecommerce`
- `seo-google`
- `seo-schema`
- `seo-geo`
- `lk-shopify-readonly`
- `lk-shopify-product-upload`
