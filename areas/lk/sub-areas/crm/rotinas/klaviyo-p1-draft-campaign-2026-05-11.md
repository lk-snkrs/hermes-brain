# LK CRM — Klaviyo P1 Draft Campaign, 2026-05-11

Status: concluído até rascunho Klaviyo pendente. Nenhum envio foi feito.

## Objetivo

Transformar a fila aprovada de curadoria/recompra da loja física em uma ação online segura no Klaviyo, preservando o padrão premium da LK e o bloqueio de envio sem aprovação final de Lucas.

## Escopo executado

- Lista P1 de loja física/Flagship preparada com 9 perfis.
- HTML customer-facing gerado em estética LK/Klaviyo, sem jargão interno como P1, Brain, preview ou sem envio.
- Visual validado em browser antes de integração.
- Lista Klaviyo criada/reutilizada.
- Perfis importados com job completo e 0 falhas.
- Template HTML criado/reutilizado como `CODE` editor.
- Campanha criada/reutilizada em status `Draft`.

## Objetos Klaviyo

- Lista: `LK Phase 5 P1 Loja Física Recompra 2026-05-11`.
- List ID: `U8YCCE`.
- Perfis submetidos: 9.
- E-mails únicos submetidos: 9.
- Profile import job: `V25zUmN1X21haW50ZW5hbmNlLnIzajExSy4xNzc4NTIwNzQ3LkFSM3A5YQ`.
- Import status: `complete`.
- Import failed count: `0`.
- Template: `LK Phase 5 P1 Curadoria Loja Física 2026-05-11`.
- Template ID: `XUSEtu`.
- Campaign draft: `LK Phase 5 P1 Curadoria Loja Física 2026-05-11, DRAFT`.
- Campaign ID: `01KRC1DPTY615GF5FNBPXMPKY6`.
- Campaign message ID: `01KRC1DPVAMF0M9SRSR7RDQX1G`.
- Campaign status: `Draft`.
- Campaign scheduled_at: `None`.
- Campaign send_time: `None`.

## Artefatos de evidência

- `reports/lk-phase5-p1-klaviyo-approved-email-2026-05-11.html`.
- `reports/lk-phase5-p1-klaviyo-approved-email-2026-05-11.md`.
- `reports/lk-phase5-p1-klaviyo-approved-email-2026-05-11.json`.
- `reports/lk-phase5-p1-klaviyo-klaviyo-objects-2026-05-11.md`.
- `reports/lk-phase5-p1-klaviyo-klaviyo-objects-2026-05-11.json`.

## Guardrails confirmados

- Nenhum envio de campanha executado.
- Nenhum agendamento de campanha executado.
- Nenhum flow ativado.
- Nenhum SMS ou WhatsApp executado nesta etapa.
- PII bruta ficou fora do relatório versionado.
- A campanha permanece pendente para revisão/aprovação final no Klaviyo.

## Observação operacional

A API do Klaviyo permitiu criar o template HTML e o rascunho da campanha, mas a associação síncrona simples do template ao `campaign_message` pode exigir seleção manual do template no editor do Klaviyo ou patch específico de relacionamento antes do envio final.

Regra para o próximo operador: antes de qualquer envio, abrir o rascunho no Klaviyo, confirmar que o HTML aprovado está aplicado ao message, conferir assunto/remetente/lista, revisar destinatários e pedir aprovação explícita de Lucas para enviar ou agendar.

## Decisão Lucas — 2026-05-11

Lucas decidiu manter a campanha em `Draft`. Não enviar, não agendar e não ativar flow nesta etapa.

Correção de navegação Klaviyo: não usar link direto não verificado. O link `https://www.klaviyo.com/campaigns/01KRC1DPTY615GF5FNBPXMPKY6` retornou “Essa página não existe” no teste do Lucas.

Como localizar no painel Klaviyo:

1. Entrar no Klaviyo pelo painel normal da conta LK.
2. Ir em Campaigns.
3. Filtrar por Drafts ou buscar pelo nome `LK Phase 5 P1 Curadoria Loja Física 2026-05-11, DRAFT`.
4. Se houver campo de busca por ID, usar `01KRC1DPTY615GF5FNBPXMPKY6`.
5. Abrir a campanha e confirmar se o template `XUSEtu` está selecionado no message antes de qualquer envio.

Regra: só registrar link de Klaviyo no Brain quando ele for testado no painel logado. Link de API `https://a.klaviyo.com/api/campaigns/01KRC1DPTY615GF5FNBPXMPKY6/` serve apenas como evidência técnica via API, não como link clicável para Lucas.

## Próximos passos possíveis

1. Manter a campanha em Draft até Lucas revisar no painel.
2. Se Lucas aprovar envio, preparar checklist final com print/preview, destinatários, assunto, link de preview, fallback de rollback e confirmação de que `send_time` continua vazio antes da ação.
3. Se Lucas não quiser enviar agora, registrar como ação pendente e avançar para P2 ou WhatsApp concierge com o mesmo padrão de preview/aprovação.
