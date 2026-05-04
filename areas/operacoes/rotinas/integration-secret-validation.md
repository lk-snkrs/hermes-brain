# Rotina — Validação de Secrets das Integrações

Objetivo: confirmar que os nomes de secrets documentados em `TOOLS.md` e `empresa/integracoes/` existem no Doppler `lc-keys/prd`, sem imprimir valores.

## Escopo

- Fonte de nomes: `TOOLS.md` e `empresa/integracoes/*.md`.
- Fonte de verdade de credenciais: Doppler `lc-keys/prd`.
- Helper canônico: `/opt/data/hermes_bruno_ingest/hermes_doppler.sh`.

## Nível de permissão

- Read-only: permitido por padrão.
- Write: não aplicável, salvo atualizar docs após divergência.
- External-send: não aplicável.
- Admin/destructive: criar, rotacionar ou remover secrets exige aprovação explícita de Lucas.

## Passo a passo seguro

1. Extrair apenas nomes token-like dos docs.
2. Rodar `hermes_doppler.sh exists SECRET_NAME...`.
3. Reportar somente `OK`/`MISSING`, nunca valores.
4. Se aparecer nome genérico como `SERVICE_KEY` ou `PROJECT_ID`, corrigir o doc para o nome real da integração ou explicar que é placeholder conceitual.
5. Se houver `MISSING` real, documentar lacuna; não criar secret sem aprovação.

## Verificação atual

Validação feita em 2026-05-04 após a Rodada B:

- Nomes reais das integrações críticas retornaram `OK` no Doppler.
- `PROJECT_ID` e `SERVICE_KEY` apareceram apenas como placeholders genéricos em troubleshooting e devem ser evitados em docs operacionais.
- Valores de secrets não foram impressos.

## Saída esperada

Resumo com contagens e lista de pendências por nome, sem valores.
