# Receipt — Hermes Central Auth Broker — mandatory skill and all-agent propagation

- Data/hora: 2026-06-28T16:57:22.131202+00:00
- Agente/profile/cron: Hermes default / operações runtime
- Empresa/área: Operações Hermes / Governança de integrações
- Responsável humano: Hermes Agent
- Pedido original: Lucas perguntou se todos os agentes foram ensinados a usar obrigatoriamente o Hermes Central Integration Auth Broker e se havia skill dedicada.
- Classificação: local-write
- Fontes usadas:
- Pedido direto de Lucas; skill library; AGENTS.md raiz/scripts/profiles/Brain; smoke central; py_compile.
- O que foi feito:
- Criei a skill devops/hermes-central-integration-auth-broker e propaguei bloco obrigatório HERMES_CENTRAL_INTEGRATION_AUTH_BROKER para 19 AGENTS.md ativos/canônicos.
- Output/artefato:
- Skill disponível e verificada; 19/19 AGENTS com bloco obrigatório exatamente 1 vez; smoke central OK; Linear marcado como excluído por decisão do Lucas.
- Aprovação: Pedido direto de Lucas para esclarecer/garantir ensino obrigatório aos agentes; mudanças locais/documentais sem writes externos.
- Envio/publicação: Telegram: resumo final nesta conversa.
- Writes externos: 0
- Riscos/bloqueios: Mudança é local/documental/procedural; runtime já estava saudável. Reativação Linear exige pedido explícito.
- Rollback/mitigação: Restaurar AGENTS.md a partir de /opt/data/backups/central-auth-broker-mandatory-skill-propagation-20260628T165621Z/ e remover skill devops/hermes-central-integration-auth-broker se necessário.
- Próximos passos: Nenhum obrigatório; opcionalmente auditar crons/scripts antigos por API raw residual em ciclo de higiene.
- Onde foi documentado no Brain: Skill devops/hermes-central-integration-auth-broker; receipt atual; report de governança já existente atualizado.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
