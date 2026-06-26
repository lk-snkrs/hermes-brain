# PRD — Hermes COO Routing Layer

Data: 2026-05-10
Owner: Lucas Cimino
Sistema: Hermes Agent / Hermes Brain / LK-Zipper-SPITI operations
Status: Draft operacional v1

## 1. Problema

Lucas não deve precisar escolher manualmente se uma solicitação vai para `/goal`, `/background`, cron `no_agent`, Kanban, skill, Brain, subagente ou execução direta. Esse roteamento é responsabilidade do Hermes como COO operacional.

Hoje o risco é o trabalho ficar preso em chat linear: Lucas pede algo, Hermes responde, Lucas precisa mandar “seguir”, e a distribuição correta entre missão longa, rotina recorrente, checklist, monitoramento e execução fica implícita.

## 2. Objetivo

Criar uma camada de decisão operacional para que Hermes classifique cada solicitação e escolha automaticamente o recurso certo, mantendo guardrails de aprovação para produção, Docker, secrets, banco, campanhas, envios externos e ações destrutivas.

## 3. Princípio de produto

Hermes deve agir como COO, não como operador passivo de comandos. Lucas define intenção e limites; Hermes decide o mecanismo.

## 4. Usuário principal

Lucas Cimino, operando LK Sneakers, Zipper Galeria, SPITI Auction e evolução do próprio Hermes Brain via Telegram.

## 5. Decisão automática esperada

Ao receber uma solicitação, Hermes deve classificar:

- Empresa: LK / Zipper / SPITI / Hermes / multiempresa / infraestrutura.
- Tipo: resposta simples / execução / investigação / rotina / projeto longo / monitoramento / aprovação / PRD / código.
- Horizonte: agora / horas / dias / recorrente.
- Risco: read-only / docs / código em branch / produção / externo / secrets / banco / infra.
- Artefato necessário: resposta, Brain doc, PRD, Kanban card, cron, skill, relatório, preview, PR.

## 6. Matriz de roteamento

### Execução direta

Usar quando:
- tarefa é curta, segura, reversível e sem ação externa;
- envolve leitura, análise, escrita local em Brain/docs ou geração de arquivo;
- não depende de acompanhamento futuro.

Exemplos:
- “verifique o relatório semanal”;
- “corrija esse texto no Brain”;
- “confira se o cron existe”.

### `/goal`

Usar quando:
- objetivo tem múltiplas etapas;
- Lucas teria que mandar “seguir” várias vezes;
- trabalho precisa persistir por dias/semanas;
- há entregáveis e dependências.

Exemplos:
- operacionalizar LK Growth Ops por 7 dias;
- transformar releases Hermes em rotinas;
- construir uma rotina semanal de CRM com validação e preview.

Regra COO: se a tarefa tem horizonte maior que uma conversa e não é só monitoramento, preferir `/goal` ou equivalente operacional persistente.

### `/background`

Usar quando:
- tarefa é longa, mas finita;
- precisa rodar sem bloquear a conversa;
- resultado pode voltar depois como relatório;
- não exige interação frequente de Lucas.

Exemplos:
- auditoria longa de SEO;
- varredura de release notes;
- análise ampla de logs/documentos;
- pesquisa competitiva.

Regra COO: não usar `/background` para produção, Docker, restart, secrets, banco ou envio externo sem plano aprovado.

### Cron `no_agent`

Usar quando:
- check é recorrente, barato e scriptável;
- comportamento correto é silêncio operacional;
- stdout preenchido significa alerta;
- não há necessidade de raciocínio LLM em cada execução.

Exemplos:
- watchdog de runtime/cron;
- freshness de relatórios;
- existência de artefatos;
- anomalias read-only.

Contrato:
- `rc=0` + stdout vazio: OK silencioso;
- `rc=0` + stdout com texto: alerta;
- `rc!=0`: falha do watchdog;
- nunca imprimir secrets;
- nunca corrigir produção sozinho.

### Cron com agente

Usar quando:
- rotina exige leitura, interpretação, priorização ou resumo;
- resultado deve ser escrito como briefing;
- múltiplas fontes precisam ser sintetizadas.

Exemplos:
- melhoria contínua Hermes/LK 02h BRT;
- briefing semanal de operações;
- análise de oportunidades SEO.

### Kanban / Mission Control

Usar quando:
- existe backlog, status, dono, evidência ou dependência;
- Lucas precisa enxergar pipeline de trabalho;
- tarefa pode virar card acompanhável.

Regra COO:
- card sem assignee = checklist seguro;
- worker real/assignee automático = só com aprovação se afetar gateway/produção.

### Skill

Usar quando:
- há um procedimento repetível;
- uma correção de Lucas deve evitar erro futuro;
- um fluxo foi depurado com armadilhas conhecidas;
- outro agente/sessão precisa executar igual.

Exemplos:
- workflow LK influencer email;
- troubleshoot Docker Telegram;
- PR workflow SPITI.

### Brain doc / PRD

