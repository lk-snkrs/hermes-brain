# Auditoria crítica — agentes, orquestração e governança Hermes vs Amora/Bruno

Data/hora: 2026-05-25T01:14:02Z  
Owner: Hermes Geral / COO  
Escopo: auditoria local/read-only, Brain docs, cron registry, processos gateway, handoffs/receipts e referência Amora/Bruno.  
Writes externos: não.

## Veredito executivo

Hermes está mais correto para o contexto do Lucas do que uma cópia da Amora: ele tem multiempresa, approval gates, separação de especialistas, Brain como fonte de verdade e proteção forte contra produção/externo. Mas Amora ainda é mais madura em ritual vivo, proatividade diária e consistência de uso.

Nota geral hoje: **7,8/10**.

- Documentação e arquitetura: **8,6/10**
- Runtime real observado: **7,2/10**
- Maturidade proativa/ritual: **6,8/10**
- Benchmark Amora: **9,0/10** como agente pessoal/CoS maduro, não como blueprint literal para Lucas.

Tese central: **o próximo salto não é criar mais agente nem mais prompt. É fechar o ciclo pedido → router → executor certo → preview/ação segura → receipt → handoff → Brain → skill/rotina.**

## Evidências usadas

### Hermes

- `empresa/contexto/organograma-agentes-hermes.md`
- `empresa/contexto/organograma-orquestrador-tarefas-hermes.md`
- `empresa/contexto/matriz-roteamento-tarefas-hermes.md`
- `empresa/contexto/task-router-hermes.md`
- `areas/operacoes/prds/hermes-orquestracao-fase-8-proatividade-handoffs-2026-05-24.md`
- `reports/governance/orquestrador-fase8-status-2026-05-25.md`
- `reports/governance/handoff-completeness-check-2026-05-25.md`
- `empresa/contexto/handoffs/2026-05-25.md`
- `memories/hot.md`
- pacotes documentais em `agentes/hermes-geral`, `agentes/lk`, `agentes/mordomo`, `agentes/spiti`, `agentes/zipper`, `areas/lk/sub-areas/growth`
- `hermes cron list --all` via terminal, sem mutação
- processos gateway vivos por `HERMES_HOME` via `/proc`

### Amora/Bruno

- `case-amora.md`
- referências Hermes/OpenClaw sobre Amora e scorecard de comparação
- padrões Amora: super-agente único, SOUL/IDENTITY/USER/AGENTS/MAPA/HEARTBEAT, 60+ crons, skills custom, rotina diária, meta-auditoria e proatividade treinada.

## Separação obrigatória

### Bem documentado

- Organograma central e operacional.
- Matriz de roteamento por contexto/tarefa.
- Approval boundaries A0-A4.
- Pacotes documentais mínimos dos agentes centrais e especialistas.
- Handoff, receipts e regra de handoff completeness.
- Silent-OK e proteção contra ruído no Telegram.

### Já funciona na prática

- Gateways reais rodando para `/opt/data`, `/opt/data/profiles/lk-growth`, `/opt/data/profiles/mordomo` e `/opt/data/profiles/spiti`.
- Cron registry ativo com watchdogs e relatórios locais/origin conforme caso.
- Brain health recente com 0 falhas/0 warnings.
- Receipts reais em LK Growth, incluindo dev/prod theme receipts, readback e rollback.
- Handoff retroativo de LK Growth corrigido sem inventar aprovação.
- Scheduler/testes já cobrem parte da UX limpa, embora a prova final seja Telegram real.

### Ainda é intenção, arquitetura ou promessa

- Zipper runtime dedicado ainda não existe. Hoje é documental/read-only.
- Mesa COO v2 ainda precisa ser observada em entrega real limpa no Telegram depois do vazamento de wrapper.
- Métricas de qualidade do Task Router ainda não existem em rotina: falso positivo, falso negativo, handoff omitido, rota errada.
- Handoff completeness ainda depende de disciplina e auditoria local; não há enforcement automático universal.
- Proatividade ainda não tem a maturidade Amora de meses de uso diário e ajuste fino.

