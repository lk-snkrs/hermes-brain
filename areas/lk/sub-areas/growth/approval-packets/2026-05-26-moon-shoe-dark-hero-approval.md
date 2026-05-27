# Approval packet — Moon Shoe guia LK: hero escuro

Data: 2026-05-26
Superfície: Shopify production theme `155065417950`, página `/pages/nike-moon-shoe-jacquemus-guia-lk`

## Pedido Lucas

Aplicar mais drama no topo do guia: seção hero com fundo escuro e letras brancas.

## Status já aplicado antes deste packet

- Kicker `GUIA LK · NIKE X JACQUEMUS`: reduzido de `12px` para `9.5px` no snippet e com override nas sections.
- Readback Shopify Admin: OK.
- HTML público já contém override `9.5px`, mas ainda também contém a regra base antiga `12px`; por cascade/override, a regra específica final deve vencer quando a página renderiza completa.

## Proposta visual

Transformar apenas o hero inicial em bloco editorial escuro:

- fundo: `#111111` / quase preto;
- texto principal e kicker: branco/off-white;
- intro: cinza claro;
- botões invertidos:
  - botão principal branco com texto preto;
  - botão secundário transparente com borda branca;
- legenda da imagem em cinza claro;
- manter imagem original à direita;
- manter corpo do guia branco abaixo.

## CSS proposto

```css
/* LK hotfix proposal 2026-05-26: Moon Shoe dark editorial hero */
article.lk-source-page--moon-shoe .lk-source-page__header {
  max-width: none !important;
  margin: 0 !important;
  padding: clamp(56px, 7vw, 92px) max(20px, calc((100vw - 1120px) / 2 + 20px)) 44px !important;
  background: #111111 !important;
  color: #f7f3ed !important;
}

article.lk-source-page--moon-shoe .lk-source-page__header h1 {
  color: #f7f3ed !important;
}

article.lk-source-page--moon-shoe .lk-source-page__eyebrow {
  color: rgba(247, 243, 237, .76) !important;
  font-size: 9.5px !important;
  letter-spacing: .16em !important;
}

article.lk-source-page--moon-shoe .lk-source-page__intro {
  color: rgba(247, 243, 237, .82) !important;
}

article.lk-source-page--moon-shoe .lk-source-hero-actions a:first-child {
  background: #f7f3ed !important;
  color: #111111 !important;
  border-color: #f7f3ed !important;
}

article.lk-source-page--moon-shoe .lk-source-hero-actions a:last-child {
  background: transparent !important;
  color: #f7f3ed !important;
  border-color: rgba(247, 243, 237, .72) !important;
}

article.lk-source-page--moon-shoe .lk-source-hero-media span {
  color: rgba(247, 243, 237, .62) !important;
}

@media (max-width: 749px) {
  article.lk-source-page--moon-shoe .lk-source-page__header {
    padding: 36px 22px 34px !important;
  }
}
```

## Risco

Baixo/médio:

- É customer-facing e em produção.
- Pode melhorar percepção editorial/premium, mas altera bastante o impacto visual acima da dobra.
- Precisa checagem desktop e mobile após aplicar.

## Rollback

Reverter os assets salvos em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/`

ou remover o bloco CSS `LK hotfix proposal 2026-05-26: Moon Shoe dark editorial hero` das sections/snippet.

## Aprovação necessária

Aplicar em produção exige aprovação explícita de Lucas no turno atual.

Frase de aprovação sugerida:

`Aprovo aplicar o hero escuro na página Moon Shoe em produção.`
