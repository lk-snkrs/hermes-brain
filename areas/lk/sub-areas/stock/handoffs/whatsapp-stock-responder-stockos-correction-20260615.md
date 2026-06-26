# Handoff — Correção WhatsApp estoque deve usar LK Stock OS

Data: 2026-06-15
Origem: Lucas / LK Ops Telegram
Dono seguinte: `lk-stock` + manutenção do responder WhatsApp LK

## Correção de Lucas

Mensagem pedida no WhatsApp interno:

> @+55 11 98555-5245 temos air jordan 1 low panda 36 e tenis new balance 9060 triple white branco 36 em estoque na loja?

Resposta anterior indevida:

> Está zerado nos candidatos consultados tamanho 36.  
> Fonte: Tiny / LK | CONTROLE ESTOQUE.  
> Confiança: média.

Lucas corrigiu: o Hermes não deveria responder estoque consultando Tiny diretamente; deveria usar obrigatoriamente o database / superfície do `LK Stock`.

## Regra operacional atualizada

- Atendimento/WhatsApp/Elle/LK Ops não consulta Tiny, Shopify, cache próprio ou delta local para disponibilidade.
- Fluxo obrigatório: `lk-stock` / Stock OS local DB pointer primeiro.
- Se Stock OS confirmar produto+tamanho com identidade segura: responder com fonte `LK Stock OS local DB (lk-stock)` e ressalva interna antes de prometer ao cliente.
- Se Stock OS não confirmar item exato: responder **não confirmado** e pedir validação/reconciliação do `lk-stock`.
- Ausência de match no Stock OS **não** vira “zerado”.

## Correção local aplicada

Arquivos locais atualizados:

- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`
  - `answer_stock()` agora chama `format_stock_os_local_answer()`.
  - Consulta apenas `LK_STOCK_OS_POINTER` / tabela `current_local_stock` do Stock OS.
  - Não chama `tiny_stock_resolver_v2()` no caminho de resposta de estoque WhatsApp.
  - Lookup do Stock OS ficou size-aware para evitar match de tamanho errado.
  - Quando um item da pergunta não resolve no Stock OS, inclui linha `não confirmado ... validar/reconciliar com lk-stock`.
- `/opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py`
  - Regressão garantindo que resposta de estoque usa Stock OS e não Tiny.
  - Regressão garantindo que item não resolvido vira validação `lk-stock`, não “zerado”.
- Skills/Brain:
  - `lk-operational-intelligence/SKILL.md`
  - `lk-shopify-readonly/references/tiny-local-stock-db-whatsapp-responder.md`
  - `areas/lk/projetos/lk-whatsapp-hermes-team-atendimento-prd-2026-05-17.md`

## Verificação executada

Comando:

```bash
python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py && python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
```

Resultado: `ok`.

Smoke local read-only com a pergunta de Lucas:

```text
Fonte: LK Stock OS local DB (lk-stock).
• Tênis Nike Air Jordan 1 Low Panda (2023) Preto — Tamanho 36 (`DC0774101-3`): 1 un. observada(s) no Stock OS.
• new balance 9060 triple white branco — Tamanho 36: não confirmado no Stock OS; validar/reconciliar com lk-stock.
Uso interno: validar com lk-stock antes de prometer ao cliente; não reservei, não alterei estoque e não consultei Tiny/Shopify direto.
```

## Produção / runtime

Writes externos executados: 0.  
Tiny/Shopify/WhatsApp send/restart executados: 0.  
Restart do responder WhatsApp em produção: **não executado**; exige aprovação escopada porque muda runtime/bot.

## Reminder OS

Reminder OS loop needed: yes  
Reminder OS owner: `lk-stock` + operador do responder WhatsApp LK  
Reminder OS next action: validar se o processo WhatsApp ativo carrega `/opt/data/scripts/lk_hermes_whatsapp_responder.py`; se Lucas aprovar, reiniciar o responder com backup/rollback e readback, depois fazer smoke no grupo/canal permitido.  
Reminder OS review trigger: próxima pergunta de estoque no WhatsApp ou aprovação explícita de Lucas para restart do responder.  
Reminder OS evidence: testes locais `ok`; handoff file atual; diff local nos arquivos listados.
