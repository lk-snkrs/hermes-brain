# Brain OS — Manifest Semantics

**Atualizado em:** 2026-06-11T13:55:54.899501+00:00
**Escopo:** semântica operacional para não confundir hub vivo, receipt, backup e artefato.

## Regra curta

Nem todo `manifest.json` é um hub canônico vivo. O significado depende do caminho, do schema e da intenção.

## Classes

### 1. Hub canônico vivo

**Exemplo de caminho:** `areas/<area>/.../projetos/<slug>/manifest.json`

Indica uma pasta canônica de projeto com pacote mínimo:

- `README.md`
- `CURRENT_STATE.md`
- `DECISIONS_AND_GUARDRAILS.md`
- `ARTIFACT_INDEX.md`
- `TIMELINE.md`
- `NEXT_STEPS.md`
- `manifest.json`

Uso: responder “onde está o estado atual?”, orientar handoff, consolidar decisões e apontar fontes.

### 2. Receipt / evidência

**Exemplo de caminho:** `reports/governance/receipts/...` ou pastas de receipts.

Indica prova de execução, verificação ou decisão histórica. Não é fonte viva por padrão.

Uso: auditar o que aconteceu, não decidir estado atual sem reconciliação.

### 3. Backup / snapshot

**Exemplo de caminho:** `backups/...`.

Indica preservação de estado anterior ou pacote de rollback. Não deve ser interpretado como versão ativa.

Uso: rollback, comparação e auditoria.

### 4. Artifact/report/script indexado

**Exemplo de caminho:** `reports/...`, `scripts/...`, `work/...`, `tmp/...`.

Indica material útil que pode justificar um hub, mas não substitui `CURRENT_STATE.md` do hub.

## Precedência para responder perguntas

1. Fonte viva externa, quando a pergunta depende de estado atual.
2. `CURRENT_STATE.md` do hub canônico.
3. `DECISIONS_AND_GUARDRAILS.md` do hub.
4. `ARTIFACT_INDEX.md` e `TIMELINE.md`.
5. Receipts/reports/backups como evidência histórica.
6. Chat/session summaries apenas como pistas.

## Guardrails

- Não usar backup como estado atual.
- Não usar receipt como aprovação atual sem verificar escopo e data.
- Não tratar scanner score alto como autorização para ação externa.
- Não mover/apagar histórico para “limpar” o Brain OS.
- Não copiar secrets para manifests ou índices.

## Critério para promover artefato a hub

Promover quando houver pelo menos 3 sinais:

- múltiplos receipts/reports recorrentes;
- dono operacional claro;
- risco de fonte viva vs snapshot;
- decisões e guardrails recorrentes;
- múltiplos agentes/perfis usando o tema;
- Lucas perguntou/corrigiu o estado recentemente;
- volume alto ou risco externo.
