# Fase 2 — LK agents runtime restart + validation (2026-06-25)

Generated at: `2026-06-25T18:31:33.491119+00:00`

## Pedido aprovado

Lucas aprovou a opção 1 após a Fase 1: restart controlado dos gateways LK e validação pós-restart, sem Docker/VPS/Traefik/secrets/prod/external writes.

## Escopo executado

Gateways LK ativos reiniciados:

- `lk-growth`
- `lk-shopify`
- `lk-collection-optimizer`
- `lk-stock`
- `lk-trends`
- `lk-finance`
- `lk-content`
- `lk-ops`

Support profiles mantidos parados porque não eram gateways ativos esperados nesta fase:

- `lk-analyst-readonly`
- `lk-content-reviewer`

## Como foi feito

1. Capturei PIDs/start ticks antes do restart.
2. Encerramento controlado por `SIGTERM` nos 8 gateways LK ativos.
3. Alguns processos não saíram dentro da janela curta e receberam `SIGKILL`; isso ficou limitado aos PIDs dos profiles LK secundários, não Main/default/Docker.
4. Rodei `/opt/data/scripts/hermes_all_gateway_watchdog.py` para restaurar os profiles gerenciados com API/webhook forçados off.
5. Validei live process por `/proc/<pid>/environ` usando `HERMES_HOME` exato.

Evidência local:

```text
/opt/data/backups/lk-agents-runtime-restart-phase2-20260625T182705Z
/opt/data/backups/lk-agents-runtime-restart-phase2-latest-validation.json
```

## Resultado pós-restart

| Profile | Live | Telegram | PID | API key | Webhook secret | Max iter | SOUL heading |
|---|---:|---|---:|---:|---:|---:|---|
| `lk-growth` | 1 | connected | 66782 | False | False | 60 | `# LK Growth OS — Hermes Specialist` |
| `lk-shopify` | 1 | connected | 66830 | False | False | 50 | `# LK Shopify Hermes` |
| `lk-collection-optimizer` | 1 | connected | 67045 | False | False | 50 | `# [LK] Otimização de Coleções / LKGOC — Hermes Specialist` |
| `lk-stock` | 1 | connected | 67157 | False | False | 50 | `# SOUL — [LK] Estoque Loja Física` |
| `lk-trends` | 1 | connected | 66920 | False | False | 45 | `# LK Trend OS — Hermes Specialist` |
| `lk-finance` | 1 | connected | 67362 | False | False | 50 | `# LK Finance — Hermes Specialist` |
| `lk-content` | 1 | connected | 67495 | False | False | 60 | `# LK Content — Hermes Specialist` |
| `lk-ops` | 1 | connected | 66825 | False | False | 40 | `# LK Ops Hermes Bot — SOUL` |
| `lk-analyst-readonly` | 0 | None |  | False | False |  | `# LK Analyst Readonly` |
| `lk-content-reviewer` | 0 | None |  | False | False |  | `# LK Content Reviewer` |

## Identidade LKGOC

O ponto crítico foi validado pós-restart:

```text
# [LK] Otimização de Coleções / LKGOC — Hermes Specialist
```

`lkgoc_growth_contam=false` para `lk-collection-optimizer`.

## Validações finais

- 8/8 gateways LK ativos com `live_count=1`.
- 8/8 gateways LK ativos com Telegram `connected`.
- API/Webhook externos dos especialistas: fechados (`API_SERVER_ENABLED=false`, `WEBHOOK_ENABLED=false`, sem key/secret no ambiente live).
- Brain health: `FAIL=0 WARN=0`.
- Secret scan high-confidence nos arquivos de identidade: `0`.
- Docker/VPS/Traefik/Main/default: não tocados.
- Shopify/Tiny/GMC/Klaviyo/WhatsApp/e-mail/prod: não tocados.

## Observações

- `lk-growth` demorou mais para registrar `telegram=connected`, por conectividade Telegram/fallback IP; após aguardar, ficou `connected` e `state_pid` atualizado para o novo PID.
- `lk-analyst-readonly` e `lk-content-reviewer` continuam parados/dormant. Na Fase 1, o smoke CLI deles bateu `HTTP 401 token_expired`; isso não foi corrigido nesta fase porque exigiria pacote de auth separado.
- Os smokes CLI seguem mostrando uma fragilidade separada (`exit 134/core dumped` em alguns runs após responder). O runtime Telegram/gateway pós-restart ficou saudável; o core dump é pendência do harness CLI, não bloqueio desta ativação.

## Conclusão

Fase 2 concluída: os gateways LK ativos foram reiniciados e agora rodam com a documentação/identidade realinhada da Fase 1. O `lk-collection-optimizer` está vivo, conectado e com SOUL LKGOC, sem contaminação Growth no arquivo carregável.
