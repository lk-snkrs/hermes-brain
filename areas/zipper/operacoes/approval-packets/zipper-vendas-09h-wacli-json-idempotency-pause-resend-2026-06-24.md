# Approval packet — Zipper OS vendas 09h — WACLI JSON/idempotência/pausa/reenvio

- Data/hora: 2026-06-24T09:24:00Z
- Empresa/área: Zipper OS / Operações Hermes
- Job vivo: `Zipper OS vendas 09h WhatsApp/email` (`357d40a5863e`)
- Schedule vivo: `0 12 * * 1-5` UTC = 09h BRT
- Modo atual: cron ativo, `deliver=local`, script `zipper_weekday_sales_report_watchdog.py`, modo no-agent
- Último status vivo antes deste packet: `error` em 2026-06-23T12:00:47Z por stdout não-JSON do WACLI
- Escopo aprovado por Lucas nesta Mesa: validação read-only/no-send + packet de idempotência/pausa/reenvio seguro
- Writes externos executados neste follow-through: 0
- values_printed: false

## Evidência verificada

1. Histórico/ledger verificado:
   - `empresa/contexto/decision-sequences/2026-06-24.jsonl` registra `mesa-2026-06-24-1` com `Fazer` limitado a diagnóstico/readback/packet local sanitizado.
   - Receipt existente: `areas/operacoes/receipts/daily-intelligence-zipper-wacli-json-sanitizer-20260624.md` documenta patch local já feito no parser WACLI sem reenvio.
2. Runtime vivo:
   - `cron list --all`: job `357d40a5863e` continua ativo, próximo run 2026-06-24T12:00:00Z, último run `error`.
3. Validação local/no-send executada agora:
   - `python3 -m py_compile /opt/data/scripts/zipper_sales_report_external_delivery.py /opt/data/scripts/zipper_weekday_sales_report_watchdog.py`: OK.
   - `/opt/data/scripts/zipper_weekday_sales_report_watchdog.py --dry-run`: exit 0; gerou readiness/dry-run; nenhum WhatsApp/e-mail enviado.
   - Período dry-run: `2026-06-01..2026-06-23`; resumo sanitizado: 4 linhas, total R$ 175.000,00, 1 artista distinto.
   - Artefatos locais do período em `/opt/data/hermes_bruno_ingest/local_sql/zipper_sales_report/artifacts/2026-06-01_2026-06-23/`: `report.json`, `whatsapp.txt`, `email.html`.
   - Secret scan local dos artefatos visíveis: `secret_pattern_hits=0`; marker interno presente no HTML; `values_printed=false`.
4. Readback WACLI read-only:
   - Account `hermes`: auth status JSON lido, `authenticated=false`.
   - Account `pessoal`: auth status JSON lido, `authenticated=false`.
   - Alvo aprovado `[ZPR] IA Bot`: read-only lookup não confirmou match com o JID aprovado enquanto `hermes` está não autenticado.

## Diagnóstico operacional

O patch local já evita traceback/JSONDecodeError cru, mas o job ainda está tecnicamente ativo e o próximo run está agendado. O dry-run passa porque ele não chama envio real. O readback WACLI mostra que as contas de WhatsApp (`hermes` e fallback `pessoal`) não estão autenticadas agora.

Risco importante: se o cron rodar com `--send`, o script atual pode tentar o WhatsApp, tratar `not authenticated` como falha recuperável do canal WhatsApp e ainda enviar e-mail interno, gerando `partial_sent_email_only_whatsapp_unauthenticated`. Portanto, a blindagem real antes de 09h BRT exige aprovação separada para pausar ou colocar gate no job antes do próximo run.

## Idempotência atual

