# Receipt — LK Shopify provider auth repair — Codex credential pool sync

- Data/hora: 2026-06-30T15:13:23.991916+00:00
- Agente/profile/cron: hermes-default
- Empresa/área: Operações Hermes / LK Shopify
- Responsável humano: Hermes
- Pedido original: Lucas pediu: CORRIGIR O LK-SHOPIFY — Provider authentication failed
- Classificação: infra-sensitive
- Fontes usadas:
- Gateway log lk-shopify com openai-codex HTTP 401 token_expired; auth.json profile/default sanitized hash comparison; one-shot model smoke; live process /proc env booleans; Telegram getMe sanitized; broker Shopify smoke read-only
- O que foi feito:
- Backup de /opt/data/profiles/lk-shopify/auth.json e config.yaml; copiado apenas credential_pool.openai-codex do default para lk-shopify; removido providers.openai-codex stale do profile; mantido active_provider=openai-codex; reiniciado somente gateway lk-shopify via scoped SIGTERM + watchdog; nenhum token/secret impresso
- Output/artefato:
- Profile lk-shopify voltou a passar smoke HERMES_HOME=/opt/data/profiles/lk-shopify hermes -z Reply exactly OK; um único gateway vivo; API_SERVER_ENABLED=false; WEBHOOK_ENABLED=false; Telegram getMe username=LKShopify_HermesBot; Shopify LK broker smoke rc=0/status=ok; values_printed=false
- Aprovação: Aprovação escopada inferida do comando direto de Lucas para corrigir o LK-SHOPIFY; escopo limitado ao profile lk-shopify e provider auth/gateway desse profile
- Envio/publicação: Telegram resposta final; OK path com evidência resumida
- Writes externos: 0; somente writes locais em auth.json/receipt e restart local do gateway lk-shopify
- Riscos/bloqueios: Se o Codex default expirar futuramente, lk-shopify pode voltar a falhar; rollback disponível no backup local. Telegram network warnings antigos não foram tratados como incidente separado.
- Rollback/mitigação: Restaurar /opt/data/backups/lk-shopify-codex-auth-repair-20260630T151033Z/auth.json.before para /opt/data/profiles/lk-shopify/auth.json e reiniciar somente lk-shopify; config.yaml backup disponível no mesmo diretório.
- Próximos passos: Nenhum bloqueio atual; monitorar só se novo Provider authentication failed aparecer.
- Onde foi documentado no Brain: Receipt sanitizado criado via Memory OS receipt writer; values_printed=false
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
