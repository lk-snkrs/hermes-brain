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

## 2026-06-01 19:50:47 — Regra obrigatória LK Growth Optimized Collection

Toda coleção que for otimizada/melhorada para SEO, GEO/AI Search, CRO, layout, hero, guia ou texto deve obrigatoriamente passar pelo fluxo **LK Growth Optimized Collection**, usando a skill `lk-superpowers-collection-optimizer`, camada CLAUDE-SEO, guia dedicado, Guia Editorial LK pós-grid, imagens editoriais reais, tag/metafields e ledger. Regra canônica: `rules/REGRA-LK-GROWTH-OPTIMIZED-COLLECTION-OBRIGATORIA.md`.

## Padrão obrigatório refinado — 2026-06-01T20:43:30Z

Feedback visual/textual aprovado por Lucas no piloto Adidas Samba Jane:

- **Texto hero/editorial maior:** o primeiro texto da coleção otimizada deve ter mais corpo. Usar como referência **500–700 caracteres** no primeiro parágrafo/bloco, com densidade de styling, intenção de uso, leitura estética e curadoria LK. Textos curtos demais passam a reprovar QA.
- **CTA de guia em fundo claro:** chamadas como “Para aprofundar versões, materiais e proporção, abra o guia completo da coleção.” devem usar **fundo claro**, visual premium e contraste suave. Fundo escuro nesse CTA não é padrão e só deve ser usado se Lucas aprovar explicitamente.
- **QA obrigatório:** antes de considerar uma coleção `LK Growth Optimized Collection` pronta, validar: texto principal com corpo suficiente + card/CTA de guia em fundo claro.

## Regra operacional obrigatória — 2026-06-01T21:06:42Z

Feedback Lucas por áudio:

- Sempre que qualquer alteração for aplicada em tema Shopify, DEV theme, preview, collection, página, guia, asset visual ou bloco renderizado, a resposta ao Lucas deve obrigatoriamente incluir o **link direto de acesso/preview** do que foi alterado.
- Não basta dizer que foi aplicado ou validado; o link precisa estar visível na resposta final do turno.
- Para tema DEV, sempre enviar URL com `preview_theme_id` correspondente.
- Para produção, enviar URL pública final.
- Esta regra vale para qualquer alteração visual, textual, SEO/CRO/GEO ou de layout.
- Se houver múltiplas páginas alteradas, listar todos os links.

## Correção obrigatória de padrão — 2026-06-01T21:59:24Z

Feedback Lucas — QA Adidas Samba Jane:

1. **CTA do guia deve ter fundo claro**
   - O bloco/frase “Para aprofundar versões, materiais e proporção, abra o guia completo da coleção.” não pode ficar com fundo escuro.
   - Padrão obrigatório: fundo claro, visual premium, contraste suave, borda discreta se necessário.
   - Qualquer CTA de guia em fundo escuro reprova QA visual.

2. **Apenas um FAQ por coleção otimizada**
   - Não pode haver dois blocos de FAQ na mesma experiência da coleção.
   - O único FAQ permitido deve ser o FAQ criado dentro do **Guia LK** / bloco editorial canônico.
   - Se existir FAQ legado, FAQ automático, FAQ duplicado de tema ou outro FAQ fora do Guia LK, ele deve ser removido/ocultado para aquela coleção.
   - Schema FAQPage também deve refletir apenas o FAQ canônico do Guia LK, evitando duplicidade para usuário e para Google/AI Search.

Regra de QA: coleção `LK Growth Optimized Collection` só pode ser aprovada se tiver CTA de guia claro e um único FAQ visível, o do Guia LK.

## Alias operacional obrigatório — 2026-06-01T22:19:59Z

