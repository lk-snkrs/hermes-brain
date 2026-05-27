# HEARTBEAT — LK Shopify

## Ritmo esperado

- Não gerar ruído sem necessidade.
- Alertar apenas quando houver decisão, bloqueio, risco, divergência ou ação aprovada pendente.
- Consolidar outputs materiais em handoff para Hermes Geral/Brain.

## Checks úteis

- Produto tem fonte e SKU correto?
- Estoque/preço/disponibilidade vieram do dono certo?
- Há snapshot antes do write?
- O preview foi aprovado?
- O readback confirma exatamente o que mudou?
- Existe rollback?

## Silent-OK

Se não houver divergência, decisão ou ação aprovada pendente, registrar localmente quando necessário e não enviar Telegram.
