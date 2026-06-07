# REGRA — LKGOC 204L Gold Source Visual Contract

Registrado em: 20260606T173422Z
Status: **BLOQUEANTE / CANÔNICO**

## Regra curta

Toda coleção LKGOC deve ser uma **cópia controlada/adaptação mínima** do padrão aprovado da New Balance 204L, não uma interpretação livre.

Gold Source visual: `https://lksneakers.com.br/collections/new-balance-204l`

## O que é obrigatório

Antes de declarar PASS em qualquer coleção LKGOC:

1. Capturar screenshot do Gold Source 204L.
2. Capturar screenshot da coleção alvo no tema DEV/unpublished.
3. Gerar comparativo visual lado a lado.
4. Confirmar equivalência visual com 204L em:
   - hierarquia de seções;
   - densidade editorial;
   - ritmo e peso visual do hero;
   - shell do guia pós-grid;
   - padrão de FAQ;
   - ordem hero → grid → guia;
   - tom premium/minimalista;
   - uso do componente único sem inventar layout novo.
5. Registrar o comparativo no receipt/QA.

## O que reprova automaticamente

- QA técnico sem comparação visual lado a lado.
- Hero/guia/FAQ presentes, mas com layout próprio não derivado do 204L.
- Branch nova que apenas usa `lk-goc-*`, mas não replica o shell 204L.
- Declaração de PASS baseada só em DOM, schema, ausência de Liquid error ou presença de imagens editoriais.
- Qualquer build que trate 204L como inspiração em vez de contrato.

## Política DEV/Production

- Rebuild/correção pode ser feito em DEV/unpublished.
- Production/main continua proibido sem aprovação explícita de Lucas.
- Se o audit visual 204L vs coleção falhar, merge para Production é bloqueado.

## Puma Speedcat — incidente de origem

A Puma Speedcat DEV de 2026-06-06 foi reprovada porque passou por QA técnico, mas não por fidelidade visual 204L. Este incidente originou esta regra.
