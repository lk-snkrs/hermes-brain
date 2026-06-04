# LK Recovery OS — Shopify recheck fallback deploy

Data: 2026-06-03 14:11 UTC
Status: `deployed_safety_flags_on_needs_next_t1_live_signal`

## Aprovação

Lucas respondeu: `aprovado` após o pacote para publicar o patch local `fix/recovery-t1-shopify-recheck-fallback`.

## Escopo executado

Publicação do patch do Worker/T1 para robustez do recheck Shopify:

- Branch: `fix/recovery-t1-shopify-recheck-fallback`
- PR: #31
- Merge squash SHA: `2b0e4f309b0745c68027a60e0aced76757e9d729`
- Worker: `lk-recovery`
- Version ID deployado: `a8be1c85-bb87-4858-92a0-cfe1e55a22f6`

## Interpretação operacional

A Shopify não foi tratada como culpada. A causa técnica corrigida foi a rigidez do Worker/T1 no recheck de orders: se o token primário não conseguisse consultar orders, o T1 retornava `unable_to_check` e falhava fechado com `t1_order_recheck_unavailable`.

O patch faz o T1 tentar tokens únicos em ordem:

1. `SHOPIFY_ACCESS_TOKEN`
2. `SHOPIFY_ADMIN_TOKEN`

Se um token retorna HTTP não OK, tenta o próximo. O fail-closed permanece: se todos os tokens falharem, continua retornando `unable_to_check`.

## Arquivos alterados

- `workers/recovery-os/src/t1.ts`
  - `alreadyOrderedAfterCheckout()` exportada/testável.
  - fallback sequencial para tokens Shopify.
  - helper `uniqueTruthy()`.
- `workers/recovery-os/src/types.ts`
  - `SHOPIFY_ADMIN_TOKEN?: string` na interface `Env`.
- `workers/recovery-os/tests/t1_scoring_eligibility.test.ts`
  - teste de fallback quando `SHOPIFY_ACCESS_TOKEN` falha e `SHOPIFY_ADMIN_TOKEN` lê orders.

## Testes

Pré-deploy em `main`:

```text
npm test
Test Files 12 passed (12)
Tests 55 passed (55)
```

CI GitHub:

```text
PR #31 / branch fix/recovery-t1-shopify-recheck-fallback
workflow run 26889703825: completed / success
commit status: success
mergeable_state: clean
```

## Deploy

Comando usado no diretório `workers/recovery-os`:

```text
npx -y node@22 node_modules/wrangler/bin/wrangler.js deploy
```

Resultado:

```text
Uploaded lk-recovery
Deployed lk-recovery triggers
custom domain: recovery.lucascimino.com
schedule: */10 * * * *
Current Version ID: a8be1c85-bb87-4858-92a0-cfe1e55a22f6
```

## Safety flags observadas no deploy

```text
LK_RECOVERY_DRY_RUN=true
LK_CHATWOOT_INTERNAL_ONLY=true
LK_LIVE_SEND_ENABLED=false
LK_WHATSAPP_SEND_ENABLED=false
LK_EMAIL_SEND_ENABLED=false
LK_RECOVERY_PAUSE=false
```

Nenhuma alteração de Shopify, Chatwoot, DB schema, secrets ou flags de envio foi feita.

## Pós-deploy

Worker health:

```text
https://recovery.lucascimino.com/healthz
{"service":"lk-recovery","status":"ok"}
HTTP 200
```

DB fallback health:

```text
https://recovery-db.lucascimino.com/healthz
{"service":"lk-recovery-db","status":"ok"}
HTTP 200
```

Checkout buffer KV:

```text
[]
```

DB safety:

```text
recovery_messages_total = 0
non_dry_run_messages = 0
```

Audit T1 desde deploy aproximado (`2026-06-03 14:00:30+00`) até `14:11:08Z`:

```text
0 rows para ações T1 monitoradas, incluindo t1_order_recheck_unavailable
```

Observação: antes do deploy havia `t1_order_recheck_unavailable` acumulado no histórico recente, último observado `2026-06-03 13:52:59.982+00`. Após deploy ainda falta um novo ciclo/evento T1 processável para provar positivamente o fallback em produção.

## Veredito

Patch correto foi publicado e deployado com segurança. O próximo critério de validação operacional é observar novo ciclo T1/candidato contactável após o deploy:

- `t1_order_recheck_unavailable` não deve voltar a crescer por falha de token/recheck;
- candidato contactável deve alcançar evidência segura em dry-run/internal-only;
- envios reais devem permanecer zerados até aprovação separada.
