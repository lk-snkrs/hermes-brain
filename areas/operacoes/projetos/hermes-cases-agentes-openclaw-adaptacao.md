# Adaptação dos cases OpenClaw para Hermes — Lucas Cimino

> Pedido do Lucas: ignorar Paperclip; adaptar os cases para Hermes.
> Fonte: ZIP recebido em 2026-05-05 com `LEIA PRIMEIRO` e 5 cases de agentes.

## Decisão principal

Não vamos usar Paperclip como camada operacional neste plano. A adaptação será Hermes-native:

- Hermes Telegram como interface principal do Lucas.
- Hermes Brain como fonte de verdade durável.
- Skills Hermes para processos repetíveis.
- Cronjobs Hermes para rotinas leves e auditáveis.
- `delegate_task`/subagentes para tarefas paralelas pontuais.
- Perfis/processos Hermes separados apenas quando houver volume e motivo real.

## Leitura do LEIA PRIMEIRO

O próprio material recomenda não copiar tudo. A regra é:

1. Ler o case mais próximo.
2. Identificar uma ideia replicável.
3. Adaptar ao contexto real.

Para Lucas, o contexto real é multiempresa: LK Sneakers, Zipper Galeria e SPITI Auction, com dados/credenciais separados e aprovações fortes para ações externas.

## Arquétipos relevantes

### Amora — 1 Chief of Staff forte

Aplicação Hermes:

- Fortalecer o Hermes atual como `Lucas Chief of Staff`.
- Ele coordena múltiplas frentes sem criar agentes permanentes desnecessários.
- Tarefa repetida vira skill.
- Rotina recorrente vira cron documentado.

Implementar agora:

- Skill/rotina de revisão diária ou semanal multiempresa.
- Skill de triagem de pendências.
- Skill de transformar pedido do Lucas em plano/backlog.

Evitar agora:

- dezenas de crons;
- múltiplos agentes permanentes;
- automações externas agressivas.

### Filippe César — CoS multiempresa com isolamento

Aplicação Hermes:

- Hermes Geral coordena LK, Zipper e SPITI.
- Cada empresa fica separada em `areas/lk`, `areas/zipper`, `areas/spiti`.
- Nenhum fluxo mistura credenciais, bancos ou contexto sem confirmação.

Implementar agora:

- Comando/skill de roteamento: identificar se a tarefa é LK, Zipper, SPITI ou global.
- Checklist de isolamento antes de acessar dados.
- Relatório consolidado periódico para Lucas.

### Aurora — dor real primeiro

Aplicação Hermes:

- Priorizar skills específicas que removem trabalho operacional real.
- Não começar por organograma bonito.

Candidatos imediatos:

- LK: briefing CRM/campanha aprovada, leads esfriando, cross-sell.
- Zipper: abordagem de colecionador, briefing de obra/artista, planejamento de feira.
- SPITI: verificação de lances, divergência de dados, briefing de lote/leilão, revisão Spiti Hub.

### Igor Gouveia — multiagente especializado

Aplicação Hermes futura:

- Usar `delegate_task` para subagentes pontuais agora.
- Considerar perfis/processos Hermes separados só depois de volume real.

Possíveis especializações futuras:

- Hermes LK Growth/CRM.
- Hermes Zipper Curatorial/Comercial.
- Hermes SPITI Produto/Leilão.
- Hermes Técnico para GitHub/infra.

Critério para separar:

- escopo recorrente;
- volume semanal;
- risco/credencial específico;
- necessidade de memória/rotina própria.

### Chris Everest — outbound/prova de valor

Aplicação Hermes futura, com aprovação humana:

- Gerar dossiês personalizados para consignadores/coletadores.
- Gerar rascunhos de abordagem e prova de valor.
- Nunca enviar automaticamente.

## Implementação Hermes em fases

### Fase 1 — agora

1. Manter Hermes atual como Chief of Staff geral.
2. Criar skills Hermes para os processos mais repetitivos.
3. Criar uma rotina leve de revisão semanal multiempresa.
4. Usar subagentes apenas via `delegate_task` para tarefas pontuais.
5. Documentar tudo no Hermes Brain.

### Fase 2 — após uso real

1. Medir quais pedidos se repetem.
2. Transformar workflows recorrentes em skills.
3. Criar crons com documentos de rotina.
4. Padronizar templates por empresa.

### Fase 3 — só se necessário

1. Criar perfis/processos Hermes separados por empresa ou domínio.
2. Adicionar gateway/canais específicos.
3. Configurar modelos por função: modelo forte no CoS, modelo mais barato em tarefas repetitivas.

## Ações executadas nesta rodada

1. Skill Hermes criada: `lucas-chief-of-staff`.
2. Skill Hermes criada: `multiempresa-routing-lucas`.
3. Rotina documental criada: `areas/operacoes/rotinas/revisao-semanal-multiempresa.md`.
4. Índice de rotinas atualizado: `empresa/rotinas/_index.md`.

## Próximas ações recomendadas

1. Escolher 1 dor real por empresa para virar skill operacional.
2. Rodar manualmente uma primeira revisão semanal multiempresa para validar o formato.
3. Só depois avaliar cron agendado, se Lucas aprovar dia/horário/canal.

## Guardrails

- Ações externas sempre com aprovação do Lucas.
- Nada de WhatsApp/email/campanha/post/deploy/merge/migração sem aprovação.
- Segredos sempre no Doppler; nunca em docs/chat.
- SPITI: silêncio é melhor que dado errado.
- VPS/Docker/infra: read-only por padrão.
