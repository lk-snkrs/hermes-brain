# Bruno/OpenClaw — Segundo Cérebro, memória e consolidação diária por crons

Data: 2026-05-19
Status: síntese corrigida para Hermes Brain
Foco: documentação do segundo cérebro e como agentes cuidam da consolidação diária do que foi feito

## Fontes consultadas

- `BRUNO-ATUAL/.../Aula-6-Organizando workspace do seu agente/Workspace + mapas.html`
- `BRUNO-ATUAL/.../Aula-7-boas práticas para memória dos agentes/Memória + contexto.html`
- `BRUNO-ATUAL/.../Aula-9-Autonomia dos agentes e heartbeats/Crons+Heartbeats.html`
- `BRUNO-ATUAL/.../Referências para seu agente/memoria-do-seu-agente.md.docx`
- `BRUNO-ATUAL/.../Referências para seu agente/crons-do-seu-agente.md.docx`
- `BRUNO-ATUAL/.../Exemplos da Amora/HEARTBEAT-amora.md.docx`

## Correção de foco

A tese principal aqui não é organograma de agentes.

A tese é:

> O segundo cérebro é um workspace versionável, documentado por MAPAs, alimentado por memória diária e consolidado por crons/heartbeats. O agente não apenas responde no chat: ele escreve, organiza, revisa e fecha o dia.

No Bruno/OpenClaw, o agente vira operação quando passa a cuidar do próprio ambiente:

1. registra atividades relevantes em `memory/YYYY-MM-DD.md`;
2. mantém `memory/hot.md` com o contexto quente;
3. consulta `MEMORY.md`, dailies recentes e MAPAs no boot;
4. usa memória semântica para buscar histórico por significado;
5. roda crons para revisão, auditoria e relatórios;
6. usa heartbeat para checks pequenos e silenciosos ao longo do dia;
7. entrega a consolidação no canal certo, normalmente Telegram/tópico Operação.

## 1. Estrutura do segundo cérebro

Aula 6 define o workspace como a estante do agente. A organização não é decoração: é o que permite escala.

Estrutura canônica Bruno/OpenClaw:

```text
workspace/
├── SOUL.md
├── IDENTITY.md
├── AGENTS.md
├── USER.md
├── MEMORY.md
├── HEARTBEAT.md
├── MAPA.md
├── content/
│   └── MAPA.md
├── memory/
│   ├── MAPA.md
│   ├── hot.md
│   ├── YYYY-MM-DD.md
│   ├── context/
│   └── projects/
├── skills/
│   └── MAPA.md
└── archive/
    └── MAPA.md
```

Papel das pastas:

- `content/`: coisas que o agente cria — posts, drafts, materiais, briefings.
- `memory/`: coisas que o agente precisa lembrar — decisões, pendências, contexto, daily notes.
- `skills/`: capacidades modulares reutilizáveis.
- `archive/`: coisas encerradas/obsoletas, preservadas para histórico.

Regra crítica: `memory/` é território do agente. O humano pode pedir salvamento, mas quem mantém a higiene operacional é o agente.

## 2. MAPAs distribuídos

O Bruno evita um arquivo central gigante. Cada pasta documenta a si mesma com um `MAPA.md` local.

Motivo:

- um mapa monolítico cresce, fica desatualizado e vira mentira oficial;
- o agente carrega contexto demais sem necessidade;
- cada domínio perde autonomia de manutenção.

Com MAPAs distribuídos:

- `MAPA.md` raiz explica a navegação geral;
- `memory/MAPA.md` explica só a memória;
- `content/MAPA.md` explica só conteúdo;
- `skills/MAPA.md` explica só skills;
- `archive/MAPA.md` explica só histórico.

Frase operacional do material: sem MAPA, o agente improvisa e vira bagunça em uma semana.

## 3. Memória do agente: três camadas + hot

Aula 7 separa a memória em três sistemas:

1. **Memória padrão / boot**
   - lê `MEMORY.md`;
   - lê `memory/hot.md`;
   - lê dailies de hoje e ontem — janela prática de 48h;
   - lê SOUL/IDENTITY/USER/AGENTS;
   - carrega MAPAs do workspace.

2. **Memória de sessão**
   - conversa atual no Telegram/Gateway;
   - útil, mas perecível;
   - satura, alucina ou perde contexto se não houver higiene.

3. **Memória semântica**
   - busca no workspace por significado, não apenas palavra exata;
   - permite perguntar por decisões antigas e recuperar arquivos relevantes.

Peça adicional central:

- `memory/hot.md`: snapshot do agora.
  - prioridades da semana;
  - negociações ativas;
  - decisões recentes;
  - métricas críticas;
  - prazos por data;
  - bloqueios que não podem sumir.

## 4. Daily notes: onde o dia é capturado

No padrão Bruno/OpenClaw, toda atividade significativa do dia vai para:

```text
memory/YYYY-MM-DD.md
```

O que entra:

- decisões;
- calls;
- pendências;
- contexto novo;
- resultados de tarefas executadas;
- promessas feitas;
- próximos passos.

