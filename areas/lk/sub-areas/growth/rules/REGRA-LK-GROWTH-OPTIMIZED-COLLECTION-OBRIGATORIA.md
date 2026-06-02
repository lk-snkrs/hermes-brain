# REGRA — LK Growth Optimized Collection obrigatória

Criado em: 2026-06-01 19:50:47

## Regra absoluta

Toda coleção da LK Sneakers que for otimizada, melhorada, refeita, atualizada para SEO/GEO/CRO, ou receber guia/layout editorial deve obrigatoriamente passar pelo fluxo:

**LK Growth Optimized Collection**

Isso vale para qualquer pedido futuro de:

- otimizar coleção;
- melhorar SEO de coleção;
- melhorar GEO/AI Search/LLM de coleção;
- melhorar CRO de coleção;
- reescrever descrição de coleção;
- criar guia de coleção;
- atualizar layout de coleção;
- aplicar padrão 204L/Moon Shoe;
- atualizar hero/collage;
- adicionar Guia Editorial LK;
- melhorar coleção por ordem de visitas;
- atualizar coleções já otimizadas.

## O que é obrigatório

Uma coleção só pode ser tratada como otimizada se seguir o contrato completo **LK Growth Optimized Collection**:

1. passar pela skill `lk-superpowers-collection-optimizer`;
2. passar pela camada pensante **CLAUDE-SEO**;
3. usar texto de coleção no padrão SEO/GEO LK;
4. ter primeiro parágrafo forte antes do “Ler mais”;
5. usar layout `lk-collection-v2`/204L gold source quando aplicável;
6. ter hero/collage atualizado;
7. usar imagens editoriais reais, não PDP/packshot;
8. ter Guia Editorial LK pós-grid;
9. ter guia dedicado `/pages/guia-[handle]`;
10. ter seção visível “Referências editoriais e contexto”;
11. ter FAQ/schema correto;
12. preparar tag Shopify `LK Growth Optimized Collection`;
13. preparar metafields `lk_growth.*`;
14. registrar/atualizar ledger local;
15. validar em DEV;
16. gerar approval packet;
17. ter rollback/receipt;
18. publicar em produção apenas com aprovação explícita.

## Proibição

Não é permitido fazer “otimização parcial” de coleção e chamar de otimizada.

Se o pedido parecer pequeno — por exemplo, “melhorar só o texto da coleção” — o agente deve:

- avisar que isso toca o padrão LK Growth Optimized Collection;
- verificar se a coleção já é tagueada/registrada;
- se não for, propor entrada no fluxo completo ou registrar como exceção temporária;
- nunca esquecer guia dedicado, tag/metafield e ledger quando a otimização for final.

## Atualização em lote

Quando uma coleção tiver a tag/registro **LK Growth Optimized Collection**, qualquer atualização de layout/padrão deve considerar todas as coleções tagueadas.

Fluxo obrigatório:

1. consultar ledger/tag/metafields;
2. listar coleções afetadas;
3. aplicar alteração em todas no DEV;
4. gerar QA em lote;
5. pedir aprovação para produção;
6. publicar só com aprovação explícita.

## Fonte operacional

Skill principal:

`skills/lk-superpowers-collection-optimizer/SKILL.md`

Ledger:

`ledgers/lk-optimized-collections-ledger.json`

## Status

Regra aprovada por Lucas e obrigatória para LK Growth.

## Atualização de padrão — 2026-06-01T20:42:56Z

Feedback Lucas — piloto Adidas Samba Jane:

1. **Texto editorial principal deve ser maior**
   - O primeiro bloco textual da coleção otimizada não deve parecer curto ou apenas introdutório.
   - Padrão mínimo recomendado para o primeiro parágrafo/bloco hero: **500–700 caracteres**, mantendo leitura premium, humana e comercial.
   - Para modelos com apelo fashion/styling, reforçar: origem/identidade do modelo, leitura estética, ocasiões de uso, combinações e papel da curadoria LK.
   - Evitar texto genérico; cada coleção deve ter densidade suficiente para SEO/GEO e decisão de compra.

2. **Blocos de chamada para guia/CTA devem ter fundo claro**
   - O texto do tipo “Para aprofundar versões, materiais e proporção, abra o guia completo da coleção.” deve ficar em card/faixa de **fundo claro**, alinhado ao padrão premium LK.
   - Evitar fundo escuro nesse CTA, salvo aprovação visual específica.
   - Padrão visual: fundo claro, contraste suave, borda/linha discreta, tipografia legível e sensação editorial.

Regra: estes dois pontos passam a ser obrigatórios no QA de qualquer coleção com tag `LK Growth Optimized Collection`.

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

