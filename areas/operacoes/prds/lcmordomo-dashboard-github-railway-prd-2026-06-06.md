# PRD — LC Mordomo Dashboard sobre projeto GitHub + Railway

Data: 2026-06-06
Status: Draft v0.1 — pronto para virar plano técnico/issue backlog
Owner: Lucas Cimino / LC Mordomo OS
Produto alvo: Dashboard LC WhatsApp existente
URL produção analisada: `https://lc-whatsapp-prd.up.railway.app/dashboard`
Ambiente alvo: GitHub + Railway

## 1. Decisão principal

O dashboard **não deve ser reconstruído do zero**.

O caminho correto é adaptar o projeto existente no GitHub, hoje publicado na Railway, para virar o cockpit oficial do **LC Mordomo OS**.

A arquitetura correta é:

- **GitHub:** fonte do código, PRs, histórico e revisão.
- **Railway:** runtime/API do dashboard existente.
- **Dashboard:** interface operacional/cockpit.
- **LC Mordomo database:** fonte de verdade para contatos, artistas, interesses, follow-ups, decision packets e ações enviadas.
- **Policy engine do Mordomo:** camada obrigatória antes de qualquer envio externo.
- **WhatsApp/e-mail:** canais de execução, nunca fonte canônica.

## 2. Contexto verificado

### 2.1 Dashboard Railway

A URL de produção respondeu:

- `/health`: conectado, versão `2.0.0`.
- `/api/version`: versão `2.0.0`.
- `/api/stats`: `totalContacts: 389`, `totalMessages: 1`, `dbEnabled: true`.
- `/api/db/test`: conexão DB OK, latência observada `592ms`.

Isso confirma que o app está vivo, com API e banco configurado no ambiente Railway.

### 2.2 Módulos já existentes no dashboard

A interface atual já tem os módulos necessários para acelerar o LC Mordomo:

- Métricas
- Contatos
- Conversas
- Busca por PDF/documento
- Histórico
- Enviar / Quick Send
- Campanha
- Agendamento
- Templates
- Artistas
- Automações
- Agentes IA

### 2.3 Infra interna conhecida

Brain registra Railway como ativo para:

- `lc-whatsapp`
- `zpr-cockpit`
- `lk-cockpit`
- `zpr-auto-like`

Secret ref interno: `RAILWAY_TOKEN`, via Doppler.

Regra de segurança: qualquer deploy, alteração Railway, variável de produção, migration ou write produtivo exige aprovação explícita do Lucas.

## 3. Problema

O dashboard atual funciona como um painel WhatsApp/LK/Supabase, mas o **LC Mordomo OS** precisa de uma fonte de verdade própria e governada.

Problemas a resolver:

1. O dashboard atual fala em Supabase/WhatsApp Agent e pode estar modelado para LK ou um CRM genérico.
2. O Mordomo já tem lógica própria de follow-up, policy, idempotência e decision packets.
3. O dashboard tem botões de envio/campanha que, se mantidos sem policy, podem violar guardrails.
4. O app está em produção na Railway; adaptações precisam ser feitas por PR/branch e deploy controlado.
5. O projeto está no GitHub, então o PRD precisa orientar implementação como alteração incremental no repo existente.

## 4. Objetivo

Transformar o projeto GitHub/Railway existente em uma interface oficial do **LC Mordomo OS**, usando a lógica visual atual do dashboard, mas apontando a camada de dados/decisão para o database canônico do Mordomo.

O dashboard deve permitir que Lucas veja, em menos de 30 segundos:

- quem precisa de follow-up hoje;
- quais follow-ups são seguros para auto-send A1;
- quais estão bloqueados por tema material;
- quais clientes têm interesse por quais artistas;
- quais PDFs/catálogos foram enviados;
- quais decision packets exigem decisão humana;
- se cron/runner/API estão saudáveis.

## 5. Não-objetivos

Nesta fase não vamos:

- substituir o projeto GitHub por outro app;
- fazer deploy direto sem PR/aprovação;
- alterar variáveis Railway de produção sem aprovação;
- ativar campanhas em massa;
- liberar envio externo direto pelo botão “Enviar” sem policy;
- usar WhatsApp ou Supabase legado como fonte final de verdade;
- expor tokens, connection strings, JIDs ou telefones brutos em logs/documentos.

## 6. Fonte de verdade LC Mordomo

Database canônico atual:

- SQLite local: `/opt/data/profiles/mordomo/state/zipper_canonical.sqlite`
- Summary: `/opt/data/profiles/mordomo/state/zipper_canonical_summary.json`

Contagens verificadas:

- Contatos: 123
- Interesses por artista: 36
- Lead enquiries: 126
- Follow-ups: 126
- Sent actions: 150
- Decision packets: 18
- Suppressions: 10

Tabelas canônicas atuais:

