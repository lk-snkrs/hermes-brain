# Correção — WhatsApp LK venda assistida Onitsuka

Data: 2026-05-26

## Pedido

Corrigir a resposta para:

`@Hermes cliente quer Onitsuka 38, o que temos?`

## Diagnóstico

O responder classificava corretamente como venda assistida e extraía:

- termo: `onitsuka`
- tamanho: `38`

A falha estava na busca fallback do Tiny: para termos amplos de marca, o Tiny retorna muitas páginas e os primeiros resultados podem ser acessórios/camisetas antes dos tênis por tamanho. O código só olhava a primeira página, então não alcançava variantes de tênis Onitsuka com estoque.

## Correção

- A busca read-only no Tiny agora pagina uma janela limitada de resultados para termos amplos.
- Quando não encontra o tamanho exato, o fallback filtra opções com numeração de calçado e ordena por proximidade do tamanho pedido.
- Mantido guardrail: sem reserva, sem compra, sem alteração Shopify/Tiny e sem promessa ao cliente.

## Validação

- Teste de regressão criado em `/opt/data/tests/test_lk_whatsapp_assisted_sale.py`.
- `python3 -m unittest /opt/data/tests/test_lk_whatsapp_assisted_sale.py -v`: OK.
- `python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --selftest`: OK.
- Consulta real read-only retornou opção Onitsuka tamanho 38 com saldo no Tiny.
- Responder local reiniciado na porta 8787.
- Health webhook local: `200 ok`.

## Resultado esperado

A pergunta agora responde com opção interna em estoque, por exemplo:

- Tênis Onitsuka Tiger Mexico 66 Beige Grass Green Marrom — tamanho 38 — SKU `1183C102250-5` — saldo 1 par.

Usar como sugestão interna; validar antes de promessa comercial sensível.
