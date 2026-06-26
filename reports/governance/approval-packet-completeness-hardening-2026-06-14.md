# Approval Packet Completeness Hardening — 2026-06-14

## Pedido

Lucas disse: "Seguir" após a wave curta de skill-quality crítica.

## Escopo

Classificação: A1 local/documental/teste-regressão.

Guardrails:

- Sem executar nenhum approval packet.
- Sem conceder aprovação nova.
- Sem runtime, Docker, VPS, Traefik, gateway, restart ou container.
- Sem alteração de cron schedule/delivery/enabled/state.
- Sem integração externa, banco, Shopify, Tiny, GMC, Klaviyo, Meta, WhatsApp ou e-mail.
- Sem secrets impressos; `values_printed=false`.

## Problema atacado

O próximo ponto de aprendizado contínuo era tornar approval packets verificáveis de forma determinística. Já existia `scripts/approval_packet_completeness_validator.py`, mas a descoberta era ampla demais e incluía evidências históricas como `APPROVAL-CAPTURED`, approvals reiterados/logs/receipts. Isso gerava ruído: histórico de aprovação podia ser tratado como packet incompleto.

## Mudanças aplicadas

- `scripts/approval_packet_completeness_validator.py`
  - adicionada função `_is_discoverable_packet`;
  - descoberta agora exige sinais de packet real no nome/conteúdo;
  - exclusão explícita de captures/reiterated/logs/receipts;
  - mantido contrato read-only/local, sem execução.

- `tests/test_approval_packet_completeness_validator.py`
  - criado teste de regressão com fixtures sintéticas locais;
  - packet completo passa;
  - packet incompleto falha com campos ausentes;
  - valor token-like é contado, mas não impresso;
  - discovery ignora approval captures e receipts.

- `hermes-brain-governance`
  - adicionada referência `references/approval-packet-completeness-hardening-20260614.md`;
  - `SKILL.md` principal agora aponta para essa referência.

## Resultado da amostra real

Gerado:

- `reports/approval-packet-completeness-sample-2026-06-14.json`

Amostra atual:

- `status`: `attention`
- `files_checked`: 10
- `failures_count`: 10
- `values_printed`: false

Interpretação: há backlog real de packets existentes incompletos nos primeiros 10 descobertos, mas isso não é autorização para executar ou reescrever packets de negócio automaticamente. A melhoria desta wave foi endurecer o mecanismo e reduzir falso positivo de evidência histórica.

Primeiros caminhos com atenção na amostra:

- `areas/hermes/operacoes/manual-producao/APPROVAL_PACKET_SUPABASE_MCP_READONLY.md`
- `areas/lk/reports/auto-sort-collections/2026-05-26-pilot-fallback-correction/APPROVAL-PACKET-FALLBACK-CORRECTION.md`
- `areas/lk/reports/auto-sort-collections/approval-packets/ruleb-recurring-apply-approval-packet-20260604.md`

## Verificações executadas

- `python3 -m unittest tests/test_approval_packet_completeness_validator.py -v`
  - 3 testes rodaram, 3 OK.

- `python3 scripts/approval_packet_completeness_validator.py --discover --limit 10 --json`
  - saída JSON válida;
  - `values_printed=false`;
  - status `attention` por backlog real de packets incompletos.

## Próximo melhor passo

Escolher uma wave pequena para corrigir os 2–3 approval packets mais críticos da amostra, sem executar nenhuma ação externa, ou avançar para o outro candidato: `Telegram noise/actionability contract tests`.
