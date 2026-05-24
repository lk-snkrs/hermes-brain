# Receipt — LK Recovery OS internal Crisp canary

Data: 2026-05-21

## Contexto

Lucas aprovou seguir com o canary interno do LK Recovery OS para checkout abandonado via Crisp WhatsApp Template API.

## Resultado

- Canal: Crisp WhatsApp Plugin Template API
- Template: `lk_checkout_abandonado_30min_v4`
- Marker aceito pelo provider: `CANARY-LK-153346F`
- Destino: número interno/admin, final `3361`
- Header image: sim
- `from_number`: configurado
- Provider response: HTTP 200 com `reason=request_accepted`
- Provider request ID: `200b47a4-2d6a-488d-9eda-7cb1dc6d7914`
- Nenhum cliente/terceiro foi usado; somente número interno/admin.

## O que mudou vs. primeiro teste/n8n

O primeiro teste havia funcionado porque o workflow n8n já usava o contrato exato do plugin Crisp:

- endpoint com `/wa/api/website/{website_id}/template/send`;
- Basic Auth do WhatsApp Plugin já configurado no n8n;
- `from_number` no payload;
- `message_template.language` como string `pt_BR`;
- `message_template.components[].index` como int;
- aceitação retornando `reason=request_accepted` e `data.request_id`.

No LK Recovery OS recém-implementado, o canary revelou incompatibilidades de contrato antes da correção:

- endpoint default sem `/wa/api`;
- credentials Doppler `CRISP_MARKETPLACE_*` não autenticavam para esse endpoint do plugin;
- `language` estava como objeto estilo Cloud API, mas Crisp esperava string;
- `index` do botão estava como string, mas Crisp esperava int;
- parser tratava o retorno `reason=request_accepted` como rejeição por faltar boolean explícito.

## Correções aplicadas no repo

Commit no PR #1: `44120ee fix: align Crisp template transport contract`

- Ajustado endpoint default para `/wa/api`.
- Adicionado `crisp_from_number`/`from_number` no sender.
- Ajustado payload para `language: "pt_BR"` e `index: 0`.
- Parser passa a reconhecer `reason=request_accepted`.
- Testes atualizados para refletir o contrato real do Crisp.

## Verificação

- Testes locais: `33 passed`
- Ruff: `All checks passed`
- Secret scan local: 0 findings
- GitHub Actions no commit `44120ee`: success

## Pendência

Confirmar no WhatsApp/InBox se o marker `CANARY-LK-153346F` apareceu para Lucas. A resposta do provider confirma aceite, mas ainda não é o mesmo que callback de entrega/visualização.
