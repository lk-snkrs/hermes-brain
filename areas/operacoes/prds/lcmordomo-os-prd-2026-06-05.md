# PRD — LC Mordomo OS

**Versão:** v0.1
**Data:** 2026-06-05
**Dono:** Lucas Cimino
**Sistema:** Hermes Agent / LC Mordomo OS
**Status:** Draft inicial para validação

## 1. Tese do produto

O **LC Mordomo OS** é o sistema operacional pessoal e multiempresa de Lucas Cimino. Ele funciona como uma camada executiva única, com **um agente principal** e **vários subagentes especializados**, cada um com seu próprio contexto, memória, Brain, skills, rotinas, fontes de verdade e limites de aprovação.

Lucas interage com **uma interface só**: o Mordomo central. Internamente, o sistema roteia o trabalho para subagentes por domínio: pessoal, LK, Zipper, SPITI, Hermes/infra e, no futuro, outros braços do ecossistema LC.

A arquitetura segue o princípio aprendido com Bruno Okamoto:

> O agente não é o cérebro. O agente lê, escreve, opera e aprende a partir do cérebro.

E também:

> Agente sem governança vira custo e risco.

## 2. Problema

Lucas tem múltiplas frentes operacionais simultâneas:

- vida pessoal;
- calendário;
- WhatsApp;
- e-mails;
- Zipper Galeria;
- SPITI Auction;
- LK Sneakers;
- Hermes/infra;
- follow-ups;
- CRM global;
- decisões comerciais;
- tarefas recorrentes;
- falhas de automação;
- relações com clientes, fornecedores, equipe e parceiros.

Hoje essas informações chegam por canais diferentes, com contextos diferentes e níveis de urgência diferentes. Sem uma camada executiva forte, o risco é:

- Lucas ser interrompido demais;
- tarefas simples ficarem paradas;
- decisões importantes se perderem;
- follow-ups não acontecerem;
- contexto ficar preso em chat;
- automações virarem ruído;
- agentes/subagentes agirem sem governança.

## 3. Objetivo

Criar um sistema Hermes-native que atue como **secretária executiva + Chief of Staff global + CRM/follow-up layer + roteador de decisão** para Lucas.

O objetivo não é criar vários bots para Lucas conversar. O objetivo é criar uma **interface central única** que protege a atenção de Lucas e usa subagentes como força operacional interna.

## 4. Princípio de arquitetura

### 4.1 Estrutura principal

```text
Lucas
  ⇄ LC Mordomo Central
      ⇄ Subagente Pessoal
      ⇄ Subagente Zipper
      ⇄ Subagente SPITI
      ⇄ Subagente LK
      ⇄ Subagente Hermes/Infra
      ⇄ Subagente CRM/Relacionamentos
      ⇄ Subagente Governança/Qualidade
          ⇄ Skills
          ⇄ Brain
          ⇄ Crons
          ⇄ Ferramentas
          ⇄ Fontes de verdade
```

### 4.2 Regra central

Lucas fala com **o agente principal**.

O agente principal:

- recebe o input;
- classifica o domínio;
- consulta memória/Brain/fonte correta;
- aciona subagente quando necessário;
- consolida resposta;
- decide se Lucas deve ser interrompido;
- prepara decisão, execução, draft, relatório ou follow-up;
- mantém governança.

Os subagentes trabalham internamente. Eles não devem virar uma confusão de interfaces para Lucas.

### 4.3 Contexto mínimo, busca sob demanda

O LC Mordomo OS não usa “memória infinita carregada” como estratégia de inteligência. A vantagem Hermes-native é separar camadas:

- **memória compacta:** regras estáveis, preferências e correções recorrentes;
- **Brain versionado:** contexto rico, decisões, PRDs, rotinas, receipts e relatórios;
- **session_search:** recuperação de histórico de conversa apenas quando necessário;
- **skills:** procedimentos reutilizáveis e verificados;
- **fontes vivas:** APIs, bancos, WhatsApp, e-mail e calendário consultados sob demanda;
- **health checks:** validação de índice, links, secrets, rotinas e drift documental.

