# Playbook — Preço/promo aprovado LK Shopify

Data: 2026-06-05
Status: template operacional local/read-only até aprovação escopada.

## Quando usar

Use apenas quando Lucas/LK Ops já aprovou a decisão/fonte de preço/promo e existe lista exata de produtos/variantes. LK Shopify operacionaliza a superfície Shopify; não decide preço.

## Workers

1. Shopify Surface Mapper
2. Price/Promo Change Controller
3. Preview/Diff Builder
4. Rollback/Risk Reviewer
5. Readback/Receipt Verifier — após execução aprovada

## Entrada obrigatória

- Fonte/decisão aprovada:
- Produtos/handles:
- Variant IDs/SKUs/tamanhos:
- Preço atual:
- Novo price:
- Novo compare-at price, se houver:
- Início/fim da promoção, se aplicável:
- Tiny/feed/app pode sobrescrever preço? sim/não/desconhecido:

## Fluxo

1. **Mapear alvos exatos**
   - Produto, variant ID, SKU, tamanho.
   - Confirmar que não é bulk aberto.

2. **Snapshot antes**
   - price/compare-at atual por variant.
   - status do produto.
   - tags/metafields promocionais envolvidos, se houver.

3. **Preview de alteração**
   - Linha por variante: atual → novo.
   - Campos escritos: price, compareAtPrice, tags/metafields/status apenas se listados.
   - O que não muda: estoque, disponibilidade, campanha, status, Tiny, GMC.

4. **Risco/rollback**
   - Risco de overwrite por feed/Tiny/app.
   - Rollback linha por linha para preço anterior.
   - Janela de execução recomendada.

5. **Readback pós-write**
   - Ler cada variant ID.
   - Comparar com packet aprovado.
   - Emitir receipt com antes/depois e divergências.

## Bloqueios

- Sem lista exata de variantes = bloquear.
- Sem fonte/decisão aprovada = bloquear.
- Estoque/disponibilidade/Tiny/campanha não entram automaticamente.
- Promo em massa exige packet próprio e amostragem/readback ampliado.

## Aprovação sugerida

> Aprovo LK Shopify alterar exclusivamente price/compare-at das variantes listadas no packet [IDs/SKUs], de [antes] para [depois], com snapshot, readback e rollback. Não aprovo estoque, status, Tiny, campanha, tags/metafields ou outros produtos fora da lista.
