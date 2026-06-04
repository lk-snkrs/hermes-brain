# LK Recovery OS — post score-gate deploy monitor

Data: 2026-06-03 13:24 UTC
Tipo: read-only monitor pós-deploy

## Contexto

Após aprovação de Lucas, foi removida a trava de score comportamental como gate de elegibilidade de carrinho abandonado. Regra ativa: score serve para priorização/analytics; carrinho abandonado com identidade contactável deve entrar no fluxo salvo safety gates.

Worker deployado previamente:

- Worker: `lk-recovery`
- Version ID: `4e1096e6-583a-4fcb-a179-68cb16264f3e`
- Main SHA local: `9b1b494`

## Verificações executadas

### Runtime

- Healthcheck Worker: HTTP 200
- Resposta: `{"service":"lk-recovery","status":"ok"}`
- `CHECKOUT_BUFFER_KV`: `[]` sem backlog
- Repo local: detached HEAD em `9b1b494`

### Flags de segurança observadas em `wrangler.toml`

- `LK_RECOVERY_DRY_RUN = "true"`
- `LK_LIVE_SEND_ENABLED = "false"`
- `LK_WHATSAPP_SEND_ENABLED = "false"`
- `LK_EMAIL_SEND_ENABLED = "false"`
- `LK_CHATWOOT_INTERNAL_ONLY = "true"`
- `LK_SCORING_ENABLED = "true"`
- `LK_SCORING_MIN_SCORE = "50"`

### DB read-only — janela 2h

Audit script: `uv run python scripts/lk_recovery_os_phone_capture_audit.py --hours 2 --run-ssh`

Principais métricas:

- `storefront_events`: 1866
- `with_cart`: 709
- `with_email_hash`: 24
- `with_phone_hash`: 0
- `with_klaviyo_hint`: 1866
- `cart_clusters_with_phone`: 1
- `candidates`: 15
- `candidates_with_cart`: 15
- `candidates_with_phone`: 1

### DB read-only — desde deploy ~13:18 UTC

- `raw_storefront_since_deploy`: 72
- `raw storefront with_cart`: 18
- `raw storefront with_email_hash`: 0
- `raw storefront with_phone_hash`: 0
- `candidates_since_deploy`: 1
- `score_under_50`: 0
- `with_phone`: 0
- `with_cart`: 1
- `latest_candidate`: 2026-06-03 13:20:01 UTC

Candidato pós-deploy observado:

- id `134`
- state `pending`
- score `50`
- has_phone `false`
- has_cart `true`
- produto: `Tênis Nike Air Jordan 1 Low OG Obsidian UNC Azul`

### Segurança de envios

- `recovery_messages_total`: 0
- `non_dry_run_messages`: 0

## Veredito

- Runtime saudável: sim.
- Buffer sem backlog: sim.
- Captura storefront ativa pós-deploy: sim.
- Candidatos continuam sendo criados: sim, 1 candidato pós-deploy.
- Candidato pós-deploy contactável/telefone: ainda não.
- Evidência de candidato score < 50 pós-deploy: ainda não apareceu organicamente.
- Evidência geral 2h de phone candidate: sim, 1 candidato com telefone e 1 cluster cart+phone.
- Envios reais: desligados/zero.

## Próximo gate

Para chamar a remoção do score gate de validada em produção por evento orgânico, ainda falta observar pelo menos um candidato contactável com score abaixo de `LK_SCORING_MIN_SCORE` ou outro evento claramente bloqueado antes pelo score que agora passe a `pending` sem envio real.
