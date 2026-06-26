# Receipt — LK support profiles auth and CLI smoke repair

- Data/hora: 2026-06-25T18:54:22.116177+00:00
- Agente/profile/cron: default
- Empresa/área: Hermes Operações / LK OS
- Responsável humano: Hermes
- Pedido original: Lucas pediu fazer 1 e 2: investigar exit 134/core dumped no Hermes CLI smoke e corrigir HTTP 401 token_expired em lk-analyst-readonly e lk-content-reviewer.
- Classificação: infra-sensitive
- Fontes usadas:
- Profile auth/config files with backups; errors.log; Hermes CLI reproduction; temp HERMES_HOME isolation tests; Brain health; sanitized smoke JSON
- O que foi feito:
- Backup criado; openai-codex credential pool dos support profiles sincronizado a partir do default sem imprimir valores; providers.openai-codex legado removido; delegation.api_mode alinhado; root cause do exit 134 isolado em Hermes CLI single-query + Honcho enabled no shutdown/finalize; criado /opt/data/scripts/hermes_profile_identity_smoke.py para smoke read-only sem contaminação de sessão e sem Honcho abort; smokes finais 2/2 OK.
- Output/artefato:
- reports/governance/lk-support-profiles-auth-and-cli-smoke-repair-2026-06-25.md; /opt/data/scripts/hermes_profile_identity_smoke.py; /opt/data/backups/lk-support-profile-auth-repair-20260625T183639Z; /opt/data/backups/lk-support-profile-identity-smoke-after-authfix-20260625T185137Z.json
- Aprovação: Aprovado por Lucas: fazer 1 e 2. Escopo limitado a support profiles LK e diagnóstico local/read-only do Hermes CLI.
- Envio/publicação: Resumo final no Telegram; relatório/receipt no Brain.
- Writes externos: 0
- Riscos/bloqueios: Auth files contêm secrets por natureza, mas nenhum valor foi impresso. O bug upstream/local do CLI+Honcho permanece como pendência de patch no runtime Hermes, mitigado por harness seguro para smokes.
- Rollback/mitigação: Restaurar auth.json/config.yaml dos dois profiles a partir de /opt/data/backups/lk-support-profile-auth-repair-20260625T183639Z; remover /opt/data/scripts/hermes_profile_identity_smoke.py se o workaround não for desejado.
- Próximos passos: Opcional: abrir tarefa separada para patch/test upstream do CLI+Honcho shutdown; activation packet separado se support profiles precisarem virar gateways ativos.
- Onde foi documentado no Brain: Sim: relatório final e receipt no Brain; script local em /opt/data/scripts.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