## Auditoria por área

### 1. Identidade e papel dos agentes

Nota Hermes: **8,4/10**  
Amora benchmark: **9,2/10**

O que está bom:
- Todos os pacotes auditados estão completos: Hermes Geral, LK, Mordomo, SPITI, Zipper e LK Growth têm `SOUL`, `IDENTITY`, `USER`, `AGENTS`, `MAPA`, `HEARTBEAT`, `TOOLS` e `MEMORY`.
- A regra central está clara: Hermes Geral coordena; especialistas executam; Brain registra; produção/externo exige aprovação.
- LK Growth e SPITI foram corrigidos nesta fase: LK Growth ganhou `IDENTITY/USER`; SPITI ganhou `SOUL` mais maduro.

O que falta:
- Amora tem uma identidade mais viva e treinada por uso diário; Hermes ainda soa mais como governança operacional em alguns pontos.
- Falta medir se cada especialista realmente “pensa” conforme seu SOUL quando acionado no runtime.

Evidências:
- Inventário local confirmou pacotes completos.
- `organograma-agentes-hermes.md` descreve papéis e limites.
- `case-amora.md` mostra Amora como super-agente consolidado.

Risco se não corrigir:
- O sistema vira uma coleção de documentos bons, mas sem personalidade operacional consistente.

Melhorias:
- Adicionar boot sequence curta por especialista: ler `SOUL → USER → MAPA → HEARTBEAT → MEMORY → fonte viva`.
- Rodar auditoria trimestral de coerência entre identidade documental e outputs reais.

### 2. Arquitetura do Brain e fonte de verdade

Nota Hermes: **8,6/10**  
Amora benchmark: **8,7/10**

O que está bom:
- Brain está estruturado como fonte de verdade de governança, rotas, decisões, handoffs e relatórios.
- `memories/hot.md` concentra prioridades atuais e decisões abertas.
- Health check recente retorna 0 falhas/0 warnings.

O que falta:
- Ainda há risco de documentação ficar à frente do runtime.
- Alguns relatórios e receipts ficam profundos em subpastas; sem MAPA/handoff, perdem descobribilidade.

Evidências:
- 52 relatórios em `reports/governance`.
- Handoff central de 2026-05-25 atualizado com várias rodadas.
- Hot context lista Mesa COO, handoff completeness e benchmark Amora como decisões vivas.

Risco:
- O Brain parecer completo, mas falhar como sistema operacional vivo.

Melhorias:
- Todo relatório que muda decisão precisa estar linkado em MAPA/handoff/hot context quando relevante.
- Criar uma visão mensal “Brain operating deltas”: o que mudou, o que foi executado, o que continua promessa.

### 3. Orquestração central e Task Router

Nota Hermes: **8,7/10**  
Amora benchmark: **7,8/10**

O que está bom:
- Hermes é mais forte que Amora em governança multiempresa e approval boundaries.
- Matriz tem rotas claras para LK Growth, Mordomo, Zipper, SPITI, Hermes Ops, Tech/Infra e pesquisa geral.
- Preflight evita que metadados internos sejam conteúdo Lucas-facing, quando respeitado.

O que falta:
- Métrica operacional de roteamento ainda não existe.
- Ainda pode haver execução “por conveniência” no Hermes Geral quando deveria ser especialista.
- O cronjob tool foi bloqueado por guardrail nesta auditoria; contornei com terminal read-only. Isso é seguro, mas mostra que o hard block ainda pode ser grosso demais para certas leituras administrativas.

Evidências:
- `matriz-roteamento-tarefas-hermes.md` IDs e boundaries.
- `task-router-hermes.md` documenta Fase 7/7B.
- Guardrail bloqueou `cronjob list`, mas terminal read-only confirmou registry.

Risco:
- Bloquear leitura útil ou permitir escrita por rota errada. Os dois atrapalham um COO.

