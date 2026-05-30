# Padrão canônico — Guia + Coleção LK

Status: **APROVADO POR LUCAS COMO PADRÃO CANÔNICO** para rollout nas próximas páginas.
Base aprovada: `new-balance-204l` para coleção/product-first e bloco guia pós-grid; `nike-moon-shoe-jacquemus-guia-lk` como referência de guia editorial dedicado.
Snapshot literal congelado da coleção 204L aprovada: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/references/collection-204l-gold-source-final/`.
Padrão de texto de coleção: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/PADRAO-TEXTO-COLECAO-LK.md`.
Ambiente de aplicação: primeiro Dev Theme Shopify `155065450718`; produção apenas após aprovação explícita de Lucas.

## Objetivo

Criar um layout único e replicável para páginas melhoradas da LK Sneakers, evitando variações soltas entre coleções, guias e FAQs.

O padrão separa dois tipos de superfície:

1. **Coleção product-first** — produtos primeiro, apoio editorial depois.
2. **Guia editorial dedicado** — página `/pages/guia...` para aprofundamento, citabilidade, GEO/AI Search e decisão de compra.

## Ordem canônica da coleção

1. Banner/header da coleção no padrão `lk-collection-v2`.
2. Bloco editorial curto com curadoria LK e collage visual.
3. Grid/listagem de produtos.
4. Bloco `Guia Editorial LK` pós-grid.
5. FAQ integrado dentro do bloco guia, sem FAQ legado duplicado.
6. CTA para abrir guia completo quando houver página dedicada.

Regra principal: a coleção nunca vira blog; produto vem antes do guia.

## Padrão visual da coleção — `lk-collection-v2`

Fonte aprovada: `/collections/new-balance-204l` no Dev Theme `155065450718` e produção atual validada.
Snapshot literal congelado pós-aprovação: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/references/collection-204l-gold-source-final/`.

Elementos obrigatórios:

- `.coll-banner` com H1 serifado, premium e limpo.
- `.lk-collection-v2` como namespace base.
- Kicker aprovado: `Curadoria LK`.
- Copy curta e comercial, sem redundância com o H1.
- Texto de coleção com 1–2 parágrafos quando a coleção tiver densidade suficiente: definição do modelo/linha + curadoria LK + orientação de escolha para SEO/GEO.
- Collage editorial à direita no desktop.
- Mobile compacto, com texto e mídia controlados para não empurrar produto.

Invariantes desktop aprovados:

- `.coll-banner`: `padding: 40px clamp(28px,3.2vw,44px) 9px`.
- `.coll-banner__title`: `Cormorant Garamond`, `clamp(42px,3.66vw,50px)`, `line-height: 1.04`.
- `.lk-collection-v2`: `padding: 16px clamp(28px,3.2vw,44px) 30px`.
- `.lk-collection-v2__inner`: `max-width: 1440px`, grid `minmax(360px,.44fr) minmax(520px,.56fr)`.
- `.lk-collection-v2__media`: collage com `transform: translateY(-102px)` e `margin-bottom: -102px` no desktop aprovado.

Invariantes mobile aprovados:

- `.coll-banner`: `padding: 28px 16px 0`.
- Breadcrumb oculto.
- H1 mobile: `38px`, `line-height: 1.02`, sem quebrar quando couber no viewport.
- Regra final 204L para evitar regressão: `font-size: clamp(32px, 9.7vw, 38px)`, `max-width: calc(100vw - 32px)`, `white-space: nowrap`, `display: inline-block`.
- `.lk-collection-v2`: `padding: 0 16px 16px`.
- Headline editorial: `24px`, `line-height: 1.04`.
- Body: `12px`, `line-height: 1.5`, clamp curto.
- Mídia colapsada não deve dominar o primeiro scroll.

## Padrão do bloco guia pós-grid

Fonte aprovada: `new-balance-204l`.

Estrutura:

1. Fundo off-white/claro com borda sutil.
2. Kicker: `GUIA EDITORIAL LK`.
3. H2 serifado grande.
4. Intro curta, objetiva e citável.
5. Card interno branco em duas colunas no desktop:
   - esquerda: `Como escolher...` com orientação prática;
   - direita: `Perguntas frequentes` em accordion;
   - divisor vertical sutil;
   - títulos alinhados pelo topo.
6. Rodapé do bloco:
   - helper/note claro à esquerda;
   - CTA preto à direita: `ABRIR GUIA COMPLETO`.

Contrato desktop do card:

```css
@media (min-width: 990px) {
  .lk-guide-standard-card--wide {
    display: grid;
    grid-template-columns: minmax(380px, .88fr) minmax(520px, 1.12fr);
    grid-template-rows: auto 1fr;
    align-items: start;
  }

  .lk-guide-standard-card--wide > h3 {
    grid-column: 1 / 2;
    grid-row: 1;
    margin: 0;
  }

  .lk-guide-standard-card--wide > ul {
    grid-column: 1 / 2;
    grid-row: 2;
  }

  .lk-guide-standard-faq {
    grid-column: 2 / 3;
    grid-row: 1 / span 2;
    align-self: start;
    margin-top: 0;
    padding-top: 0;
    border-top: 0;
    border-left: 1px solid #e2dbd0;
  }
}
```

Contrato mobile do bloco guia:

- Uma coluna.
- FAQ abaixo do conteúdo de escolha.
- Espaçamento alvo herdado da 204L: `margin-top: 24px`, `padding-top: 22px`, `border-top: 1px solid #e2dbd0`.
- CTA com boa área de toque, sem parecer banner agressivo.

