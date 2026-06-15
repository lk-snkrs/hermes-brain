# Elle — deploy de regras aprovadas por Lucas

Data: 2026-06-15
Responsável: lk-ops
Sistema: `/opt/elle-chatwoot` no VPS

## Escopo aprovado
Lucas aprovou colocar em prática correções para:
- reduzir fricção de tamanho;
- pedir modelo + numeração apenas quando necessário para estoque/pronta entrega;
- melhorar classificação/relatório do observer;
- manter off-topic/spam comercial sem resposta pública;
- seguir regra operacional de follow-up 60min/23h após última mensagem da cliente.

## Alterações aplicadas

### App Elle (`app.py`)
- Prompt da IA atualizado para **não perguntar tamanho como gate genérico de venda**.
- Regra explícita: só pedir tamanho quando cliente pedir fit/numeração, disser que grade está indisponível, ou quando for necessário para handoff de estoque/pronta entrega.
- Regra explícita: estoque/pronta entrega sem modelo/tamanho claro deve pedir **modelo + numeração** e transbordar para Larissa/lk-stock, sem prometer disponibilidade.
- Copy de handoff de estoque/loja/pronta entrega passou a pedir: “me envie o modelo e a numeração que você procura”.

### Observer (`elle_observer_summary.py`)
- Bucket antes confuso “não respondeu corretamente: event_filter” foi trocado para **“silêncio correto: evento operacional/sistema”**.
- `human_takeover_lock` passou para **“silêncio correto: humano já assumiu”**.
- Default do observer já estava ajustado para usar `logs/events.jsonl` local quando existir.

## Backup
- Backup criado no VPS: `/opt/elle-chatwoot/backups/elle-approved-rules-20260615T011012Z/`

## Deploy/verificação
- `python3 -m py_compile app.py elle_observer_summary.py`: OK.
- `docker compose build elle-chatwoot`: OK.
- `docker compose up -d elle-chatwoot`: OK.
- Health pós-deploy: `ok=true`, `dry_run=false`, `write_enabled=true`, `kill_switch=false`, `public_reply_enabled=true`, `ai_enabled=true`, `observer_enabled=true`.

## Testes sintéticos pós-deploy
- `Tem em estoque` → `stock_handoff`, pede modelo + numeração, transfere para Larissa; não promete disponibilidade.
- `Tem na loja hoje para retirar?` → `stock_handoff`, pede modelo + numeração, transfere para Larissa; não promete disponibilidade.
- Produto/site → `product_clear`, conduz para site/checkout.
- Carrinho → `product_clear`, ajuda a finalizar/tirar dúvida.
- Onitsuka tamanho 37 → `product_clear`, recomenda tamanho normal; não pede outro tamanho.
- Mensagem veterinária/comercial externa → `offtopic_spam`, sem resposta pública.

## Observação sobre follow-up automático
Não foi encontrado um scheduler/cron local ativo de follow-up conversacional dentro de `/opt/elle-chatwoot`, `/opt/data/scripts`, `/opt/data/cron`, `/etc/cron.d` ou systemd. A regra 60min/23h foi registrada como regra operacional; para automatizar envio ativo de follow-ups é necessário localizar o dono atual do fluxo (ex.: Chatwoot/n8n/Shopify/CRM) ou criar um worker novo com cópia, limites, opt-out e deduplicação.
