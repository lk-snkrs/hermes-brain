# LK Crisp Inbox test — 2026-05-21

## Pedido
Lucas pediu teste para `+55 11 98111-9821` após correção de Inbox visibility da Crisp.

## Correções adicionais antes/durante o teste
- Workflows ativos verificados com `new_session: true`, `type: text`, `as: text`, `BODY.text` component-level.
- Checkout workflow: já estava com `from_number` real da LK (`...5000`) após readback.
- Cart Intent workflow: removido `from_number` mascarado e atualizado para o número real da LK (`...5000`).
- Snapshot Cart/Checkout antes desse patch salvo no VPS: `/root/hermes-snapshots/n8n-crisp-from-number-fix-20260521-093220/`.

## Testes enviados
1. Marker `INBOX062919`
   - Destino final: `9821`
   - Crisp response: `request_accepted`
   - Request ID: `8929b2bf-a094-456d-afc1-ada389e62016`
   - Observação: primeiro teste usou direct payload antes da correção explícita do `from_number` real no script de teste.

2. Marker `INBOX063246`
   - Destino final: `9821`
   - Crisp response: `request_accepted`
   - Request ID: `e6f3cf6f-0e8e-47c6-b04a-b38d1ba3f817`
   - Payload: `crisp_options: { as: 'text', type: 'text', new_session: true }`, `BODY.text`, componente `BODY.text`, `from_number` real LK.

## Verificação imediata
- n8n callback workflows checados logo após os testes: nenhum callback encontrado ainda para os request IDs.
- Crisp REST conversations checado por marker e telefone logo após os testes: nenhum registro encontrado ainda.

## Verificação após Lucas reportar não-recebimento
- Lucas informou que não recebeu o teste novo no número final `9821`.
- n8n callback workflows ativos verificados: `HTTOStvvzcz0sELN` e `8heG4ZyRp85p0MQj`, ambos ativos/publicados.
- Busca em 50 execuções recentes do callback debug e 5 execuções recentes do callback capture: nenhum hit para `INBOX063246`, `INBOX062919`, `e6f3cf6f...` ou `8929b2bf...`.
- Busca global em 100 execuções recentes do n8n: nenhum hit para os marcadores/request_ids.
- Supabase `lk_crisp_whatsapp_receipts`, `lk_crm_checkout_sequences` e `lk_crm_event_log`: 0 linhas para os request_ids `e6f3cf6f...` e `8929b2bf...`.
- Crisp REST: 160 conversas recentes e respectivas mensagens checadas; nenhum `INBOX063246`/`INBOX062919` encontrado. Menções a `9821` eram de conversas de clientes não relacionadas.

## Interpretação
`request_accepted` confirmou apenas que a Crisp aceitou/enfileirou o teste, mas o não-recebimento + ausência de callback/Inbox indicam que a tentativa não virou entrega real nem conversa visível. O delta contra o primeiro teste confirmado é importante: o primeiro sucesso (`INBOX114811`) foi template de checkout **sem mídia** (`lk_checkout_abandonado_30min_v2`) com `crisp_options` híbrido e `new_session:false`; os testes posteriores introduziram template com imagem/header e, no teste final, `new_session:true`. Não continuar com retestes cegos no mesmo número sem isolar uma variável ou usar outro número interno controlado.
