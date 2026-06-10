# Next Steps — Chatwoot / Elle / LK Atendimento

## P0 — Consolidação Brain/Git

- Revisar este hub canônico.
- Decidir se os 26 arquivos Chatwoot ainda untracked devem ser adicionados ao Git do Brain.
- Antes de qualquer commit/push: rodar focused secret scan e excluir caches/artefatos sensíveis.

## P1 — Operação segura

- Manter Chatwoot como camada interna/copiloto até nova aprovação.
- Para pós-venda POS, confirmar objetivo do próximo lote antes de qualquer novo apply.
- Separar claramente:
  - nota privada/internal context;
  - mensagem externa ao cliente;
  - automação/campanha.

## P2 — Produto/arquitetura

- Transformar os PRDs dispersos em roadmap único: Elle core, Shopify context, WhatsApp templates, POS flagship, Cloud migration.
- Criar checklist de activation readiness antes de qualquer runtime/campanha.
- Definir owner operacional para manutenção do Chatwoot após cada deploy.

## Bloqueios que continuam

- Nenhuma mensagem externa sem aprovação escopada.
- Nenhum write em Chatwoot/Shopify/Tiny/WhatsApp/Evolution sem snapshot/readback/receipt.
- Nenhum secret no Brain/Git/Telegram.
