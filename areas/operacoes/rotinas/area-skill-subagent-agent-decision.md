# Matriz de decisão — área, skill, rotina, subagent ou agente permanente

## Objetivo

Evitar criação estética de agentes e escolher a menor estrutura suficiente para cada necessidade operacional do Hermes Brain.

Esta rotina adapta as aulas Bruno/OpenClaw sobre cases e multi-agente para o contexto Hermes: primeiro um CoS forte, áreas bem documentadas e skills/rotinas reaproveitáveis; só depois subagentes ou agentes permanentes quando houver volume, risco e autonomia que justifiquem manutenção extra.

## Área dona

Operações / Hermes Geral.

## Quando usar

Use antes de propor:

- novo agente permanente;
- novo canal/grupo/tópico;
- novo cron recorrente;
- nova skill;
- nova área/subárea no Brain;
- separação de runtime por negócio;
- automação com autonomia operacional.

## Regra-mãe

A ordem padrão é:

```text
pergunta/tarefa pontual
→ documento/área existente
→ rotina documentada
→ skill reutilizável
→ subagent pontual
→ cron/automação
→ agente/canal permanente
```

Subir um nível só quando o nível anterior virou gargalo real.

## Critérios de decisão

### 1. Manter como tarefa pontual

Escolha quando:

- aconteceu uma vez;
- não há repetição clara;
- não exige memória operacional nova;
- não exige aprovação/canal/processo próprio.

Exemplo: responder uma pergunta isolada sobre um documento já existente.

### 2. Criar ou atualizar área/documento no Brain

Escolha quando:

- a informação precisa virar fonte de verdade;
- várias pessoas/agentes precisam navegar o contexto;
- há regras por negócio ou processo;
- o conhecimento é durável.

Exemplo: novo subdomínio Zipper, nova rotina SPITI, novo contexto LK.

### 3. Criar rotina documentada

Escolha quando:

- o fluxo se repete;
- há passos claros;
- há critérios de sucesso/falha;
- humanos precisam entender o processo;
- pode virar cron depois, mas ainda não precisa rodar automaticamente.

Exemplo: `material-ingest-to-prd.md`, `brain-improvement-score.md`, `cron-inventory.md`.

### 4. Criar skill

Escolha quando:

- a rotina é executada por Hermes várias vezes;
- há comandos, verificações e pitfalls específicos;
- o custo de relembrar o procedimento é alto;
- repetir manualmente aumenta risco.

Critério prático: se já foi executado 2–3 vezes ou exigiu correção não trivial, virar skill ou patch de skill existente.

### 5. Usar subagent pontual

Escolha quando:

- há pesquisa/análise independente;
- contexto intermediário seria grande demais;
- revisão paralela melhora qualidade;
- não precisa de memória permanente própria.

Exemplo: review isolado de PR, análise de um módulo grande, comparação de alternativas.

Limite: subagent não deve virar “departamento imaginário”. Se o trabalho precisa persistir, ele volta para Brain/rotina/skill.

### 6. Criar cron/automação

Escolha quando:

- há cadência real;
- prompt/job pode ser self-contained;
- o output tem destinatário claro;
- falha é detectável;
- Lucas aprovou a cadência quando houver entrega recorrente.

Toda automação precisa de rotina documentada antes de virar cron.

### 7. Criar agente/canal permanente

Escolha apenas quando houver sinais fortes:

- volume recorrente alto;
- contexto muito isolado;
- risco que exige escopo separado;
- canal próprio com responsáveis claros;
- SLA ou atendimento contínuo;
- benefício maior que custo de manutenção;
- guardrails, permissões e rollback documentados.

Exemplos possíveis no futuro:

- suporte LK se houver volume de atendimento e FAQ consolidado;
- agente SPITI se leilões ativos exigirem rotina diária separada;
- canal Zipper se equipe/colecionadores exigirem interface própria.

Não criar agente permanente só porque “parece organizado”.

## Score rápido de maturidade

Antes de criar agente permanente, pontue de 0 a 2 cada critério:

- Volume recorrente real.
- Risco/escopo isolado.
- Canal próprio necessário.
- Rotina já documentada.
- Skill/procedimento já testado.
- Dados/fonte de verdade claros.
- Aprovações e permissões claras.
- Manutenção semanal justificada.

Interpretação:

- 0–5: manter em área/rotina.
- 6–10: criar skill, subagent pontual ou cron leve.
- 11–16: avaliar agente/canal permanente com PRD.

## Guardrails

- Produção, VPS, Docker, Traefik, volumes, redes, bancos, credenciais, campanhas, WhatsApp/email/posts e contato externo exigem aprovação Lucas.
- Novo agente/canal permanente precisa de PRD leve antes de execução.
- Brain continua fonte de verdade; agente não substitui documentação.
- Doppler continua fonte de secrets; nunca documentar valores.

## Output esperado

```md
# Decisão de arquitetura operacional — [tema]

## Necessidade

## Volume/riscos

## Opções consideradas

- Área/documento:
- Rotina:
- Skill:
- Subagent:
- Cron:
- Agente/canal permanente:

## Decisão

## Por que não subir mais um nível agora

## Aprovações necessárias

## Próximo passo seguro
```

## Como verificar sucesso

- A decisão evita duplicar contexto.
- O caminho escolhido tem dono e arquivo canônico.
- Nenhuma automação/agente/canal permanente foi criado sem PRD e aprovação.
- Se virou rotina/skill, está indexado no Brain.
