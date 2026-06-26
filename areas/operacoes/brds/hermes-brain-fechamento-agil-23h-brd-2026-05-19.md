# BRD — Hermes Brain: Fechamento Ágil 23h e consolidação multi-agente

Data: 2026-05-19
Status: **para aprovação de Lucas**
Responsável de negócio: Lucas Cimino
Sistema: Hermes Brain / Hermes Central / agentes especialistas
Tipo: BRD — Business Requirements Document

## 1. Resumo executivo

Lucas já tem o Hermes Brain como fonte de verdade documental, mas a operação agora tem múltiplos agentes, crons e perfis especialistas. O risco não é “não existir Brain”; o risco é algum trabalho do dia ficar preso em chat, profile, output local ou cron isolado e não subir para a Grande Mente.

Este BRD propõe o **Fechamento Ágil 23h**: um cron diário, às **23h BRT**, que fecha o dia de trabalho quando Lucas provavelmente já parou de operar, consolida o que aconteceu nas últimas 24h e registra no Hermes Brain:

- o que foi feito;
- decisões;
- pendências;
- riscos;
- entregas por agente/especialista;
- crons que rodaram;
- lacunas de handoff;
- próximos passos para amanhã.

A proposta adapta Bruno/OpenClaw sem copiar cegamente: Bruno sugere Revisão do Dia às 18h; para Lucas, o horário correto é **23h BRT**, porque 18h ainda é horário ativo de trabalho.

## 2. Problema de negócio

Hoje o Hermes já registra muita coisa no Brain:

- reports em `reports/`;
- decisões e pendências em `empresa/` e `memories/`;
- rotinas em `empresa/rotinas/` e `areas/*/rotinas/`;
- handoffs e documentação de agentes especialistas;
- outputs de crons como LK, Zipper, SPITI e Operações.

Mas a operação ficou multi-agente:

- Hermes Central / Grande Mente;
- LK Growth;
- Mordomo;
- SPITI;
- Zipper;
- LK OS;
- ZIZ OS;
- crons script-only;
- crons agent-driven;
- watchdogs silenciosos;
- reports externos aprovados.

Sem uma consolidação diária, existem riscos:

1. **Perda por compactação** — uma decisão fica só no chat e some da memória operacional.
2. **Agente-ilha** — um especialista executa algo e o Hermes Central não fica sabendo.
3. **Cron órfão** — um cron gera output, mas não vira contexto acionável.
4. **Ruído no Telegram** — confirmações operacionais aparecem para Lucas quando deveriam só salvar no Brain.
5. **Pendência invisível** — algo prometido fica aberto sem entrar na Mesa COO do dia seguinte.
6. **Memória inflada** — tentar jogar logs ou outputs longos na memória persistente em vez de versionar no Brain.

## 3. Inspiração Bruno/OpenClaw — releitura calma

### 3.1 Aula 6 — Workspace + MAPAs distribuídos

Bruno ensina que o agente escala quando tem workspace organizado e `MAPA.md` distribuído. Sem mapa, o agente improvisa e a estrutura vira bagunça. Cada pasta deve ter propósito claro.

Adaptação Hermes:

- O Hermes Brain já é o workspace vivo.
- `MAPA.md` global e MAPAs locais são a navegação oficial.
- Fechamento 23h deve salvar nos lugares corretos, não criar arquivos soltos.
- Se encontrar output sem rota, deve registrar gap de mapa/rotina.

### 3.2 Aula 7 — Memória + higiene de contexto

Bruno ensina 3 memórias:

1. boot/contexto padrão: `MEMORY.md`, dailies recentes, `hot.md`, MAPAs;
2. sessão: chat atual, limitado e sujeito a compactação;
3. semântica/workspace: busca por significado nos arquivos.

Ponto crítico: Memory Flush automático ajuda, mas não é 100% confiável. Bruno fala em confiabilidade aproximada de 70%. O princípio é: **salve antes de limpar**.

Adaptação Hermes:

- Chat/Telegram não é fonte final.
- Memória persistente do Hermes não deve virar log de sessão.
- O Brain guarda decisões, reports, receipts e dailies.
- Fechamento 23h é a rede de segurança contra compactação.

### 3.3 Aula 9 — Crons + Revisão do Dia + Heartbeat

Bruno diferencia:

- **cron**: horário exato, tarefa isolada, entrega definida;
- **heartbeat**: checagens leves, com silêncio quando não há valor.

O cron-âncora de Bruno é a Revisão do Dia às 18h. Ele lê a daily note, lista pendências, olha amanhã e manda resumo. Bruno também recomenda meta-cron às 7h para auditar crons.

