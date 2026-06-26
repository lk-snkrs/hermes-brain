# LK Recovery OS — recheck hypothesis corrected: Shopify is correct

Data: 2026-06-03 13:50 UTC
Status: `local_patch_ready_needs_approval_for_external_push_deploy`

## Trigger

Lucas respondeu: `seguir, o shopify esta certo`.

Interpretação: retirar a culpa da Shopify/loja e reabrir a hipótese. Não executar alteração externa/produção sem approval packet explícito.

## Correção de hipótese

A Shopify/loja pode estar correta. O problema isolado é no contrato/robustez do Worker T1:

- O T1 chama `alreadyOrderedAfterCheckout()` antes de qualquer ação.
- Se esse recheck não conseguir consultar orders, retorna `unable_to_check`.
- O runner falha fechado e registra `t1_order_recheck_unavailable`, sem mandar e sem contexto útil.
- O audit registrou 21 ocorrências em 48h.

O achado anterior contra Doppler não deve ser comunicado como “Shopify errado”. A formulação correta é: **o Worker estava rígido demais em um único secret/env (`SHOPIFY_ACCESS_TOKEN`) e não tentava o token admin alternativo disponível (`SHOPIFY_ADMIN_TOKEN`) para o recheck de orders**.

## Patch local preparado

Branch local: `fix/recovery-t1-shopify-recheck-fallback`

Arquivos alterados:

- `workers/recovery-os/src/t1.ts`
- `workers/recovery-os/src/types.ts`
- `workers/recovery-os/tests/t1_scoring_eligibility.test.ts`

Comportamento novo:

- `alreadyOrderedAfterCheckout()` agora aceita `SHOPIFY_ADMIN_TOKEN` opcional no Env.
- Para o recheck de orders, tenta tokens únicos em ordem:
  1. `SHOPIFY_ACCESS_TOKEN`
  2. `SHOPIFY_ADMIN_TOKEN`
- Se um token retorna erro HTTP, tenta o próximo.
- Só retorna `unable_to_check` se todos falharem.

## TDD / testes

Foi criado primeiro teste RED:

- `falls back to SHOPIFY_ADMIN_TOKEN when SHOPIFY_ACCESS_TOKEN cannot read orders`

Falha inicial observada:

- `TypeError: alreadyOrderedAfterCheckout is not a function`

Depois do patch:

- Teste específico: `2 passed`
- Full Worker suite: `12 files / 55 tests passed`

## Segurança

Nenhum push, PR, merge, deploy, secret change ou run manual T1 em produção foi executado após esta correção local.

Flags conhecidas continuam como guardrail esperado:

- `LK_RECOVERY_DRY_RUN=true`
- `LK_LIVE_SEND_ENABLED=false`
- `LK_WHATSAPP_SEND_ENABLED=false`
- `LK_EMAIL_SEND_ENABLED=false`

## Próximo approval packet

Se Lucas aprovar explicitamente:

1. Commit local.
2. Push branch.
3. Abrir PR.
4. Merge após CI.
5. Deploy Worker.
6. Pós-deploy: healthcheck, KV buffer, DB safety, e monitorar se `t1_order_recheck_unavailable` para de crescer e se o candidato contactável avança para evidência operacional sem envio live.

Não ativar envio real nem WhatsApp live sem aprovação separada.
