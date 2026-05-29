# Approval packet — Automação semanal LK Sort Manual Regra B

Data: 2026-05-28

## Objetivo
Atualizar 1x por semana a ordem das coleções manuais da Shopify usando a Regra B LK Sort Manual.

## Regra operacional
- Top 4: últimos 4 produtos criados, ativos e publicados na Online Store.
- Corpo: score = 70% venda líquida/capturada Shopify + 30% visitas GA4 em página de produto.
- Pedidos válidos: `paid` e `partially_paid`.
- Expurgar: cancelado/refunded/void/pending/authorized/fraude.
- OOS/não vendável: depois do corpo vendável.

## Escopo da automação
Inclui:
- Descobrir todas as coleções Shopify com `sortOrder = MANUAL` e mais de 1 produto.
- Gerar snapshot/rollback pré-write.
- Recalcular alvo com dados recentes de Shopify + GA4 + Tiny snapshot local.
- Executar `collectionReorderProducts` somente em coleções que precisem de mudança.
- Verificar Admin full order e público Top 12.
- Gerar receipt JSON/MD.

Não inclui:
- Produto, preço, estoque, tags, SEO, tema, checkout, GMC, campanhas, clientes ou Klaviyo.
- Publicar produtos, alterar disponibilidade ou criar coleções.

## Artefatos preparados
- Script base aplicado em lote: `/opt/data/hermes_bruno_ingest/scripts/apply_all_manual_collections_ruleB_net_sales_ga4_20260528.py`
- Wrapper semanal seguro: `/opt/data/hermes_bruno_ingest/scripts/lk_weekly_collection_sort_ruleB.sh`
- Logs semanais: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/weekly-logs/`

## Modos
### Dry-run seguro
Comando:
```bash
/opt/data/hermes_bruno_ingest/scripts/lk_weekly_collection_sort_ruleB.sh
```
Efeito:
- Não altera Shopify.
- Gera snapshot/plano e contagem de coleções que seriam reordenadas.

### Apply com write Shopify
Comando:
```bash
APPLY=1 /opt/data/hermes_bruno_ingest/scripts/lk_weekly_collection_sort_ruleB.sh
```
Efeito:
- Executa writes Shopify de ordenação manual de coleções.
- Gera snapshot antes do write e receipt depois.

## Cron proposto — opção recomendada
Executar toda sexta-feira às 06:00 BRT, com write automático:
```cron
0 6 * * 5 APPLY=1 /opt/data/hermes_bruno_ingest/scripts/lk_weekly_collection_sort_ruleB.sh
```

## Alternativa mais conservadora
Executar toda sexta-feira às 06:00 BRT em dry-run e pedir aprovação manual para apply:
```cron
0 6 * * 5 /opt/data/hermes_bruno_ingest/scripts/lk_weekly_collection_sort_ruleB.sh
```

## Riscos
- A ordem muda automaticamente no storefront 1x por semana.
- Produtos novos podem subir ao Top 4 sem venda, por desenho da regra.
- Se GA4 ou Tiny estiver indisponível, o script precisa reportar isso no receipt; evitar aplicar cegamente se a fonte crítica falhar.

## Rollback
- Cada execução salva `rollback-snapshot-pre-write.json` com a ordem anterior.
- Rollback é reaplicar a lista `current_order_product_ids` do snapshot para cada coleção afetada via `collectionReorderProducts`.

## Aprovação necessária
Como `APPLY=1` faz Shopify write recorrente, exige aprovação explícita de Lucas antes de instalar cron automático.

Frase sugerida para aprovação:
> Aprovado habilitar cron semanal com APPLY=1 para LK Sort Manual Regra B todo domingo às 06:00 BRT.
