# QA Checklist — LK SUPERPOWERS Collection Optimizer

Atualizado em: 2026-06-02T11:06:41Z

## Camada CLAUDE-SEO

- [ ] Mapa de intenção de busca registrado.
- [ ] Entidades principais/secundárias definidas.
- [ ] Ângulos editoriais definidos.
- [ ] FAQ nasceu de dúvidas reais de decisão.
- [ ] Copy evita keyword stuffing e texto genérico.
- [ ] Estrutura conversa com GEO/LLM e tom LK.

## Coleção

- [ ] Handle correto.
- [ ] Dev Theme usado antes de production.
- [ ] H1/title preserva intenção da coleção.
- [ ] Descrição principal em múltiplos `<p>` reais.
- [ ] Primeiro parágrafo/bloco hero tem **500–700 chars** ou exceção registrada; regra antiga de 350–450 chars está obsoleta para LKGOC.
- [ ] Primeiro parágrafo menciona modelo/coleção, LK Sneakers, original/autenticidade e intenção de busca.
- [ ] “Ler mais” presente e funcional.
- [ ] Bloco editorial/visual tem densidade suficiente, idealmente 600–800 chars em coleção prioritária.
- [ ] Não há duplicação literal entre descrição principal e bloco editorial.
- [ ] Layout segue `lk-collection-v2`/204L gold source.
- [ ] Hero/collage atualizado.
- [ ] Produto aparece antes do guia longo.
- [ ] Guia pós-grid aparece após grid com respiro visual.
- [ ] FAQ/schema único, sem duplicação visual/JSON-LD.
- [ ] Modal de imagem funciona.
- [ ] Mobile não quebra leitura/product-first.

## Imagens/assets

- [ ] Imagens não são PDP/packshot/produto isolado.
- [ ] Imagens têm pessoa usando, campanha, styling, ambiente real, ativação ou contexto cultural.
- [ ] Fonte original registrada.
- [ ] Asset baixado/subido para Shopify/CDN própria quando possível.
- [ ] Alt text coerente e premium.

## Guia dedicado

- [ ] Página guia existe em DEV/local antes da produção.
- [ ] Layout segue Moon Shoe/Jacquemus como shell editorial, não apenas classes/copy.
- [ ] Não é `<article>` simples, texto corrido, Markdown/HTML cru ou FAQ básico sem layout.
- [ ] Hero editorial premium presente.
- [ ] Imagem contextual/editorial renderizada.
- [ ] Tipografia/spacing com aparência de matéria premium.
- [ ] Tabela comparativa útil quando houver versões, colorways, materiais, proporção ou usos.
- [ ] Cards/fontes externas com links e contexto editorial.
- [ ] Texto completo SEO/GEO/LLM.
- [ ] Blocos citáveis LK.
- [ ] FAQ visual no padrão.
- [ ] CTA discreto para coleção.
- [ ] Seção visível “Referências editoriais e contexto”.
- [ ] Links externos relevantes funcionam.
- [ ] Render desktop validado visualmente contra Moon Shoe.
- [ ] Render mobile validado visualmente contra Moon Shoe.
- [ ] Hero preto/full-bleed no padrão aprovado, não hero branco/texto corrido.
- [ ] Texto abaixo do hero segue a mesma régua/largura útil do hero; H2/parágrafos/quote não ficam estreitos/desalinhados.
- [ ] Imagem do hero é editorial/com pessoa usando e o tênis está claramente visível, sem calça tapando, corte ruim ou escala pequena.
- [ ] Legenda e alt não prometem o que a imagem não mostra.
- [ ] FAQ: até 4 perguntas em 1 coluna desktop; se passar de 4, usar 6 ou 8 perguntas e grid 2 colunas equilibrado no desktop; mobile 1 coluna.
- [ ] CTA final discreto, alinhado à régua e sem quebrar em duas linhas no desktop quando couber.
- [ ] Se qualquer item visual falhar, bloquear production mesmo com HTTP/title/meta/schema corretos.

## Governança

- [ ] Tag proposta: `LK Growth Optimized Collection`.
- [ ] Metafields propostos/preparados.
- [ ] Ledger local atualizado/preparado.
- [ ] Approval packet gerado.
- [ ] Rollback plan pronto.
- [ ] Produção não tocada sem aprovação explícita.