- Idempotency key do período atual (`2026-06-01..2026-06-23`): `10223464e5cd718bc1ceb2579733c276371059f7f85af1b740672239bc416b4b`.
- `state.json` tem 24 registros enviados anteriores; último envio registrado: `2026-06-01..2026-06-21` com status `partial_sent_email_only_whatsapp_unauthenticated` em 2026-06-22T12:00:34Z.
- Não há `sent_record` confirmado para a key atual no readback sanitizado; o dry-run não marca como enviado.
- Sem `--force`, duplicidade só é bloqueada quando WhatsApp e e-mail já constam como enviados para a key; para key nova/sem registro, o próximo `--send` tentará entrega.

## Clarificação de política — Lucas

Lucas perguntou em 2026-06-24 se, quando o WACLI quebrar, **enviar apenas por e-mail é OK**.

Interpretação operacional recomendada: **sim, para este report interno do Zipper OS, e-mail-only é um fallback aceitável quando WhatsApp/WACLI falhar**, desde que:

1. seja somente para os destinatários internos já aprovados do report Zipper;
2. o gerador/QA do conteúdo passe (`py_compile`, dry-run, secret scan e marker/HTML OK);
3. o erro de WhatsApp seja registrado de forma sanitizada (`values_printed=false`);
4. o estado/idempotência marque claramente `email=sent` e `whatsapp=failed/skipped`, sem mascarar como entrega completa;
5. Telegram só alerte se houver ação necessária — por exemplo WACLI continua quebrado, reenvio WhatsApp pendente ou risco operacional real;
6. não usar `--force` nem reenviar e-mail duplicado sem aprovação explícita.

Isto muda a decisão preferida: não é necessário pausar o cron apenas porque o WACLI está quebrado, se o objetivo de negócio for garantir que o report interno chegue por e-mail.

## Opções de decisão atualizadas

### Opção A — Aplicar fallback email-only quando WACLI quebrar

- Ação: patch local no delivery layer para tratar falha WhatsApp/WACLI como canal degradado e seguir com e-mail interno quando o e-mail ainda não foi enviado.
- Escopo: local script write + backup + `py_compile` + `--dry-run` + teste com simulação/no-send do erro WACLI + readback de cron.
- Efeito: próximo run pode enviar e-mail mesmo se WhatsApp quebrar; status deve ficar `partial_sent_email_only_whatsapp_failed` ou equivalente, nunca `sent` completo.
- Rollback: reverter diff do script.
- Risco: é mudança de comportamento em rotina de envio externo interno; requer aprovação explícita de apply.

### Opção B — Pausa preventiva do cron antes do run de hoje

- Ação: pausar somente o job `357d40a5863e` até autenticação WACLI e decisão de reenvio.
- Escopo: `cronjob pause 357d40a5863e` + readback `cron list`.
- Efeito: impede WhatsApp/e-mail automático às 09h BRT.
- Rollback: `cronjob resume 357d40a5863e` após validação/autorização.
- Risco: relatório interno de hoje não sai automaticamente; pode ser reenviado depois com approval separado.

### Opção C — Não mexer no script agora, aceitar comportamento parcial atual

- Ação: nenhuma mudança agora; monitorar próximo run.
- Efeito: preserva rotina atual.
- Risco: hoje o script já faz e-mail-only para alguns casos de `not authenticated`, mas não para todo WACLI quebrado/non-JSON; falhas diferentes ainda podem bloquear o e-mail.

## Reenvio seguro depois da pausa/gate

Reenvio real só deve ser considerado depois de:

1. WACLI account escolhido autenticado (`authenticated=true`) e alvo aprovado confirmado por read-only.
2. Dry-run do período desejado OK.
3. Confirmação explícita de Lucas do canal e payload: WhatsApp, e-mail, ambos, ou nenhum.
4. Sem `--force` salvo se Lucas aprovar reenvio duplicado conscientemente.
5. Receipt final com external writes, canais, idempotency key e verificação pós-envio.

## Recomendação

A recomendação operacional é **Opção A agora** se a intenção for realmente blindar antes do run de 09h BRT, porque é reversível, mínima e não altera script nem envia mensagens. A Opção B é melhor como correção estrutural depois, mas cruza mudança de comportamento do job. A Opção C aceita risco de e-mail parcial hoje.
