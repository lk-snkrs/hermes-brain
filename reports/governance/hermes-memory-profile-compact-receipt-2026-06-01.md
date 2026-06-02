# Receipt — compactação de memória built-in dos profiles Hermes

Data: 2026-06-01  
Tipo: saneamento local/documental de memória Hermes.  
Escopo: `MEMORY.md` e `USER.md` dos profiles especialistas/read-only.  
Não-ações: sem restart de gateway, sem Docker/VPS/Traefik, sem write externo, sem secrets impressos.

## Objetivo

Aplicar a política canônica `memories/politica-memoria-hermes.md`: memória built-in do Hermes como boot mínimo; memória rica no Brain/dailies/hot/context files/skills/session_search/reports.

## Backup

Backups dos arquivos anteriores salvos em:

`reports/governance/memory-backups/20260601-memory-boot-compact/`

Manifest:

`reports/governance/memory-backups/20260601-memory-boot-compact/manifest.json`

## Resultado por profile

- default: já estava OK antes desta etapa — `MEMORY.md` 1.092/2.200 (49,6%); `USER.md` 1.019/1.375 (74,1%).
- lk-growth: `MEMORY.md` 900/2.200 (40,9%); `USER.md` 979/1.375 (71,2%).
- lk-ops: `MEMORY.md` 826/2.200 (37,5%); `USER.md` 982/1.375 (71,4%).
- lk-shopify: `MEMORY.md` 811/2.200 (36,9%); `USER.md` 972/1.375 (70,7%).
- spiti: `MEMORY.md` 717/2.200 (32,6%); `USER.md` 581/1.375 (42,3%).
- mordomo: `MEMORY.md` 819/2.200 (37,2%); `USER.md` 441/1.375 (32,1%).
- lk-trends: `MEMORY.md` 688/2.200 (31,3%); `USER.md` 926/1.375 (67,3%).
- brain-process: `MEMORY.md` 761/2.200 (34,6%); `USER.md` 424/1.375 (30,8%).
- lk-content-reviewer: `MEMORY.md` 761/2.200 (34,6%); `USER.md` 424/1.375 (30,8%).
- lk-analyst-readonly: `MEMORY.md` 761/2.200 (34,6%); `USER.md` 424/1.375 (30,8%).
- hermes-ops-readonly: `MEMORY.md` 761/2.200 (34,6%); `USER.md` 424/1.375 (30,8%).

## Verificação

- Todos os profiles auditados ficaram abaixo do limite de memória built-in.
- Secret scan regex nos arquivos finais: nenhum achado.
- Mudança afeta próxima sessão/restart de cada profile; sessões já abertas podem continuar usando snapshot antigo.

## Interpretação

A melhoria de memória saiu de “corrigir default + política” para “corrigir ecossistema de profiles”. A memória injetada agora está curta em todos os profiles auditados. A memória rica deve continuar sendo organizada no Brain e nas skills, não reexpandida nos arquivos `memories/` dos profiles.

## Próximos passos recomendados

1. Revisar se algum profile legacy/read-only deve ser aposentado em vez de mantido.
2. Quando houver nova correção recorrente, salvar em skill/Brain, não em built-in memory longa.
3. Avaliar provider externo de memória em spike isolado, se houver necessidade real de recall semântico além de Brain + session_search.