Adaptação Hermes:

- A lógica da Revisão do Dia é correta.
- O horário de 18h é errado para Lucas.
- Para Lucas, o cron-âncora deve rodar às **23h BRT**.
- O output deve ser principalmente Brain-first, com Telegram só se aprovado/necessário.

### 3.4 Aula 13 — Multi-agente sem overengineering

Bruno alerta que vários agentes aumentam manutenção. Multi-agente só vale quando há domínio contínuo, canais distintos ou necessidade real de separação.

Adaptação Hermes:

- Lucas já tem estrutura multiempresa/multi-agente real.
- O problema não é criar mais agentes; é garantir que todos reportem à Grande Mente.
- O Fechamento 23h deve tratar cada agente/profile como fonte possível de handoff.
- Nenhum agente especialista deve ter “vida própria” fora do Brain.

## 4. Objetivos de negócio

1. Garantir que o trabalho do dia não dependa da janela de contexto do Telegram.
2. Fazer o Hermes Brain virar a fonte oficial do que aconteceu no dia.
3. Consolidar outputs de crons e agentes especialistas em um fechamento único.
4. Reduzir ruído no Telegram principal de Lucas.
5. Preparar a Mesa COO do dia seguinte com contexto limpo.
6. Detectar gaps de handoff, documentação e crons sem receipt.
7. Criar um ciclo Bruno/OpenClaw adaptado à realidade Hermes-native.

## 5. Não-objetivos

Este projeto **não** deve:

- criar novos agentes paralelos;
- enviar WhatsApp, e-mail, Klaviyo, campanha ou mensagem externa;
- alterar Shopify, GMC, Meta Ads, Tiny, Supabase, VPS, Docker ou banco;
- rodar ações produtivas fora do Brain;
- salvar credenciais, tokens ou logs crus;
- mandar relatório longo para Lucas todo dia às 23h;
- substituir a Mesa COO da manhã;
- substituir relatórios específicos de LK/Zipper/SPITI.

## 6. Requisito central

Criar um cron diário chamado:

```text
Hermes Brain Fechamento Ágil 23h
```

Schedule proposto:

```text
0 2 * * *
```

Interpretação:

- 02:00 UTC = 23:00 BRT do dia anterior, considerando UTC-3.
- O prompt do cron deve sempre calcular a data operacional em `America/Sao_Paulo`.
- O arquivo diário deve usar a data BRT, não a data UTC.

Exemplo:

```text
Execução UTC: 2026-05-20 02:00
Data operacional BRT: 2026-05-19
Arquivo: reports/daily-consolidation/2026-05-19.md
```

## 7. Modelo operacional proposto

```text
Durante o dia
  ↓
Chats, crons, reports, specialists e scripts geram outputs
  ↓
23h BRT — Fechamento Ágil
  ↓
Lê Brain + cron outputs + handoffs + reports recentes
  ↓
Consolida por área/agente
  ↓
Salva daily consolidation no Brain
  ↓
Atualiza pendências/hot docs quando seguro
  ↓
Produz resumo curto ou fica silencioso conforme regra aprovada
  ↓
Mesa COO da manhã usa o fechamento como fonte
```

## 8. Entradas do Fechamento 23h

O cron deve consultar, de forma segura e read-only:

### 8.1 Brain documental

- `reports/` — relatórios e receipts recentes;
- `areas/*/` — rotinas, projetos, handoffs e status por empresa;
- `empresa/gestao/pendencias.md` — pendências globais;
- `memories/*.md` — memórias executivas compactas;
- `MAPA.md` e MAPAs locais quando precisar localizar destino correto;
- `CHANGELOG.md` e `ROADMAP-30-DIAS-HERMES.md` quando houver mudança estrutural.

### 8.2 Crons Hermes

Usar `cronjob list` para inventariar:

- crons ativos;
- crons pausados;
- última execução;
- status;
- destino (`origin`, `local`, etc.);
- jobs que deveriam ser silenciosos;
- jobs que deveriam gerar receipt no Brain.

### 8.3 Agentes e profiles especialistas

O fechamento deve ter seção por agente/profile:

- Hermes Central / Grande Mente;
- LK Growth;
- Mordomo;
- LK OS / relatórios comerciais;
- Zipper OS;
- SPITI OS;
- ZIZ OS;
- outros perfis ativos.

Para cada um:

```md
- Atividade detectada:
- Handoff recebido:
- Artefato salvo no Brain:
- Pendência criada/fechada:
- Risco ou bloqueio:
- Próximo passo:
```

