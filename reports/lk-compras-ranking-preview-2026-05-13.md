# LK Compras — Ranking Preview v1

Status: `read_only_sanitized_ranking_preview_ready`
Data: 2026-05-13T06:05:01.090056+00:00
Fonte: `platform_signal_wacli_local` (`lk-compras`) a partir da Signal Queue v1.

## Veredito

Criei um preview de ranking local/sanitizado para priorizar sinais de compra por produto/tamanho/preço/logística. Isto ainda é sinal de WhatsApp, não fato de compra, estoque ou fornecedor validado.

## Resumo técnico

- Mensagens reprocessadas: 1000.
- Clusters candidatos: 33.
- Top candidatos no preview: 25.
- Critério: volume + pedido/resposta/negociação/preço/logística/fechamento + presença de produto/tamanho.
- Sem nomes, telefones, JIDs ou texto literal de mensagens.

## Top candidatos sanitizados

### 1. Ranking `9b875420b618` — score 170

- Produto/hint: `produto_nao_identificado`.
- Tamanhos detectados: não identificado.
- Preço detectado: R$ 402.
- Logística: prazo, proximidade_sp, envio/transportadora.
- Classes: proximidade_sp_logistica=14, produto_tamanho_estoque=12, resposta_fornecedor=9, pedido_de_compra=8, negociacao_preco=7, fechamento_compra=5.
- Próximo passo recomendado: `rank_cheapest_vs_closer_to_sp`.
- Evidência: 6 IDs sanitizados; chat_hash `487148e1e3`; última msg `2026-05-13T00:28:22Z`.

### 2. Ranking `22d9073eb321` — score 42

- Produto/hint: `on`.
- Tamanhos detectados: não identificado.
- Preço detectado: sem preço detectado.
- Logística: proximidade_sp, prazo.
- Classes: pedido_de_compra=3, proximidade_sp_logistica=2, produto_tamanho_estoque=2, resposta_fornecedor=2, negociacao_preco=2.
- Próximo passo recomendado: `validate_product_size_stock_context`.
- Evidência: 6 IDs sanitizados; chat_hash `487148e1e3`; última msg `2026-05-12T23:34:14Z`.

### 3. Ranking `9fa6fcca3f5c` — score 26

- Produto/hint: `produto_nao_identificado`.
- Tamanhos detectados: não identificado.
- Preço detectado: R$ 301.
- Logística: retirada/motoboy, envio/transportadora.
- Classes: proximidade_sp_logistica=6, produto_tamanho_estoque=1, pedido_de_compra=1.
- Próximo passo recomendado: `rank_cheapest_vs_closer_to_sp`.
- Evidência: 6 IDs sanitizados; chat_hash `147b539713`; última msg `2026-05-12T16:07:15Z`.

### 4. Ranking `75a074e8a348` — score 18

- Produto/hint: `on / preto`.
- Tamanhos detectados: não identificado.
- Preço detectado: R$ 328–2.810.
- Logística: sem sinal logístico claro.
- Classes: pedido_de_compra=2, fechamento_compra=2.
- Próximo passo recomendado: `compare_price_options`.
- Evidência: 2 IDs sanitizados; chat_hash `e102c1e25a`; última msg `2026-05-13T00:56:57Z`.

### 5. Ranking `240fe97f105a` — score 15

- Produto/hint: `produto_nao_identificado`.
- Tamanhos detectados: não identificado.
- Preço detectado: sem preço detectado.
- Logística: prazo, retirada/motoboy.
- Classes: proximidade_sp_logistica=3, resposta_fornecedor=1.
- Próximo passo recomendado: `needs_manual_context_or_ignore`.
- Evidência: 4 IDs sanitizados; chat_hash `92daa92b55`; última msg `2026-05-12T15:42:20Z`.

### 6. Ranking `2966fb126679` — score 14

- Produto/hint: `new balance / on`.
- Tamanhos detectados: 38.
- Preço detectado: R$ 2.026–9.060.
- Logística: sem sinal logístico claro.
- Classes: pedido_de_compra=1, negociacao_preco=1.
- Próximo passo recomendado: `compare_price_options`.
- Evidência: 1 IDs sanitizados; chat_hash `e102c1e25a`; última msg `2026-05-12T16:21:00Z`.

### 7. Ranking `df81698be946` — score 14

- Produto/hint: `adidas / samba`.
- Tamanhos detectados: 34, 44.
- Preço detectado: R$ 1.900–2.026.
- Logística: sem sinal logístico claro.
- Classes: pedido_de_compra=1, negociacao_preco=1.
- Próximo passo recomendado: `compare_price_options`.
- Evidência: 1 IDs sanitizados; chat_hash `e102c1e25a`; última msg `2026-05-12T00:44:57Z`.

### 8. Ranking `025b787bc9f6` — score 14

- Produto/hint: `nike / air force`.
- Tamanhos detectados: 40.
- Preço detectado: R$ 1.999–2.999.
- Logística: sem sinal logístico claro.
- Classes: pedido_de_compra=1, negociacao_preco=1.
- Próximo passo recomendado: `compare_price_options`.
- Evidência: 1 IDs sanitizados; chat_hash `e102c1e25a`; última msg `2026-05-12T00:33:57Z`.

### 9. Ranking `9618b1952269` — score 14

- Produto/hint: `on / white`.
- Tamanhos detectados: 38.
- Preço detectado: R$ 2.026–4.799.
- Logística: sem sinal logístico claro.
- Classes: pedido_de_compra=1, negociacao_preco=1.
- Próximo passo recomendado: `compare_price_options`.
- Evidência: 1 IDs sanitizados; chat_hash `e102c1e25a`; última msg `2026-05-11T22:15:31Z`.

### 10. Ranking `14c00463aea4` — score 13

- Produto/hint: `on / white`.
- Tamanhos detectados: 39.
- Preço detectado: R$ 566–5.090.
- Logística: sem sinal logístico claro.
- Classes: pedido_de_compra=1, fechamento_compra=1.
- Próximo passo recomendado: `compare_price_options`.
- Evidência: 1 IDs sanitizados; chat_hash `e102c1e25a`; última msg `2026-05-12T22:47:56Z`.

## Como usar operacionalmente

1. Confirmar produto/tamanho exato no contexto privado antes de qualquer ação.
2. Se houver preço + logística, comparar menor preço viável versus fonte mais próxima de São Paulo quando a diferença for pequena.
3. Se virar compra humana, preparar somente um preview de lançamento Notion; write no Notion exige aprovação separada.

## Não executado

- Nenhum WhatsApp enviado.
- Nenhum contato com fornecedor/grupo/cliente.
- Nenhuma compra, reserva, pagamento ou escolha final de fornecedor.
- Nenhum write em Notion, Shopify, Tiny, banco, Klaviyo, Meta, Google ou n8n.
- Nenhum cron/automação recorrente criado.

## Próximo seguro

A próxima evolução é uma calibragem read-only mais precisa por janela de 24h/7d, com amostras privadas e regras melhores de extração de modelo, tamanho, preço e distância logística. Qualquer envio, compra, contato ou Notion write continua bloqueado até aprovação explícita com payload inline.
