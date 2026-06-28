# PRD / Approval Packet — PDP Product Suggestions v3 — Motor LK

- Data/hora: 2026-06-27T10:12:16Z
- Agente/profile: lk-shopify
- Área: LK / Shopify / PDP CRO
- Superfície: PDP `Você também pode gostar` / `Relacionados`
- Status: aprovado por Lucas para avançar em especificação/handoff; sem write externo executado neste documento
- Referências históricas verificadas:
  - `areas/lk/sub-areas/shopify/approval-packets/pdp-product-suggestions-v2-dev-20260626.md`
  - `areas/lk/sub-areas/shopify/receipts/pdp-product-suggestions-v2-production-merge-20260626.md`
  - `areas/lk/sub-areas/shopify/reports/2026-06-25-cart-drawer-cross-sell-xy-readonly-packet-v0.md`

## Pedido aprovado

Lucas perguntou se o LK Stock já tinha a base para o ranking e aprovou a evolução proposta após a distinção entre:

- `lk-stock` como dono de elegibilidade operacional;
- Shopify/Growth/CRO como dono do ranking visual do PDP;
- Curadoria LK como camada editorial/família/variante;
- Shopify Recommendations API como fonte automática filtrada, mas não autoridade final.

## Problema

O Product Suggestions v2 já removeu o erro estrutural de depender de `product.collections.first` e passou a usar:

```text
Shopify Recommendations API filtrada
+ fallback Liquid estrito
+ dedupe contra Curadoria LK quando detectável
```

Mas ainda não é um motor proprietário LK. Em alguns PDPs, a API retorna candidatos fracos ou sem densidade suficiente. Exemplo histórico: `ALD Saint George Bege/Marrom` ficou dependente de fallback porque a API trazia duplicatas/cross-type.

## Objetivo v3

Criar um **Product Suggestion Service LK** para ordenar recomendações do PDP por relevância comercial/editorial, sem transformar estoque em motor visual e sem prometer disponibilidade.

Resultado esperado:

```text
PDP produto X
→ candidatos por Curadoria LK / família / silhueta
→ candidatos por Recommendations API
→ candidatos por histórico agregado de co-compra/sequência, quando houver
→ elegibilidade operacional fornecida pelo lk-stock como filtro/contrato
→ regras de bloqueio cross-type
→ top 4 sugestões coerentes ou esconder bloco se fraco
```

## Donos por camada

| Camada | Dono natural | Papel no v3 |
|---|---|---|
| Curadoria LK / família / cápsula | LKGOC + Shopify | Agrupamento editorial, variações e famílias como ALD hats, AJ1 Low, Mexico 66 |
| Ranking PDP / render / fallback | lk-shopify + Growth/CRO | Ordenar, deduplicar, renderizar e medir qualidade do bloco |
| Estoque/disponibilidade/elegibilidade operacional | lk-stock | Informar se candidato pode entrar como elegível; nunca usado como score principal sem contrato |
| Co-compra / compra sequencial | lk-shopify/Growth com dados agregados; validar com Stock quando necessário | Sinal probabilístico X→Y, confidence/lift/support/recency |
| Shopify Recommendations API | Shopify | Fonte de candidatos, não autoridade final |

## Requisitos funcionais

1. Excluir sempre o produto atual.
2. Excluir itens já exibidos na Curadoria LK quando detectável.
3. Bloquear cross-type ruim:
   - boné não recomenda tênis;
   - camiseta não entra como variação de boné;
   - acessórios só entram quando a regra permitir cross-sell explícito.
4. Renderizar até 4 cards.
5. Esconder o bloco se houver menos de 2 candidatos confiáveis.
6. Usar sinais de ranking nesta ordem inicial:
   - match de família/silhueta/cápsula;
   - co-compra X→Y quando houver support mínimo;
   - compra sequencial 30/90/180 dias quando houver sinal agregado;
   - Recommendations API filtrada;
   - fallback Liquid estrito.
