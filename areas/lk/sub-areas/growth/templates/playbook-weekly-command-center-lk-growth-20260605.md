# Playbook — LK Growth Weekly Command Center

Data: 2026-06-05
Status: template operacional local/read-only.

## Quando usar

Use para revisão semanal ou sob demanda de Growth: GA4, GSC, GMC, Shopify read-only, SERP/DataForSEO, PageSpeed/CrUX, reviews, paid/influencer signals e performance.

## Workers mínimos possíveis

- Growth Planner
- Growth Data Scout
- SEO/GEO Analyst, se houver busca/IA/conteúdo
- CRO/PDP Analyst, se houver conversão/PDP/coleção
- GMC/Product Data Analyst, se houver Merchant/feed/produto
- Growth Governor/Critic

Selecionar apenas os necessários.

## Fluxo

1. **Objetivo e janela**
   - Período analisado:
   - Escopo: site/PDP/coleção/GMC/GEO/CRO:
   - Pergunta principal de negócio:

2. **Fonte e status**
   - GA4/Shopify conversão/receita:
   - GSC demanda/CTR/posição:
   - GMC issues:
   - SERP/DataForSEO:
   - PageSpeed/CrUX:
   - Gaps declarados:

3. **Fila 0–100**
   - Impacto comercial /25
   - Evidência/demanda /20
   - Confiança /15
   - Esforço invertido /10
   - Risco invertido /10
   - Rollback/readback /10
   - Aderência canônica /10

4. **Top 3–5 ações**
   - Oportunidade:
   - Evidência:
   - Score:
   - Próximo output: diagnóstico / packet / handoff / bloqueio:
   - Aprovação exigida?:

5. **Governor**
   - Bloquear se não decision-grade.
   - Rebaixar se falta GA4/GSC/Shopify/GMC quando a recomendação depende disso.
   - Separar evidência, hipótese, opinião e decisão.

## Saída para Lucas

Telegram curto:

- Veredito:
- Top 3:
- O que posso preparar sem aprovação:
- O que exige aprovação:
- O que está bloqueado por falta de dado:

## Bloqueios

- Não executar writes.
- Não enviar relatório longo no Telegram.
- Não usar stock/Tiny como critério decisivo de SEO/CRO.
