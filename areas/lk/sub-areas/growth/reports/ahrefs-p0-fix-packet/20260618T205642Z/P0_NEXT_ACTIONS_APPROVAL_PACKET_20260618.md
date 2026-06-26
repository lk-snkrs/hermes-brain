# LK Growth — Próximas ações P0/GMC/Judge.me/Links internos

Gerado UTC: `2026-06-18T22:20:02Z`
Modo: read-only/prep; writes externos executados nesta etapa: `0`. values_printed=false.

## 1) Merchant Center / Free Local Listings

**Veredito:** o e-mail do Google é compatível com um problema real, mas o snapshot autenticado atual está pior que o alerta de e-mail.

- E-mail: queda Free local listings BR de `2.088` para `1.632` ativos (`-21%`).
- Merchant API atual: total products/statuses `23626`; local offers `11537`.
- `FREE_LOCAL_LISTINGS` BR `approved`: `475`.
- `FREE_LOCAL_LISTINGS` BR `disapproved`: `11062`.
- `LOCAL_INVENTORY_ADS` BR `approved`: `1`.
- `LOCAL_INVENTORY_ADS` BR `disapproved`: `11536`.
- Expiração nos próximos 3 dias: `0`; expirados: `0`.
- Causa provável: não é expiração; é indisponibilidade/reprovação local por `local_stores_lack_inventory` + contrato LIA `mhlsf_full_missing_valid_link_template`.
- Handoff registrado para LK Stock validar inventário local/sync: `areas/lk/sub-areas/stock/handoffs/gmc-free-local-listings-local-inventory-drop-20260618.md`.

**Bloqueado sem aprovação:** qualquer write em GMC/feed/Simprosys, fetch/reprocess ou ajuste de disponibilidade/local inventory.

## 2) Judge.me — validação dev

- Dev theme `lk-new-theme/dev` (`155065450718`) contém patch `lk_picture_src` no asset `snippets/judgeme_widgets.liquid`.
- Validação pública por `preview_theme_id` não carregou o dev theme; HTML retornou igual ao production, ainda com `=&gt;` no `src`.
- Production ainda tem bug em PDPs afetadas, ex. `camiseta-jacquemus-the-typo-azul` e `air-jordan-4-craft-medium-olive`.
- Status: patch tecnicamente presente em dev, mas **não validado visualmente/publicamente**. Não recomendo aplicar production até validar por preview real/browser autenticado ou duplicar teste em um theme preview acessível.

## 3) Links internos 404 — pacote de edição

- Linhas restantes após Samba: `18`.
- Origens editáveis por Admin já localizadas: `15` linhas em blog/page.
- Origens em collection/rich content ou template: `3` linhas, precisam caminho de edição específico.
- Sem candidato automático seguro: `0` linhas.
- CSV de preview: `p0-internal-link-edit-approval-preview.csv`.

**Ação recomendada:**
- Blog Nude Project: trocar links de produtos 404/draft para `/collections/nude-project` ou remover link do produto específico.
- Blog Fear of God Essentials: trocar links de produtos 404/draft para `/collections/fear-of-god-essentials`.
- Página Saint Studio: remover links para produtos 404 ou apontar para a própria página/collection segura; evitar `/collections/all` genérico quando possível.
- Página Autenticidade/collections com links para guias inexistentes: criar páginas-guia se estiverem no roadmap ou trocar para collections públicas equivalentes.

## 4) Aprovações propostas

### Aprovação B1 — Conteúdo interno 404
- Escopo: editar somente links internos quebrados em blogs/pages já identificados no CSV; sem publicar produto, sem alterar preço/estoque, sem mexer em tema.
- Risco: baixo/médio; melhora crawl e UX. Rollback: backup do body_html de cada artigo/página antes/depois.

### Aprovação B2 — Redirects seletivos
- Escopo: criar redirects só para URLs que não devem voltar como produto/página e possuem destino equivalente validado.
- Risco: médio para handles de produto draft; por isso não recomendo redirect automático para produtos draft.

### Aprovação B3 — GMC Local micro-piloto
- Escopo: após resposta do LK Stock, micro-piloto de 10–20 offers LIA para corrigir `link_template`/surface correto ou acionar Simprosys/local feed.
- Risco: alto se aplicado no surface errado; Simprosys pode sobrescrever. Rollback/readback obrigatório.

### Aprovação B4 — Judge.me production
- Escopo: aplicar o patch `lk_picture_src` em production theme somente depois de validação real do preview.
- Status atual: **não recomendado ainda**, porque o preview público não carregou dev theme.

## Arquivos de evidência

- GMC detail: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/gmc/local-listings-drop-20260618/merchant_destination_country_status_counts.json`.
- GMC expiration: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/gmc/local-listings-drop-20260618/local-expiration-check.json`.
- Judge.me validation: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-p0-fix-packet/20260618T205642Z/judgeme-dev-public-validation.json`.
- Link edits preview: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-p0-fix-packet/20260618T205642Z/p0-internal-link-edit-approval-preview.csv`.