- `contact`
- `lead_enquiry`
- `artist_interest`
- `followup`
- `sent_action`
- `suppression`
- `decision_packet`

Decisão: o dashboard Railway deve consumir uma API Mordomo que lê/escreve nesses objetos, ou numa réplica futura equivalente, mas sempre preservando o contrato canônico.

## 7. Arquitetura alvo

```text
GitHub repo existente
  -> branch/PR de adaptação LC Mordomo
  -> CI/test/build
  -> Railway deploy controlado

Dashboard Railway
  -> API adapter /api/mordomo/*
  -> Mordomo DB/API
  -> Policy Engine
  -> Runner/cron
  -> WhatsApp/e-mail somente quando permitido
```

## 8. Componentes

### 8.1 Frontend dashboard

Reaproveitar UI atual, mas reorganizar prioridade:

P0 na home:

- Follow-ups hoje
- Bloqueados/material
- Decision packets
- Artistas mais ativos
- Leads recentes
- Saúde do Mordomo

Reduzir destaque inicial de:

- Campanha em massa
- Envio rápido direto

Esses módulos podem existir, mas como recursos controlados por policy/aprovação.

### 8.2 Backend/API Railway

Manter endpoints existentes quando possível, mas adicionar namespace explícito:

- `GET /api/mordomo/stats`
- `GET /api/mordomo/contacts`
- `GET /api/mordomo/artists`
- `GET /api/mordomo/followups`
- `GET /api/mordomo/decision-packets`
- `GET /api/mordomo/actions`
- `GET /api/mordomo/automation/status`
- `POST /api/mordomo/followups/{id}/preview`
- `POST /api/mordomo/followups/{id}/approve-send`
- `POST /api/mordomo/followups/{id}/auto-send-if-safe`

### 8.3 Compatibility layer

Para acelerar sem reescrever tudo:

- `/api/stats` pode agregar `/api/mordomo/stats`.
- `/api/contacts` pode mapear para contatos Mordomo.
- `/api/artists` pode mapear para `artist_interest` agregado.
- `/api/messages` pode mapar `sent_action` + conversas.
- `/api/agents/followup` deve virar preview, não envio.
- `/api/campaign/*` deve ficar protegido/desabilitado para LC Mordomo até aprovação explícita.

### 8.4 Policy Engine

Nenhuma rota de envio pode bypassar policy.

Saídas obrigatórias:

- `ALLOW_AUTO_SEND`
- `BLOCK_MATERIAL`
- `NEEDS_LUCAS_DECISION`
- `NOOP_ALREADY_SENT`
- `NOOP_NOT_DUE`
- `SNOOZE`
- `ERROR_REQUIRES_REVIEW`

## 9. Regras de auto-follow-up A1

Auto-send só pode ocorrer quando todos os critérios passarem:

- contexto: LC/Zipper;
- canal: WhatsApp individual;
- tipo: pós-PDF leve;
- risk class: A1;
- `due_at` vencido;
- histórico relido antes do envio;
- nenhuma resposta posterior do cliente;
- sem tema material;
- contato não suprimido;
- idempotency key inédita;
- registro em `sent_action` obrigatório;
- falha vira decision packet ou erro, não retry cego.

Bloqueios materiais:

- preço;
- disponibilidade;
- reserva;
- pagamento;
- desconto/negociação;
- frete/logística;
- dimensão/medida/tamanho;
- reclamação;
- ambiguidade comercial.

## 10. Requisitos funcionais

### P0 — Discovery e congelamento seguro

1. Identificar repo GitHub correto.
2. Identificar Railway project/service/environment corretos.
3. Clonar/abrir repo em branch local.
4. Rodar app/test/build localmente, se possível.
5. Mapear stack, endpoints, schema e variáveis necessárias sem expor secrets.
6. Confirmar que nenhuma rota crítica envia mensagens sem policy.

Critério de aceite:

- documento técnico `implementation-inventory.md` com repo, stack, endpoints, env names mascarados, scripts e risco.

### P1 — API read-only Mordomo

Adicionar/adaptar endpoints read-only:

- stats;
- contatos;
- artistas/interesses;
- follow-ups;
- decision packets;
- sent actions;
- automation status.

Critério de aceite:

- dashboard carrega dados Mordomo em modo read-only;
- nenhum envio externo possível;
- testes de API passam.

### P2 — UI LC Mordomo

Adaptar telas existentes:

- Métricas viram visão LC Mordomo.
- Contatos mostram interesse por artista e próximo follow-up.
- Artistas mostram interessados e pendências.
- Histórico mostra sent actions/blocked actions.
- Automações mostra cron/runner status.
- Agentes IA geram preview/classificação, não envio livre.

Critério de aceite:

- Lucas consegue ver follow-ups, bloqueados e interesses sem entrar em arquivos internos.

### P3 — Preview/approval individual

