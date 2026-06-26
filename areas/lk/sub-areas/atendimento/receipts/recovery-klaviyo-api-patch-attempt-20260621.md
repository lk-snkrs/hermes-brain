# Receipt — LK Recovery/Klaviyo — tentativa API PATCH do header webhook

- Data/hora: 2026-06-21T16:27:22.441313+00:00
- Agente/profile/cron: Hermes/default via Doppler-first lk-content
- Empresa/área: LK Sneakers / Atendimento / Recovery
- Responsável humano: Hermes/Operações + LK Atendimento
- Pedido original: Lucas aprovou “Tenta o 2”: tentar correção via endpoint alternativo validado para alinhar o header X-Chatwoot-Token da action Klaviyo 109063868 ao token esperado pelo Chatwoot, sem envio/ativação de flow/campanha e com readback sanitizado.
- Classificação: external-write
- Fontes usadas:
- Klaviyo Flows API GET/PATCH via Doppler-first; Klaviyo developer docs Update Flow Action; Chatwoot PostgreSQL read-only para comparação booleana do token; logs Rails read-only; monitor Recovery 7d
- O que foi feito:
- Preflight GET confirmou action 109063868 live/WEBHOOK e header presente mas divergente; tentativa PATCH aprovada foi executada contra o endpoint beta/documentado sem imprimir valores; variações com revision beta/stable, content-type e payloads settings-only/status/action_type foram rejeitadas pela API; tentativa adicional sem trailing slash retornou 400 exigindo/invalidando attributes.definition; readback final confirmou que o header continua divergente.
- Output/artefato:
- Correção via API não aplicada. Evidência sanitizada: external_write_attempted=true; external_write_succeeded=false; patch_status observados=404 not_found em variações beta/stable iniciais e 400 invalid em endpoint sem trailing slash; readback_status=200; post_header_matches=false; x_chatwoot_token_header_present=true; values_printed=false. Monitor pós-tentativa: Shopify Recovery ativo, Klaviyo/webhook segue 0 conversa em 24h.
- Aprovação: Aprovado por Lucas no Telegram: “Tenta o 2”. Escopo limitado a tentativa de correção via endpoint alternativo validado, com readback/rollback e sem envio, sem campanha, sem flow activation, sem Shopify/Chatwoot DB write e sem restart.
- Envio/publicação: Nenhum envio a cliente; nenhuma campanha/flow ativada; nenhuma mensagem manual.
- Writes externos: Tentativa PATCH Klaviyo executada; API rejeitou e readback confirmou sem mudança efetiva. Sem Shopify write, sem Chatwoot DB write, sem WhatsApp/e-mail send, sem Docker/VPS/gateway restart.
- Riscos/bloqueios: Klaviyo Update Flow Action beta/documentação exige attributes.definition para PATCH de flow-action; GET da action não expõe definition, então a API rejeita settings-only. Continuar tentando payload especulativo pode arriscar corromper configuração do flow; caminho recomendado é UI Klaviyo ou suporte/export oficial com definition completo.
- Rollback/mitigação: Não houve mudança efetiva segundo readback; rollback não necessário. Se uma futura correção for feita via UI, rollback é restaurar o header anterior salvo apenas em sessão segura ou reverter manualmente na UI; não persistir valores em Brain.
- Próximos passos: Recomendado: fazer correção manual via UI Klaviyo na action 109063868, atualizando apenas o header X-Chatwoot-Token, depois rodar monitor de 401/KlaviyoCartJob/conversas/skips. Alternativa técnica só com definition completo validado oficialmente.
- Onde foi documentado no Brain: Receipt local/Brain + ledger decision-sequences; nenhum secret impresso; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
