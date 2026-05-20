# Zipper — Decisões

- Vendas reais ficam no banco Zipper Vendas `pcstqxpdzibheuopjkas`, tabela `vendas_tango`.
- SPITI/leilão usa banco separado `rmdugdkantdydivgnimb`.
- Nunca confundir vendas de galeria com dados de leilão.
- Comunicação com colecionadores exige aprovação Lucas/Osmar.
- 2026-05-18: Mordomo Hermes deve priorizar Zipper e SPITI antes da LK, operando em contato único com Lucas e roteando/salvando no cérebro/Supabase correto por contexto.
- 2026-05-18: Para Zipper/SPITI, evoluir o schema atual do Supabase; não criar CRM paralelo. Usar views/consultas primeiro e só adicionar tabelas/campos mínimos após lacuna clara.
- 2026-05-18: Segmentação por artista deve considerar sinais negativos/desfit. Interesse artístico isolado não autoriza envio; exemplo: cliente que achou Flávia Junqueira cara demais deve ser excluído ou ir para revisão manual.
- 2026-05-18: Em aprovações de PRD/plano, reportar sempre os próximos passos concretos, na ordem, com critério de conclusão; Lucas corrigiu que apenas dizer o que foi salvo é insuficiente.
