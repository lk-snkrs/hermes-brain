# LC Mordomo OS — Zipper canonical CRM local

Data: 2026-06-06
Escopo: camada local derivada/read-only para normalizar contatos, interesses por artista e follow-ups do Zipper.

## Resultado

Criado/recriado o builder local:

- Script: `/opt/data/profiles/mordomo/scripts/zipper_canonical_store_build.py`
- SQLite: `/opt/data/profiles/mordomo/state/zipper_canonical.sqlite`
- Summary: `/opt/data/profiles/mordomo/state/zipper_canonical_summary.json`

A camada é derivada de arquivos locais; não envia mensagens, não escreve Supabase e não altera fonte externa.

## Tabelas canônicas

- `contact`: cliente/contato, rótulo operacional, hash e referência mascarada.
- `lead_enquiry`: origem do lead, canal, conta e resumo.
- `artist_interest`: vínculo contato ↔ artista, PDF/material e status do interesse.
- `followup`: fila operacional normalizada, due_at, status, intenção, risco e draft.
- `sent_action`: ações enviadas/registradas, com payload bruto preservado localmente.
- `suppression`: casos resolvidos/suprimidos.
- `decision_packet`: casos que precisam decisão ou falharam.
- `meta`: build/source/version.

## Verificação

- `python3 -m py_compile zipper_canonical_store_build.py`: OK
- Builder executado duas vezes: contagens estáveis/idempotentes.
- `pragma integrity_check`: `ok`

Contagens finais:

- contacts: 123
- lead_enquiries: 126
- artist_interests: 36
- followups: 126
- sent_actions: 150
- suppressions: 10
- decision_packets: 18

Checagens operacionais:

- Interesse Flávia Junqueira presente: 1
- Follow-ups `waiting_client` com due_at: 6
- Pós-PDF seguros aguardando cliente: 5
- Decision packets pendentes/falhas: 18

## Observações

A fila operacional `mordomo_followup_queue.json` ainda é a origem runtime atual. O SQLite canônico agora permite consultar CRM/interesses/follow-ups sem misturar conceitos, mas o executor ainda precisa ser promovido para usar essa camada como fonte de decisão e reconciliação.

## Próximo passo recomendado

Promover o runner do Mordomo OS para, em cada ciclo:

1. Rebuildar o `zipper_canonical.sqlite` localmente.
2. Consultar `followup` + `artist_interest` para candidatos A1/A2.
3. Reconciliar com histórico WhatsApp/e-mail antes de envio.
4. Auto-enviar apenas follow-ups seguros pós-PDF.
5. Registrar `sent_action` e atualizar a fila runtime.
6. Escalar só decisão/falha/material question para Lucas.
