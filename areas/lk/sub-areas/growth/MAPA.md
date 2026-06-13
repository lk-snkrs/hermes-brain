# MAPA — LK Growth OS

Subárea especialista da LK Sneakers para Search, Google, Merchant, Analytics, CRO e AI Visibility.

## Missão

Transformar dados de GA4, Search Console, Merchant Center, Shopify, SERP e auditorias técnicas em uma fila semanal de melhorias comerciais para LK: mais tráfego qualificado, melhor CTR, melhor conversão e maior visibilidade em IA, sempre com preview e aprovação antes de writes.

## Escopo

Escopo canônico detalhado: `ESCOPO-18-TOPICOS.md`.

- GA4 / Google Analytics: sessões, usuários, conversão, receita, landing pages, funil e impacto pós-mudança.
- Google Search Console: queries, páginas, impressões, cliques, CTR, posição, indexação, sitemaps e inspeção de URL.
- Google Merchant Center: reprovações, warnings, feed, atributos, preço, disponibilidade e supplemental feed.
- Shopify SEO: title/meta, H1, descrições, canonicals, PDPs, coleções, handles e schema.
- Shopify CRO/theme: PDP mobile, collection pages, filtros, ordenação, CTA, trust blocks, reviews e dev-theme previews.
- GEO / AI Search: `llms.txt`, blocos citáveis, FAQ, schema e estrutura para ChatGPT/Perplexity/Gemini/AI Overviews.
- PageSpeed / CrUX / Core Web Vitals: LCP, INP, CLS e performance mobile.
- Reviews/prova social: Judge.me ou fonte equivalente, snippets e impacto de conversão.
- Paid/influencer signals como contexto: Pareto, FHITS, Meta/Google Ads, produtos divulgados e gargalos de PDP/coleção.
- Claude Blog/content engine: briefs, outlines, artigos/FAQs, clusters, schema editorial, GEO/AEO e repurpose quando a oportunidade for conteúdo/taxonomia comercial.
- Concorrência/SERP e Google Business/local SEO quando aplicável.

## Checklist canônico — 18 tópicos

Antes de declarar um diagnóstico de Growth completo, verificar os 18 tópicos em `ESCOPO-18-TOPICOS.md`: GA4, GSC, GMC, Shopify SEO, Shopify CRO, GEO/AI Search, PageSpeed/CrUX/CWV, schema, reviews, paid signals, influencer/social demand, concorrência/SERP, Google Business/local, Klaviyo/CRM signals, catálogo/product data quality, conteúdo/taxonomia comercial, mensuração/QA de eventos e impact review/experimentation.

## Fontes de verdade

1. Dados comerciais e conversão: Shopify, GA4, GSC e GMC.
2. Demanda/search: GSC, SERP, paid/influencer signals.
3. Diagnóstico público: HTML, PageSpeed, robots/sitemap, schema e `llms.txt`.
4. Brain/Hermes: decisões, guardrails, histórico, skills e rotinas.

## Regras LK críticas

- Relatório SEO/CRO sem dados de vendas, visitas/sessões, conversão, receita, GSC/CTR ou demanda deve ser marcado como não decision-grade.
- Stock/Tiny pode ser contexto operacional, mas não critério decisivo de SEO/CRO.
- Não falar publicamente em pronta entrega/encomenda/estoque como taxonomia; disponibilidade e prazo vão para chat/atendimento.
- Alterações de theme sempre primeiro em dev theme/preview.
- Writes em Shopify, GMC/feed, campanhas, Klaviyo/WhatsApp/email, preço, estoque ou produção exigem aprovação explícita atual de Lucas.

## Agente Telegram

- Perfil Hermes: `lk-growth`.
- Bot Telegram: `LKGrowth_HermesBot`.
- Secret Doppler: `TELEGRAM_LK_GROWTH_BOT_TOKEN` em `lc-keys/prd`.
- Canal recomendado: `[LK] Growth OS` ou DM com o bot para temas de SEO/GMC/CRO/GA4/GSC/GEO.

## Arquivos desta subárea

