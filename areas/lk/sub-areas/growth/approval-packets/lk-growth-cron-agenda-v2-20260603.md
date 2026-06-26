# Approval Packet — LK Growth OS Cron Agenda v2

Data UTC: 2026-06-03T15:07:51.362342+00:00
Status: **aguardando aprovação do Lucas**
Writes externos: **não**
Alteração em cron real: **não executada ainda**

## Objetivo

Reestruturar a cadência semanal do perfil `lk-growth` para cobrir melhor SEO, GEO/AI Search, CRO, GMC/Product Data, Local Inventory, PageSpeed/CWV, mensuração e impact review, sem invadir o novo agente **[LK] Otimização de Coleção**.

## Decisões de Lucas incorporadas

1. Entrega/ruído:
   - Crons técnicos: avisar no Telegram só quando houver ação, risco ou oportunidade relevante.
   - Segunda-feira: relatório sempre, mesmo sem alerta crítico.
2. Horário:
   - Janela preferida: **08:00–09:00 BRT**.
3. CRO:
   - Prioridade inicial: **PDP mobile**, **checkout/funil**, **collections → PDP**.
   - Depois: reviews/prova social.
4. GEO/AI Search:
   - Rodar junto com SEO na terça.
5. GMC:
   - Cobrir health, product data quality, local inventory, Simprosys e recomendações de supplemental feed.
6. PageSpeed/CWV:
   - Embutir no CRO semanal, não cron separado por enquanto.
7. Priorização do Growth Command Center:
   - Tudo, mas com peso comercial: receita, conversão, demanda, risco e esforço.
8. Entrega:
   - Crons estratégicos: Brain + Telegram + handoff quando necessário.
   - Monitores simples: relatório local + Telegram só se houver alerta.
9. Handoff para novo agente de coleção:
   - LK Growth gera handoff local para **[LK] Otimização de Coleção** e também envia para Lucas aprovar/ver como ficou.

## Agenda semanal proposta

### Segunda — 08:30 BRT

**Cron:** `LK Growth Weekly Command Center`

**Tipo:** estratégico

**Entrega:** Brain + Telegram sempre + handoff se necessário

**Objetivo:** abrir a semana com visão executiva e prioridades.

**Cobre:**
- Shopify/GA4: receita, pedidos, conversão, canais, landing pages e funil.
- GSC: páginas/queries com maior oportunidade.
- GMC: saúde resumida e riscos comerciais.
- CRO: gargalos mobile/PDP/collection/checkout.
- GEO/AI: readiness de páginas citáveis, FAQ/schema, llms/agents quando aplicável.
- PageSpeed/CWV: somente se houver impacto comercial claro.
- Paid/influencer/Klaviyo: sinais de demanda, sem alterar campanhas/envios.
- Top 5 ações da semana por impacto/esforço/risco.

**Regra:** não executar writes. Gerar approval packets e handoffs.

---

### Terça — 08:30 BRT

**Cron:** `LK SEO/GSC + GEO Opportunities Review`

**Tipo:** estratégico/técnico

**Entrega:** Brain + Telegram só se houver oportunidade/risco/decisão

**Objetivo:** transformar demanda orgânica e AI visibility em backlog acionável.

**Cobre:**
- GSC: queries com alta impressão e CTR baixa.
- Páginas posição 4–15.
- Quedas de clique/impressão/posição.
- Titles/metas candidatos.
- SERP/PAA/concorrência.
- Blocos citáveis para AI Search.
- FAQ/schema e legibilidade GEO.
- llms.txt / llms-full.txt / agents.md quando aplicável.

**Output esperado:**
- 3 oportunidades SEO.
- 3 oportunidades GEO.
- Approval packet para writes.
- Handoff para **[LK] Otimização de Coleção** quando envolver coleção/LKGOC.

---

### Quarta — 08:30 BRT

**Cron:** `LK CRO/PDP Funnel Review read-only`

**Tipo:** estratégico/técnico

**Entrega:** Brain + Telegram só se houver gargalo/decisão

**Objetivo:** rotina dedicada de conversão, hoje ausente.

**Prioridade inicial:**
1. PDP mobile.
2. Checkout/funil.
3. Collections → PDP.
4. Depois: reviews/prova social.

**Cobre:**
- PDP mobile: CTA, preço, mídia, trust, WhatsApp, informações críticas.
- Funil: PDP → carrinho → checkout, quando GA4/Shopify permitir.
- Collections: tráfego, cliques para PDP, filtros/ordenação, cards.
- PageSpeed/CWV: embutido no diagnóstico CRO.
- Reviews/prova social: backlog futuro.
- Mensuração: eventos essenciais para confiar nos dados.

**Output esperado:**
- 1 gargalo principal.
- 2–3 testes pequenos.
- Impacto/esforço/risco.
- Rollback e aprovação necessária.
- Handoff se envolver coleção/LKGOC.

---

### Quinta — 08:30 BRT

**Cron:** `LK GMC/Product Data + Local Inventory Review`

**Tipo:** estratégico/técnico

**Entrega:** Brain + Telegram se houver issue/risco/oportunidade; resumo curto se saudável

**Objetivo:** saúde do Merchant, product data e Local Inventory.

