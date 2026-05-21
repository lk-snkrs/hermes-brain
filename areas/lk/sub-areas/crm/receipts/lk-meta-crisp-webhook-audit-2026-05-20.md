# Receipt — Meta/Crisp webhook audit

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / Meta

## Pedido

Lucas perguntou se devemos arrumar o webhook da Meta para apontar para Crisp.

## Verificações read-only

### Phone ID

Phone ID auditado: `1220780761111140`

Campos verificados:

- Número: `+55 11 94956-5000`
- Verified name: `LK Sneakers & Apparels`
- Quality: `GREEN`
- Platform: `CLOUD_API`
- Code verification: `VERIFIED`
- `webhook_configuration.application_host`: `api-partners.zoppy.com.br`

### WABA canônica LK

WABA auditada: `1478026007140488`

Edge `subscribed_apps` retornou:

- App: `Crisp`
- Link: `http://crisp.chat/`
- ID: `1289905004399861`

## Interpretação

A WABA canônica da LK já aparece inscrita no app Crisp em `subscribed_apps`. Portanto, não é correto afirmar que simplesmente precisamos trocar tudo para Crisp sem antes entender a diferença entre:

1. WABA subscription: já mostra Crisp; e
2. Phone ID `webhook_configuration`: ainda mostra host legado/terceiro.

Isso sugere configuração híbrida/histórica ou campo legado no Phone ID. Mudar webhook/app de produção diretamente pode afetar recebimento de mensagens inbound e operação do WhatsApp.

## Comparativo dos testes

- Teste que aparentou chegar: Crisp Template API com shape legado/provado no fluxo LK, `crisp_options: { "as": "text" }`, request `143ddd3a-a91e-4067-b18a-ba7d5aecfdec`.
- Teste que não chegou: Crisp Template API com shape documentado novo, `crisp_options: { "type": "text", "new_session": true }`, request `6ea55176-5cd6-48a5-9c41-84be37f27a8a`.

## Decisão recomendada

Não alterar o webhook Meta em produção ainda.

Próximo passo seguro:

1. Voltar ao shape legado `crisp_options: { "as": "text" }` para teste interno controlado, porque foi o caminho que aparentou chegar.
2. Em paralelo, localizar o Callback URL/log do plugin Crisp para obter receipt final por `request_id`.
3. Só mexer em webhook/app Meta se confirmarmos que o app Crisp não está recebendo eventos apesar de estar inscrito na WABA.

## Rollback caso um write de webhook/app seja aprovado depois

Antes de qualquer alteração:

- salvar snapshot do Phone ID;
- salvar snapshot de WABA `subscribed_apps`;
- registrar app/host atual redigido;
- aplicar mudança em janela curta;
- testar inbound e outbound interno;
- rollback imediato para configuração anterior se inbound do WhatsApp parar de aparecer no Crisp.