### 8.4 Session search — uso limitado

O cron pode usar `session_search` apenas para contexto recente quando necessário, mas não deve tentar reconstruir todo o dia só pelo chat.

Regra: se algo é importante e foi encontrado só em chat, o fechamento deve registrar como **“precisa de receipt/documentação”**.

### 8.5 Conversas e projetos por agente/profile

O Fechamento 23h deve cobrir não só “agentes” em abstrato, mas também as **conversas e projetos ativos** que vivem com cada um deles.

Para cada agente/profile relevante, registrar:

```md
- Conversas relevantes do dia:
- Projeto/rotina relacionado:
- Decisão ou pedido de Lucas:
- Artefato/receipt no Brain:
- Próximo follow-up:
- O que ficou apenas em chat e precisa ser documentado:
```

Cobertura mínima por família:

- **Hermes Central / Grande Mente:** Mission Control, Brain, governança, crons, Mesa COO, decisões multiempresa.
- **Lucas pessoal / Mordomo:** WhatsApp pessoal, agenda, follow-ups, conversas com clientes/fornecedores/contatos, sem expor conteúdo sensível no relatório executivo.
- **LK OS / LK Growth / LK reports:** vendas, CRM, Klaviyo, SEO/CRO/GEO, paid/influencer, stock/sourcing, WhatsApp LK e reports comerciais.
- **Zipper OS:** vendas de obras, colecionadores, artistas, feiras, comunicação, logística e WhatsApp/e-mail aprovados.
- **SPITI OS:** Hub, Financial, lances/leilões, CRM, conteúdo/growth, bot/profile SPITI e fontes oficiais.
- **ZIZ OS e outros perfis futuros:** registrar como área própria assim que houver profile, bot, rotina ou projeto ativo.
- **Watchdogs/crons script-only:** não são agentes conversacionais, mas entram como fonte operacional se geram alerta, receipt, relatório ou falha.

Critério importante: uma conversa só entra no fechamento se gerar decisão, pendência, risco, entrega, compromisso, correção, follow-up ou mudança de projeto. O fechamento **não deve virar transcrição de chat**.

### 8.6 Inventário vivo de cobertura

Para garantir que todos os agentes, conversas e projetos continuem cobertos, a Fase 1 deve criar ou atualizar um inventário vivo em:

```text
areas/operacoes/inventarios/crons-agentes-profiles.md
```

Esse inventário deve mapear:

- agente/profile/bot;
- canal ou superfície de conversa;
- empresa/área;
- projetos/rotinas associados;
- destino do handoff;
- se entra no Fechamento 23h;
- status: ativo, pausado, legado, desconhecido ou precisa validar.

Sem esse inventário, o BRD cobre bem a lógica, mas a cobertura real ainda fica parcial.

## 9. Saídas esperadas

### 9.1 Arquivo principal diário

Criar/sobrescrever de forma idempotente:

```text
reports/daily-consolidation/YYYY-MM-DD.md
```

Formato sugerido:

```md
# Fechamento Ágil — YYYY-MM-DD

Data operacional: YYYY-MM-DD BRT
Gerado em: timestamp UTC/BRT
Status: draft/ok/attention

## 1. Resumo executivo
- ...

## 2. Hoje foi feito
### Hermes Central
- ...
### LK
- ...
### Zipper
- ...
### SPITI
- ...
### ZIZ
- ...
### Mordomo / Lucas pessoal
- ...

## 3. Decisões do dia
- Decisão:
  - Área:
  - Fonte:
  - Onde foi registrada:

## 4. Pendências e bloqueios
- Pendência:
  - Responsável:
  - Próximo passo:
  - Prazo/urgência:

## 5. Crons e automações
- OK:
- Atenção:
- Pausados relevantes:
- Jobs com output local:
- Jobs com ruído Telegram indevido:

## 6. Handoffs de especialistas
- LK Growth:
- Mordomo:
- Zipper:
- SPITI:
- ZIZ:

## 7. Riscos / guardrails
- ...

## 8. Amanhã
- ...

## 9. Promover para memória/skills/rotinas
- ...

## 10. Fontes
- Arquivo/cron/report consultado: ...
```

### 9.2 Atualizações opcionais e seguras

O cron pode atualizar, se houver evidência clara e sem risco:

- `empresa/gestao/pendencias.md` — adicionar/fechar pendências factuais;
- `memories/pending.md` — versão compacta de pendências ativas;
- `empresa/gestao/hot.md` ou equivalente, se existir/adotado;
- inventário de crons/agentes, quando o job detectou mudança.

