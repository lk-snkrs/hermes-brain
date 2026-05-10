# Rotina — LK Pareto-Compatible Monthly Reconciliation

## Status

Ativa como metodologia de conferência a partir de 2026-05-10.

## Objetivo

Quando Lucas enviar ou citar relatório mensal do Maicon/Pareto, reconciliar os números da LK em dois modos:

1. **Pareto-compatible** — reproduz a lógica/naming da Pareto para conferir se os números estão próximos o suficiente.
2. **Lucas-operacional** — consolida aliases por pessoa e cruza Shopify/produto/SKU/tamanho para decisão interna.

## Regra de tolerância

Lucas validou que a conferência não precisa ser 100,00% idêntica quando a metodologia está correta. Aderência de **99%+** e diferenças pequenas de poucos reais são operacionalmente aceitáveis.

Não gastar energia tentando zerar centavos/reais pequenos se:

- a conta Meta está correta;
- a janela está correta;
- a métrica canônica está correta;
- a diferença vem de rounding, naming, anúncios sem conversão ou recorte CSV/PDF.

## Fonte Meta correta

- Conta: `act_1242062509867163`.
- Nível: `ad`.
- Período: mês fechado do relatório.
- Métrica de compra/valor: uma action canônica por anúncio, preferindo `offsite_conversion.fb_pixel_purchase`.
- Nunca somar `purchase`, `omni_purchase` e `offsite_conversion.fb_pixel_purchase` como se fossem compras distintas.

## Naming Pareto-compatible

No modo Pareto-compatible, seguir o agrupamento/naming do relatório/CSV da Pareto, mesmo quando a leitura gerencial puder consolidar depois.

Regras conhecidas:

- **Maria**, **Maria Fernanda** e **Mariah** devem ficar separadas.
- A regra ampla `maria` não pode engolir `maria fernanda` nem `mariah`.
- Helena pode aparecer separada em blocos Pareto, como `Helena` e `Helena 4 camp. abril`; consolidar apenas na visão Lucas-operacional.
- Silvia deve seguir o naming CSV/Pareto no modo compatible; aliases ampliados demais podem capturar criativos/campanhas que não entraram no recorte Pareto.
- Lala pode ter pequena diferença de spend/ad count por anúncios late-month/zero-conversion; compras e receita são mais importantes para a conferência.

## Shopify

Shopify é fonte de verdade para pedido, produto, SKU, tamanho e receita por produto quando há ponte segura.

Para bater receita total mensal do PDF Pareto, não assumir que Shopify Admin `total_price` é a mesma métrica. Na auditoria de abril/2026:

- PDF Pareto: `233 pedidos`, `R$ 722.636,36`.
- Shopify Admin API: `233 pedidos web pagos/parcialmente reembolsados`, mas `R$ 772.659,42` em `total_price`.

Conclusão: pedidos bateram; receita provavelmente usa Shopify Analytics, GA4 ou métrica líquida ajustada.

## Abril/2026 — auditoria base

Ver relatório versionado:

```text
reports/lk-pareto-april-2026/reconciliation-audit.md
```

Meta global abril bateu exatamente:

- Investimento: `R$ 38.954,76`.
- Compras: `229`.
- Valor Meta: `R$ 797.654,65`.
- ROAS: `20,48`.
- CPA: `R$ 170,11`.

## Criativos

Não usar `thumbnail_url` 64×64 do Meta em e-mails/relatórios LK.

Criativos em relatório LK só entram quando houver uma fonte nítida e segura:

1. screenshot validado do endpoint `/AD_ID/previews`;
2. asset exportado/fornecido pela Pareto/Maicon;
3. mídia real via Page/Instagram com permissão suficiente;
4. ou contact sheet/auditoria visual separada.

Todo layout visual precisa seguir DesignMD LK.
