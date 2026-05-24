# Memories — MAPA

Escopo: memória operacional durável do Hermes Brain. Esta pasta não é transcrição de chat; é a camada de contexto que deve sobreviver a reinício, compactação e troca de agente.

## Camadas Bruno/OpenClaw adaptadas

- `hot.md` — contexto quente/current: prioridades, riscos, decisões recentes e bloqueios que o Hermes deve carregar antes de agir.
- `daily/` — notas diárias curadas no formato `YYYY-MM-DD.md`, com decisões, entregas, pendências e aprendizados do dia.
- `decisions.md` — decisões duráveis globais que não pertencem claramente a uma única área.
- `pending.md` — pendências globais abertas.
- `lessons.md` — aprendizados recorrentes e lições operacionais.
- `lk.md`, `zipper.md`, `spiti.md` — memória por empresa quando o fato não exige rotina/decisão própria.
- `consolidation_weekly/` — consolidações semanais históricas.

## Regra de uso

Se Lucas corrigir, aprovar ou decidir algo que pode ser necessário depois, salvar em pelo menos um destino estruturado:

1. daily note do dia em `daily/YYYY-MM-DD.md`;
2. arquivo vivo na área correspondente (`areas/**/decisions/`, `rotinas/`, `receipts/`, `reports/` etc.);
3. `hot.md` se o assunto ainda estiver ativo/current;
4. índice/MAPA local para o próximo agente encontrar.

## Anti-padrão

- Deixar decisão apenas no Telegram/chat.
- Usar compactação como fonte de verdade.
- Salvar tudo em um único arquivo gigante.
- Guardar payload bruto, secret, PII ou log completo em memória versionável.
