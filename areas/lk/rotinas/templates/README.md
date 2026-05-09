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

## Próximo passo

Gerar exemplos preenchidos com dados fictícios ou dados reais read-only, conforme autorização e disponibilidade das integrações.