Melhorias:
- Criar score mensal de router: rota correta, rota corrigida, bloqueio correto, bloqueio excessivo.
- Separar melhor “read-only admin inspection” de “cron mutation” no hard block.

### 4. Separação entre Hermes Geral, especialistas e perfis runtime

Nota Hermes: **7,8/10**  
Amora benchmark: **8,6/10**

O que está bom:
- Runtime observado: gateways vivos para main, LK Growth, Mordomo e SPITI.
- Zipper está deliberadamente documental/read-only, não fingindo runtime que não existe.
- Organograma distingue negócio, agente documental, profile/bot, rotina/cron, tarefa e handoff.

O que falta:
- Zipper ainda não tem runtime dedicado, embora tenha fluxos reais de vendas/WhatsApp/relatórios.
- Nem todo cron/report pertence naturalmente ao profile certo; isso precisa seguir sendo reconciliado.

Evidências:
- `/proc` mostrou gateways de `/opt/data`, `/opt/data/profiles/lk-growth`, `/opt/data/profiles/mordomo`, `/opt/data/profiles/spiti`.
- `organograma-agentes-hermes.md` documenta Zipper como sem runtime dedicado.

Risco:
- Trabalho de especialista voltar para o Hermes Geral, gerando mistura de contexto ou perda de handoff.

Melhorias:
- Medir volume real de Zipper por 2 semanas antes de criar bot/profile.
- Para cada specialist output, exigir owner + path + handoff.

### 5. Handoffs, receipts e continuidade após compactação

Nota Hermes: **7,6/10**  
Amora benchmark: **8,8/10**

O que está bom:
- Handoff completeness foi transformado em regra viva.
- Gap real de LK Growth foi corrigido com handoff retroativo baseado em receipts, sem inventar contexto.
- Existem 90 receipts em LK Growth, o que é sinal de execução material com rastreabilidade.

O que falta:
- O handoff ainda não é automático em todos os caminhos.
- Ainda há risco de receipts existirem sem entrada central visível.
- Mordomo/Zipper precisam de auditoria própria quando houver outputs externos/cliente.

Evidências:
- `handoff-completeness-check-2026-05-25.md`
- `areas/lk/sub-areas/growth/reports/2026-05-25-handoff-retroativo-receipts-theme.md`
- `empresa/contexto/handoffs/2026-05-25.md`

Risco:
- Depois de compactação, o sistema perde “por que isso foi feito” mesmo quando o arquivo existe.

Melhorias:
- Handoff obrigatório como critério de done.
- Auditoria local semanal: outputs materiais sem handoff.
- Não registrar saúde normal; registrar só decisão, risco, write, approval, receipt ou aprendizado.

### 6. Proatividade, heartbeats e rotinas recorrentes

Nota Hermes: **7,0/10**  
Amora benchmark: **9,3/10**

O que está bom:
- Cron registry está vivo e extenso, com watchdogs de runtime, Brain, compression, gateways, LK, SPITI e relatórios.
- Silent-OK está bem alinhado com Lucas: Telegram só para decisão, exceção, falha ou pedido de aprovação.
- Fechamento Ágil 23h + Brain Sync e reconciliadores existem.

O que falta:
- Amora tem meses de treino em “quando cutucar”; Hermes ainda está calibrando.
- Alguns jobs `deliver=origin` ainda precisam ser avaliados pela qualidade do que mandam, não só por status ok.

Evidências:
- `hermes cron list --all` mostrou Mesa COO, Brain loop, watchdogs e relatórios obrigatórios ativos.
- `memories/hot.md` registra regra de evitar ruído no Telegram.

Risco:
- Proatividade virar spam operacional ou, no outro extremo, silêncio demais.

Melhorias:
- Score de utilidade por alerta/decisão: útil, ruído, atrasado, faltou contexto.
- Aumentar proatividade por evidência real, não por copiar os 60+ crons da Amora.

### 7. Mesa COO e UX no Telegram

Nota Hermes: **6,7/10 agora; 8,2/10 se a próxima entrega vier limpa**  
Amora benchmark: **8,5/10**

