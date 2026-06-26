# Runtime Repair Runbook — Hermes/LK produção

Gerado em: 2026-05-30T21:41:19+00:00  
Status: **canônico v0.1**

## Regras gerais

Antes de qualquer reparo:

1. Fazer triagem read-only.
2. Identificar profile exato.
3. Não imprimir secrets.
4. Não mexer em Docker/VPS/Traefik/Main Hermes por problema de especialista, salvo aprovação explícita.
5. Uma mudança por vez.
6. Verificar com evidência objetiva.
7. Se houver write/restart, registrar receipt sanitizado.

## LK Shopify offline ou não responde

Use quando Lucas disser “LK Shopify está offline”, “não responde”, “bot sumiu” ou equivalente.

### Diagnóstico read-only

Verificar:

1. Existe processo `hermes gateway run` com `HERMES_HOME=/opt/data/profiles/lk-shopify`?
2. `gateway_state.json` indica `running` e Telegram `connected`?
3. Logs recentes mostram inbound do Lucas?
4. Logs mostram `response ready` depois do inbound?
5. Há conflito de polling Telegram?
6. API/webhook continuam desligados?
7. `Agent budget`/max iterations bate com esperado (`50`)?
8. Active agents está preso ou há trabalho longo/compressão?

### Interpretação

- Processo ausente: offline real.
- Processo vivo + Telegram connected + sem resposta: degradado; precisa round-trip/probe.
- Conflito de polling: provável duplicidade/sessão Telegram antiga; não iniciar múltiplos gateways sem limpar evidência.
- Resposta muito lenta: problema de fast lane/performance, não necessariamente offline.

### Ação segura típica

Permitida se escopo local estiver claro/aprovado:

1. Backup de config/env/launcher afetados, se for alterar.
2. Reiniciar somente `lk-shopify`.
3. Forçar/confirmar API/webhook off.
4. Verificar `/proc/<pid>/environ` com `HERMES_HOME` correto.
5. Verificar startup no log.
6. Enviar/propor probe curto.
7. Só declarar resolvido depois de round-trip ou evidência equivalente.

### Bloqueado sem aprovação explícita

- Docker/VPS/Traefik.
- Main Hermes/default.
- Shopify/Tiny writes.
- Troca de token.
- Alterar outros profiles.

## LK Ops / Atendimento lento ou sem resposta

### Diagnóstico

1. Processo com `HERMES_HOME=/opt/data/profiles/lk-ops`.
2. Telegram connected.
3. Logs de inbound/response.
4. `max_iterations` esperado: `40`.
5. Verificar se trabalho Tiny/cache/terminal está bloqueando chat.
6. Verificar API/webhook off no processo vivo, não só no arquivo.
7. Separar “conectado” de “rápido o suficiente para atendimento”.

### Ação segura típica

- Se gateway parado: restart apenas do `lk-ops`, com API/webhook off.
- Se lento: reduzir trabalho pesado no Telegram, mover análise para background/local e responder curto.
- Se env/config divergem do processo: corrigir launcher/env somente com escopo aprovado.

## LK Trends não responde

### Diagnóstico

1. Processo `lk-trends` vivo.
2. Telegram connected.
3. Há inbound pós-restart?
4. Logs têm resposta curta ou sessões longas?
5. `max_iterations` esperado: `45`.

### Ação segura típica

- Restart isolado se parado/degradado e escopo aprovado.
- Probe curto pós-restart.
- Não transformar trend em compra/reposição/write.

## Cron não entregou

Não assumir que falhou.

### Diagnóstico

1. Ver `last_run_at`.
2. Ver `last_status`.
3. Ver `last_delivery_error`.
4. Ver `deliver`.
5. Ler output local se `deliver=local`.
6. Separar “rodou localmente” de “chegou no Telegram”.

### Interpretação

- `last_status=ok` + `deliver=local`: cron rodou, mas foi salvo localmente.
- `last_status=error`: corrigir script/job.
- `last_delivery_error`: problema de entrega, não necessariamente do job.
- Relatório que Lucas quer no Telegram deve preservar `origin`/Telegram.

### Regra de comunicação

Extrair só a resposta humana final. Não reenviar prompt bruto, wrapper técnico, skill carregada ou job id como conteúdo para Lucas.

## Provider/modelo travou

Use quando houver timeout, “No response from provider”, fallback, stream interrompido ou compressão falhando.

### Diagnóstico

1. Ler logs recentes do profile afetado.
2. Separar:
   - auth failure;
   - quota/crédito;
   - timeout;
   - stale-call;
   - fallback real;
   - compressão/auxiliary.
3. Rodar smoke test quando necessário.
4. Não diagnosticar por chute.

### Ação segura típica

- Se só uma chamada pesada: não reiniciar tudo.
- Se provider degradado repetidamente: usar fallback configurado ou propor mudança escopada.
- Se compressão falhou: priorizar proteção de contexto e verificar watchdog/self-heal.

## Gateway duplicado ou conflito de polling

### Diagnóstico

1. Identificar processos por `/proc/<pid>/environ`, não só por `pgrep`.
2. Confirmar `HERMES_HOME` exato.
3. Ver se há dois gateways reais para o mesmo profile.
4. Ver logs de Telegram polling conflict.
5. Ignorar wrappers/helpers que não são gateway real.

### Ação segura típica

- Se duplicidade real persistente: matar/reiniciar somente o profile duplicado com rollback claro.
- Se conflito transitório após restart: aguardar/monitorar e não fazer restart em cascata.

## API/webhook exposto ou suspeito

### Diagnóstico

1. Identificar porta/listener.
2. Confirmar se bind é `127.0.0.1` ou `0.0.0.0`.
3. Confirmar proteção por Docker/firewall/Traefik/auth.
4. Não imprimir API keys/webhook secrets.

### Bloqueado sem aprovação

- Alterar Docker compose.
- Firewall/VPS.
- Traefik.
- Expor/restringir porta produtiva.
- Rotacionar segredo.

### Saída esperada

Um approval packet curto com:

- risco;
- evidência;
- mudança proposta;
- rollback;
- verificação.

## Template de receipt curto

```md
# Receipt — [profile/surface] — [data]

- Pedido:
- Evidência antes:
- Ação executada:
- Ação não executada:
- Verificação:
- Rollback disponível:
- Pendência:
```