Cada subagente deve operar com **Context Budget**: iniciar pelo boot mínimo, ler índices antes de arquivos grandes, buscar fonte específica quando a tarefa exigir, e devolver handoff compacto ao Mordomo Central. Subagente que precisa carregar tudo para funcionar ainda não está pronto para virar runtime separado.

## 5. Agente principal: LC Mordomo Central

### 5.1 Função

O LC Mordomo Central é o **Chief of Staff global** de Lucas.

Responsabilidades:

- proteger a atenção de Lucas;
- rotear qualquer entrada para o domínio correto;
- transformar ruído em ação;
- consolidar decisões;
- priorizar urgências;
- manter memória executiva global;
- coordenar subagentes;
- impedir ações sensíveis sem aprovação;
- criar ou atualizar skills quando padrões se repetem;
- manter Lucas informado apenas quando há decisão, exceção, falha ou aprovação.

### 5.2 O que ele deve entregar para Lucas

- Decisão pronta.
- Draft pronto.
- Alerta acionável.
- Resumo executivo.
- Pedido de aprovação claro.
- Follow-up já executado quando for classe segura.
- Registro silencioso quando não precisa interromper.

### 5.3 O que ele não deve entregar

- Logs crus.
- JSON.
- Dumps de cron.
- Várias filas soltas.
- “Tem coisa para ver” sem ação clara.
- Alertas de sucesso desnecessários.
- Discussão técnica quando Lucas precisa de decisão.

## 6. Subagentes

Cada subagente tem escopo próprio, memória própria, Brain próprio, skills próprias, rotinas próprias e limites próprios.

### 6.1 Subagente Pessoal

**Escopo:** vida pessoal, calendário, compromissos, lembretes, conversas pessoais, logística pessoal.

**Memória própria:**

- preferências pessoais;
- contatos recorrentes;
- tom por contato;
- compromissos e padrões de agenda;
- pendências pessoais.

**Ações autônomas permitidas:**

- criar evento quando data/hora/contexto são claros;
- registrar lembrete;
- preparar follow-up;
- responder internamente ao Lucas com síntese;
- agendar confirmação logística simples quando permitido.

**Ações bloqueadas sem aprovação:**

- enviar WhatsApp/e-mail externo fora de classe segura;
- negociar preço/prazo/condição;
- comprometer Lucas em evento ambíguo;
- lidar com assunto sensível sem validação.

### 6.2 Subagente Zipper

**Escopo:** Zipper Galeria, colecionadores, artistas, obras, PDFs, propostas, feiras, follow-ups e CRM de interesse artístico.

**Memória própria:**

- clientes e colecionadores;
- interesse por artista;
- PDFs enviados;
- histórico de contato;
- supressões por budget/negative fit;
- follow-ups pós-PDF;
- tom Zipper: sofisticado, leve, sem hard sell.

**Fontes de verdade:**

- Zipper Supabase / `vendas_tango` para vendas reais;
- CRM/conversas/followups locais;
- PDFs comerciais validados;
- Brain Zipper;
- Gmail/WhatsApp quando autorizado.

**Ações autônomas permitidas:**

- registrar interesse por artista;
- atualizar CRM local;
- enviar follow-up pós-PDF em classes seguras já aprovadas;
- enviar acknowledgement seguro quando cliente diz que vai pensar/olhar com calma;
- agendar follow-up de 2 meses quando a conversa fica aberta sem objeção de preço/negociação;
- preparar proposta/draft para aprovação.

**Ações bloqueadas sem aprovação:**

- preço;
- disponibilidade específica;
- reserva;
- desconto;
- condição de pagamento;
- negociação;
- contato com artista/coletor fora de fluxo aprovado;
- campanha em lote;
- publicação/press/public communication.

### 6.3 Subagente SPITI

**Escopo:** SPITI Auction, leilões, lotes, lances, Spiti Hub, relatórios, divergências e comunicações operacionais.

**Memória própria:**

- regras de fonte de verdade;
- histórico de lotes/leilões;
- pendências de lances;
- divergências;
- relatórios;
- decisões operacionais.

**Fonte de verdade:**

- e-mail como fonte prioritária para lances;
- sistemas internos validados;
- site apenas como apoio quando confirmado;
- Brain SPITI.