Permitir:

- gerar preview de follow-up;
- aprovar envio individual explicitamente;
- registrar `sent_action`;
- impedir duplicidade;
- criar decision packet quando inseguro.

Critério de aceite:

- teste confirma que aprovação individual envia só uma vez e registra idempotência.

### P4 — Auto-follow-up A1

Habilitar apenas depois de P0-P3:

- rota `auto-send-if-safe`;
- policy completa;
- releitura de histórico;
- dedupe;
- registro;
- dashboard com liga/desliga e auditoria.

Critério de aceite:

- casos A1 safe enviam automaticamente;
- casos materiais bloqueiam;
- duplicidade não acontece;
- erros aparecem como decisão/erro limpo.

## 11. Requisitos de GitHub

### 11.1 Fluxo de trabalho

- Trabalhar em branch: `feature/lcmordomo-dashboard-adapter`.
- Não commitar secrets, `.env`, dumps ou PII.
- Criar PR com:
  - resumo do que muda;
  - screenshots ou vídeo curto da UI;
  - checklist de guardrails;
  - testes executados;
  - rollback Railway.

### 11.2 Estrutura esperada no PR

Arquivos esperados, a depender da stack real:

- API adapter Mordomo.
- Policy gate para rotas de envio.
- UI copy/labels LC Mordomo.
- Tests de endpoints e policy.
- Documentação `docs/lcmordomo-dashboard.md`.
- `.env.example` atualizado sem valores reais.

### 11.3 Proteções

O PR não pode:

- alterar Railway production diretamente;
- incluir token Railway/GitHub/Doppler/Supabase;
- ativar campanha/envio por default;
- remover guardrails existentes;
- migrar schema produtivo sem plano e aprovação.

## 12. Requisitos Railway

### 12.1 Ambientes

Usar ambientes separados se disponíveis:

- `production`: atual `lc-whatsapp-prd`.
- `staging` ou preview environment: validação do PR.

Se não existir staging, criar somente após aprovação Lucas.

### 12.2 Variáveis

Variáveis devem ser referenciadas por nome, não valor.

Categorias esperadas:

- Railway runtime/app.
- DB legado atual do dashboard.
- Mordomo API/DB connector.
- WhatsApp/Evolution/wacli connector.
- LLM provider, se usado por agentes.
- Auth/session.

Nenhum secret deve ser exibido no PRD, PR ou logs.

### 12.3 Deploy

Deploy production exige aprovação explícita.

Antes de deploy:

- build passa;
- testes passam;
- secret scan limpo;
- preview/staging validado;
- rollback documentado;
- rotas de envio externas desabilitadas ou policy-gated.

## 13. API atual observada e adaptação

Endpoints atuais encontrados no app:

- `/health`
- `/api/version`
- `/api/stats`
- `/api/db/test`
- `/api/metrics?days=`
- `/api/funnel`
- `/api/insights`
- `/api/contacts?`
- `/api/contacts/by-artist?artist=`
- `/api/contacts/by-tag?tag=`
- `/api/messages?`
- `/api/conversations?`
- `/api/scan`
- `/api/scan/full`
- `/api/scan/status`
- `/api/templates`
- `/api/campaign/*`
- `/api/scheduled`
- `/api/quicksend/*`
- `/api/automations/*`
- `/api/agents/*`

Adaptação recomendada:

- manter endpoints de leitura compatíveis;
- trocar backend de dados para Mordomo adapter;
- travar endpoints de envio com policy;
- transformar agentes de “executor” em “preview/classifier”.

## 14. UX alvo por tela

### Home / Métricas

Mostrar:

- follow-ups vencidos;
- seguros A1;
- bloqueados;
- decision packets abertos;
- artistas mais requisitados;
- leads recentes;
- status Railway/API;
- status cron Mordomo.

### Contatos

Mostrar:

- nome;
- telefone mascarado;
- artista(s) de interesse;
- PDFs enviados;
- último contato;
- próximo follow-up;
- tags/notas;
- status de risco.

### Artistas

Mostrar:

- artista;
- número de interessados;
- follow-ups pendentes;
- PDFs/catálogos associados;
- clientes bloqueados/decision packets.

### Follow-ups

Criar ou priorizar tela dedicada, mesmo que reaproveite Agentes IA/Histórico:

- vencidos hoje;
- futuros;
- safe auto-send;
- bloqueados;
- enviados;
- cancelados/snoozed.

### Automações

Mostrar:

- health Railway;
- versão app;
- DB status;
- cron Mordomo status;
- última execução;
- política ativa;
- auto-send on/off.

## 15. Segurança

### 15.1 Botões perigosos

Botões existentes que devem ser bloqueados ou policy-gated no LC Mordomo:

- Enviar WhatsApp + Email.
- Enviar teste.
- Iniciar Campanha.
- Agendar envio em massa.
- Agent followup send.

