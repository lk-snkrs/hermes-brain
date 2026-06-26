# Receipt — Cron quinzenal Curadoria LK PDP

Data: 2026-06-07
Timestamp UTC: 20260607T014334Z

## Pedido

Lucas aprovou criar um cron para manter a Curadoria LK PDP viva com relatório recorrente read-only.

Cadência escolhida por Lucas no prompt de decisão:

- Quinzenal
- Segunda-feira
- 08:00 BRT
- Entrega aqui no Telegram

## Execução

Criado cron Hermes no perfil `lk-shopify`.

- Job ID: `7e5ba8b565d5`
- Nome: `LK Curadoria PDP maintenance quinzenal`
- Schedule: `0 11 * * 1`
- Interpretação: servidor em UTC; `11:00 UTC` = `08:00 BRT`
- Próxima execução: `2026-06-08T11:00:00+00:00`
- Delivery: `telegram`
- Mode: `no-agent`
- Script: `lk_curadoria_pdp_maintenance_report.py`
- Script físico: `/opt/data/profiles/lk-shopify/scripts/lk_curadoria_pdp_maintenance_report.py`

Observação: o scheduler dispara toda segunda, mas o script aplica gate quinzenal com âncora `2026-06-08`; semanas fora do ciclo não imprimem stdout e ficam silenciosas.

## Escopo do script

Read-only.

O script:

1. faz `git fetch origin production` no repositório local `/opt/data/hermes_bruno_ingest/lk-new-theme-production-sync`;
2. lê `origin/production:sections/lk-pdp.liquid`;
3. identifica snippets de Curadoria renderizados;
4. parseia grupos/handles;
5. checa readiness pública via `https://lksneakers.com.br/products/<handle>.js`;
6. classifica blocos em verde/amarelo/vermelho/cinza;
7. grava JSON e Markdown em `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/`;
8. entrega um resumo curto via Telegram.

## Verificações realizadas

### Gateway cron

Comando:

```bash
HERMES_HOME=/opt/data/profiles/lk-shopify /opt/hermes/.venv/bin/hermes cron status
```

Resultado:

- Gateway running
- PID reportado: `367`

### Cron list/readback

Comando:

```bash
HERMES_HOME=/opt/data/profiles/lk-shopify /opt/hermes/.venv/bin/hermes cron list --all
```

Resultado relevante:

- `7e5ba8b565d5 [active]`
- Schedule `0 11 * * 1`
- Next run `2026-06-08T11:00:00+00:00`
- Deliver `telegram`
- Mode `no-agent`

### Dry-run forçado

Comando:

```bash
HERMES_HOME=/opt/data/profiles/lk-shopify /opt/data/profiles/lk-shopify/scripts/lk_curadoria_pdp_maintenance_report.py --force
```

Resultado final validado:

- Status: `AÇÃO`
- Semáforo: verde `15`, amarelo `0`, vermelho `20`, cinza `0`
- Handles públicos checados: `260`
- Arquivo Markdown: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260606T223921-0300.md`
- Nenhum write Shopify/DEV/Production executado.

## Risco

- O relatório usa storefront público `.js`; se houver rate limit ou instabilidade CDN, algum handle pode aparecer como inválido temporariamente. O script usa domínio `lksneakers.com.br`, user-agent tipo browser e retry básico.
- O relatório é diagnóstico/readiness; não aplica correções automaticamente.
- O gate quinzenal fica no script, não no cron expression, porque cron simples não representa bem “a cada 14 dias na segunda”.

## Rollback / desativação

Para remover/desativar o cron, usar o job id `7e5ba8b565d5` via Hermes cron CLI.

Script local removível:

- `/opt/data/profiles/lk-shopify/scripts/lk_curadoria_pdp_maintenance_report.py`

Artefatos gerados ficam em:

- `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/`

## Bloqueio

Nenhum bloqueio atual. A primeira execução programada está prevista para `2026-06-08T11:00:00+00:00`.

## Próxima decisão

Após o primeiro relatório automático, decidir se o ciclo deve continuar apenas como alerta/read-only ou se algum bloco vermelho vira approval packet para DEV.
