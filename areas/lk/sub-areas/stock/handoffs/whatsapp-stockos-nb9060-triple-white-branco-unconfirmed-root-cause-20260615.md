# Handoff — NB 9060 Triple White Branco 36 não confirmado no Stock OS

Data: 2026-06-15
Origem: LK Ops / Lucas Telegram
Dono seguinte: `lk-stock`

## Contexto
Lucas apontou a resposta:

> new balance 9060 triple white branco — Tamanho 36: não confirmado no Stock OS; validar/reconciliar com lk-stock.

Pedido: verificar motivo do erro.

## Achado operacional
Não foi uma conclusão de estoque zerado. Foi queda no caminho seguro de `não confirmado`, porque o responder WhatsApp/atendimento não pode consultar Tiny diretamente e só usa a superfície `LK Stock OS local DB (lk-stock)`.

O termo extraído pelo responder para esse item ficou literal:

- `new balance 9060 triple white branco`
- tamanho: `36`

O lookup atual em `lk_hermes_whatsapp_responder.py` faz busca `LIKE` literal em `sku`, `handle`, `title` ou `tiny_codigo` com filtro exato de tamanho. Se o Stock OS tiver o item como `New Balance 9060 Triple White`, outro handle/SKU, sem o sufixo `branco`, ou com identidade não resolvida, o item cai em `não confirmado`.

## Causa provável
Matcher/alias do Stock OS/responder está rígido demais para sinônimos de cor e título:

- `triple white branco` não gera fallback para `triple white`;
- não tenta alias/crosswalk por modelo `9060` + cor sem palavra extra;
- não aciona fallback Tiny read-only, porque LK Ops/WhatsApp não é dono de estoque; isso deve ser feito por `lk-stock`.

## Correção adicional — SKU informado por Lucas
Lucas informou que, neste caso, o SKU é `U9060NRJ`.

Conclusão operacional: sim, pelo SKU a chance de resolução é maior. O responder já extrai `U9060NRJ`, `U9060NRJ-36` e `9060` como termos quando o SKU aparece na pergunta. A falha anterior foi não pedir SKU/código interno quando a busca por nome não confirmou.

Correção local aplicada em `/opt/data/scripts/lk_hermes_whatsapp_responder.py`:

- respostas `não confirmado` agora dizem para pedir SKU/código interno quando o pedido veio só por nome/modelo;
- regressão em `/opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py` exige a frase `Peça SKU/código interno` e garante que Tiny continua fora do caminho de atendimento.

Verificação executada:

```bash
python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py && python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
```

Resultado: `ok`.

## Limite
Este handoff não afirma disponibilidade, quantidade, reserva ou falta do produto. Apenas explica por que o responder retornou `não confirmado` e registra a correção para pedir SKU/código interno.

## Próxima ação solicitada ao lk-stock
1. Verificar no Stock OS / fallback autorizado se o item `New Balance 9060 Triple White Branco`, tamanho `36`, possui identidade/alias correto.
2. Se existir, criar/ajustar alias/crosswalk para que buscas por:
   - `new balance 9060 triple white branco`
   - `new balance 9060 triple white`
   - `9060 triple white`
   resolvam para o mesmo item/tamanho.
3. Se Stock OS estiver incompleto, reconciliar conforme política do `lk-stock`.
4. Retornar evidência segura para atendimento, sem promessa automática ao cliente.

## Writes externos
0. Nenhuma consulta Tiny/Shopify write, nenhuma promessa ao cliente, nenhum envio WhatsApp.

## Reminder OS
loop needed: yes
owner: `lk-stock`
next action: reconciliar alias/identidade do NB 9060 Triple White Branco tamanho 36 no Stock OS.
review trigger: próxima pergunta de disponibilidade deste modelo ou revisão de aliases Stock OS.
