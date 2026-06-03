# PRD — Superpowers Operating System para Hermes/Lucas

**Data:** 2026-06-02  
**Status:** PRD aprovado em direção; implementação pendente de plano executor  
**Owner lógico:** Hermes Geral / default profile  
**Escopo de rollout:** todos os perfis, com rollout gradual e fail-safe  
**Modo Superpowers usado:** Full — `superpowers` + `brainstorming` + `writing-plans` + `hermes-agent`  

---

## 1. Resumo executivo

Implementar o **Superpowers Operating System** como uma camada nativa de disciplina operacional no ecossistema Hermes/Lucas.

Hoje, Superpowers já existe como skill/procedimento e foi incorporado em memória, Brain, skills e AGENTS.md. Porém, a aderência ainda depende demais do agente lembrar e obedecer ao prompt. O produto proposto transforma Superpowers em um sistema observável e parcialmente auto-corretivo:

- classifica automaticamente o tipo e risco de cada tarefa;
- seleciona os procedimentos/skills obrigatórios antes de agir;
- registra evidência de conformidade;
- impede ou sinaliza claims sem verificação;
- mede qualidade, autonomia, segurança e ruído;
- corrige automaticamente drift local/documental/runtime permitido;
- entrega um resumo diário curto no Telegram com score e decisões pendentes;
- preserva aprovação explícita para Docker, VPS, secrets, Traefik e writes externos.

A tese: **Superpowers deixa de ser uma lembrança no prompt e vira uma camada operacional do Hermes.**

---

## 2. Objetivos

### 2.1 Objetivos de produto

1. **Usar a skill certa antes de agir**
   - PRD → `superpowers` + `brainstorming`.
   - Plano de implementação → `writing-plans`.
   - Código/feature/bugfix → `test-driven-development`.
   - Bug/falha → `systematic-debugging`.
   - Claim de conclusão → `verification-before-completion`.
   - Multi-workstream → `dispatching-parallel-agents` ou `delegate_task` com verificação do parent.
   - Skill authoring → `writing-skills`.

2. **Reduzir retrabalho e erro operacional**
   - Menos execução sem contexto.
   - Menos diagnóstico por chute.
   - Menos “feito” sem evidência.
   - Menos drift entre Brain, skills, crons e runtime.

3. **Aumentar autonomia segura**
   - Permitir correções locais e runtime amplas quando não envolvem Docker/VPS/secrets/externos.
   - Manter fail-closed para ações sensíveis.
   - Evitar approval loops quando a ação é local, diagnóstica, documental ou já aprovada no escopo.

4. **Criar observabilidade diária**
   - Score composto por risco.
   - Violação procedural rastreável.
   - Decisões pendentes claras.
   - Telegram com resumo curto, não painel técnico.

5. **Aprendizado automático controlado**
   - Patches em skills quando uma lacuna procedural é descoberta.
   - Receipts locais no Brain.
   - Correção de AGENTS.md/Brain docs quando há drift.

### 2.2 Objetivos de qualidade

- Procedimento correto carregado antes de agir em tarefas relevantes.
- Verificação fresca antes de claims de conclusão.
- Telegram com baixo ruído e alto valor acionável.
- Rollout reversível e perfil por perfil.
- Score útil para decisão, não métrica cosmética.

---

## 3. Não objetivos

1. **Não copiar `obra/superpowers` literalmente**
   - Usar como metodologia fonte, adaptada ao Hermes, Telegram, Brain, perfis e multiempresa.

2. **Não criar burocracia para tarefas triviais**
   - Tarefas simples usam Micro-Superpowers internamente, sem ritual exposto.

3. **Não transformar Telegram em painel técnico**
   - Telegram recebe resumo diário curto, decisões e anomalias reais.

4. **Não permitir ações sensíveis sem aprovação**
   - Bloqueado sem aprovação escopada: Docker, VPS, Traefik, secrets, external writes, mensagens externas sensíveis, clientes/fornecedores/campanhas/logística/preço/reserva.

5. **Não depender de Mem0 ou provider externo de memória**
   - Brain continua sendo a camada rica; built-in memory continua boot mínimo.

6. **Não fazer enforcement cego**
   - O sistema deve reconhecer exceções legítimas, microtarefas e contexto de urgência.