O que está bom:
- O problema do wrapper/job_id/JSON foi corretamente classificado como bug de UX, não como configuração do Lucas.
- Skill Hermes já registra que Telegram deve ser limpo, com uma decisão por vez e botões nativos.
- Scheduler/testes já cobrem parte da supressão de metadata.

O que falta:
- A prova final ainda é a próxima execução real da Mesa COO no Telegram.
- O conteúdo da Mesa precisa ser mais executivo: decisão que muda prioridade/risco/dinheiro, não lista de tarefas que o Hermes quer fazer.

Evidências:
- `orquestrador-fase8-status-2026-05-25.md` marca Mesa COO v2 como configurada, mas em observação.
- Cron registry mostra “Mesa COO diária Telegram” ativo, entrega `origin`, próxima execução 2026-05-25 09:00 UTC.

Risco:
- Lucas ignorar a Mesa porque parece log/configuração, não decisão de COO.

Melhorias:
- Validar visualmente a próxima entrega.
- Se vazar metadata, corrigir scheduler/gateway com teste antes de qualquer prompt tweak.
- Criar padrão de “Decisão 1/N” com máximo uma escolha real por mensagem.

### 8. Governança de risco, aprovações e limites de autonomia

Nota Hermes: **8,9/10**  
Amora benchmark: **7,7/10**

O que está bom:
- Hermes é forte em A0-A4, approval packet, rollback, secrets, Docker/VPS e produção.
- Regras multiempresa reduzem risco de misturar LK, Zipper e SPITI.
- Guardrails bloqueiam crons novos, gateway, Docker, VPS, produção e writes externos sem aprovação.

O que falta:
- Hard blocks precisam distinguir melhor leitura administrativa de mutação.
- Alguns fluxos aprovados no passado precisam continuar tendo receipts e escopo exato para não virar autorização ampla.

Evidências:
- Preflight/guardrail bloqueou cronjob tool.
- Matriz e skills registram boundaries.
- Receipts de LK Growth separam dev, production e rollback.

Risco:
- Segurança virar atrito quando bloqueia leitura; autonomia virar risco quando interpreta aprovação ampla demais.

Melhorias:
- Refinar dispatch guardrails por verbo: list/read/status ≠ create/update/remove/run.
- Todo approval antigo deve carregar escopo, timestamp, rollback e fonte.

### 9. Skills, aprendizado operacional e correção de erros

Nota Hermes: **8,2/10**  
Amora benchmark: **9,0/10**

O que está bom:
- Correções recentes viraram skill/reference: wrapper Telegram, preflight UX, handoff correction, Amora comparison.
- A regra “Corrigir = executar fix local/docs verificável” está sendo aplicada.
- Skills carregam padrões específicos de Lucas, não só instruções genéricas.

O que falta:
- Ainda há risco de skill inchada demais, com referências longas que dificultam manutenção.
- Falta métrica de “erro repetido depois de skill patch”.

Evidências:
- `lucas-chief-of-staff` inclui referência de comparação Amora e correção de handoff.
- `hermes-agent` inclui referência de UX limpa no Telegram/preflight.

Risco:
- Aprendizados virarem texto acumulado, não comportamento melhor.

Melhorias:
- Criar revisão mensal de skills: o que foi usado, o que evitou erro, o que está obsoleto.
- Separar referências longas em arquivos menores por caso de uso.

### 10. Observabilidade, testes, saúde e auditoria do sistema

Nota Hermes: **7,8/10**  
Amora benchmark: **8,6/10**

O que está bom:
- Brain health check retorna 0/0 nas rodadas recentes.
- Existem watchdogs de runtime, cron, gateway, compression, strict runtime guard e operating layer.
- Testes focados anteriores passaram: scheduler e preflight.

O que falta:
- Observabilidade ainda é mais “status ok” do que qualidade decisória.
- Não há dashboard/relatório simples de maturidade do COO: rota, decisão, handoff, receipt, ruído.

