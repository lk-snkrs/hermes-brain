# Mesa COO — correção de convenção de data do Fechamento 23h — 2026-05-23

Status: aplicado.

## Problema

A Mesa COO de 2026-05-23 podia interpretar incorretamente a ausência de `reports/daily-consolidation/2026-05-23.md` pela manhã como erro/falta do report das 23h.

Isso é falso antes das 23h BRT do próprio dia, porque o cron `Hermes Brain Fechamento Ágil 23h + Brain Sync` (`3fc45b0830c6`) roda às `02:00 UTC`, consolidando o dia BRT anterior. O fechamento das 23h BRT de 2026-05-22 gera `reports/daily-consolidation/2026-05-22.md`, mesmo que o runtime UTC seja 2026-05-23.

## Evidência viva verificada

- `3fc45b0830c6` — ativo, `deliver=local`, `last_status=ok`, último run `2026-05-23T02:08:40.857450+00:00`, próximo run `2026-05-24T02:00:00+00:00`.
- Report existente do último fechamento concluído: `reports/daily-consolidation/2026-05-22.md`.
- Digest consolidado existente: `reports/hermes-daily-digest/2026-05-23.md`.
- Ainda não há `reports/daily-consolidation/2026-05-23.md` porque o fechamento das 23h BRT de 2026-05-23 ainda não rodou.

## Correção aplicada

1. Skill `mesa` atualizada para explicitar a convenção de data BRT/UTC do Fechamento Ágil 23h.
2. Cron `749ee30b51eb` — `Mesa COO diária Telegram` — atualizado apenas no prompt, mantendo:
   - schedule `30 11 * * *`;
   - `deliver=origin`;
   - skills `mesa`, `lucas-chief-of-staff`, `multiempresa-routing-lucas`;
   - workdir `/opt/data/hermes_bruno_ingest/hermes-brain`;
   - toolsets existentes.
3. O novo prompt instrui a Mesa a usar o último `reports/daily-consolidation/*.md` existente + digest/continuous improvement do dia, e só marcar erro se o cron vivo mostrar falha ou se o arquivo esperado para o último fechamento BRT concluído estiver ausente.

## Escopo não alterado

- Nenhum schedule foi alterado.
- Nenhum delivery foi alterado.
- Nenhum cron foi criado/removido/pausado.
- Nenhum gateway/Docker/VPS/Shopify/GMC/Tiny/WhatsApp/email foi tocado.

## Rollback

Reverter o prompt do cron `749ee30b51eb` para a versão anterior, se necessário. Não há rollback de runtime externo porque a mudança foi apenas prompt/documentação local.
