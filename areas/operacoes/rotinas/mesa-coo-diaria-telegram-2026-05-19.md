# Mesa COO diária no Telegram — rotina operacional

Data: 2026-05-19
Owner: Hermes Geral / Chief of Staff
Status: operacionalizado em cron + skill `/mesa`

## Decisão

A Mesa COO passa a existir no Telegram em dois modos:

1. **On-demand**: Lucas pode chamar `Mesa COO`, `Mesa COO diária` ou `/mesa`.
2. **Diário automático**: cron `749ee30b51eb` — `Mesa COO diária Telegram`, entrega em `origin`, 08h30 BRT (`30 11 * * *` UTC).

## Propósito

A Mesa COO não é catálogo de módulos. É a superfície diária de decisão para Lucas:

- o que Lucas decide agora;
- o que está bloqueado por Lucas;
- o que Hermes pode fazer sozinho com segurança;
- riscos por empresa/sistema;
- fontes vivas verificadas.

## Fonte de verdade

Ordem de leitura:

1. Brain versionado local.
2. `memories/current.md`, quando existir.
3. Inventário runtime/crons/canais.
4. `cronjob list` como fonte viva de jobs.
5. Reports recentes em `reports/`.
6. Mission Control/PRDs como shape de produto, não como runtime truth.

## Guardrails

A Mesa nunca aprova nem executa automaticamente:

- WhatsApp, e-mail, cliente, fornecedor ou social;
- Shopify, GMC, Tiny, Meta, Google Ads, Klaviyo ou campanhas;
- Docker, VPS, gateway, banco, migração ou deploy;
- qualquer payload externo sem aprovação explícita de Lucas no turno atual.

Saídas de risco viram pacote de decisão/preview com fonte, alvo, payload, risco e rollback.

## Contrato de saída

Formato curto para Telegram:

```md
## Mesa COO — YYYY-MM-DD

**Decisão 1 agora:** ...
- Recomendação: ...
- Se aprovado, Hermes faz: ...
- Não faz: ...
- Fonte: ...

**Bloqueado por Lucas:**
- ...

**Hermes pode fazer sozinho hoje:**
- ...

**Riscos:**
- ...

**Fontes vivas verificadas:**
- Crons: ...
- Brain: ...
- Mission: ...

**Próximo passo recomendado:** ...
```

## Estado implementado

- Skill criada: `mesa`.
- Slash skill esperado após recarga de skills/gateway: `/mesa`.
- Cron criado: `749ee30b51eb`.
- Próxima execução: 2026-05-20 11:30 UTC / 08:30 BRT.

## Nota de gateway

A skill foi criada no filesystem. Se o gateway não reconhecer `/mesa` imediatamente, executar `/reload-skills` ou reiniciar o gateway com plano/rollback. Reinício de gateway/Docker não deve ser feito automaticamente sem gate explícito de Lucas.
