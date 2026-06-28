# Approval packet — ZPR WhatsApps pendentes — recuperação idempotente no-send

- Data/hora: 2026-06-27T09:38:54+00:00
- Empresa/área: Zipper OS / Mordomo Hermes
- Origem: Mesa COO 2026-06-27, Decisão 1/4, botão `Fazer`
- Escopo aprovado agora: readback WACLI + preparação idempotente das pernas WhatsApp pendentes
- Escopo explicitamente não aprovado agora: enviar WhatsApp, reenviar e-mail, pairing/reconectar WACLI, alterar cron/runtime, contato externo adicional
- Writes externos executados neste follow-through: 0
- values_printed: false

## Readback executado

- WACLI health read-only em `reports/wacli-health/2026-06-27.md`.
- Resultado atual: `hermes.authenticated=false`; `pessoal.authenticated=false`; JSON status lido com sucesso.
- Nenhum pairing, sync, envio, cron mutation ou segredo impresso.

## Pernas pendentes confirmadas

1. ZPR Flávia Junqueira / Mylene Costa
   - Handoff: `areas/zipper/handoffs/zpr-flavia-mylene-costa-whatsapp-pendente-20260626.md`
   - Report local: `/opt/data/profiles/mordomo/reports/zpr_flavia_mylene_costa_20260626.json`
   - Estado verificado: e-mail enviado/verificado; WhatsApp pendente por `wacli_pessoal_not_authenticated`.
   - Idempotência no report: `existing_email_count=0` antes do primeiro envio; `existing_whatsapp_exact=false`; resumo final `email=true`, `whatsapp=false`, `partial=true`.
   - PDF WhatsApp safe selecionado no report: fallback `whatsapp_safe=true`; values_printed=false.

2. ZPR Ivan Grilo / Fabiana Herani
   - Handoff: `areas/zipper/handoffs/zpr-ivan-grilo-fabiana-herani-whatsapp-pendente-20260626.md`
   - Report local: `/opt/data/profiles/mordomo/reports/zpr_ivan_grilo_fabiana_herani_20260626.json`
   - Estado verificado: e-mail enviado/verificado; WhatsApp pendente por `wacli_pessoal_not_authenticated`.
   - Idempotência no report: `existing_email_count=0` antes do primeiro envio; `existing_whatsapp_exact=false`; resumo final `email=true`, `whatsapp=false`, `partial=true`.
   - PDF WhatsApp safe no report: `whatsapp_safe=true`; values_printed=false.

## Plano de recuperação idempotente — no-send preparado

Quando WACLI estiver autenticado e Lucas aprovar explicitamente o envio WhatsApp-only, executar apenas este fluxo:

1. Fazer novo readback WACLI `pessoal` com `auth status --json`; continuar somente se `authenticated=true`.
2. Fazer readback local dos dois reports/handoffs e confirmar que:
   - `summary.email=true` permanece como já enviado;
   - `summary.whatsapp=false` ou `whatsapp_readback.ok=false` permanece pendente;
   - nenhum report final `ok=true, partial=false` posterior substituiu o estado parcial.
3. Para cada lead, antes de enviar:
   - confirmar PDF selecionado existe e é WhatsApp-safe;
   - rodar readback de mensagens enviadas (`from-me`) para detectar texto + PDF exatos já enviados;
   - se texto+PDF já existirem, marcar `already_sent` e não reenviar.
4. Enviar somente WhatsApp texto + PDF para os dois casos ainda pendentes, usando o payload original dos scripts/handoffs.
5. Não chamar Gmail send, não usar `--force`, não alterar cron, não fazer pairing no mesmo fluxo.
6. Após envio, fazer sync/readback e atualizar queue/report com `email=already_sent/skipped`, `whatsapp=true`, `partial=false` apenas se texto+PDF forem verificados.
7. Registrar receipt final com external writes=WhatsApp only, ids/readback sanitizados e `values_printed=false`.

## Comandos/artefatos de execução bloqueados até aprovação separada

- Scripts candidatos: `/opt/data/profiles/mordomo/scripts/send_zpr_flavia_mylene_costa_20260626.py` e `/opt/data/profiles/mordomo/scripts/send_zpr_ivan_grilo_fabiana_herani_20260626.py`.
- Atenção: os scripts atuais são multicanal. Para recuperação WhatsApp-only, não executar o caminho normal sem wrapper/patch temporário aprovado, porque o código também prepara Gmail e pode sobrescrever reports. O fluxo correto é wrapper dedicado WhatsApp-only ou patch escopado com backup + rollback.
- Bloqueado: `--force`, Gmail send, reenvio de e-mail, pairing WACLI, cron mutation, cliente/colecionador contact fora do payload original.

## Próximo gate

Status atual: **preparado, ainda bloqueado para envio**.

Para mandar os WhatsApps depois, faltam duas condições:

1. WACLI `pessoal` autenticado (`authenticated=true`) em readback novo.
2. Aprovação explícita de Lucas para `enviar somente os 2 WhatsApps ZPR pendentes, sem reenviar e-mail`, ou payload/escopo equivalente.

Rollback se um wrapper/patch WhatsApp-only for aprovado depois: manter backup do script/report/queue antes da mudança, restaurar backup e revalidar queue/report; se WhatsApp já tiver sido enviado e verificado, rollback técnico não apaga mensagem externa, apenas corrige estado local.
