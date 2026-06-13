# Handoff LK Stock → LC Hermes — Pendência de identidade operacional

Data/hora: 2026-06-12T00:20:48Z
Agente/profile: `lk-stock`
Empresa/área: LK Sneakers / Stock OS / Shopify↔Tiny identity
Responsável humano: Lucas Cimino

## Produto / contexto

Produto: Meia Saint Studio Pima Branco
Handle Shopify: `meia-saint-studio-pima-branco`
Shopify product_id informado: `9228298027230`
Shopify variant_id informado: `48283857780958`
Shopify inventory_item_id informado: `50411563319518`
GMC offerId informado: `5774345588926734768`

Lucas trouxe diagnóstico de que o produto foi cadastrado/publicado sem chave operacional para ligar Shopify → Tiny/Stock OS.

## Verificação local feita pelo lk-stock

Consulta na DB local Stock OS apontada pelo pointer canônico:

- DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_variant_promotion_20260611T023437Z.db`
- stage: `gate_b3_full_live_match_variant_promotion_completed`
- busca por `48283857780958`, `9228298027230`, `50411563319518`, `5774345588926734768`, `meia-saint-studio-pima-branco`, `Meia Saint Studio Pima Branco`: **0 matches** em `current_local_stock` e **0 matches** em `canonical_current`.
- Houve match amplo apenas por `Saint Studio` em `stock_observations`, mas para outro produto (`bolsa-minimal-saint-studio-cacto-caramelo`), portanto não resolve este caso.

## Diagnóstico operacional

Status: `IDENTITY_GAP_BLOCKS_STOCK_DECISION`

Isto não é uma simples falta de estoque encontrado. É uma lacuna de identidade operacional:

```text
Shopify variant_id 48283857780958
→ sem SKU/barcode/metafield/código Tiny confiável
→ sem mapping local Stock OS
→ sem saldo Tiny/Stock OS resolvível
→ reposição automática bloqueada
```

O `offerId` do GMC não deve ser usado como SKU/Tiny. Ele é identificador de feed/oferta, não chave operacional de estoque.

## Decisão segura atual

- Não aprovar reposição automática ainda.
- Não prometer disponibilidade/pronta entrega.
- Não criar compra/transferência.
- Não fazer Tiny write.
- Não fazer Shopify write.

## Próximo passo recomendado

Tratar como pendência de identidade SKU/Tiny/Shopify:

1. Investigar read-only no Tiny por título/marca/categoria para achar candidato real da meia.
2. Se houver candidato Tiny único e confiável, registrar proposta de alias local:
   - `Shopify variant_id 48283857780958 → Tiny codigo/SKU X`.
3. Se não houver candidato confiável, criar pendência para cadastro humano/operacional preencher SKU/barcode/metafield ou confirmar criação no Tiny.
4. Só depois do vínculo resolvido rodar estoque/reposição.

## Guardrails

- `tiny_write`: 0
- `shopify_write`: 0
- `writes_externos`: 0
- `public_availability_safe`: 0
- `availability_claim_allowed`: 0

## Mensagem curta para LC Hermes

A resposta correta para esse alerta é:

> Não aprovar reposição automática ainda. O produto vendido existe no Shopify/GMC, mas está sem identidade operacional: variant `48283857780958` não tem SKU, barcode, metafield ou vínculo Tiny/Stock OS. A DB local também não resolve product/variant/handle/título. Classificar como `IDENTITY_GAP_BLOCKS_STOCK_DECISION` e abrir pendência para lk-stock encontrar ou confirmar o código Tiny correto antes de qualquer decisão de reposição.

## Onde fica documentado

`areas/operacoes/handoffs/handoff-lk-stock-identity-gap-meia-saint-studio-pima-branco-20260612T002048Z.md`

## Backfill funcional — Handoff + Reminder OS (2026-06-12T19:01:04Z)

- Agente/profile: Hermes Agent default / backfill local de handoff funcional
- Pedido original: Corrigir handoffs recentes que estavam como documentação passiva, sem transferência operacional verificável.
- Status: scheduled_check; handoff normalizado retroativamente para contrato funcional.
- Fontes/evidência: `areas/operacoes/handoffs/handoff-lk-stock-identity-gap-meia-saint-studio-pima-branco-20260612T002048Z.md`; `reports/handoff-functionality/handoff-functionality-2026-06-12.json`; ledger Reminder OS quando aplicável.
- Output artifact: este próprio handoff atualizado com bloco canônico de continuidade.
- Aprovação Lucas: autorização explícita no Telegram — “CORRIGIR POR FAVOR” — limitada a correção local/documental e Reminder OS; sem aprovação para writes externos/runtime.
- Writes externos: nenhum; 0 Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/prod/runtime writes.
- Reminder OS loop needed: no
- Reminder OS owner: [LK] Estoque / profile lk-stock
- Reminder OS next action: Validar evidência read-only de estoque/disponibilidade usando Stock OS/Tiny conforme regra LK; devolver confirmado/não confirmado/divergente sem Shopify/Tiny writes.
- Reminder OS review trigger: Revisar no próximo ciclo LK Stock ou quando Lucas pedir status de estoque/disponibilidade.
- Evidence: areas/operacoes/handoffs/handoff-lk-stock-identity-gap-meia-saint-studio-pima-branco-20260612T002048Z.md

## Reminder OS closure — 2026-06-12

- Status: expired/closed by Lucas request.
- Reason: conservative backfill loop reviewed; no longer treated as active pending work.
- Writes externos: 0.
- Reminder OS loop needed: no
- Evidence: areas/operacoes/reminder-os/reminders.jsonl
