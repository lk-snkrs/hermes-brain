# Approval packet — reduzir ruído do cron 02h30

Criado em: 2026-05-27T12:16:51Z  
Escopo: alteração única de delivery do job `98478b820720`.  
Tipo: runtime cron mutation — exige aprovação explícita.

## Decisão proposta

Mover o cron abaixo de `origin` para `local`:

- Job: `98478b820720`
- Nome: Relatório Hermes diário 23h + 02h para Lucas
- Schedule vivo: `30 5 * * *` UTC / 02h30 BRT
- Delivery atual observado: `origin`
- Delivery proposto: `local`

## Por que fazer

O job 02h30 tende a duplicar a função da Mesa COO no Telegram. O padrão aprovado para reduzir ruído é:

- Telegram/origin: decisão, exceção, relatório explicitamente desejado ou alerta relevante.
- Local: relatório técnico/estrutural que serve como insumo para Brain/Mesa COO.

A Mesa COO (`749ee30b51eb`) continua sendo a fila executiva principal no Telegram.

## Evidência

Reconciliação de 2026-05-27 confirmou:

- scheduler vivo: 21 jobs;
- todos `last_status=ok`;
- sem `last_delivery_error`;
- `98478b820720` vivo com `deliver=origin`;
- documentação anterior dizia `local`, então existe drift doc/runtime.

Arquivos de suporte:

- `reports/governance/main-mordomo-final-reconciliation-2026-05-27.md`
- `areas/operacoes/rotinas/cron-control-plane.md`

## O que será alterado se aprovado

Somente este campo no scheduler:

```text
job_id: 98478b820720
deliver: origin -> local
```

## O que NÃO será alterado

- Não mudar schedule.
- Não mudar prompt.
- Não pausar/remover job.
- Não criar cron novo.
- Não reiniciar gateway.
- Não tocar Docker/VPS/Traefik/container.
- Não tocar Shopify/Tiny/WhatsApp/e-mail/banco.
- Não tocar secrets.

## Comando operacional previsto

Via ferramenta Hermes:

```python
cronjob(action="update", job_id="98478b820720", deliver="local")
```

## Verificação pós-mudança

1. Rodar `cronjob(action='list')`.
2. Confirmar no job `98478b820720`:
   - `deliver=local`;
   - `enabled=true`;
   - `state=scheduled`;
   - `last_status=ok` permanece registrado;
   - `last_delivery_error=null`.
3. Registrar receipt no Brain.
4. Rodar:
   - `python scripts/brain_health_check.py`
   - `python scripts/operational_docs_guard.py`
5. Atualizar `areas/operacoes/rotinas/cron-control-plane.md` se necessário.

## Rollback

Se Lucas quiser voltar o relatório 02h30 para Telegram:

```python
cronjob(action="update", job_id="98478b820720", deliver="origin")
```

## Risco

Baixo.

Impacto esperado:

- Menos ruído no Telegram às 02h30 BRT.
- Relatório continua rodando e sendo salvo localmente.
- Mesa COO permanece como superfície executiva.

Risco principal:

- Lucas deixar de ver no Telegram um relatório que ainda queria receber diariamente. Rollback é simples: voltar `deliver=origin`.

## Aprovação necessária

Aprovação escopada sugerida:

> Aprovo mover o job `98478b820720` para `local`, sem mudar schedule/prompt/gateway/Docker/external writes.
