# HEARTBEAT — Agente Zipper

Status: documental/read-only; runtime dedicado Zipper pendente/futuro.

## Checks sugeridos

- Feiras próximas e pendências associadas.
- Relatórios comerciais pendentes.
- Comunicação aprovada aguardando envio.
- Inconsistência entre vendas reais e relatórios.
- Inbox/ZPR com pedido que exige fonte viva (`CRM/Main`, `vendas_tango`) antes de resposta.
- Drafts sensíveis aguardando aprovação Lucas/Osmar.

## Política de ruído

Silent-OK: não avisar quando tudo está saudável.

Alertar apenas quando houver:

- decisão necessária;
- bloqueio por aprovação;
- divergência de fonte;
- risco de cliente/artista/colecionador receber dado sem fonte;
- oportunidade comercial clara com evidência;
- falha de fonte read-only relevante.

## Bloqueios permanentes sem aprovação explícita

- contato externo;
- preço, proposta, desconto, reserva ou disponibilidade;
- logística sensível;
- publicação/campanha;
- alteração de CRM, banco, site, automação, cron, gateway ou runtime.

## Handoff

Se houver output material ou decisão pendente, registrar no ledger:

- `empresa/contexto/handoff-ledger.md`
- `empresa/contexto/handoffs/YYYY-MM-DD.md`

Todo registro deve declarar `Writes externos: não` quando a execução foi apenas read-only/local.
