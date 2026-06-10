# LK CRM — Mapa

## Objetivo

Organizar recompra, retenção e relacionamento de clientes LK a partir de dados reais, sempre com preview e aprovação do Lucas antes de qualquer ação externa.

## Loop Hermes

```text
pedido/cliente → segmentação → recomendação → preview Lucas → envio aprovado → resultado → lesson
```

## Skills

- `skills/cross-sell/SKILL.md` — navegação de área para `skills/lk-crosssell/SKILL.md`.
- `skills/leads-esfriando/SKILL.md` — navegação de área para `skills/lk-leads-esfriando/SKILL.md`.

## Decisões vivas

- `decisions/2026-05-21-crisp-hugo-larissa-response-brain.md` — arquitetura e guardrails do cérebro de respostas LK no Crisp/Hugo: tudo passa pelo Brain via MCP, aprende com Larissa, e transborda obrigatoriamente sob encomenda/status pedido/entrega.
- `decisions/2026-05-20-checkout-abandonado-copy-canonica.md` — fonte de verdade atual para copy/tom/guardrails do WhatsApp checkout abandonado LK. Consultar antes de editar template Meta/Crisp/n8n ou preparar novo draft.

## Rotinas

- `rotinas/cross-sell-monitor.md` — oportunidades pós-pedido.
- `rotinas/rfm-semanal.md` — cálculo e relatório RFM.
- `rotinas/outcomes-tracker.md` — acompanhamento das sugestões do Hermes.
- `rotinas/playbook-campanha-crm-aprovada.md` — campanha CRM com segmentação, preview e aprovação Lucas antes de envio.
- `rotinas/playbook-newsletter-klaviyo-lk.md` — produção de newsletter LK no Klaviyo: design, copy, preview, rascunho, aprovação e pós-envio.
- `rotinas/playbook-whatsapp-meta-templates-carrinho-checkout-abandonado-2026-05-19.md` — playbook para templates WhatsApp Meta via Crisp/n8n: carrinho/checkout abandonado, categorias Marketing, aprovação Meta, QA interno, decisão canônica de copy e rollout seguro.
- `rotinas/aprendizado-diario-larissa-crisp-hugo.md` — rotina desejada de 21h para aprender com respostas reais da Larissa no Crisp/Hugo e atualizar o LK Response Brain com guardrails.
- `rotinas/klaviyo-p1-draft-campaign-2026-05-11.md` — primeira execução P1 em Klaviyo: lista, import, template e campanha em Draft, sem envio/agendamento.
- `rotinas/phase5-next-decision-router-readonly-2026-05-11.md` — router de próxima decisão da Fase 5: manter P1 Klaviyo em Draft, bloquear repetição WhatsApp e preparar P2 preview ou refresh Data Spine.

## Dados principais

- Supabase LK `cnjimxglpktznenpbail`.
- Shopify LK.
- Klaviyo.
- Evolution Clo para WhatsApp aprovado.
- Crisp/Hugo LK: credenciais e lacunas não secretas em `knowledge/lk-response-brain/credentials-required.md`.

## Regras

- Não sugerir produto fora de estoque.
- Respeitar regra de 90 dias para cross-sell por cliente.
- Não disparar campanha ou WhatsApp sem aprovação explícita.
- Registrar resultado para fechar o ciclo de aprendizado.
- HTML customer-facing de CRM não deve conter jargões internos como P1, Brain, preview, Klaviyo, sem envio, SKU/Tiny ou mecânica de estoque.

## Projetos Brain OS

- `projetos/recovery-os/` — hub canônico Brain OS Onda 4 para CRM Recovery OS: checkout/carrinho abandonado, Crisp/Hugo, n8n callbacks, WhatsApp Meta, Klaviyo e outcome tracking.
