# LK Growth Audit — Onitsuka Tiger Mexico 66 FAQ / Schema / GEO

Data: 2026-05-28
URL auditada: https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66
Framework: claude-seo local skills (`seo`, `seo-schema`, `seo-geo`) + LK collection patterns

## Resumo executivo

A página já tem FAQPage JSON-LD para o FAQ integrado dentro do Guia LK. Porém, há um problema de governança: existem dois blocos FAQPage JSON-LD na mesma página e ainda existe o bloco legado `.coll-faq` no HTML/render desktop. Isso cria duplicidade visual/semântica e pode confundir Google/LLMs.

## Evidências live

Fonte pública SSR retornou HTTP 200 e HTML inicial com 1.272.018 caracteres.

Meta:
- Title: Onitsuka Tiger Mexico 66 Original na LK Sneakers
- Meta description: Compre Onitsuka Tiger Mexico 66 original na LK Sneakers. Alta procura, curadoria premium, autenticidade garantida e opções em até 10x.
- Canonical: https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66

JSON-LD detectado:
1. Organization / ShoeStore / ClothingStore
2. BreadcrumbList
3. CollectionPage
4. FAQPage — 5 perguntas do FAQ integrado ao Guia LK
5. FAQPage — 4 perguntas do FAQ legado `.coll-faq`

FAQ integrado ao Guia LK:
- Quanto custa um Onitsuka Tiger no Brasil?
- Qual a diferença entre ASICS e Onitsuka Tiger?
- O Onitsuka Tiger Mexico 66 é da ASICS?
- Como escolher entre Mexico 66, SD, Sabot e Slip-on?
- O Mexico 66 tem a forma grande ou pequena?

FAQ legado ainda presente:
- Por que o Onitsuka Tiger Mexico 66 é tão procurado?
- Qual Mexico 66 escolher: couro, camurça, SD ou Sabot?
- O Onitsuka Tiger Mexico 66 tem a forma grande ou pequena?
- O Mexico 66 da LK Sneakers é original?

Robots/AI access:
- Googlebot permitido para `/collections/`
- GPTBot permitido
- ChatGPT-User permitido
- OAI-SearchBot permitido
- ClaudeBot permitido
- PerplexityBot permitido

llms.txt:
- Existe no root.
- Hoje funciona mais como instrução UCP/Shopify/agent-commerce.
- Linka para `/tools/seo/llms.txt` e `/tools/seo/llms-full.txt`, mas a página Onitsuka não foi revalidada nesses arquivos durante este audit.

## Diagnóstico

### O que está certo
- FAQ dentro do Guia LK está com JSON-LD FAQPage correspondente.
- O conteúdo é SSR no HTML inicial, bom para Google e crawlers AI que não executam JS.
- A página tem CollectionPage, BreadcrumbList e Organization/ShoeStore/ClothingStore.
- Robots permite os principais bots de busca e AI search.
- Title/meta/canonical estão adequados para intenção transacional.

### O que está errado ou subótimo
- Existem dois FAQPage JSON-LD na mesma URL.
- O `.coll-faq` legado ainda está presente no HTML e visível no desktop; no mobile foi ocultado por CSS, mas o JSON-LD legado continua no HTML.
- O H2 “Perguntas Frequentes” aparece duas vezes na hierarquia renderizada.
- Para Google, FAQ rich result comercial é restrito e não deve ser vendido como ganho de rich snippet; o valor aqui é mais estrutura/entidade/GEO do que resultado rico.
- Para GEO/AI, duplicidade de perguntas pode reduzir clareza de fonte, especialmente quando duas FAQs respondem temas semelhantes com wording diferente.

## Recomendação

Prioridade alta, baixo risco:
- Consolidar em uma única FAQ canônica: a FAQ integrada dentro do Guia LK.
- Remover/desabilitar o bloco `.coll-faq` legado para Onitsuka em desktop e mobile.
- Remover o segundo FAQPage JSON-LD legado da coleção Onitsuka.
- Manter apenas um FAQPage JSON-LD com as perguntas visíveis dentro do Guia LK.
- Opcional: incluir no FAQ integrado uma pergunta de autenticidade se for comercialmente desejável, porque hoje ela existe no legado mas não no Guia LK.

## Aprovação necessária

A correção mexe em produção/tema visível e em schema público. Precisa de aprovação explícita de Lucas antes de executar.

## Rollback esperado se aprovado

- Backup dos assets alterados em `receipts/theme-prod/`.
- Patch escopado para handle `onitsuka-tiger-mexico-66`.
- Readback Admin + validação storefront:
  - JSON-LD FAQPage count = 1
  - `.coll-faq` count/visible = 0 para essa coleção
  - perguntas do JSON-LD = perguntas visíveis no Guia LK
  - desktop e mobile sem FAQ duplicado
