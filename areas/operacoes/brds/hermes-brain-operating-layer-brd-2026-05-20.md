# BRD — Hermes Brain Operating Layer — 2026-05-20

## Objetivo

Adicionar ao ecossistema Bruno/OpenClaw uma camada Hermes-native de operação viva: todo evento relevante vira artefato, toda decisão crítica sobe para o Brain, todo especialista deixa rastro e todo runtime documentado é reconciliado contra evidência real.

## Escopo implementado nesta fase

1. Receipt Ledger universal.
2. Brain Steward cron/watchdog.
3. Customer-Facing Decision Guard.
4. Runtime Truth Reconciler.
5. Hot Memory Compiler.
6. Skill Promotion Engine.
7. Approval Ledger.
8. Webhook/Event → Brain.
9. Profiles especialistas com contrato de handoff.
10. Mission Control como cockpit do Brain.
11. Session Search + Semantic Recovery.
12. Silent-OK watchdogs.
13. Voice-to-Brain.
14. Brain Diff Digest.
15. Source Confidence.

## Não-escopo desta fase

- Não alterar Docker, Traefik, containers, volumes, root password, redes ou produção.
- Não conectar webhooks externos produtivos ainda.
- Não enviar mensagens/campanhas/customer-facing sem aprovação.
- Não transformar Mission Control em fonte de verdade; ele é cockpit sobre o Brain.

## Métrica de sucesso

- Arquivos/t/templates/rotinas criados e indexados.
- Watchdog estrutural silent-OK ativo.
- Reconciler runtime com cron local/read-only ativo.
- Health check do Brain com FAIL=0 WARN=0.
- Brain Sync dry-run bloqueando corretamente scripts/config/artefatos não permitidos e permitindo docs seguros.
