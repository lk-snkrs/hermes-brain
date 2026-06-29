# Approval packet — ZPR WhatsApps pendentes — refresh no-send — 2026-06-28

- Data/hora: 2026-06-28T13:45:10.730571+00:00
- Empresa/área: Zipper OS / Mordomo Hermes
- Origem: Mesa COO 2026-06-28, Decisão 3/3, resposta `Sim`
- Escopo aprovado agora: readback WACLI + refresh do pacote idempotente das pernas WhatsApp pendentes
- Escopo explicitamente não aprovado agora: enviar WhatsApp, reenviar e-mail, pairing/reconectar WACLI, alterar cron/runtime, executar scripts multicanal, contato externo adicional
- Writes externos executados neste follow-through: 0
- values_printed: false

## Readback WACLI executado agora

- Readback: `reports/wacli-health/2026-06-28-zpr-pending-readonly.json`
- `hermes.authenticated=false`, `pessoal.authenticated=false`
- JSON status válido para as duas contas.
- Nenhum pairing, sync, envio, cron mutation ou segredo impresso.

## Pernas pendentes confirmadas

1. **ZPR Flávia Junqueira / Mylene Costa**
   - Handoff: `areas/zipper/handoffs/zpr-flavia-mylene-costa-whatsapp-pendente-20260626.md`
   - Report local: `/opt/data/profiles/mordomo/reports/zpr_flavia_mylene_costa_20260626.json`
   - Estado verificado no report: `ok=true`, `partial=true`, `summary.email=true`, `summary.whatsapp=false`.
   - WhatsApp blocker: `wacli_pessoal_not_authenticated`.
   - Readback WhatsApp no report: `whatsapp_readback.ok=false`.
   - E-mail já enviado/verificado no handoff; não reenviar e-mail.
   - PDF WhatsApp-safe selecionado no report: `whatsapp_safe=true`; values_printed=false.

2. **ZPR Ivan Grilo / Fabiana Herani**
   - Handoff: `areas/zipper/handoffs/zpr-ivan-grilo-fabiana-herani-whatsapp-pendente-20260626.md`
   - Report local: `/opt/data/profiles/mordomo/reports/zpr_ivan_grilo_fabiana_herani_20260626.json`
   - Estado verificado no report: `ok=true`, `partial=true`, `summary.email=true`, `summary.whatsapp=false`.
   - WhatsApp blocker: `wacli_pessoal_not_authenticated`.
   - Readback WhatsApp no report: `whatsapp_readback.ok=false`.
   - E-mail já enviado/verificado no handoff; não reenviar e-mail.
   - PDF WhatsApp-safe selecionado no report: `whatsapp_safe=true`; values_printed=false.

## Plano de recuperação idempotente — no-send preparado

Quando WACLI estiver autenticado e Lucas aprovar explicitamente o envio WhatsApp-only, executar apenas este fluxo:

1. Fazer novo readback WACLI `pessoal` com `auth status --json`; continuar somente se `authenticated=true`.
2. Fazer readback local dos dois reports/handoffs e confirmar que:
   - `summary.email=true` permanece como já enviado;
   - `summary.whatsapp=false` ou `whatsapp_readback.ok=false` permanece pendente;
   - nenhum report final `ok=true, partial=false` posterior substituiu o estado parcial.
3. Antes de qualquer envio, verificar duplicidade local/WhatsApp: texto + PDF exatos já enviados (`from-me`); se já existirem, marcar `already_sent` e não reenviar.
4. Enviar somente a perna WhatsApp texto + PDF para os casos ainda pendentes, usando payload original dos scripts/handoffs.
5. Não chamar Gmail send, não usar `--force`, não alterar cron, não fazer pairing no mesmo fluxo.
6. Após envio aprovado, fazer sync/readback e atualizar queue/report com `email=already_sent/skipped`, `whatsapp=true`, `partial=false` apenas se texto+PDF forem verificados.
7. Registrar receipt final com external writes=WhatsApp only, ids/readback sanitizados e `values_printed=false`.

## Comandos/artefatos bloqueados até aprovação separada

- Scripts candidatos: `/opt/data/profiles/mordomo/scripts/send_zpr_flavia_mylene_costa_20260626.py` e `/opt/data/profiles/mordomo/scripts/send_zpr_ivan_grilo_fabiana_herani_20260626.py`.
- Os scripts atuais são multicanal. Para recuperação WhatsApp-only, não executar o caminho normal sem wrapper/patch temporário aprovado, porque o código também prepara Gmail e pode sobrescrever reports.
- Bloqueado: `--force`, Gmail send, reenvio de e-mail, pairing WACLI, cron mutation, cliente/colecionador contact fora do payload original.

## Próximo gate

Status atual: **prepared_blocked_for_send**.

Para mandar os WhatsApps depois, faltam duas condições:

1. WACLI `pessoal` autenticado (`authenticated=true`) em readback novo.
2. Aprovação explícita de Lucas para `enviar somente os 2 WhatsApps ZPR pendentes, sem reenviar e-mail`, ou payload/escopo equivalente.

Rollback se um wrapper/patch WhatsApp-only for aprovado depois: manter backup do script/report/queue antes da mudança, restaurar backup e revalidar queue/report; se WhatsApp já tiver sido enviado e verificado, rollback técnico não apaga mensagem externa, apenas corrige estado local.

## Evidência

- `areas/zipper/operacoes/approval-packets/zpr-whatsapp-pendentes-recovery-idempotente-2026-06-27.md`
- `reports/wacli-health/2026-06-28-zpr-pending-readonly.json`
- `areas/zipper/handoffs/zpr-flavia-mylene-costa-whatsapp-pendente-20260626.md`
- `areas/zipper/handoffs/zpr-ivan-grilo-fabiana-herani-whatsapp-pendente-20260626.md`
- `/opt/data/profiles/mordomo/reports/zpr_flavia_mylene_costa_20260626.json`
- `/opt/data/profiles/mordomo/reports/zpr_ivan_grilo_fabiana_herani_20260626.json`
