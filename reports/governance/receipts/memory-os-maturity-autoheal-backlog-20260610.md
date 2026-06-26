# Receipt — Memory OS maturity auto-heal backlog

Data UTC: 2026-06-10T17:30:20Z
Executor: Hermes Agent / default profile
Escopo: local/documental + testes; sem writes externos.

## Gatilho

Lucas respondeu ao alerta:

> Memory OS: maturação de ciclos reais com atenção.
> report_status_not_ok:daytime-latest.json:attention
> report_status_not_ok:scorecard-latest.json:attention
> report_status_not_ok:adoption-latest.json:attention

Pedido: “Corrigir e adicionar no auto heal”.

## Diagnóstico

A causa atual era backlog local de evidência de adoção:

- `daytime-latest.json`: `status=attention`
- `scorecard-latest.json`: `status=attention`
- `adoption-latest.json`: `status=attention`
- adoption gap inicial: `170`
- wrapper anterior curava apenas `10` por ciclo, deixando findings de maturação acionáveis.

## Correção

Atualizado `/opt/data/scripts/hermes_memory_os_daytime_checker.py`:

- adicionada `recommended_adoption_auto_heal_limit(adoption_report, requested_limit, cap=250)`;
- quando o adoption linter está em `attention` e `gap_count` excede o limite solicitado, o checker amplia o lote até `min(gap_count, 250)`;
- `requested_limit=0` continua desabilitando auto-heal;
- auto-heal existente já pagina gaps e reroda o linter até fechar o backlog ou atingir o limite.

Teste atualizado:

- `/opt/data/tests/test_memory_os_autoheal_v120.py`
- novo caso garante limite recomendado para maturity findings;
- novo caso garante paginação de lote seguro até fechar gaps.

## Execução real

Comando executado:

```bash
/opt/hermes/.venv/bin/python /opt/data/scripts/hermes_memory_os_daytime_checker.py --json --since-minutes 240 --adoption-auto-heal-limit 10
```

Resultado sanitizado:

- status final: `ok`
- adoption gap final: `0`
- auto-heal limit efetivo: `170`
- attempted: `170`
- healed: `170`
- failed: `0`
- skipped: `0`
- passes: `4`
- routes restantes: `0`

## Verificação

Após probe + wrapper:

- `daytime-latest.json`: `ok`
- `scorecard-latest.json`: `ok`
- `adoption-latest.json`: `ok`
- `cycle-maturity-latest.json`: `ok`
- cycle findings: `[]`
- wrapper stdout bytes: `0`

Gates finais executados:

- Memory OS tests v1.20-v2.3: OK.
- `test_memory_os_autoheal_v120.py`: 5 tests OK, incluindo regressão de auto-size e paginação de backlog.
- Brain health: `All checks passed`.
- Operational docs guard: `scanned_files=396`, `fail_count=0`.
- Focused secret scan: `files_scanned=6`, `possible_secrets=0`.

## Guardrails

- Sem Docker/VPS/Traefik/gateway/container/restart.
- Sem cron mutation.
- Sem provider externo/Mem0/Honcho.
- Sem writes em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco.
- Sem secrets impressos.
- Auto-heal restrito a metadados locais/sanitizados de Memory OS.
