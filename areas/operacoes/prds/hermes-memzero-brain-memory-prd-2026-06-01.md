# PRD — Mem0 + Hermes Brain Memory Architecture

> **Superpowers workflow aplicado:** `superpowers` + referência `hermes-memory-architecture-prd-workflow-20260601` + `writing-plans`.

**Data:** 2026-06-01  
**Status:** HISTÓRICO / DECISÃO SUPERADA: Lucas decidiu **não usar Mem0**. Não há canário/backlog ativo; reabrir só com novo pedido explícito.**

---

## 1. Resposta curta à pergunta de produto

### Devemos usar Mem0 mesmo tendo Hermes Brain?

**Recomendação:** não por padrão, e não agora no profile produtivo.

Mem0 não deve ser tratado como “mais um Brain”. Se ele guardar o mesmo conteúdo rico que o Brain já guarda, vira duplicação com risco:

- duas fontes de verdade;
- recall antigo/ruidoso;
- vazamento entre domínios/perfis;
- dificuldade de auditoria e deleção;
- custo/latência sem benefício claro.

### Quando Mem0 faria sentido?

Apenas como **camada aditiva de recall semântico**, não como fonte canônica.

Ele pode fazer sentido se resolver um problema real que Brain + `session_search` + context files não resolvem bem, por exemplo:

- lembrar padrões semânticos distribuídos em muitas conversas sem exigir busca manual;
- recuperar preferências não óbvias de Lucas sem inflar `USER.md`;
- trazer contexto relevante para um perfil descartável/canário sem carregar documentos longos no prompt;
- comparar qualidade de recall vs `session_search` em dataset sintético.

### Tese final

**Hermes Brain continua sendo a memória rica canônica. Mem0, se usado, deve ser só um índice semântico auxiliar, escopado, auditável, apagável e alimentado com conteúdo filtrado.**

---

## 2. Problema

A arquitetura de memória do Hermes já foi corrigida para separar:

- memória curta/injetada: `MEMORY.md` + `USER.md`, boot mínimo;
- memória rica: Hermes Brain, daily notes, `hot.md`, context files, skills, reports/receipts, `session_search`.

A dúvida agora é se ativar Mem0 adicionaria inteligência ou apenas duplicaria o Brain.

O risco principal é confundir três papéis:

1. **Fonte canônica:** onde a verdade operacional vive.
2. **Índice/recall:** mecanismo para encontrar a verdade certa.
3. **Prompt boot:** mínimo que entra sempre no contexto.

Se Mem0 virar fonte canônica paralela, piora a governança. Se virar índice auxiliar controlado, pode ser útil em um subconjunto de casos.

---

## 3. Objetivos

1. Definir o papel correto de Mem0 no ecossistema Hermes + Brain.
2. Evitar duplicação entre Mem0 e Hermes Brain.
3. Preservar o Brain como fonte de verdade operacional.
4. Criar uma estratégia segura de spike antes de qualquer ativação real.
5. Definir critérios objetivos para decidir “usar / não usar / usar só em perfis específicos”.

---

## 4. Não-objetivos

- Não ativar Mem0 agora.
- Não alterar `config.yaml` de produção.
- Não reiniciar gateway/profile/Docker/VPS.
- Não enviar dados reais sensíveis para provider externo.
- Não migrar o Brain para Mem0.
- Não substituir daily notes, reports, skills ou context files.
- Não usar Mem0 como lugar para credenciais, tokens, pedidos, estoque, logs, IDs de cron, PRs ou status operacional vivo.

---

## 5. Arquitetura proposta

### L0 — Sessão atual

Contexto conversacional imediato. É volátil.

**Uso:** raciocínio em andamento.  
**Não usar como:** memória durável.

### L1 — Built-in injected memory

`MEMORY.md` e `USER.md`.

**Uso:** boot mínimo, preferências estáveis, guardrails e ponteiros.  
**Meta:** curto, curado, aproximadamente 40–60% do limite quando possível.

### L2 — Hot / Daily

- `memories/hot.md`: prioridades e estado current.
- `memories/daily/YYYY-MM-DD.md`: decisões e entregas do dia.

**Uso:** continuidade operacional sem inflar prompt fixo.

### L3 — Hermes Brain canônico

`areas/`, `agentes/`, `empresa/`, `memories/`, `reports/`, `receipts/`.