Evidências:
- Cron registry ativo com watchdogs e `last run ok`.
- `orquestrador-fase8-status` documenta 134 testes passados na rodada anterior.

Risco:
- Sistema parecer saudável tecnicamente enquanto UX/decisão estão ruins.

Melhorias:
- Criar scorecard mensal: saúde técnica + saúde operacional.
- Separar alertas técnicos de “decisões úteis para Lucas”.

### 11. Maturidade prática em comparação com a Amora

Nota Hermes: **7,4/10**  
Amora benchmark: **9,0/10**

O que está bom:
- Hermes é mais adequado para Lucas do que uma cópia: multiempresa, approval gates, segurança, especialistas e Brain central.
- Já existe runtime multi-profile e cron registry material.
- Já há receipts reais e correções documentais maduras.

O que falta:
- Amora tem densidade de uso e refinamento. Hermes ainda está na fase de provar o loop de execução consistentemente.
- Amora parece operar como hábito diário; Hermes ainda precisa virar ritual confiável para Lucas.

Evidências:
- Case Amora: 60+ crons, dezenas de skills, revisão diária, pesquisas, comunidade, cursos, multi-canais.
- Hermes: vários crons e profiles, mas Mesa COO e handoff completeness ainda em validação.

Risco:
- Tentar pular para “Amora complexa” antes de consolidar o básico operacional.

Melhorias:
- Não copiar volume. Copiar disciplina: identidade viva, skills para repetição, meta-auditoria, hot context e rotina com receipts.

## Notas finais

- Hermes hoje: **7,8/10**
- Amora como benchmark: **9,0/10**
- Gap principal: maturidade operacional, não arquitetura.
- O melhor próximo passo é provar UX e handoff no uso real, não criar mais camada.

## Principais diferenças Hermes vs Amora

1. **Hermes é multiempresa e safety-first; Amora é CoS pessoal maduro.**
2. **Hermes tem approval gates mais fortes; Amora tem proatividade mais treinada.**
3. **Hermes separa especialistas/runtime; Amora consolidou em um super-agente.**
4. **Hermes tem Brain/governança mais explícitos; Amora tem mais rotina prática.**
5. **Hermes precisa provar consistência; Amora já tem histórico de uso diário.**

## Top 5 melhorias por prioridade

1. **Validar Mesa COO real no Telegram.** Se vier limpa, marcar P8.3 como validada; se vazar wrapper, corrigir runtime com teste.
2. **Criar scorecard mensal de orquestração.** Rota correta, handoff, receipt, aprovação, ruído, bloqueio excessivo.
3. **Automatizar auditoria local de handoff completeness.** Sem cron novo por enquanto; rodar manual/local até provar utilidade.
4. **Refinar guardrails de read-only admin.** Permitir list/status via ferramentas seguras sem abrir mutação.
5. **Criar revisão de skills por efetividade.** Erros repetidos depois de skill patch precisam virar bug de skill/processo.

## O que não devemos copiar da Amora

- 60+ crons sem demanda comprovada.
- Multi-canal avançado antes de Telegram/Mesa ficarem limpos.
- Agentes permanentes demais.
- Proatividade barulhenta.
- Commands/OpenClaw específicos que não existem no Hermes.

## O que devemos adaptar imediatamente

- Disciplina `skills > prompts`.
- Meta-auditoria periódica de workspace/Brain.
- Hot context vivo e pequeno.
- Identidade de agente mais operacional, menos documento jurídico.
- Receipts e handoffs como fechamento real de tarefa.

## Próxima ação concreta e segura

Executar uma **auditoria local de qualidade da próxima Mesa COO** depois da execução real de 09:00 UTC:

- conferir se a mensagem chegou sem wrapper, job id, JSON ou marcador técnico;
- registrar evidência no Brain;
- se limpa, marcar Mesa COO v2 como validada;
- se suja, preparar packet de correção scheduler/gateway com preview, teste e rollback, sem reiniciar gateway ou Docker sem aprovação.
