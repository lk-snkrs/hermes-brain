# Elle — correção log path + off-topic/spam comercial (2026-06-15)

## Escopo aprovado por Lucas
- Fazer correção 1: observer usar o log real da Elle por padrão.
- Fazer correção 2: Elle não responder publicamente mensagens comerciais/off-topic como o caso de veterinária/atendimento domiciliar.

## Alterações executadas
- VPS: `/opt/elle-chatwoot`.
- Backup criado antes da alteração: `backups/elle-fix-logpath-spam-20260615T002727Z/` com `app.py`, `elle_observer_summary.py`, `docker-compose.yml` e `.env`.
- `elle_observer_summary.py`:
  - `--log` agora aceita default automático.
  - Ordem de escolha: `ELLE_LOG_PATH` -> `logs/events.jsonl` local, se existir -> `/var/log/elle/events.jsonl`.
  - Resultado: rodar o observer no host de `/opt/elle-chatwoot` passa a ler `logs/events.jsonl`, o log real montado pelo compose.
- `app.py`:
  - adicionados termos e função `is_offtopic_spam_text` para mensagens comerciais/off-topic.
  - adicionada classificação `offtopic_spam` com `reply=''`, `handoff=False`, labels `whatsapp-api`, `offtopic`, `spam_review`, e motivo `offtopic_or_commercial_spam_no_public_reply`.
  - A classificação off-topic retorna antes de chamar IA, evitando resposta pública automática.

## Deploy
- Sintaxe validada com `python3 -m py_compile app.py elle_observer_summary.py`.
- Container recriado com `docker compose up -d --no-deps --build --force-recreate elle-chatwoot`.

## Verificação real
- Health público após deploy: `ok=true`, `dry_run=false`, `write_enabled=true`, `kill_switch=false`, `public_reply_enabled=true`, `ai_enabled=true`, `ai_provider=openrouter`, `observer_enabled=true`.
- Smoke dentro do container:
  - Caso veterinária/atendimento domiciliar -> `category=offtopic_spam`, `handoff=false`, `reply=''`, labels `offtopic/spam_review`.
  - Caso site LK -> segue `product_clear` com resposta pública normal.
  - Caso produto “Você tem New Balance 9060?” -> segue `product_clear` com link/coleção, sem prometer disponibilidade.
- Observer sem `--log` no host agora leu o log real: `eventos totais no log: 512` nas últimas 24h no momento da verificação.

## Observações
- Nenhum secret foi impresso.
- Não houve alteração de Tiny/Shopify/estoque.
- O health mostrou `hmac_secret_present=false`, mas isso já aparecia antes e não foi parte do escopo desta correção.
