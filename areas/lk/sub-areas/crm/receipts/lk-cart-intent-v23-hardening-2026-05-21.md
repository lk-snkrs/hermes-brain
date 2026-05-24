# LK Cart Intent v2.3 — hardening n8n

Data: 2026-05-21 00:06 UTC
Workflow: `XLODECE4MvNRNCQ9` — `LK - Cart Intent 30min Full Funnel - Crisp (ATIVO)`
Aprovado por: Lucas no Telegram (`perfeito corrigir`)

## Alterações aplicadas

1. Adicionada trilha imediata de identidade antes do delay de 30min:
   - `LK Cart Intent Webhook`
   - `Crisp REST Get Conversation Meta - Identity Immediate`
   - `Atualizar identity index imediato`

2. A trilha imediata:
   - consulta Crisp REST com Website Token;
   - atualiza `staticData.identityIndex` com phone/e-mail quando disponível;
   - registra `identityAuditLog` técnico;
   - retorna `[]`, portanto não envia WhatsApp.

3. Mantido envio somente na trilha com delay:
   - `Wait 30 min`
   - `Crisp REST Get Conversation Meta`
   - `Filtrar cart intent elegíveis`
   - send Crisp apenas se elegível.

4. Adicionada trava por telefone:
   - razão de skip: `phone_frequency_cap_96h`;
   - objetivo: evitar múltiplos cart-intent para o mesmo telefone em janela curta.

5. Atualizado label interno:
   - `cart_intent_30min_v2_3_crisp_rest_identity`.

## Readback / verificação

- Workflow ativo: `true`
- `versionId`: `b3bc2ecb-1f7e-4849-a0a4-2f240cb0c948`
- `activeVersionId`: `b3bc2ecb-1f7e-4849-a0a4-2f240cb0c948`
- versão publicada corresponde à atual: `true`
- Edge webhook:
  - `Wait 30 min`
  - `Preparar log cart intent evento`
  - `Crisp REST Get Conversation Meta - Identity Immediate`
- Edge imediato:
  - `Crisp REST Get Conversation Meta - Identity Immediate` → `Atualizar identity index imediato`
- Edge delay:
  - `Wait 30 min` → `Crisp REST Get Conversation Meta`
- Filtro contém `phone_frequency_cap_96h`: `true`
- Filtro contém label v2.3: `true`

## Backup / rollback

Backup bruto do workflow antes da alteração:

`/opt/data/hermes_bruno_ingest/.secrets/lk-cart-intent-v23-hardening-20260521T000559Z/workflow_before.json`

Script aplicado:

`/opt/data/hermes_bruno_ingest/scripts/lk_cart_intent_v23_hardening_20260521.py`

Rollback seguro: restaurar o JSON de backup via API n8n ou remover os dois nodes imediatos e reverter o Code node `Filtrar cart intent elegíveis` com `filter_before.js` do mesmo diretório.

## Observações

- Nenhum teste WhatsApp foi disparado.
- Nenhum cliente foi contactado por esta ação.
- A alteração é customer-facing apenas de forma defensiva: reduz risco de múltiplos envios e melhora resolução de identidade antes do envio.
- Supabase 30min pós/verificação tinha eventos v2.3 e `identity_update`, mas ainda sem telefone/e-mail real capturado no período observado.
