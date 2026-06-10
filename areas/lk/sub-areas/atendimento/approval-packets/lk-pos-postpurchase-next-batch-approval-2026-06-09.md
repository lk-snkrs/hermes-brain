# Approval packet — LK POS pós-compra / próximo lote Evolution

Data: 2026-06-09T16:17:04Z
Área: LK / Atendimento / Pós-compra / Evolution API LK Flagship
Status: aguardando aprovação explícita para envio externo.

## Contexto

O canário real único anterior foi bem-sucedido:

- pedido: `#147694`
- Evolution aceitou `201/PENDING`
- reconciliação local confirmou `server_ack` e `delivered` com `matched=1 updated=1`

## Pedido atual do Lucas

Lucas disse “Seguir”. Pela regra operacional deste perfil, “seguir” permite continuar o fluxo seguro, mas não autoriza novo write externo/produção. Portanto este pacote prepara o próximo passo sem executar envios.

## Proposta de próximo lote

Enviar lote pequeno de 3 mensagens reais via Evolution API LK Flagship Store.

Próximos candidatos, apenas por número de pedido:

- `#147695`
- `#147697`
- `#147698`

Todos estão atualmente:

- `status=scheduled`
- `dry_run=true`
- `send_executed=false`
- `external_write_executed=false`
- com telefone presente
- com mensagem preparada

## Estado da fila antes de eventual aprovação

- jobs `scheduled` pendentes: 9
- lote recomendado: 3
- remanescentes após lote de 3: 6

## Guardrails para execução se aprovado

Se Lucas aprovar explicitamente, executar com wrapper temporário de limite rígido, não com worker genérico permanente:

1. criar backup pré-envio;
2. selecionar apenas os 3 pedidos listados;
3. chamar Evolution `sendText` no máximo 3 vezes;
4. após cada envio, atualizar ledger local;
5. verificar webhook de reconciliação `server_ack`/`delivered`;
6. parar se houver erro HTTP ou status inesperado;
7. não alterar Doppler, cron, Shopify, Tiny, Chatwoot ou Vercel.

## Frase de aprovação necessária

Para executar o próximo lote real, pedir aprovação explícita como:

> Aprovo enviar 3 mensagens reais de pós-compra pela Evolution LK Flagship para os pedidos #147695, #147697 e #147698.

Sem essa aprovação, não enviar.
