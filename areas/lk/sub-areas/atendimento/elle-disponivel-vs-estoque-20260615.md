# Elle — regra Lucas: “está disponível?” vs “tem em estoque?”

Data: 2026-06-15
Origem: áudio Lucas → lk-ops
Sistema: `/opt/elle-chatwoot`

## Correção aprovada
Lucas corrigiu a distinção de intenção:

- Quando a cliente pergunta apenas **“está disponível?” / “disponível?”**, Elle deve tratar como pergunta comercial de site e responder **sim**, orientando a pessoa a seguir pelo site, selecionar a numeração e finalizar a compra.
- Quando a cliente pergunta **“tem em estoque?”**, **“pronta entrega?”**, **“tem na loja?”**, **“retirada”** ou **“reserva”**, Elle deve seguir o fluxo de estoque/pronta entrega: transbordar para Larissa/lk-stock e pedir modelo + numeração se faltar contexto.

## Guardrail operacional
- O “sim” de “está disponível?” é no sentido de **seguir pelo site/checkout**.
- Não transformar esse caso em promessa de pronta entrega/estoque físico.
- Estoque/pronta entrega continua dono do `lk-stock`.

## Deploy aplicado
Backup criado no VPS:
- `/opt/elle-chatwoot/backups/elle-disponivel-vs-estoque-20260615T012935Z/`

Alterações:
- `product_available_reply()` agora começa com “Sim...” e orienta site/numeração/checkout.
- Nova função `is_available_checkout_question()` separa “está disponível?” de termos duros de estoque/loja/retirada/reserva.
- Prompt da IA atualizado com a regra “disponível” vs “estoque”.

Verificação pós-deploy:
- `Está disponível?` → `product_clear`, sem handoff, resposta começa com “Sim...” e orienta site/numeração/checkout.
- `Esse New Balance 9060 está disponível?` → `product_clear`, sem handoff.
- `O tamanho 37 está disponível?` → `product_clear`, sem handoff.
- `Tem em estoque?` → `stock_handoff`, handoff para Larissa/lk-stock, pede modelo + numeração.
- `Esse New Balance 9060 tem em estoque?` → `stock_handoff`.
- `Tem na loja hoje para retirar?` → `stock_handoff`.

Health pós-deploy:
- `ok=true`
- `dry_run=false`
- `write_enabled=true`
- `kill_switch=false`
- `public_reply_enabled=true`
- `ai_enabled=true`
- `observer_enabled=true`
