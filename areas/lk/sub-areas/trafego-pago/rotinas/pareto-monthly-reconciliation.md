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

## Correção conceitual — Meta não é venda real

O PDF Pareto chama o campo do Meta de `Receita`, mas a leitura correta para LK é:

- `R$ 722.636,36` = venda/receita e-commerce do negócio no mês, segundo Pareto/Shopify/analytics.
- `R$ 797.654,65` = valor de conversão **atribuído pelo Meta Ads Manager**, não venda real da LK.

Como o valor atribuído pelo Meta ultrapassa a receita total do e-commerce em `R$ 75.018,29`, ele não pode ser descrito como “a Meta vendeu R$ 797 mil”. A frase correta é: **o Meta atribuiu R$ 797.654,65 no gerenciador**.

Isso pode acontecer por janela de atribuição, sobreposição com outros canais, deduplicação imperfeita, diferença entre plataformas e GA4/Shopify e regras do pixel. O próprio PDF alerta que há diferenças de atribuição entre plataformas e GA4.

## Fonte Meta correta

- Conta: `act_1242062509867163`.
- Nível: `ad`.
- Período: mês fechado do relatório.
- Métrica de compra/valor: uma action canônica por anúncio, preferindo `offsite_conversion.fb_pixel_purchase`.
- Nome do campo em relatórios LK: `valor atribuído Meta` ou `valor de conversão no gerenciador`, nunca `venda da Meta`.
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

## Script operacional

Use:

```bash
/opt/hermes/.venv/bin/python scripts/lk_monthly_pareto_reconciliation.py --month 2026-04
```

O script gera `.md` e `.json` em:

```text
/opt/data/lk_monthly_pareto_reconciliation_reports/
```

Ele consulta Meta Ads direto, nível `ad`, usa compra/valor canônicos e gera duas leituras:

- `Pareto-compatible`: naming/lógica Pareto, incluindo Marias separadas.
- `Lucas-operacional`: aliases consolidados para decisão interna.

## Abril/2026 — auditoria base

Ver relatórios versionados:

```text
reports/lk-pareto-april-2026/reconciliation-audit.md
reports/lk-pareto-april-2026/pareto-compatible-script-output.md
```

Meta global abril bateu exatamente com o campo Meta/Ads Manager da Pareto, mas agora com nomenclatura corrigida:

- Investimento: `R$ 38.954,76`.
- Compras atribuídas no gerenciador: `229`.
- Valor atribuído Meta no gerenciador: `R$ 797.654,65`.
- Receita/venda e-commerce Pareto: `R$ 722.636,36`.
- ROAS Meta atribuído: `20,48`.
- CPA Meta atribuído: `R$ 170,11`.

## Criativos

Não usar `thumbnail_url` 64×64 do Meta em e-mails/relatórios LK.

Criativos em relatório LK só entram quando houver uma fonte nítida e segura:

1. screenshot validado do endpoint `/AD_ID/previews`;
2. asset exportado/fornecido pela Pareto/Maicon;
3. mídia real via Page/Instagram com permissão suficiente;
4. ou contact sheet/auditoria visual separada.

Todo layout visual precisa seguir DesignMD LK.
