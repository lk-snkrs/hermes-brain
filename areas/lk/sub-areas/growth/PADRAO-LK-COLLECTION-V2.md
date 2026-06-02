# Padrão canônico `lk-collection-v2`

Status: **aprovado por Lucas em 2026-05-28** como padrão visual para replicar em próximas coleções, usando a coleção New Balance 204L no Dev Theme como gold source.

## Fonte de verdade aprovada

- Gold source: `/collections/new-balance-204l`
- Dev theme aprovado: `155065450718`
- Namespace base: `.lk-collection-v2`
- Modificador da gold source: `.lk-collection-v2--new-balance-204l`
- Escopo aprovado neste registro: **desktop hero/header editorial da coleção**. Mobile e produção continuam exigindo validação/approval próprios quando forem migrados.

## Regra de governança

- Toda coleção LK que for melhorada a partir deste ponto deve migrar para o namespace `lk-collection-v2`.
- O padrão v2 aprovado deve ser replicado como contrato visual, não como inspiração solta.
- Implementar primeiro em dev theme, validar visualmente e por computed styles, e só então promover para production com aprovação explícita, rollback e receipt.
- Não usar novos overrides soltos em `layout/theme.liquid` como padrão de evolução; se algum override tardio for necessário, ele deve fazer parte do contrato documentado e ser replicado/validado junto.

## Objetivo

Criar um contrato único para collections premium LK, evitando drift entre `lk-204l-*`, `lk-next-*` e hotfixes específicos por handle.

## Namespace

Classes base:

- `.lk-collection-v2`
- `.lk-collection-v2--{handle}`
- `.lk-collection-v2__inner`
- `.lk-collection-v2__copy`
- `.lk-collection-v2__eyebrow`
- `.lk-collection-v2__headline`
- `.lk-collection-v2__body`
- `.lk-collection-v2__media`
- `.lk-collection-v2__card`
- `.lk-collection-v2__card--large`

Elementos herdados do banner do tema que fazem parte do contrato visual:

- `.coll-banner`
- `.coll-banner__crumbs`
- `.coll-banner__title`

Handles migrados devem adicionar modificador:

- `.lk-collection-v2--new-balance-204l`
- `.lk-collection-v2--onitsuka-tiger-mexico-66`
- `.lk-collection-v2--onitsuka-tiger-mexico-66-sabot`

## Contrato desktop aprovado — 204L gold source

Valores aprovados após microajustes de Lucas:

- `.coll-banner`
  - fundo preto `#101010` via `--lk-v2-bg`
  - `padding: 40px clamp(28px,3.2vw,44px) 9px !important`
  - `margin-bottom: 0 !important`
  - mesma distância lateral da seção `.lk-collection-v2`; usar a seção como fonte de verdade.
- `.coll-banner__crumbs`
  - `font-size: 10px`
  - `line-height: 1.6`
  - `letter-spacing: .15em`
  - `margin: 0 0 14px`
  - topo do breadcrumb é a régua vertical para o topo da collage.
- `.coll-banner__title`
  - fonte: `Cormorant Garamond`
  - `font-size: clamp(42px,3.66vw,50px) !important`
  - computed aprovado no viewport validado: ~`46.85px`
  - `line-height: 1.04`
  - `max-width: min(48vw,620px)`
- `.lk-collection-v2`
  - `padding: 16px clamp(28px,3.2vw,44px) 30px !important`
  - `border-bottom: 1px solid #242424`
  - `box-shadow: 0 -1px 0 var(--lk-v2-bg)`
- `.lk-collection-v2__inner`
  - `max-width: 1440px`
  - grid desktop: `minmax(360px,.44fr) minmax(520px,.56fr)`
  - gap: `clamp(38px,4vw,64px)`
- `.lk-collection-v2__eyebrow`
  - texto aprovado: `Curadoria LK`
  - `font-size: 10px`
  - `letter-spacing: .19em`
  - `margin: 0 0 8px`
- `.lk-collection-v2__headline`
  - fonte: `Cormorant Garamond`
  - desktop médio aprovado: `32px` no breakpoint `990–1280px`
  - regra base: `clamp(30px,2.7vw,42px)`
  - `line-height: 1.02`
- `.lk-collection-v2__body`
  - `font-size: clamp(13.5px,.95vw,15.5px)`
  - em `990–1280px`: `14px`, `line-height: 1.62`
- `.lk-collection-v2__media`
  - grid collage: `1.08fr .92fr`, duas linhas
  - altura base: `clamp(340px,30vw,420px)`; em `990–1280px`: `372px`
  - desktop lift aprovado: `transform: translateY(-102px) !important`
  - compensação: `margin-bottom: -102px !important`
  - deve ficar acima visualmente do fundo do banner sem o banner cobrir as imagens.

## Invariantes de validação desktop

Antes de dizer que uma coleção está “igual ao padrão”, validar no browser:

- `titleFont` próximo do gold source no mesmo viewport.
- `titleLeft`, `crumbLeft`, `.lk-collection-v2__inner`/copy left com diferença **0px ou visualmente imperceptível**.
- `mediaTopMinusCrumbTop` próximo de `0–2px` no viewport de validação; na gold source final ficou ~`1.7px`.
- `bannerPaddingBottom` = `9px`.
- `rootPaddingTop` = `16px`.
- `eyebrowMarginBottom` = `8px`.
- `mediaTransform` = `translateY(-102px)` no desktop aprovado.
- Screenshot sem barra/máscara artificial evidente e sem sobreposição indesejada do `.coll-banner` sobre a collage.

