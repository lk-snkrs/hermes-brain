# Approval packet — LK POS pós-compra / novo lote após telefone inválido

Data: 2026-06-09T16:34:51Z
Área: LK / Atendimento / Pós-compra / Evolution API LK Flagship
Status: aguardando aprovação explícita para envio externo.

## Contexto

O lote anterior aprovado parou corretamente no primeiro erro:

- pedido `#147695`
- Evolution retornou `400 Bad Request`
- causa sanitizada: `exists=false`
- interpretação: número não existe/não apto no WhatsApp segundo Evolution
- `#147697` e `#147698` não foram tentados

## Pedido atual do Lucas

Lucas disse “Seguir”. Pela regra deste perfil, “seguir” permite continuar o fluxo seguro, mas não autoriza novo write externo/produção. Portanto, este pacote só prepara o próximo lote.

## Proposta de novo lote

Enviar lote pequeno de 3 mensagens reais via Evolution API LK Flagship Store, excluindo `#147695`.

Candidatos:

- `#147697`
- `#147698`
- `#147699`

Todos estão atualmente:

- `status=scheduled`
- `dry_run=true`
- `send_executed=false`
- `external_write_executed=false`
- com telefone presente
- com mensagem preparada

## Estado da fila antes de eventual aprovação

- jobs `scheduled` pendentes: 8
- lote recomendado: 3
- remanescentes após lote de 3: 5
- jobs com `send_error`: 1 (`#147695`)

## Guardrails para execução se aprovado

Se Lucas aprovar explicitamente:

1. criar backup pré-envio;
2. selecionar apenas `#147697`, `#147698`, `#147699`;
3. chamar Evolution `sendText` no máximo 3 vezes;
4. parar no primeiro erro HTTP/status inesperado;
5. após cada aceite, atualizar ledger local;
6. verificar webhook de reconciliação `server_ack`/`delivered`;
7. não alterar Doppler, cron, Shopify, Tiny, Chatwoot ou Vercel.

## Frase de aprovação necessária

Para executar o próximo lote real, pedir aprovação explícita:

> Aprovo enviar 3 mensagens reais de pós-compra pela Evolution LK Flagship para os pedidos #147697, #147698 e #147699.

Sem essa aprovação, não enviar.