### 15.2 Exibição de PII

- Relatórios/documentos: telefone mascarado.
- UI operacional: telefone pode aparecer se Lucas estiver logado e for necessário, mas logs devem mascarar.
- Nunca exibir JID bruto em logs genéricos.

### 15.3 Auditoria

Toda tentativa de envio precisa registrar:

- quem/qual processo solicitou;
- policy result;
- idempotency key;
- mensagem hash/preview;
- status;
- timestamp.

## 16. Testes obrigatórios

### Unit tests

- material question bloqueia;
- `?` sem termo material não bloqueia reenvio de PDF seguro;
- due_at futuro não envia;
- already sent não envia;
- contato suprimido não envia;
- thread com resposta posterior não envia;
- A1 pós-PDF safe libera.

### API tests

- `/api/mordomo/stats` responde;
- `/api/mordomo/contacts` pagina;
- `/api/mordomo/artists` agrega interesses;
- `/api/mordomo/followups` filtra status;
- `/api/mordomo/followups/{id}/preview` não envia;
- endpoints antigos compatíveis não quebram UI.

### E2E/smoke

- dashboard abre;
- métricas carregam;
- contatos carregam;
- artista abre lista de interessados;
- follow-up preview aparece;
- botão de envio sem aprovação é bloqueado.

## 17. Rollback

Rollback técnico:

- manter branch main atual intacta;
- deploy via Railway deve ter rollback para deployment anterior;
- migrations produtivas proibidas na fase P0-P2;
- feature flag para `LC_MORDOMO_MODE` e `AUTO_SEND_A1_ENABLED`.

Flags recomendadas:

- `LC_MORDOMO_MODE=readonly|approval|auto_a1`
- `AUTO_SEND_A1_ENABLED=false` por padrão
- `CAMPAIGN_SEND_ENABLED=false` por padrão
- `QUICKSEND_EXTERNAL_ENABLED=false` por padrão

## 18. Plano de execução recomendado

### Passo 1 — Discovery GitHub/Railway

Ação:

- identificar repo exato e serviço Railway;
- clonar repo;
- mapear stack e scripts;
- rodar build/test local.

Critério de pronto:

- inventory salvo com repo, branch, stack, endpoints, Railway service e riscos.

### Passo 2 — PR técnico read-only

Ação:

- adicionar adapter read-only `/api/mordomo/*`;
- conectar summary/SQLite ou API Mordomo;
- UI exibe dados canônicos.

Critério de pronto:

- PR aberto com testes passando e sem envio externo.

### Passo 3 — UI de follow-up/decision packets

Ação:

- criar/ajustar telas para follow-ups, bloqueios e decisões.

Critério de pronto:

- Lucas consegue operar a fila sem abrir JSON/SQLite.

### Passo 4 — Approval flow

Ação:

- preview + aprovação individual;
- registro em sent_action;
- dedupe.

Critério de pronto:

- envio individual aprovado funciona em teste/staging e não duplica.

### Passo 5 — Auto A1

Ação:

- ligar auto-follow-up A1 com flag e policy.

Critério de pronto:

- safe A1 envia; material bloqueia; erro alerta limpo.

## 19. Perguntas abertas para execução

Antes de mexer no GitHub/Railway, preencher:

1. Qual é o repo GitHub exato?
2. Qual é o Railway project/service/environment exato?
3. O app atual usa Supabase, Postgres Railway ou outro DB?
4. Existe staging/preview environment?
5. Qual auth protege `/dashboard` em produção?
6. O dashboard deve continuar com branding LK SNKRS ou mudar para LC Mordomo/Zipper?
7. O SQLite local do Mordomo será lido diretamente, replicado para Supabase/Postgres, ou exposto por API interna?

Recomendação: para começar rápido, usar API adapter read-only, não migração de banco.

## 20. Critérios de aceite do MVP

MVP aceito quando:

- projeto GitHub existente foi identificado e documentado;
- app Railway continua saudável;
- dashboard mostra dados do LC Mordomo database;
- follow-ups aparecem com due/status/risk;
- artistas mostram clientes interessados;
- decision packets aparecem separados;
- rotas de envio estão bloqueadas ou policy-gated;
- nenhum deploy production foi feito sem aprovação;
- PR tem testes e rollback;
- Lucas consegue ver “quem precisa de follow-up hoje” pelo dashboard.

## 21. Conclusão

Sim: o projeto estando no GitHub e na API Railway muda o PRD.

Não é “criar um dashboard”. É **adaptar o dashboard vivo** para virar o cockpit do LC Mordomo OS, com PR controlado no GitHub e deploy seguro na Railway.

A regra central permanece:

- Railway roda o dashboard.
- GitHub governa mudança.
- LC Mordomo database governa verdade.
- Policy engine governa envio.