- **LKGOC** significa **LK Growth Optimized Collection**.
- Sempre que Lucas falar “LKGOC”, interpretar como o padrão/skill/processo **LK Growth Optimized Collection**.
- O termo se refere ao pacote completo de otimização de coleção: texto hero robusto, layout editorial, imagens editoriais, guia pós-grid, Guia LK, FAQ único canônico, CTA claro, schema, QA, ledger/tag/metafields quando aplicável e link obrigatório de preview após qualquer alteração.
- Regra de comunicação: responder usando o contexto LKGOC sem pedir esclarecimento quando Lucas usar essa sigla.

## Correção LKGOC CTA — 2026-06-01T23:48:29Z

Padrão obrigatório Lucas:
- No LKGOC, o bloco de texto “Para aprofundar versões, materiais e proporção, abra o guia completo da coleção.” deve usar **o mesmo fundo claro/card editorial do bloco acima**.
- O botão/link **ABRIR GUIA COMPLETO** deve ter **fonte branca** sobre botão/fundo escuro.
- QA visual deve reprovar se o card “Para aprofundar...” estiver com cor divergente do bloco acima ou se o texto do botão não estiver branco.

## Correção LKGOC mobile CTA — 2026-06-02T00:11:52Z

Padrão obrigatório:
- LKGOC precisa validar **desktop e mobile** separadamente.
- No mobile, o bloco “Para aprofundar versões, materiais e proporção...” deve manter o mesmo fundo claro do card editorial acima (`#faf8f4` / família visual clara), sem cair em variação escura ou fundo diferente.
- O botão “ABRIR GUIA COMPLETO” deve manter texto branco também no mobile.
- QA LKGOC só passa após checagem visual mobile.

## Correção LKGOC Guia LK novo — 2026-06-02T00:16:23Z

Padrão obrigatório atualizado por Lucas:
- O bloco Guia LK do LKGOC deve usar a versão nova adaptada para desktop, não a versão antiga.
- Desktop: card editorial e FAQ no mesmo card amplo, com **divisor vertical** entre o conteúdo de escolha e o FAQ.
- Mobile: o mesmo padrão deve adaptar com divisor superior entre conteúdo e FAQ, mantendo espaçamento premium.
- O card “Para aprofundar versões, materiais e proporção...” deve usar o mesmo fundo claro dos cards internos do Guia LK (`#fff` com borda `#e2dbd0`), não uma variação diferente.
- O botão “ABRIR GUIA COMPLETO” deve manter fundo escuro e texto branco.
- QA LKGOC deve reprovar se a coleção estiver usando versão antiga do Guia LK ou se o card de aprofundamento tiver cor diferente dos cards internos.

## Regra LKGOC — coleção + guia juntos — 2026-06-02T00:25:03Z

Feedback Lucas:

- Todo trabalho de **LKGOC / LK Growth Optimized Collection** deve tratar **coleção otimizada + Guia LK dedicado** como um pacote único.
- Não considerar a coleção pronta se o guia dedicado correspondente não estiver planejado, escrito e pronto para publicação/approval.
- Objetivo central: **contar e vender histórias**, não apenas descrever produto.
- Todo texto de coleção e todo Guia LK devem seguir a lógica:
  1. história/origem/DNA do modelo;
  2. como o modelo volta ou se transforma nos tempos atuais;
  3. por que ele é relevante agora em moda, cultura, comportamento e styling;
  4. como a curadoria LK ajuda a escolher versão, cor, proporção, autenticidade e intenção de uso;
  5. fechamento comercial premium, humano e editorial.
- O guia deve cruzar o passado do modelo com sua leitura contemporânea, explicando por que ele importa hoje.
- QA LKGOC reprova textos genéricos, puramente técnicos ou sem narrativa histórica/comercial.

## Regra LKGOC — pesquisa na internet obrigatória — 2026-06-02T00:56:58Z

- Todo **LKGOC / LK Growth Optimized Collection** deve fazer pesquisa na internet antes de escrever ou publicar coleção/Guia LK.
- A pesquisa deve alimentar narrativa, SEO/GEO e curadoria, cobrindo quando aplicável:
  - história/origem/DNA do modelo;
  - contexto cultural e fashion;
  - relevância contemporânea;
  - styling atual;
  - dúvidas reais de busca;
  - SERP/concorrentes;
  - fontes editoriais e páginas oficiais.
