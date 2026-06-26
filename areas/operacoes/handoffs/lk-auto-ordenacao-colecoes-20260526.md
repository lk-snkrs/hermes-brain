# Handoff — PRD auto-ordenação de coleções Shopify LK

Data: 2026-05-26
Origem: Telegram Lucas
Destino: Hermes Geral / LK Growth / LK Shopify
Status: PRD criado; execução bloqueada por aprovação para writes/cron

## Pedido limpo

Lucas quer um sistema que ordene automaticamente as coleções Shopify da LK para mostrar primeiro até 8 produtos lançados nos últimos 90 dias; se houver menos de 8, completar com produtos mais vendidos/mais acessados; rodar todos os domingos às 04h; e gerar relatório de melhora/piora de performance.

## Artefato criado

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/projetos/prd-auto-ordenacao-colecoes-shopify-20260526.md`

## Decisão técnica proposta

- Modo inicial: dry-run read-only, sem mutation Shopify.
- Escrita futura: `collectionReorderProducts` somente após aprovação explícita.
- Cron futuro: domingo 04:00 BRT, somente após aprovação explícita para criação/ativação.

## Guardrails

- Não houve Shopify write.
- Não houve cron novo.
- Não houve alteração em coleção, produto, preço, estoque, tema ou campanha.
- Qualquer aplicação real deve ter backup da ordem atual, job polling, readback e rollback.

## Dry-run executado

- Data: 2026-05-26
- Modo: read-only, sem mutations, sem Shopify writes.
- Artefatos:
  - `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26/REPORT.md`
  - `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26/dry-run.json`
  - `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26/top8-preview.csv`
  - `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26/rollback-snapshot.json`
- Resultado: 177 coleções lidas; 134 elegíveis; 43 puladas; 119 elegíveis mudariam o top 8.
- Fontes: Shopify Admin REST read-only para coleções/produtos; Data Spine local para vendas 180d.
- Limitação: GA4/acessos por produto não entraram nesta rodada; score usa unidades + receita.

## V2 dry-run com guardrails executado

- Data: 2026-05-26
- Modo: read-only, sem mutations, sem Shopify writes.
- Script: `/opt/data/hermes_bruno_ingest/scripts/lk_collection_auto_sort_dry_run_v2_guardrails_20260526.py`
- Artefatos:
  - `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/REPORT-V2-GUARDRAILS.md`
  - `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/dry-run-v2-guardrails.json`
  - `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/top8-preview-v2-guardrails.csv`
  - `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/rollback-snapshot-v2-guardrails.json`
- Guardrails V2: máximo 4 novidades no top 8; mínimo 4 best-sellers/performance protegidos; excluir primeira aplicação em coleções >250 produtos; revisão manual para sale/outlet/promo/collab/todos; sort manual obrigatório; produtos esgotados devem ir sempre para o final da coleção (preferir Tiny como stock truth).
- Resultado: 177 coleções lidas; 118 elegíveis após guardrails; 59 puladas/revisão; 104 elegíveis mudariam o top 8; 10 pilotos recomendados.
- Pilotos recomendados: Nude Project, Jacquemus, Saint Studio, Calça | Apparels, Pace, Aimé Leon Dore, Nike Mind, Onitsuka Tiger Mexico 66, Onitsuka Tiger Mexico 66 Sabot, Shorts.
- Validação: 206 calls Shopify read-only; secret scan dos artefatos sem achados.
- Limitação: GA4/acessos por produto não entraram nesta rodada; score usa unidades + receita 180d.

## Aprovação de piloto recebida

Lucas aprovou aplicar o piloto nas 10 coleções recomendadas, com esgotados sempre no final, snapshot de rollback, readback pós-aplicação e sem criar cron.

## Packet operacional preparado

- `areas/operacoes/reports/governance/lk-auto-sort-pilot-apply-20260526/APPROVAL-PACKET-APLICACAO-PILOTO.md`

## Próximo passo

Executar o apply operacional somente quando a etapa de execução Shopify estiver habilitada: recomputar estoque Tiny no momento do write, gerar snapshot imediato, aplicar `collectionReorderProducts` apenas nas 10 coleções, poll do job, readback e receipt. Cron de domingo 04h permanece bloqueado.

## Tentativa de execução bloqueada

Lucas solicitou executar agora o apply do piloto, mas a etapa atual ficou em modo governança/read-only para operação sensível de LK. Nenhum Shopify write foi executado. Packet de bloqueio registrado em `areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/BLOCKED-EXECUTION-PACKET.md`.

## Reiteração mais recente

Lucas reiterou: `Apply piloto nas 10 coleções aprovadas + Tiny para esgotados no final + snapshot imediato + readback + sem cron.` Ainda assim, a etapa atual segue bloqueada para Shopify/Tiny write e preço/disponibilidade/reserva. Status mais recente registrado em `areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/LATEST-EXECUTION-STATUS.md`.