---

## 4. Usuários e superfícies

### 4.1 Usuário principal

- Lucas Cimino, via Telegram, recebendo respostas, decisões, alertas e resumo diário.

### 4.2 Perfis envolvidos

Rollout gradual para todos os perfis:

1. `default` / Hermes Geral.
2. Perfis de gestão, Brain e Mesa COO.
3. Mordomo e assistência pessoal.
4. Perfis LK: Ops, Growth, Shopify, Trends, Atendimento, SEO/CRO quando existentes.
5. SPITI.
6. Zipper.
7. Outros especialistas futuros.

### 4.3 Superfícies Hermes

- Telegram Gateway.
- CLI/local sessions.
- Cron scheduler.
- Skills system.
- Brain docs/reports/routines.
- AGENTS.md/profile identity docs.
- Dashboard/Mission Control/Hermes dashboard quando disponível.
- Session store/telemetry local.

---

## 5. Princípios operacionais

1. **Skills antes de ação**
   - Se uma skill pode aplicar, carregar antes de responder ou agir.

2. **Peso proporcional ao risco**
   - Micro para simples.
   - Light para rotina diária.
   - Full para PRD, auditoria, código, produção, crons, multiempresa, externo, governança e tarefas recorrentes.

3. **Evidência antes de claim**
   - “Feito”, “corrigido”, “passando”, “rodou”, “está saudável” exigem evidência fresca.

4. **Autonomia com fronteiras**
   - Correções locais e runtime não-sensíveis podem ser automáticas.
   - Infra/externo/secrets ficam approval-gated.

5. **Silent-OK com digest executivo**
   - Sem spam de sucesso.
   - Um resumo diário curto com score e decisões pendentes.

6. **Aprendizado vira skill/Brain, não memória inchada**
   - Memória curta só para preferências duráveis.
   - Procedimentos e detalhes ficam em skills/Brain.

---

## 6. Arquitetura proposta

### 6.1 Componentes

#### A. `SuperpowersClassifier`

Classifica cada turno/tarefa em:

- tipo: pergunta simples, PRD, plano, código, debug, auditoria, operação, cron, perfil, negócio, externo, produção, skill authoring, pesquisa, decisão;
- risco: A0–A4;
- peso Superpowers: Micro, Light ou Full;
- skills candidatas obrigatórias;
- necessidade de evidência;
- necessidade de aprovação.

#### B. `ProcedureSelector`

Transforma classificação em procedimento:

- skills a carregar;
- ordem de procedimento;
- gates necessários;
- formato de saída esperado;
- telemetria mínima.

Exemplo:

- PRD: `superpowers` → `brainstorming` → perguntas → design → aprovação → PRD → `writing-plans` se implementação.
- Debug: `systematic-debugging` → reprodução/evidência → hipótese → fix → verificação.
- Claim: `verification-before-completion` → comando/evidência fresca → resposta.

#### C. `SkillLoadEnforcer`

Garante que skills obrigatórias foram carregadas quando aplicável.

Modo por fase:

- Observe-only: registra falta.
- Warn: adiciona lembrete interno/telemetry.
- Soft-block: impede conclusão sem carregar skill.
- Hard-block seletivo: usado só em classes de alto risco.

#### D. `VerificationGate`

Intercepta claims de conclusão e exige evidência fresca quando risco ou tipo exigem.

Claims monitorados:

- feito;
- corrigido;
- passando;
- saudável;
- sem erro;
- enviado;
- entregue;
- atualizado;
- ativo;
- funcionando.

O gate deve diferenciar:

- evidência local/documental;
- evidência runtime;
- evidência externa;
- claim parcial com limitação explícita.

#### E. `ApprovalBoundaryEngine`

Decide se a ação é permitida automaticamente ou exige aprovação.

Permitido automaticamente, com backup/receipt quando necessário:

- skills locais;
- Brain docs;
- AGENTS.md;
- planos/reports locais;
- telemetry local;
- configs de perfil não-sensíveis;
- crons locais/silent-OK não externos;
- runtime amplo não-Docker/VPS/secrets/externo quando rollback e healthcheck existirem.

Bloqueado sem aprovação escopada:

