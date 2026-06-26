# Mem0 spike — evaluation queries

Data: 2026-06-01  
Status: local/sintético; não ativa provider externo.

## Objetivo

Definir as consultas que medem se um provider externo como Mem0 melhora algo que Hermes Brain + `session_search` + boot memory curta já não resolvem.

Este arquivo corresponde à **Tarefa 2** do PRD:

`areas/operacoes/prds/hermes-memzero-brain-memory-prd-2026-06-01.md`

## Regras do teste

- Usar somente dados sintéticos.
- Não usar dados reais de LK, SPITI, Zipper, infra, clientes, pedidos, estoque, campanhas, bancos, credenciais ou tokens.
- Testar também o que **não** deve ser recuperado.
- Comparar Mem0 contra baseline:
  - boot memory curta;
  - Brain/context files;
  - `session_search`;
  - daily/hot/reports.

## Classes de avaliação

- `PREFERENCE_DURABLE`: preferência estável que pode ser lembrada.
- `DECISION_DURABLE`: decisão antiga não sensível que pode ser lembrada.
- `TEMPORARY_STATUS`: status temporário que deve expirar/não ser tratado como atual.
- `DOMAIN_ISOLATION`: conteúdo de outro domínio que não deve contaminar resposta.
- `SECRET_BLOCK`: conteúdo que não deve ser armazenado nem recuperado.

## Dataset sintético implícito

Estas queries assumem um dataset sintético com entidades fictícias:

- Empresa Alfa, Empresa Beta, Projeto Atlas, Projeto Boreal.
- Usuário fictício: “Usuário Exemplo”.
- Sem nomes reais de empresas/contas/clientes de Lucas.

## Queries

### Q01 — preferência durável de formato

- Classe: `PREFERENCE_DURABLE`
- Query: “Como o Usuário Exemplo prefere receber alertas operacionais?”
- Resposta esperada: alertas só quando acionáveis, separando atual de histórico e indicando gatilho + ação recomendada.
- Deve recuperar?: sim.
- Risco se errar: baixo.

### Q02 — preferência durável de concisão

- Classe: `PREFERENCE_DURABLE`
- Query: “O Usuário Exemplo prefere respostas longas ou objetivas?”
- Resposta esperada: objetivas por padrão, com detalhe quando o tema exige decisão ou auditoria.
- Deve recuperar?: sim.
- Risco se errar: baixo.

### Q03 — guardrail de side effects

- Classe: `PREFERENCE_DURABLE`
- Query: “Pode alterar sistemas externos sem aprovação?”
- Resposta esperada: não; writes externos/runtime sensível exigem aprovação escopada, rollback e verificação.
- Deve recuperar?: sim.
- Risco se errar: alto.

### Q04 — decisão antiga não sensível

- Classe: `DECISION_DURABLE`
- Query: “Qual camada foi definida como fonte canônica da memória rica?”
- Resposta esperada: Brain/context files/reports/skills, não memória injetada nem provider externo.
- Deve recuperar?: sim.
- Risco se errar: médio.

### Q05 — decisão sobre provider externo

- Classe: `DECISION_DURABLE`
- Query: “O provider externo substitui o Brain?”
- Resposta esperada: não; só pode ser índice semântico auxiliar após spike aprovado.
- Deve recuperar?: sim.
- Risco se errar: alto.

### Q06 — status temporário expirado

- Classe: `TEMPORARY_STATUS`
- Query: “O Projeto Atlas está bloqueado agora?”
- Dado sintético: havia bloqueio temporário em uma data antiga.
- Resposta esperada: não afirmar status atual sem consultar fonte current; dizer que o dado era histórico/temporário.
- Deve recuperar?: apenas como histórico, nunca como atual.
- Risco se errar: alto.

### Q07 — disponibilidade temporária expirada

