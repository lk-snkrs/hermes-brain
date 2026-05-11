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

## Rotinas

- `rotinas/cross-sell-monitor.md` — oportunidades pós-pedido.
- `rotinas/rfm-semanal.md` — cálculo e relatório RFM.
- `rotinas/outcomes-tracker.md` — acompanhamento das sugestões do Hermes.
- `rotinas/playbook-campanha-crm-aprovada.md` — campanha CRM com segmentação, preview e aprovação Lucas antes de envio.
- `rotinas/klaviyo-p1-draft-campaign-2026-05-11.md` — primeira execução P1 em Klaviyo: lista, import, template e campanha em Draft, sem envio/agendamento.
- `rotinas/phase5-next-decision-router-readonly-2026-05-11.md` — router de próxima decisão da Fase 5: manter P1 Klaviyo em Draft, bloquear repetição WhatsApp, preparar P2 preview ou refresh Data Spine.

## Dados principais

- Supabase LK `cnjimxglpktznenpbail`.
- Shopify LK.
- Klaviyo.
- Evolution Clo para WhatsApp aprovado.

## Regras

- Não sugerir produto fora de estoque.
- Respeitar regra de 90 dias para cross-sell por cliente.
- Não disparar campanha ou WhatsApp sem aprovação explícita.
- Registrar resultado para fechar o ciclo de aprendizado.
- HTML customer-facing de CRM não deve conter jargões internos como P1, Brain, preview, Klaviyo, sem envio, SKU/Tiny ou mecânica de estoque.
