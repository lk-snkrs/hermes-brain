# Decisions and Guardrails — LK Shopify Theme Backups Archive

## Decisões

- Onda 12 cria hub de arquivo/rollback de theme para impedir que backups sejam confundidos com estado production atual.

## Guardrails

- Backup é rollback/evidência histórica, não fonte viva do theme atual.
- Production/main Shopify continua proibido sem aprovação explícita e fluxo correto.
- DEV/unpublished e preview devem ser rotulados como não customer-facing.
- Não publicar, promover, deletar ou alterar assets nesta onda.
