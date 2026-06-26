# LKGOC — regra de namespace para Guia Editorial

Registrado em: 2026-06-03T21:04:49.986541+00:00

## Regra

Para novos blocos LKGOC de guia editorial de coleção, o namespace final deve ser `lk-goc-*`.

O padrão visual aprovado da 204L pode e deve ser usado como Gold Source, mas o CSS/HTML deve ser clonado e renomeado para `lk-goc-*`, não mantido como `lk-guide-standard-*` no componente novo.

## Correto

- `lk-goc-guide-panel`
- `lk-goc-guide-panel__eyebrow`
- `lk-goc-guide-panel__intro`
- `lk-goc-guide-grid`
- `lk-goc-guide-card`
- `lk-goc-guide-card--wide`
- `lk-goc-guide-faq`
- `lk-goc-guide-media`
- `lk-goc-guide-panel__cta`

## Incorreto

- Usar `lk-guide-standard-panel` como namespace final de um componente LKGOC novo.
- Corrigir visual importando o seletor antigo sem renomear.
- Criar `lk-goc-guide-panel` sem copiar o CSS base equivalente da 204L.

## Princípio

**Mesmo CSS/contrato visual da 204L, namespace LKGOC novo.**

Ou seja: copiar/adaptar visual aprovado, trocar apenas conteúdo e namespace para `lk-goc-*` quando for componente LKGOC novo.

## Evidência do erro corrigido

Adidas Samba DEV foi corrigido para usar `lk-goc-guide-panel` com CSS base e overrides equivalentes ao padrão 204L, sem `lk-guide-standard-panel` no snippet.

Receipt final:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/adidas-samba-guide-goc-cssbase-final-20260603T210404Z`
