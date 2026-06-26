# LC Mordomo OS — P2 Zipper readiness/blocker cleanup plan

**Data:** 2026-06-06
**Status:** aberta em modo local/dry-run
**Origem:** P1.22 final audit/readiness summary

## Objetivo

Abrir a P2 para limpar blockers upstream do fluxo Zipper/Mordomo OS de forma local, testada e auditável, sem produção.

P2 não autoriza:

- criação de cron real;
- execução real de `hermes cron create`;
- mutação do scheduler;
- sender real;
- runtime-send;
- WhatsApp/e-mail/Telegram externo;
- Supabase/infra/produção.

## Estado herdado da P1

P1 terminou como auditoria/artefato completa, mas produção ficou **NO-GO**.

Artefatos P1 consolidados:

- P1.8–P1.21: 14/14 artefatos presentes.
- Testes integrados Zipper até P1.22: 87/87 OK.
- Health P1.22: fail=0, warn=0.
- Estado efetivo: zero cron real, zero Hermes CLI real, zero scheduler mutation, zero sender, zero runtime-send, zero envio externo.

Blockers principais herdados:

- `p120_not_clean`
- `p121_command_not_executable_now`
- `cron_real_approval_not_recorded`
- `final_execute_phrase_missing`
- `ledger_not_clean_silent_ok`
- `state_and_rollback_rehearsal_not_complete`
- `upstream_blockers_present`
- `no_fake_cron_id_available`
- `no_actionable_candidates_current_snapshot`

## Estratégia P2

P2 deve limpar blockers por evidência local, não por bypass.

Princípios:

1. Revalidar inputs e estado antes de mudar gates.
2. Manter TDD para cada módulo novo.
3. Separar readiness técnica de aprovação humana.
4. Separar cron local/no-agent de runtime-send/envio externo.
5. Preferir fixtures limpas e simulações injetáveis antes de qualquer runtime real.
6. Se aparecer side effect real, parar e marcar `NO-GO`.

## Sequência proposta

### P2.1 — Blocker taxonomy and dependency map — concluído

Módulo local criado para ler P1.22 e gerar taxonomia/árvore de blockers com dependências e owner lógico.

Artefatos P2.1:

- `/opt/data/profiles/mordomo/scripts/zipper_followup_p2_blocker_taxonomy.py`
- `/opt/data/profiles/mordomo/scripts/test_zipper_followup_p2_blocker_taxonomy.py`
- `/opt/data/profiles/mordomo/state/zipper_followup_p2_blocker_taxonomy.json`
- `areas/operacoes/reports/lcmordomo-p201-zipper-blocker-taxonomy-2026-06-06.md`

Resultado P2.1:

- Go/No-Go permanece `NO-GO`.
- Categorias finais: `approval_phrase_missing`, `command_envelope_readiness`, `data_current_snapshot`, `ledger_cleanliness`, `rehearsal_completion`, `sender_runtime_guard`, `upstream_dependency`.
- Owners: `local_p2` e `lucas_decision`; nenhum blocker conhecido ficou `uncategorized`.
- `seguir` não registra decisão de produção.
- Frase de decisão futura registra apenas decisão, sem executar comando, criar cron, habilitar runtime-send ou aprovar envio externo.
- Próxima sequência recomendada: P2.2 → P2.3 → P2.4 → P2.5 → P2.6.
- Estado efetivo: zero cron real, zero Hermes CLI real, zero scheduler mutation, zero sender, zero runtime-send, zero envio externo.

### P2.2 — Clean fixture builder for readiness rehearsal — concluído

Fixture local limpa criada para representar caminho técnico sem blockers, usando dados sintéticos/sanitizados.

Artefatos P2.2:

- `/opt/data/profiles/mordomo/scripts/zipper_followup_p2_clean_fixture_builder.py`
- `/opt/data/profiles/mordomo/scripts/test_zipper_followup_p2_clean_fixture_builder.py`
- `/opt/data/profiles/mordomo/state/zipper_followup_p2_clean_fixture_builder.json`
- `areas/operacoes/reports/lcmordomo-p202-zipper-clean-fixture-builder-2026-06-06.md`

