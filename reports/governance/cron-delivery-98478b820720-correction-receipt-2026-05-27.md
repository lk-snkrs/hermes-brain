# Receipt — correção do delivery do cron 02h30

Data/hora: 2026-05-27T12:20:16Z

## Contexto

Foi preparado e aprovado um packet para reduzir ruído movendo o job `98478b820720` de `origin` para `local`. Após a execução, Lucas corrigiu a intenção: **ele quer receber esse resumo no Telegram**.

## Correção executada

O job foi imediatamente revertido para `origin`.

- Job: `98478b820720`
- Nome: Relatório Hermes diário 23h + 02h para Lucas
- Delivery correto: `origin`
- Schedule preservado: `30 5 * * *`
- Estado: `enabled=true`, `state=scheduled`
- Último status preservado: `ok`
- Último erro de delivery: `null`

## Escopo tocado

Somente o campo `deliver` do job `98478b820720` foi corrigido de volta para `origin`.

## Escopo não tocado

- Nenhum schedule alterado.
- Nenhum prompt alterado.
- Nenhum cron pausado/removido/criado.
- Nenhum gateway reiniciado.
- Nenhum Docker/VPS/Traefik/container tocado.
- Nenhum Shopify/Tiny/WhatsApp/e-mail/banco tocado.
- Nenhum secret tocado.

## Documento atualizado

- `areas/operacoes/rotinas/cron-control-plane.md`

A documentação agora registra que Lucas quer o resumo 02h30 no Telegram e que `origin` é o comportamento correto para este job.

## Rollback inverso

Só usar se Lucas pedir explicitamente para parar este resumo no Telegram:

```python
cronjob(action="update", job_id="98478b820720", deliver="local")
```
