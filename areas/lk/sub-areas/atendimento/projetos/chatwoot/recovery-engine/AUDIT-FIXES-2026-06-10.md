# Audit 10/jun/2026 + Correções ("corrigir tudo")

Audit executado por 3 agentes paralelos (código Ruby/Vue · dados Postgres · integrações Shopify/Evolution/Klaviyo), 100% read-only. Relatório completo entregue ao Lucas (`Audit-Recuperacao-LK-2026-06-10.html`). Em seguida, TODAS as correções críticas/altas foram implementadas e deployadas em `v2-recovery17`.

## Críticos encontrados → corrigidos
1. **Resposta de agente nunca chegava ao cliente** — webhook_url da inbox 3 = `http://localhost:8080/chatwoot/webhook/Pessoal` (SERVER_URL errado + instância antiga). 393 msgs perdidas em 40min de log. FIX: URL corrigida no banco p/ Railway/LK Flagship + Lucas setou SERVER_URL no Railway. Validado: status sent + read receipts.
2. **Broadcast "simulado" enviava REAL** via Evolution (gating desatualizado). FIX: gating alinhado; amostra simulada só nota.
3. **Ciclo do pedido sem idempotência** (fulfillments/update re-dispara) → mensagens duplicadas quando templates preenchidos. FIX: RecoveryEventLog dedup por (pedido, tipo) + followup 1x.
4. **Race nos toques** (guard não-atômico) → toque duplicado possível. FIX: claim atômico update_all.
5. **Webhook fora de ordem** → lembrete pra quem já comprou. FIX: registro de compras + checagem no momento do envio.
6. **Duplo-enqueue de broadcast** → envio em massa 2x. FIX: recusa por status + claim atômico + supressão gravada antes do envio.

## Altos → corrigidos
- Nome de template não resolvido ia LITERAL pro cliente → guard (não envia + warn). JSON malformado idem.
- Dedup em FileStore volátil por container → **Redis cache store**.
- UI mentia (badge "Ativo" e tempos hardcoded) → derivados da config real.
- `/segments` 500 (varchar >= int) → cast NULLIF::numeric.
- Token Klaviyo fraco (lkdemo123) e aceito via query string → rotacionado, só header.
- Amostra real de broadcast re-enviada no disparo em massa → last_broadcast_at na amostra.
- Segredos em claro no GET settings → mascarados (••••+4, update ignora máscara).

## Médios corrigidos
Klaviyo capture via dispatcher (ganhou caminho Evolution + sanitização) · contador de broadcast não herda amostra · status `notified` ao fim da régua · delays sempre ordenados · telefone mascarado em logs · ENTRY_RE aceita acentos · endpoint `test` responde `simulated` preciso.

## Pendências conhecidas (NÃO corrigidas — backlog)
- BroadcastSendJob monolítico (job de horas, sem retomada; morre em deploy → status 'sending' eterno).
- Customer 360: sem tratamento de 429/timeout (painel mostra chave i18n literal); matching email-OU-phone limit:1 (risco de mostrar pedidos de outro cliente); moeda formatada USD/en.
- RFM sobreposto (winback=66% da base); 1.218 contatos sync sem pedido fora de segmento.
- Cupons DISCOUNT_TOUCH_1/2/3 e templates Browse/Checkout/Winback: UI existe, backend não lê ("planejado").
- Webhook Shopify 200-sempre (evento com erro é perdido sem retry).
- 1 conversa nova por toque (avaliar lock_to_single_conversation na inbox 3).
- Captura de telefone no checkout (gargalo: 78,6% dos carrinhos inalcançáveis) — 3 alavancas documentadas em captura-telefone/.
- Telefones de carrinho sem DDI (51/100) — dispatcher normaliza :BR, mas vale normalizar no save.

## Extra implementado na mesma sessão
- **Interpolação de placeholders** nos templates (`{{nome}} {{produto}} {{valor}} {{link}} {{pedido}} {{rastreio}}`) com limpeza elegante de ausentes — base para o sonho do Lucas: conteúdo por tipo de produto (estilo AI Product Content do BiteSpeed).
- Biblioteca de templates `nome :: texto` (multilinha) + 8 templates redigidos no tom LK, aprovados e testados.
