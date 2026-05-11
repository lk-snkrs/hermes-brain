# Rotina — Watchdogs `no_agent` Hermes v0.13

Data: 2026-05-10
Escopo: propostas de watchdogs script-only para Hermes/LK.

## Objetivo

Usar o modo `no_agent` da v0.13 para checks baratos, silenciosos e read-only. O agente só deve ser acionado quando há stdout não vazio, ou seja, quando existe anomalia relevante.

## Contrato dos scripts

- Exit code `0` com stdout vazio: tudo OK, não enviar nada.
- Exit code `0` com stdout não vazio: alerta operacional claro para Lucas/Hermes.
- Exit code não-zero: erro do watchdog, deve virar alerta de falha do próprio check.
- Nunca imprimir secrets.
- Nunca reiniciar Docker/gateway/serviços.
- Nunca escrever em banco, Shopify, campanha ou canal externo.

## Watchdogs candidatos

### 1. Hermes runtime drift

Alerta se:
- versão não contém `Hermes Agent v0.13.0`;
- imagem não contém `hermes-agent-custom:v0.13.0-20260510`;
- container esperado não está `Up`;
- gateway não reporta `Status: ✓ running`.

Status: precisa aprovação antes de criar cron real se rodar no VPS/Docker.

### 2. Cron scheduler health

Alerta se:
- `hermes cron status` não mostra scheduler rodando;
- job `f5a23dd6a1bd` não existe ou está disabled;
- próximo run está ausente ou muito atrasado;
- `jobs.json` não é JSON válido.

Status: documentado; criação de cron real precisa aprovação se tocar produção.

### 3. LK weekly influencer email artifact

Alerta se, até o horário combinado, o relatório/preview semanal não foi gerado ou não tem evidência de validação.

Guardrail:
- não enviar e-mail;
- não chamar Cloudflare/Klaviyo para envio real;
- apenas reportar ausência de artifact/preview.

### 4. Data freshness LK

Alerta se fontes essenciais ficarem defasadas:
- Shopify orders/source-of-truth;
- Tiny estoque `LK | CONTROLE ESTOQUE`;
- GA4 sessões/canais;
- Meta Ads ad-level para influenciadores;
- Pareto/Metricool quando aplicável.

Guardrail:
- somente leitura;
- sem exportar PII;
- sem corrigir token automaticamente.

## Template de mensagem de alerta

```text
⚠️ Watchdog Hermes/LK: [nome]
Problema: [anomalia]
Evidência: [comando/arquivo/status sem secrets]
Impacto provável: [curto]
Ação segura recomendada: [read-only/plano]
Aprovação necessária: [sim/não e por quê]
```

## Artefato preparado

Script read-only preparado em:

- `areas/operacoes/scripts/hermes_runtime_cron_watchdog.py`

Escopo do script:

- verifica versão Hermes esperada (`v0.13.0`) usando `/opt/hermes/.venv/bin/hermes` quando disponível;
- verifica `terminal.backend: local` e `terminal.cwd: /opt/data` sem imprimir secrets;
- verifica existência de processo `hermes gateway run` sem acessar env de processos;
- valida `/opt/data/cron/jobs.json` e o job diário `f5a23dd6a1bd`;
- não chama APIs externas, não reinicia Docker/gateway, não altera cron, não escreve arquivos e não imprime variáveis de ambiente.

Contrato validado:

- `python3 areas/operacoes/scripts/hermes_runtime_cron_watchdog.py --verbose` mostra diagnóstico manual;
- `python3 areas/operacoes/scripts/hermes_runtime_cron_watchdog.py` retorna `rc=0` e stdout vazio quando está OK, compatível com cron `no_agent` silencioso;
- cópia executável instalada em `/opt/data/scripts/hermes_runtime_cron_watchdog.py`, porque o `cronjob` neste runtime resolve scripts relativos ao diretório de scripts do `HERMES_HOME` (`/opt/data/scripts/`).

## Próximo passo seguro

O script está pronto para ativação como cron `no_agent`, mas a criação do cron real ainda muda a agenda operacional do Hermes. Antes de ativar, Lucas deve aprovar explicitamente a criação do job.

Proposta recomendada para aprovação:

- Nome: `Hermes runtime + cron watchdog no_agent`
- Schedule: `*/30 * * * *`
- Delivery: `origin`
- Modo: `no_agent=True`
- Script: `hermes_runtime_cron_watchdog.py` em `/opt/data/scripts/` (o `cronjob` rejeita caminho absoluto e resolve relativo ao diretório de scripts do `HERMES_HOME`)
- Comportamento: silêncio quando OK; alerta só se houver drift/anomalia.

## Cron real ativado — runtime/cron health

Aprovado por Lucas e criado em 2026-05-10:

- Job ID: `edd06fe19397`
- Nome: `Hermes runtime + cron watchdog no_agent`
- Schedule: `*/30 * * * *`
- Delivery: `origin`
- Modo: `no_agent=True`
- Script: `hermes_runtime_cron_watchdog.py`
- Primeira execução de verificação: `2026-05-10T23:06:38+00:00`, status `ok`
- Próximo run confirmado: `2026-05-10T23:30:00+00:00`

Observação operacional: foi tentada a criação com caminho absoluto e o scheduler recusou; a forma correta neste runtime é instalar/copy em `/opt/data/scripts/` e referenciar apenas o nome do arquivo. A primeira tentativa também falhou antes da cópia para `/opt/data/scripts/`; depois da correção, o run manual agendado ficou `ok`.

## Cron real ativado — freshness de artefatos v0.13

Criado em 2026-05-10 como continuação read-only da operacionalização v0.13:

- Job ID: `e7a61e275c37`
- Nome: `Hermes v0.13 artifacts freshness watchdog no_agent`
- Schedule: `0 12 * * *` (09:00 BRT)
- Delivery: `origin`
- Modo: `no_agent=True`
- Script fonte: `areas/operacoes/scripts/hermes_artifacts_freshness_watchdog.py`
- Script executável: `/opt/data/scripts/hermes_artifacts_freshness_watchdog.py`
- Contrato validado manualmente: `rc=0` e stdout vazio quando OK; `--verbose` confirma report semanal atual, board `lk-growth-ops` com 7 cards e cron jobs esperados presentes.

Escopo do script:
- valida freshness do último JSON do relatório semanal LK em `/opt/data/lk_weekly_influencer_sales_reports/`;
- valida existência e contagem mínima do board Kanban `lk-growth-ops`;
- valida docs operacionais v0.13 no Hermes Brain;
- valida presença dos crons `f5a23dd6a1bd` e `edd06fe19397`;
- não lê tokens, não chama APIs externas, não reinicia serviços, não corrige nada sozinho e não exporta dados.
