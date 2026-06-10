# Timeline — Chatwoot / Elle / LK Atendimento

## 2026-06-02

- PRD Elle/Chatwoot/Shopify/WhatsApp/transbordo.
- Primeiros receipts de Chatwoot WhatsApp API, token/Doppler, Shopify OAuth/app config, integration connected e feature flags.
- Elle MVP 1C com approval packet para writes internos.
- Diagnóstico e correção de conexão Elle/Chatwoot.
- Pesquisa de lifecycle messaging e Recovery OS + Chatwoot.

## 2026-06-03

- Readiness check Chatwoot.
- Evolution API + Chatwoot guidance/intake.
- WhatsApp campaign capability e feature enabled.
- PRD + plano + implementação do WhatsApp Template Builder.
- Deploy/verificação de templates.
- PRD/event sync Shopify → Chatwoot.
- Sidebar Templates: PRD, handoff, PR package e live validation.
- Reports de import/backfill de telefone Shopify → Chatwoot.

## 2026-06-09

- Diagnósticos read-only Chatwoot/Elle, data services e Chatwoot Cloud.
- Migration pack Elle → Chatwoot Cloud.
- Config dual-target Chatwoot preparada.
- Credenciais/webhook recebidos e dry-run controlado pós-credenciais.
- Smoke test controlado, copiloto interno ativado, canário pós-ativação, observação de evento real e diagnóstico read-only da inbox WhatsApp.

## 2026-06-10

- Camada **PÓS VENDA LK FLAGSHIP** criada/documentada.
- 10 pedidos POS elegíveis registrados como conversas/notas internas.
- State local de idempotência salvo.
- Pasta canônica do projeto Chatwoot criada no Brain.

## 2026-06-10 — Motor de recuperação: audit + corrigir tudo (Claude/Cowork + Lucas)

- Audit 3 frentes (código/dados/integrações) do fork lk-chatwoot → 6 críticos, 6 altos.
- TODOS críticos corrigidos e deployados (`v2-recovery17` + migração recovery_event_logs): webhook Evolution da inbox 3 (resposta de agente estava 100% quebrada), broadcast simulado que enviava real, dedup do ciclo de pedido, claims atômicos, guard de template, Redis cache, Klaviyo header-only, segredos mascarados, UI honesta.
- Incidente "(vazio)" (6 clientes) estancado e causas raiz corrigidas.
- Templates das journeys redigidos (tom LK), gravados e testados no número do Lucas; interpolação {{nome}}/{{produto}}/{{valor}}/{{link}}/{{pedido}}/{{rastreio}} implementada.
- Klaviyo: token rotacionado; flows Checkout Started + Added to Cart apontados pro Chatwoot.
- Decisão Lucas: fluxos permanecem DESLIGADOS até ordem explícita.
- Docs: `projetos/chatwoot/recovery-engine/`.
