# Padrão LK — Guias editoriais, source pages e páginas de coleção

Este documento define o padrão obrigatório para qualquer guia editorial, source page, guia linkado em coleção ou página de apoio SEO/GEO da LK Sneakers.

## Regra central

A LK tem **dois moldes canônicos diferentes**. Não misturar:

1. **Coleção Shopify produto-first** → padrão visual/comercial **New Balance 204L**.
   - URL pública de referência: `https://lksneakers.com.br/collections/new-balance-204l`
   - Uso: coleção com produtos primeiro, hero escuro com collage, guia/FAQ pós-grid.
   - Regra: uma nova coleção produto-first deve espelhar a 204L em estrutura, hierarquia, espaçamento, grid, hero, guide card e FAQ. Trocam-se apenas copy, assets e fatos específicos.

2. **Guia editorial/source page independente** → padrão visual/editorial **Nike x Jacquemus Moon Shoe**.
   - URL pública de referência: `https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk`
   - Snapshot canônico local: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/references/moon-shoe-jacquemus-canonical-guide-pattern.html`
   - Referência interna: guia Moon Shoe / Jacquemus / “Monshu”

Atenção: se o navegador estiver preso em **Shopify dev preview** (`lk-new-theme/dev`, barra “Draft”), a URL pública Moon Shoe pode renderizar só o título/rodapé porque o preview usa outro tema/template. Para auditoria desse padrão, usar a URL fora do preview ou o snapshot local acima.

Nenhuma coleção/guia deve ser criada como página textual genérica ou como variação solta. Antes de criar ou alterar: classificar tipo, declarar molde e validar contra o molde correto.

## Lei anti-invenção

A LK não cria páginas “da cabeça”. Todo novo guia, página de marca, source page ou coleção editorial deve nascer de um dos moldes aprovados abaixo. Se o pedido não encaixar em um molde existente, o executor deve primeiro propor um **novo padrão/template para aprovação** e só depois criar a página.

Regras obrigatórias:

- reutilizar estrutura, hierarquia visual, espaçamento e componentes aprovados;
- declarar qual molde está sendo usado antes de escrever ou montar a página;
- consultar fontes reais antes de afirmar contexto de marca, cultura, collab, materiais ou origem do modelo;
- nunca inventar nomes de seções, labels visíveis, CTAs ou formatos novos sem aprovação;
- quando houver dúvida entre “coleção” e “guia”, separar: coleção vende primeiro; guia aprofunda depois;
- toda exceção precisa ficar registrada no brief, com motivo comercial/SEO/CRO claro.

## Moldes canônicos

1. **Coleção Shopify produto-first**
   - Produtos aparecem antes de qualquer texto longo.
   - Topo minimalista no padrão 204L: H1 limpo e dominante; kicker curto sem repetir o nome da coleção; parágrafo breve; hero escuro com collage quando o molde for aplicado.
   - Se o H1 já mostra o nome da coleção, o kicker não repete esse nome. Exemplo correto: `CURADORIA LK`; evitar `CURADORIA LK · NEW BALANCE 204L` quando o H1 já é `New Balance 204L`.
   - Grid padrão: 20 produtos por página para preservar respiro, performance e leitura premium; exceções precisam ser aprovadas no brief.
   - Guia/FAQ/schema ficam depois do grid ou em página linkada.
   - Padrão visual de referência quando aplicável: **New Balance 204L**.
   - Paridade 204L exige validação renderizada, não só cópia de classes: H1 ~52px desktop, `display:inline-block`, collage alinhado ao topo do breadcrumb, mesmo padding superior do bloco, mesma altura/transform/margem do collage, card pós-grid 2 colunas e FAQ alinhado ao título da coluna esquerda.

2. **Guia editorial linkado à coleção**
   - Página independente em `/pages/guia-...`.
   - Visual e estrutura no padrão Moon Shoe.
   - A coleção pode ter CTA discreto apontando para o guia, mas não deve virar uma matéria longa antes dos produtos.

3. **Source page / matéria de marca ou collab**
   - Página editorial premium para contexto de marca, collab, origem, matérias externas e leitura de curadoria.
   - Hero forte, fontes externas, cards de referência, blocos citáveis LK e CTA discreto.
   - Não pode ser artigo simples de texto corrido.

4. **Página de apoio SEO/GEO / autenticidade / comparação**
   - Usa o padrão editorial quando for customer-facing.
   - Deve ter fontes, tabela ou checklist útil, FAQ e blocos citáveis.
   - Não pode virar página genérica de palavras-chave.

## Ordem obrigatória de criação

1. Classificar o tipo: coleção produto-first, guia linkado, source page ou apoio SEO/GEO.
2. Abrir o padrão canônico correspondente: Moon Shoe para guias/source pages; 204L para coleção produto-first quando aplicável.
3. Preencher `templates/brief-guia-editorial-colecao-lk.md`.
4. Listar fontes reais que serão usadas.
5. Produzir rascunho/preview no molde escolhido.
6. Fazer QA contra este documento antes de pedir aprovação.
7. Só fazer write em Shopify produção com aprovação explícita.

## O que torna o padrão correto

O guia correto tem aparência de matéria editorial premium, não de bloco SEO simples. Ele combina:

- curadoria de produto;
- narrativa de moda;
- fontes externas relevantes;
- comparação clara;
- visual rico;
- FAQ estruturada;
- CTA comercial discreto.

## Estrutura obrigatória

Todo guia novo deve conter, salvo justificativa explícita:

1. **Hero editorial**
   - layout visual forte;
   - imagem contextual/editorial;
   - eyebrow curto;
   - H1 com leitura premium;
   - introdução curada, não genérica.

2. **Fonte/tipografia com cara editorial**
   - uso de fonte serifada para H1 e headings quando aplicável;
   - espaçamento de matéria;
   - hierarquia visual refinada;
   - nada com aparência de texto corrido básico.

3. **Imagem ou módulo visual relevante**
   - imagem de produto, campanha, street style ou contexto cultural;
   - alt text descritivo;
   - não usar imagem apenas decorativa sem contexto.

4. **Tabela comparativa**
   - obrigatória sempre que houver versões, colorways, materiais, proporções ou usos diferentes;
   - formato similar ao Moon Shoe: `Colorway / Leitura visual / Por que importa` ou equivalente;
   - a tabela deve ajudar a comprar melhor, não apenas preencher SEO.

5. **Sinais editoriais e fontes externas**
   - cards com links para fontes como Vogue, GQ, Hypebeast, Hypebae, Highsnobiety, Adidas/Nike/Onitsuka oficial etc.;
   - explicar por que a fonte importa para a leitura do produto;
   - usar `rel="nofollow noopener"` quando link externo;
   - nunca inventar fonte ou citação.

6. **Blocos citáveis LK**
   - blocos próprios com frases que uma IA ou Google AI Overview conseguiria citar;
   - linguagem clara, factual e premium;
   - sem parecer briefing interno.

7. **Contexto de moda/cultura**
   - origem do modelo;
   - por que voltou ou importa hoje;
   - como aparece em styling, cultura pop, runway, street style ou collabs;
   - relação com o olhar de curadoria da LK.

8. **Orientação comercial real**
   - explicar diferença entre versões, materiais, proporção, cor e contexto de uso;
   - ajudar o cliente a escolher;
   - manter a LK como boutique premium com atendimento humano.

9. **FAQ em acordeão ou estrutura equivalente**
   - perguntas úteis para compra;
   - respostas objetivas;
   - compatível com Schema/FAQ quando aplicável.

10. **CTA discreto**
   - botão preto/limpo ou equivalente premium;
   - direcionar para coleção/produtos relevantes ou atendimento;
   - não usar CTA grosseiro ou repetitivo.

## Linguagem obrigatória

Usar:

- curadoria exclusiva;
- boutique premium;
- seleção especializada;
- produto original;
- atendimento humano;
- orientação de escolha;
- versão, material, proporção, cor, contexto de uso.

Evitar:

- “pronta entrega”, “encomenda”, “estoque” como taxonomia pública;
- texto genérico de SEO;
- blocos visíveis com rótulos internos como “Sinal editorial”;
- promessa operacional que deve ficar no atendimento;
- linguagem de marketplace ou busca por menor preço.

## Checklist antes de publicar

Antes de qualquer guia ir para produção, verificar:

- [ ] O guia Moon Shoe foi usado como referência visual.
- [ ] Há hero editorial com imagem.
- [ ] Há tabela comparativa útil.
- [ ] Há pelo menos uma seção de fontes externas/fashion signals quando o tema permitir.
- [ ] Há blocos citáveis LK.
- [ ] Há FAQ.
- [ ] Há CTA discreto.
- [ ] A copy evita linguagem operacional proibida.
- [ ] O topo da coleção foi revisado quando o guia for linkado em coleção.
- [ ] O guia não é apenas texto corrido.
- [ ] O link da coleção aponta para `/pages/...`, não só para âncora interna.
- [ ] Existe rollback/backup antes de qualquer alteração em produção.

## Fluxo obrigatório para próximos guias

1. Pesquisar o produto/modelo em fontes de moda, cultura sneaker, site oficial e SERP.
2. Abrir o guia Moon Shoe e mapear a estrutura visual.
3. Criar rascunho HTML no padrão Moon Shoe.
4. Validar se há tabelas, imagens, fonte editorial, cards de referência e FAQ.
5. Gerar preview/local ou dev quando possível.
6. Só publicar em produção com aprovação explícita quando houver alteração visível.
7. Após publicar, validar HTML público, mobile e links.
8. Registrar receipt e rollback.

## Aplicação imediata

As páginas atuais abaixo precisam ser refeitas para esse padrão antes de serem consideradas finais:

- `https://lksneakers.com.br/pages/guia-adidas-samba`
- `https://lksneakers.com.br/pages/guia-onitsuka-tiger-mexico-66`