**Princípio:**

> Silêncio é melhor que dado errado.

**Ações autônomas permitidas:**

- leitura/revisão quando fonte é acessível;
- apontar divergência;
- preparar relatório;
- preparar decisão para Lucas;
- registrar pendência.

**Ações bloqueadas sem aprovação:**

- afirmar lance atual sem fonte verificada;
- contatar bidder/cliente;
- alterar sistema/site;
- deploy;
- enviar relatório externo;
- mexer em banco/produção.

### 6.4 Subagente LK

**Escopo:** LK Sneakers, Shopify, Tiny, CRM, campanhas, estoque, recompra, SEO, analytics, influenciadores, performance e relatórios.

**Memória própria:**

- regras LK;
- fontes corretas;
- rotinas comerciais;
- campanhas;
- produtos/SKU;
- aprendizados de estoque;
- clientes e segmentos.

**Fontes de verdade:**

- Shopify para vendas/pedidos/clientes/catálogo;
- Tiny `LK | CONTROLE ESTOQUE` para estoque operacional;
- GA4/Meta/Google como sinais, não como receita final;
- Brain LK.

**Ações autônomas permitidas:**

- relatórios read-only;
- reconciliação local;
- análise de estoque e demanda;
- preparar campanhas/drafts;
- atualizar Brain/relatórios;
- apontar oportunidades.

**Ações bloqueadas sem aprovação:**

- WhatsApp/Klaviyo/e-mail externo;
- alterações Shopify/Tiny/Merchant;
- preço;
- estoque;
- campanhas pagas;
- orçamento;
- contato com cliente/fornecedor;
- compra/reposição.

### 6.5 Subagente Hermes/Infra

**Escopo:** Hermes Agent, cron, gateway, Telegram, Docker, VPS, Doppler, scripts, logs, skills, Brain health, automações.

**Memória própria:**

- arquitetura runtime;
- jobs ativos;
- falhas conhecidas;
- skills e correções;
- runbooks;
- integrações.

**Ações autônomas permitidas:**

- leitura de logs sanitizados;
- checagem de cron;
- inspeção read-only de sistema;
- correção local de scripts não sensíveis quando dentro de fluxo estabelecido;
- atualização de skill/documentação;
- self-healing de automações seguras já aprovadas.

**Ações bloqueadas sem aprovação:**

- restart de produção;
- alteração Docker/VPS/Traefik/volume/network;
- deploy;
- mudança de secrets;
- rotação de credenciais;
- banco de produção;
- qualquer ação destrutiva.

### 6.6 Subagente CRM/Relacionamentos

**Escopo:** visão global de relacionamentos de Lucas, sem misturar dados de empresas.

**Memória própria:**

- pessoas recorrentes;
- relação com Lucas;
- empresa/contexto;
- tom adequado;
- pendências abertas;
- histórico de follow-up;
- preferências de contato.

**Regra crítica:**

O CRM pode ter uma visão global para Lucas, mas os dados operacionais sensíveis devem ser salvos no domínio correto: Zipper, SPITI, LK, pessoal ou infra.

### 6.7 Subagente Governança/Qualidade

**Escopo:** auditar o sistema, como Bruno faz com agente de governança.

Responsabilidades:

- verificar se crons rodaram;
- detectar falhas silenciosas;
- verificar se skills estão atualizadas;
- detectar ruído enviado ao Lucas;
- auditar memória/Brain;
- sugerir skill quando tarefa se repete;
- checar se ações sensíveis foram bloqueadas corretamente.

## 7. Memória e Brain

### 7.1 Camadas de memória

O LC Mordomo OS usa múltiplas camadas:

1. **User Profile:** preferências permanentes de Lucas.
2. **Memory compacta:** regras globais e fatos duráveis.
3. **Session Search:** recuperação de contexto conversacional.
4. **Hermes Brain:** fonte durável para decisões, PRDs, rotinas, skills e conhecimento por área.
5. **CRM local/DB:** objetos estruturados de contatos, leads, follow-ups, propostas e histórico.
6. **Subagent memory:** memória operacional por domínio.

### 7.2 Regra de escrita