## Regra Telegram/preview — draft visível em Shopify DEV — 2026-06-02T12:14:03Z

Feedback Lucas: draft local sozinho não serve em fluxo por Telegram, porque Lucas não consegue ver/validar visualmente.

Regra obrigatória LKGOC:

- Todo draft visual de coleção, Guia LK, source page, CTA, FAQ ou bloco editorial deve ser materializado em **Shopify DEV theme/preview** antes de pedir opinião/aprovação.
- A resposta no Telegram deve trazer o **link direto de preview Shopify** (`preview_theme_id=155065450718` ou tema DEV ativo equivalente).
- Arquivo local/Brain é apenas backup/rollback/evidência; não é output final para Lucas validar.
- Se ainda não for possível criar preview no Shopify DEV, declarar bloqueio técnico e não apresentar como “pronto”.
- Para guia dedicado, o padrão é: rascunho → snippet/template/section no DEV theme → URL preview clicável → QA visual desktop/mobile → só então approval de produção.

## Regra visual canônica — hero preto LK — 2026-06-02T12:24:15Z

Correção Lucas: o padrão aprovado New Balance 204L / Moon Shoe não usa hero editorial branco. O hero/topo deve ter base **preta/escura**, com texto claro e imagem/editorial integrada.

Aplicação obrigatória:
- Coleções produto-first: `lk-collection-v2` com banner/hero preto (`#101010` ou equivalente), como New Balance 204L.
- Guias dedicados `/pages/guia-*`: shell editorial com hero preto/full-bleed, seguindo Moon Shoe; nunca hero branco/texto corrido dentro do `main-page` estreito.
- QA visual deve comparar explicitamente: fundo do hero, largura do hero, contraste, presença de imagem/contexto, tabela/cards/FAQ e CTA discreto.

## Regra de fontes externas — portais internacionais primeiro — 2026-06-02T12:43:12Z

Feedback Lucas: cliente brasileiro valoriza saber o que está “bombando lá fora”.

Regra obrigatória para Guia LK e blocos GEO:
- Links externos de referência devem priorizar **portais internacionais de moda/sneakers/cultura**: ex. Vogue, GQ, Highsnobiety, Hypebeast/Hypebae, Who What Wear, Glamour US/UK, Elle, Harper's Bazaar, Complex, Sneaker News, Sole Retriever, WWD.
- Evitar usar portal brasileiro como card de autoridade principal quando o objetivo é tendência/styling/global signal.
- Fonte oficial da marca pode entrar como evidência de produto, mas os cards editoriais devem mostrar leitura internacional/tendência global.
- Se usar fonte brasileira, deve ser exceção justificada, não padrão.

## Refinamento de fontes internacionais — revistas de moda reconhecíveis — 2026-06-02T12:47:59Z

Feedback Lucas por áudio: quando for usar links externos em guias LK, priorizar revistas/portais internacionais de moda reconhecíveis pelo cliente brasileiro, porque dão mais percepção de desejo global.

Prioridade editorial obrigatória para cards/fonte externa:
1. **Revistas de moda internacionais mainstream e aspiracionais**: Vogue, GQ, Marie Claire, Elle, Harper's Bazaar, Glamour, Who What Wear, W Magazine, InStyle, Vanity Fair quando relevante.
2. **Portais sneaker/streetwear globais**: Highsnobiety, Hypebeast/Hypebae, Complex, Sneaker News, Sole Retriever, WWD.
3. **Fonte oficial da marca**: usar para evidência técnica/produto, não como principal prova de tendência.
4. **Fontes brasileiras**: só como exceção justificada; não usar como card principal de tendência global.

Critério comercial: escolher fontes que comuniquem “isso está bombando lá fora” de forma imediatamente reconhecível para o público LK.

## Referência LKGOC

O padrão completo de LKGOC vive em um único documento canônico:

- `LKGOC-PADRAO-CANONICO.md`

Não duplicar regras longas aqui. Este arquivo deve apenas complementar seu escopo específico e apontar para o canônico.
