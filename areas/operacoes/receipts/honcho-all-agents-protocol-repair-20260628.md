# Receipt — Honcho all-agents protocol repair after Lucas reported agents stopped using Honcho

- Data/hora: 2026-06-28T18:27:21.649403+00:00
- Agente/profile/cron: Hermes default / Honcho control-plane
- Empresa/área: Operações Hermes / Memória Honcho
- Responsável humano: Hermes Agent
- Pedido original: Lucas reportou: “Vários agentes pararam de usar o Honcho”.
- Classificação: local-write
- Fontes usadas:
- honcho-memory-operations skill; live config.yaml/honcho.json audit; hermes memory status; profile AGENTS/SOUL; gateway roster/watchdog; Honcho context/search probes.
- O que foi feito:
- Auditei 17 profiles: provider honcho e honcho.json presentes; identifiquei falha protocol_aware em perfis com boot sem bloco Honcho e skill local ausente. Copiei skill honcho-memory-operations para 16 profiles; inseri bloco HONCHO_USAGE_PROTOCOL_ENFORCEMENT no topo de AGENTS/SOUL; atualizei skill global; reiniciei/recarreguei 12 gateways especialistas gerenciados; validei roster e memory status.
- Output/artefato:
- 17/17 profiles com provider=honcho e honcho_json=true; 17/17 com bloco Honcho no topo de AGENTS/SOUL; 16/16 profiles com skill local honcho-memory-operations; 13/13 gateways esperados vivos; memory status provider honcho available nos perfis amostrados; values_printed=false.
- Aprovação: Correção local/procedural/runtime leve a partir de falha reportada por Lucas; sem writes externos, sem secrets, sem Docker/VPS/Traefik.
- Envio/publicação: Telegram: resumo final nesta conversa.
- Writes externos: 0
- Riscos/bloqueios: Honcho search ainda retorna ruído/contaminação operacional de pedidos/clientes; agentes foram instruídos a tratar ruído como sinal de degradação e preferir Brain/fonte viva, não repetir dados sensíveis.
- Rollback/mitigação: Backups em /opt/data/backups/honcho-all-agents-protocol-repair-20260628T182109Z, honcho-skill-recopy-after-propagation-note-20260628T182126Z e honcho-protocol-move-to-top-20260628T182456Z.
- Próximos passos: Monitorar próximos turnos dos especialistas; se algum ainda ignorar Honcho, auditar prompt/truncation específico e criar teste de comportamento por profile.
- Onde foi documentado no Brain: Receipt atual; skill honcho-memory-operations atualizada; AGENTS/SOUL dos profiles.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
