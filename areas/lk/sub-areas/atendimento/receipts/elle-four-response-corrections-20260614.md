# Elle — 4 correções de resposta aplicadas

Data: 2026-06-14
Perfil: lk-ops
Escopo: Elle Chatwoot production receiver `/opt/elle-chatwoot` no VPS LK

## Pedido do Lucas

Corrigir sequencialmente os 4 pontos identificados no atendimento da Elle:

1. Carrinho/checkout não pode ficar sem resposta comercial.
2. Home/site geral não deve responder institucional genérico nem ficar silenciosa.
3. Relatório deve diferenciar não resposta correta vs possível falha.
4. Pós-venda sensível deve ter acolhimento + Larissa; mensagens curtas pós-transbordo não devem parecer erro.

## Alterações aplicadas

Arquivos alterados:

- `/opt/elle-chatwoot/app.py`
- `/opt/elle-chatwoot/elle_observer_summary.py`

Backup/rollback:

- `/root/elle-rollbacks/elle-4-corrections-20260614-203659/`

### 1. Carrinho/checkout

Adicionada detecção determinística para `carrinho`, `checkout`, `Seu Carrinho de Compras` e `/cart`.

Resposta segura esperada:

> Oi! Como vai? Aqui é a Elle da LK. Sou uma IA de atendimento ainda em fase de aprendizado, então posso errar em alguns casos, mas vou fazer o possível para te ajudar e chamar a Larissa quando precisar. Vi que você estava no carrinho. Posso te ajudar a finalizar a compra ou tirar alguma dúvida antes do pedido?

Categoria: `product_clear`  
Handoff: `false`

### 2. Home/site geral

Adicionada detecção para home/site geral LK (`LK Sneakers Jardins`, `Curadoria de Sneakers Originais`, `https://lksneakers.com.br/`).

Resposta segura esperada:

> Oi! Como vai? Aqui é a Elle da LK. Sou uma IA de atendimento ainda em fase de aprendizado, então posso errar em alguns casos, mas vou fazer o possível para te ajudar e chamar a Larissa quando precisar. Vi que você estava olhando nosso site. Você está procurando algum modelo, marca ou numeração específica? Posso te ajudar a encontrar no site.

Categoria: `product_clear`  
Handoff: `false`

### 3. Relatório de não resposta

`elle_observer_summary.py` agora inclui seção:

- `não resposta por motivo`
- `Não resposta: correta x revisar`

Categorias novas/normalizadas:

- correta: evento operacional/fora do escopo
- correta: humano já assumiu
- correta: follow-up curto após transbordo
- correta: transbordo humano sem resposta automática
- revisar: carrinho/checkout sem resposta
- revisar: home/site sem resposta
- revisar: processado/ignorado sem motivo seguro

### 4. Pós-venda sensível e mensagens curtas pós-handoff

Pós-venda sensível segue com resposta pública acolhedora e transbordo para Larissa, sem decidir reembolso/prazo/estorno.

Mensagens curtas após humano/transbordo (`ok`, `.`, `sim`, `obrigado/obrigada`) são marcadas como `followup_pos_handoff` no observador/fallback e não como falha de atendimento.

## Verificação executada

Sintaxe:

- `python3 -m py_compile app.py elle_observer_summary.py` OK local e no VPS.

Deploy:

- `docker compose build elle-chatwoot` OK.
- `docker compose up -d --no-deps --force-recreate elle-chatwoot` OK.
- Container `elle-chatwoot` running.

Health externo:

- `https://elle.lkskrs.online/healthz` retornou `200`.
- Flags verificadas: `dry_run=false`, `write_enabled=true`, `kill_switch=false`, `public_reply_enabled=true`, `ai_enabled=true`, `ai_secret_present=true`.

Testes sintéticos dentro do container:

- Carrinho `/cart`: `category=product_clear`, `handoff=false`, `reply_allowed=true`.
- Home LK: `category=product_clear`, `handoff=false`, `reply_allowed=true`.
- Reclamação/pós-venda sensível: `category=human_handoff`, `handoff=true`, `reply_allowed=true`, copy de acolhimento + Larissa + horário.
- `Ok` após `incoming_blocked_by_human_takeover`: `customer_intent=followup_pos_handoff`, `followup_needed=false`.

## Guardrails mantidos

- Nenhuma consulta/afirmação de estoque foi feita.
- Nenhuma promessa de disponibilidade, reserva, prazo, preço ou desconto foi adicionada.
- Handoff público segue nomeando Larissa; atribuição interna continua para Giselia conforme configuração existente.
- Secrets não foram impressos; apenas presença/status foi verificada.
