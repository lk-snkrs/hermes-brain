# Approval Packet — Nike Mind 002 architecture/CTR/GEO — 2026-06-22

**Status:** preview/read-only; nenhum write externo.  
**Gerado:** 2026-06-22T17:50:07.989491+00:00  
**Fonte:** Shopify Admin read-only, DataForSEO Brasil/pt, histórico Brain, QA público.  
**values_printed:** false.

## Veredito

Nike Mind 002 deve ser tratado como **cluster dentro da arquitetura Mind 001/002**, não como collection separada nova neste momento. A URL `/collections/nike-mind-002` retorna 404, mas há 7 PDPs ativos de Mind 002 dentro da collection `/collections/nike-mind-001`.

## Demanda

- DataForSEO `nike mind 002`: **3.600 buscas/mês**, intenção **transactional**, CPC 0,27, competição alta.
- `nike mind 001`: 27.100 buscas/mês; o cluster 001/002 deve capturar comparação e intenção de sneaker fechado vs slide aberto.

## Produtos Mind 002 encontrados em Shopify read-only

| Produto | Handle | Observação de arquitetura |
|---|---|---|
| Tênis Nike Mind 002 Black Hyper Crimson Preto | `tenis-nike-mind-002-black-hyper-crimson-preto` | em `nike-mind-001` + coleções comerciais |
| Tênis Nike Mind 002 Light Smoke Grey Cinza | `tenis-nike-mind-002-light-smoke-grey-cinza` | em `nike-mind-001` + coleções comerciais |
| Tênis Nike Mind 002 Light Khaki Bege | `tenis-nike-mind-002-light-khaki-bege` | em `nike-mind-001` + coleções comerciais |
| Tênis Nike Mind 002 Light Violet Ore Roxo | `tenis-nike-mind-002-light-violet-ore-roxo` | em `nike-mind-001` + coleções comerciais |
| Tênis Nike Mind 002 Thunder Blue Azul | `tenis-nike-mind-002-thunder-blue-azul` | em `nike-mind-001` + coleções comerciais |
| Tênis Nike Mind 002 Sail Bege | `tenis-nike-mind-002-sail-bege` | em `nike-mind-001` + coleções comerciais |
| Tênis Nike Mind 002 Grey Football Grey Cinza | `tenis-nike-mind-002-grey-football-grey-cinza` | em `nike-mind-001` + coleções comerciais |


## Problema/opportunidade

- A busca por Mind 002 existe e é transacional, mas não há collection `/nike-mind-002` pública.
- Os PDPs Mind 002 já estão associados à collection `nike-mind-001`, que agora está limpa de schema/visual duplicado.
- Risco principal: canibalizar ou confundir Mind 001 se tentarmos criar uma taxonomia separada sem medir.

## Recomendação operacional

### Fase 1 — sem write em produtos/PDP

1. Medir D+7 do hub Mind limpo.
2. Melhorar arquitetura interna da página/hub Mind para explicitar: **Mind 001 = slide aberto; Mind 002 = sneaker fechado**.
3. Garantir que `llms.txt`/source map cite o guia Nike Mind 001/002 e a collection como fonte canônica.

### Fase 2 — write proposto, se aprovado depois

- Ajuste mínimo em `descriptionHtml`/bloco do hub Mind, se necessário, para reforçar Mind 002 sem criar página 404 nova.
- Opcional: criar collection `/collections/nike-mind-002` só se GSC mostrar demanda/queries suficientes e Shopify confirmar que coleção manual/automática não causará manutenção duplicada.

## Aprovação necessária para qualquer write

Não executar agora. Próximo passo recomendado é **GSC/GA4 filtered read-only** para Mind 002 por handles/queries e um packet de copy específico se os dados confirmarem.

## Guardrails

Sem preço, estoque, disponibilidade, produtos, PDP global, GMC/feed, campanhas, Klaviyo/WhatsApp ou checkout.
