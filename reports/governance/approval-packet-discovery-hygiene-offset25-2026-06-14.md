# Approval Packet Completeness — discovery hygiene + offset 25 batch — 2026-06-14

## Pedido

Lucas respondeu `Seguir, aprovados` após a amostra `--limit 25` ficar verde e após o discovery sem limite apontar backlog amplo. Escopo executado: endurecer o discovery para reduzir falsos/ambíguos históricos e corrigir o próximo lote controlado, sem executar qualquer packet ou ação externa/produtiva.

## Higiene do discovery

Alterado `scripts/approval_packet_completeness_validator.py`:

- Adicionado `--offset` para permitir batching controlado (`--offset N --limit M`).
- Discovery agora exclui path parts arquivais/auxiliares:
  - `receipts`
  - `recibos`
  - `logs`
  - `references`
  - `templates`
  - `handoffs`
- Mantidas as exclusões por nome já existentes: `APPROVAL-CAPTURED`, `APPROVAL-REITERATED`, `APPROVAL-LOG`, `DECISION-LOG`, `receipt`, `recibo`, `log`, `captured`, `reiterated`.

Teste adicionado em `tests/test_approval_packet_completeness_validator.py`:

- `test_discovery_supports_offset_for_controlled_batches`
- Regressão expandida para garantir que `templates/approval-packet-template.md` não entra como packet vivo.

## Próximo lote corrigido

Comando do lote:

```bash
python3 scripts/approval_packet_completeness_validator.py --discover --offset 25 --limit 25 --json
```

Antes:

- `status=attention`
- `files_checked=25`
- `failures_count=25`
- `values_printed=false`

Depois:

- `status=ok`
- `files_checked=25`
- `failures_count=0`
- `values_printed=false`

Artefatos:

- Antes: `reports/approval-packet-completeness-batch25-offset25-2026-06-14-before-hygiene.json`
- Depois: `reports/approval-packet-completeness-batch25-offset25-2026-06-14-after.json`

## Amostra acumulada

Amostra `--limit 50` após a correção:

- `status=ok`
- `files_checked=50`
- `failures_count=0`
- `values_printed=false`

Artefato:

- `reports/approval-packet-completeness-sample50-2026-06-14-after-offset25.json`

## Backlog amplo depois da hygiene

Discovery sem limite após hygiene + lote offset25:

- `status=attention`
- `files_checked=1370`
- `failures_count=1317`
- `values_printed=false`

Artefato:

- `reports/approval-packet-completeness-all-2026-06-14-after-offset25.json`

Comparação com medição anterior ampla:

- Antes: `files_checked=1391`, `failures_count=1363`.
- Agora: `files_checked=1370`, `failures_count=1317`.

Interpretação: o discovery ficou menos poluído por templates/receipts/references/handoffs/logs, e 25 packets adicionais foram saneados. O backlog restante ainda é grande e deve continuar em batches controlados.

## Backups

Backups dos 25 arquivos corrigidos:

- `/opt/data/backups/approval-packet-wave-offset25/20260614T_fix_25/`

## Gates rodados

- `python3 -m py_compile scripts/approval_packet_completeness_validator.py tests/test_approval_packet_completeness_validator.py`: OK.
- `python3 -m unittest tests/test_approval_packet_completeness_validator.py tests/test_telegram_noise_contract_validator.py tests/test_telegram_noise_contract_validator_20260614.py`: 10 testes OK.
- `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-06-14-approval-packet-offset25.json`: `fail_count=0`, `warn_count=0`.
- `python3 scripts/operational_docs_guard.py`: `scanned_files=602`, `fail_count=0`.
- `git diff --check`: OK.
- Focused credential hygiene em 34 artefatos: `token_value_findings_count=0`, `values_printed=false`.

## Non-actions / limites preservados

- Nenhum approval packet foi executado.
- Nenhum write Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco/cliente/fornecedor foi feito.
- Nenhum Docker/VPS/Traefik/gateway/runtime/cron foi alterado.
- Nenhum Telegram foi enviado por script.
- Nenhum secret, token, refresh token, password, service-account JSON ou connection string foi impresso.

## Próximo passo recomendado

Continuar em batches controlados:

```bash
python3 scripts/approval_packet_completeness_validator.py --discover --offset 50 --limit 25 --json
```

Se esse próximo lote tiver muitos artefatos claramente históricos/ambíguos, repetir primeiro a hygiene do discovery antes de corrigir conteúdo.
