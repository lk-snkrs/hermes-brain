# CRM de interesse por artista + negative-fit — Zipper

Data: 2026-06-05
Contexto: correção operacional de Lucas para o Mordomo/Zipper.

## Decisão operacional

Toda pessoa que demonstrar interesse por um artista deve ser registrada por artista, canal e evidência. Esse registro deve alimentar campanhas futuras, por exemplo: se alguém se interessou por Flávia Junqueira, pode ser candidata a convite de exposição da artista em agosto.

Mas se a pessoa respondeu que não faz sentido por dinheiro/orçamento, ela não deve ser chamada automaticamente para novidades/campanhas futuras, mesmo que tenha demonstrado interesse antes.

## Status/supressão

- `do_not_send_novidades = 0`: elegível para revisão/campanha futura, desde que o contexto seja apropriado e Lucas aprove o envio.
- `do_not_send_novidades = 1`: suprimir de novidades/campanhas automáticas.
- `suppression_reason = budget_decline`: a pessoa sinalizou falta de orçamento, valores acima das posses, fora do budget, sem condições etc.

Essa supressão é de campanha/novidades, não necessariamente bloqueio absoluto de relacionamento. Lucas pode reaprovar contato específico depois.

## Banco local

Fonte local atual:

`/opt/data/profiles/mordomo/state/mordomo_crm.sqlite`

Tabelas criadas/atualizadas:

- `zipper_artist_interest`: uma linha por `contact_key + artist`.
- `zipper_artist_interest_events`: timeline de evidências, leads, PDFs enviados, follow-ups e respostas.
- `zipper_campaign_suppression`: bloqueios de campanha por contato, especialmente `budget_decline`.

Relatórios:

- `/opt/data/profiles/mordomo/reports/zipper_artist_interest_backfill_last.json`
- `/opt/data/profiles/mordomo/reports/zipper_artist_interest_thread_audit_last.json`

Scripts:

- `/opt/data/scripts/zipper_artist_interest_backfill.py`
- `/opt/data/scripts/zipper_artist_interest_thread_audit.py`

## Query prática

Lista de pessoas interessadas em uma artista, excluindo quem não deve receber novidades:

```sql
select contact_label, contact_name, email, whatsapp_jid, status, last_interaction_at
from zipper_artist_interest
where artist = 'Flávia Junqueira'
  and coalesce(do_not_send_novidades, 0) = 0
order by last_interaction_at desc;
```

Lista de suprimidos por orçamento:

```sql
select contact_label, artist, reason, evidence_summary, updated_at
from zipper_campaign_suppression
where status = 'do_not_send_novidades'
  and reason = 'budget_decline'
order by updated_at desc;
```

## Classificação de respostas

Marcar `budget_decline` quando houver frases como:

- “valores acima das minhas posses”
- “fora do meu orçamento”
- “não tenho orçamento/condição”
- “muito caro”
- “quem sabe em outro momento” quando em contexto de impossibilidade de compra

Não marcar como budget decline quando a pessoa apenas diz:

- “vou olhar”
- “estou em dúvida”
- “qualquer coisa entro em contato”
- “vou ver com cliente/marido/sócio”

Esses casos ficam como interesse em aberto. Quando a resposta for claramente “vi/olhei, estou em dúvida, qualquer coisa entro em contato”, sem preço/disponibilidade/negociação/recusa, o Mordomo pode responder automaticamente com encerramento curto e educado, por exemplo: “Perfeito, {{nome}}. Fico à disposição por aqui caso queira conversar sobre alguma obra específica ou tirar qualquer dúvida. Obrigado!”. Depois deve reagendar um follow-up suave para 2 meses, porque o momento atual pode não ser o certo, mas pode voltar a fazer sentido depois.

## Guardrail

Campanha futura por artista deve consultar `zipper_artist_interest` e excluir `do_not_send_novidades=1` antes de gerar lista de envio. Envio externo continua approval-gated por Lucas, salvo fluxos estreitos já aprovados.

## Correção de backfill — 2026-06-05

Não confiar apenas em `mordomo_followup_queue.json` e `zipper_zpr_enquiry_leads.jsonl`: isso subconta artistas com histórico anterior/manual. Para montar universo de interessados por artista, varrer também:

- `/opt/data/profiles/mordomo/reports/*<artista>*send*.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/zipper/logs/zpr_pdf_sends.jsonl`
- Brain Zipper `inbox/caso-*`, `inbox/site-leads/*`, `inbox/email-intake/*`, `inbox/zpr-enquiry/*`
- histórico WhatsApp/Gmail quando o contato tiver JID/thread

Manter duas contagens separadas:

- universo bruto de interesse/evidência, incluindo casos sem canal completo ou que precisam revisão;
- universo acionável para campanha, com canal utilizável, dedupe por e-mail/WhatsApp/nome e exclusão de `do_not_send_novidades`.

Para Flávia Junqueira, a primeira varredura estreita retornou 8 e estava errada por subcontagem. A varredura ampla local em 2026-06-05 encontrou 28 linhas brutas e 17 contatos únicos com canal utilizável antes de revisão humana final.
