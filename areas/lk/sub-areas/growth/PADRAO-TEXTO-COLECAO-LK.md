# Padrão canônico — texto de coleção LK

Status: **aprovado como complemento do padrão 204L**.
Fonte analisada por HTML público: `https://lksneakers.com.br/collections/new-balance-204l`.
Relação: este documento complementa `PADRAO-CANONICO-GUIA-E-COLECAO-LK.md` e o snapshot literal `references/collection-204l-gold-source-final/`.

## Princípio

Ao criar ou padronizar uma nova coleção LK, o texto da coleção não deve ser apenas um parágrafo genérico. Ele deve ser uma curadoria curta, premium e útil, com densidade semântica suficiente para SEO/GEO, mantendo a página product-first.

O texto pode ter **1 ou 2 parágrafos**. Dois parágrafos são preferíveis quando a coleção tem história, collab, fit, materiais, colorways ou intenção de busca clara.

## Estrutura recomendada do texto da coleção

### Parágrafo 1 — definição + intenção de busca

Responder de forma natural:

- o que é a linha/modelo/collab;
- por que ela importa;
- qual silhueta, estética ou categoria ela representa;
- quais termos de busca reais fazem sentido para a coleção.

Exemplo de função, não de copy fixa:

> O [modelo/linha] traduz [busca estética ou funcional] em uma silhueta [descrição objetiva], com [materiais/proporção/história] e leitura [fashion/casual/performance/colecionável].

### Parágrafo 2 — curadoria LK + decisão de compra

Responder:

- como a LK seleciona a coleção;
- quais cores, versões, materiais ou combinações merecem atenção;
- como o cliente deve escolher;
- reforço de autenticidade e atendimento humano;
- chamada discreta para confirmar melhor opção via chat, quando necessário.

Exemplo de função, não de copy fixa:

> Na LK Sneakers, a curadoria prioriza [colorways/versões] para quem busca [intenção comercial], com autenticidade e orientação humana para comparar cor, proporção, tamanho e melhor uso antes da escolha.

## Regras de SEO/GEO

- Incluir naturalmente o nome da coleção/modelo no H1 e no texto.
- Usar variações semânticas reais: `original`, `masculino`, `feminino`, `unissex`, `colorway`, `collab`, `edição`, `silhueta`, `perfil baixo`, `camurça`, `mesh`, etc. apenas quando forem verdadeiras para a coleção.
- Preferir frases citáveis por IA: claras, autocontidas e sem depender do layout.
- Não encher de keyword stuffing. A copy deve soar como curadoria humana, não bloco SEO.
- Quando houver guia dedicado, o texto da coleção deve introduzir e o guia deve aprofundar.

## Tom LK

- premium;
- minimalista;
- editorial;
- humano;
- comercialmente inteligente;
- seguro e direto.

## Termos e limites

Evitar em superfície pública:

- `estoque` como taxonomia;
- `encomenda`;
- `pronta entrega`;
- linguagem operacional de Tiny/fornecedor;
- rótulos inventados que pareçam internos.

Fit/tamanho:

- não usar “roda grande/pequeno”;
- usar `tem forma grande`, `tem forma regular`, `tem forma mais apertada`, `sensação mais apertada no pé`.

## Padrão observado na 204L por HTML

HTML público validado na coleção 204L:

- H1: `New Balance 204L`.
- Title SEO: `New Balance 204L Original na LK Sneakers`.
- Meta description: `Compre New Balance 204l original na LK Sneakers. Alta procura, curadoria premium, autenticidade garantida e opções em até 10x.`
- Hero textual com dois níveis:
  - H2 curto/editorial: `Perfil baixo, leitura fashion.`
  - texto de coleção com definição + curadoria + orientação humana.
- Guia pós-grid com H2 explicativo e FAQ integrado.
- `FAQPage` único no HTML.

## Checklist antes de publicar preview

- O texto tem 1–2 parágrafos úteis, não apenas uma frase decorativa.
- A primeira frase define a coleção/modelo.
- A segunda camada explica a curadoria LK e ajuda a escolher.
- O texto conversa com SEO/GEO sem perder tom premium.
- Produto continua vindo antes do guia longo.
- Sem termos proibidos.
- Guia dedicado, quando existir, está linkado e coerente.

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

