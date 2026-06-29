# Receipt — Honcho all-agents post-repair audit

- Data/hora: 2026-06-28T18:33:28.269395+00:00
- Agente/profile/cron: Hermes default / Honcho audit
- Empresa/área: Operações Hermes / Memória Honcho
- Responsável humano: Hermes Agent
- Pedido original: Lucas pediu novo audit para verificar se os agentes voltaram a usar Honcho corretamente.
- Classificação: local-write
- Fontes usadas:
- reports/governance/honcho-all-agents-post-repair-audit-2026-06-28.md; config.yaml/honcho.json; hermes memory status por profile; AGENTS/SOUL; skill local honcho-memory-operations; gateway watchdog; Honcho context/search current probes.
- O que foi feito:
- Auditei 17 profiles quanto a configured, active/functioning, protocol_aware e roster runtime. Validei provider honcho, honcho.json, skill local, bloco Honcho no topo de AGENTS/SOUL, memory status e gateways gerenciados. Rodei secret scan nos artefatos.
- Output/artefato:
- 17/17 profiles passaram configured+active+protocol-aware. Missing gates: 0. Gateway count issues: 0 nos gerenciados. Watchdog e cron OK. Secret scan: 0 hits. values_printed=false.
- Aprovação: Auditoria local/read-only com escrita de report/receipt; sem writes externos.
- Envio/publicação: Resumo ao Lucas no Telegram.
- Writes externos: 0
- Riscos/bloqueios: Critério useful só se comprova em próximos turnos reais; Honcho ainda pode retornar ruído semântico e deve ser tratado como ruído conforme protocolo.
- Rollback/mitigação: Não aplicou mudança nova além de report/receipt; correção anterior tem backups em /opt/data/backups/honcho-*.
- Próximos passos: Monitorar comportamento dos agentes; se algum ignorar Honcho em decisão dependente de histórico, auditar prompt/truncation daquele profile.
- Onde foi documentado no Brain: Report JSON/MD e receipt atual.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
