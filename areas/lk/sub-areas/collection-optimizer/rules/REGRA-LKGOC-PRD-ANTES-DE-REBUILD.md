# REGRA — LKGOC PRD antes de Rebuild

Registrado em: 20260606T180847Z
Status: **BLOQUEANTE / CANÔNICO**

## Regra curta

Nenhuma coleção LKGOC pode ser reconstruída, aprovada ou marcada como PASS sem PRD e perguntas/brief respondidos.

## Gate -2 obrigatório

Antes de Contract Lock, build DEV ou QA:

1. PRD da execução existe.
2. Perguntas bloqueantes foram respondidas por Lucas ou marcadas como default aprovado.
3. Gold Source 204L confirmado.
4. Critérios de aceite visual definidos.
5. Worker/Superpowers veto definido.

## Status

- Sem PRD: `FAIL_NO_PRD`
- Sem perguntas respondidas: `FAIL_NO_QUESTIONS`
- Sem side-by-side 204L: `FAIL_VISUAL_CONTRACT_204L`
- Com tudo aprovado: `READY_FOR_DEV_BUILD`

## Relação com DEV/Production

- DEV/unpublished continua permitido após Gate -2.
- Production/main continua proibido sem aprovação explícita de Lucas.

## Incidente de origem

Criado após falha Puma Speedcat, quando QA técnico foi confundido com fidelidade visual LKGOC.
