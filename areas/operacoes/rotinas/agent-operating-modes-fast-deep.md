# Agent Operating Modes — fast lane, deep work e handoff

Status: rotina local v0.1
Criado em: 2026-06-10T14:13:27Z

## Objetivo

Padronizar como Hermes e especialistas escolhem o modo operacional de cada pedido, evitando que chat rápido vire auditoria pesada ou que ação sensível seja executada sem packet.

## Modos

1. **Fast lane**
   - Resposta curta, baixo risco, pouca ferramenta.
   - Usar para: confirmação, status simples, pergunta com fonte já disponível, próxima decisão Mesa já registrada.
   - Evitar: pesquisa ampla, código, runtime, produção, financeiro, cliente/fornecedor.

2. **Deep work**
   - Auditoria, investigação, código, relatório, plano, comparação.
   - Deve produzir artefato local/receipt quando material.
   - Preferir background/subagentes quando longo.

3. **no_agent watchdog**
   - Script recorrente com contrato `rc=0 + stdout vazio = OK/silencioso`.
   - Telegram só recebe stdout anômalo ou erro.

4. **Approval packet**
   - Para A3/A4: produção, Shopify/Tiny/GMC/Klaviyo/WhatsApp/email, runtime/gateway/Docker/VPS/provider/secrets.
   - `Fazer` só executa o safe_action descrito no card; se o card prometeu packet/preview, não executa produção.

5. **Handoff/delegation**
   - Quando outro agente/especialista é dono.
   - Deve incluir dono, escopo, evidência, limites, approval pendente e próximo passo.

## Regra de decisão

- Se há risco externo/runtime: approval packet.
- Se é local/documental e claro: executar.
- Se é longo mas seguro: deep work/background, silent-OK até resultado.
- Se é sequência Mesa: usar Decision Sequence Ledger antes de responder.
- Se envolve especialista permanente: handoff com receipt.

## Métrica de qualidade

- Fast lane responde rápido sem perder precisão.
- Deep work gera artefato verificável.
- Watchdog saudável não fala.
- Approval packet não vira loop depois de aprovação escopada.
- Handoff permite especialista retomar sem session_search.
