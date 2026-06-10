# Decisions and Guardrails — GMC Merchant Center / LK Growth

## Decisões válidas

- Este hub é canônico para orientação inicial deste projeto no Brain OS.
- Originais permanecem onde estão.
- Estado vivo deve ser confirmado em fonte viva antes de ação externa.

## Guardrails

- Sem GMC/feed/API write sem aprovação escopada
- Sem Shopify write sem aprovação escopada
- Distinguir diagnóstico de mudança externa

## Bloqueios gerais Brain OS

- Sem secrets.
- Sem writes externos.
- Sem runtime/Docker/VPS/gateway/cron.
- Sem mover/apagar histórico.
- Sem GitHub push sem aprovação.
