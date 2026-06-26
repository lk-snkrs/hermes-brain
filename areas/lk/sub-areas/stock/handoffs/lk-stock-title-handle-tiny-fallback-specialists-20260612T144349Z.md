# Handoff curto — fallback Tiny por título/handle oficial no LK Stock

- Data: 2026-06-12T14:43:49Z
- Origem: Mesa COO — decisão aprovada por Lucas (`Fazer`)
- Dono primário: `[LK] Estoque Loja Física` / `lk-stock`
- Donos informados: Hermes Geral, lk-growth, lk-shopify, lk-ops, lk-trends, Atendimento, Growth/SEO/CRO, Klaviyo/relatórios
- Writes externos: `0`
- Tiny write: `0`
- Shopify write: `0`
- Compra/reserva/promessa externa: `0`

## Regra oficial

Antes de concluir `sem estoque`, `not_found` ou `identity_gap` para produto LK cuja identidade Shopify/Stock OS não é confiável, `lk-stock` deve tentar fallback Tiny read-only por título/handle normalizado.

## Quando acionar

Aplicar quando houver qualquer uma destas lacunas:

- SKU Shopify vazio/ausente;
- barcode/metafield/código Tiny ausente;
- variante genérica (`Default Title`);
- Stock OS DB sem alias/crosswalk consultável;
- busca por variant_id/handle/título sem linha estável.

## Sequência para `lk-stock`

1. Consultar primeiro Stock OS DB local/hot path.
2. Se a falha for identidade ausente/ambígua, classificar como `identity_missing_needs_title_fallback`, não como `sem estoque`.
3. Buscar Tiny read-only por título/handle normalizado.
4. Para candidato exato/alta confiança, chamar `produto.obter.estoque` read-only.
5. Considerar somente depósito `LK | CONTROLE ESTOQUE`.
6. Responder em duas camadas:
   - estoque interno via `fact_tiny_stock`;
   - identidade operacional resolvida ou ainda pendente.
7. Se houver saldo mas identidade seguir quebrada, manter: `local_consult_safe=1`, `identity_resolved_safe=0`, `public_availability_safe=0`, `availability_claim_allowed=0`.

## Regra para especialistas não-donos

Não concluir “sem estoque” por conta própria quando Shopify/Stock OS não acharem identidade. Não consultar Tiny diretamente fora de `lk-stock`. Encaminhar para `lk-stock` com título, handle, variant_id, SKU/tamanho se houver e contexto.

Copy recomendado:

```text
📦 Estoque atual: identidade não resolvida no Stock OS — encaminhar para lk-stock aplicar fallback Tiny read-only por título/handle antes de concluir sem estoque.
```

## Artefatos verificados

- Profile runtime: `/opt/data/profiles/lk-stock/AGENTS.md`
- Skill profile `lk-stock`: `/opt/data/profiles/lk-stock/skills/productivity/lk-stock/SKILL.md`
- Referência profile: `/opt/data/profiles/lk-stock/skills/productivity/lk-stock/references/title-fallback-when-shopify-identity-missing-20260612.md`
- Referência central LK OI: `/opt/data/skills/productivity/lk-operational-intelligence/references/lk-stock-title-handle-tiny-fallback-20260612.md`
- Política central DB local: `/opt/data/skills/productivity/lk-operational-intelligence/references/lk-stock-db-local-primary-query-policy-20260611.md`

## Observação de QA

Durante verificação, a suite local de Stock OS expôs uma regressão antiga no modo dashboard `lookup_stock("all")` do adapter read-only. Corrigido localmente em `areas/lk/sub-areas/stock/scripts/lk_stock_api_adapter.py`; testes específicos e suite Stock OS passaram.

## Backfill funcional — Handoff + Reminder OS (2026-06-12T19:01:04Z)

- Agente/profile: Hermes Agent default / backfill local de handoff funcional
- Pedido original: Corrigir handoffs recentes que estavam como documentação passiva, sem transferência operacional verificável.
- Status: scheduled_check; handoff normalizado retroativamente para contrato funcional.
- Fontes/evidência: `areas/lk/sub-areas/stock/handoffs/lk-stock-title-handle-tiny-fallback-specialists-20260612T144349Z.md`; `reports/handoff-functionality/handoff-functionality-2026-06-12.json`; ledger Reminder OS quando aplicável.
- Output artifact: este próprio handoff atualizado com bloco canônico de continuidade.
- Aprovação Lucas: autorização explícita no Telegram — “CORRIGIR POR FAVOR” — limitada a correção local/documental e Reminder OS; sem aprovação para writes externos/runtime.
- Writes externos: nenhum; 0 Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/prod/runtime writes.
- Reminder OS loop needed: no
- Reminder OS owner: [LK] Estoque / profile lk-stock
- Reminder OS next action: Validar evidência read-only de estoque/disponibilidade usando Stock OS/Tiny conforme regra LK; devolver confirmado/não confirmado/divergente sem Shopify/Tiny writes.
- Reminder OS review trigger: Revisar no próximo ciclo LK Stock ou quando Lucas pedir status de estoque/disponibilidade.
- Evidence: areas/lk/sub-areas/stock/handoffs/lk-stock-title-handle-tiny-fallback-specialists-20260612T144349Z.md

## Reminder OS closure — 2026-06-12

- Status: expired/closed by Lucas request.
- Reason: conservative backfill loop reviewed; no longer treated as active pending work.
- Writes externos: 0.
- Reminder OS loop needed: no
- Evidence: areas/operacoes/reminder-os/reminders.jsonl
