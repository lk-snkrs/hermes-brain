# LK Recovery OS — remover score como gate de carrinho abandonado

Data: 2026-06-03T13:08Z
Operador: Hermes lk-ops
Escopo: alteração local no Worker Recovery OS; sem push, sem deploy, sem writes externos, sem envio ao cliente.

## Decisão de negócio do Lucas

Lucas corrigiu a regra: carrinho abandonado não deve depender de score. Todo carrinho abandonado com pessoa conhecida/contactável deve entrar no fluxo de carrinho abandonado. Score fica apenas para priorização/analytics.

## Mudança local implementada

Branch local:

- `fix/abandoned-cart-eligibility-no-score-gate`

Commit local:

- `4eec991 fix(recovery-os): remove score gate from abandoned cart eligibility`

Arquivos alterados:

- `workers/recovery-os/src/scoring.ts`
- `workers/recovery-os/src/t1.ts`
- `workers/recovery-os/tests/scoring_eligibility.test.ts`
- `workers/recovery-os/tests/t1_scoring_eligibility.test.ts`

## Comportamento novo

### Candidate materialization

Antes:

- `score < LK_SCORING_MIN_SCORE` bloqueava criação/atualização de `recovery_candidates`.

Agora:

- `score >= LK_SCORING_MIN_SCORE` ainda cria candidato para preservar comportamento legado de alta intenção;
- **ou** carrinho abandonado + identidade contactável cria candidato mesmo com score baixo/zero.

Eventos de carrinho reconhecidos como sinal de abandono/intenção:

- `add_to_cart`
- `cart_create`
- `cart_update`
- `cart_view`
- `begin_checkout`
- `checkout_started`
- `checkout_contact_info_submitted`

Contato considerado na eligibility:

- `phone_hash` ou `phone_e164` no cluster/evento.

### T1 collection

Antes:

- `collectScoringCandidates` lia `recovery_candidates` com filtro `score >= LK_SCORING_MIN_SCORE`.

Agora:

- remove o filtro de score;
- mantém filtros de segurança/funil: `state=pending`, `phone_e164 not null`, `channel_pref=whatsapp`, recovery URL/cart permalink/produto/imagem, idade mínima;
- ordena por `score.desc` apenas para priorização.

### Produto do carrinho

`pickProduct` agora prioriza também `cart_create`, `cart_update` e `cart_view`, não só `add_to_cart`, evitando perder produto em carrinho real de storefront.

## Testes TDD

RED observado:

- `tests/scoring_eligibility.test.ts` falhou porque `cart_update` com score `0` não criava candidato.
- `tests/t1_scoring_eligibility.test.ts` falhou porque `collectScoringCandidates` não era exportado/continuava preso ao caminho antigo.

GREEN/verificação:

```text
npm test
Test Files  12 passed (12)
Tests       54 passed (54)
```

## Segurança operacional

Não executado:

- push GitHub;
- PR;
- deploy Cloudflare Worker;
- alteração Supabase/PostgREST;
- alteração Shopify/Klaviyo/Chatwoot/WhatsApp;
- live send.

Próximo passo se aprovado explicitamente:

1. push da branch;
2. abrir PR;
3. aguardar CI;
4. merge/deploy Worker sob escopo explícito;
5. pós-deploy: `/healthz`, KV, `recovery_messages_total=0`, e métricas de candidatos com telefone.
