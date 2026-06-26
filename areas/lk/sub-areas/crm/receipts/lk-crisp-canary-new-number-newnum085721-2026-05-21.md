# LK Crisp canary — novo número interno — 2026-05-21T08:57:22Z

## Escopo

Lucas pediu no turno atual: enviar teste para número final `9821`.

## Payload

- Canal: Crisp WhatsApp Plugin Template API
- Template: `lk_checkout_abandonado_30min_v4`
- Header image: sim
- Crisp options: `{ as: text, type: text, new_session: false }`
- BODY component inclui `text` renderizado
- Destino: final `9821`
- Marker: `NEWNUM085721`
- Imagem pré-validada: HTTP `200`, content-type `image/png`

## Resposta síncrona Crisp

- HTTP: `200`
- error: `False`
- reason: `request_accepted`
- request_id: `None`

## Verificação imediata pós-envio

- Crisp REST conversas recentes: sem sessão localizada para o final `9821` nas primeiras páginas recentes no momento da checagem.
- n8n callback workflows checados: `HTTOStvvzcz0sELN` e `8heG4ZyRp85p0MQj`.
- Resultado: nenhum hit recente contendo `NEWNUM085721` ou final `9821` na checagem imediata.

## Confirmação humana

Lucas confirmou por screenshot que o WhatsApp chegou no aparelho.

Evidência visual:

- Header image do produto renderizado corretamente.
- Domínio/link preview: `lksneakers.com.br`.
- Texto contém marker `NEWNUM085721`.
- CTA exibido: `Finalizar compra`.
- Horário visual no WhatsApp: `05:57`.

## Conclusão

Este canary confirma que o caminho Crisp Template API com `lk_checkout_abandonado_30min_v4`, `HEADER IMAGE`, shape híbrido `{ as: text, type: text, new_session: false }` e `text` no componente `BODY` entrega corretamente em um número interno não bloqueado pela Meta.
