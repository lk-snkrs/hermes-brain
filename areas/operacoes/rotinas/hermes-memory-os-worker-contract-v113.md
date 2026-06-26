# Hermes Memory OS — contrato v1.13 para agentes e workers

Criado: 2026-06-09T19:03:57Z

## Regra operacional

Todo agente ou worker que criar receipt operacional novo sob qualquer segmento `receipts/` deve usar:

```bash
python3 /opt/data/scripts/hermes_memory_os_receipt_writer.py ...
```

Se o worker legado já criou um arquivo e não pode reescrever o corpo, registrar evidência sem sobrescrever:

```bash
python3 /opt/data/scripts/hermes_memory_os_worker_receipt_guard.py --path <receipt> --title <título> --empresa-area <área> --pedido <pedido> --source <fonte> --reason <motivo>
```

Ou usar diretamente `hermes_memory_os_receipt_writer.py --register-existing`.

## Alertas

- OK: stdout vazio, sem Telegram.
- Problema seguro: checker tenta auto-heal primeiro.
- Problema corrigido: Telegram curto informando que foi detectado e resolvido.
- Problema não corrigido / decisão humana: Telegram pergunta Lucas.

## Fora de escopo

- Mission Control não é superfície operacional do Memory OS.
- Sem Docker/VPS/Traefik/gateway/provider externo ou writes externos sem aprovação separada.
