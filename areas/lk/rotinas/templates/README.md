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

## Próximo passo

Validar o formato com Lucas. Depois, gerar a primeira execução com dados reais read-only e mascarados, antes de qualquer cron ou integração de escrita.
