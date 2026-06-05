# LK Growth — leitura dos crons e decisão sobre subagentes

Data: 2026-06-04
Modo: read-only/local docs. Nenhum cron, profile, gateway ou integração externa alterado.
Fonte runtime: `/opt/data/profiles/lk-growth/cron/jobs.json` atualizado em `2026-06-04T11:53:54Z` + output do cron `1240644c5f3f`.

## Inventário resumido

Total no perfil `lk-growth`: 15 jobs.

### Recorrentes ativos

- Segunda 11:30 UTC — `LK Growth Weekly Command Center` (`738d3deabaeb`): visão executiva, 18 tópicos, top prioridades por impacto/esforço/risco, read-only/preview.
- Terça 11:30 UTC — `LK SEO/GSC + GEO Opportunities Review` (`4edbacaf43ff`): demanda orgânica, GSC, SERP, GEO/AI visibility, backlog SEO/GEO.
- Quarta 11:30 UTC — `LK CRO/PDP Funnel Review read-only` (`9a34dea6ee4b`): gargalos de conversão, PDP mobile, funil, collections, testes pequenos.
- Quinta 11:30 UTC — `LK GMC/Product Data + Local Inventory Review` (`1240644c5f3f`): Merchant/product data/local inventory; último status `ok` em 2026-06-04.
- Sexta 11:30 UTC — `LK Experiment Ledger + Impact Review` (`de3a45d36040`): medir mudanças recentes, classificar impacto, fechar aprendizado.
- Sábado 11:30 UTC — `LK Storefront QA Light Monitor` (`6cdd70fcec80`): QA público leve, deliver local, Telegram só anomalia.

### Pausado / substituído

- `LK GMC Review read-only mandatory delivery` (`d4c26da4cd48`) está pausado desde 2026-06-03: duplicado, timeout anterior, substituído por Agenda v2 GMC Review.

### One-shots ativos

Há múltiplos D+7/D+14 impact reviews para artigos, coleções, guias e correções GMC/SEO publicadas entre 2026-05-29 e 2026-06-01. Eles funcionam como accountability pós-write: validar público, GSC/GA4/Shopify quando disponível, e dizer se ficou decision-grade ou não.

## Aprendizados operacionais

1. O Growth já tem um sistema semanal dividido por domínio. Não precisa de mais crons genéricos.
2. O padrão correto é `read-only/preview → approval packet → write aprovado → D+7/D+14 impact review`.
3. O output de quinta mostrou boa maturidade: dados autenticados GMC, zero writes, problema nominal, packet proposto, rollback e artefatos no Brain.
4. O ponto fraco atual é excesso de one-shots no Telegram/origin: útil para accountability, mas pode virar ruído se muitos revisarem pequenas mudanças ao mesmo tempo.
5. O perfil `lk-growth` mistura muitas especialidades dentro de prompts longos. Isso aumenta contexto carregado e risco de relatório pesado. A solução não é criar vários bots independentes, mas dividir execução dentro do job.
6. O job precisa de “consenso operacional”: coleta por especialistas, síntese única e fila priorizada final. Sem isso, subagentes podem gerar peças soltas.

## Devemos criar subagentes?

Sim, mas no sentido de **subagentes trabalhadores internos por run**, não novos perfis/bots/crons autônomos neste momento.

### Recomendação

Criar um desenho de execução com 4–5 subagentes internos chamados pelo `lk-growth` quando o job for grande:

1. `Growth Data Scout`
   - Lê/normaliza GA4, GSC, Shopify, GMC, DataForSEO, Ahrefs/PageSpeed/Klaviyo quando disponíveis.
   - Só coleta evidência e gaps. Não recomenda sozinho.

2. `SEO/GEO Analyst`
   - Analisa queries, SERP, AI mentions, llms/agents, FAQ/schema e citabilidade.
   - Produz oportunidades com evidência e nível de confiança.

3. `CRO/PDP Analyst`
   - Analisa conversão, PDP mobile, collection→PDP, PageSpeed/CWV e hipóteses de teste.
   - Se não houver GA4/Shopify, marca non decision-grade.

4. `GMC/Product Data Analyst`
   - Analisa Merchant issues, product data, Local Inventory/LIA, price/landing/color/GTIN.
   - Sempre output em approval packets, sem writes.

5. `Growth Editor/Governor`
   - Consolida os outputs, remove duplicidade, prioriza top 5, verifica guardrails, transforma em Telegram curto + Brain report.

### Guardrail

Subagentes não devem:

- publicar ou escrever em Shopify/GMC/Klaviyo/Meta/WhatsApp;
- criar crons novos;
- falar com Lucas diretamente;
- salvar memória global;
- decidir prioridade final isoladamente;
- rodar ferramentas autenticadas sem secret handling seguro.

### Quando criar novo profile/bot separado

Só criar profile/bot novo quando houver ownership operacional separado e fila própria recorrente, por exemplo:

- `lk-collection-optimizer` já existe para LKGOC/coleções.
- `lk-shopify` para superfície Shopify/theme/GMC execution preview.
- Futuro `lk-content-manager` se conteúdo/inbox/score virar rotina diária real com Renan/LK.

Não criar novo subagente/bot apenas por estética. Primeiro provar a demanda dentro de `lk-growth`.

## Decisão recomendada

- Agora: padronizar subagentes internos no prompt/skill dos jobs grandes.
- Não criar novos crons autônomos.
- Não criar novos bots até haver caso de uso real, dono, cadência, skill, permissões, output e kill criteria.
- Próxima evolução segura: atualizar skill `lk-seo-weekly-improvement` com um bloco `Subagent execution pattern` e aplicar primeiro no `Weekly Command Center`/sexta `Experiment Ledger`.