Quando o agente escreve:

- ao longo da conversa;
- quando o humano pede “salva isso importante”;
- no fechamento do dia;
- antes/depois de compactação quando o sistema faz Memory Flush.

Formato recomendado:

```md
## 2026-05-19

- 09:30 — Decisão: ...
- 11:10 — Call: ...
- 14:20 — Execução: ...
- 16:45 — Pendente: ...
- 18:00 — Consolidação: ...
```

Princípio: não é transcrição de chat. É essência operacional.

## 5. Memory Flush não substitui consolidação deliberada

O material fala do “silent memory flush” antes da compactação automática. Ele tenta salvar contexto antes de comprimir, mas a confiabilidade real estimada pelo Bruno é cerca de 70%.

Implicação operacional:

- para contexto importante, não confiar só no flush;
- salvar manualmente quando for decisão durável;
- usar cron de fechamento do dia para consolidar;
- usar heartbeat/maintenance para destilar aprendizados duráveis para `MEMORY.md`.

Prompt-base de salvamento direcionado:

```text
salva isso importante: [DECISÃO / CONTEXTO]

Salva tanto na daily note de hoje quanto no lugar estruturado que faz sentido
(ex: pasta do projeto, context/decisoes/, ou context/people/{nome}.md).
Me mostra onde você salvou.
```

Regra: se vou perguntar isso de novo, salva.

## 6. Crons: de assistente para operação

Aula 9 define cron como o mecanismo que transforma agente em operação.

Frase central:

> cron = onde você dá super poderes ao agente. Sem cron, ele é assistente. Com cron, ele é operação.

Diferença entre cron e heartbeat:

- **Cron**: horário exato, tarefa isolada, output entregue direto no canal. Ex.: revisão diária às 18h.
- **Heartbeat**: check periódico com tolerância de tempo, múltiplas verificações pequenas, agente decide se fala ou fica quieto.

Categorias de cron:

1. monitoramento — health check, auditoria de workspace, auditoria de crons;
2. pesquisa/estudo — tendências, docs novas, padrões de memória;
3. sumarização/relatórios — vendas, KPIs, tickets, newsletter;
4. planejamento/reflexão — revisão do dia, pendências, preparação de amanhã.

## 7. Cron-âncora: Revisão do Dia

A Revisão do Dia é a peça exata que Lucas pediu: o agente consolida o que foi feito durante o dia.

No material Bruno/OpenClaw, ela roda no fim da tarde, normalmente 18h, e entrega no Telegram/tópico Operação.

Fluxo:

```text
18h cron dispara
  ↓
Lê memory/YYYY-MM-DD.md
  ↓
Cruza com memória semântica e pendências
  ↓
Lista o que foi feito
  ↓
Lista o que ficou aberto/prometido
  ↓
Lê agenda/prazos do dia seguinte
  ↓
Entrega resumo no Telegram
  ↓
Atualiza hot.md se necessário
```

Output típico:

```md
Hoje fiz:
- ...
- ...

Aberto:
- ...
- ...

Amanhã:
- ...
- ...

Riscos/bloqueios:
- ...
```

Prompt original adaptado:

```text
cria um cron todo dia 18h chamado revisao-do-dia que:
1. lê minha daily note do dia (memory/YYYY-MM-DD.md) e cruza com memória semântica;
2. lista o que ficou pendente, cruzando decisões do dia com pendencias.md;
3. alerta sobre amanhã lendo calls, deadlines e prazos do dia seguinte;
4. manda resumo no Telegram tópico Operação no formato:
   - Hoje fiz: ...
   - Aberto: ...
   - Amanhã: ...
5. roda em sessão isolada.
```

## 8. Meta-cron: auditoria dos próprios crons

Bruno reforça que cron também quebra. Então existe um supervisor: o meta-cron.

Fluxo:

```text
07h cron de auditoria dispara
  ↓
Lista crons que rodaram nas últimas 24h
  ↓
Classifica OK / falhou / silencioso esperado
  ↓
Inclui erro quando houver
  ↓
Entrega resumo no Telegram/tópico Operação
```

Prompt-base:

```text
cria um cron toda manhã 7h que checa todos os crons que rodaram nas últimas 24h,
lista os que deram OK e os que falharam, e me manda resumo no Telegram tópico Operação.
Se algum falhou, inclui o erro pra eu poder corrigir.
Roda em sessão isolada e usa contexto leve.
```

Princípio: você não confia 100% em cron; você confia em cron que audita cron.

## 9. Heartbeat: agente que respira

Heartbeat não é relatório agendado. É batida periódica.

No exemplo da Amora:

- poll a cada 30 minutos;
- janela ativa 08h–22h;
- quiet hours 22h–08h;
- sorteia 2–4 checks por heartbeat para evitar ruído;
- fica em silêncio se não houver algo relevante.

Arquivos centrais:

- `HEARTBEAT.md`: como vigia — frequência, checks, silêncio, regras de interrupção;
- `memory/hot.md`: o que vigia — prioridades, prazos, negociações, decisões recentes.