Resultado P2.2:

- Fixture Go/No-Go: `GO-TECHNICAL-FIXTURE-NOT-PRODUCTION`.
- Snapshot real preservado bloqueado: `NO-GO`.
- P1.18–P1.21 sintéticos gerados com `blocking_reasons=[]`.
- Fake cron id sintético: `fixture-cron-zpr-clean-001`.
- Rehearsal state/rollback sintético completo: sim.
- P1.20 sintético elegível tecnicamente para futura criação de cron: sim.
- P1.21 sintético renderiza comando futuro e marca `command_executable_now=true` no fixture.
- Nenhuma decisão de produção registrada.
- Nenhuma aprovação de runtime-send/envio externo registrada.
- Estado efetivo: zero cron real, zero Hermes CLI real, zero scheduler mutation, zero sender, zero runtime-send, zero envio externo.

### P2.3 — State + rollback rehearsal completion repair — concluído

Repair local/sintético criado para limpar blockers de rehearsal usando fake cron id/stubs, preservando snapshot real bloqueado.

Artefatos P2.3:

- `/opt/data/profiles/mordomo/scripts/zipper_followup_p2_state_rollback_repair.py`
- `/opt/data/profiles/mordomo/scripts/test_zipper_followup_p2_state_rollback_repair.py`
- `/opt/data/profiles/mordomo/state/zipper_followup_p2_state_rollback_repair.json`
- `areas/operacoes/reports/lcmordomo-p203-zipper-state-rollback-repair-2026-06-06.md`

Resultado P2.3:

- Repair Go/No-Go: `REHEARSAL-COMPLETE-FIXTURE-ONLY`.
- Fake cron id: `fixture-cron-zpr-clean-001`.
- Blockers de fixture limpos: `state_and_rollback_rehearsal_not_complete`, `no_fake_cron_id_available`.
- State check stub executado: sim.
- Rollback stub executado: sim.
- Post-check stub executado: sim.
- Snapshot real preservado bloqueado: `NO-GO`.
- Elegível para cron real agora: não.
- Estado efetivo: zero cron real criado/removido, zero Hermes CLI real, zero scheduler mutation, zero sender, zero runtime-send, zero envio externo.

### P2.4 — Ledger cleanliness repair — concluído

Repair local/sintético criado para limpar semântica de ledger/silent-OK sem depender de candidatos inexistentes e mantendo idempotência separada de aprovação humana.

Artefatos P2.4:

- `/opt/data/profiles/mordomo/scripts/zipper_followup_p2_ledger_cleanliness_repair.py`
- `/opt/data/profiles/mordomo/scripts/test_zipper_followup_p2_ledger_cleanliness_repair.py`
- `/opt/data/profiles/mordomo/state/zipper_followup_p2_ledger_cleanliness_repair.json`
- `areas/operacoes/reports/lcmordomo-p204-zipper-ledger-cleanliness-repair-2026-06-06.md`

Resultado P2.4:

- Ledger Go/No-Go: `LEDGER-CLEAN-SILENT-OK-FIXTURE-ONLY`.
- Blocker de fixture limpo: `ledger_not_clean_silent_ok`.
- Stdout contract: `silent_ok`.
- Stdout vazio: sim.
- Entradas sintéticas: 0.
- Candidate count: 0.
- Snapshot real preservado bloqueado: `NO-GO`.
- Elegível para cron real agora: não.
- Estado efetivo: zero cron real criado/removido, zero Hermes CLI real, zero scheduler mutation, zero sender, zero runtime-send, zero envio externo.

### P2.5 — Approval surface reconciliation — concluído

Reconciliação local/dry-run criada para separar frase casual, decisão de produção, execução futura, runtime-send e envio externo.