Problema identificado nelas:

- sem tabelas;
- sem cards de fontes externas;
- sem estrutura visual Moon Shoe;
- muito textuais para o padrão LK.

## Status

Este padrão é mandatório para LK Growth, SEO/GEO, Shopify collection pages e qualquer guia editorial ligado a coleção ou produto.

## 2026-06-01 19:50:47 — Regra obrigatória LK Growth Optimized Collection

Toda coleção que for otimizada/melhorada para SEO, GEO/AI Search, CRO, layout, hero, guia ou texto deve obrigatoriamente passar pelo fluxo **LK Growth Optimized Collection**, usando a skill `lk-superpowers-collection-optimizer`, camada CLAUDE-SEO, guia dedicado, Guia Editorial LK pós-grid, imagens editoriais reais, tag/metafields e ledger. Regra canônica: `rules/REGRA-LK-GROWTH-OPTIMIZED-COLLECTION-OBRIGATORIA.md`.

## Padrão obrigatório refinado — 2026-06-01T20:43:30Z

Feedback visual/textual aprovado por Lucas no piloto Adidas Samba Jane:

- **Texto hero/editorial maior:** o primeiro texto da coleção otimizada deve ter mais corpo. Usar como referência **500–700 caracteres** no primeiro parágrafo/bloco, com densidade de styling, intenção de uso, leitura estética e curadoria LK. Textos curtos demais passam a reprovar QA.
- **CTA de guia em fundo claro:** chamadas como “Para aprofundar versões, materiais e proporção, abra o guia completo da coleção.” devem usar **fundo claro**, visual premium e contraste suave. Fundo escuro nesse CTA não é padrão e só deve ser usado se Lucas aprovar explicitamente.
- **QA obrigatório:** antes de considerar uma coleção `LK Growth Optimized Collection` pronta, validar: texto principal com corpo suficiente + card/CTA de guia em fundo claro.

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