- Docker/container/compose/volumes;
- VPS/SSH/Traefik/firewall/DNS;
- secrets/tokens/env sensível;
- writes externos;
- mensagens para clientes/fornecedores;
- preço, reserva, disponibilidade, negociação, logística, campanha ou reclamação sem fonte/aprovação.

#### F. `TelemetryRecorder`

Registra eventos estruturados por sessão/tarefa:

- timestamp;
- profile;
- platform;
- task type;
- risk tier;
- required skills;
- loaded skills;
- procedure weight;
- verification evidence present/absent;
- approval required/granted/blocked;
- auto-corrections applied;
- final status;
- user-visible Telegram messages count/noise class.

Nenhum secret deve ser persistido. Conteúdo sensível deve ser redigido ou resumido.

#### G. `ComplianceScorer`

Calcula score composto diário e por perfil.

Dimensões:

1. **Conformidade procedural**
   - Skill correta carregada antes de agir.
   - Gates seguidos.

2. **Qualidade/verificação**
   - Claims com evidência fresca.
   - Testes/healthchecks/leituras usados quando necessário.

3. **Autonomia segura**
   - Tarefas resolvidas sem microgerenciamento.
   - Não criou approval loop.
   - Não ultrapassou fronteiras sensíveis.

4. **Redução de retrabalho**
   - Menos correções por falha de processo.
   - Menos repetição de pergunta já respondida.

5. **Ruído Telegram**
   - Penaliza status spam.
   - Premia resumo curto/decisão acionável.

6. **Aprendizado**
   - Lacunas viram skill/Brain patch quando apropriado.

#### H. `AutoCorrectionEngine`

Executa correções seguras quando telemetry detecta drift.

Categorias automáticas:

- patch de skill quando procedimento incompleto/errado;
- atualização de referência Brain;
- AGENTS.md com regra faltante;
- relatório local de drift;
- ajuste de cron local/silent-OK se não externo e sem risco sensível;
- config de perfil não-sensível com backup e verificação;
- geração de plano/approval packet para ações bloqueadas.

#### I. `DailyDigestGenerator`

Gera resumo diário curto no Telegram:

Formato desejado:

```text
Superpowers OS — resumo diário
Score: 92/100 🟢

Melhorou:
- PRDs e auditorias usaram Full Superpowers.
- 3 claims foram verificados antes de resposta.

Atenção:
- 1 perfil ainda em observe-only.
- 1 decisão pendente: aprovar enforcement em perfil X.

Ação sugerida:
- Aprovar Fase N ou manter observe-only por mais 24h.
```

Sem job IDs, sem wrappers, sem raw telemetry, sem boilerplate técnico.

#### J. Dashboard / Mission Control surface

Dashboard para inspeção rica:

- score diário e histórico;
- heatmap por perfil;
- violações por tipo;
- skills mais exigidas;
- tasks sem verificação;
- auto-correções aplicadas;
- decisões pendentes;
- rollout status por perfil;
- links para receipts/PRDs/planos.

Telegram continua somente executivo.

---

## 7. Matriz Micro / Light / Full

### Micro-Superpowers

Uso:

- perguntas simples;
- ações únicas sem risco;
- respostas informativas sem side effect.

Comportamento:

- classificar intenção internamente;
- checar se precisa ferramenta;
- responder direto;
- sem ritual visível.

### Light Superpowers

Uso:

- rotina diária;
- docs locais;
- triagem read-only;
- follow-ups simples;
- relatórios curtos;
- monitoramento.

Comportamento:

- carregar skill/domain quando relevante;
- consultar Brain/session/files se necessário;
- executar/verificar;
- salvar aprendizado durável só se útil;
- Telegram limpo.

### Full Superpowers

Uso obrigatório:

- PRD/spec/plano de produto;
- auditoria;
- código/bugfix/refactor;
- debugging;
- runtime/perfil/cron;
- multiempresa;
- produção/external-adjacent;
- decisões recorrentes;
- mudanças em skills;
- tarefas com 5+ tool calls;
- qualquer claim crítico.

Comportamento:

- skill chain explícita;
- design antes de implementação quando aplicável;
- plano escrito quando execução multi-step;
- verificação fresca;
- receipt/Brain artifact;
- score/telemetry.

