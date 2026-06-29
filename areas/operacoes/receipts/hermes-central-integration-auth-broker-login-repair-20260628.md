# Receipt — Hermes Central Integration Auth Broker — login/instance repair

- Data/hora: 2026-06-28T16:22:02.449879+00:00
- Agente/profile/cron: Hermes default / operações runtime
- Empresa/área: Operações Hermes / Governança de integrações
- Responsável humano: Hermes Agent
- Pedido original: Corrigir a instância central do Hermes Auth Broker e autenticar/logar as integrações necessárias sem login individual por agente.
- Classificação: infra-sensitive
- Fontes usadas:
- Runtime live /proc; hermes-cli-integrations inventory/smoke; gws auth status; MCP tests; unit tests; Doppler presence checks; approval explícita de Lucas.
- O que foi feito:
- Reautentiquei Google Workspace no diretório central do broker, corrigi scripts hermes_cli_run/hermes_cli_integrations, corrigi Klaviyo smoke via broker, adicionei probe Linear read-only, validei runtime/cron/MCP/smokes.
- Output/artefato:
- Report: reports/governance/hermes-central-integration-auth-broker-login-repair-2026-06-28.md; Google Workspace/Klaviyo/Shopify/GitHub/Notion/Sentry/Supabase/Vercel/Cloudflare OK; Linear 401 pendente.
- Aprovação: Aprovação escopada atual de Lucas em 2026-06-28: "Seguir por favor, corrigir a instância e vamos dar login no que for necessário"; escopo limitado a Auth Broker/login central/local, sem writes externos de negócio, com backup/rollback e verificação.
- Envio/publicação: Telegram: resumo final nesta conversa; silent-OK para checks saudáveis.
- Writes externos: 0 writes externos de negócio; OAuth/login central local e arquivos de credencial gws cifrados no runtime central.
- Riscos/bloqueios: Google Workspace agora tem credenciais cifradas centrais; manter diretório 0700 e arquivos 0600. Linear continua inválido HTTP 401 e requer token válido.
- Rollback/mitigação: Restaurar scripts a partir de /opt/data/backups/auth-broker-login-fix-20260628T154052Z/; para Google Workspace, usar gws auth logout/re-auth controlado se necessário.
- Próximos passos: Rotacionar/fornecer LINEAR_API_KEY válido no Doppler se Linear for necessário; não há outro blocker crítico.
- Onde foi documentado no Brain: reports/governance/hermes-central-integration-auth-broker-login-repair-2026-06-28.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