## Padrão do guia editorial dedicado `/pages/guia...`

Usar quando a coleção tem busca, história, collab, autenticidade, fit/tamanho ou potencial GEO/AI Search.

Estrutura recomendada:

1. Hero editorial premium.
2. Contexto: por que essa linha/collab importa.
3. Como escolher versão, cor, material ou proporção.
4. Autenticidade e curadoria LK.
5. Blocos citáveis para AI Search:
   - respostas curtas;
   - perguntas frequentes;
   - definições objetivas;
   - orientação de compra segura.
6. Tabelas comparativas quando houver colorways, versões, materiais ou diferenças objetivas.
7. CTA circular:
   - guia aponta para coleção;
   - coleção aponta para guia.
8. FAQ final com `FAQPage` JSON-LD quando aplicável.

### Padrão de tabela comparativa em guias

Fonte aprovada: `nike-moon-shoe-jacquemus-guia-lk`, bloco `Colorways do Nike x Jacquemus Moon Shoe`, versão mobile `compact table v3`.

Uso:

- Comparar colorways, versões, materiais, silhuetas, fit ou diferenças objetivas.
- Priorizar leitura comparativa sobre estética de card.
- Evitar transformar comparativo em lista editorial quando a comparação lado a lado ajuda a decisão.

Contrato visual:

- Desktop: tabela tradicional, limpa e alinhada ao guia.
- Mobile: tabela real compacta com cabeçalho visível, não cards.
- Manter `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>` e `<td>` como estrutura semântica e visual.
- Usar cabeçalhos curtos em uppercase pequeno.
- Usar bordas finas, fundo off-white no cabeçalho e padding compacto.
- Primeira coluna pode usar `Cormorant Garamond` quando for nome de colorway/modelo.
- Wrapper pode usar `overflow-x:auto` como segurança, mas o ideal é caber em 3 colunas no mobile.
- Remover qualquer comportamento antigo de `td:before` / labels repetidos no mobile.

Evitar:

- Cards pesados.
- Sombra, fundos de card por linha ou blocos com aparência de dashboard.
- Lista editorial empilhada para comparativos que precisam ser comparados rapidamente.
- Pseudo-tabela com labels repetidos em cada linha.

## Copy canônica

Tom:

- premium;
- minimalista;
- humano;
- comercialmente útil;
- sem exagero publicitário.

Vocabulário preferido:

- curadoria exclusiva;
- autenticidade;
- seleção LK;
- atendimento humano;
- orientação via chat;
- original no Brasil;
- escolher tamanho/modelo/cor com segurança.

Evitar em superfície pública:

- `estoque` como taxonomia;
- `encomenda`;
- `pronta entrega`;
- labels inventadas tipo `Sinal editorial`;
- linguagem operacional de Tiny/fornecedor.

Fit/tamanho:

- Não usar “roda grande/pequeno”.
- Usar: `tem forma grande`, `tem forma regular`, `tem forma mais apertada`, `sensação mais apertada no pé`.
- Air Jordan 4 e Jordan Mid: recomendação técnica LK = considerar 1 tamanho acima, especialmente entre tamanhos ou buscando conforto.

## FAQ padrão por objeção real

As perguntas devem cobrir decisão de compra, não SEO genérico.

Temas recorrentes:

1. O modelo é original/autêntico?
2. Como escolher tamanho?
3. Qual versão/colorway faz mais sentido?
4. Combina com que estilo de uso?
5. Por que comprar com curadoria LK?
6. Como confirmar disponibilidade/prazo pelo atendimento?

## Schema/GEO

- `FAQPage` apenas uma vez por coleção/guia.
- Se FAQ está no bloco guia, desativar FAQ legado separado.
- Blocos do guia devem ser citáveis por IA: respostas curtas, claras e sem dependência de layout.
- Product/Collection schema não deve conflitar com FAQ.

## Ordem de rollout

1. Mapear páginas/coleções já melhoradas.
2. Classificar:
   - coleção product-first sem guia;
   - coleção com guia desconectado;
   - guia dedicado já existente;
   - página que não merece guia por ser bucket genérico.
3. Aplicar primeiro no Dev Theme `155065450718`.
4. Validar desktop e mobile separadamente.
5. Enviar preview para Lucas.
6. Production apenas com aprovação explícita.
7. Registrar rollback, receipt e revisão de impacto D+7.

## Checklist de QA antes de enviar preview

- Produto aparece antes do guia.
- H1 não repete kicker.
- Kicker útil e curto.
- Desktop: collage alinhada ao padrão 204L.
- Mobile: título/copy/mídia compactos.
- Guia pós-grid com card branco em duas colunas no desktop.
- FAQ alinhado no topo da coluna direita.
- FAQ legado desativado.
- `FAQPage` JSON-LD único.
- CTA guia ↔ coleção funciona.
- Sem termos proibidos.
- Screenshot desktop e mobile conferidos.
- Preview usa `preview_theme_id=155065450718`.

## Regra de aprovação

Pode preparar e subir preview em dev theme quando autorizado no escopo do lote.

Não pode publicar produção, alterar página/coleção pública, tema production, menu, SEO field ou Shopify object global sem aprovação explícita atual de Lucas.
