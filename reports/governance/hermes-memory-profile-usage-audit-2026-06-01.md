# Auditoria rápida — uso de memória built-in por profile

Data: 2026-06-01  
Escopo: tamanho dos arquivos `memories/MEMORY.md` e `memories/USER.md` por profile. Não altera runtime/gateway.

## Resultado

- default: `MEMORY.md` 1.092/2.200 (50%); `USER.md` 1.019/1.375 (74%) — OK após compactação.
- lk-shopify: `MEMORY.md` 2.345/2.200 (107%); `USER.md` 1.368/1.375 (99%) — precisa compactar.
- lk-trends: `MEMORY.md` 2.088/2.200 (95%); `USER.md` 1.362/1.375 (99%) — precisa compactar.
- spiti: `MEMORY.md` 2.315/2.200 (105%); `USER.md` 1.344/1.375 (98%) — precisa compactar.
- mordomo: `MEMORY.md` 2.341/2.200 (106%); `USER.md` 1.307/1.375 (95%) — precisa compactar.
- lk-ops: `MEMORY.md` 2.354/2.200 (107%); `USER.md` 1.362/1.375 (99%) — precisa compactar.
- brain-process: `MEMORY.md` 2.163/2.200 (98%); `USER.md` 1.351/1.375 (98%) — precisa compactar se continuar ativo.
- lk-content-reviewer: `MEMORY.md` 2.163/2.200 (98%); `USER.md` 1.351/1.375 (98%) — precisa compactar se continuar ativo.
- lk-growth: `MEMORY.md` 2.715/2.200 (123%); `USER.md` 1.290/1.375 (94%) — prioridade máxima de compactação.
- lk-analyst-readonly: `MEMORY.md` 2.163/2.200 (98%); `USER.md` 1.351/1.375 (98%) — precisa compactar se continuar ativo.
- hermes-ops-readonly: `MEMORY.md` 2.163/2.200 (98%); `USER.md` 1.351/1.375 (98%) — precisa compactar se continuar ativo.

## Interpretação

A correção foi aplicada ao profile default, mas o ecossistema ainda tem o mesmo problema nos especialistas: quase todos estão com memória built-in perto ou acima do limite.

Isso confirma a análise: a política precisa ser aplicada por profile, com cada especialista mantendo apenas boot mínimo e usando Brain/skills/context files para memória rica.

## Ordem recomendada de saneamento

1. `lk-growth` — maior excesso e perfil com muito contexto operacional/SEO/CRO/GEO.
2. `lk-ops`, `lk-shopify`, `spiti`, `mordomo` — acima do limite.
3. `lk-trends` — quase cheio.
4. Perfis worker (`brain-process`, `lk-content-reviewer`, `lk-analyst-readonly`, `hermes-ops-readonly`) — compactar ou aposentar se forem legados/dormant.

## Regra de execução

Para cada profile:

1. Backup dos dois arquivos de memória.
2. Migrar detalhes ricos para Brain/area/profile skill/context file.
3. Reescrever `MEMORY.md` como ponteiros + guardrails do domínio.
4. Reescrever `USER.md` com preferências de Lucas relevantes ao domínio, sem duplicar todo o perfil global.
5. Verificar tamanho final e ausência de secrets.
6. Não reiniciar gateway por causa disso; a nova memória entra em efeito na próxima sessão/restart do profile.
