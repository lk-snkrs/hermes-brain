# Elle — correção de copy sem emoji e abertura com Olá

Data: 2026-06-15 02:04 UTC / 2026-06-14 23:04 BRT
Área: LK / Atendimento / Elle

## Pedido do Lucas

- Remover emoji das mensagens da Elle.
- Preferir “Olá” em vez de “Oi” por soar mais simpático.

## Alterações aplicadas

Ambiente: VPS `lc`, diretório `/opt/elle-chatwoot`.

Arquivos alterados:

- `/opt/elle-chatwoot/elle_followup_worker.py`
  - Stage 1 passou a começar com `Olá!`.
  - Emoji final removido.
  - Stage 2 passou a começar com `Olá!`.
- `/opt/elle-chatwoot/app.py`
  - Greeting determinístico mudou de `Oi` para `Olá`.

Cópias atuais do follow-up:

1º follow-up:
> Olá! Passando para saber se consigo te ajudar com alguma dúvida antes de finalizar. Se quiser, é só me chamar por aqui.

2º follow-up:
> Olá! Ainda posso te ajudar por aqui? Se quiser seguir com a compra ou tirar alguma dúvida, me manda uma mensagem que eu te ajudo.

## Deploy e verificação

- Backup criado no VPS: `/opt/elle-chatwoot/backups/copy-ola-noemoji-20260615T020229Z/`.
- `python3 -m py_compile app.py elle_followup_worker.py`: OK.
- `docker compose up -d --no-deps --build --force-recreate elle-chatwoot`: OK.
- String verificada dentro do container `/app`: OK.
- Health público `https://elle.lkskrs.online/healthz`: `ok=true`, `public_reply_enabled=true`, `ai_enabled=true`, `kill_switch=false`.
- Worker dry-run: `checked=112`, `eligible=0`, `sent=0`, sem disparo real.

## Observação

Correção tratada como ajuste de estilo aprovado pelo Lucas. Não houve alteração de regra de estoque, preço, desconto, reserva, prazo ou handoff.
