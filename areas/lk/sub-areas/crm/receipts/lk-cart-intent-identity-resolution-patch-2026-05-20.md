# LK Cart Intent — Identity Resolution Patch

Data: 2026-05-20
Workflow: `XLODECE4MvNRNCQ9` — `LK - Cart Intent 30min Full Funnel - Crisp (ATIVO)`
Node alterado: `Filtrar cart intent elegíveis`

## Motivo

Correção solicitada por Lucas: eventos de carrinho vindos de Pixel/Instagram e Klaviyo devem conseguir enviar recuperação de carrinho abandonado **quando a pessoa puder ser identificada**. A versão anterior capturava os sinais, mas exigia telefone direto no próprio evento atual.

## Alteração

Implementada camada de `identityIndex` no static data do workflow:

- indexa tokens de identidade quando algum evento traz telefone/email resolvido;
- tokens usados: Crisp session, Klaviyo `_kx`/`klaviyo_id`/`__kla_id`, Meta `_fbp`/`_fbc`/`fbclid`, Google `gclid`/`_ga`, `_shopify_y`, `anonymous_id`, cart token, email/phone;
- em eventos futuros de carrinho sem telefone direto, tenta resolver telefone pelo token já conhecido;
- se resolver telefone BR válido, segue para a régua de carrinho abandonado;
- se não resolver, continua sem envio e registra skip `missing_or_unresolved_brazil_whatsapp_phone`.

## Guardrails preservados

- Não envia por Pixel/Klaviyo anônimo.
- Não envia se não houver telefone BR resolvido.
- Não envia sem itens no carrinho.
- Não envia sem permalink de carrinho.
- Mantém dedup/pending/sent.
- Mantém template gate.
- Mantém workflow ativo no mesmo ID.

## Readback

- `active`: true
- `versionId`: `724cb7ac-3afa-4d8b-ba8d-7fccf4f1e001`
- `activeVersionId`: `724cb7ac-3afa-4d8b-ba8d-7fccf4f1e001`
- markers confirmados: `identityIndex`, `matchedKnownIdentity`, `cart_intent_30min_v2_1_identity_resolution`

## Rollback

Backup bruto do workflow e JS anterior salvo em:

`/opt/data/hermes_bruno_ingest/.secrets/lk-cart-intent-identity-resolution-20260520T213150Z`

Rollback: restaurar `filter_before.js` no node `Filtrar cart intent elegíveis` ou restaurar `n8n_workflow_before.json` via n8n API.
