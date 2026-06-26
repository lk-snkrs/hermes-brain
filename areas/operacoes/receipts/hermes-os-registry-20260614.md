# Receipt — Hermes OS Registry — snapshot canônico de OS/camadas operacionais

- Data/hora: 2026-06-14T23:52:31.636426+00:00
- Agente/profile/cron: Hermes default
- Empresa/área: Operações / Runtime Governance
- Responsável humano: Hermes Agent
- Pedido original: Lucas pediu criar um mapa dos OS rodando hoje no Hermes.
- Classificação: local-write
- Fontes usadas:
- /proc/*/environ + cmdline; /opt/data/cron/jobs.json; /opt/data/profiles/*/cron/jobs.json
- O que foi feito:
- Criado registry canônico em areas/operacoes/runtime/hermes-os-registry-2026-06-14.md e indexado no MAPA de Operações.
- Output/artefato:
- areas/operacoes/runtime/hermes-os-registry-2026-06-14.md; areas/operacoes/MAPA.md
- Aprovação: Pedido direto de Lucas para criar o mapa; escopo local/documental/read-only.
- Envio/publicação: Resposta manual no Telegram após verificação.
- Writes externos: nenhum
- Riscos/bloqueios: Snapshot pode ficar stale; antes de afirmar estado vivo, revalidar processos e registries. Registry não autoriza writes externos/prod.
- Rollback/mitigação: Remover a linha adicionada em areas/operacoes/MAPA.md e apagar/restaurar o arquivo do registry se necessário.
- Próximos passos: Opcional: transformar em rotina/watchdog read-only silent-OK após aprovação de cadência/kill criteria.
- Onde foi documentado no Brain: areas/operacoes/runtime/hermes-os-registry-2026-06-14.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