**Cobre:**
- GMC issues, warnings e disapprovals.
- Product data quality: GTIN, MPN, brand, condition, imagens, títulos, variantes.
- Divergência Shopify ↔ GMC.
- Simprosys feed contract.
- Local inventory / LIA_ offers.
- Google Business Profile store code.
- Supplemental feed recommendations.
- Schema Product/Offer quando impactar Merchant.

**Mudança proposta:**
- Manter a revisão GMC principal.
- Pausar/corrigir o watchdog duplicado que deu timeout antes de continuar usando.

---

### Sexta — 08:30 BRT

**Cron:** `LK Experiment Ledger + Impact Review`

**Tipo:** estratégico

**Entrega:** Brain + Telegram se houver aprendizado/decisão

**Objetivo:** medir o que foi feito e fechar a semana com aprendizado.

**Cobre:**
- Mudanças SEO/GEO/CRO/GMC live dos últimos 7–14 dias.
- Antes/depois: GSC, GA4, Shopify, GMC, PageSpeed quando disponível.
- Classificação: melhorou, neutro, piorou, inconclusivo.
- Próximo teste recomendado.
- Reverter/iterar/manter.

**Regra:** sexta é dia de medição e decisão, não de mudança em produção.

---

### Sábado — 08:30 BRT opcional

**Cron:** `LK Storefront QA Light Monitor`

**Tipo:** monitor simples

**Entrega:** local + Telegram apenas se houver anomalia

**Objetivo:** detectar quebras óbvias sem gerar ruído.

**Cobre:**
- Home HTTP 200.
- 1 PDP prioritária HTTP 200.
- 1 collection prioritária HTTP 200.
- robots.txt, sitemap, llms.txt.
- 5xx/404 anormal.
- noindex/canonical quebrado evidente.
- title/meta vazios em páginas críticas.

---

### Domingo

Sem rotina fixa pesada.

Apenas D+7/D+14/D+30 pontuais quando existirem.

## Handoff para [LK] Otimização de Coleção

Quando LK Growth detectar oportunidade em coleção/LKGOC:

1. Criar briefing local no Brain com:
   - URL/handle.
   - Evidência: GSC/GA4/Shopify/GMC/SERP quando disponível.
   - Problema/oportunidade.
   - Hipótese de impacto.
   - Métrica de sucesso.
   - Restrições premium/LK.
   - Risco.
   - Prazo sugerido.
2. Enviar resumo para Lucas aprovar/ver.
3. Não executar alteração visual/textual LKGOC no LK Growth.
4. Após execução pelo novo agente, LK Growth mede D+7/D+14.

## Alterações em jobs atuais propostas

### Manter, mas renomear/ajustar horário

- Atual: `LK Growth OS Weekly Growth Review`
- Novo: `LK Growth Weekly Command Center`
- De: segunda 10:00 BRT aproximado atual
- Para: **segunda 08:30 BRT**

### Manter e ampliar escopo

- Atual: `LK Growth OS GMC Review read-only`
- Novo: `LK GMC/Product Data + Local Inventory Review`
- Para: **quinta 08:30 BRT**

### Manter, ajustar horário e nome

- Atual: `LK SEO/GEO Experiment Ledger — weekly impact review`
- Novo: `LK Experiment Ledger + Impact Review`
- Para: **sexta 08:30 BRT**

### Criar novos

- `LK SEO/GSC + GEO Opportunities Review` — terça 08:30 BRT.
- `LK CRO/PDP Funnel Review read-only` — quarta 08:30 BRT.
- `LK Storefront QA Light Monitor` — sábado 08:30 BRT, opcional/silencioso.

### Pausar ou corrigir

- `LK GMC Review read-only mandatory delivery`
  - Motivo: duplicado com GMC Review e último status foi timeout.
  - Recomendação: pausar por enquanto ou aumentar timeout/corrigir script depois.

## Riscos

- Excesso de ruído se os crons técnicos mandarem mensagem mesmo sem ação.
  - Mitigação: técnicos só Telegram se houver alerta/oportunidade/decisão.
- Duplicidade entre segunda e sexta.
  - Mitigação: segunda = priorização; sexta = medição.
- Conflito com novo agente LKGOC.
  - Mitigação: LK Growth só gera handoff/briefing e mede impacto.
- Dados autenticados ausentes podem deixar recomendações não decision-grade.
  - Mitigação: marcar lacunas explicitamente.

## Aprovação necessária

Para implementar nos crons reais, Lucas precisa aprovar:

1. Criar os 3 novos crons:
   - SEO/GSC + GEO terça 08:30.
   - CRO/PDP Funnel quarta 08:30.
   - Storefront QA Light sábado 08:30.
2. Renomear/ajustar horários dos 3 crons existentes principais.
3. Pausar ou corrigir o watchdog GMC duplicado.

## Pedido de aprovação

Lucas, aprova eu aplicar a **Agenda v2** nos crons reais do perfil `lk-growth`?

Opções:

- **Aprovo completo** — cria/ajusta tudo acima.
- **Aprovo sem sábado** — cria segunda a sexta, deixa QA light fora.
- **Aprovo só novos crons** — cria terça/quarta/sábado, sem mexer nos existentes.
- **Aprovo docs apenas** — manter como planejamento, sem alterar cron real.
