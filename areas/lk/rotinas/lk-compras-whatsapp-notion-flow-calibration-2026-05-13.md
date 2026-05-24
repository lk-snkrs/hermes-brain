# LK Compras — WhatsApp → Compra → Notion Calibration

Status: `read_only_calibration_started`
Data: 2026-05-13
Escopo: LK Sneakers / LK OS / wacli / WhatsApp Business LK Compras / Notion
Fonte: `platform_signal` local wacli (`lk-compras`), leitura sanitizada.

## Correção Lucas registrada

O sistema correto é **Notion**, não Noxon.

Fluxo normal de compras LK:

1. LK manda um pedido de compra.
2. Alguém responde com disponibilidade/preço/logística.
3. A LK escolhe:
   - o menor preço viável; ou
   - a opção mais perto de São Paulo quando a diferença de preço não for muito grande.
4. A compra é feita por humanos.
5. A compra é lançada no Notion.

## Calibragem inicial read-only

Leitura local/sanitizada realizada sobre as últimas 1.000 mensagens sincronizadas do `lk-compras`.

Snapshot técnico:

- Chats no store: 50.
- Grupos no store: 34.
- Mensagens no store no momento: 4.210.
- Mensagens analisadas nesta passada: 1.000.
- Mensagens em grupos: 985.
- Mensagens em DMs: 15.
- Mensagens enviadas pela conta LK Compras: 19.
- Mensagens de terceiros/desconhecidas: 981.
- Chats únicos na amostra: 15.
- Mensagens com links: 9.
- Mensagens com mídia/anexo: 92.

Nenhum nome, telefone, JID ou texto literal de conversa foi publicado neste relatório.

## Sinais encontrados na amostra

- `pedido_de_compra`: 28.
- `resposta_fornecedor`: 17.
- `negociacao_preco`: 39.
- `proximidade_sp_logistica`: 30.
- `fechamento_compra`: 15.
- `produto_tamanho_estoque`: 23.
- `humano/ruido`: 8.

Interpretação: o canal `lk-compras` tem sinal operacional suficiente para virar fonte do LK OS, principalmente em negociação/preço, logística/proximidade SP, pedido/resposta e fechamento.

## Regra operacional aprendida

A decisão de compra não deve ser modelada só como “menor preço”. O roteador precisa calcular/registrar duas opções:

1. **Menor preço viável**.
2. **Melhor proximidade logística com São Paulo**, quando o delta de preço for pequeno.

Campo novo sugerido para fila LK OS:

```json
{
  "decision_basis": "cheapest|closer_to_sp_small_price_delta|human_override",
  "price_delta_vs_cheapest": null,
  "sp_proximity_signal": "near|far|unknown",
  "notion_logging_required_after_purchase": true
}
```

## Roteador LK Compras v1

1. Detectar pedido de compra.
2. Agrupar respostas por produto/tamanho/fornecedor.
3. Extrair sinais: preço, disponibilidade, prazo, local/proximidade SP, mídia/link.
4. Gerar ranking:
   - opção A: menor preço;
   - opção B: mais perto de SP se diferença pequena;
   - opção C: revisão humana se dados incompletos.
5. Preparar preview para Lucas/Júlio.
6. Após aprovação e compra humana, preparar lançamento no Notion.

## Guardrails

- Read-only/sanitizado nesta etapa.
- Nenhum WhatsApp enviado.
- Nenhuma resposta a fornecedor/grupo/cliente.
- Nenhuma compra/reserva/pagamento.
- Nenhum write em Notion.
- Nenhum write em Shopify, Tiny, Merchant, banco, Klaviyo, Meta, Google ou n8n.
- Dados brutos ficam privados em `/opt/data/hermes_bruno_ingest/local_sql/wacli_lk_compras/` com permissão restrita.

## Próximo bloco seguro

Criar o **classificador LK Compras v1** local/read-only:

- entrada: mensagens `lk-compras` já sincronizadas;
- saída: fila sanitizada de oportunidades por produto/tamanho/preço/logística;
- sem envio;
- sem Notion write;
- sem compra;
- sem texto literal em Telegram.

Depois, aprovar separadamente qualquer ação externa ou lançamento real em Notion.
