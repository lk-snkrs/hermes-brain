# Handoff — LK Stock fallback Tiny por título/handle oficializado

- Data: 2026-06-12T10:27:11Z
- Origem: decisão Mesa COO aprovada por Lucas (`Fazer`)
- Dono primário: `[LK] Estoque Loja Física` / `lk-stock`
- Donos informados: Hermes Geral, lk-growth, lk-shopify, lk-ops, lk-trends, Atendimento, Growth/SEO/CRO, Klaviyo/relatórios
- Writes externos: `0`
- Tiny write: `0`
- Shopify write: `0`
- Compra/reserva/contato externo: `0`

## Regra oficial

Antes de concluir `sem estoque`, `not_found` ou `identity_gap` para produto LK cuja identidade Shopify/Stock OS não é confiável, `lk-stock` deve tentar fallback Tiny read-only por título/handle normalizado.

Isso vale especialmente quando:

- SKU Shopify está vazio;
- barcode/metafield/código Tiny estão ausentes;
- variante é genérica (`Default Title`);
- Stock OS DB não tem alias/crosswalk consultável;
- a busca por variant_id/handle/título não encontra linha estável.

## Sequência operacional

1. `lk-stock` consulta primeiro a Stock OS DB local/hot path.
2. Se o blocker for identidade ausente/ambígua, classifica como `identity_missing_needs_title_fallback`, não como estoque inexistente.
3. `lk-stock` pesquisa Tiny read-only por título/handle normalizado.
4. Para candidato exato/alta confiança, chama `produto.obter.estoque` read-only.
5. Usa apenas depósito `LK | CONTROLE ESTOQUE`.
6. Responde em duas camadas:
   - estoque interno via `fact_tiny_stock`;
   - identidade operacional ainda resolvida ou pendente.
7. Se estoque existir mas identidade seguir quebrada, manter guardrails: `local_consult_safe=1`, `identity_resolved_safe=0`, `public_availability_safe=0`, `availability_claim_allowed=0` até alias/cadastro.

## Copy para especialistas não-donos

```text
📦 Estoque atual: identidade não resolvida no Stock OS — encaminhar para lk-stock aplicar fallback Tiny read-only por título/handle antes de concluir sem estoque.
```

## Caso que originou a regra

`Meia Saint Studio Pima Branco` quase virou falso `sem estoque`: Shopify/Stock OS não tinham identidade confiável, mas Tiny provou saldo no depósito `LK | CONTROLE ESTOQUE`. Conclusão correta: estoque interno encontrado via fallback Tiny; automação/pronta entrega pública seguem bloqueadas até vínculo operacional.

## Artefatos atualizados/verificados

- Profile runtime rule updated: `/opt/data/profiles/lk-stock/AGENTS.md`
- Skill `lk-stock` do profile especialista já contém a regra e referência: `/opt/data/profiles/lk-stock/skills/productivity/lk-stock/SKILL.md`
- Referência do profile `lk-stock`: `/opt/data/profiles/lk-stock/skills/productivity/lk-stock/references/title-fallback-when-shopify-identity-missing-20260612.md`
- Handoff/regra no skill central LK Operational Intelligence: `/opt/data/skills/productivity/lk-operational-intelligence/references/lk-stock-title-handle-tiny-fallback-20260612.md`
- Política DB local central atualizada: `/opt/data/skills/productivity/lk-operational-intelligence/references/lk-stock-db-local-primary-query-policy-20260611.md`
- Roteamento para scripts/agentes não-donos atualizado: `/opt/data/skills/productivity/multiempresa-routing-lucas/references/lk-stock-routing-applies-to-scripts-20260611.md`

## Não autorizado por esta decisão

Esta decisão não autoriza Tiny/Shopify writes, compra, reserva, contato com cliente/fornecedor, WhatsApp/Klaviyo/campanha, cron/gateway novo ou promessa pública de disponibilidade.

## Backfill funcional — Handoff + Reminder OS (2026-06-12T19:01:04Z)

- Agente/profile: Hermes Agent default / backfill local de handoff funcional
- Pedido original: Corrigir handoffs recentes que estavam como documentação passiva, sem transferência operacional verificável.
- Status: scheduled_check; handoff normalizado retroativamente para contrato funcional.
- Fontes/evidência: `areas/lk/sub-areas/stock/handoffs/lk-stock-title-handle-tiny-fallback-official-20260612T102711Z.md`; `reports/handoff-functionality/handoff-functionality-2026-06-12.json`; ledger Reminder OS quando aplicável.
- Output artifact: este próprio handoff atualizado com bloco canônico de continuidade.
- Aprovação Lucas: autorização explícita no Telegram — “CORRIGIR POR FAVOR” — limitada a correção local/documental e Reminder OS; sem aprovação para writes externos/runtime.
- Writes externos: nenhum; 0 Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/prod/runtime writes.
- Reminder OS loop needed: no
- Reminder OS owner: [LK] Estoque / profile lk-stock
- Reminder OS next action: Validar evidência read-only de estoque/disponibilidade usando Stock OS/Tiny conforme regra LK; devolver confirmado/não confirmado/divergente sem Shopify/Tiny writes.
- Reminder OS review trigger: Revisar no próximo ciclo LK Stock ou quando Lucas pedir status de estoque/disponibilidade.
- Evidence: areas/lk/sub-areas/stock/handoffs/lk-stock-title-handle-tiny-fallback-official-20260612T102711Z.md

## Reminder OS closure — 2026-06-12

- Status: expired/closed by Lucas request.
- Reason: conservative backfill loop reviewed; no longer treated as active pending work.
- Writes externos: 0.
- Reminder OS loop needed: no
- Evidence: areas/operacoes/reminder-os/reminders.jsonl
