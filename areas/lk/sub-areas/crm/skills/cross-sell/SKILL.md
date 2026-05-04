# Skill — LK Cross-sell

Fonte canônica atual: `skills/lk-crosssell/SKILL.md`.

Esta cópia de área existe para navegação no modelo Bruno/OpenClaw adaptado ao Hermes.
Não duplicar lógica operacional aqui sem atualizar a skill canônica.

## Quando usar

- Pedido LK com status fulfilled.
- Cliente elegível para recomendação complementar.
- Lucas pede oportunidade de recompra, cross-sell ou cliente recente.

## Fluxo Hermes

```text
pedido fulfilled → histórico cliente → elegibilidade 90 dias → estoque → recomendação → preview Lucas → envio aprovado → registro resultado
```

## Credenciais

Buscar via Doppler `lc-keys/prd`; nunca versionar valores.

- `SUPABASE_LK_URL`
- `SUPABASE_LK_SERVICE_KEY`
- `KLAVIYO_API_KEY` quando houver campanha.
- `EVOLUTION_API_KEY` / `EVOLUTION_INSTANCE` quando houver WhatsApp aprovado.

## Aprovação

Obrigatória antes de qualquer envio externo ao cliente.
