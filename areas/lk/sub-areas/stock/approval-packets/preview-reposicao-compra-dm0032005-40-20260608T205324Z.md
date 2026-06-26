# Preview — reposição/compra `DM0032005-40` sem envio

Data UTC: 2026-06-08T20:53:24Z
Dono: `[LK] Estoque Loja Física` / `lk-stock`
Escopo aprovado por Lucas: **preparar preview de reposição/compra para `DM0032005-40`, sem enviar e sem write Tiny/Shopify**.
Status: **SUPERSEDED — não usar para execução. A recomendação de 4 unidades usou demanda de fixture/teste (`shopify_fixture`) e não blend/venda real. Ver rollback `areas/lk/sub-areas/stock/receipts/lk-stock-rollback-wrong-p0-fixture-blend-dm0032005-40-20260608T211459Z.md`. Nenhuma ação externa foi executada.**

## Item

- Produto: `Tênis Air Max Plus Black University Blue Preto`
- SKU/tamanho: `DM0032005-40 / 40`
- Tiny código: `DM0032005-40`
- Tiny id: `937674228`
- Shopify variant legacy ID: `44265045295326`
- Shopify handle: `air-max-plus-black-university-blue`
- Situação Tiny: `A`
- Preço Tiny cadastrado: `1999.99` *(preço de cadastro/consulta, não custo de compra)*

## Fonte e motivo

- Fonte viva Tiny read-only reconfirmada em: `2026-06-08T20:46:20Z`
- Depósito avaliado: `LK | CONTROLE ESTOQUE`
- Saldo oficial no depósito: `0.0`
- `desconsiderar`: `N`
- Mapping Shopify/Tiny: `high`, 1 match exato Shopify + 1 match exato Tiny
- Score Gate C: `P0`, score `21.0`
- Demanda local usada: `6.0` unidades em 30 dias
- Risco: venda perdida por estoque zerado no tamanho 40

## Sugestão de quantidade

Cálculo local de cobertura:

- Vendas 30d: `6.0`
- Média diária: `0.2`
- Cobertura mínima proposta: `15` dias
- Necessidade mínima calculada: `3` unidades
- Buffer P0 por estoque zerado: `+1` unidade

**Recomendação para decisão:** comprar/repor **4 unidades** do tamanho `40`.

Faixa segura:

- Mínimo: `3` unidades para cobrir ~15 dias.
- Recomendado: `4` unidades por ser P0 e estoque zerado.
- Teto de teste: `6` unidades, equivalente ao volume observado em 30 dias.

## Preview de mensagem interna / fornecedor

> Olá. Preciso verificar disponibilidade para reposição do item abaixo:
>
> - Produto: Tênis Air Max Plus Black University Blue Preto
> - SKU/código: DM0032005-40
> - Tamanho: 40
> - Quantidade desejada: 4 unidades
> - Motivo: tamanho 40 zerado no depósito LK | CONTROLE ESTOQUE e com venda/demanda recente.
>
> Pode confirmar disponibilidade, prazo e condição?

## Preview de decisão interna LK

> Recomendo abrir reposição/compra de 4 unidades do SKU `DM0032005-40` tamanho `40`.
> Evidência: Tiny `LK | CONTROLE ESTOQUE` confirmou saldo `0`, demanda local 30d `6` unidades, Gate C `P0`.
> Antes de qualquer envio/compra/write, aprovar canal, fornecedor/destino, quantidade final e rollback/receipt.

## Guardrails

- Mensagem **não enviada**.
- Compra **não executada**.
- Fornecedor **não contatado**.
- Tiny write: `0`.
- Shopify write: `0`.
- Reserva/promessa ao cliente: `0`.
- Cron/runtime novo: `0`.

## Aprovação para executar depois

Se quiser executar, aprovar com escopo completo, por exemplo:

```text
Aprovo enviar o preview de reposição do DM0032005-40 para [fornecedor/canal], quantidade 4, sem write Tiny/Shopify, e registrar receipt.
```

Ou ajuste a quantidade/canal antes da execução.