Se houver ambiguidade, o cron não deve editar; deve registrar sugestão no fechamento.

### 9.3 Entrega para Lucas

Proposta padrão para aprovação:

- **Salvar o relatório completo no Brain.**
- **Não mandar relatório longo no Telegram às 23h.**
- Enviar Telegram às 23h somente se houver:
  - falha crítica de cron;
  - risco para amanhã cedo;
  - pendência A1/A2 que precisa de Lucas antes de dormir;
  - erro de integração/segurança.
- Caso contrário, a Mesa COO da manhã referencia o fechamento.

Opção alternativa, se Lucas preferir:

- mandar sempre um resumo curtíssimo às 23h:

```text
Fechamento 23h salvo no Brain.
Atenções: X.
Amanhã: Y.
```

## 10. Regras de silêncio e ruído

O fechamento 23h deve seguir a regra Bruno de heartbeat silencioso adaptada para cron:

- Sem novidade relevante → salva no Brain e não interrompe.
- Tudo OK → não mandar “tudo certo” gratuito, salvo se Lucas escolher receber confirmação.
- Atenção leve → registrar no Brain e deixar para Mesa COO.
- Atenção crítica → avisar Lucas no Telegram.

## 11. Requisitos funcionais

### RF1 — Criar daily consolidation

Todo dia às 23h BRT, criar `reports/daily-consolidation/YYYY-MM-DD.md` com o fechamento do dia.

### RF2 — Consolidar por área e agente

O relatório deve separar pelo menos:

- Hermes Central;
- Lucas pessoal/Mordomo;
- LK;
- Zipper;
- SPITI;
- ZIZ;
- Operações/Infra/Governança.

### RF3 — Auditar crons das últimas 24h

Incluir status dos crons relevantes:

- OK;
- falhou;
- pausado;
- output local;
- output no Telegram;
- sem receipt/documentação.

### RF4 — Detectar handoff ausente

Se um agente/profile tiver atividade ou cron associado sem registro no Brain, marcar como gap.

### RF5 — Preparar amanhã

Gerar seção “Amanhã” com pendências, prazos, decisões abertas e pontos para a Mesa COO.

### RF6 — Promover aprendizados duráveis com parcimônia

Não jogar tudo na memória. Promover apenas:

- correção de Lucas;
- regra operacional durável;
- preferência estável;
- rotina repetida;
- decisão de governança.

### RF7 — Ser idempotente

Se rodar duas vezes, deve atualizar o mesmo arquivo do dia ou criar versão com timestamp apenas se necessário, sem duplicar pendências.

## 12. Requisitos não funcionais

- Segurança: nunca incluir secrets ou valores de tokens.
- Auditabilidade: todo item relevante deve apontar fonte.
- Baixo ruído: Telegram só para alerta/resumo aprovado.
- Custo: usar contexto enxuto; não varrer tudo sem necessidade.
- Clareza: relatório deve ser executivo, não log bruto.
- Separação multiempresa: LK, Zipper, SPITI, ZIZ e Lucas pessoal não devem ser misturados.
- Sem writes externos: somente Brain/local, salvo aprovação explícita futura.

## 13. Guardrails

O cron 23h **pode**:

- ler arquivos do Brain;
- listar crons Hermes;
- ler outputs locais de jobs;
- escrever relatório no Brain;
- atualizar pendências documentais com evidência;
- sugerir ajustes em rotinas;
- reportar gaps.

O cron 23h **não pode**:

- enviar mensagens para clientes/equipe/WhatsApp/e-mail;
- alterar campanhas, Shopify, GMC, Tiny, Meta, Klaviyo, Supabase ou bancos;
- mexer em Docker/VPS/containers/volumes/networks;
- criar/pausar/remover outros crons sem aprovação;
- imprimir ou salvar secrets;
- declarar dado vivo sem consultar fonte real.

## 14. Relação com crons existentes

Hoje já existem crons ativos de relatório, watchdog e entrega. O Fechamento 23h não substitui esses jobs. Ele é a camada de consolidação:

- jobs comerciais continuam fazendo sua função;
- jobs que entregam externamente continuam conforme aprovado;
- jobs silenciosos continuam silenciosos;
- o Fechamento 23h verifica se os artefatos foram salvos e se alguma pendência precisa subir para o Brain.

Exemplo: o Pulso 16h da LK deve continuar enviando para os destinos aprovados e salvando artefatos. O Fechamento 23h só registra que houve execução e se há pendência/risco, sem mandar confirmação operacional desnecessária para Lucas.

## 15. Integração com Mesa COO

