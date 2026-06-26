# Hermes Orquestração — Fase 8: Proatividade supervisionada e handoffs maduros

Data: 2026-05-24  
Status: aberto para execução local/read-only  
Owner: Hermes Geral / COO  
Base: Task Router v1 operacional, Fase 7B handoff packets, UX limpa de cron/Telegram

## Objetivo

Levar a orquestração de “roteia com segurança” para “coordena como COO”: especialistas com rituais claros, handoffs auditáveis, Mesa COO mais útil e proatividade silenciosa quando não há exceção.

Esta fase não autoriza produção, envio externo, Docker/VPS, publicação, alteração de cron ou contato com cliente. Essas ações continuam exigindo aprovação explícita por escopo.

## Definição de pronto

Fase 8 estará pronta quando:

1. Cada especialista ativo/documentado tiver um contrato mínimo de handoff:
   - escopo;
   - fontes permitidas;
   - output path;
   - quando escalar para Lucas;
   - o que nunca fazer sem aprovação;
   - formato de handoff.
2. A Mesa COO produzir decisões acionáveis em formato 1/N com botões, sem metadados técnicos.
3. O Task Router cobrir lacunas de especialistas secundários, principalmente Zipper e LK Ops.
4. Handoffs relevantes forem salvos no Brain, não apenas no chat.
5. Proatividade for silenciosa por padrão: alertar só decisão, exceção, bloqueio ou oportunidade clara.
6. Testes/gates locais comprovarem que a UX limpa e o bloqueio de side effects continuam funcionando.

## Pacotes de trabalho

### P8.1 — Contrato de handoff por especialista

Criar ou revisar contratos operacionais para:

- Hermes Geral / COO;
- LK Growth;
- Mordomo;
- SPITI;
- Zipper documental/read-only;
- Operações Hermes.

Entrega local:

- atualizar `agentes/*/AGENTS.md`, `HEARTBEAT.md` ou criar documento de handoff quando necessário;
- sem mudar runtime, cron ou gateway.

### P8.2 — Zipper v1 documental/read-only

Fechar o buraco atual entre “Zipper existe no Brain” e “Zipper tem comportamento operacional previsível”.

Escopo permitido:

- mapear fontes aprovadas: CRM/Main, `vendas_tango`, Brain institucional;
- criar matriz de tipos de pedido Zipper;
- definir templates de rascunho interno e relatório;
- bloquear contato externo, preço, proposta, artista/colecionador e logística sensível sem aprovação.

Não incluso nesta fase sem nova aprovação:

- criar bot/runtime dedicado Zipper;
- conectar WhatsApp/e-mail;
- mudar credenciais, gateway, Docker ou cron.

### P8.3 — Mesa COO v2

Transformar a Mesa COO em uma fila de decisões executivas mais parecida com “conselho operacional”:

- 1 decisão por mensagem;
- máximo 4 decisões por ciclo;
- botões nativos;
- motivo, ação proposta, risco e bloqueio;
- nenhuma linha de `Cronjob Response`, `job_id`, JSON ou marcador técnico;
- quando a decisão envolve especialista, incluir destino e output esperado.

### P8.4 — Handoff ledger

Criar um ponto único no Brain para registrar handoffs relevantes:

- decisões duráveis;
- packets preparados;
- outputs de especialista;
- aprovações/bloqueios;
- receipts de writes aprovados;
- rollback ou próxima ação.

Formato preferido: arquivos markdown por data/área, com template simples e pesquisável.

### P8.5 — Testes de regressão e gates

Manter TDD:

- RED: adicionar testes para lacunas antes de mudar código;
- GREEN: implementar a menor mudança;
- REFACTOR: limpar docs/skills;
- verificar com suíte focada.

Gates mínimos:

- `pytest tests/cron/test_scheduler.py tests/agent/test_lucas_task_router_preflight.py`
- verificação de docs/Brain quando arquivos forem alterados;
- secret scan focado nos arquivos modificados;
- confirmar zero writes externos.

## Ordem sugerida

1. P8.1: contratos de handoff.
2. P8.2: Zipper read-only, porque é a maior lacuna de roteamento.
3. P8.4: handoff ledger para não perder outputs.
4. P8.3: Mesa COO v2 usando os contratos/ledger.
5. P8.5: regressão final e relatório.

## Riscos

- Criar proatividade demais e gerar ruído no Telegram.
- Especialista executar fora do escopo por conveniência.
- Handoff virar burocracia e não fonte de verdade.
- Misturar documentação com runtime real.

Mitigação:

- silent-OK;
- approval gates A3/A4;
- registrar o mínimo útil;
- diferenciar docs, runtime e crons vivos.

## Próxima ação imediata

Começar por P8.1 e P8.2 em modo local/read-only:

1. auditar `agentes/*/AGENTS.md` e `HEARTBEAT.md`;
2. criar contrato de handoff padrão;
3. aplicar primeiro no Zipper documental/read-only;
4. só depois decidir se vale runtime dedicado Zipper.