---

## 8. Matriz de risco A0–A4

### A0 — trivial/local sem risco

- Resposta simples.
- Sem writes.
- Sem dados sensíveis.
- Micro.

### A1 — local/documental

- Brain docs.
- Skills.
- Relatórios locais.
- AGENTS.md.
- Light ou Full conforme complexidade.
- Auto-correção permitida.

### A2 — runtime local não-sensível

- Configs de perfil não-secretas.
- Toolsets.
- Crons locais/silent-OK.
- Watchdogs locais.
- Full.
- Backup/rollback/healthcheck obrigatórios.
- Auto-correção permitida se não envolver Docker/VPS/secrets/externos.

### A3 — produção-adjacent/sensível

- Gateway/restarts relevantes.
- Perfis especialistas com impacto operacional.
- Entregas Telegram desejadas.
- Business data flows.
- Full.
- Pode preparar e aplicar runtime amplo não-Docker/VPS/secrets/externos conforme política aprovada, sempre com rollback/evidência.

### A4 — bloqueado sem aprovação atual

- Docker/compose/containers/volumes.
- VPS/SSH/Traefik/DNS/firewall.
- Secrets/tokens/env sensível.
- External writes.
- Mensagens de negócio sensíveis.
- Pagamentos, preço, reservas, logística, reclamação, campanhas.

Saída esperada: approval packet limpo, não execução.

---

## 9. Score composto

### 9.1 Score total

Score diário: 0–100.

Pesos iniciais:

- 30% Conformidade procedural.
- 25% Verificação/evidência.
- 20% Autonomia segura.
- 10% Redução de retrabalho.
- 10% Ruído Telegram.
- 5% Aprendizado/auto-correção.

### 9.2 Multiplicador por risco

Violações em tarefas de maior risco têm penalidade maior:

- A0: peso 0.25.
- A1: peso 0.75.
- A2: peso 1.25.
- A3: peso 1.75.
- A4: peso 2.5.

### 9.3 Exemplos de penalidade

- PRD sem `superpowers + brainstorming`: penalidade alta.
- Claim “feito” sem evidência: penalidade média/alta conforme risco.
- Debug com fix antes de root cause: penalidade alta.
- Telegram com status spam: penalidade de ruído.
- Ação sensível sem aprovação: bloqueio e penalidade crítica.

### 9.4 Estados do score

- 95–100: 🟢 Excelente.
- 85–94: 🟢 Bom com pequenas melhorias.
- 70–84: 🟡 Atenção.
- 50–69: 🟠 Risco operacional.
- 0–49: 🔴 Falha de governança.

---

## 10. Requisitos funcionais

### RF1 — Classificação automática de tarefa

O sistema deve classificar cada novo turno/tarefa em tipo, risco e peso Superpowers.

Critérios de aceite:

- PRD detectado por termos: PRD, produto, requisitos, spec, plano de produto, roadmap, “faça perguntas”.
- Debug detectado por erro, falha, stacktrace, não funciona, bug, timeout, crash.
- Código detectado por repo, arquivo, teste, branch, PR, implementação.
- Runtime detectado por Hermes, gateway, cron, profile, toolset, config, model, provider, Telegram bot.
- Sensível detectado por Docker, VPS, secrets, SSH, Traefik, externos, clientes, preço, reserva, logística.

### RF2 — Seleção de skills obrigatórias

O sistema deve mapear tipo/risco para skills obrigatórias.

Critérios de aceite:

- PRD sempre exige `superpowers` e `brainstorming`.
- Implementação multi-step exige `writing-plans`.
- Código exige `test-driven-development` ou justificativa explícita para prototype mode.
- Debug exige `systematic-debugging`.
- Claims exigem `verification-before-completion`.
- Skill edits exigem `writing-skills`.

### RF3 — Enforcement progressivo

O sistema deve suportar modos:

1. observe-only;
2. warn;
3. soft-block;
4. hard-block seletivo.

Critérios de aceite:

- Default inicial por perfil é observe-only.
- Hard-block só ativa após baseline e aprovação/rollout interno do perfil.
- A0/Micro nunca deve virar burocracia.

### RF4 — Registro de telemetry local

O sistema deve registrar eventos estruturados sem secrets.

