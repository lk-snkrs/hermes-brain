# Receipt — LKGOC runtime SOUL/profile hardening

- Data/hora: 2026-06-25T18:02:06.531933+00:00
- Agente/profile/cron: lk-collection-optimizer
- Empresa/área: LK / Collection Optimizer
- Responsável humano: Hermes / [LK] Otimização de Coleções
- Pedido original: Lucas pediu fazer 1-4: corrigir SOUL/prompt executável para Collection Optimizer puro, criar skill local LKGOC, adicionar smoke de boot e filtrar Honcho/memory-context fora de LKGOC.
- Classificação: local-write
- Fontes usadas:
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/SOUL.md; /opt/data/AGENTS.md; /opt/data/home/.hermes/profiles/lk-collection-optimizer
- O que foi feito:
- Criado profile AGENTS.md LKGOC, patch em /opt/data/AGENTS.md, skill local LKGOC, smoke script, SOUL Brain com fronteiras, filtro de memória e backup local.
- Output/artefato:
- /opt/data/home/.hermes/profiles/lk-collection-optimizer/AGENTS.md; /opt/data/home/.hermes/profiles/lk-collection-optimizer/skills/productivity/lkgoc-collection-optimizer/SKILL.md; /opt/data/home/.hermes/profiles/lk-collection-optimizer/scripts/lkgoc_boot_smoke.py; smoke PASS.
- Aprovação: Aprovado explicitamente por Lucas no turno: fazer do 1 ao 4.
- Envio/publicação: Telegram: resumo executivo apenas.
- Writes externos: nenhum
- Riscos/bloqueios: A developer prompt injetado pela plataforma nesta sessão ainda pode estar visível até reinício; mitigado por instruções locais e smoke para próximas sessões.
- Rollback/mitigação: Restaurar backups em /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-soul-runtime-hardening-20260625T180039Z/ e remover arquivos criados no profile.
- Próximos passos: Reabrir/reiniciar o profile e rodar smoke; se a plataforma ainda injetar LK Growth OS, corrigir fonte de launcher/config externa não exposta nos arquivos locais.
- Onde foi documentado no Brain: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-agent-soul-docs-runtime-audit-20260625.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