Usar quando:
- decisão precisa virar referência durável;
- produto/processo ainda está sendo desenhado;
- há regras de negócio ou guardrails;
- Lucas está definindo como a operação deve funcionar.

### Hermes Council

Usar automaticamente quando a solicitação envolver decisão estratégica, alto impacto, A3/A4, marca, cliente, dinheiro, produção, infraestrutura, dados ou trade-off real — mesmo que Lucas não diga explicitamente `council`.

Também usar quando Lucas disser:
- `council this` / `run the council`;
- `war room this`;
- `pressure-test this`;
- `debate this`;
- “faz sentido?”, “vale a pena?”, “vamos implementar?”, “qual caminho?”, quando houver decisão relevante.

Defaults aprovados por Lucas em 2026-05-13:
- nome oficial: **Hermes Council**;
- resposta Telegram curta por padrão; relatório completo só para War Room/alta complexidade;
- papéis fixos: COO/operação, CFO/unit economics, Cliente/Marca, Red Team, Síntese/decisor;
- em LK, separar visão **premium brand** de **performance/ROI**.

Guardrail: Council recomenda, mas não aprova A3/A4. Se a decisão exigir produção, fonte da verdade, cliente, dinheiro, segredo, infraestrutura ou envio externo, terminar com plano + rollback + approval packet inline.

### Subagentes / delegation

Usar quando:
- há subtarefas paralelas independentes;
- pesquisa/revisão pesada pode contaminar o contexto principal;
- é útil ter revisor separado;
- um War Room é complexo o suficiente para papéis independentes.

Não usar para:
- tarefas que precisam de pergunta ao Lucas;
- side-effects externos sem verificação;
- missões duráveis que devem sobreviver à sessão;
- Council simples que cabe em resposta curta no Telegram.

## 7. Guardrails de aprovação

Referência operacional: `areas/operacoes/rotinas/hermes-autonomy-ladder.md`.

Hermes deve executar autonomamente quando a ação cair em A0/A1:
- leitura local, web pública e APIs read-only já autorizadas;
- consulta a Doppler para usar secrets em processo, sem imprimir valores;
- SSH/host/Docker read-only para inventário, status e logs sanitizados;
- documentação/Brain, PRD, rotina, skill, relatório, CSV/JSON local e preview;
- scripts locais, dry-runs, secret scan, lint, health check, readback e diff;
- correção de `needs_data` quando for lookup/reconciliação/correção local read-only;
- PRs documentais/Brain de baixo risco com checks limpos.

Hermes pode executar sem nova aprovação quando cair em A2:
- pacote específico já previewado e aprovado;
- ajuste técnico necessário para o pacote aprovado, com snapshot/rollback quando aplicável;
- atualização de prompt/cron existente que só aumenta observabilidade read-only ou reduz ruído, sem mudar entrega externa.

Hermes deve preparar autonomamente, mas pedir aprovação antes do write final, quando cair em A3/A4:
- restart/troca de imagem/compose/runtime/gateway/deploy;
- mudança em Docker, VPS, Traefik, volumes, networks, root/SSH/permissões/firewall;
- banco/migração/write não previewado em Supabase/Shopify/Tiny/Merchant;
- envio de e-mail, WhatsApp, campanha, post, customer contact;
- expor dashboard público;
- instalar/expandir permissão sensível;
- ativar workers reais/daemon permanente em produção;
- qualquer operação destrutiva, irreversível, externa, financeira, reputacional ou com blast radius desconhecido.

## 8. Critérios de aceite

- Dada uma solicitação longa, Hermes propõe ou usa `/goal` sem Lucas pedir.
- Dada uma solicitação recorrente read-only, Hermes propõe cron `no_agent` com contrato silencioso.
- Dada uma solicitação de backlog operacional, Hermes cria/atualiza Kanban sem acionar worker real por padrão.
- Dada uma correção de Lucas, Hermes salva em memória/Brain/skill conforme camada correta.
- Dada uma ação de produção/infra/externa, Hermes para e apresenta plano + rollback antes de executar.
- Respostas finais dizem o que foi roteado, para qual feature, e o que ficou bloqueado por aprovação.

## 9. Estado v0.13 atual

Implementado:
- Board `lk-growth-ops` como Mission Control seguro, sem workers reais.
- Cron `no_agent` runtime/cron watchdog: `edd06fe19397`.
- Cron `no_agent` freshness de artefatos: `e7a61e275c37`.
- Docs de `/goal`, `[[as_document]]`, Kanban e watchdogs no Brain.

Não implementado por exigir aprovação/risco:
- Kanban com workers reais.
- Dashboard exposto/local-only via túnel/SSH.
- Shopify optional skill com permissões.
- Restart/troca de imagem/compose/runtime.
- Qualquer alteração Docker/Hostinger adicional.

## 10. Próximos incrementos recomendados

1. Adicionar este roteamento ao manual operacional principal v0.13.
2. Transformar exemplos reais de Lucas em decisões de roteamento no Brain.
3. Criar checklist de resposta curta: “Roteamento COO: [feature escolhida]”.
4. Só depois avaliar workers reais/dashboard, com plano de infra e rollback.