Checks típicos:

- inbox triage;
- pendências paradas;
- mention sweep;
- memory maintenance;
- calendário próximo;
- weather/news guard.

Para o segundo cérebro, o check mais importante é:

```text
Memory maintenance — a cada 3 dias, lê memory/YYYY-MM-DD.md recentes e destila aprendizados duráveis para MEMORY.md.
```

## 10. Adaptação Hermes-native

No Hermes Brain, o equivalente correto é:

```text
Hermes Brain
├── MAPA.md                         # navegação da Grande Mente
├── HEARTBEAT.md                    # regras globais de proatividade
├── memories/                       # memória executiva durável
├── reports/                        # evidências e relatórios
├── empresa/gestao/pendencias.md    # pendências cross-empresa
├── empresa/decisoes/               # decisões permanentes
├── areas/<empresa>/MAPA.md         # mapas distribuídos por OS
├── areas/<empresa>/rotinas/        # rotinas documentadas
└── areas/operacoes/rotinas/        # crons, health checks, brain sync
```

A adaptação não deve copiar literalmente `memory/YYYY-MM-DD.md` se o Brain já usa `reports/`, `memories/`, `empresa/` e `areas/`. Mas precisa preservar o mesmo ciclo:

```text
execução do dia
  ↓
receipt / daily note / report curto
  ↓
consolidação diária por cron
  ↓
pendências e decisões atualizadas
  ↓
hot/current atualizado
  ↓
mapa/índice atualizado se nasceu artefato novo
  ↓
meta-cron audita se a rotina rodou
```

## 11. Rotina mínima recomendada para o Grupo Cimino

### 07h — Auditoria dos crons e agentes

Objetivo: saber se a operação automática está viva.

Entradas:

- lista de cronjobs Hermes;
- últimas execuções;
- erros;
- entregas esperadas no Telegram/Brain;
- handoffs de especialistas.

Saída:

```md
## Auditoria 24h

Crons OK:
- ...

Falhas:
- ...

Especialistas sem handoff:
- ...

Ações recomendadas:
- ...
```

### 18h — Consolidação do dia / Mesa COO EOD

Objetivo: fechar o dia e preparar amanhã.

Entradas:

- outputs do dia no Hermes principal;
- receipts de especialistas LK/Zipper/SPITI/Mordomo;
- reports criados;
- pendências e decisões;
- agenda/prazos de amanhã.

Saída:

```md
## Fechamento do dia — YYYY-MM-DD

Hoje foi feito:
- ...

Decisões tomadas:
- ...

Pendente / bloqueado:
- ...

Especialistas:
- LK Growth: ...
- Mordomo: ...
- SPITI: ...
- Zipper: ...

Amanhã:
- ...

Salvar no Brain:
- arquivos criados/atualizados: ...
- pendências atualizadas: ...
- decisões promovidas: ...
```

### A cada 3 dias — Memory maintenance

Objetivo: tirar aprendizados duráveis das dailies/receipts e promover para memória estável.

Saída:

- atualizar `memories/*.md` quando for durável;
- atualizar `memory/hot` equivalente quando for contexto quente;
- arquivar/limpar pendências encerradas;
- não salvar segredos, tokens, logs crus ou ruído de sessão.

### Mensal — Auditoria de MAPAs

Objetivo: evitar que o segundo cérebro vire bagunça.

Checklist:

- toda pasta importante tem `MAPA.md`;
- MAPAs apontam para arquivos reais;
- arquivos novos estão indexados no mapa certo;
- rotinas com cron real têm `.md` correspondente;
- crons órfãos são removidos ou documentados;
- áreas especialistas têm local de receipt/handoff.

## 12. Decisão para o Hermes

Aplicar o padrão Bruno/OpenClaw nesta ordem:

1. **Documentação do segundo cérebro**: Brain como workspace vivo, com mapas distribuídos.
2. **Daily/receipt por execução relevante**: nada importante fica só em chat.
3. **Cron de fechamento do dia**: consolida o que foi feito e prepara amanhã.
4. **Meta-cron de auditoria**: verifica se os próprios crons e especialistas cumpriram handoff.
5. **Heartbeat com silêncio**: vigia hot/current e só interrompe quando há algo relevante.
6. **Memory maintenance**: promove aprendizados duráveis e limpa contexto quente.

Não é “mais agente”. É **mais cérebro bem mantido**.

## 13. Próximo PRD sugerido

Criar o PRD `hermes-brain-daily-consolidation-crons` com três entregas:

1. inventário vivo de crons/agentes/profiles e seus destinos de output;
2. rotina Hermes de fechamento diário 18h, com entrega Telegram + arquivo Brain;
3. meta-cron 07h para auditar crons, handoffs e falhas das últimas 24h.

Guardrails:

- sem credenciais em memória;
- sem writes externos fora do Brain/Telegram de reporte;
- todo cron real precisa de rotina documentada;
- outputs devem ser curtos, acionáveis e linkar fontes/artefatos;
- falha de cron precisa aparecer no dia seguinte, não virar silêncio operacional.
