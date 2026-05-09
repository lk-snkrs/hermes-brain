# Teste da rotina `material-ingest-to-prd.md` — 2026-05-09

## Status

Concluído como teste documental seguro.

## Fonte usada

- Fonte: `areas/operacoes/projetos/mission-control-prd.md`.
- Tipo: PRD antigo/interno do Brain.
- Motivo da escolha: a fila ativa pedia testar `material-ingest-to-prd.md` em um segundo pacote pequeno ou PRD antigo antes de automatizar.
- Artefatos locais fora do repo: `/opt/data/hermes_bruno_ingest/material_ingest_to_prd_test_20260509/`.

## Fluxo aplicado

1. Preparação de área segura fora do repo principal.
2. Inventário da fonte.
3. Extração textual simples.
4. Corpus consolidado.
5. Documentação executiva do material.
6. Matriz aplicar/adaptar/deferir/rejeitar.
7. Revisão do PRD e decisão de próximo passo.

## Resultado

A rotina funcionou para documento único, mas precisa reconhecer formalmente um **modo leve**. Para ZIPs/cursos, o fluxo completo continua correto. Para PRD antigo ou documento único, o mínimo suficiente é:

- inventário simples;
- texto/corpus;
- documentação executiva;
- matriz de decisão;
- revisão ou PRD atualizado;
- secret scan;
- registro no Brain se houver decisão ou pendência.

## Matriz resumida

- Mission Control operacional: **adaptar** como relatório read-only.
- Mission Control visual/UI: **deferir** até haver volume e aprovação de escopo.
- Cron recorrente: **deferir** porque vira runtime/cadência operacional.
- Ações executáveis pelo painel: **rejeitar nesta fase**; relatório pode recomendar, não executar.

## Decisão Hermes-native

Não automatizar ingestão ainda. O próximo ganho seguro é criar um script/relatório executivo para `brain_improvement_score`, usando o health check JSON já versionado, pendências e changelog. Cron, UI e entrega recorrente por Telegram continuam exigindo aprovação explícita.

## Lacunas identificadas

1. `material-ingest-to-prd.md` precisava documentar o modo leve para fonte única.
2. O projeto Hermes Brain Improvement System precisava registrar que o teste P2 foi concluído.
3. A fila de pendências precisava trocar “testar material-ingest” por “avaliar script executivo de score”.

## Verificações

- Nenhum material bruto de terceiro foi versionado.
- Nenhuma produção, VPS, Docker, banco, campanha, mensagem externa, secret ou runtime foi alterado.
- Artefatos locais criados fora do repo de produção.
- Health check/secret scan finais registrados no PR desta rodada.