A Mesa COO diária deve usar o fechamento 23h como fonte prioritária para:

- decisões pendentes;
- bloqueios;
- riscos;
- próximos passos;
- crons com falha;
- especialistas sem handoff.

Assim a manhã começa com contexto limpo, sem depender de compactação do chat.

## 16. Prompt proposto do cron

```text
Execute o Fechamento Ágil diário do Hermes Brain para Lucas Cimino.

Horário operacional: 23h BRT.
Data operacional: calcule em America/Sao_Paulo. Se a execução UTC cair no dia seguinte, use a data BRT do fechamento.

Objetivo:
Consolidar o que aconteceu nas últimas 24h no Hermes Brain e na estrutura de agentes/crons, sem writes externos e sem ruído desnecessário no Telegram.

Passos:
1. Leia AGENTS.md, MAPA.md e o BRD/routine do Fechamento Ágil.
2. Liste cronjobs ativos/pausados e identifique execuções relevantes das últimas 24h.
3. Leia reports/artefatos recentes em reports/, areas/*, empresa/gestao e memories/.
4. Separe por área: Hermes Central, Lucas/Mordomo, LK, Zipper, SPITI, ZIZ, Operações/Governança.
5. Identifique decisões, pendências, bloqueios, riscos, handoffs de especialistas e gaps.
6. Crie/atualize reports/daily-consolidation/YYYY-MM-DD.md.
7. Se houver pendência factual clara, atualize o arquivo documental correto; se houver dúvida, apenas sugira.
8. Nunca envie mensagem externa, nunca altere produção, nunca mexa em Docker/VPS, nunca salve secrets.
9. Entrega Telegram: só envie resumo curto se houver atenção crítica ou se a configuração aprovada mandar sempre resumir. Caso contrário, finalize silencioso com output local/Brain.

Formato do relatório: use o template do BRD.
```

## 17. Configuração proposta do cron Hermes

Nome:

```text
Hermes Brain Fechamento Ágil 23h
```

Schedule:

```text
0 2 * * *
```

Delivery recomendado:

```text
local
```

Motivo: evitar ruído às 23h. O conteúdo fica no Brain e a Mesa COO da manhã puxa o resumo. Alertas críticos podem ser exceção futura, se implementados no prompt/script.

Toolsets sugeridos:

```text
file, terminal, cronjob, skills, session_search
```

Workdir:

```text
/opt/data/hermes_bruno_ingest/hermes-brain
```

Modelo:

- usar modelo estável atual do Hermes;
- não alterar provider/model sem aprovação separada.

## 18. Critérios de aceite

Lucas aprova este BRD quando estiver confortável com:

1. Horário: **23h BRT**.
2. Cron Brain-first: salva no Brain, não manda relatório longo no Telegram.
3. Estrutura multi-agente: consolida Hermes Central + especialistas.
4. Sem writes externos.
5. Sem criação de agentes novos.
6. Mesa COO da manhã usa o fechamento como insumo.
7. Meta-cron 07h fica como próxima etapa ou etapa 2, não precisa entrar no primeiro cron se Lucas quiser começar simples.

## 19. Faseamento sugerido

### Fase 1 — Aprovação e criação do cron 23h

- Criar cron `Hermes Brain Fechamento Ágil 23h`.
- Rodar uma vez manualmente em modo teste.
- Validar arquivo em `reports/daily-consolidation/`.
- Ajustar ruído/escopo.

### Fase 2 — Meta-cron 07h

- Criar auditoria matinal de crons e handoffs.
- Entregar resumo para Mesa COO/Brain.
- Alertar apenas falhas relevantes.

### Fase 3 — Memory maintenance

- A cada 3 dias, promover aprendizados duráveis para memórias/skills/rotinas.
- Não transformar memória em log.

### Fase 4 — Auditoria mensal dos MAPAs

- Conferir se MAPAs ainda refletem a realidade.
- Arquivar obsoletos.
- Corrigir rotas quebradas.

## 20. Decisão solicitada a Lucas

Aprovar ou ajustar:

1. **Horário:** 23h BRT está correto?
2. **Entrega:** local/Brain apenas, com Telegram só se crítico?
3. **Escopo da Fase 1:** apenas fechamento 23h, deixando meta-cron 07h para depois?
4. **Áreas obrigatórias:** Hermes Central, Lucas/Mordomo, LK, Zipper, SPITI, ZIZ e Operações — incluir mais alguma?

## 21. Status de implementação

Este BRD é uma proposta. Nenhum cron novo deve ser criado até Lucas aprovar explicitamente este pacote.