Artefatos P2.5:

- `/opt/data/profiles/mordomo/scripts/zipper_followup_p2_approval_surface_reconciliation.py`
- `/opt/data/profiles/mordomo/scripts/test_zipper_followup_p2_approval_surface_reconciliation.py`
- `/opt/data/profiles/mordomo/state/zipper_followup_p2_approval_surface_reconciliation.json`
- `areas/operacoes/reports/lcmordomo-p205-zipper-approval-surface-reconciliation-2026-06-06.md`

Resultado P2.5 para a frase recebida `aprovo`:

- Approval Go/No-Go: `GO-TECHNICAL-NOT-PRODUCTION`.
- Classe da frase: `casual_continue`.
- Decisão de produção registrada: não.
- Execução aprovada: não.
- Elegível para cron real agora: não.
- Bloqueio humano restante: `production_decision_phrase_missing`.
- Validação não persistente da frase exata de decisão: `GO-ELIGIBLE-BUT-NOT-EXECUTED`, sem execução e sem runtime/external-send.
- Estado efetivo: zero cron real criado/removido, zero Hermes CLI real, zero scheduler mutation, zero sender, zero runtime-send, zero envio externo.

### P2.6 — Final P2 readiness audit — concluído

Auditoria final local/dry-run criada para consolidar P2.1–P2.5.

Artefatos P2.6:

- `/opt/data/profiles/mordomo/scripts/zipper_followup_p2_final_readiness_audit.py`
- `/opt/data/profiles/mordomo/scripts/test_zipper_followup_p2_final_readiness_audit.py`
- `/opt/data/profiles/mordomo/state/zipper_followup_p2_final_readiness_audit.json`
- `areas/operacoes/reports/lcmordomo-p206-zipper-final-p2-readiness-audit-2026-06-06.md`

Resultado final P2:

- P2 Final Go/No-Go: `GO-ELIGIBLE-BUT-NOT-EXECUTED` após frase exata recebida no turno atual.
- Technical fixture clean: sim.
- Decisão de produção registrada: sim.
- Elegível para futura criação de cron: sim.
- Execução aprovada: não.
- Elegível para cron real agora: não.
- Artefatos P2 esperados/encontrados: 15/15.
- Blockers técnicos/humanos restantes nesta auditoria: nenhum.
- Estado efetivo: zero cron real criado/removido, zero Hermes CLI real, zero scheduler mutation, zero sender, zero runtime-send, zero envio externo.

## Frases de aprovação continuam separadas

Casual:

- `seguir`
- `fazer`
- `aprovado`
- `aprovado seguir`

Significa apenas continuar etapa local segura.

Produção futura exigiria frase fora do fluxo casual:

- `DECIDIR PRODUCAO CRON LOCAL ZIPPER NO-AGENT SEM ENVIO EXTERNO`

E execução futura exigiria frase separada:

- `EXECUTAR CRON REAL LOCAL NO-AGENT ZIPPER SEM ENVIO EXTERNO`

Nenhuma dessas aprova runtime-send ou envio externo.

## Verificação mínima de cada P2.x

Cada etapa deve passar:

```bash
cd /opt/data/profiles/mordomo/scripts
python3 -m py_compile <module>.py <test_module>.py
python3 -m unittest <test_module> -v
python3 <module>.py --write --self-test
```

E deve comprovar:

- `cron_created=false`
- `command_executed=false`
- `real_hermes_cli_called=false`
- `scheduler_mutated=false`
- `sender_called=false`
- `runtime_send_enabled=false`
- `sends_now=false`
- `external_call_count=0`
- `raw_pii_failure_count=0`

## Próximo passo imediato

P2 concluída em modo local/dry-run com decisão de produção registrada, após frase exata recebida no turno atual. Próximo passo seguro: parar aqui ou iniciar etapa separada de execução futura com frase exata própria e verificação fresca; execução real continua não executada e runtime-send/envio externo seguem bloqueados.
