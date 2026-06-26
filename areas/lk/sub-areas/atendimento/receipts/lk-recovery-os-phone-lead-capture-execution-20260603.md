# LK Recovery OS — handoff captação telefone/leads pré-checkout

Data: 2026-06-03
Escopo: execução read-only/local após Lucas dizer “Então vamos fazer seguir”.
Status: `audit_done_local_mvp_ready_approval_needed_for_writes`

## O que foi feito

1. Audit read-only do fallback DB para medir funil pré-checkout → telefone.
2. Criado MVP local de métrica read-only:
   - `/opt/data/lk-recovery-os/scripts/lk_recovery_os_phone_capture_audit.py`
   - `/opt/data/lk-recovery-os/tests/test_phone_capture_audit_script.py`
3. Criado plano faseado:
   - `/opt/data/lk-recovery-os/docs/plans/2026-06-03-phone-lead-capture-plan.md`
4. Nenhum write externo em Shopify/Klaviyo/Chatwoot/WhatsApp.
5. Nenhum envio ao cliente.

## Evidência 24h — fallback DB

- `storefront_events`: 8.929
- `with_klaviyo_hint`: 8.929
- `with_cart`: 3.259
- `with_email_hash`: 48
- `with_phone_hash`: 1
- `cart_clusters_with_phone`: 0
- `candidates`: 125
- `candidates_with_cart`: 125
- `candidates_with_phone`: 0

Eventos:

- `identity_update`: 4.782; with_phone_hash 1.
- `view_product`: 3.925; with_cart 3.036; with_email_hash 9; with_phone_hash 0.
- `cart_update`: 112; with_cart 112; with_email_hash 9.
- `cart_view`: 87; with_cart 87; with_email_hash 4.
- `add_to_cart`: 23; with_cart 23; with_email_hash 1.
- `begin_checkout`: 1; with_cart 1.

Identity links:

- `klaviyo_profile_id`: 4.933; with_phone 1.288; with_email 4.932.
- `email_hash`: 4.932; with_phone 1.288.
- `cart_token`: 1.874; with_phone 0; with_email 6.
- `phone_hash`: 1.284.

## Interpretação

- O Recovery OS captura bastante tráfego/carrinho/cookie Klaviyo.
- Existem muitos perfis/links com telefone no grafo de identidade.
- O gargalo atual é o join: cart_token recente não está caindo no mesmo cluster de telefone.
- `recovery_candidates` estão sendo criados com carrinho/produto, mas sem telefone, então não são acionáveis para WhatsApp.

## Recomendação técnica

Próximo bloco aprovado deveria ser:

1. TDD no Worker para reproduzir o cenário `cart_token + kla_cookie/profile + Klaviyo phone`.
2. Corrigir/fortalecer stitching/backwardStitch até `cart_clusters_with_phone > 0` em eventos live.
3. Adicionar enriquecimento server-side por e-mail/customer/profile quando contato parcial existir.
4. Só depois preparar CTAs de microconversão no tema/dev:
   - `Enviar carrinho para meu WhatsApp`
   - `Consultar tamanho com a Elle`
   - `Avisar tamanho/preço`
5. Manter live sends desligados até aprovação separada.

## Verificação local

Comando rodado:

```bash
python3 tests/test_phone_capture_audit_script.py
python3 scripts/lk_recovery_os_phone_capture_audit.py --hours 24 --run-ssh
```

Resultado:

- `Ran 2 tests` / `OK`.
- Audit read-only executado com sucesso.

## Pendências/approval

Requer aprovação explícita antes de:

- alterar Worker em produção;
- alterar theme/pixel Shopify, mesmo em dev theme;
- consultar/mutar Klaviyo além de lookup seguro já escopado;
- criar/enviar WhatsApp/Chatwoot real;
- ativar `LK_LIVE_SEND_ENABLED` ou canal de envio.
