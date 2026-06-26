# PRD — Hermes Brain Daily Consolidation Crons

Data: 2026-05-19
Status: proposto
Origem: correção Lucas sobre Bruno/OpenClaw — foco em segundo cérebro e consolidação diária via crons

## Problema

O Hermes já tem memória, rotinas, relatórios e vários crons, mas ainda falta formalizar o equivalente Bruno/OpenClaw da **Revisão do Dia**:

- fechar o que foi feito durante o dia;
- promover decisões e pendências para o Brain;
- detectar especialistas que executaram sem handoff;
- preparar amanhã;
- auditar se os próprios crons rodaram.

Sem isso, parte do trabalho fica dispersa entre Telegram, profiles, outputs de cron, reports e memória de sessão.

## Inspiração Bruno/OpenClaw

Aula 6:
- segundo cérebro = workspace com MAPAs distribuídos;
- `memory/` é território do agente;
- cada pasta documenta a si mesma.

Aula 7:
- dailies em `memory/YYYY-MM-DD.md`;
- boot lê `MEMORY.md`, `hot.md`, dailies 48h e MAPAs;
- Memory Flush não é 100% confiável;
- decisões duráveis devem ser salvas explicitamente.

Aula 9:
- cron transforma assistente em operação;
- Revisão do Dia fecha o dia às 18h;
- meta-cron às 7h audita os crons;
- heartbeat vigia contexto quente e fica em silêncio quando não há novidade.

## Objetivo

Implementar no Hermes Brain um ciclo diário:

```text
07h — Auditoria de crons e handoffs
18h — Fechamento do dia / consolidação Brain
A cada 3 dias — manutenção de memória
Mensal — auditoria de MAPAs e rotinas
```

## Não-objetivos

- Não enviar mensagens externas para clientes.
- Não executar ações produtivas em Shopify, GMC, WhatsApp, e-mail, ads, banco ou VPS.
- Não criar novos agentes paralelos.
- Não salvar segredos, tokens, connection strings ou logs crus.
- Não misturar todos os outputs em um arquivo gigante.

## Entregável 1 — Inventário vivo de crons/agentes

Criar arquivo:

```text
areas/operacoes/inventarios/crons-agentes-profiles.md
```

Conteúdo mínimo:

```md
# Inventário — crons, agentes e profiles

Atualizado em: YYYY-MM-DD

## Crons ativos
- Nome:
  - ID:
  - schedule:
  - destino:
  - escopo:
  - último status:
  - rotina/documentação:

## Crons pausados
- ...

## Profiles/bots especialistas
- Nome:
  - Canal/profile:
  - Escopo:
  - Local de handoff:
  - Autonomia:
  - Último handoff conhecido:

## Gaps
- ...
```

## Entregável 2 — Cron 07h: auditoria dos crons e especialistas

Nome sugerido:

```text
Hermes Brain cron audit 07h
```

Schedule:

```text
0 10 * * *   # 07h BRT em UTC-3
```

Prompt conceitual:

```text
Execute auditoria operacional das últimas 24h.

1. Liste cronjobs Hermes ativos/pausados e últimas execuções relevantes.
2. Identifique falhas, atrasos, jobs silenciosos indevidos ou jobs sem documentação.
3. Verifique se profiles/bots especialistas com atividade esperada tiveram handoff no Brain.
4. Produza resumo curto para Lucas no Telegram:
   - OK
   - falhas
   - sem handoff
   - ações sugeridas
5. Se encontrar documentação faltante, proponha arquivo/rotina, mas não escreva em produção externa.
```

Saída esperada:

```md
## Auditoria 24h — Hermes

OK:
- ...

Falhas/atenção:
- ...

Sem handoff:
- ...

Ações sugeridas:
- ...
```

## Entregável 3 — Cron 18h: Fechamento do Dia / Brain Consolidation

Nome sugerido:

```text
Hermes Brain EOD consolidation 18h
```

Schedule:

```text
0 21 * * *   # 18h BRT em UTC-3
```

Prompt conceitual:

```text
Execute a consolidação diária do Hermes Brain para Lucas.

1. Leia outputs relevantes das últimas 24h: reports, receipts, handoffs, cron outputs e contexto de sessão disponível.
2. Consolide o que foi feito por área: Lucas pessoal, LK, Zipper, SPITI, Operações, Governança.
3. Separe decisões, pendências, riscos e bloqueios.
4. Promova aprendizados duráveis para a memória/arquivo correto quando for seguro.
5. Atualize ou proponha atualização de pendências e hot/current, sem segredos.
6. Entregue no Telegram uma versão curta e salve uma versão no Brain.
```

Arquivo diário sugerido:

```text
reports/daily-consolidation/YYYY-MM-DD.md
```

Formato:

```md
# Fechamento do Dia — YYYY-MM-DD

## Hoje foi feito
- ...

## Decisões
- ...

## Pendências / bloqueios
- ...

## Especialistas
- LK Growth: ...
- Mordomo: ...
- SPITI: ...
- Zipper: ...

## Amanhã
- ...

## Promover para memória
- ...

## Fontes
- ...
```

## Entregável 4 — Maintenance a cada 3 dias

Nome sugerido:

```text
Hermes Brain memory maintenance
```

Objetivo:

- ler consolidações diárias recentes;
- destilar aprendizados duráveis;
- atualizar `memories/*.md` ou docs estruturais;
- arquivar pendências encerradas;
- manter hot/current enxuto.

Guardrail:

- sempre mostrar/promover apenas informação durável;
- não registrar “feito X” efêmero em memória global;
- não gravar credenciais ou logs sensíveis.

## Entregável 5 — Auditoria mensal de MAPAs

Objetivo:

- verificar MAPAs distribuídos;
- detectar arquivo novo sem link;
- detectar rotina com cron mas sem `.md`;
- detectar doc obsoleto apontando para versão errada;
- consolidar gaps de documentação do Brain.

## Critérios de aceite

- Existe inventário versionado de crons/agentes/profiles.
- Existe rotina documentada para auditoria 07h.
- Existe rotina documentada para consolidação 18h.
- Consolidação separa: feito, decisões, pendências, especialistas, amanhã, fontes.
- Meta-cron detecta falhas de cron e ausência de handoff.
- Nenhum write externo produtivo é feito.
- Outputs são curtos no Telegram e completos no Brain.
- Arquivos novos são linkados no `MAPA.md` correto.

## Riscos

- Ruído excessivo no Telegram.
  - Mitigação: output curto; detalhes ficam no Brain.

- Salvar dado sensível por engano.
  - Mitigação: secret scan, redaction e regra de não salvar logs crus.

- Cron virar “mais um relatório” sem ação.
  - Mitigação: sempre incluir pendência, dono/contexto e próximo passo.

- Especialistas continuarem ilhas.
  - Mitigação: campo obrigatório “sem handoff” na auditoria 07h.

## Próximo passo operacional

Após aprovação do Lucas:

1. Criar `areas/operacoes/inventarios/crons-agentes-profiles.md`.
2. Criar rotina `.md` da auditoria 07h.
3. Criar rotina `.md` da consolidação 18h.
4. Criar primeiro cron em modo seguro, entregando no Telegram/origin e salvando no Brain.
5. Rodar manualmente uma vez antes de ativar recorrência.
