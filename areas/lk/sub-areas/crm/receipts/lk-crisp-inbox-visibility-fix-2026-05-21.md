# LK Crisp Inbox visibility fix — 2026-05-21

## Contexto
Lucas reportou que conversas disparadas pelo n8n não estavam aparecendo corretamente na Inbox da Crisp. Screenshot mostrava erro de resposta do WhatsApp indicando que o usuário respondeu, mas não pôde ser encontrado na Crisp.

## Documentação consultada
Crisp WhatsApp API quickstart: template messages podem ser enviados como `note` ou como `text`. Para aparecer como mensagem normal no inbox, usar `crisp_options.type = "text"`. A documentação também indica que `text` deve existir em pelo menos um componente do template e recomenda adicionar `text` nos componentes para melhor resultado. A opção `new_session` controla iniciar nova conversa na Crisp.

## Diagnóstico
- Workflow checkout ativo: `kWQbmEMuvdipcGjd` / `LK - Checkout Abandonado 30min/24h/72h Polling GraphQL - Crisp (ATIVO)`.
- Workflow cart intent ativo: `XLODECE4MvNRNCQ9` / `LK - Cart Intent 30min Full Funnel - Crisp (ATIVO)`.
- Ambos já usavam `crisp_options.type = "text"` e `as = "text"`.
- Ambos usavam `new_session: false`, o que pode deixar contatos sem sessão prévia sem conversa criada/achável na Crisp.
- Checkout já tinha `BODY.text` no componente na versão corrente, mas execuções antigas não tinham.
- Cart Intent não tinha `text: fallbackText` no componente `BODY`.

## Correção aplicada
Snapshots raw dos workflows salvos no VPS em:
`/root/hermes-snapshots/n8n-crisp-inbox-20260521-091546/`

Patch aplicado:
- Checkout: `crisp_options: { as: 'text', type: 'text', new_session: true }`.
- Cart Intent: `crisp_options: { as: 'text', type: 'text', new_session: true }`.
- Cart Intent: adicionado `text: fallbackText` no componente `BODY`.
- Mantido top-level `BODY.text` para compatibilidade LK/Crisp.

## Verificação
Readback n8n após update:
- Checkout `active: true`; `versionId` = `activeVersionId` = `a1c4ea2d-9149-4300-bfb1-1e5502cc5b51`.
- Cart Intent `active: true`; `versionId` = `activeVersionId` = `8078d666-33e8-4de6-8b7b-c1a15e9d74b9`.
- Ambos têm `new_session: true`, `as: text`, `type: text`, e `BODY` component com `text: fallbackText`.

## Observação
A correção vale para próximos disparos. Mensagens já enviadas sem sessão/conversa criada podem não aparecer retroativamente no Inbox da Crisp.
