# Projeto — Hermes Brain Improvement System

## Status

Em implantação documental.

Esta primeira versão adiciona rotina, templates e critérios de score para transformar material externo em melhoria rastreável do Hermes Brain.

## Contexto

Lucas enviou o pacote Bruno/OpenClaw atualizado em 2026-05-08 e pediu leitura pasta por pasta, documentação, reflexão e PRD.

A análise local gerou:

- `/opt/data/hermes_bruno_ingest/bruno_upload_20260508_204305_analysis/bruno_updated_upload_documentation.md`;
- `/opt/data/hermes_bruno_ingest/bruno_lesson_by_lesson.md`;
- `/opt/data/hermes_bruno_ingest/bruno_to_hermes_adaptation_plan.md`;
- `/opt/data/hermes_bruno_ingest/PRD_bruno_openclaw_to_hermes.md`.

Conclusão: o pacote está bom como material estratégico, mas não deve ser copiado. O Hermes Brain já tem estrutura própria mais rica. O ganho correto é criar um sistema de ingestão, comparação, PRD e melhoria contínua.

## Objetivo

Criar um processo repetível para que novos materiais enviados ao Hermes sejam tratados assim:

```text
material externo
→ extração segura
→ inventário
→ leitura estruturada
→ comparação com Hermes Brain
→ matriz aplicar/adaptar/deferir/rejeitar
→ PRD
→ branch/PR quando fizer sentido
→ aprovação Lucas antes de produção
```

## Entregas desta rodada

- Rotina: `areas/operacoes/rotinas/material-ingest-to-prd.md`.
- Rotina: `areas/operacoes/rotinas/brain-improvement-score.md`.
- Rotina: `areas/operacoes/rotinas/retomada-planos-prds.md`.
- Template: `areas/operacoes/templates/matriz-decisao-bruno-hermes.md`.
- Template: `areas/operacoes/templates/prd-hermes-brain-improvement.md`.
- Projeto: este documento.
- Índices: `areas/operacoes/MAPA.md`, `empresa/rotinas/_index.md`, roadmap e changelog.

## Não objetivos

- Não reorganizar o Brain inteiro.
- Não criar novo runtime ou agente permanente.
- Não criar Mission Control agora.
- Não mexer em Docker/VPS/Traefik/volumes/redes.
- Não alterar campanhas, WhatsApp, email, posts ou contato com clientes.
- Não fazer merge em `main` sem aprovação Lucas.
- Não versionar conteúdo bruto de curso/material de terceiros dentro do Brain.

## Princípios

1. Hermes não vira OpenClaw; Hermes adapta apenas o que melhora a operação.
2. Brain é fonte de verdade para regras e procedimentos; Doppler é fonte de verdade para secrets.
3. Material externo entra por análise local segura antes de virar documento versionado.
4. Toda decisão relevante precisa explicar por que aplicar, adaptar, deferir ou rejeitar.
5. Rotina documentada não significa cron ativo.
6. Produção e ações externas exigem aprovação explícita.

## Backlog

### P0 — Feito nesta rodada

- Documentar rotina de ingestão material → PRD.
- Criar template de PRD.
- Criar matriz de decisão Bruno/Hermes.
- Criar rotina de score do Brain.
- Criar rotina de retomada de planos/PRDs.
- Linkar nos índices.

### P1 — Feito na rodada seguinte

- Criar rotina de higiene de memória e pendências.
- Criar rotina de security checkup antes de novas integrações, canais, agents, crons e ações sensíveis.
- Criar template de nova integração.
- Criar template de novo canal/agente/subagent/cron.
- Criar template de resumo de entrega para fechar rodadas com evidência.

### P2 — Próximas rodadas recomendadas

- Testar a rotina `material-ingest-to-prd.md` com um segundo pacote pequeno ou um PRD antigo. — concluído em 2026-05-09 com `reports/material-ingest-to-prd-test-2026-05-09.md`.
- Avaliar script opcional de `brain_improvement_score.py` somente depois de validar melhor o formato manual.
- Avaliar cron semanal de retomada de planos pendentes.
- Transformar as partes mais repetidas em skill canônica, se o fluxo se repetir.

## Critérios de pronto da rodada

- Arquivos criados e indexados.
- Health check do Brain passando.
- Secret scan whole-repo com `possible_secrets 0`.
- Diff revisado.
- PR draft aberto, se GitHub/Doppler disponível.
- Nenhuma alteração produtiva executada.

## Entregas P1 adicionadas

- Rotina: `areas/operacoes/rotinas/memory-hygiene-pendencias.md`.
- Rotina: `areas/operacoes/rotinas/security-checkup.md`.
- Template: `areas/operacoes/templates/nova-integracao.md`.
- Template: `areas/operacoes/templates/novo-canal-agente.md`.
- Template: `areas/operacoes/templates/delivery-summary.md`.

Esses documentos fecham a lacuna entre análise/PRD e operação contínua: antes de criar integrações, canais, agentes, crons ou automações novas, o Brain agora tem uma checagem explícita de segurança, memória e escopo mínimo.

## Entrega P1 aplicada — higiene real de pendências

Em 2026-05-09 a rotina `memory-hygiene-pendencias.md` foi aplicada pela primeira vez sobre o Brain real.

Entregas:

- `empresa/gestao/pendencias.md` reescrito como fila executiva atual.
- `memories/pending.md` compactado para boot mental.
- `reports/memory-hygiene-2026-05-09.md` criado como evidência da revisão.
- Decisão de autonomia documental de baixo risco registrada em decisões permanentes.

Resultado: pendências antigas de 2026-04-19 foram arquivadas/reclassificadas; Meta Ads deixou de aparecer como urgência atual porque a consolidação de 2026-04-28 registra correção em 2026-04-25.


## Entrega P2 aplicada — Rodada G Health Checks

Em 2026-05-09 a Rodada G foi concluída como melhoria estrutural segura do Brain.

Entregas:

- `scripts/brain_health_check.py` expandido para validar secrets, links/anchors, arquivos obrigatórios, agentes, MAPAs, rotinas indexadas e skills canônicas.
- `areas/operacoes/rotinas/brain-health-check.md` atualizado com comando, critérios e limites.
- `reports/brain-health-check-2026-05-09.json` criado como primeiro relatório JSON versionado.
- Pendências e roadmap atualizados para retirar Rodada G da fila ativa.

Resultado: `FAIL=0 WARN=0` em todos os checks, sem alteração em produção/runtime.


## Entrega P2 aplicada — teste Material Ingest to PRD

Em 2026-05-09 a rotina `material-ingest-to-prd.md` foi testada em modo leve usando o PRD interno `areas/operacoes/projetos/mission-control-prd.md`.

Entregas:

- Artefatos locais fora do repo em `/opt/data/hermes_bruno_ingest/material_ingest_to_prd_test_20260509/`.
- Relatório versionado: `reports/material-ingest-to-prd-test-2026-05-09.md`.
- Rotina atualizada para separar modo completo de pacote/ZIP e modo leve para documento único/PRD antigo.
- Pendência ativa removida da fila e próximo passo concentrado em avaliar script executivo para `brain_improvement_score`.

Resultado: o fluxo é útil, mas não deve virar automação cega. O próximo ganho seguro é um script/relatório local read-only; cron, UI ou Telegram recorrente exigem aprovação explícita.
