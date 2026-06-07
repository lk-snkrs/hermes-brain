# Receipt — piloto read-only de manutenção Curadoria LK PDP

Data: 2026-06-07
Timestamp UTC: 20260607T101645Z

## Escopo

Rodar o primeiro relatório piloto read-only do cron de manutenção da Curadoria LK PDP, sem qualquer write Shopify/DEV/Production.

## Evidência

Cron verificado:

- Job: `7e5ba8b565d5`
- Nome: `LK Curadoria PDP maintenance quinzenal`
- Schedule: `0 11 * * 1`
- Equivalência operacional: segunda 08:00 BRT
- Próxima execução: `2026-06-08T11:00:00+00:00`
- Deliver: `telegram`
- Mode: `no-agent`
- Script: `lk_curadoria_pdp_maintenance_report.py`

Execução piloto forçada:

- Comando: `HERMES_HOME=/opt/data/profiles/lk-shopify /opt/data/profiles/lk-shopify/scripts/lk_curadoria_pdp_maintenance_report.py --force`
- Resultado: `AÇÃO`
- Semáforo: verde 27 · amarelo 1 · vermelho 7 · cinza 0
- Handles públicos checados: 260
- Markdown: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260607T071257-0300.md`
- JSON: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260607T071257-0300.json`

## Prioridades detectadas

Vermelho:

- `top30-nb-9060`: 7 handles inválidos/erro em `/products/{handle}.js`
- `top30-sl72-og`: 9 handles inválidos/erro
- `top30-mexico66-sd`: 8 handles inválidos/erro
- `top30-nb-530`: 8 handles inválidos/erro
- `top30-sb-dunk-low`: 4 handles inválidos/erro
- `top30-adidas-gazelle`: 1 handle inválido/erro
- `top30-asics-gel-1130-regular`: 1 handle inválido/erro

Amarelo:

- `top30-air-jordan-4-regular`: 1 handle público com `available=false`

## Interpretação

O cron está ativo e a rotina piloto cumpriu o papel: encontrou blocos antigos/frágeis que precisam revisão antes de novas expansões. Como a validação pública usa `.js`, eventuais oscilações de CDN/rate-limit podem gerar falso positivo; os grupos vermelhos devem passar por revisão focada antes de qualquer alteração em tema.

## O que não aconteceu

- Nenhum Shopify write.
- Nenhum DEV upload.
- Nenhum Production merge.
- Nenhuma alteração em produto, preço, estoque, Tiny, GMC, Klaviyo ou Ads.

## Próxima decisão recomendada

Preparar um approval packet de reparo read-only priorizando os grupos vermelhos de maior impacto:

1. `top30-nb-530`
2. `top30-nb-9060`
3. `top30-sl72-og`
4. `top30-mexico66-sd`
5. `top30-sb-dunk-low`

Fluxo seguro: revalidar handles atuais, buscar substitutos públicos/sem placeholder, montar proposta de troca, pedir aprovação DEV; só depois escrever em tema unpublished.

## Rollback

Não aplicável para o piloto, pois não houve write externo. Para o cron, remover/pausar o job `7e5ba8b565d5` se Lucas quiser parar a rotina.
