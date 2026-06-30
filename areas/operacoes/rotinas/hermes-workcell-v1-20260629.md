# Hermes Workcell v1 — Onda 0/Onda 1

Data: 2026-06-29  
Status: aprovado por Lucas para **piloto local/read-only/documental**.  
Não cria agente, worker, cron ou runtime novo.

## Objetivo

Transformar capacidade instalada do Hermes em uma esteira simples de trabalho:

`pedido → escopo/card → planner → executor → QA/reviewer → receipt → Mesa só se decisão/bloqueio`

## Papéis

| Papel | Responsabilidade | Pode ser |
|---|---|---|
| Planner | entende pedido, checa histórico/fonte, define escopo e risco | Hermes Geral ou especialista |
| Executor | realiza ação local/read-only/local-write aprovada ou prepara packet | agente atual/subagente |
| QA/Reviewer | verifica artefatos, gates, riscos e ausência de extrapolação | subagente independente ou checagem direta |
| Recorder | registra receipt/handoff e próximo gatilho | Hermes Geral/Memory OS writer |

## Fluxo obrigatório para tarefa material

1. **Escopo**
   - O que foi aprovado?
   - O que está explicitamente fora?
   - Qual risco A0-A4?

2. **Plano curto**
   - 3 a 6 passos no máximo.
   - Sem inventar runtime novo.

3. **Execução**
   - Fazer apenas o aprovado.
   - Se aparecer ação sensível, parar e criar approval packet.

4. **QA/review**
   - Verificar paths, conteúdo, health/varredura de credenciais quando aplicável.
   - Para entrega importante, preferir subagente QA independente.

5. **Receipt/handoff**
   - Registrar o que foi feito, fonte, não-ações, rollback e próximo passo.

6. **Resposta Telegram**
   - Resultado executivo primeiro.
   - Evidência resumida.
   - Paths como suporte, não como substituto do resultado.

## Critério de uso de subagente QA

Use QA independente quando houver:

- 3+ artefatos;
- governança/rotina nova;
- risco de confundir documentação com runtime;
- impacto em futuras decisões de agentes;
- skill/Brain policy;
- qualquer entrega que Lucas usará como padrão recorrente.

## Anti-padrões

- Criar um “mega agente” Workcell.
- Criar cron para cada etapa.
- Exigir card para pergunta simples.
- Mais processo que entrega.
- Registrar caminho sem explicar resultado.
- Considerar docs como runtime active.

## Piloto Onda 1

O primeiro piloto real é a própria execução aprovada por Lucas em 2026-06-29:

- criar Task OS Minimalista;
- criar Workcell v1;
- criar Telegram Executive UX v2;
- especificar Ops Bridge read-only;
- gerar inventário Skill Surface Diet read-only;
- QA independente;
- receipt final.

Ver relatório: `reports/governance/hermes-power-user-onda0-onda1-pilot-2026-06-29.md`.
