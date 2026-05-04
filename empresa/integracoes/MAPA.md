# Integrações — Mapa

Mapa operacional de integrações do Grupo Cimino no Hermes Brain.

Regra: este diretório guarda nomes de integrações, usos, escopos e nomes de secrets. Valores de credenciais vivem no Doppler `lc-keys/prd` e nunca entram no GitHub.

## Regra comum de permissão

Cada integração deve separar ações em quatro níveis:

1. Read-only — consultar/listar/validar sem alterar estado.
2. Write — criar/atualizar dados internos ou drafts sem envio externo.
3. External-send — mensagem, email, campanha, post, webhook para terceiro ou contato com cliente; exige preview e aprovação de Lucas.
4. Admin/destructive — credenciais, permissões, deletes, billing, deploy, containers, volumes, compose, redes ou produção; exige aprovação explícita + backup/rollback.

## Docs por ferramenta

- [Shopify LK](shopify.md)
- [Supabase](supabase.md)
- [Evolution API / WhatsApp](evolution.md)
- [n8n](n8n.md)
- [GitHub](github.md)
- [Hostinger VPS](hostinger.md)
- [Telegram](telegram.md)
- [Analytics / GA4 / GSC](analytics.md)
- [Klaviyo](klaviyo.md)
- [Meta Ads / Instagram](meta-ads.md)

## Por negócio

### LK Sneakers

- Shopify — `shopify.md`
- Supabase LK — `supabase.md`
- Klaviyo — `klaviyo.md`
- GA4/GSC — `analytics.md`
- Meta Ads — `meta-ads.md`
- Evolution Clo — `evolution.md`
- Telegram — `telegram.md`
- Judge.me, Frenet, Tiny ERP — pendentes de subdoc próprio quando houver uso operacional recorrente.

Detalhe: `../../areas/lk/contexto/ferramentas.md`.

### Zipper Galeria

- Supabase Zipper Vendas — `supabase.md`
- Supabase SPITI/Zipper CRM quando aplicável — `supabase.md`
- Evolution ZipperGaleria — `evolution.md`
- GA4 — `analytics.md`
- Instagram/Metricool quando documentado — `meta-ads.md` ou subdoc futuro.
- Email/produção — pendente de subdoc próprio quando houver rotina operacional documentada.

Detalhe: `../../areas/zipper/contexto/ferramentas.md`.

### SPITI Auction

- Supabase SPITI/Zipper CRM — `supabase.md`
- Email como fonte de verdade de lances — pendente de subdoc próprio.
- LeiloesBR — pendente de subdoc próprio.
- n8n — `n8n.md`
- Evolution conforme regras de envio aprovadas — `evolution.md`

Detalhe: `../../areas/spiti/MAPA.md`.

## Próxima rodada recomendada

- Criar subdocs adicionais para Judge.me, Frenet, Tiny ERP, Email/Google Workspace, LeiloesBR, Railway, Vercel, Notion/NocoDB e Metricool quando virarem fluxos recorrentes.
- Transformar integrações com uso frequente em skills executáveis com verificação e aprovação.
