# Receipt — LK estoque via Telegram + WhatsApp responder

Data: 2026-05-26
Owner: LK Ops / Atendimento
Status: implementação local/read-only concluída; ativação/restart de WhatsApp não executado nesta etapa

## Pedido limpo

Lucas pediu para implementar agilidade nas pesquisas de estoque no Telegram e nos grupos de WhatsApp, usando o Tiny como fonte do estoque real da LK.

## Fonte de verdade confirmada

- Estoque real: Tiny, depósito `LK | CONTROLE ESTOQUE`.
- Shopify: catálogo/evento/superfície, não fonte final de disponibilidade.
- Respostas de estoque devem ser por produto/SKU/tamanho e sempre com ressalva: sem reserva, sem alteração de estoque, sem promessa de preço/prazo/entrega.

## O que foi feito

- Verificado PRD existente: `areas/lk/projetos/lk-whatsapp-hermes-team-atendimento-prd-2026-05-17.md`.
- Verificado responder operacional: `/opt/data/scripts/lk_hermes_whatsapp_responder.py`.
- Confirmado que o responder já usa `tiny_stock_resolver_v2()` com Tiny read-only, paginação, variações e `LK | CONTROLE ESTOQUE`.
- Adicionado caminho local/manual para Telegram:
  - função `answer_for_cli()`;
  - flags `--ask`, `--stock-only`, `--json-output`;
  - objetivo: permitir que Hermes prepare resposta de estoque no Telegram usando o mesmo resolver do WhatsApp, sem enviar WhatsApp e sem criar Notion.
- Criado teste de regressão garantindo que `answer_for_cli(..., stock_only=True)` não chama `send_text` e mantém fonte/guardrails.
- Atualizada referência do skill `lk-shopify-readonly` com o uso do CLI para Telegram.

## Comando de uso Telegram/manual

```bash
python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py \
  --ask '@Hermes tem U9060WHT 38?' \
  --stock-only \
  --json-output
```

## Verificação

- `python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/tests/test_lk_whatsapp_assisted_sale.py`: OK.
- `python3 -m unittest /opt/data/tests/test_lk_whatsapp_assisted_sale.py -v`: 4 testes OK.
- `python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --selftest`: OK; wacli `hermes` autenticado e grupos-alvo conhecidos.
- `--ask '@Hermes tem Onitsuka 38?' --stock-only --json-output`: retornou resposta stock-only com fonte Tiny/LK Controle Estoque e guardrail; nenhum envio WhatsApp executado.

## Runtime WhatsApp

- Processo local detectado: `python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --port 8787`.
- `wacli --account hermes sync --follow ... --webhook http://127.0.0.1:8787/wacli` ativo.
- O processo do WhatsApp não foi reiniciado nesta etapa, porque a mudança adicionada é o caminho CLI/Telegram e não altera a lógica do servidor já rodando.

## Bloqueios mantidos

- Nenhuma alteração em Tiny.
- Nenhuma alteração em Shopify.
- Nenhum envio WhatsApp iniciado por esta tarefa.
- Nenhuma reserva, preço, prazo, desconto, compra ou contato externo prometido.
- Nenhum cron/gateway/profile criado ou alterado.

## Próximo passo sugerido

Se Lucas quiser que a nova capacidade também fique acoplada automaticamente ao Telegram runtime principal ou que o WhatsApp seja reiniciado para carregar qualquer mudança futura, preparar aprovação escopada com rollback antes de restart/produção.
