# Skill — LK Leads Esfriando

Fonte canônica atual: `skills/lk-leads-esfriando/SKILL.md`.

Esta cópia de área organiza a skill dentro do CRM LK sem substituir a versão canônica.

## Quando usar

- Clientes sem recompra em janela de 30–60 dias.
- Queda de interação em Klaviyo/site.
- Lucas pede oportunidades de reativação ou risco de churn.

## Fluxo Hermes

```text
cliente sem recompra → interação recente → risco → estratégia → preview Lucas → campanha/contato aprovado → resultado → lesson
```

## Segmentos iniciais

- Quente: interagiu, mas não comprou.
- Frio: sem interação.
- Risco: compra anterior em marca/cluster com baixa lealdade.

## Credenciais

Buscar via Doppler `lc-keys/prd`; nunca versionar valores.

- `SUPABASE_LK_SERVICE_KEY`
- `KLAVIYO_API_KEY`
- `EVOLUTION_API_KEY` / `EVOLUTION_INSTANCE` se houver WhatsApp aprovado.

## Aprovação

Obrigatória antes de disparo Klaviyo, WhatsApp, cupom ou mensagem direta.
