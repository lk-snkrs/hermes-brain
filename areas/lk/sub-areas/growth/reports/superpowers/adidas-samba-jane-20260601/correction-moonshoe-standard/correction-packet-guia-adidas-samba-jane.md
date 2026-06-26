# Correction Packet — Guia Adidas Samba Jane no padrão Moon Shoe

Data: 2026-06-02T11:08:24Z
Status: **local/dev-ready**. Não publicado. Shopify production intocada nesta correção.

## Motivo

Lucas reprovou o guia público atual por estar sem o layout correto. Diagnóstico confirmado: a página publicada renderiza como texto corrido/artigo simples, fora do padrão Guia LK.

## Padrão aplicado no draft

- Guia dedicado `/pages/guia-*` = padrão **Nike x Jacquemus Moon Shoe**.
- Não usar padrão 204L aqui; 204L é para coleção produto-first.
- Conteúdo mantém narrativa LKGOC: história/DNA → relevância atual → styling → comparação → curadoria LK → FAQ.

## Pesquisa usada

- DataForSEO/SERP Brasil para `Adidas Samba Jane`:
  - adidas Brasil oficial: Samba clássico reinventado como Mary Jane.
  - LK collection aparece na SERP.
  - FFW: lançamento e contexto fashion do Samba Jane.
  - PAA/relacionadas: diferença entre versões, autenticidade, colorways.
- DataForSEO/SERP US para `Adidas Samba Jane styling Mary Jane sneaker`:
  - adidas US: heritage soccer vibes + Mary Jane style.
  - The Mom Edit: outfits/styling com Samba Jane.
  - Glamour: Mary Jane sneakers como continuidade/tensão depois dos Sambas.
  - sinais sociais: vídeos de styling e discussão de tendência.

## Artefato local

- HTML draft: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/superpowers/adidas-samba-jane-20260601/correction-moonshoe-standard/guia-adidas-samba-jane-moonshoe-standard-draft.html`

## QA local contra padrão

- [x] Shell editorial premium inspirado em Moon Shoe.
- [x] Hero editorial com CTA duplo.
- [x] Imagem contextual/styling.
- [x] Tabela comparativa Samba OG / Sambae / Samba Jane.
- [x] Cards de referências externas com links.
- [x] Bloco citável LK.
- [x] FAQ visual em `<details>`.
- [x] CTA discreto para coleção.
- [x] Sem termos proibidos como taxonomia pública.

## Bloqueios

- Produção Shopify não alterada nesta etapa.
- Página pública errada ainda existe até aprovação explícita de Lucas para deletar/rollback ou substituir.
- Próximo write externo exige aprovação escopada.

## Próxima ação recomendada

1. Deletar ou substituir a página pública errada `Page ID 127553700062` após aprovação.
2. Subir o draft em DEV/preview ou aplicar em Shopify page apenas com aprovação.
3. Validar visual desktop/mobile antes de considerar final.