**Uso:** fonte rica de verdade operacional, decisões, domínio, evidência e histórico curado.

### L4 — Skills

Procedimentos repetíveis, troubleshooting, padrões de verificação e rollback.

**Uso:** memória procedural.  
**Regra:** SOP não vai para Mem0 nem `MEMORY.md`; vira skill/reference.

### L5 — Session search

Histórico conversacional real.

**Uso:** recuperar origem de decisões e contexto passado sem promover tudo para memória.

### L6 — Mem0 / provider externo opcional

**Uso permitido:** índice semântico auxiliar, com ingestão filtrada e escopo claro.

**Não permitido:** fonte canônica, armazenamento de segredo, repositório paralelo do Brain, log bruto ou memória viva de produção.

---

## 6. Decisão de produto

### Decisão recomendada agora

**Não usar Mem0.**

O spike canário fica **rejeitado/encerrado** por decisão de Lucas. Reabrir somente se Lucas pedir novo PRD/spike explicitamente.

### Por quê

Hoje o maior problema já foi resolvido pela higiene:

- memória injetada compactada;
- Brain rico preservado;
- política canônica criada;
- roteador operacional documentado;
- provider externo ainda vazio na configuração.

Adicionar Mem0 agora sem hipótese específica criaria complexidade antes de provar ganho.

---

## 7. Casos de uso candidatos para spike

### Caso A — Recall semântico de preferências não sensíveis

Dataset sintético com preferências de resposta, formato, alertas e estilo.

**Pergunta:** Mem0 recupera preferências úteis melhor do que `USER.md` curto + `session_search`?

### Caso B — Recall cross-session de decisões não sensíveis

Dataset sintético de decisões de produto sem nomes reais de cliente, pedido, estoque, credenciais ou infraestrutura.

**Pergunta:** Mem0 encontra a decisão correta sem puxar ruído antigo?

### Caso C — Perfil descartável de teste

Criar profile canário sem dados reais.

**Pergunta:** Mem0 respeita escopo por profile e é simples de desligar/apagar?

---

## 8. Requisitos funcionais do spike

1. Criar ou usar um profile descartável.
2. Ativar Mem0 somente nesse profile, se o spike for aprovado.
3. Usar dataset sintético e não sensível.
4. Testar recall de:
   - preferência estável;
   - decisão antiga;
   - status temporário que não deve ser recuperado;
   - conteúdo de domínio diferente que não deve contaminar o recall.
5. Medir:
   - precisão;
   - ruído;
   - latência;
   - facilidade de inspeção/deleção;
   - isolamento por profile.
6. Registrar resultado em report local.
7. Encerrar o spike com decisão: `não usar`, `usar só canário`, `usar em perfil específico`, ou `avaliar alternativa`.

---

## 9. Requisitos não-funcionais

### Privacidade

- Nenhum dado real sensível no spike inicial.
- Nenhum segredo ou credencial.
- Nenhum dado operacional de cliente, pedido, estoque, fornecedor, banco, campanha ou token.

### Governança

- Brain continua fonte canônica.
- Todo conteúdo persistido em Mem0 deve ter classe de dado e motivo.
- Deve existir rollback: desligar provider e apagar dados do teste.

### Segurança

- Sem Docker/VPS/gateway restart no PRD.
- Sem mudanças em produção sem aprovação separada.
- Sem exportar dados reais antes de avaliação explícita de risco.

### Qualidade

- Mem0 só passa se trouxer contexto útil com menos ruído do que `session_search`.
- Deve falhar corretamente em status temporário: não pode ressuscitar informação velha como se fosse atual.

---

## 10. A0–A4 matriz de autonomia

### A0 — Permitido sem aprovação adicional

- Ler docs oficiais e locais.
- Escrever PRD/plano local.
- Criar report de avaliação.
- Criar dataset sintético local.

### A1 — Permitido com cuidado local

- Criar arquivos de spike local sem provider real.
- Criar checklist de teste.
- Preparar comandos sem executá-los.

### A2 — Requer aprovação explícita

- Criar profile descartável real.
- Alterar config de memória de profile canário.
- Instalar dependência/SDK de provider externo.

### A3 — Requer aprovação explícita forte + rollback

- Ativar Mem0/Honcho/etc. em qualquer profile real.
- Enviar qualquer conteúdo real do Brain para provider externo.
- Conectar provider externo a Telegram/gateway.