Critérios de aceite:

- Cada evento inclui profile, task type, risk, required skills, loaded skills, gates, verification e status.
- Secret scan ou redaction antes de persistência.
- Arquivos ficam em Brain ou runtime local apropriado.

### RF5 — Verification gate

O sistema deve detectar claims de conclusão e exigir evidência quando aplicável.

Critérios de aceite:

- Se claim crítico sem evidência, o agente deve verificar antes de responder ou declarar status parcial.
- O gate permite respostas honestas: “configurado, mas não ativo”, “arquivo escrito, runtime não reiniciado”, “triagem feita, ação externa bloqueada”.

### RF6 — Auto-correção segura

O sistema deve corrigir drift local e criar approval packets para ações bloqueadas.

Critérios de aceite:

- Skill incompleta pode receber patch.
- Brain docs/AGENTS.md podem ser atualizados.
- Config local não-sensível pode ser ajustada com backup.
- Docker/VPS/secrets/externos nunca são executados sem aprovação escopada.

### RF7 — Digest diário Telegram

O sistema deve entregar um resumo diário curto com score + decisões pendentes.

Critérios de aceite:

- Máximo recomendado: 8 bullets curtos.
- Sem job IDs/wrappers/raw JSON.
- Inclui score, status, principais melhorias, principais riscos, decisões pendentes.
- Silent-OK para detalhes; dashboard/Brain para relatório completo.

### RF8 — Dashboard

O sistema deve expor visão rica para inspeção.

Critérios de aceite:

- Score por dia/perfil.
- Violações por classe.
- Rollout status por perfil.
- Auto-correções aplicadas.
- Decisões pendentes.
- Links para artifacts locais.

### RF9 — Perfil e rollout fail-safe

O sistema deve permitir ativar/desativar por perfil e por modo.

Critérios de aceite:

- Cada perfil tem estado: disabled, observe, warn, soft-block, hard-block.
- Rollback simples para modo anterior.
- Falha no Superpowers OS não deve impedir resposta básica do Hermes; deve degradar para observe/report.

---

## 11. Requisitos não funcionais

### Segurança

- Nunca persistir secrets.
- Redigir tokens/chaves em telemetry.
- Fail-closed em A4.
- Approval packets limpos para ações sensíveis.

### Performance

- Classificação deve ser leve e não adicionar latência perceptível em Micro tasks.
- Para tarefas simples, não carregar cadeia longa de skills.
- Dashboard/score pode ser assíncrono.

### Observabilidade

- Eventos locais auditáveis.
- Receipts legíveis.
- Separar runtime truth de Brain health.

### UX

- Telegram executivo.
- Sem wrapper técnico.
- Sem approval loop.
- Perguntas uma por vez em brainstorming.

### Manutenibilidade

- Regras declarativas por skill/tipo/risco.
- Skill map versionado.
- Fácil adicionar novas skills/procedimentos.

---

## 12. Rollout proposto

### Fase 0 — Baseline e inventário

Objetivo: medir estado atual sem alterar runtime.

Entregáveis:

- inventário de perfis;
- mapa de skills obrigatórias por tarefa;
- baseline de sessões recentes;
- baseline de Telegram noise;
- relatório inicial de score.

Modo: observe-only.

### Fase 1 — Selector observável no default

Objetivo: classificar tarefas e registrar telemetry no Hermes Geral.

Entregáveis:

- `SuperpowersClassifier` inicial;
- `ProcedureSelector` declarativo;
- telemetry local;
- score diário do default.

Modo: observe-only → warn.

### Fase 2 — Enforcement leve no default

Objetivo: impedir falhas óbvias de processo em tarefas de risco.

Entregáveis:

- soft-block para PRD sem `superpowers + brainstorming`;
- verification gate para claims críticos;
- debug gate para falhas/bugs;
- digest diário curto.

Modo: warn → soft-block seletivo.

### Fase 3 — Auto-correção local

Objetivo: corrigir drift seguro automaticamente.

Entregáveis:

- skill patch suggestions/applies;
- Brain doc drift patch;
- AGENTS.md propagation;
- local receipts;
- approval packet generator para A4.

Modo: soft-block + auto-correct A1/A2 permitido.