- `SOUL.md` — personalidade, postura e anti-patterns do agente.
- `IDENTITY.md` — papel, missão, escopo, autonomia e fontes de verdade.
- `USER.md` — perfil de Lucas/LK para este especialista, preferências e guardrails.
- `AGENTS.md` — regras operacionais e aprovações.
- `TOOLS.md` — ferramentas e integrações.
- `MEMORY.md` — memória local da subárea.
- `HEARTBEAT.md` — cadência e checks.
- `ESCOPO-18-TOPICOS.md` — checklist canônico do escopo Growth.
- `CRONS-MIGRATION.md` — mapa de migração das rotinas/cron jobs para o LK Growth OS.
- `CONNECTORS-READONLY-INVENTORY.md` — status dos conectores Shopify, GA4, GSC, GMC, PSI/CrUX, Klaviyo e Meta.
- `CLAUDE-ADS-HERMES-NOTE.md` — nota operacional da instalação Claude Ads/AgriciDaniel no universo LK Growth e modo de uso Hermes.
- `CLAUDE-BLOG-HERMES-NOTE.md` — nota operacional da instalação Claude Blog/AgriciDaniel no universo LK Growth e uso diário para conteúdo/GEO/FAQ/clusters.
- `IMPACT-REVIEWS.md` — política e estado dos follow-ups/impact reviews no profile `lk-growth`.
- Handoff obrigatório para Hermes Central: `../../../operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`.
- `contexto/` — mapas por fonte e domínio.
- `agentic-os/FASE-1B-LK-GROWTH-OS-20260605.md` — OS operacional do agente-funcionário LK Growth: inbox, radar, score, rotinas, workers temporários selecionados automaticamente por tipo de demanda, permissões e feedback loop.
- `agentic-os/inbox-growth.md` — fila operacional de entradas Growth.
- `agentic-os/opportunity-ledger.md` — ledger de oportunidades e score 0-100.
- `agentic-os/feedback-ledger.md` — feedback/aprendizado Growth e regra 1x/2x/3x.
- `rotinas/` — rotinas operacionais.
- `rotinas/growth-decision-router.md` — matriz de decisão para escolher GA4/GSC/GMC/Shopify/CRO/GEO/Ads/Blog/DataForSEO por sintoma.
- `rotinas/growth-d7-review-digest-ledger.md` — rotina local para consolidar reviews D+7 em digest/ledger antes de qualquer mudança de cron ou entrega.
- `rotinas/lk-growth-impact-review-readonly-prewrite-gate-2026-06-12.md` — gate aprovado por Lucas: impact review read-only obrigatório antes de novos writes Growth relacionados a mudanças já aplicadas.
- `rotinas/dataforseo-mcp-reload-approval-2026-05-19.md` — approval packet para expor DataForSEO MCP no runtime ativo sem violar guardrails de VPS/Hermes.
- `templates/growth-audit-output-template.md` — template padrão de auditoria Growth com fatos, interpretação, recomendação, approval packet, rollback e review de impacto.
- `templates/index-playbooks-lk-growth-20260605.md` — playbooks práticos LK Growth para Weekly Command Center, GMC/Product Data, SEO/GEO não-LKGOC, CRO/PDP handoff e Impact Review.
- `templates/d7-review-digest-template.md` — template do digest consolidado de reviews D+7.
- `reports/growth-360-smoke-test-2026-05-19.md` — validação documental do fluxo 360º e próximos critérios de smoke test live controlado.
- `projetos/growth-action-prd-2026-05-19.md` — PRD de ação para cadência semanal orientada a receita, conversão e reviews D+7.
- `prds/lk-otimizacao-colecao-agent-prd-2026-06-03.md` — PRD do agente `[LK] Otimização de Coleção`, especialista LKGOC documental/sem runtime ativado nesta etapa.
- `contexto/` — mapas por fonte e domínio.
- `rotinas/` — rotinas operacionais.
- `templates/` — formatos padronizados de auditoria/approval packet.
- `skills/` — processos repetíveis.
- `projetos/` — PRDs, backlog e approval log.

## 2026-06-01 20:02:48 — Regra transversal: LK Growth Optimized Collection

Para qualquer otimização/melhoria de Shopify collection da LK envolvendo SEO, GEO/AI Search/LLM, CRO, layout, hero, descrição, Guia Editorial LK ou guia dedicado, o fluxo obrigatório é **LK Growth Optimized Collection**.

Fonte canônica: `sub-areas/growth/rules/REGRA-LK-GROWTH-OPTIMIZED-COLLECTION-OBRIGATORIA.md`.
Skill operacional: `sub-areas/growth/skills/lk-superpowers-collection-optimizer/SKILL.md`.
Tag Shopify: `LK Growth Optimized Collection`.

