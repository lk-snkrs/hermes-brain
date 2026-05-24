# Receipt — auditoria de envios WhatsApp CRM e visibilidade Crisp Inbox

Data: 2026-05-21
Área: LK CRM / WhatsApp / Crisp / n8n / Supabase / Shopify

## Pedido

Lucas suspeitou de erro porque as mensagens não estavam aparecendo na Inbox do Crisp e pediu verificação.

## Escopo read-only

Verificado sem disparar mensagem, sem executar workflow manualmente e sem alterar produção:

- n8n workflow checkout abandonado: `kWQbmEMuvdipcGjd`
- n8n workflow cart intent: `XLODECE4MvNRNCQ9`
- n8n callback workflows Crisp
- Supabase/PostgREST CRM state
- Shopify GraphQL `abandonedCheckouts`
- Crisp REST Website API para amostra de conversas recentes

## Achados principais

### 1. Workflows ativos

Ambos os workflows principais estão ativos e com `activeVersionId == versionId`:

- Checkout abandonado: ativo
- Cart Intent: ativo

### 2. Não houve envio real nos ciclos mais recentes

Nas execuções recentes do checkout abandonado, o workflow rodou a cada 5 minutos com sucesso, mas parou em:

- `A cada 5 min`
- `Shopify GraphQL abandonedCheckouts`
- `Postgres Load CRM State`
- `Filtrar elegíveis + dedup`

O node de envio Crisp não foi alcançado nos ciclos auditados.

Nas execuções recentes de Cart Intent, o fluxo capturou eventos e aguardou 30 minutos, mas parou em:

- `Filtrar cart intent elegíveis`

Também não alcançou o node `Crisp Send cart intent` nas execuções recentes.

### 3. Shopify tem abandonos, mas o workflow atual só considera pós-cutoff e WhatsApp elegível

Consulta Shopify `abandonedCheckouts(first: 250)` mostrou:

- 250 checkouts retornados
- 241 antes do cutoff de migração `2026-05-20T14:15:00Z`
- 9 depois do cutoff
- desses 9:
  - 5 tinham telefone e idade suficiente
  - 4 estavam sem telefone válido

Os 5 pós-cutoff com telefone já foram processados como `sent`/aceitos anteriormente.

### 4. Supabase mostra accepted/sent, mas isso não é prova de Inbox nem entrega final

Supabase `lk_crm_checkout_sequences` tem 5 sequências de checkout 30min com status `sent` e resposta Crisp `request_accepted`.

`request_accepted` significa aceito/enfileirado pela Crisp, não confirmação de entrega no aparelho e não garantia de ancoragem visual na Inbox.

### 5. Callback/receipt real não apareceu para esses envios

Os workflows de callback existem e estão ativos, mas os callbacks recentes encontrados eram verificações/testes ou callbacks antigos/debug, não recibos reais reconciliando os request IDs dos envios recentes.

### 6. Crisp Inbox scan parcial não confirmou ancoragem para todos os envios aceitos

Uma varredura read-only nas páginas recentes da Crisp REST API encontrou conversas para parte dos telefones, mas não confirmou ancoragem de todos os envios aceitos. Também havia exemplo recente de mensagem de usuário indicando: `user replied to a message but it could not be found in Crisp`, o que reforça que WhatsApp delivery e Inbox/session anchoring são validações diferentes.

## Diagnóstico

Não há evidência de que os ciclos mais recentes estejam enviando mensagens invisíveis. O mais preciso é:

1. Os workflows estão ativos.
2. O Cart Intent está capturando eventos, mas sem telefone/contato resolvido e/ou apenas eventos `product_view`/`identity_update`; por isso não envia.
3. O Checkout tinha 5 candidatos pós-cutoff com telefone; esses foram aceitos pela Crisp antes da correção atual de anchoring.
4. Depois da correção de anchoring, ainda não houve novo envio elegível para validar a Inbox.
5. Os envios aceitos antes da correção podem não aparecer retroativamente no Crisp Inbox.

## Próximos passos recomendados

Sem aprovação adicional:

- Continuar monitorando execuções reais até surgir novo checkout pós-cutoff com telefone.
- Verificar se o próximo envio chega ao node `Crisp Send checkout touchpoint` e se aparece na Inbox.

Com aprovação explícita de Lucas:

- Enviar um canary interno controlado com imagem para validar a forma atual (`new_session:false`, `as:text`, `type:text`, BODY.text e HEADER IMAGE) e checar simultaneamente aparelho + Inbox + callback.
- Se o canary atual continuar fora da Inbox, reabrir a hipótese de sessão/anchoring e testar alternativa controlada com `new_session:true` ou estratégia de criação/lookup de conversa antes do template send.

## Segurança

- Nenhuma mensagem foi enviada nesta auditoria.
- Nenhuma alteração de workflow foi feita.
- Nenhum dado sensível foi registrado integralmente.
- Telefones foram tratados internamente e devem ser reportados apenas por final/last4.
