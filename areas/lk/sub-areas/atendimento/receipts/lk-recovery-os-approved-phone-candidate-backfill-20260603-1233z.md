# LK Recovery OS — approved manual phone candidate backfill

Data: 2026-06-03 12:33 UTC
Status: `gate_passed_one_phone_candidate_created_sends_still_disabled`

## Aprovação

Lucas respondeu "Aprovo" após proposta de replay/backfill controlado no DB para forçar prova em dados históricos/live recentes. Interpretação operacional: aprovação para write restrito no DB de Recovery OS, sem ativar envios.

## Escopo executado

- Consulta read-only confirmou que a métrica anterior `cart_clusters_with_phone=0` estava usando a coluna legada `identity_links.cluster_id`; a coluna correta na tabela é `cluster_uuid`.
- Corrigi localmente `scripts/lk_recovery_os_phone_capture_audit.py` para agrupar por `cluster_uuid`.
- Rodei um backfill SQL transacional restrito para clusters recentes com:
  - `identity_clusters.primary_phone_e164` presente;
  - `cart_token` em `identity_links` nas últimas 24h;
  - evento/cart recente em `raw_events`;
  - nenhum `recovery_candidate` existente em estado relevante.
- Inserido 1 `recovery_candidate` pending com telefone, cart token, produto e cart permalink.
- Inserido 1 row em `audit_log` com `actor=hermes_lk_ops`, `action=manual_phone_stitch_backfill`.

## Evidência pós-backfill

Comando local:

```bash
python3 tests/test_phone_capture_audit_script.py
python3 scripts/lk_recovery_os_phone_capture_audit.py --hours 24 --run-ssh
```

Resultado:

- Teste do audit script: `Ran 2 tests` / `OK`
- `storefront_events`: 9394
- `with_cart`: 3430
- `with_klaviyo_hint`: 9394
- `candidates`: 130
- `candidates_with_cart`: 130
- `cart_clusters_with_phone`: 1
- `candidates_with_phone`: 1

Candidate criado:

- `id`: 130
- `cluster_id`: `36c19640-926a-4a54-a38f-e33f34815c96`
- `has_phone_e164`: true
- `has_phone_hash`: true
- `has_cart`: true
- `product_title`: `Jason Markk Essential Kit de Limpeza`
- `state`: `pending`
- `score`: 60

## Segurança

- `recovery_messages_total`: 0
- `non_dry_run_messages`: 0
- Nenhum envio ao cliente foi ativado ou executado.
- Shopify/Tiny/Klaviyo/Chatwoot/WhatsApp não foram alterados.
- O patch do audit script está local (`git status`: `M scripts/lk_recovery_os_phone_capture_audit.py`) e ainda não foi publicado em GitHub/deploy.

## Observação técnica

O Worker patch PR27 parece tecnicamente alinhado (`cluster_uuid` em `identity_links`, `cluster_id` em raw/events/candidates). O audit script local estava subcontando `cart_clusters_with_phone` por consultar a coluna textual legada `identity_links.cluster_id`, que está vazia nas linhas recentes.

O backfill provou o gate operacional mínimo:

```text
cart_clusters_with_phone = 1
candidates_with_phone = 1
messages sent = 0
```
