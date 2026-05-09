# Brain Improvement Score — 2026-05-09

## Status geral

Score geral: **88/100**

Leitura executiva: o Hermes Brain está saudável e bem estruturado para uso operacional. A base Bruno/OpenClaw já foi adaptada de forma Hermes-native. As lacunas agora são de maturidade executiva: relatórios, score automatizável, Mission Control read-only, matriz multi-agente, higiene de memória e auditorias recorrentes.

## Evidência usada

- Estado de referência: `origin/main` após merge do PR #2, commit `bb7d16d`.
- Health check técnico: `python3 scripts/brain_health_check.py` → `All checks passed`.
- Agentes principais com estrutura completa observada:
  - `agentes/hermes-geral/`;
  - `agentes/lk/`;
  - `agentes/zipper/`;
  - `agentes/spiti/`.
- Contagem observada no Brain:
  - `agentes/`: 24 Markdown files;
  - `areas/`: 92 Markdown files;
  - `empresa/`: 24 Markdown files;
  - `seguranca/`: 2 Markdown files;
  - `skills/`: 5 Markdown files;
  - rotinas de Operações: 22;
  - templates de Operações antes desta rodada: 2.
- Gap analysis Bruno/Hermes: `/opt/data/hermes_bruno_ingest/bruno_lesson_gap_analysis_20260509.md`, 495 linhas, secret scan `possible_secrets 0`.

## Resultado por dimensão

### 1. Identidade e agentes — 94/100

Fato: os quatro agentes principais têm documentação operacional completa: `SOUL.md`, `AGENTS.md`, `TOOLS.md`, `USER.md`, `MEMORY.md` e `HEARTBEAT.md`.

Interpretação: a base está madura. O próximo ganho é consistência fina entre identidade, memória persistente do Hermes e regras por negócio.

Melhoria recomendada: incluir auditoria de identidade no score recorrente.

### 2. MAPAs e navegação — 90/100

Fato: o Brain tem `areas/`, `empresa/`, mapas por negócio, índices de rotinas e documentação de operações.

Interpretação: a navegação está funcional, mas ainda pode ganhar detecção de pasta/arquivo órfão e exigência formal de MAPA/README para novas pastas operacionais.

Melhoria recomendada: estender health check/score para detectar órfãos e links não indexados.

### 3. Rotinas e crons — 84/100

Fato: há rotinas documentadas em `areas/operacoes/rotinas/` e índice global em `empresa/rotinas/_index.md`. O próprio índice avisa que rotina documentada não prova cron ativo.

Interpretação: a documentação está boa; o risco é confundir rotina com execução real. Crons e runtime precisam continuar sendo verificados antes de qualquer afirmação.

Melhoria recomendada: criar relatório “rotinas documentadas vs crons reais” quando houver rodada de automação.

### 4. Skills e procedimentos — 86/100

Fato: há skills canônicas e rotinas documentadas; a skill `bruno-openclaw-hermes-brain-adaptation` já reconhece o novo formato do upload Bruno.

Interpretação: a disciplina existe. Falta score específico para skill drift: caminhos antigos, ferramentas indisponíveis, duplicação entre rotina e skill.

Melhoria recomendada: adicionar seção de “skill drift” no score recorrente.

### 5. Segurança, secrets e aprovações — 91/100

Fato: há docs em `seguranca/`, Doppler como fonte de secrets, secret scan usado nas rodadas e guardrails fortes para produção/infra/banco/ações externas.

Interpretação: a segurança está acima da média. A lacuna é rotina mensal de revisão de scopes, prompt injection e recovery por sistema crítico.

Melhoria recomendada: criar `security-checkup.md` na próxima rodada P1.

### 6. Integrações — 88/100

Fato: o Brain documenta integrações por ferramenta e separa read-only, write, external-send e admin/destructive em várias rotinas.

Interpretação: a base está madura. Falta um template único para nova integração e inventário executivo de scopes por ferramenta.

Melhoria recomendada: criar `empresa/integracoes/_templates/nova-integracao.md`.

### 7. Roadmap, changelog e pendências — 86/100

Fato: `ROADMAP-30-DIAS-HERMES.md`, `CHANGELOG.md`, `empresa/gestao/pendencias.md` e `memories/pending.md` existem e registram histórico e pendências.

Interpretação: rastreabilidade boa, mas pendências antigas e novas precisam de higienização periódica para não misturar urgência real com histórico.

Melhoria recomendada: criar rotina de retomada/higiene de pendências com status: ativo, bloqueado, histórico, arquivado.

### 8. Links, arquivos e consistência — 85/100

Fato: `brain_health_check.py` passou sem falhas.

Interpretação: tecnicamente consistente. A pontuação não é 100 porque ainda falta uma camada executiva que consolide consistência, riscos e próximos passos em relatório único.

Melhoria recomendada: usar `report-health-executivo.md` e evoluir para script depois.

## Correções seguras recomendadas

1. Criar e manter matriz multi-agente.
   - Risco: baixo/documental.
   - Motivo: evita criar agentes permanentes sem necessidade real.

2. Criar PRD Mission Control read-only.
   - Risco: baixo/documental.
   - Motivo: resolve pendência explícita e evita construir UI cedo demais.

3. Criar template health executivo.
   - Risco: baixo/documental.
   - Motivo: transforma checks técnicos em decisão executiva.

4. Criar rotina de higiene de memória e pendências.
   - Risco: baixo/documental.
   - Motivo: reduz conflito entre memory tool, Brain, memories e histórico.

## Itens que exigem aprovação Lucas

- Ativar cron semanal de Mission Control ou retomada de PRDs.
- Criar UI/app visual de Mission Control.
- Conectar novos canais como WhatsApp, email, grupos ou tópicos com envio externo.
- Alterar VPS/Docker/Traefik/volumes/redes/runtime.
- Mutar bancos, campanhas, mensagens externas ou dados de clientes/colecionadores.

## Próximo passo recomendado

Concluir a rodada P0 documental com:

- matriz `area-skill-subagent-agent-decision.md`;
- PRD `mission-control-prd.md`;
- template `report-health-executivo.md`;
- este score manual.

Depois, a próxima rodada P1 deve criar higiene de memória, security checkup, template de integração nova e template de canal novo.

## Não alterado

- Produção.
- VPS/Docker/Traefik/volumes/redes.
- Bancos.
- Secrets.
- Campanhas.
- WhatsApp/email/posts.
- Clientes/colecionadores.
