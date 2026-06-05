# Approval Packet — LK Weekly Collection Sort Rule B recorrente APPLY

Gerado em: 2026-06-04T09:45:43Z
Status: `approval_packet_prepared_not_executed`

## Decisão pedida

Autorizar ou não o cron semanal **LK Weekly Collection Sort Rule B** a rodar em modo **APPLY real recorrente**.

## Estado atual

- Cron job: `787134d4ac5c` — `LK Weekly Collection Sort Rule B`.
- Agenda atual: sexta-feira 09:00 UTC.
- Script atual: `/opt/data/scripts/lk_weekly_collection_sort_ruleB.sh`.
- Segurança atual: **dry-run por padrão**; APPLY real só roda quando `LK_WEEKLY_COLLECTION_SORT_APPLY=1`.
- Nenhuma recorrência APPLY foi ativada por este packet.

## Evidência do APPLY real já validado

Última execução APPLY real validada:

- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/all-manual-ruleB-net-sales-ga4-20260603T122044Z/RECEIPT.md`
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/all-manual-ruleB-net-sales-ga4-20260603T122044Z/receipt-final.json`
- Coleções selecionadas: **140**
- Movimentos totais: **4982**
- Admin full ok: **140/140**
- Admin top12 ok: **n/d**
- Público top12 ok: **140/140**
- Rollback snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/all-manual-ruleB-net-sales-ga4-20260603T122044Z/rollback-snapshot-pre-write.json`

## Escopo exato se aprovado

Se Lucas aprovar explicitamente, executar somente:

1. Criar `/opt/data/scripts/lk_weekly_collection_sort_ruleB_apply_recurring.sh`.
2. Esse wrapper fará apenas:
   - `export LK_WEEKLY_COLLECTION_SORT_APPLY=1`;
   - chamar `/opt/data/scripts/lk_weekly_collection_sort_ruleB.sh`;
   - preservar `flock`, logs, async runner e receipts do wrapper existente.
3. Atualizar **somente** o cron `787134d4ac5c` para usar o novo wrapper recorrente APPLY.
4. Verificar com `cronjob list` que o script do job mudou para `lk_weekly_collection_sort_ruleB_apply_recurring.sh`.
5. Fazer uma verificação sintática/local do novo wrapper; não rodar APPLY manual extra sem pedido separado.

## O que NÃO está aprovado por este packet

- Não alterar produtos, preço, estoque, tags, SEO, GMC, tema, campanhas ou clientes.
- Não mexer em Docker, VPS, Traefik, gateway, providers ou secrets.
- Não alterar outros crons.
- Não rodar uma execução APPLY manual imediata, salvo pedido explícito separado.
- Não mudar a lógica Rule B; apenas a recorrência do modo APPLY.

## Risco

Risco principal: toda sexta o Shopify terá reordenação real de coleções manuais conforme a Regra B. Mesmo com rollback snapshot por execução, é uma automação A3 porque muda superfície comercial da loja.

## Rollback

Se precisar voltar atrás:

1. Atualizar o cron `787134d4ac5c` de volta para `lk_weekly_collection_sort_ruleB.sh`.
2. Verificar `cronjob list`.
3. Se uma execução APPLY já tiver rodado e o resultado precisar ser revertido, usar o `rollback-snapshot-pre-write.json` da execução correspondente.
4. Registrar receipt de rollback no Brain.

## Critério de parada automática recomendado

Na primeira falha de:

- `async runner exit status != 0`;
- `admin_full_ok` incompleto;
- `public_top12_ok` incompleto;
- ausência de rollback snapshot;
- lock preso por execução anterior;

pausar retorno para dry-run e alertar Lucas com evidência curta.

## Aprovação necessária

Para eu ativar a recorrência APPLY, responda exatamente ou de forma equivalente:

**APROVO RULE B APPLY RECORRENTE**

Sem essa aprovação, o cron permanece em dry-run.
