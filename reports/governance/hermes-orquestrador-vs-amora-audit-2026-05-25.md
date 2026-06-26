# Auditoria — Orquestrador Hermes vs Amora/Bruno

Data: 2026-05-25  
Owner: Hermes Geral / COO  
Escopo: auditoria local/read-only, comparação documental e operacional.  
Writes externos: não.

## Resumo executivo

O Hermes está **bem acima de uma implantação inicial** e já tem uma fundação operacional comparável ao padrão Amora em arquitetura: identidade por agente, Brain como fonte de verdade, Task Router, approval gates, handoff packets, silent-OK e separação entre central COO e especialistas.

A diferença principal é maturidade de uso real:

- **Amora** é referência de agente único maduro em produção diária, com muitos meses de refinamento, proatividade treinada, dezenas de skills e 60+ crons/rituais.
- **Hermes/Lucas** está mais correto para um ambiente multiempresa e mais seguro em approval gates, mas ainda precisa provar consistência operacional em uso real: Mesa limpa no Telegram, handoffs efetivamente usados, runtime dedicado onde fizer sentido e menos lacunas entre documentação e execução.

Nota geral comparativa:

- **Hermes hoje:** 7,4/10 como COO operacional multiempresa.
- **Hermes como documentação/arquitetura:** 8,3/10.
- **Hermes como rotina viva/proativa:** 6,4/10.
- **Benchmark Amora:** 9,0/10 em maturidade de agente pessoal/CoS, mas não deve ser copiado 1:1 porque o contexto do Lucas exige multiempresa, approval gates mais fortes e menor tolerância a ruído.

Tese: **não falta “mais prompt”; falta fechar o loop execução → receipt → handoff → aprendizado → rotina.**

## Fontes auditadas

### Referência Amora/Bruno

- `bruno-atual-20260519-analysis/texts/...LEIA_PRIMEIRO.docx.txt`
- `bruno-atual-20260519-analysis/texts/...AGENTS-amora.md.docx.txt`
- `bruno-atual-20260519-analysis/texts/...HEARTBEAT-amora.md.docx.txt`
- `cache/documents/paperclip_cases_20260505/.../case-amora.md`
- Skills/referências Hermes sobre Amora/OpenClaw e Task Router.

### Hermes/Lucas

- `empresa/contexto/organograma-agentes-hermes.md`
- `empresa/contexto/organograma-orquestrador-tarefas-hermes.md`
- `empresa/contexto/matriz-roteamento-tarefas-hermes.md`
- `empresa/contexto/task-router-hermes.md`
- `areas/operacoes/prds/hermes-orquestracao-fase-8-proatividade-handoffs-2026-05-24.md`
- `reports/governance/orquestrador-fase8-status-2026-05-25.md`
- Pacotes documentais `agentes/*` e LK Growth.

## Comparativo por área

### 1. Arquitetura central / modelo mental

Nota Hermes: **8,5/10**  
Benchmark Amora: **8,5/10**

Pontos fortes:

- Modelo central está claro: `Hermes Geral coordena; especialistas executam; Brain registra; produção/externo exige aprovação`.
- Melhor que Amora para contexto multiempresa, porque separa LK, Zipper, SPITI, Mordomo, Operações Hermes e Governança.
- A decisão de não criar muitos agentes permanentes à toa é correta. O próprio case Amora ensina que Bruno reduziu 5 agentes para 1 super-agente.

Lacunas:

- Ainda há risco de o Hermes Geral continuar executando tarefas de especialista por conveniência quando o caminho certo é rotear/handoff.
- O organograma está forte em documentação; precisa de mais receipts reais provando que cada rota foi usada corretamente.

Melhoria recomendada:

- Criar uma métrica mensal simples: `% de tarefas roteadas corretamente`, `% com handoff`, `% que exigiram aprovação`, `% com correção de rota`.