### A4 — Bloqueado neste PRD

- Docker/VPS/Traefik.
- Gateway restart produtivo.
- External writes de negócio.
- Credenciais em memória/provider.
- Substituir Brain por Mem0.

---

## 11. Métricas de sucesso

O spike só é considerado bem-sucedido se:

- precisão de recall útil for claramente superior ao baseline em casos definidos;
- não recuperar status temporário como verdade atual;
- respeitar isolamento por profile/domínio;
- houver deleção/rollback claro;
- custo e latência forem aceitáveis;
- auditoria mostrar que não virou fonte canônica paralela.

Baseline de comparação:

- `USER.md`/`MEMORY.md` boot mínimo;
- Brain policy/context files;
- `session_search`;
- reports/receipts/daily/hot.

---

## 12. Riscos

### Risco 1 — Dupla fonte de verdade

Mitigação: Mem0 nunca recebe verdade canônica; recebe apenas resumos sintéticos/filtrados ou ponteiros.

### Risco 2 — Recall antigo virar instrução atual

Mitigação: incluir testes de status temporário e política de expiração.

### Risco 3 — Vazamento entre empresas/perfis

Mitigação: profile descartável no spike; depois escopo por profile obrigatório.

### Risco 4 — Privacidade/custo

Mitigação: dataset sintético; nenhum dado real antes de aprovação.

### Risco 5 — Prompt ainda inflar

Mitigação: Mem0 não substitui higiene de prompt; recall externo deve ser seletivo.

---

## 13. Plano de implementação do spike

> Este plano é deliberadamente local/canário. Não executa provider real sem aprovação.

### Tarefa 1 — Preparar dataset sintético

**Objetivo:** criar exemplos sem dados reais para testar recall.

**Arquivo:**

- Criar: `reports/governance/mem0_spike-synthetic-dataset-2026-06-01.md`

**Conteúdo mínimo:**

- 10 preferências duráveis sintéticas;
- 10 decisões antigas sintéticas;
- 10 status temporários que devem expirar;
- 5 exemplos de domínio cruzado que não devem contaminar.

**Verificação:** arquivo existe, sem secrets, sem dados reais.

### Tarefa 2 — Definir queries de avaliação

**Arquivo:**

- Criar: `reports/governance/mem0_spike-eval-queries-2026-06-01.md`

**Verificação:** cada query tem resposta esperada e classe de risco.

### Tarefa 3 — Criar approval packet para ativação canário

**Arquivo:**

- Criar: `reports/governance/mem0_canary-approval-packet-2026-06-01.md`

**Deve conter:**

- profile alvo;
- provider;
- dados permitidos;
- dados bloqueados;
- comandos propostos;
- rollback;
- critérios de sucesso/falha.

### Tarefa 4 — Se aprovado, ativar apenas no profile canário

**Status:** depende de aprovação futura.

**Não executar agora.**

### Tarefa 5 — Rodar avaliação e comparar baseline

**Status:** depende de ativação futura.

Comparar Mem0 contra:

- consulta manual em Brain;
- `session_search`;
- boot memory curta.

### Tarefa 6 — Decisão final

Criar report final:

- `reports/governance/mem0_spike-result-YYYY-MM-DD.md`

Decisão possível:

1. não usar;
2. manter só canário;
3. usar em um profile de baixo risco;
4. reavaliar outro provider;
5. abandonar providers externos por enquanto.

---

## 14. Critérios de bloqueio

Não prosseguir se:

- Mem0 exigir envio amplo de dados reais para funcionar;
- não houver deleção/rollback claro;
- não houver isolamento por profile;
- recall trouxer ruído ou status temporário como atual;
- custo/latência forem imprevisíveis;
- houver risco de misturar LK/SPITI/Zipper/Hermes infra.

---

## 15. Conclusão

**Não é recomendável usar Mem0 agora como segunda memória rica. Sim, isso seria duplo e perigoso se duplicar o Brain.**

O desenho correto é:

- Brain = memória rica canônica;
- `MEMORY.md`/`USER.md` = boot mínimo;
- skills = procedimento;
- daily/hot/reports/session_search = continuidade/evidência/histórico;
- Mem0 = possível índice semântico auxiliar, só depois de spike isolado e aprovado.

Minha recomendação prática: **não ativar Mem0 em produção por enquanto. Se quisermos aprender, fazer um canário sintético e pequeno.**