- Memória compacta só guarda fatos duráveis.
- Brain guarda decisões, processos, PRDs, rotinas e conhecimento operacional.
- CRM/DB guarda dados estruturados de relacionamento e follow-up.
- Skills guardam procedimentos repetíveis.
- Session search guarda histórico recuperável, não deve virar memória permanente automaticamente.

## 8. Skills

### 8.1 Regra de criação

Aplicar a regra do Bruno:

> Se repetiu 3 vezes, vira skill.

Adaptação para Lucas:

- 1 vez: executar normalmente.
- 2 vezes na mesma semana ou mesmo formato: documentar padrão.
- 3 vezes ou alto impacto: criar/atualizar skill.
- Se envolve ação externa: skill precisa ter aprovação, preview, guardrails, rollback e verificação.

### 8.2 Skills iniciais necessárias

- `lcmordomo-routing`
- `lcmordomo-decision-inbox`
- `lcmordomo-calendar-intake`
- `lcmordomo-whatsapp-intake`
- `lcmordomo-email-intake`
- `lcmordomo-followup-engine`
- `zipper-post-pdf-followup`
- `zipper-artist-interest-crm`
- `spiti-bid-verification`
- `lk-readonly-commerce-brief`
- `hermes-cron-governance`
- `lcmordomo-memory-hygiene`

## 9. Inboxes operacionais

### 9.1 Global Intake Inbox

Recebe sinais de:

- Telegram;
- WhatsApp;
- e-mail;
- calendário;
- Brain;
- crons;
- scripts;
- CRM;
- integrações.

### 9.2 Decision Inbox

Só sobe para Lucas quando há:

- decisão real;
- risco;
- aprovação necessária;
- cliente aguardando;
- falha de automação;
- exceção operacional;
- ambiguidade material;
- bloqueio que Lucas precisa resolver.

Formato obrigatório:

```text
Urgência:
Contexto:
O que aconteceu:
Por que importa:
Recomendação:
Ação sugerida:
Aprovação necessária:
Bloqueador:
```

### 9.3 Follow-up Inbox

Gerencia pendências por classe:

- follow-up seguro automático;
- follow-up que exige leitura recente;
- follow-up que exige draft;
- follow-up que exige Lucas;
- follow-up bloqueado.

### 9.4 Incident Inbox

Falhas de cron, script, integração, API ou runtime.

Regra: alertar Lucas só quando a falha exige decisão, impacta operação ou não pode ser autocorrigida com segurança.

## 10. Autonomia e aprovação

### A0 — Silencioso/read-only

Permitido sem aprovação:

- ler arquivos locais;
- consultar Brain;
- gerar relatório local;
- classificar mensagens;
- atualizar estado local não sensível;
- verificar cron/log sanitizado;
- criar draft local.

### A1 — Local/reversível

Permitido sem aprovação:

- escrever relatório;
- atualizar PRD/Brain local;
- criar skill local;
- corrigir parser local de automação segura;
- registrar CRM/follow-up local.

### A2 — Automação segura pré-aprovada

Permitido sem nova aprovação somente quando a classe está explicitamente autorizada e os guardrails passam.

Exemplos atuais:

- Zipper pós-PDF safe acknowledgement/follow-up;
- confirmação logística simples já classificada como segura;
- calendário claro com data/hora/contexto.

### A3 — Preview obrigatório

Preparar, mas não executar sem aprovação:

- resposta a cliente fora de classe segura;
- e-mail/WhatsApp externo;
- campanha;
- proposta;
- preço/disponibilidade;
- alterações comerciais;
- relatórios sensíveis.

### A4 — Aprovação explícita + plano/rollback

Bloqueado sem aprovação atual:

- dinheiro;
- fornecedor;
- campanha paga;
- deploy;
- banco de produção;
- infra/VPS/Docker;
- secrets;
- ação destrutiva;
- contato sensível;
- negociação.

## 11. Crons e rotinas

Crons são o heartbeat explícito do LC Mordomo OS.

Cada cron precisa ter:

- nome legível;
- dono/subagente;
- horário;
- fonte consultada;
- skill/script chamado;
- output esperado;
- política de silêncio;
- quando alertar Lucas;
- verificação;
- fallback.

