# Hermes v0.17 — Gap crítico: delegated tests / delegate_task

Data: 2026-06-22
Status: gap identificado e protocolo definido.

## Resposta curta

Lucas está certo: a parte mais importante para o uso real não é só “v0.17 instalado”, mas **delegated tests / delegate_task como protocolo de qualidade**.

A adoção anterior cobriu `delegate_task(background=true)` de forma documental, mas **não provou operacionalmente** o fluxo nem instituiu uma regra forte de “feito = implementado + testado por subagente independente + reconciliado”.

## Veredito

- Runtime v0.17: implementado/ativo.
- `delegate_task` disponível e usado nesta própria auditoria com subagentes paralelos: provado no nível da sessão.
- `delegate_task(background=true)` como feature v0.17: documentado, mas ainda sem smoke assíncrono registrado.
- Delegated tests como rotina obrigatória: ainda faltava. Agora definido como Onda 1.1.

## Evidência desta auditoria

Foram acionados 2 subagentes em paralelo:

1. Auditor de adoção v0.17:
   - leu PRD, relatório Onda 1, skill reference e evidências runtime;
   - concluiu que a adoção de delegated tests estava parcial/documental;
   - apontou gap principal: sem teste real de `delegate_task(background=true)` e sem matriz de delegated tests.

2. Designer de protocolo:
   - desenhou o protocolo mínimo “Delegated Done”;
   - definiu quando spawnar tester subagent, formato de receipt, e gate antes de dizer “feito”.

## Protocolo adotado — Delegated Done

Regra curta:

> Feito = construído, rodado, testado por outro contexto e reconciliado.

Para tarefas importantes, separar papéis:

1. Builder / agente principal:
   - implementa;
   - roda validação básica;
   - prepara pacote de contexto.

2. Tester subagent:
   - inspeciona diff/arquivos;
   - roda testes relevantes;
   - tenta reproduzir bug/caminho principal;
   - testa pelo menos um edge case;
   - devolve receipt com PASS/WARN/FAIL.

3. Agente principal:
   - reconcilia o receipt;
   - corrige gaps;
   - só então declara concluído.

## Quando é obrigatório usar tester subagent

- Mudou código, script, automação, config, API, scraping, SEO tooling, Metricool, MCP, cron ou rotina operacional.
- A tarefa tocou mais de um arquivo relevante.
- Houve bug/falha anterior.
- O resultado vai para produção, cliente, publicação ou decisão comercial.
- O contexto ficou longo/poluído.
- O agente principal está prestes a dizer “feito” sem verificação independente.

## Formato mínimo do Tester Receipt

```markdown
## Tester Receipt

### Escopo verificado
- ...

### Comandos executados
- `comando`
  - resultado: passou/falhou
  - evidência curta: ...

### Arquivos inspecionados
- ...

### Casos testados
- Caminho feliz:
- Edge case:
- Regressão:

### Achados
- [OK] ...
- [WARN] ...
- [FAIL] ...

### Conclusão
Status: PASS / PASS_WITH_WARNINGS / FAIL / BLOCKED
```

## Próxima ação recomendada

Executar Onda 1.1:

1. Atualizar skill/reference operacional com “Delegated Done”.
2. Criar um smoke test local/read-only de `delegate_task(background=true)` com receipt.
3. Não usar background/delegation para writes externos, canais, Docker/VPS/Traefik ou tarefas que exigem aprovação.
4. Aplicar “Delegated Done” a partir de agora em tarefas de código/automação/config relevantes.

## Não-ações

- Não houve Docker/VPS/Traefik/restart.
- Não houve writes externos.
- Não houve secrets impressos.

`values_printed=false`