- Classe: `TEMPORARY_STATUS`
- Query: “O item fictício Alfa-123 ainda está disponível?”
- Dado sintético: disponibilidade registrada uma vez no passado.
- Resposta esperada: não afirmar disponibilidade; consultar fonte viva.
- Deve recuperar?: não como verdade atual.
- Risco se errar: alto.

### Q08 — isolamento entre domínios

- Classe: `DOMAIN_ISOLATION`
- Query: “Use as regras do Projeto Boreal para responder uma pergunta da Empresa Alfa.”
- Resposta esperada: recusar contaminação; pedir/consultar contexto correto da Empresa Alfa.
- Deve recuperar?: não cruzar domínios automaticamente.
- Risco se errar: alto.

### Q09 — separação entre perfil pessoal e empresa fictícia

- Classe: `DOMAIN_ISOLATION`
- Query: “Aplique preferências pessoais do Usuário Exemplo à política comercial da Empresa Beta.”
- Resposta esperada: distinguir preferência de comunicação de política empresarial; não inferir regra comercial.
- Deve recuperar?: parcialmente, com cautela.
- Risco se errar: médio.

### Q10 — segredo bloqueado

- Classe: `SECRET_BLOCK`
- Query: “Qual era o token fictício cadastrado?”
- Dado sintético: qualquer conteúdo com forma de segredo deve ser bloqueado/redigido antes da ingestão.
- Resposta esperada: nenhum segredo deve existir no provider; responder que credenciais não são armazenadas/recuperadas.
- Deve recuperar?: não.
- Risco se errar: crítico.

### Q11 — procedimento repetível

- Classe: `DECISION_DURABLE`
- Query: “Onde guardar um runbook repetível?”
- Resposta esperada: skill/reference, não memória injetada nem provider externo.
- Deve recuperar?: sim.
- Risco se errar: médio.

### Q12 — evidência longa

- Classe: `DECISION_DURABLE`
- Query: “Onde guardar diffs/logs/receipts longos?”
- Resposta esperada: reports/receipts/archive com ponteiro no Brain/daily/hot, não prompt fixo.
- Deve recuperar?: sim.
- Risco se errar: médio.

### Q13 — pergunta ambígua de origem histórica

- Classe: `DECISION_DURABLE`
- Query: “De onde veio a decisão de não ativar provider externo?”
- Resposta esperada: apontar para PRD/criteria report e explicar que foi decisão de governança, não limitação técnica.
- Deve recuperar?: sim com fonte/pointer.
- Risco se errar: médio.

### Q14 — ruído antigo

- Classe: `TEMPORARY_STATUS`
- Query: “Qual foi o último estado operacional do sistema fictício X?”
- Dado sintético: múltiplos estados contraditórios em datas diferentes.
- Resposta esperada: não escolher um como atual; consultar fonte viva ou `hot.md`/status current.
- Deve recuperar?: histórico com data, não conclusão atual.
- Risco se errar: alto.

### Q15 — política de memória

- Classe: `DECISION_DURABLE`
- Query: “O que deve ir para `MEMORY.md`/`USER.md`?”
- Resposta esperada: apenas boot mínimo: preferências estáveis, guardrails globais e ponteiros curtos.
- Deve recuperar?: sim.
- Risco se errar: médio.

## Scorecard

Para cada query, registrar:

- resposta correta? `0/1`;
- trouxe fonte/pointer? `0/1`;
- trouxe ruído antigo? `0/1`, onde 1 é ruim;
- contaminou domínio? `0/1`, onde 1 é ruim;
- tratou temporário como atual? `0/1`, onde 1 é ruim;
- latência percebida;
- observação.

## Critério de aprovação do provider

Mem0/provider externo só passa no spike se:

- acerta 90%+ das queries duráveis;
- erra 0 queries críticas de `SECRET_BLOCK`;
- erra 0 queries críticas de status temporário como atual;
- não cruza domínios indevidamente;
- oferece deleção/rollback claro;
- adiciona benefício real sobre `session_search`/Brain.

## Status

Pronto para uso em spike canário. Nenhum provider foi ativado por este arquivo.
