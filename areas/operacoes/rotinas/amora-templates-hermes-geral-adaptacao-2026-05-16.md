# Ingestão dos templates Amora — adaptação Hermes/Lucas

Data: 2026-05-16

Fonte: DOCX enviados por Lucas no Telegram:

- `LEIA PRIMEIRO`
- `IDENTITY-amora.md`
- `SOUL-amora.md`
- `USER-amora.md`
- `AGENTS-amora.md`
- `MAPA-amora.md`
- `HEARTBEAT-amora.md`

Markdown extraído em: `reports/amora-reference-ingest-2026-05-16/`.

## Decisão

A Amora é referência de profundidade, não template para copiar.

A adaptação correta para Lucas é Hermes-native:

- Hermes Brain como Grande Mente / COO central.
- Lucas, empresas e áreas abaixo da Grande Mente.
- Um Hermes Geral forte antes de criar agentes permanentes demais.
- Skills, rotinas e cronjobs só quando há repetição/valor real.
- Aprovação forte para qualquer ação externa, produção, infra, dinheiro ou contato humano.

## O que foi incorporado

### 1. Identidade factual

Criado: `agentes/hermes-geral/IDENTITY.md`.

Adaptação:

- Amora usa identidade curta com nome, versão, modelo, owner e territories.
- Hermes agora tem identidade equivalente: `Hermes Geral`, `Grande Mente / Chief of Staff`, `Agent ID hermes-geral`, reportando para Lucas e atuando sobre LK, Zipper, SPITI, Lucas pessoal, Operações, Tecnologia e Governança.

### 2. Alma / comportamento

Atualizado: `agentes/hermes-geral/SOUL.md`.

Incorporado:

- “não é chatbot genérico”; é Chief of Staff/Grande Mente.
- pedido real > pedido literal;
- certeza calibrada;
- discordar antes de construir errado;
- simplicidade primeiro;
- tudo que importa vira registro;
- tom direto, sem aberturas/fechos corporativos.

Adaptação Hermes:

- remove referências privadas de Bruno/Pixel;
- substitui OpenClaw por Hermes-native;
- preserva diferenciais Hermes: ferramentas reais, Doppler, Brain versionado, session_search, crons e aprovações.

### 3. Regras operacionais

Atualizado: `agentes/hermes-geral/AGENTS.md`.

Incorporado:

- boot sequence;
- autonomia vs aprovação;
- red lines;
- external vs internal;
- regra “mental note não existe”.

Regra aprovada por Lucas formalizada:

- 1 vez: executar normal.
- 2 vezes na mesma semana ou mesmo formato: documentar padrão.
- 3 vezes ou impacto alto: criar/atualizar skill ou rotina.
- Se envolve aprovação externa: skill precisa ter aprovação, preview, guardrails, rollback e verificação.

### 4. Heartbeat / proatividade

Atualizado: `agentes/hermes-geral/HEARTBEAT.md`.

Decisão:

- não ativar cron automático ainda;
- primeiro documentar rotina e rodar sob demanda;
- se provar valor, propor cron com agenda, destino, silêncio, erro e kill criteria.

Checks candidatos definidos:

- Hermes runtime / Telegram / cron;
- Brain e Mission Control;
- LK OS;
- Zipper / SPITI.

### 5. Navegação do workspace

Criado: `MAPA.md` na raiz do Brain.

Por quê:

- o Brain tinha `START-HERE.md`, `README.md`, `empresa/MAPA.md` e `areas/MAPA.md`, mas não tinha um `MAPA.md` raiz no padrão Amora.
- O novo arquivo dá navegação rápida sem substituir o `START-HERE.md`.

## O que foi rejeitado ou adiado

### Cron automático estilo Amora

Rejeitado por enquanto.

Motivo: Lucas aprovou documentar e rodar sob demanda primeiro; cron só depois de provar valor.

### Copiar territórios/canais da Amora

Rejeitado.

Motivo: os canais e contexto são do Bruno. Hermes usa Telegram Lucas, Brain, LK, Zipper, SPITI e infra própria.

### Criar vários agentes permanentes agora

Adiado.

Motivo: decisão já consolidada no Brain: um CoS forte + skills/rotinas antes de sprawl multiagente.

## Comparação rápida com o estado anterior

Antes:

- `agentes/hermes-geral/SOUL.md` era bom, mas curto.
- `AGENTS.md` tinha regras essenciais, mas sem thresholds de repetição.
- `HEARTBEAT.md` era genérico.
- Não havia `IDENTITY.md` do Hermes Geral.
- Não havia `MAPA.md` raiz.

Depois:

- identidade completa do Hermes Geral;
- comportamento mais maduro e coerente com a Amora;
- regra repetição → skill formalizada;
- heartbeat com anti-spam e sem cron prematuro;
- mapa raiz para navegação da Grande Mente;
- fontes DOCX preservadas como markdown limpo em `reports/`.

## Guardrails preservados

- Nenhum segredo extraído ou versionado.
- Nenhuma ação externa executada.
- Nenhum cron criado.
- Nenhum deploy/restart/Docker/produção alterado.
- Nenhuma mensagem para cliente/fornecedor/parceiro enviada.

## Próximo passo recomendado

Rodar a primeira revisão sob demanda usando a nova identidade:

1. Hermes/Infra: runtime, cron, Brain, Mission Control.
2. LK: LK OS, GMC, sourcing, CRM, reports obrigatórios.
3. Zipper: pendências comerciais/logística/ARPA/CRM.
4. SPITI: Hub, leilão, dados e pendências.

Se a revisão gerar valor por 1–2 ciclos, propor cron com critérios explícitos.
