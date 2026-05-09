# Templates read-only — LK Operating System

Status: v0.1 documental.
Objetivo: padronizar os primeiros relatórios internos antes de criar crons, integrações de escrita ou automações.

## Templates

- `daily-sales-brief-07h.md` — briefing diário de vendas, conversão, estoque, recompra, pricing e aprovações.
- `stock-intelligence-center.md` — diagnóstico por produto/modelo/tamanho para ruptura, reposição, sourcing e pricing.
- `weekly-ceo-review.md` — revisão semanal estratégica para Lucas/equipe.

## Regras globais

- São templates read-only.
- Não executam ações externas.
- Não alteram Shopify, Tiny, Notion, Klaviyo, WhatsApp, Meta, Google, n8n, banco ou tema.
- Toda peça de layout/produto precisa de HTML visual para aprovação, não apenas Markdown.
- Toda ação externa exige preview e aprovação explícita.
- Dados pessoais devem ser mascarados por padrão no Telegram.
- Equipe/destinatários ainda precisam ser mapeados antes de qualquer envio recorrente.

## Exemplos preenchidos

- `examples/daily-sales-brief-07h-exemplo.md` — exemplo fictício de briefing diário.
- `examples/stock-intelligence-center-exemplo.md` — exemplo fictício de diagnóstico de estoque por tamanho/variante.
- `examples/weekly-ceo-review-exemplo.md` — exemplo fictício de revisão semanal CEO.

Os exemplos existem para calibrar formato e raciocínio antes de dados reais. Não representam vendas reais da LK e não autorizam nenhuma ação externa.

## Primeiro relatório real read-only

- `../../../../reports/lk-daily-sales-brief-real-2026-05-08-ga4-v02.md` — primeira execução real agregada/read-only com Shopify, Tiny `LK | CONTROLE ESTOQUE` e GA4 Data API.
- `../../../../reports/lk-paid-attribution-brief-real-2026-05-08-v03.md` — primeira execução real agregada/read-only de atribuição paga/influencers com GA4, Shopify web sanitizado e Meta Ads Insights.
- Lucas aprovou o formato geral do Daily Brief em 2026-05-09 com o feedback “ficou bacana”.
- Os relatórios não exportam dados pessoais nem valores de secrets e não executam ações externas.

## Próximo passo

Padronizar UTM/cupom por influencer e reconciliar Meta Ads plataforma × GA4 × Shopify antes de qualquer recomendação de escala/pausa. Antes de cron ou envio recorrente, ainda falta mapear destinatários/equipe e aprovar cadência.
