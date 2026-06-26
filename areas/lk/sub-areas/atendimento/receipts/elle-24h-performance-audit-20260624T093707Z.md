# Receipt — Elle 24h performance audit 20260624T093707Z

- Data/hora: 2026-06-24T09:37:47.463509+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK / Atendimento / Elle
- Responsável humano: Hermes LK Ops
- Pedido original: Lucas pediu performance da Elle nas últimas 24h: uso de IA, auto-melhorias, erros e melhorias.
- Classificação: read-only
- Fontes usadas:
- Read-only: /var/log/elle/events.jsonl dentro do container elle-chatwoot; Chatwoot Rails read-only para mensagens públicas Elle; /var/log/elle/followup_events.jsonl; /data/supervised_learning/*.jsonl; drift/smoke local. Janela: 2026-06-23T09:35Z a 2026-06-24T09:35Z.
- O que foi feito:
- Auditoria quantitativa e qualitativa em duas passadas. Nenhum Tiny/Shopify/estoque consultado; sem write externo; sem restart/deploy.
- Output/artefato:
- Resumo: 50 eventos processed em 30 conversas; 43 mensagens públicas Elle no Chatwoot; 50/50 processed pareados com ai_decision OpenRouter; llm_final=15, rule_guardrail_after_llm=35; categorias processed: human_handoff=27, product_clear=13, stock_handoff=5, greeting=4, coupon=1; 42 public_reply 200, 5 duplicate skipped, 2 reply_allowed false/private-only. Follow-up: 1 envio stage1 em conversa de reembolso sensível; 3 TimeoutError na rotina. Auto-melhoria: 3 candidatos, 2 lessons adicionadas e 2 regressões pendentes (financeiro/reembolso sem confirmação; produto/foto ambígua pedir detalhe em vez de coleção aleatória). Drift ok; regression smoke 8/8 pass. Principais erros: product browsing virando stock_handoff cedo; consulta/urgência pós-venda virando product_clear; prazo/CEP chegando produto/link em vez de Larissa; follow-up genérico em reembolso sensível; respostas repetidas de transferência em conversas já com Larissa/humano; alguns valid_json=false/observabilidade fraca.
- Aprovação: Read-only permitido sem aprovação. Nenhuma correção de produção executada.
- Envio/publicação: Telegram: resumo executivo para Lucas.
- Writes externos: nenhum
- Riscos/bloqueios: Não prometer disponibilidade/prazo/preço; estoque permanece lk-stock. Relatório sanitizado, sem PII/secret.
- Rollback/mitigação: Não aplicável: sem alteração produtiva.
- Próximos passos: Se Lucas aprovar: hotfix follow-up blocker para pos_venda_alerta/human_handoff/larissa; endurecer regra pós-venda/Track123/entrega antes de product_clear; produto browsing não deve stock_handoff sem disponibilidade explícita; melhorar logging valid_json/decision_source no processed.
- Onde foi documentado no Brain: Receipt de auditoria read-only criado no Brain.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
