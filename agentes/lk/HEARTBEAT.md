# HEARTBEAT — Agente LK

Status: LK documental + LK Growth profile ativo para Growth/SEO/CRO/GEO/GMC/analytics/conteúdo.

## Checks sugeridos

- Frescor dos dados Shopify/Supabase/Tiny quando usados como fonte.
- Falhas em full sync, GMC/feed, GSC/GA4/GMC ou morning briefing.
- Oportunidades críticas de CRM/cross-sell com evidência.
- Meta Ads/Klaviyo/GMC autenticação quando campanhas estiverem ativas.
- Pendências de aprovação Lucas/Renan para campanhas, conteúdos, source pages, Klaviyo ou writes.
- Divergência entre estoque/preço/disponibilidade em fontes vivas.

## Política de ruído

Silent-OK: não avisar quando tudo está saudável.

Alertar apenas quando houver:

- decisão necessária;
- bloqueio por aprovação;
- risco de publicar/enviar dado errado;
- oportunidade comercial clara com evidência;
- falha de fonte read-only relevante;
- write aprovado que precisa receipt/rollback.

## Bloqueios permanentes sem aprovação explícita

- Shopify/GMC/Klaviyo/Meta/theme/produção;
- preço, disponibilidade, reserva ou promessa material para cliente;
- WhatsApp/e-mail/campanha/bulk;
- alteração de feed, anúncios, automação, cron, gateway ou runtime.

## Handoff

Registrar outputs materiais no ledger:

- `empresa/contexto/handoff-ledger.md`
- `empresa/contexto/handoffs/YYYY-MM-DD.md`

Todo registro deve declarar `Writes externos: não` quando a execução foi apenas read-only/local.