### 2. Identidade dos agentes: SOUL / IDENTITY / USER / AGENTS / MAPA / HEARTBEAT / TOOLS / MEMORY

Nota Hermes: **8,0/10**  
Benchmark Amora: **9,0/10**

Inventário verificado:

- Hermes Geral: pacote completo, com `SOUL` forte e `AGENTS` maduro.
- LK documental: pacote completo.
- Mordomo: pacote completo.
- SPITI: pacote completo, mas `SOUL.md` ainda é raso demais.
- Zipper: pacote completo e culturalmente mais denso.
- LK Growth: operacionalmente forte, mas falta `IDENTITY.md` e `USER.md` próprios na subárea.

Comparação com Amora:

- Amora é mais coesa em “uma personalidade viva” e boot sequence.
- Hermes é mais robusto em governança e separação de domínio.
- Hermes ainda tem alguns arquivos que parecem documentação de segurança/roteamento, não uma voz viva de agente.

Notas por subárea:

- Hermes Geral: **8,8**
- LK documental: **8,0**
- LK Growth: **7,2** — falta IDENTITY/USER próprios.
- Mordomo: **8,0**
- SPITI: **6,8** — SOUL fraco para importância do domínio.
- Zipper: **8,3**

Melhoria recomendada:

1. Criar `IDENTITY.md` e `USER.md` para LK Growth.
2. Reescrever `agentes/spiti/SOUL.md` com mais profundidade: silêncio > dado errado, precisão de lote/lance, postura institucional, relação Hub/Financial/CRM.
3. Adicionar uma seção curta de boot sequence padronizada nos AGENTS dos especialistas: ler SOUL → USER → MAPA → HEARTBEAT → MEMORY → fonte viva.

### 3. Task Router / approval gates

Nota Hermes: **8,7/10**  
Benchmark Amora: **7,5/10**

Pontos fortes:

- Hermes é mais seguro que Amora para o contexto do Lucas: A0-A4, production/external writes bloqueados, approval packets e rotas por negócio.
- Há proteção explícita contra Docker/VPS/gateway/Traefik/secrets sem aprovação.
- Há regra de não expor metadata técnica no Telegram.

Lacunas:

- O router ainda depende muito de disciplina documental + testes específicos; precisa de telemetria operacional para falsos positivos/negativos.
- Algumas rotas secundárias ainda são “documental/read-only” e não têm executor runtime dedicado.

Melhoria recomendada:

- Adicionar um relatório mensal de “erros de roteamento”: quando Hermes executou aqui mas deveria ter handoff, quando bloqueou demais, quando pediu aprovação desnecessária.

### 4. Handoff / ledger / receipts

Nota Hermes: **7,0/10**  
Benchmark Amora: **8,5/10**

Pontos fortes:

- Handoff packet e ledger existem.
- Template está definido.
- Fase 8 já colocou handoff como obrigatório para outputs materiais.

Lacunas:

- O ledger ainda pode virar documento morto se não for usado pelos especialistas reais.
- Falta uma rotina simples que confira se outputs em `reports/`, `areas/*/rotinas/` ou approval packets recentes têm handoff correspondente quando deveriam.

Melhoria recomendada:

- Criar um **Handoff Completeness Check** local/read-only semanal: lista outputs materiais sem handoff e gera apenas exceções.
- Definir `handoff_required=true` não como texto bonito, mas como critério de fechamento da tarefa.

### 5. Proatividade / HEARTBEAT / silent-OK

Nota Hermes: **6,8/10**  
Benchmark Amora: **9,0/10**

Pontos fortes:

- Contrato silent-OK está correto e alinhado com preferência do Lucas.
- Hermes já separa relatórios obrigatórios de watchdogs silenciosos.
- O caso da Mesa COO v2 corrige o problema de “blocão” e vai para decisão 1/N.

Lacunas:

- Ainda falta treino real: saber quando interromper Lucas com valor, não com status.
- A próxima Mesa precisa provar Telegram limpo: sem wrapper, sem job id, sem JSON, sem marcador técnico.
- Falta um `hot.md`/prioridades vivas tão central quanto o `memory/hot.md` da Amora.

Melhoria recomendada:

1. Criar/fortalecer `empresa/gestao/hot.md` como fila viva do COO: prioridades da semana, decisões abertas, riscos, handoffs pendentes.
2. Mesa COO deve puxar desse hot/contexto, não de intuição solta.
3. Começar com poucos checks proativos, medir utilidade e só depois ampliar.

### 6. Mesa COO / UX de decisão no Telegram

Nota Hermes: **6,5 agora; 8,0 se a próxima entrega real vier limpa**  
Benchmark Amora: **8,0**

Pontos fortes:

- Contrato v2 está certo: uma decisão por vez, máximo quatro, botões, sem metadados técnicos.
- A falha anterior foi corretamente tratada como bug de UX/runtime, não como configuração para Lucas tolerar.

Lacunas:

- A prova final ainda é visual: próxima execução real no Telegram.
- O conteúdo da Mesa ainda precisa melhorar em qualidade executiva: menos “tarefa que o Hermes quer fazer”, mais “decisão que muda prioridade, risco ou dinheiro”.

Melhoria recomendada:

- Classificar cada decisão Mesa como uma destas categorias:
  - dinheiro/receita;
  - risco/bloqueio;
  - cliente/externo;
  - produção/sistema;
  - prioridade estratégica.
- Se não cair em nenhuma, provavelmente não merece Telegram.

### 7. Runtime de especialistas

Nota Hermes: **6,2/10**  
Benchmark Amora: **8,5/10**

Pontos fortes:

- Existem profiles ativos para Mordomo, LK Growth e SPITI.
- Zipper foi corretamente mantido como documental/read-only até justificar runtime próprio.
- Hermes evita “agent sprawl” sem volume real.

Lacunas:

- Zipper ainda não tem runtime dedicado.
- LK Chief of Staff amplo ainda está mais documental que runtime; LK Growth cobre Growth, mas não toda operação LK.
- Handoff entre profile especialista e central ainda precisa de prova contínua.

Melhoria recomendada:

- Não criar bot Zipper ainda por vaidade. Primeiro medir volume de pedidos Zipper no Hermes/Mordomo por 2 semanas.
- Se houver volume, criar approval packet para Zipper runtime com escopo read-only + Telegram/WhatsApp mention responder limitado.

### 8. Brain / MAPA / navegação / fonte de verdade

Nota Hermes: **7,8/10**  
Benchmark Amora: **8,5/10**

Pontos fortes:

- Brain está bem mais amplo que Amora porque cobre empresas, governança, skills, rotinas, reports, PRDs e handoffs.
- MAPAs existem para os agentes principais.
- A regra “chat não é fonte de verdade” está internalizada.

Lacunas:

- O volume do Brain é alto; risco de arquivos antigos/legados confundirem futuros agentes.
- Ainda há menção documentada a marcas legadas em alguns AGENTS (`cerebro-cimino`, `/root`, `Claw`) com status de manutenção gradual.

Melhoria recomendada:

- Criar uma rotina local mensal de `legacy drift`: procurar instruções antigas que pareçam executáveis e marcar como legado ou atualizar para Hermes-native.

### 9. Skills / repetição vira procedimento

Nota Hermes: **7,5/10**  
Benchmark Amora: **9,0/10**

Pontos fortes:

- O ecossistema de skills do Hermes é grande e já guarda muitas correções do Lucas.
- Existem skills especializadas para Hermes, Chief of Staff, multiempresa, Brain governance, LK, Zipper, SPITI e roteamento.

Lacunas:

- Skills estão fortes, mas algumas estão enormes; risco de difícil manutenção e excesso de contexto.
- Falta medir quais skills são realmente usadas e quais estão obsoletas/conflitantes.

