# Moon Shoe dark hero — pronto para aplicar, aguardando turno com write liberado

Data: 2026-05-26

## Destino

- Shopify production theme: `155065417950`
- Página pública: `https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk`

## Pedido limpo

Lucas aprovou e reforçou aplicar em produção o hero escuro no topo do guia Moon Shoe.

## Evidências

- Approval packet original: `2026-05-26-moon-shoe-dark-hero-approval.md`
- Pedido explícito anterior: `Aprovo aplicar o hero escuro na página Moon Shoe em produção.`
- Reforço atual: corrigir/aplicar em produção.
- Kicker já reduzido para `9.5px` em assets Shopify, com readback Admin OK em execução anterior.

## Preview técnico aprovado

Aplicar apenas no hero inicial:

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

## Bloqueio do turno atual

Apesar da aprovação explícita de Lucas, o roteamento deste turno impôs boundary de read-only/local/documentação para produção. Não executar Shopify production write neste turno.

## Rollback

- Remover o bloco CSS `LK hotfix proposal 2026-05-26: Moon Shoe dark editorial hero` dos assets aplicados.
- Ou restaurar backups em `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/`.

## Próximo passo

Executar em turno/rota sem boundary read-only: backup imediato do asset, PUT Shopify production, readback Admin, verificação pública desktop/mobile.