7. Separar `score` de `eligibility`:
   - disponibilidade/vendável é filtro;
   - não vira ranking principal por si só.
8. Output deve ser auditável por handle com reason codes.

## Contrato de dados proposto

Artefato gerado por rotina read-only/agregada:

```json
{
  "schema_version": 1,
  "generated_at": "ISO-8601",
  "by_handle": {
    "produto-x": [
      {
        "handle": "produto-y",
        "score": 87,
        "reason_codes": ["same_family", "copurchase_xy"],
        "confidence": 0.23,
        "lift": 2.1,
        "support": 11,
        "eligibility": "eligible_or_unknown"
      }
    ]
  },
  "by_family": {
    "ald-hats": [
      {"handle": "bone-ald-exemplo", "score": 82, "reason_codes": ["same_family"]}
    ]
  }
}
```

## Handoff para LK Stock

Solicitação ao `lk-stock` / Stock OS: responder **somente sobre elegibilidade operacional e campos disponíveis**, sem o lk-shopify consultar estoque diretamente.

Perguntas para o `lk-stock`:

1. Quais campos confiáveis existem para produto ativo/vendável?
2. Existe classificação operacional de família/cor/silhouette que pode ser compartilhada como metadado, sem expor estoque bruto?
3. Existe endpoint/arquivo/relatório para elegibilidade por handle/SKU com status sanitizado (`eligible`, `ineligible`, `unknown`, `needs_reconciliation`)?
4. Existe histórico agregado de co-compra ou sequência de compra no Stock OS, ou isso deve ficar em LK Shopify/Growth?
5. Quais caveats impedem usar determinado produto como candidato de PDP?

## Fora de escopo nesta aprovação

- Nenhum write Shopify/theme/Production.
- Nenhuma consulta direta de estoque por lk-shopify.
- Nenhuma alteração de preço, estoque, disponibilidade, checkout, Tiny, GMC, Klaviyo, ads, WhatsApp ou campanhas.
- Nenhuma promessa de disponibilidade.
- Nenhuma alteração no v2 publicado sem approval packet específico.

## Risco

| Risco | Nível | Mitigação |
|---|---:|---|
| Recomendação incoerente por regra fraca | Médio | reason codes + hide-if-weak + QA por amostra |
| Duplicar Curadoria LK | Médio | dedupe por handles `.lk-variante` detectáveis |
| Confundir estoque com recomendação | Alto | contrato: Stock só elegibilidade, não ranking visual |
| Dados de co-compra insuficientes | Médio | fallback por família/silhueta + API filtrada |
| Expor PII de pedidos/clientes | Alto | somente agregados; sem IDs, nomes, emails, telefones |

## Critérios de aceite do packet v3 read-only

Antes de qualquer DEV/theme write:

- [ ] Handoff Stock respondido ou marcado como `não confirmado`.
- [ ] Dataset agregado sem PII.
- [ ] Amostra mínima de PDPs validada:
  - ALD Saint George / bonés;
  - Air Jordan 1 Low;
  - Onitsuka Mexico 66;
  - New Balance 9060/530;
  - apparel/acessório para testar bloqueio cross-type.
- [ ] Top 4 por PDP com reason codes.
- [ ] Lista de bloqueios/caveats.
- [ ] Approval packet DEV separado com diff pretendido, QA e rollback.

## Rollback futuro

Se v3 for implementado em DEV/Production futuramente:

1. Reverter para Product Suggestions v2 publicado via PR/commit da época.
2. Remover leitura do artefato v3 e manter Recommendations API filtrada + fallback Liquid.
3. Se o artefato JSON falhar, tema deve esconder ou cair para v2, nunca mostrar lista genérica ampla.

## Próxima decisão

A próxima etapa segura é **read-only**:

> Produzir o packet v3 read-only com matriz de candidatos/reason codes e handoff do `lk-stock` sobre elegibilidade operacional, sem write Shopify/Production.