### Fase 4 — Rollout multi-profile gradual

Objetivo: levar para todos os perfis com fail-safe.

Ordem sugerida:

1. default;
2. Brain/Mesa COO;
3. Mordomo;
4. LK Growth/Shopify/Ops;
5. SPITI;
6. Zipper;
7. demais.

Cada perfil passa por:

- observe 24–48h;
- score baseline;
- warn;
- soft-block em classes de alto risco;
- auto-correct permitido conforme política.

### Fase 5 — Dashboard e hard-block seletivo

Objetivo: maturidade operacional.

Entregáveis:

- dashboard;
- score histórico;
- hard-block seletivo A3/A4;
- decisões pendentes centralizadas;
- integração com Mission Control/Hermes dashboard quando apropriado.

---

## 13. Políticas de auto-correção

### 13.1 Permitido automaticamente

- Criar/editar relatórios Brain locais.
- Patch em skill local quando há lacuna clara.
- Atualizar AGENTS.md local.
- Criar plano/PRD/receipt.
- Ajustar configuração não-secreta de perfil com backup.
- Ajustar cron local/silent-OK quando não envolve externo e tem rollback.
- Rodar testes e healthchecks locais.
- Gerar dashboard local.

### 13.2 Permitido com cuidado e receipt

- Reiniciar processo de perfil não-Docker quando rollback/healthcheck estiverem claros.
- Aplicar runtime amplo não-Docker/VPS/secrets/externos.
- Alterar toolsets de perfil não-sensíveis.
- Ativar watchdog local silent-OK.

### 13.3 Bloqueado sem aprovação escopada

- Docker/compose/container/volume.
- VPS/SSH/Traefik/DNS/firewall.
- Secrets/tokens/env sensível.
- External writes/API POST/PUT/DELETE.
- Envio de mensagem externa de negócio sensível.
- Campanhas, preço, reserva, logística, reclamações.

---

## 14. UX do digest diário

### 14.1 Conteúdo

- Score geral.
- Status: verde/amarelo/laranja/vermelho.
- 2–4 melhorias relevantes.
- 1–3 atenções reais.
- Decisões pendentes.
- Próxima ação recomendada.

### 14.2 Exemplo

```text
Superpowers OS — resumo diário
Score: 91/100 🟢

Melhorou:
- PRDs seguiram Superpowers + brainstorming.
- Claims críticos tiveram evidência antes da resposta.
- Drift em 2 docs locais foi corrigido automaticamente.

Atenção:
- LK Growth ainda está em observe-only.
- 1 task de runtime precisa aprovação por envolver Docker.

Decisão:
- Aprovar soft-block no Mordomo amanhã?
```

### 14.3 Anti-ruído

Não enviar:

- “tudo ok” sem score/decisão;
- job ID;
- raw JSON;
- telemetry completa;
- logs técnicos;
- fallback benigno;
- recuperado sem ação.

---

## 15. Dashboard

### 15.1 Visões mínimas

- Overview diário.
- Score por perfil.
- Violação por tipo de procedimento.
- Claims sem evidência.
- Skills obrigatórias mais usadas.
- Auto-correções aplicadas.
- Decisões bloqueadas por aprovação.
- Rollout status.

### 15.2 Dados mínimos por evento

```json
{
  "timestamp": "2026-06-02T00:00:00Z",
  "profile": "default",
  "platform": "telegram",
  "task_type": "prd",
  "risk": "A2",
  "weight": "full",
  "required_skills": ["superpowers", "brainstorming"],
  "loaded_skills": ["superpowers", "brainstorming", "writing-plans", "hermes-agent"],
  "verification_required": true,
  "verification_present": true,
  "approval_required": false,
  "auto_correction": false,
  "status": "ok"
}
```

---

## 16. Acceptance criteria

### Produto

- Todo PRD passa por `superpowers + brainstorming`.
- Todo plano multi-step passa por `writing-plans`.
- Todo debug relevante passa por `systematic-debugging`.
- Todo claim crítico passa por verificação ou é declarado parcial.
- Todo perfil tem rollout status visível.
- Telegram recebe resumo diário curto com score + decisões pendentes.

### Segurança

