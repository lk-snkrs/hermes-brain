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

## Contrato de saída — v2

Formato curto para Telegram: **uma mensagem = uma decisão**.

A Mesa COO v2 usa o contrato dos especialistas e o handoff ledger para escolher decisões reais, não status saudável.

Fontes novas da Fase 8:

- `empresa/contexto/contratos-handoff-especialistas.md`
- `empresa/contexto/handoff-ledger.md`
- `empresa/contexto/handoffs/YYYY-MM-DD.md`
- `areas/operacoes/prds/hermes-orquestracao-fase-8-proatividade-handoffs-2026-05-24.md`

Formato visível:

```md
## Mesa COO — YYYY-MM-DD

**Decisão 1/4:** ...
- Dono: Hermes Geral / LK Growth / Mordomo / SPITI / Zipper / Operações
- Por que importa: ...
- Se escolher Fazer: ...
- Evidência: ...
- Limite/risco: ...
```

Regras:

1. Máximo 4 decisões reais por ciclo.
2. Se não houver decisão real, enviar no máximo 3 bullets e parar.
3. Não incluir catálogo de módulos, watchdog saudável, wrappers, job IDs, JSON ou marcadores técnicos visíveis.
4. Para cron com botões nativos, o marcador `HERMES_INLINE_BUTTONS` só pode existir como marcador oculto final, removido pelo scheduler antes do Telegram.
5. Quando a ação final for produção/contato/publicação/preço/disponibilidade/Docker/VPS/gateway/cron/write externo, **Fazer** significa preparar/validar approval packet ou preview read-only, não executar produção.
6. Loops Reminder OS só viram decisão da Mesa quando forem acionáveis: `waiting_lucas`, alta severidade, risco real de abandono ou decisão humana clara. Backlog baixo/stale deve ficar local, resumido ou expirado.
7. Ao usar Reminder OS como fonte, a Mesa deve citar evidência curta e nunca expor JSON bruto do ledger, job ID ou wrapper técnico.

## Integração Reminder OS

Spec canônica: `areas/operacoes/reminder-os/mesa-coo-integration-v1.md`.

Critério: Reminder OS alimenta a Mesa com loops que precisam de decisão executiva; a Mesa não vira lista de tarefas. `Fazer` preserva o escopo seguro descrito na decisão e não autoriza writes externos/runtime por inferência.

## Estado implementado

- Skill criada: `mesa`.
- Slash skill esperado após recarga de skills/gateway: `/mesa`.
- Cron criado: `749ee30b51eb`.
- Próxima execução: 2026-05-20 11:30 UTC / 08:30 BRT.

## Nota de gateway

A skill foi criada no filesystem. Se o gateway não reconhecer `/mesa` imediatamente, executar `/reload-skills` ou reiniciar o gateway com plano/rollback. Reinício de gateway/Docker não deve ser feito automaticamente sem gate explícito de Lucas.