- Fontes preferenciais: Google/SERP, DataForSEO, páginas oficiais da marca, Highsnobiety, Hypebeast, Vogue, GQ, Who What Wear, Glamour, FFW, Sneaker News, Complex, Footwear News e veículos editoriais equivalentes.
- O LKGOC não deve inventar história nem escrever só com conhecimento genérico.
- A narrativa final deve cruzar **internet + SERP + fontes editoriais + curadoria LK + intenção comercial atual**.
- Guia LK só passa em QA se explicar: passado/DNA do modelo, por que ele importa agora, como escolher e por que a curadoria LK ajuda a comprar melhor.

## Padrão visual aprovado — Guia LK dedicado Moon Shoe / Samba Jane — 2026-06-02

Status: **aprovado por Lucas** após correção do guia Adidas Samba Jane no DEV.

Este refinamento passa a ser obrigatório para qualquer **Guia LK dedicado** (`/pages/guia-*`) criado pelo LKGOC:

- Referência visual principal: **Moon Shoe/Jacquemus** para shell editorial; Samba Jane DEV aprovado como refinamento de aplicação.
- Hero: fundo preto/escuro (`#101010`), full-bleed, texto branco, CTAs discretos e imagem editorial integrada.
- Imagem do hero: deve mostrar pessoa usando o tênis/modelo ou silhueta equivalente de forma clara. Não basta ser Vogue/Glamour/ELLE se o calçado estiver tapado pela calça, cortado ou invisível. Produto isolado/packshot continua proibido.
- Fonte de imagem: priorizar Vogue, GQ, ELLE, Marie Claire, Harper's Bazaar, Glamour, Who What Wear e portais sneaker/cultura; se a melhor imagem visível vier de outra fonte editorial de styling, pode usar com justificativa e fonte registrada.
- Régua/largura: o conteúdo abaixo do hero deve seguir a **mesma lógica de rail do hero preto**. H2, parágrafos, quotes e signals não podem voltar para coluna estreita ou centralizada pelo wrapper padrão do `main-page`.
- FAQ: até 4 perguntas em 1 coluna no desktop; com mais de 4, usar quantidade par e equilibrada — 6 ou 8 perguntas em 2 colunas no desktop; mobile sempre 1 coluna.
- CTA final: discreto, alinhado à régua do guia; no desktop, manter texto em uma linha quando couber e botão à direita sem quebrar o layout.
- QA visual obrigatório: desktop e mobile no Shopify DEV preview antes de approval; readback técnico não substitui validação visual.

Exemplo de regra CSS funcional aprovada para guias dedicados com hero full-bleed:

```css
@media (min-width: 990px) {
  .lk-source-page--HANDLE { --lk-guide-rail: max(72px, calc((100vw - 1180px) / 2)); }
  .lk-source-page--HANDLE .lk-source-page__header {
    width: 100vw;
    margin-left: calc(50% - 50vw);
    margin-right: calc(50% - 50vw);
    padding-left: var(--lk-guide-rail);
    padding-right: var(--lk-guide-rail);
    background: #101010;
  }
  .lk-source-page--HANDLE > section {
    padding-left: var(--lk-guide-rail);
    padding-right: var(--lk-guide-rail);
  }
  .lk-source-page--HANDLE > section > h2,
  .lk-source-page--HANDLE > section > p,
  .lk-source-page--HANDLE > section > .lk-source-quote,
  .lk-source-page--HANDLE > section > .lk-source-signal {
    width: min(1180px, calc(100vw - (2 * var(--lk-guide-rail))));
    max-width: none;
    margin-left: 0;
    margin-right: 0;
  }
}
```

## Referência LKGOC

O padrão completo de LKGOC vive em um único documento canônico:

- `LKGOC-PADRAO-CANONICO.md`

Não duplicar regras longas aqui. Este arquivo deve apenas complementar seu escopo específico e apontar para o canônico.