Snippet de validação:

```js
(() => {
  const banner = document.querySelector('.coll-banner');
  const root = document.querySelector('.lk-collection-v2');
  const crumb = document.querySelector('.coll-banner__crumbs');
  const title = document.querySelector('.coll-banner__title');
  const inner = document.querySelector('.lk-collection-v2__inner');
  const copy = document.querySelector('.lk-collection-v2__copy');
  const media = document.querySelector('.lk-collection-v2__media');
  const eyebrow = document.querySelector('.lk-collection-v2__eyebrow');
  const headline = document.querySelector('.lk-collection-v2__headline');
  return {
    titleFont: getComputedStyle(title).fontSize,
    titleLeft: +title.getBoundingClientRect().left.toFixed(2),
    crumbLeft: +crumb.getBoundingClientRect().left.toFixed(2),
    innerLeft: +inner.getBoundingClientRect().left.toFixed(2),
    copyLeft: +copy.getBoundingClientRect().left.toFixed(2),
    leftDiffTitleVsInner: +(title.getBoundingClientRect().left - inner.getBoundingClientRect().left).toFixed(2),
    mediaTopMinusCrumbTop: +(media.getBoundingClientRect().top - crumb.getBoundingClientRect().top).toFixed(2),
    bannerPaddingBottom: getComputedStyle(banner).paddingBottom,
    rootPaddingTop: getComputedStyle(root).paddingTop,
    eyebrowMarginBottom: getComputedStyle(eyebrow).marginBottom,
    visualGapEyebrowHeadline: +(headline.getBoundingClientRect().top - eyebrow.getBoundingClientRect().bottom).toFixed(2),
    mediaTransform: getComputedStyle(media).transform
  };
})()
```

## Moon Shoe final — aprovação 2026-05-30

Lucas aprovou como **perfeito** o ajuste desktop da coleção `/collections/nike-x-jacquemus-moon-shoe-sp` após o topo do collage/imagens alinhar com o topo de `.coll-banner__crumbs`, e não com `.coll-banner__title`.

Contrato final aprovado para o padrão v2:

- O topo do bloco visual/collage deve usar `.coll-banner__crumbs` como régua vertical.
- Diferença alvo: `mediaTopMinusCrumbTop = 0px` ou visualmente imperceptível.
- `.coll-banner` não deve ter linha inferior no hero: `border-bottom: 0`.
- O layout deve preservar leitura produto-first: banner/título + collage editorial no topo, produtos logo depois, guia editorial após o grid.
- Para compatibilidade com páginas já construídas em `lk-204l-*`, pode haver classe dupla durante a migração:
  - legado operacional: `.lk-204l-coll-preview`, `.lk-204l-collage`, `.lk-204l-card`;
  - namespace canônico novo: `.lk-collection-v2`, `.lk-collection-v2__media`, `.lk-collection-v2__card`.
- Próximas coleções novas devem nascer diretamente em `lk-collection-v2`; `lk-204l-*` fica apenas como compatibilidade/ponte de migração, não como novo padrão.
- O asset canônico criado para novos temas é `assets/lk-collection-v2.css`, incluído em `layout/theme.liquid`.

Validação pública feita na produção após salvar dev + production:

```js
{
  hasV2: true,
  rootClass: "lk-204l-coll-preview lk-collection-v2 lk-collection-v2--nike-x-jacquemus-moon-shoe-sp",
  v2CssLoaded: true,
  runtime: true,
  mediaTopMinusCrumbTop: 0,
  collBannerBorder: "0px none"
}
```

## Processo obrigatório para replicar em próximas coleções

1. Criar implementação no Dev Theme `155065450718`.
2. Usar a 204L aprovada e a Moon Shoe final como gold sources: 204L para contrato base; Moon Shoe para o alinhamento breadcrumb → collage.
3. Usar o namespace novo `lk-collection-v2` desde o início:
   - `.lk-collection-v2`
   - `.lk-collection-v2--{handle}`
   - `.lk-collection-v2__inner`
   - `.lk-collection-v2__copy`
   - `.lk-collection-v2__eyebrow`
   - `.lk-collection-v2__headline`
   - `.lk-collection-v2__body`
   - `.lk-collection-v2__media`
   - `.lk-collection-v2__card`
   - `.lk-collection-v2__card--large`
4. Trocar apenas conteúdo, assets e modificador de handle; preservar o contrato visual.
5. Validar computed styles e screenshot.
6. Enviar preview com `preview_theme_id=155065450718` e cache-buster `lkqa=...`.
7. Produção só com aprovação explícita de Lucas, rollback e receipt.

## Não fazer

- Não corrigir cada handle com mais `:has(...)`/hotfix específico como estratégia principal.
- Não publicar production sem preview aprovado.
- Não declarar paridade apenas por métrica de DOM; validar screenshot e tipografia real.
- Não trocar a linguagem aprovada por labels como “Sinal editorial”; usar vocabulário premium e minimalista, como `Curadoria LK`.
- Não mudar espaçamentos por intuição quando Lucas pedir porcentagem; aplicar a redução/aumento literal e compensar media lift apenas quando necessário.

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

