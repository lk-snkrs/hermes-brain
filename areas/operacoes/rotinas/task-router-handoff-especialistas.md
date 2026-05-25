# Rotina — Task Router e Handoff de Especialistas

Data: 2026-05-24  
Status: Fase 1 documental aprovada  
Relacionado:
- `empresa/contexto/organograma-orquestrador-tarefas-hermes.md`
- `empresa/contexto/matriz-roteamento-tarefas-hermes.md`
- `empresa/contexto/task-router-hermes.md`
- `templates/handoff-especialista.md`

## Objetivo

Garantir que o Hermes Geral distribua tarefas para o especialista correto, evite executar no perfil errado e receba handoff suficiente para manter a Grande Mente atualizada.

## Quando usar

Use esta rotina quando Lucas pedir qualquer coisa que pareça pertencer a um domínio especialista:

- LK Growth: conteúdo, blog, source page, SEO, CRO, GEO, GMC, analytics.
- Mordomo: WhatsApp pessoal, agenda, follow-ups, intake.
- SPITI: Hub, leilões, lotes, CRM, Financial, Growth SPITI.
- Zipper: obras, artistas, colecionadores, CRM, comunicação, vendas.
- Hermes Ops: crons, Brain hygiene, skills, watchdogs, runtime.
- Tecnologia/Infra: GitHub, deploy, VPS, Docker, Mission Control.

## Fluxo

### 1. Classificar

Hermes Geral identifica:

- empresa/área;
- tipo de tarefa;
- risco A0-A4;
- especialista dono;
- output esperado;
- approval boundary.

### 2. Consultar matriz

Abrir `empresa/contexto/matriz-roteamento-tarefas-hermes.md` quando houver dúvida ou quando for tarefa operacional sensível.

### 3. Distribuir ou executar

- Se a tarefa é central/governança/read-only simples: Hermes Geral pode executar.
- Se a tarefa tem especialista dono: distribuir para o especialista.
- Se o especialista está indisponível: preparar briefing/requirements e marcar `executor_pendente`.
- Se há ação A3/A4 sem aprovação: preparar packet ou bloquear.

### 4. Verificar output

Antes de reportar:

- o arquivo existe;
- o link/receipt abre ou foi lido;
- os guardrails foram respeitados;
- não houve write externo não aprovado;
- o próximo passo está claro.

### 5. Registrar handoff

Usar `templates/handoff-especialista.md` quando houver:

- conteúdo criado/revisado/aprovado/enviado;
- decisão operacional;
- approval packet;
- receipt/rollback/evidência;
- write externo;
- risco/bloqueio;
- aprendizado/correção de Lucas;
- output que precisa sobreviver ao chat.

O handoff pode ser:

- arquivo separado no Brain;
- seção no relatório/packet;
- atualização de rotina/skill;
- registro em fechamento diário.

## Padrões por especialista

### LK Growth

- Rota: `lk-growth-content` ou `lk-growth-analytics-readonly`.
- Output padrão: `areas/lk/sub-areas/growth/drafts/` ou `reports/`.
- Handoff obrigatório para conteúdo, packets, SEO/CRO/GEO/GMC e qualquer approval.
- Proibido publicar/alterar Shopify/GMC/Klaviyo/Meta/theme sem aprovação explícita.

### Mordomo

- Rota: `mordomo-personal-intake`.
- Output padrão: alertas, drafts, eventos/follow-ups permitidos, registros no Brain quando durável.
- Handoff obrigatório para exceções, decisões, contatos sensíveis e aprendizados de tom.

### SPITI

- Rota: `spiti-os`.
- Output padrão: PRD, análise, relatório, branch/PR quando aprovado.
- Handoff obrigatório para Hub/Financial/Growth, lote/lance, riscos e PRs.
- Regra: silêncio é melhor que dado errado.

### Zipper

- Rota: `zipper-os-readonly-comm-crm`.
- Output padrão: análise, draft, relatório, documentação.
- Handoff obrigatório para propostas, comunicação, logística, relatórios e decisões.
- Enquanto não houver profile dedicado, não fingir que existe runtime Zipper operacional.

### Hermes Ops / Tecnologia

- Rota: `hermes-ops-brain-governance` ou `tech-infra-mission-control`.
- Output padrão: PRD, plano, relatório, patch documental, PR/branch.
- Handoff obrigatório para mudanças de governança, skills, crons, runtime, deploys e riscos.

## Anti-padrões

- Fazer conteúdo LK no Hermes Geral quando LK Growth é o executor.
- Deixar output de especialista apenas no chat local.
- Criar cron sem kill criteria.
- Dizer que algo roda sem verificar runtime real.
- Misturar fontes LK/Zipper/SPITI.
- Tratar `/background`, “seguir” ou botão genérico como autorização para write externo.
- Entregar caminho interno quando Lucas precisa de arquivo/link/preview.

## Checklist de conclusão

Antes de responder a Lucas:

- [ ] Contexto e executor corretos.
- [ ] Output/arquivo/link verificado.
- [ ] Produção/externo não executado sem aprovação.
- [ ] Handoff criado ou explicitamente dispensável.
- [ ] Próxima decisão formulada de forma curta.
