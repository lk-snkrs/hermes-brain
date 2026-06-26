# Receipt — LK Chatwoot canonical project folder

- Data/hora: 2026-06-10T18:34:39.274462+00:00
- Agente/profile/cron: LK Atendimento / Hermes default
- Empresa/área: LK / Atendimento / Chatwoot
- Responsável humano: Hermes
- Pedido original: Lucas pediu consolidar tudo que foi feito usando LK Atendimento no projeto Chatwoot em uma pasta canônica no Brain.
- Classificação: local-write
- Fontes usadas:
- Brain local areas/lk/sub-areas/atendimento com 77 artefatos Chatwoot; session_search de Chatwoot/LK Atendimento como conferência; sem acessar runtime externo.
- O que foi feito:
- Criada pasta canônica areas/lk/sub-areas/atendimento/projetos/chatwoot com README, CURRENT_STATE, DECISIONS_AND_GUARDRAILS, ARTIFACT_INDEX, TIMELINE, NEXT_STEPS e manifest.json; MAPA de Atendimento atualizado para apontar para o hub.
- Output/artefato:
- Hub canônico local/documental criado; originais preservados; inventário estruturado com categorias, paths, títulos, tracked_by_git e contagem.
- Aprovação: Pedido explícito de Lucas no Telegram: criar pasta canônica com as informações do projeto Chatwoot feitas via LK Atendimento.
- Envio/publicação: Nenhum envio externo.
- Writes externos: 0
- Riscos/bloqueios: Alguns artefatos antigos podem conter nomes de chaves/inspects sanitizados; não foram copiados para a pasta canônica, apenas referenciados no inventário. Rodar secret scan antes de commit/push.
- Rollback/mitigação: Remover a seção Chatwoot canônica do MAPA.md e apagar a pasta projetos/chatwoot se Lucas quiser desfazer a consolidação documental.
- Próximos passos: Revisar com Lucas; depois decidir se commitar/pushar para lk-snkrs/hermes-brain e se adicionar os artefatos Chatwoot ainda locais/untracked.
- Onde foi documentado no Brain: areas/lk/sub-areas/atendimento/projetos/chatwoot/README.md; CURRENT_STATE.md; DECISIONS_AND_GUARDRAILS.md; ARTIFACT_INDEX.md; TIMELINE.md; NEXT_STEPS.md; manifest.json; MAPA.md
- Source confidence: fonte-primária

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