### Rotinas iniciais recomendadas

1. **Decision Inbox diário/contínuo**
   - Só envia decisões acionáveis.

2. **Follow-up watchdog**
   - Executa classes seguras.
   - Escala classes bloqueadas.

3. **Calendar intake watchdog**
   - Detecta compromissos claros.

4. **Zipper CRM/follow-up watchdog**
   - Pós-PDF, artista, interesse, supressões.

5. **SPITI verification watchdog**
   - Divergência de lances/fontes, sem afirmar dado não verificado.

6. **LK read-only intelligence**
   - Relatórios comerciais/estoque, sem writes.

7. **Hermes governance watchdog**
   - Crons, skills, logs, falhas, ruído.

## 12. Mission Control / superfície visual

O LC Mordomo OS deve ter uma superfície de controle para Lucas, mas não deve depender dela para operar.

Módulos desejados:

- Decision Inbox;
- Follow-ups;
- CRM global roteado;
- subagentes;
- crons;
- falhas/incidentes;
- approvals;
- agenda;
- Mission Queue;
- learning loop;
- status por empresa;
- guardrails visíveis.

Regra: a interface deve mostrar **ação**, não log.

## 13. Dados e isolamento

### 13.1 Separação por domínio

- Zipper não mistura com SPITI.
- LK não mistura com Zipper.
- Pessoal não mistura com empresa, salvo quando Lucas explicitamente cruza contexto.
- Hermes/infra não assume ação comercial.

### 13.2 Fontes de verdade

Cada subagente precisa declarar:

- fonte primária;
- fonte secundária;
- fonte proibida para afirmação final;
- quando escalar.

## 14. Learning loop

O sistema deve aprender a partir de:

- aprovações de Lucas;
- correções de Lucas;
- rejeições;
- drafts editados;
- respostas reais enviadas por Lucas;
- falhas de automação;
- decisões comerciais;
- feedback de qualidade.

Destino do aprendizado:

- preferência durável → memory/user profile;
- regra operacional → Brain;
- processo repetível → skill;
- decisão de empresa → área da empresa no Brain;
- falha recorrente → runbook/skill/cron fix;
- contato específico → CRM/contact profile.

## 15. Requisitos funcionais

### RF1 — Interface única

Lucas deve poder mandar qualquer pedido para o LC Mordomo Central sem escolher subagente.

### RF2 — Roteamento automático

O sistema deve classificar cada entrada como pessoal, LK, Zipper, SPITI, Hermes/infra, CRM global ou desconhecido.

### RF3 — Subagentes especializados

Cada domínio deve ter subagente com memória, skills, rotinas, fontes e limites próprios.

### RF4 — Decision Inbox

O sistema deve transformar ruído em pacotes de decisão claros.

### RF5 — Follow-up engine

O sistema deve registrar, deduplicar, executar ou escalar follow-ups conforme classe de risco.

### RF6 — CRM global roteado

O sistema deve manter visão global de relacionamentos sem misturar dados operacionais entre empresas.

### RF7 — Calendar intake

Compromissos claros devem virar evento/reminder automaticamente quando dentro das regras.

### RF8 — Skill learning

Processos repetidos devem virar skills ou rotinas documentadas.

### RF9 — Cron governance

Falhas de cron devem ser autocorrigidas quando seguras ou escaladas quando sensíveis.

### RF10 — Approval gates

Ações externas/sensíveis devem respeitar A0–A4.

## 16. Requisitos não funcionais

- Segurança por padrão.
- Não expor secrets.
- Menos Telegram, mais ação.
- Logs técnicos fora do canal Lucas.
- Verificabilidade antes de conclusão.
- Idempotência em sends/follow-ups.
- Separação multiempresa.
- Operação silenciosa quando não há decisão.
- Escalabilidade por subagente, não por caos de bots.

## 17. MVP

### MVP 1 — Núcleo do LC Mordomo Central

Entregas:

- SOUL/contrato do agente principal;
- mapa de subagentes;
- matriz A0–A4;
- Decision Inbox format;
- routing rules;
- arquivo Brain do PRD;
- learning loop inicial.

Critério de pronto:

- qualquer entrada de Lucas pode ser classificada e respondida com domínio, risco e próxima ação.

### MVP 2 — Zipper primeiro

Entregas:

- Zipper subagent spec;
- CRM de interesse por artista;
- pós-PDF follow-up seguro;
- supressão budget_decline;
- Decision Packets para preço/disponibilidade/negociação;
- Zipper follow-up watchdog.

Critério de pronto:

- leads/PDFs/follow-ups Zipper deixam de depender de memória de chat e entram em fluxo estruturado.

### MVP 3 — SPITI

Entregas:

- SPITI subagent spec;
- fonte de verdade de lances;
- rotina de divergência;
- relatório seguro;
- escalation policy.

Critério de pronto:

- nenhum dado de lance é afirmado sem fonte correta; divergências viram pacote de decisão.

### MVP 4 — Pessoal + calendário

Entregas:

- calendar intake;
- reminders;
- contact profiles;
- tom por pessoa;
- follow-ups logísticos simples.

Critério de pronto:

- compromissos claros são capturados e Lucas recebe confirmação, não pergunta se alguém viu.

### MVP 5 — LK

Entregas:

- LK subagent spec;
- relatórios read-only;
- CRM/rebuy intelligence;
- stock intelligence;
- preview-only campaigns.

Critério de pronto:

- LK entra no mesmo modelo global, mas com fontes e guardrails próprios.

### MVP 6 — Governança

Entregas:

- subagente de governança;
- cron health;
- skill health;
- noise audit;
- incident inbox.

Critério de pronto:

- falhas de automação seguras são corrigidas antes de virarem ruído para Lucas.

## 18. Fora de escopo inicial

- Envio externo amplo sem aprovação.
- Campanhas automáticas.
- Negociação automática.
- Deploy/infra automático.
- Alteração de preço/estoque/lance.
- Agentes autônomos sem supervisão.
- UI completa antes do fluxo operacional funcionar.
- Criar muitos subagentes especialistas sem demanda comprovada.

## 19. Riscos

### R1 — Sprawl de agentes

Mitigação: começar com um agente central forte e poucos subagentes por domínio.

### R2 — Sprawl de skills

Mitigação: curadoria; skill só quando repetição real ou alto impacto.

### R3 — Telegram virar lixo

Mitigação: delivery taxonomy: silencioso, recibo, digest, urgente, aprovação, erro.

### R4 — Mistura multiempresa

Mitigação: roteamento obrigatório e fontes separadas.

### R5 — Ação externa indevida

Mitigação: A0–A4, preview obrigatório e current-turn approval.

### R6 — Memória inflada

Mitigação: memory compacta, Brain durável, CRM estruturado e hygiene routine.

## 20. Métricas de sucesso

- Menos interrupções inúteis no Telegram.
- Mais follow-ups executados no prazo.
- Menos leads perdidos.
- Mais decisões chegam prontas.
- Menos falhas de cron sem diagnóstico.
- Menos contexto repetido por Lucas.
- Mais processos viram skills reutilizáveis.
- Cada negócio tem memória/CRM/rotinas separados.
- Lucas sente que fala com uma secretária única, não com várias ferramentas.

## 21. Próximos passos

1. Validar com Lucas a tese: **um agente principal + subagentes com memória própria**.
2. Escrever o SOUL do LC Mordomo Central.
3. Criar o mapa inicial de subagentes e permissões.
4. Formalizar a matriz A0–A4 em Brain/skill.
5. Começar MVP 2 por Zipper, porque já há fluxo real de PDFs/follow-ups/CRM.
6. Depois SPITI.
7. Depois Pessoal/calendário.
8. Depois LK.
9. Criar Governança/Quality watchdog transversal.

## 22. Decisão de produto recomendada

A arquitetura correta é:

> **LC Mordomo Central como agente principal e subagentes especializados por domínio, cada um com memória, Brain, skills, rotinas, ferramentas e permissões próprias. Lucas vê uma única interface; o sistema decide internamente quem trabalha.**

Essa é a versão Hermes-native do padrão Bruno/OpenClaw: agente como operador, Brain como contexto, skills como processo, crons como rotina e governança como proteção.
