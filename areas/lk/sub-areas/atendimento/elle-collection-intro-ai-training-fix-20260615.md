# Elle — correção coleção genérica + intro IA em treinamento

Data: 2026-06-15 10:00 UTC / 2026-06-15 07:00 BRT
Área: LK / Atendimento / Elle

## Correção solicitada pelo Lucas

Lucas apontou dois problemas após auditoria da madrugada:

1. Corrigir o caso de cliente navegando em coleção/site genérico e dizendo “gostaria de saber mais”.
2. A Elle errou ao não falar que é um bot/IA de atendimento em treinamento.

## Alteração aplicada em produção

Ambiente: VPS `lc`, `/opt/elle-chatwoot`.

Arquivo alterado:

- `/opt/elle-chatwoot/app.py`

Mudanças:

- `product_context_reply(...)` agora abre conversa em vez de empurrar checkout/numeração.
- Para “Estava navegando em <produto/coleção> e gostaria de saber mais”, o `classify(...)` força resposta determinística de contexto do produto/coleção mesmo quando a IA sugere resposta genérica.
- Prompt da IA reforçado: primeira resposta deve apresentar a Elle como IA de atendimento em treinamento; não empurrar checkout/numeração/modelo específico em coleção genérica.

## Cópia esperada no smoke

Para mensagem de coleção genérica, a resposta testada foi:

> Olá, Ana! Como vai? Aqui é a Elle da LK. Sou uma IA de atendimento ainda em fase de aprendizado, então posso errar em alguns casos, mas vou fazer o possível para te ajudar e chamar a Larissa quando precisar. Vi que você estava olhando uma página da LK. Como posso te ajudar?

## Deploy e verificação

- Backup criado no VPS: `/opt/elle-chatwoot/backups/collection-intro-ai-training-20260615T100042Z/`.
- `python3 -m py_compile app.py elle_followup_worker.py`: OK.
- `docker compose up -d --no-deps --build --force-recreate elle-chatwoot`: OK.
- Health público `https://elle.lkskrs.online/healthz`: `ok=true`, `public_reply_enabled=true`, `ai_enabled=true`, `kill_switch=false`.
- Smoke dentro do container: `category=product_clear`, `handoff=False`, resposta com intro de IA em treinamento e pergunta aberta.
- Follow-up dry-run: `checked=115`, `eligible=0`, `sent=0`.

## Observação

Esta correção não altera estoque, preço, prazo, reserva, desconto ou qualquer write em Shopify/Tiny/Chatwoot além do deploy já aprovado para comportamento da Elle.
