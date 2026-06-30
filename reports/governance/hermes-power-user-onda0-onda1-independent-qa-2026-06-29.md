# QA independente — Hermes Power-User Onda 0/Onda 1

Data: 2026-06-29  
Modo: read-only QA por subagente independente.  
Escopo: verificar artefatos locais do Brain; sem writes do subagente, sem runtime, sem cron, sem Docker/VPS, sem credenciais, sem externo.

## Veredito inicial

**FAIL parcial / PASS com ressalvas** antes das correções finais.

## Achados do QA

| Checagem | Status inicial | Observação |
|---|---:|---|
| Artefatos esperados existem | PASS | 6 arquivos esperados existiam. |
| Escopo local/read-only/documental | PASS | Documentos bloqueavam cron/restart/Docker/VPS/dashboard/API/credenciais/writes externos/produção. |
| `empresa/rotinas/_index.md` | PASS parcial | Rotinas novas indexadas; reports governance fora do índice de rotinas é aceitável. |
| `areas/operacoes/MAPA.md` | FAIL | MAPA não apontava para os novos documentos. |
| Evidência Workcell no piloto | FAIL parcial | Report tinha etapas, mas faltavam resultados objetivos de QA, health, varredura de credenciais e receipt. |
| Duplicidade | WARN | Havia cópia duplicada do report em `areas/operacoes/reports/`. |

## Correções solicitadas pelo QA

1. Indexar novos documentos no MAPA.
2. Complementar o report do piloto com evidência objetiva.
3. Remover/neutralizar duplicata documental.
4. Rodar Brain health e varredura de credenciais após as correções.

## Status após correção

Ver relatório final do piloto e receipt final para evidência pós-correção.
