# Frente — Product FAQ/GEO Top 50 LK

Criado em: 2026-06-16T16:32:41.525111+00:00
Área: LK / Growth
Status: proposta aprovada conceitualmente pelo Lucas via voz; sem autorização de writes em produção ainda.

## Objetivo
Melhorar captura orgânica, AI Overviews/GEO e conversão dos 50 produtos mais relevantes da LK por venda/demanda, atualizando descrição e FAQ com intenção real de compra/search.

## Princípio central
Não produzir FAQ genérico. Cada pergunta precisa passar pelo FAQ Real Intent Gate:
- evidência de GSC/SERP/PAA/PAS/DataForSEO;
- objeção real de compra;
- comparação entre modelos/colorways;
- dúvida de tamanho, material, conforto, uso, styling ou autenticidade específica;
- bloco citável para AI Search/GEO;
- sem promessas de estoque/prazo/pronta entrega/encomenda.

## Escopo da frente
1. Selecionar Top 50 produtos por vendas/receita em janela recente.
2. Cruzar com GSC: impressões, cliques, CTR, posição e queries por PDP.
3. Cruzar com SERP/DataForSEO: PAA, snippets, concorrentes e linguagem de busca.
4. Classificar produtos por prioridade:
   - P0: alta venda + alta impressão + CTR baixo;
   - P1: alta venda + produto com busca crescente;
   - P2: produto premium/hero com potencial de AI citation;
   - P3: manutenção editorial.
5. Criar pacote por lote, não 50 writes de uma vez.

## Lotes recomendados
- Lote 1: 10 produtos — maior impacto e menor risco.
- Lote 2: próximos 15 — após medir estabilidade e impacto.
- Lote 3: próximos 25 — escala com padrão validado.

## Entregáveis por produto
- diagnóstico breve;
- descrição otimizada, mantendo tom LK;
- FAQ com 5–7 perguntas reais;
- bloco citável answer-first para AI Search;
- links internos relevantes;
- campos alterados e campos não alterados;
- rollback;
- plano de medição D7/D14/D28.

## Guardrails
- Sem alteração de preço, estoque, desconto, campanha, GMC/feed, Klaviyo/WhatsApp.
- Sem theme production sem packet separado.
- Sem remover módulos globais sem dev-preview e aprovação.
- Nenhum write em produção sem aprovação explícita por lote.

## Próximo passo read-only
Gerar ranking Top 50 com colunas:
- produto;
- URL/handle;
- receita 90d;
- unidades/pedidos 90d;
- sessões PDP, se disponível;
- CVR PDP, se disponível;
- principais queries GSC;
- impressões/cliques/CTR/posição;
- oportunidade SEO/GEO;
- prioridade P0/P1/P2/P3;
- recomendação de lote.

## Aprovação necessária futura
Aplicar em produção exige aprovação explícita por lote, com payload fechado, rollback/readback e medição.


## Adendo Lucas — usar todo o stack de inteligência
Registrado em: 2026-06-16T16:35:08.960148+00:00

Diretriz do Lucas: usar todas as skills e fontes disponíveis para maximizar inteligência antes de propor conteúdo, FAQ ou CRO.

### Stack obrigatório por lote
- Shopify read-only: ranking de receita, unidades, pedidos, handles, PDPs.
- GA4: sessões PDP, add_to_cart, begin_checkout, purchase/CVR quando disponível.
- GSC: queries por URL, impressões, cliques, CTR, posição e páginas com gap.
- DataForSEO: volume, SERP, PAA/PAS, concorrentes, snippets e intenção.
- Google/SEO skills locais: padrões LK, LKGOC, coleção/PDP, FAQ Real Intent Gate.
- Fetch público: HTML, meta, schema, FAQ visível, duplicidades e conteúdo legado/global.
- PageSpeed/CWV quando alteração visual entrar no escopo.
- Paid/social/influencer como sinal contextual de demanda, não como verdade final.
- Claude/Cloud Code ou ferramenta equivalente: usar como segunda opinião/critic pass para lote, quando disponível, sem writes externos e sem expor secrets.

### Gate visual PDP
Toda alteração visual deve ser diagnosticada separadamente de descrição/FAQ:
- primeiro audit read-only/mobile;
- depois dev-theme/preview;
- só production theme com aprovação explícita, rollback e QA.

### Perguntas visuais por PDP/lote
- O bloco de descrição/FAQ aparece antes ou depois do que deveria no mobile?
- O FAQ ajuda compra ou empurra o CTA para baixo?
- Existem blocos globais redundantes/legados?
- Trust blocks, reviews, tamanho, frete/troca e CTA estão claros sem poluir?
- O produto premium tem storytelling suficiente sem prejudicar velocidade?
- Há risco de LCP/CLS/INP se mexer no layout?


## Adendo — Claude SEO como critic pass obrigatório
Registrado em: 2026-06-16T16:37:27.272066+00:00

Confirmado: há referências locais para uso de Claude SEO/claude-seo no stack LK Growth, incluindo:
- `/opt/data/profiles/lk-growth/skills/productivity/lk-shopify-product-upload/references/claude-seo-upstream-for-lk-products.md`
- `/opt/data/profiles/lk-growth/skills/productivity/lk-seo-weekly-improvement/references/claude-seo-full-connector-validation-20260519.md`
- `/opt/data/profiles/lk-growth/skills/productivity/lk-seo-weekly-improvement/references/full-geo-seo-claude-audit-20260522.md`
- `/opt/data/profiles/lk-growth/skills/productivity/lk-seo-weekly-improvement/references/claude-seo-google-connectors-readiness-20260519.md`

Uso obrigatório na frente Top 50:
1. gerar draft inicial com dados Shopify/GSC/GA4/DataForSEO/SERP/fetch público;
2. passar por critic pass Claude SEO/skill equivalente para detectar:
   - FAQ genérico;
   - pergunta sem intenção real;
   - excesso de texto que prejudique conversão;
   - lacuna de comparação/modelo/material/calce/styling;
   - risco de duplicidade com FAQ global;
   - oportunidade de bloco citável GEO/AI Overview;
3. só depois montar approval packet de lote.

Claude SEO não autoriza write. É etapa de inteligência/revisão. Writes continuam exigindo aprovação explícita do Lucas por lote.
