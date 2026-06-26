# Approval packet + Telegram noise hardening — 2026-06-14

## Pedido

Lucas aprovou: "Fazer 1 depois fazer o 2".

Sequência executada:

1. Corrigir documentalmente 2–3 approval packets críticos da amostra, sem executar nada.
2. Adicionar contract tests para ruído/actionability em Telegram.

## Escopo e guardrails

Classificação: A1 local/documental/testes.

Não ações:

- nenhum approval packet executado;
- nenhuma aprovação nova assumida;
- nenhum Telegram enviado;
- sem runtime, Docker, VPS, Traefik, gateway, restart ou cron mutation;
- sem Shopify, Tiny, GMC, Klaviyo, Meta, WhatsApp, e-mail, banco ou integrações externas;
- nenhum secret impresso; `values_printed=false`.

## Parte 1 — Approval packets corrigidos

Foram corrigidos 3 packets da amostra real, apenas adicionando campos mínimos ausentes e guardrails. Nenhuma ação operacional foi executada.

### 1. Supabase MCP read-only

Arquivo:

- `areas/hermes/operacoes/manual-producao/APPROVAL_PACKET_SUPABASE_MCP_READONLY.md`

Campos adicionados/clarificados:

- target/owner;
- escopo permitido;
- exclusões explícitas;
- verificação;
- secret hygiene.

### 2. LK auto-sort collections fallback correction

Arquivo:

- `areas/lk/reports/auto-sort-collections/2026-05-26-pilot-fallback-correction/APPROVAL-PACKET-FALLBACK-CORRECTION.md`

Campos adicionados/clarificados:

- decisão/ação solicitada;
- escopo permitido;
- exclusões explícitas;
- opções de aprovação;
- secret hygiene.

### 3. LK Weekly Collection Sort Rule B recorrente APPLY

Arquivo:

- `areas/lk/reports/auto-sort-collections/approval-packets/ruleb-recurring-apply-approval-packet-20260604.md`

Campos adicionados/clarificados:

- target/owner;
- escopo permitido;
- exclusões explícitas;
- secret hygiene.

### Validação dos 3 corrigidos

Comando equivalente rodado:

```bash
python3 scripts/approval_packet_completeness_validator.py <3 packets> --json
```

Resultado:

- `status=ok`
- `files_checked=3`
- `failures_count=0`
- `values_printed=false`

## Parte 2 — Telegram noise/actionability contract tests

Foi endurecido o validador local:

- `scripts/telegram_noise_contract_validator.py`

E criado teste regressivo:

- `tests/test_telegram_noise_contract_validator.py`

Contratos cobertos:

1. mensagem acionável passa quando contém alerta + gatilho + ação clara;
2. wrapper/metadata leak falha;
3. alerta sem ação clara falha;
4. silent-OK exige stdout vazio quando `status=ok`;
5. CLI JSON conta achados sem imprimir valores (`values_printed=false`).

Amostra real gerada:

- `reports/telegram-noise-contract-sample-2026-06-14.json`

Resultado da amostra:

- `status=attention`
- `files_checked=20`
- `failures_count=1`
- `values_printed=false`

Falha encontrada:

- `areas/hermes/operacoes/receipts/cron-0230-report-telegram-explanation-fix-2026-05-26.md`
- categoria: `wrapper_or_metadata_noise`

Interpretação: há um artifact histórico com ruído/wrapper-like. Isso virou backlog documental; não é envio Telegram atual nem runtime ativo.

## Verificações finais

Verificações finais registradas no output da sessão:

- `python3 -m unittest tests/test_approval_packet_completeness_validator.py -v`
- `python3 -m unittest tests/test_telegram_noise_contract_validator.py -v`
- `python3 -m py_compile scripts/approval_packet_completeness_validator.py scripts/telegram_noise_contract_validator.py tests/test_approval_packet_completeness_validator.py tests/test_telegram_noise_contract_validator.py`
- JSON parse das amostras;
- Brain Health;
- Operational docs guard;
- focused credential hygiene scan;
- `git diff --check` nos artefatos relevantes.

## Resultado

A cadeia agora tem dois gates locais mais fortes:

1. approval packets antigos podem ser saneados/documentados antes de qualquer execução;
2. mensagens Telegram futuras podem ser testadas contra ruído de wrapper/metadata e falta de ação clara.

Próximo passo recomendado: corrigir o único artifact histórico de Telegram noise encontrado ou integrar o validator em uma rotina local/silent-OK existente, sem criar novo ruído.
