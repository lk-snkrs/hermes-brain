# Handoff — Klaviyo wishlist T97an8 corrigido e reativado

- Data: 2026-06-17
- Área: LK / Atendimento / CRM Ops
- Solicitante/aprovação: Lucas — “seguir do 1 ao 4”
- Sistema externo alterado: Klaviyo
- Flow: `T97an8` — `Swym - Wishlist Winback (Lembrete)`
- Action: `104217194` — `Email - Wishlist Winback`
- Template antigo: `YwnNTz`
- Template final associado no readback: `Ti5z7w`
- Nome template final: `LK FIXED Swym Wishlist T97an8 — CODE — 20260617T141304Z`
- Metric/evento usado para validação: `Swym-addToWishlist` / `UcN9EY`
- Secrets: não impressos (`values_printed=false`)

## O que foi feito

1. Snapshot/readback do flow pausado e evento real recente.
2. Tentativa segura de patch no template antigo `YwnNTz`; Klaviyo rejeitou o PATCH direto no ID antigo.
3. Criado template CODE corrigido a partir do HTML antigo, substituindo variáveis inexistentes por propriedades reais do evento Swym.
4. Associada a action `104217194` ao template corrigido e colocada em `live`.
5. Flow `T97an8` reativado para `live`.
6. Validação read-only final confirmou o template efetivo `Ti5z7w` no flow/action.

## Variáveis corrigidas

- `event.ProductTitle` → `event.ProductName`
- `event.ProductImageURL` → `event.ImageURL`
- `event.Price` → `event.ProductPrice`
- `event.Brand` → `event.ProductBrand`
- `event.VariantTitle` → `event.VariantInfo`
- `event.ProductURL` permaneceu válido.

## Evidência de validação final

Comando read-only final retornou `exit_code=0` e `result=ok_final_readback_validated`.

Readback final:

- Flow status: `live`
- Action status: `live`
- Template associado: `Ti5z7w`
- Variáveis no template final:
  - `event.ImageURL`
  - `event.ProductBrand`
  - `event.ProductName`
  - `event.ProductPrice`
  - `event.ProductURL`
  - `event.VariantInfo`
  - `first_name`
- Variáveis antigas restantes: nenhuma.
- Evento real tinha todas as chaves necessárias.
- Render local com evento real:
  - nome do produto presente: sim
  - imagem presente: sim
  - preço presente: sim
  - ProductURL presente: sim
  - padrão `R$` vazio: não

## Receipts / artefatos

- Receipt principal: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/20260617T141414Z-klaviyo-T97an8-associate-fixed-template-reactivate.json`
- Render validado: `/opt/data/profiles/lk-ops/tmp/klaviyo_T97an8_repair/20260617T141414Z-T97an8-rendered-fixed-template.html`
- Validador final read-only: `/opt/data/profiles/lk-ops/tmp/klaviyo_validate_T97an8_final_readonly.py`

## Limites

- Nenhum e-mail/teste/campanha foi enviado.
- Nenhum template foi deletado.
- O template antigo `YwnNTz` ficou como histórico, mas não é o template associado no flow final.

## Reminder OS

- Reminder OS loop needed: no
- Motivo: incidente corrigido, flow reativado e validação final passou.
