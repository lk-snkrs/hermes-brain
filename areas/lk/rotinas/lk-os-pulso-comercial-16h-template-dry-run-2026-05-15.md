# LK OS — Pulso Comercial 16h Template + Dry-run

Gerado em: `2026-05-15T09:43:30.432123+00:00`
Status: `template_and_dry_run_only`
Modo: read-only/local; sem cron/envio/write.

## Veredito

- Criei o formato operacional do **Pulso Comercial 16h** para LK OS.
- Este artefato não ativa cron e não envia mensagem automática.
- O dry-run usa snapshot local disponível; a base Shopify local está defasada, com último pedido em `2026-04-16T20:13:58+00:00`, então os números abaixo são validação de formato, não pulso comercial real de hoje.

## Contrato do Pulso Comercial 16h

Objetivo: responder no meio/fim da tarde se o dia precisa de intervenção comercial leve, sem virar dump de dados.

### Fontes esperadas

- `fact_shopify`: pedidos, receita, canal online/POS, produtos vendidos no dia.
- `fact_ga4`: tráfego e conversão do dia, se disponível.
- `fact_tiny_stock`: estoque operacional por SKU/tamanho; enquanto Tiny snapshot estiver parcial, rotular como parcial.
- `platform_signal`: Meta/Google/Metricool/Klaviyo apenas como sinal, não receita operacional.
- `derived_reconciliation`: leitura Hermes cruzando venda, tráfego e estoque.

### Template Telegram

```text
LK Pulso 16h — [data BRT]
Status: [verde/amarelo/vermelho]

1. Vendas até agora
- Receita: R$ [x] ([online/POS])
- Pedidos: [x]
- Ticket médio: R$ [x]

2. Produtos/SKUs que importam
- Top vendidos: [produto — tamanho — SKU — receita]
- Atenção estoque: [SKU/tamanho com risco ou Tiny parcial]

3. Tráfego/conversão
- Sessões/conversão: [GA4 se fresco; senão indisponível]
- Sinal mídia: [platform_signal, sem chamar de venda real]

4. Ação recomendada
- [nenhuma ação | olhar PDP | reforçar story/manual | preparar sourcing | aguardar fechamento do dia]

Não executado
- Sem campanha, WhatsApp, Klaviyo, preço, estoque, Shopify/Tiny/Merchant write, fornecedor ou compra.
```

## Dry-run com snapshot local

- Último dia BRT disponível no snapshot: `2026-04-16`
- Receita do último dia disponível: `R$ 11,209.97`
- Pedidos do último dia disponível: `6`
- Online/POS no último dia: `5` / `1`
- Receita últimos 7 dias disponíveis: `R$ 287,590.24`
- Pedidos últimos 7 dias disponíveis: `93`

### Top itens do último dia disponível

- Tênis Onitsuka Tiger Mexico 66 SD Cream Peacoat Navy Red Bege — 34; SKU `1183A872.101-1`; qtd `1`; receita `R$ 2,499.99`
- Tênis Onitsuka Tiger Mexico 66 Gold White Dourado — 38; SKU `1183B566.201-5`; qtd `1`; receita `R$ 2,399.99`
- Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege — 38; SKU `1183C123.252-5`; qtd `1`; receita `R$ 2,199.99`
- Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege — 40; SKU `1183C123.252-7`; qtd `1`; receita `R$ 2,199.99`
- Tênis Adidas Samba Disney 101 Dalmatians Penny Branco — 35; SKU `KJ5990-2`; qtd `1`; receita `R$ 1,999.99`
- Structured Classic Ball Cap Script Lululemon Verde Musgo; SKU `sem SKU`; qtd `1`; receita `R$ 599.99`

## Estoque / Data Quality

- Tiny snapshot ativo: `tiny_stock_20260515T092206Z`
- Status Tiny: `partial_api_rate_limited`
- Estoques Tiny consolidados: `314` de `17605` produtos listados
- Conclusão: o Pulso 16h pode mostrar risco de estoque apenas como `fact_tiny_stock_partial` até o snapshot completar.

## Gatilhos de status

- **Verde:** vendas dentro do esperado, sem falha de API, sem SKU P1 crítico novo.
- **Amarelo:** vendas abaixo do ritmo, GA4 sem dado, Tiny parcial em SKU vendido, ou produto P1 com estoque incerto.
- **Vermelho:** falha de pagamento/canal, queda brusca de tráfego/conversão, produto P1 vendido com risco operacional confirmado, ou erro de API que bloqueia decisão.

## O que não foi feito

- cron_creation
- telegram_scheduled_send
- shopify_write
- tiny_write
- merchant_write
- klaviyo_send
- whatsapp_send
- supplier_contact
- purchase

## Próximo passo

- Se aprovado futuramente, transformar este template em rotina `no_agent`/cron ou comando sob demanda **somente depois** de reconciliar dados frescos e contrato de entrega.
- Agora ele fica como template/dry-run P1 concluído, sem entrega automática.
