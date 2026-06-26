# Handoff — LC Hermes / melhoria sistêmica de contexto mínimo

Data/hora: 2026-06-06T00:17:58Z
Origem: Mordomo Hermes / Lucas Cimino
Destino operacional: LC Hermes / Hermes Agent central / profile `default`
Área: Operações / Hermes Brain / governança de subagentes
Status: aprovado por Lucas para handoff sistêmico
Risco: A1 documental/prompt de rotina existente; sem writes externos

## Pedido de Lucas

Lucas corrigiu que a decisão sobre **subagentes com contexto mínimo + Brain sob demanda** não deve ficar aplicada apenas no Mordomo.

A responsabilidade deve ser do **LC Hermes / Hermes Agent central**, cobrindo o sistema inteiro, e o relatório do ciclo deve ser entregue/registrado no lado do LC Hermes também.

## Decisão operacional

A governança de contexto mínimo passa a ser uma regra sistêmica do Hermes, não uma preferência local do Mordomo:

- subagentes não carregam tudo;
- usam Context Budget;
- consultam índice/MAPA primeiro;
- fazem busca sob demanda em Brain, `session_search`, skills e fontes vivas autorizadas;
- sobem handoff compacto com decisão, fonte, status, próximos passos e blockers;
- melhorias A0/A1 devem ser promovidas pelo LC Hermes para Brain/skills/rotinas/checks do ecossistema inteiro.

## Escopo sistêmico esperado

LC Hermes deve aplicar e auditar isso em:

- Hermes Agent central/default profile;
- Brain versionado;
- crons de governança 01h/02h/02h15/02h30;
- registry de subagentes;
- skills e rotinas globais;
- LK, Zipper, SPITI, Mordomo, Mission Control e demais especialistas;
- handoffs entre especialistas e Hermes Central.

## O que já foi aplicado no Brain

Arquivos já atualizados antes deste handoff:

- `areas/operacoes/decisions/subagentes-contexto-minimo-brain-sob-demanda-2026-06-05.md`
- `areas/operacoes/mordomo/subagent-registry-2026-06-05.md`
- `areas/operacoes/prds/lcmordomo-os-prd-2026-06-05.md`
- `areas/operacoes/rotinas/hermes-nightly-governance-cycle.md`
- `areas/operacoes/rotinas/brain-health-check.md`
- `areas/operacoes/MAPA.md`

Health check anterior da mudança: `reports/brain-health-check-2026-06-05-subagent-context-governance.json`, com `FAIL=0/WARN=0`.

## Ajuste necessário no LC Hermes

O cron sistêmico relevante é:

- `f5a23dd6a1bd` — `Lucas Brain daily intelligence loop`
  - schedule: `0 5 * * *` UTC / 02h BRT
  - delivery: `local`
  - owner correto: **LC Hermes / Hermes Agent central / Operações Hermes**
  - escopo correto: sistema inteiro, não Mordomo.

O digest relacionado é:

- `98478b820720` — `Relatório Hermes diário 01h + 02h + 02h15 para Lucas`
  - schedule: `30 5 * * *` UTC / 02h30 BRT
  - delivery: `origin` para Lucas
  - deve também gravar artefato local em `reports/hermes-daily-digest/` e mencionar quando o LC Hermes aplicou melhoria sistêmica.

## Requisitos para o próximo run do LC Hermes

1. Ler esta decisão/handoff como fonte de governança.
2. Verificar se a regra aparece em prompts/rotinas/checks globais, não só em docs do Mordomo.
3. Procurar subagentes/crons que ainda pedem contexto amplo demais ou carregamento integral.
4. Corrigir apenas A0/A1 local/documental/prompt seguro.
5. Não alterar produção, Docker, gateways, delivery externo, WhatsApp/e-mail, dados de negócio, secrets ou fontes de verdade sem aprovação explícita de Lucas.
6. Registrar relatório local do LC Hermes com:
   - arquivos/crons verificados;
   - melhorias aplicadas;
   - gaps que exigem aprovação;
   - próximos passos.

## Entrega esperada

- Relatório local do LC Hermes em `reports/hermes-continuous-improvement/` ou `reports/governance/`.
- Digest curto para Lucas apenas se houver decisão, melhoria real, falha ou risco; sem logs técnicos.

## Checklist

- [x] Sem envio externo executado neste handoff.
- [x] Sem Telegram enviado por este handoff.
- [x] Sem cron novo criado.
- [x] Sem alteração de delivery externo.
- [x] Handoff registrado no Brain versionado.
- [x] Escopo sistêmico LC Hermes explicitado.
