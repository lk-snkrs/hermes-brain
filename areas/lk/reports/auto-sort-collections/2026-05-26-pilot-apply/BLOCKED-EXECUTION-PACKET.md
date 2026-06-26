# Packet — execução piloto auto-ordenação Shopify bloqueada por governança

Data: 2026-05-26
Destino: LK Growth / Shopify Collections
Status: execução Shopify não realizada; packet local registrado.

## Pedido limpo

Executar agora o apply do piloto Shopify nas 10 coleções aprovadas, usando Tiny para empurrar esgotados ao final, com snapshot imediato, readback pós-aplicação e sem cron.

## Evidências

Aprovação verbal/textual recebida para o piloto nas 10 coleções:

1. Nude Project
2. Jacquemus
3. Saint Studio
4. Calça | Apparels
5. Pace
6. Aimé Leon Dore
7. Nike Mind
8. Onitsuka Tiger Mexico 66
9. Onitsuka Tiger Mexico 66 Sabot
10. Shorts

Artefatos base existentes:

- `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/REPORT-V2-GUARDRAILS.md`
- `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/dry-run-v2-guardrails.json`
- `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/top8-preview-v2-guardrails.csv`
- `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/rollback-snapshot-v2-guardrails.json`
- `areas/operacoes/reports/governance/lk-auto-sort-pilot-apply-20260526/APPROVAL-PACKET-APLICACAO-PILOTO.md`

## Preview técnico da execução aprovada

A execução real deve:

1. ler as 10 coleções no Shopify imediatamente antes do write;
2. gerar snapshot imediato de rollback;
3. consultar/reconciliar Tiny/SQLite para classificar produtos com estoque confirmado zerado;
4. recomputar ordem final com esgotados no final;
5. gerar moves somente para posições alteradas;
6. aplicar `collectionReorderProducts` por coleção;
7. poll do job assíncrono;
8. readback da ordem aplicada;
9. salvar receipt com sucesso/falhas por coleção;
10. não criar cron.

## Risco

- A operação altera a vitrine pública das coleções.
- A operação pode impactar conversão se estoque/ordem forem classificados de forma incorreta.
- A operação toca merchandising público, então exige execução em perfil operacional habilitado para write Shopify e validação pós-write.

## Bloqueio

A execução foi bloqueada nesta etapa de governança/read-only. Nenhum `collectionReorderProducts` foi executado.

Não houve:

- Shopify write;
- Tiny write;
- cron;
- alteração de preço, estoque, produto, tema, checkout, SEO, tags, campanha ou comunicação.

## Rollback

Rollback preparado conceitualmente:

- snapshot pré-write imediato deve ser salvo antes da execução;
- se houver falha ou necessidade de reversão, restaurar a ordem anterior por `collectionReorderProducts` usando o snapshot;
- poll do job;
- readback;
- registrar receipt de rollback.

## Nova tentativa de execução

Lucas reiterou a solicitação de executar o apply do piloto Shopify nas 10 coleções aprovadas. A etapa permaneceu bloqueada para writes Shopify/Tiny e ações que afetem disponibilidade/merchandising público; portanto, nenhum `collectionReorderProducts` foi executado.

## Próximo passo

Encaminhar para execução operacional Shopify habilitada ou reemitir a aprovação em um contexto que permita write Shopify. A frase de execução permanece:

> Executar agora o apply do piloto Shopify nas 10 coleções aprovadas, usando Tiny para empurrar esgotados ao final, com snapshot imediato, readback e sem cron.
