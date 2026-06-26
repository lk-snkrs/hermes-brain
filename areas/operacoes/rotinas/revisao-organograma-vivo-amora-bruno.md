# Rotina — revisão do organograma vivo estilo Amora/Bruno

Data: 2026-05-30
Owner: Hermes Geral / Governança Brain
Status: rotina documental; não é cron ativo.

## Objetivo

Manter o organograma vivo como Bruno/Amora: claro o suficiente para qualquer agente saber quem é, quem chama quem, onde vive, quais permissões tem, como registra handoff e quando fica em silêncio.

## Cadência recomendada

- Revisão leve: mensal ou após mudança relevante de runtime/profile/bot/cron.
- Revisão imediata: quando Lucas apontar agente fora do ar, rota errada, approval loop, ruído de Telegram, output sem handoff ou confusão de dono lógico.

## Checklist de revisão

### 1. Agentes e identities

Para cada agente/frente principal, verificar se existem e continuam atuais:

- `SOUL.md`
- `IDENTITY.md`
- `USER.md`
- `AGENTS.md`
- `MAPA.md`
- `HEARTBEAT.md`
- `TOOLS.md`
- `MEMORY.md`

### 2. Runtime truth

Verificar, sem mexer em Docker/produção:

- profile esperado;
- bot/canal esperado;
- estado do watchdog global;
- se Main continua check-only;
- se profiles prepared/read-only continuam fora de auto-start.

### 3. Dono lógico vs runtime atual

Para cada rotina material, classificar:

- dono lógico;
- runtime atual;
- cron registry atual;
- destino ideal;
- se migração é necessária ou apenas estética.

### 4. Handoff e receipts

Checar se outputs materiais foram registrados quando houve:

- decisão durável;
- preview/approval packet;
- write externo;
- bloqueio/risco;
- alteração de runtime/cron/docs de governança;
- aprendizado que virou skill/rotina.

### 5. Silent-OK

Confirmar que Telegram recebe apenas:

- decisão;
- exceção;
- falha acionável;
- alerta com ação necessária;
- relatório que Lucas explicitamente quer ali.

Não mandar sucesso saudável, wrapper técnico, job id cru, JSON, prompt interno ou ruído de watchdog.

## Outputs da revisão

Toda revisão deve produzir, no mínimo:

1. relatório em `reports/governance/`;
2. handoff em `empresa/contexto/handoffs/`;
3. atualização dos docs canônicos se houver drift;
4. Brain health check;
5. secret scan focado nos arquivos alterados.

## Métrica de maturidade

- 10/10 documentação: qualquer agente entende escopo, fonte, runtime, boundary e handoff.
- 10/10 operação: o pedido vai para o executor certo, gera preview/ação segura, registra receipt/handoff e vira skill/rotina quando repetível.

## Não fazer sem aprovação

- criar novo cron;
- migrar cron;
- reiniciar gateway/profile fora de escopo aprovado;
- criar bot/runtime;
- tocar Docker/VPS/Traefik/produção;
- executar write externo.