## Alias operacional obrigatório — 2026-06-01T22:19:59Z

- **LKGOC** significa **LK Growth Optimized Collection**.
- Sempre que Lucas falar “LKGOC”, interpretar como o padrão/skill/processo **LK Growth Optimized Collection**.
- O termo se refere ao pacote completo de otimização de coleção: texto hero robusto, layout editorial, imagens editoriais, guia pós-grid, Guia LK, FAQ único canônico, CTA claro, schema, QA, ledger/tag/metafields quando aplicável e link obrigatório de preview após qualquer alteração.
- Regra de comunicação: responder usando o contexto LKGOC sem pedir esclarecimento quando Lucas usar essa sigla.

## Regra LKGOC — coleção + guia juntos — 2026-06-02T00:25:03Z

Feedback Lucas:

- Todo trabalho de **LKGOC / LK Growth Optimized Collection** deve tratar **coleção otimizada + Guia LK dedicado** como um pacote único.
- Não considerar a coleção pronta se o guia dedicado correspondente não estiver planejado, escrito e pronto para publicação/approval.
- Objetivo central: **contar e vender histórias**, não apenas descrever produto.
- Todo texto de coleção e todo Guia LK devem seguir a lógica:
  1. história/origem/DNA do modelo;
  2. como o modelo volta ou se transforma nos tempos atuais;
  3. por que ele é relevante agora em moda, cultura, comportamento e styling;
  4. como a curadoria LK ajuda a escolher versão, cor, proporção, autenticidade e intenção de uso;
  5. fechamento comercial premium, humano e editorial.
- O guia deve cruzar o passado do modelo com sua leitura contemporânea, explicando por que ele importa hoje.
- QA LKGOC reprova textos genéricos, puramente técnicos ou sem narrativa histórica/comercial.

## Regra LKGOC — pesquisa na internet obrigatória — 2026-06-02T00:56:58Z

- Todo **LKGOC / LK Growth Optimized Collection** deve fazer pesquisa na internet antes de escrever ou publicar coleção/Guia LK.
- A pesquisa deve alimentar narrativa, SEO/GEO e curadoria, cobrindo quando aplicável:
  - história/origem/DNA do modelo;
  - contexto cultural e fashion;
  - relevância contemporânea;
  - styling atual;
  - dúvidas reais de busca;
  - SERP/concorrentes;
  - fontes editoriais e páginas oficiais.
- Fontes preferenciais: Google/SERP, DataForSEO, páginas oficiais da marca, Highsnobiety, Hypebeast, Vogue, GQ, Who What Wear, Glamour, FFW, Sneaker News, Complex, Footwear News e veículos editoriais equivalentes.
- O LKGOC não deve inventar história nem escrever só com conhecimento genérico.
- A narrativa final deve cruzar **internet + SERP + fontes editoriais + curadoria LK + intenção comercial atual**.
- Guia LK só passa em QA se explicar: passado/DNA do modelo, por que ele importa agora, como escolher e por que a curadoria LK ajuda a comprar melhor.

## Referência LKGOC

O padrão completo de LKGOC vive em um único documento canônico:

- `LKGOC-PADRAO-CANONICO.md`

Não duplicar regras longas aqui. Este arquivo deve apenas complementar seu escopo específico e apontar para o canônico.

## Projetos Brain OS

- `projetos/gmc-merchant-center/` — hub canônico inicial para GMC/Merchant Center dentro de LK Growth.
- `projetos/theme-cro-performance/` — hub canônico Brain OS Onda 3 para theme/CRO/performance, previews, PageSpeed/CWV e impact reviews.
- `projetos/seo-cro-weekly-improvement/` — hub canônico Brain OS Onda 6 para LK SEO / CRO Weekly Improvement.
- `projetos/rewards-loyalty-trust/` — hub canônico Brain OS Onda 6 para LK Rewards / Loyalty / Trust.
- `projetos/source-pages-geo-experiments/` — hub canônico Brain OS Onda 7 para source pages, GEO/AI Search experiments, comparison tables e impact reviews.
- `projetos/growth-evidence-ledger/` — hub canônico Brain OS Onda 11 para receipts, approval packets, backups, impact reviews e evidência Growth/GMC/SEO/CRO/GEO.
- `projetos/shopify-growth-os/` — hub canônico Brain OS Onda 14 para Shopify como superfície Growth: SEO fields, PDP/coleção, CRO, schema, theme previews e handoffs com aprovação antes de writes.
