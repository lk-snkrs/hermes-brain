# Receipt — Elle prioridade de pronta entrega/estoque sobre status de pedido

- Data/hora UTC: 2026-06-15T15:32Z
- Área: LK / Atendimento / Elle / Chatwoot
- Correção humana: Lucas mostrou conversa em que cliente perguntou “Voces tem a pronta entrega o Salomon XT-6 Vanilla ICE tamanho 39 ?” e a Elle respondeu pedindo número do pedido.
- Regra correta: pronta entrega/disponibilidade/loja física/retirada/reserva é estoque/pronta entrega, portanto deve transbordar para Larissa/lk-stock sem prometer disponibilidade e sem pedir número de pedido.

## Diagnóstico

- A mensagem tinha `pronta entrega`, mas também continha a palavra `entrega`.
- No fluxo com Gemini/classificação, `order_status` podia vencer antes de `hard_stock`.
- Resultado incorreto anterior: categoria de pedido/status e pedido de número do pedido.

## Alteração

- `hard_stock` agora vence antes de `order_status`.
- Adicionado ramo determinístico antes do uso final do Gemini:
  - `category=stock_handoff`;
  - `handoff=true`;
  - labels incluem `estoque`, `humano`, `lk-stock`;
  - `blocked_reasons=['stock_or_availability_lk_stock']`.
- Reordenado ramo com AI para que `hard_stock` continue vencendo antes de `order_status`.

## Verificação

- `python3 -m py_compile app.py`: OK.
- Teste sintético antes do deploy:
  - frase exata: `Voces tem a pronta entrega o Salomon XT-6 Vanilla ICE tamanho 39 ?`;
  - resultado: `category=stock_handoff`;
  - `handoff=true`;
  - label `lk-stock=true`;
  - não contém “número do pedido” na resposta;
  - regressão: `qual o status da entrega?` não vira `stock_handoff`.
- Rebuild/recreate do container `elle-chatwoot`: OK.
- Teste sintético dentro do container novo:
  - `exact_prompt_category=stock_handoff`;
  - `exact_prompt_handoff=true`;
  - `has_lk_stock_label=true`;
  - `does_not_ask_order_number=true`;
  - `order_status_not_stock=true`;
  - `values_printed=false`.
- Health público:
  - `ok=true`;
  - `write_enabled=true`;
  - `kill_switch=false`;
  - `public_reply_enabled=true`;
  - `ai_enabled=true`;
  - `ai_model=google/gemini-2.5-flash`;
  - `ai_secret_present=true`;
  - `debounce_enabled=true`;
  - `debounce_seconds=15.0`.

## Rollback

- Backup salvo em `/opt/elle-chatwoot/backups/lucas-pronta-entrega-stock-priority-20260615T152939Z/app.py`.

## Segurança

- Não foi consultado estoque diretamente.
- Não foi prometida disponibilidade.
- Não foi feito teste em cliente real.
- Sem impressão de telefone, e-mail, URL, token, secret ou PII.
