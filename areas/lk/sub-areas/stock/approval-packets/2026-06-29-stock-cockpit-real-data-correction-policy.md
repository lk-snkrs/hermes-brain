# Approval packet — Stock Cockpit correção real dos blocos 1–4

Data: 2026-06-29
Agente: lk-stock
Superfície: Inventory Hub / Stock OS DB / Tiny / Shopify / Supabase

## Pedido

Lucas pediu “Fazer a correção real” dos blocos:

1. Negativos
2. SKU/tamanho ausente
3. Problemas técnicos acionáveis
4. Parent/base não vendável

## Estado verificado read-only

Fonte de auditoria: Stock OS DB, `freshness=tiny_full_sync_nightly`, `values_printed=false`.

| Bloco | Health bruto | Observação |
|---|---:|---|
| Negativos | 29 | Tiny readback atual: 18 ainda negativos, 1 `-2`, 1 já `0`, 1 já `2`, 9 sem match exato no resolver |
| SKU/tamanho ausente | 104 | Parte parece produto sem grade/tamanho único; parte precisa cadastro/variante |
| Problemas técnicos acionáveis | 418 | 171 parecem stale/resolvíveis por readback Tiny exato; o restante envolve Tiny/Shopify missing/duplicate/deposit |
| Parent/base não vendável | 215 | Linhas de produto/modelo não vendáveis; devem ficar fora de disponibilidade e, se mantidas, não deveriam poluir saúde operacional |

Arquivos read-only gerados:

- `areas/lk/sub-areas/stock/reports/stock-cockpit-issue-fix-20260629/summary.json`
- `areas/lk/sub-areas/stock/reports/stock-cockpit-issue-fix-20260629/negativos_tiny_readback.json`

## Correções possíveis

### A. Saneamento seguro do read model/Supabase

Escopo:

- corrigir status/action/raw da latest snapshot para itens com readback seguro;
- remover parent/base da fila de problema operacional, mantendo busca interna;
- transformar produtos sem tamanho em `ÚNICO`/`OS` apenas quando regra determinística for aprovada;
- manter `public_availability_safe=0` e `availability_claim_allowed=0`.

Risco:

- não muda Tiny; se a origem upstream seguir errada, futura sincronização pode reintroduzir.

Rollback:

- backup da latest snapshot antes do update;
- restaurar linhas de `lk_stock_items` e snapshot metadata a partir do backup.

Readback:

- contar novamente health buckets;
- validar MR530SG sentinel;
- validar `/api/stock-cockpit/v2/health` após deploy/sync.

### B. Correção real em Tiny

Escopo típico:

- para negativos ainda negativos no Tiny, ajustar estoque do depósito `LK | CONTROLE ESTOQUE` para `0` ou valor físico informado;
- para no-match/missing/duplicate, corrigir cadastro/código/variação no Tiny.

Risco:

- altera fonte operacional de estoque; pode afetar venda, disponibilidade e conciliação.

Rollback:

- backup/readback Tiny por SKU antes de alteração;
- reverter SKU para quantidade/código anterior por item.

Readback:

- Tiny exact SKU readback por item;
- novo Stock OS sync;
- conferência no Hub.

### C. Correção real em Shopify

Escopo típico:

- corrigir SKU/variant title/tamanho em variante Shopify quando Shopify é a origem do bloqueio;
- resolver duplicidades de variante/produto.

Risco:

- altera storefront/admin product data; pode afetar SEO, carrinho, estoque e integrações.

Rollback:

- readback GraphQL antes/depois por variant/product id;
- reverter campos por variant/product id.

## Recomendação operacional

Não executar write cego em Tiny/Shopify para os 766 sinais. Começar com lote 1 governado:

1. Supabase/read-model sanitation para casos determinísticos e reversíveis.
2. Tiny readback/packet para negativos reais ainda negativos.
3. Shopify/Tiny identity packet para duplicidades/missing.

## Aprovação necessária

Preciso de aprovação escopada indicando qual política aplicar primeiro:

- `Supabase/read-model determinístico` — corrige filas/health sem alterar Tiny/Shopify.
- `Tiny negativos para 0` — altera Tiny para negativos confirmados.
- `Shopify/Tiny cadastro` — altera SKU/tamanho/duplicidades na origem, por lote.

Sem uma dessas políticas, a correção real seria adivinhação de estoque/cadastro.

values_printed=false
