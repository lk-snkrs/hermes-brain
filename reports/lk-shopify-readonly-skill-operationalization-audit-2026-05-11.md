# LK Shopify Read-only Skill Operationalization Audit — 2026-05-11

## Veredito

A skill `lk-shopify-readonly` foi auditada e sincronizada para atender ao padrão de “100% operacionalizada” no Hermes Brain.

## Evidências verificadas

- Runtime skill carregável em `/opt/data/skills/productivity/lk-shopify-readonly/SKILL.md`.
- Brain copy existe em `skills/lk-shopify-readonly/SKILL.md`.
- Brain copy foi sincronizada com a runtime skill, conteúdo idêntico.
- Referências Brain sincronizadas: 13 arquivos em `skills/lk-shopify-readonly/references/`.
- Índice principal aponta para a skill: `empresa/skills/_index.md`.
- Mapa LK aponta para a skill: `areas/lk/MAPA.md`.
- Mapa ecommerce LK aponta para a skill: `areas/lk/sub-areas/ecommerce/MAPA.md`.
- Guardrails presentes na skill:
  - Doppler-only secrets.
  - Shopify REST `GET` e GraphQL `query` como padrão.
  - Tiny como verdade de estoque.
  - Shopify stock não tratado como estoque final.
  - Sem Shopify mutation, campanha, envio externo, customer-facing send ou admin/destructive action sem aprovação explícita de Lucas.
  - Exceção SKU-only documentada com backup, rollback e verificação live, apenas quando Lucas aprova explicitamente.

## O que foi corrigido

Antes da auditoria, a runtime skill estava mais atualizada que a cópia do Hermes Brain. A cópia Brain foi atualizada para espelhar a versão runtime e todas as referências operacionais atuais.

## O que não foi feito

- Nenhum acesso live ao Shopify foi necessário para a auditoria da skill.
- Nenhum token foi impresso.
- Nenhuma mutation Shopify foi feita.
- Nenhum preço, estoque, produto, cliente, pedido, tag, tema, webhook, app, admin setting, campanha, Klaviyo, WhatsApp ou banco de produção foi alterado.
- Nenhum cron foi criado.

## Status pós-verificação

Verificações finais ficam registradas no PR desta mudança: health check do Brain, diff check, secret scan de arquivos alterados, PR merge e sync local para `origin/main`.
