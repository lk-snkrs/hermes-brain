# Mem0 canary approval packet

Data: 2026-06-01  
Status: pacote de aprovação; **não executado**.

## Objetivo

Definir exatamente o que seria aprovado caso Lucas queira testar Mem0/provider externo de memória de forma segura, isolada e reversível.

Este arquivo corresponde à **Tarefa 3** do PRD:

`areas/operacoes/prds/hermes-memzero-brain-memory-prd-2026-06-01.md`

## Decisão recomendada

Não ativar em produção agora.

Se Lucas quiser testar, aprovar apenas este escopo:

> “Aprovo criar um profile canário descartável e ativar provider externo de memória apenas nele, usando dataset sintético, sem dados reais, sem gateway produtivo, sem Docker/VPS/Traefik, sem credenciais no Brain e com rollback documentado.”

## Escopo permitido se aprovado

### Permitido

1. Criar ou usar um profile Hermes descartável, por exemplo `memory-canary`.
2. Configurar provider externo de memória somente nesse profile.
3. Usar dataset sintético local.
4. Rodar queries de avaliação em:
   - `reports/governance/mem0_spike-eval-queries-2026-06-01.md`
5. Comparar contra baseline:
   - Brain/context files;
   - `session_search`;
   - built-in memory curta.
6. Salvar resultado local em report.
7. Desligar provider e remover dados do teste ao final, se desejado.

### Bloqueado

- Ativar provider externo no profile default produtivo.
- Ativar em especialistas reais como LK, SPITI, Mordomo, Zipper, Shopify, Growth, Ops ou Trends.
- Enviar conteúdo real do Brain para o provider.
- Enviar conversas reais de Lucas.
- Enviar dados de cliente, pedido, estoque, campanha, fornecedor, financeiro, bancos, infra, tokens, secrets, endpoints sensíveis ou credenciais.
- Alterar Docker/VPS/Traefik/gateway produtivo.
- Mudar cron, webhooks, Telegram bot ou processos runtime produtivos.

## Dados permitidos

Somente dados sintéticos, por exemplo:

- Empresa Alfa;
- Empresa Beta;
- Projeto Atlas;
- Projeto Boreal;
- Usuário Exemplo;
- preferências fictícias;
- decisões fictícias não sensíveis;
- status temporários fictícios para testar expiração/ruído.

## Dados proibidos

- Qualquer segredo ou credencial.
- Dados reais de Lucas/Cimino.
- Dados reais de LK/SPITI/Zipper.
- Pedidos, estoque, clientes, suppliers, campanhas, contas, bancos, tokens, logs, IPs, URLs privadas ou connection strings.
- Conteúdo bruto de `MEMORY.md`, `USER.md`, daily, hot, reports ou session transcripts reais.

## Pré-requisitos antes de executar

1. Confirmar comando/config oficial de Hermes para memory provider no runtime atual.
2. Confirmar que o profile canário não herda gateway/API/webhook produtivos.
3. Confirmar que dataset é sintético.
4. Confirmar forma de deleção/export/rollback do provider.
5. Confirmar que nenhuma chave/provider secret será impressa em logs ou reports.

## Comandos propostos — rascunho, não executar sem aprovação

> Os comandos abaixo são placeholders operacionais e devem ser validados contra a versão atual do Hermes antes de execução. Não executar automaticamente.

```bash
# 1. Criar profile canário descartável, se aprovado
hermes profile create memory-canary

# 2. Ver config do profile sem imprimir secrets
HERMES_HOME=/opt/data/profiles/memory-canary hermes config path
HERMES_HOME=/opt/data/profiles/memory-canary hermes memory status

# 3. Configurar provider externo apenas no canário
# Comando exato depende da versão atual e deve ser confirmado via docs/CLI:
HERMES_HOME=/opt/data/profiles/memory-canary hermes memory setup

# 4. Rodar sessão de teste com dataset sintético
HERMES_HOME=/opt/data/profiles/memory-canary hermes chat -q "Use apenas o dataset sintético autorizado para o spike de memória e responda às queries de avaliação."

# 5. Desligar provider ao final, se decidido
HERMES_HOME=/opt/data/profiles/memory-canary hermes memory off
```

## Plano de rollback

1. Desligar provider no profile canário:

```bash
HERMES_HOME=/opt/data/profiles/memory-canary hermes memory off
```

2. Remover dados do provider usando ferramenta/API oficial do provider, sem imprimir tokens.
3. Arquivar report de resultado.
4. Opcionalmente exportar e deletar profile canário:

```bash
hermes profile export memory-canary
hermes profile delete memory-canary
```

5. Verificar que nenhum profile real foi alterado.

## Métricas de sucesso

- 90%+ de acerto em preferências/decisões duráveis sintéticas.
- 0 falhas em `SECRET_BLOCK`.
- 0 casos de status temporário tratado como atual.
- 0 contaminação entre domínios sintéticos.
- Latência aceitável.
- Deleção/rollback confirmados.
- Benefício demonstrável sobre Brain + `session_search`.

## Métricas de falha

Encerrar e não avançar se:

- o provider exige ingestão ampla de dados reais;
- não há deleção clara;
- não há isolamento por profile;
- recall traz ruído antigo como verdade atual;
- vaza domínio sintético entre contextos;
- exige alteração runtime produtiva para testar;
- custo/latência são incertos ou altos.

## Resultado esperado do canário

Um report final em:

`reports/governance/mem0_spike-result-YYYY-MM-DD.md`

com decisão:

- `não usar`;
- `manter só canário`;
- `testar em profile real de baixo risco`;
- `avaliar outro provider`;
- `abandonar provider externo por enquanto`.

## Status atual

Pacote pronto para aprovação futura. Nenhuma configuração, provider, runtime, gateway, Docker, VPS, cron ou dado real foi alterado.