Melhoria recomendada:

- Auditoria trimestral de skills: usadas, duplicadas, desatualizadas, perigosas, candidatas a consolidação.
- Para cada fluxo repetido 2-3 vezes, criar skill curta ou referência, não aumentar prompts gerais.

### 10. Observabilidade, testes e saúde

Nota Hermes: **7,6/10**  
Benchmark Amora: **8,0/10**

Pontos fortes:

- Testes focados existem para scheduler e preflight.
- Brain health check passa.
- Secret scan focado é rotina antes de reportar.
- Há preocupação correta em não reiniciar gateway/Docker sem aprovação.

Lacunas:

- Runtime truth ainda é consultado de forma sob demanda, não sempre conectado a um dashboard/receipts executivos.
- Alguns checks dependem de ferramentas bloqueadas por guardrails quando o contexto atual é approval-gated; precisamos separar melhor leitura de gerenciamento.

Melhoria recomendada:

- Criar um snapshot local read-only de runtime/cron/profile por dia e deixar a Mesa usar apenas resumo executivo dele.
- Mission Control deve mostrar estado e receipts, mas não virar painel que permite writes perigosos sem approval gate.

## Ranking de lacunas por impacto

### P0 — Corrigir antes de chamar de maduro

1. **Validar Mesa COO real no Telegram**: sem wrapper, sem job id, sem JSON, com botões nativos.
2. **Handoff real obrigatório**: outputs materiais de especialistas precisam aparecer no ledger/handoffs, não só nos reports.
3. **Hot context do COO**: criar/fortalecer uma fila viva de prioridades, riscos e decisões abertas.

### P1 — Melhorias de maturidade próximas

1. Completar LK Growth com `IDENTITY.md` e `USER.md`.
2. Reforçar SPITI `SOUL.md`.
3. Criar check semanal de handoff completeness.
4. Criar métrica de roteamento correto/incorreto.
5. Limpar ou marcar legados executáveis em `AGENTS.md` antigos.

### P2 — Só depois de volume real

1. Runtime dedicado Zipper.
2. Mais crons/proatividade.
3. Mais especialistas permanentes.
4. Dashboard Mission Control com ações reais além de preview/read-only.

## Nota por área

- Arquitetura central: **8,5**
- Identidade/documentação dos agentes: **8,0**
- Task Router/approval gates: **8,7**
- Handoff/ledger: **7,0**
- Proatividade/heartbeat: **6,8**
- Mesa COO/UX Telegram: **6,5 agora / 8,0 se validar ao vivo**
- Runtime de especialistas: **6,2**
- Brain/MAPA/fonte de verdade: **7,8**
- Skills/procedimentos: **7,5**
- Observabilidade/testes: **7,6**

## Veredito

O Hermes está **conceitualmente mais bem governado que a Amora para o contexto do Lucas**, porque precisa operar multiempresa com alto risco de writes externos, clientes, produção, estoque, leilão, arte, Docker/VPS e segredos. A Amora é mais madura em rotina viva e proatividade diária.

A próxima evolução não é criar mais agentes. É tornar o ciclo operacional inevitável:

```text
Pedido → Router → Executor certo → Preview/ação segura → Receipt → Handoff → Brain → Skill/rotina se repetir → Mesa só se houver decisão real
```

Se esse ciclo virar padrão, Hermes passa de “boa arquitetura” para COO de verdade.

## Próxima ação recomendada

Próximo passo único: **fortalecer o hot context + handoff completeness**, sem criar novo cron ainda.

Entrega local sugerida:

1. Criar/atualizar `empresa/gestao/hot.md` com prioridades, decisões abertas e handoffs pendentes.
2. Criar uma rotina documental `areas/operacoes/rotinas/handoff-completeness-check.md`.
3. Só depois decidir se isso vira watchdog/cron silencioso.

Nenhuma ação externa foi executada nesta auditoria.
