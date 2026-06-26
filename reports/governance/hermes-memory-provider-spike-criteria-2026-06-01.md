# Spike futuro — provider externo de memória Hermes

Data: 2026-06-01

## Decisão atual

Não ativar provider externo agora. A arquitetura correta primeiro é:

1. memória built-in/injetada como boot mínimo;
2. Brain como memória rica curada;
3. skills para procedimentos;
4. daily/hot/reports/session_search para histórico e estado;
5. só depois avaliar provider externo.

Config atual verificada anteriormente: `memory.provider` vazio, usando built-in memory.

## Providers candidatos

- Honcho
- Mem0
- Hindsight
- Supermemory
- outro backend compatível com Hermes, se surgir opção melhor

## Critérios de avaliação

### Privacidade e segurança

- O provider recebe dados sensíveis? Quais?
- Permite escopo por profile?
- Permite exclusão/expiração?
- Dá para desativar e exportar dados?
- Existe risco de vazar LK/SPITI/Zipper/infra no mesmo espaço vetorial?

### Qualidade de recall

- Recupera fatos úteis sem trazer ruído antigo?
- Distingue preferência durável de status temporário?
- Respeita isolamento entre profiles?
- Ajuda mais do que `session_search` + Brain?

### Governança

- Existe trilha de auditoria?
- Dá para ver por que uma memória foi recuperada?
- Dá para bloquear tipos de conteúdo: secrets, credenciais, PIDs, cron IDs, status volátil?

### Operação

- Custo previsível?
- Latência aceitável?
- Rollback simples?
- Não depende de restart amplo/Docker/VPS sem plano?

## Desenho de teste recomendado

Fazer um piloto isolado, não no profile default produtivo:

1. criar/usar profile descartável;
2. habilitar provider apenas nele;
3. injetar dataset sintético sem dados reais sensíveis;
4. testar recall de preferências duráveis vs ruído histórico;
5. testar isolamento e deleção;
6. registrar resultado em relatório;
7. só então decidir se vale para algum profile real.

## Guardrail

Provider externo não substitui Brain. Ele pode ser uma camada de recall semântico, mas a verdade operacional canônica continua em Brain/skills/context files/reports.

## Status

Backlog futuro. Nenhuma configuração alterada.
