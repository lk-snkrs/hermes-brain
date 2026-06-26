# Template — Approval Packet para mudança de cron delivery / Telegram noise v0.16

Status: template operacional/documental. Usar antes de qualquer mudança real em `deliver`, schedule, script, cron, gateway ou Telegram delivery.

## Princípio

Mudança de delivery de cron existente exige approval separado com lista nominal dos jobs. A aprovação deve dizer exatamente quais jobs mudam e o que não muda.

## Packet

```md
# Approval Packet — Cron delivery / Telegram noise

Data:
Owner:
Escopo solicitado:

## Jobs nominais

1. `[job_id]` — [nome]
   - status atual:
   - deliver atual:
   - último status:
   - razão para mudar/manter:
   - novo deliver proposto:
   - risco: A0/A1/A2/A3/A4
   - rollback:

## O que está aprovado se Lucas disser sim

- alterar apenas `deliver` dos jobs listados nominalmente;
- manter schedule/script/prompt/state iguais;
- verificar registry após mudança;
- registrar receipt no Brain.

## O que continua bloqueado

- alterar schedule;
- alterar script;
- criar/remover cron;
- mudar prompt/model/toolsets;
- reiniciar gateway;
- Docker/VPS/Traefik;
- secrets;
- envios externos;
- qualquer job não listado nominalmente.

## Verificação obrigatória

- cron list/registry antes e depois;
- `enabled/state/last_status/last_delivery_error` preservados quando aplicável;
- rollback command documentado;
- secret scan em artefatos;
- Brain Health.

## Opções para Lucas

- Aprovar exatamente os jobs listados.
- Manter como está.
- Ajustar lista.
```

## Classificação rápida

Manter `origin` normalmente para:

- Mesa/relatório executivo que Lucas quer receber;
- decisão humana;
- falha atual não recuperada;
- restart/auto-heal sensível;
- runtime drift acionável.

Preferir `local` normalmente para:

- OK saudável;
- auditoria estrutural sem decisão;
- selftest/regressão sem anomalia;
- receipt técnico;
- logs completos.