- Zero secrets em telemetry, Brain reports ou Telegram.
- A4 sempre bloqueado sem aprovação escopada.
- Auto-correções têm rollback ou são puramente documentais.

### Qualidade

- Score composto gerado diariamente.
- Violações geram aprendizado ou decisão.
- Menos retrabalho por falta de processo.
- Sem aumento material de ruído no Telegram.

### Operacional

- Sistema degrada para observe-only se falhar.
- Pode desativar por perfil.
- Pode reverter modo por perfil.
- Brain health e secret scan continuam passando após patches documentais.

---

## 17. Riscos e mitigação

### Risco: burocracia excessiva

Mitigação:

- Micro/Light/Full.
- Não expor ritual em tarefas simples.
- Telegram só resumo/decisão.

### Risco: enforcement bloqueia trabalho legítimo

Mitigação:

- Rollout observe-only primeiro.
- Soft-block antes de hard-block.
- Override por perfil com receipt.

### Risco: latência

Mitigação:

- Classificador leve.
- Regras declarativas antes de LLM quando possível.
- Dashboard assíncrono.

### Risco: auto-correção perigosa

Mitigação:

- Limites claros A0–A4.
- Backups/rollback.
- Approval packet para sensível.

### Risco: métrica vira teatro

Mitigação:

- Score ponderado por risco.
- Penalizar ruído e ausência de evidência.
- Usar métricas para decisões, não vaidade.

---

## 18. Perguntas resolvidas neste PRD

1. **Nível de automação:** máximo.
2. **Escopo:** todos os perfis, rollout gradual e fail-safe.
3. **Autonomia:** runtime amplo permitido, exceto Docker/VPS/secrets/externos.
4. **Telegram:** resumo diário curto com score + decisões pendentes.
5. **Métrica:** score composto por conformidade, qualidade, autonomia e risco.

---

## 19. Decisões ainda pendentes antes da implementação

1. Onde implementar primeiro o núcleo técnico:
   - no agent loop principal;
   - como plugin;
   - como camada híbrida plugin + hooks no runtime.

2. Onde persistir telemetry:
   - Brain reports JSONL;
   - session DB extension;
   - diretório runtime por perfil;
   - combinação dos três.

3. Qual dashboard usar primeiro:
   - relatório local/Brain;
   - Mission Control;
   - Hermes dashboard oficial/terceiro;
   - página estática local.

4. Qual janela de baseline:
   - 24h;
   - 48h;
   - 7 dias.

5. Horário do digest diário:
   - acoplar ao ciclo 02h30;
   - criar rotina própria;
   - incluir no relatório Hermes existente.

---

## 20. Recomendação do PRD

Implementar como **sistema híbrido**:

1. Começar com telemetry/selector observe-only no default.
2. Persistir eventos em Brain/runtime local com secret redaction.
3. Gerar score diário e anexar ao relatório Hermes existente.
4. Adicionar soft-blocks seletivos para PRD/debug/claim crítico.
5. Expandir perfil por perfil.
6. Só depois criar dashboard rico.
7. Auto-correção local entra após baseline e com rollback.

Essa abordagem entrega o objetivo “máximo” sem quebrar o ecossistema: começa medindo, depois orienta, depois bloqueia seletivamente, depois corrige.

---

## 21. Próximo artefato recomendado

Criar um **Implementation Plan — Superpowers Operating System** usando `writing-plans`, com tarefas pequenas e verificáveis:

1. inventário técnico dos pontos de hook no Hermes;
2. schema de telemetry;
3. classifier rule-based v0;
4. selector declarativo;
5. recorder local;
6. scorer diário;
7. digest generator;
8. soft gates para PRD/debug/claim;
9. auto-correction engine A1/A2;
10. dashboard mínimo;
11. rollout por perfil;
12. testes e rollback.

O plano de implementação deve ser escrito antes de tocar código/runtime.

---

## 22. Receipts de Superpowers

- Design aprovado por Lucas: sistema completo com runtime selector/enforcer + telemetry + auto-correção local + dashboard/digest.
- Preferência registrada no PRD: resumo diário curto com score + decisões pendentes.
- Guardrail mantido: sem Docker/VPS/secrets/externos sem aprovação escopada.
- Escopo: todos os perfis com rollout gradual e fail-safe.
