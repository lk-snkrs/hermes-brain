# Mission Control ↔ Mesa COO alignment

Data: 2026-05-19
Owner: Mission Control / Hermes Geral
Status: PRD/milestone seguro; sem deploy/UI nesta alteração

## Direção

Mission Control deve representar a mesma verdade operacional da Mesa COO diária no Telegram. A UI atual não deve ganhar mais cards por módulo; deve reduzir para decisão, bloqueio, ação segura, risco e evidência.

## Fonte canônica de produto

- PRD de rebuild: `/opt/data/hermes_bruno_ingest/mission-control-cimino/docs/rebuild/mission-control-zero-based-rebuild-prd-2026-05-19.md`.
- Rotina Telegram: `areas/operacoes/rotinas/mesa-coo-diaria-telegram-2026-05-19.md`.
- Runtime/canais: `areas/operacoes/rotinas/runtime-profile-channel-inventory-2026-05-19.md`.
- Skill audit: `empresa/skills/skill-audit-2026-05-19.md`.

## Home v1 desejada

1. **Decisão agora**
   - uma decisão principal;
   - recomendação;
   - fonte;
   - gate exigido;
   - CTA de preparação segura, não write externo.

2. **Bloqueado por Lucas**
   - ações que não andam sem payload/alvo/aprovação;
   - alternativa segura disponível.

3. **Hermes pode fazer sozinho**
   - read-only;
   - draft;
   - packet;
   - simulação;
   - documentação/Brain.

4. **Riscos**
   - empresa/sistema;
   - risco se ignorado;
   - fonte/freshness.

5. **Fontes e receipts**
   - cronjob list;
   - Brain docs;
   - reports;
   - receipts do Work Kernel;
   - estado de Mission deploy quando aplicável.

## Não fazer

- Não empilhar novos módulos sem passar pela Mesa.
- Não transformar simulação em execução produtiva.
- Não autorizar writes externos pela UI.
- Não usar marker/release como substituto de utilidade para Lucas.

## Milestone seguro sugerido

`feat/mission-mesa-coo-home-v1`

Escopo:

- Criar dataset local `mesaCooSnapshot` derivado dos docs/fixtures atuais.
- Trocar home para os 5 módulos acima.
- Manter Work Kernel, Approval Center preview-first e `externalWritesEnabled: false`.
- Mover catálogo/roadmap técnico para Advanced.
- Validar browser + build + auth gates.
- Deploy só com aprovação/autor correto.

## Critério de aceite

Lucas deve abrir Mission Control e responder em menos de 60 segundos:

- qual decisão precisa tomar;
- o que está bloqueado por ele;
- o que Hermes fará sozinho sem risco;
- onde está a fonte.
