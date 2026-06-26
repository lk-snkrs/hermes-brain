# Handoff — Mesa COO 2026-06-08 — LK Growth/GMC + LK Shopify

Data UTC: 2026-06-08T14:37:43Z

## Escopo

Handoff operacional para agentes/especialistas após execução da Mesa COO 2026-06-08.

- Empresas/superfícies: LK Sneakers / GMC Local-LIA / Shopify theme Production public PDP QA.
- Agentes destinatários: LK Growth/GMC, LK Shopify OS, LK Ops/Tiny apenas se houver impacto futuro em estoque/availability.
- IMBOX/Inbox/COO: fora do escopo por preferência explícita de Lucas; não incluir em próximas Mesas/rotinas salvo pedido explícito.

## Decisão 2/3 — LK Growth/GMC — link_template Local/LIA

- Pedido/evento: Lucas escolheu `Fazer` para avançar micro-piloto `link_template` GMC Local/LIA.
- Resultado verificado: approval packet read-only criado para 10 ofertas `local:pt:BR:LIA_*` com `store_code=LK001`.
- Writes externos: não; `0` ProductInput/Merchant API/feed/Simprosys/POS/Shopify writes.
- Aprovação: pendente para qualquer write real.
- Snapshot/readback/receipt:
  - `areas/lk/sub-areas/growth/approval-packets/gmc/link-template-micro-pilot-20260608T1420Z/approval-packet.md`
  - `areas/lk/sub-areas/growth/approval-packets/gmc/link-template-micro-pilot-20260608T1420Z/pilot-offers.csv`
  - `areas/lk/sub-areas/growth/approval-packets/gmc/link-template-micro-pilot-20260608T1420Z/packet.json`
- Verificações: Brain health passou; secret scan focado `0`; CSV/JSON consistentes com 10 ofertas; `external_writes=0`.
- Risco/bloqueio: surface dono ainda não confirmado. Não executar bulk em 10.441 itens; não executar `fetchNow`/reprocess; não alterar Simprosys/POS/app config/Shopify/feed sem aprovação escopada.
- Próximo passo seguro: se Lucas aprovar, primeiro confirmar surface dono exato, tirar snapshot dos 10 resources/config/status, mutar somente `link_template/mobile_link_template`, fazer readback e manter rollback no mesmo surface.
- Frase de aprovação futura registrada no packet: `Aprovo executar o micro-piloto link_template GMC Local/LIA nas 10 ofertas deste packet, no surface [NOME DO SURFACE], mutando apenas link_template/mobile_link_template, com snapshot, readback e rollback.`

## Decisão 3/3 — LK Shopify OS — public PDP cache recheck

- Pedido/evento: Lucas escolheu `Fazer` para revalidar cache/QA público de ASICS GT-2160 + Adidas Samba Wales Bonner após merge Production.
- Fonte viva consultada: receipt Production merge `areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-asics-gt2160-walesbonner-github-merge-20260608T0125Z/receipt.md`.
- Resultado verificado: recheck público cache-busted OK em 4 PDPs, 5 rodadas cada.
- Writes externos: não; `0` Shopify/theme/GitHub/Admin writes.
- Aprovação: não aplicável para read-only QA; correções futuras em theme Production seguem GitHub PR/merge/deploy, não Asset API direto.
- Snapshot/readback/receipt:
  - `areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/public-cache-recheck-asics-walesbonner-20260608T143603Z/qa.md`
  - `areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/public-cache-recheck-asics-walesbonner-20260608T143603Z/qa.json`
- Resultado técnico:
  - HTTP 200: `20/20`
  - Markers esperados presentes: `20/20`
  - Classes canônicas presentes: `20/20`
  - Cloudflare/challenge-like: `0/20`
  - Veredito: `OK`; intermitência residual edge/cache não reproduzida.
- Próximo passo: nenhum write necessário agora. Se o problema reaparecer, abrir approval packet/PR path específico com evidência pública atual.

## Regras para agentes na próxima retomada

1. Não repetir pendência do grupo Telegram `[LK] Produção de Conteúdo`; Lucas informou que já foi destravada.
2. Não incluir IMBOX/Inbox em COO/Mesa/rotinas salvo pedido explícito.
3. Para GMC `link_template`, tratar o estado como packet pronto para decisão, não como execução liberada.
4. Para Shopify Production/theme, manter regra dura: Production via GitHub PR/merge/deploy/readback/QA; Asset API direto em Production bloqueado por padrão.
5. Antes de próxima Mesa, reconciliar estado vivo via receipts/sessões recentes, não apenas relatório consolidado diário.

## Onde ficou documentado

- Este handoff: `areas/lk/handoffs/handoff-mesa-coo-20260608-gmc-shopify-agents-20260608T143743Z.md`
- Índice de rotinas atualizado anteriormente para o approval packet GMC.
- Skill `mesa` deve preservar a regra de criar handoff quando decisões executadas gerarem estado que especialistas precisam carregar.
