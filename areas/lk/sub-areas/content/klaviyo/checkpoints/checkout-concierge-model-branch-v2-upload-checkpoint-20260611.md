# Checkpoint — Checkout Concierge Model Branch v2 — Klaviyo

Data: 2026-06-11
Aprovação: Lucas — “Sim, subir o que fizemos no Klaviyo”

## Resultado

Upload parcial concluído no Klaviyo.

- Flow original live `QVNtnC` preservado/intocado.
- Draft anterior `U5C43z` preservado/intocado.
- Templates CODE criados no Klaviyo para a arquitetura de 3 e-mails por jornada:
  - Email 1 universal: `SPTRa9`
  - Email 2 — New Balance 9060: `YdbvFA`
  - Email 2 — New Balance 530: `VMJzyu`
  - Email 2 — fallback curadoria LK: `QWQHig`
  - Email 3 — 10% off: `WSwa6W`

## Bloqueio

A criação automática do novo flow com `multi-branch-split` via Klaviyo API retornou erro server-side 500 mesmo após ajuste do filtro de branch para tipo string. Não houve criação de novo flow branchado.

## Segurança

- Ativação: não realizada.
- Envio/teste externo: não realizado.
- Cupom: não criado.
- Segmentos/listas: não alterados.
- Secrets: não impressos.

## Próxima ação segura

No Klaviyo UI, montar ou ajustar o draft branchado usando os templates já criados:

1. Trigger: Started Checkout.
2. Email 1 universal → template `SPTRa9`.
3. Split por modelo no checkout:
   - contém 9060 → template `YdbvFA`.
   - contém 530 → template `VMJzyu`.
   - fallback → template `QWQHig`.
4. Email 3 comercial 10% off → template `WSwa6W`.
5. Manter tudo em draft/manual até dupla confirmação explícita.

## Receipt técnico sanitizado

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/klaviyo-qvntnc-checkout-model-branch-v2-upload-20260611.json`
