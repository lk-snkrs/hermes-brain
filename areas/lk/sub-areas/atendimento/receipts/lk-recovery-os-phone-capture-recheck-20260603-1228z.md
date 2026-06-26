# LK Recovery OS — phone capture live recheck

Data: 2026-06-03 12:28 UTC
Status: `live_events_active_but_phone_cart_candidate_gate_still_zero`

## Pedido

Lucas pediu para o Hermes procurar/verificar se o patch PR27 já gerou evidência live de carrinho/candidato com telefone.

## Comando read-only executado

```bash
python3 scripts/lk_recovery_os_phone_capture_audit.py --hours 24 --run-ssh
python3 scripts/lk_recovery_os_phone_capture_audit.py --hours 1 --run-ssh
date -u +'%Y-%m-%d %H:%M:%S %Z'
```

## Evidência 24h

- `storefront_events`: 9257
- `with_cart`: 3383
- `with_email_hash`: 48
- `with_phone_hash`: 1
- `with_klaviyo_hint`: 9257
- `candidates`: 126
- `candidates_with_cart`: 126
- `cart_clusters_with_phone`: 0
- `candidates_with_phone`: 0

Identity graph 24h:

- `klaviyo_profile_id`: 5000 rows / `with_phone`: 1307 / latest `2026-06-03 12:27:47.649+00`
- `cart_token`: 1950 rows / `with_phone`: 0 / latest `2026-06-03 12:27:37.196+00`
- `phone_hash`: 1303 rows / latest `2026-06-03 12:26:59.362+00`

## Evidência 1h

- `storefront_events`: 962
- `with_cart`: 390
- `with_email_hash`: 2
- `with_phone_hash`: 0
- `with_klaviyo_hint`: 962
- `candidates`: 7
- `candidates_with_cart`: 7
- `cart_clusters_with_phone`: 0
- `candidates_with_phone`: 0

Identity graph 1h:

- `klaviyo_profile_id`: 566 rows / `with_phone`: 133 / latest `2026-06-03 12:27:54.667+00`
- `cart_token`: 240 rows / `with_phone`: 0 / latest `2026-06-03 12:27:51.38+00`
- `phone_hash`: 133 rows / latest `2026-06-03 12:26:59.362+00`

## Interpretação

O tráfego live continua entrando após o deploy e há telefone no grafo Klaviyo/Shopify. Porém o gate de WhatsApp recovery ainda não passou: nenhum cluster com `cart_token` herdou telefone e nenhum `recovery_candidate` recente tem telefone.

Isso mantém o status como: patch técnico deployado/testado, mas não validado em produção por evento live acionável.

## Segurança

Nenhuma escrita externa/produção foi feita. Consulta foi read-only via SSH/psql. Envios ao cliente continuam fora de escopo/desligados conforme receipt PR27.
