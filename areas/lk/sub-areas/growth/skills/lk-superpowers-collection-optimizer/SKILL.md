# Skill — LK SUPERPOWERS Collection Optimizer

Versão: v1.0  
Atualizado em: 2026-06-01 19:34:26  
Área: LK Growth  
Status: aprovado como processo operacional local — produção sempre exige aprovação explícita.

## Missão

Transformar coleções Shopify da LK Sneakers em páginas premium de alta performance para SEO, GEO/AI Search, CRO e descoberta orgânica, sempre combinando:

- coleção produto-first otimizada;
- guia editorial dedicado;
- imagens editoriais reais;
- referências externas relevantes;
- tags/metafields/ledger;
- QA, approval e rollback.

## Gatilhos de uso

Use esta skill quando Lucas pedir:

- “otimizar coleção”;
- “melhorar SEO/GEO de coleção”;
- “criar guia de coleção”;
- “atualizar layout de coleção otimizada”;
- “aplicar padrão 204L/Moon Shoe”;
- “fazer guia LK”;
- “priorizar coleções por visitas”;
- “atualizar coleções tagueadas”;
- “seguir com SUPERPOWERS”.

## Contrato de coleção SUPERPOWERS

Uma coleção só pode ser chamada de **LK Growth Optimized Collection** quando todos os itens existirem ou tiverem exceção registrada:

1. Descrição principal reescrita no padrão SEO/GEO LK.
2. Primeiro parágrafo forte antes do “Ler mais”.
3. Layout `lk-collection-v2` baseado na 204L gold source.
4. Hero/collage atualizado.
5. Imagens editoriais reais, baixadas/subidas para Shopify/CDN própria quando possível.
6. Bloco editorial/visual com densidade semântica.
7. Grid de produtos antes do conteúdo longo.
8. Guia Editorial LK pós-grid.
9. Guia dedicado `/pages/guia-[handle]` no padrão Moon Shoe/Jacquemus.
10. Seção visível “Referências editoriais e contexto”.
11. FAQ e schema sem duplicação.
12. CTA cruzado coleção ↔ guia.
13. Tag Shopify `LK Growth Optimized Collection`.
14. Metafields `lk_growth.*`.
15. Registro no ledger local.
16. QA DEV.
17. Approval packet único.
18. Rollback/receipt.
19. Revisão de impacto em ~7 dias.
20. Refresh mensal do guia quando houver novidades.

## Documentos canônicos obrigatórios

Antes de executar, consultar:

- `PADRAO-CANONICO-GUIA-E-COLECAO-LK.md`
- `PADRAO-GUIAS-EDITORIAIS-LK.md`
- `PADRAO-LK-COLLECTION-V2.md`
- `PADRAO-TEXTO-COLECAO-LK.md`
- `rules/PADRAO-CRIACAO-TEXTO-COLECOES-SEO-GEO-LK.md`
- `PADRAO-CANONICO-BLOCO-GUIA-POS-GRID-COLECOES-LK.md`
- `rules/REGRA-PRODUCTION-GUIAS-COLECOES-LK.md`
- `references/collection-204l-gold-source-final/`
- `references/moon-shoe-jacquemus-canonical-guide-pattern.html`

## Camada pensante obrigatória — CLAUDE-SEO

Toda otimização de coleção SUPERPOWERS deve passar por uma etapa explícita de raciocínio **CLAUDE-SEO** antes de escrever ou publicar copy.

Função da camada CLAUDE-SEO:

- transformar pesquisa, SERP, GSC, contexto de moda e intenção comercial em estrutura semântica;
- definir entidades principais e secundárias;
- mapear intenção de busca: informacional, comercial, comparação, autenticidade, styling e compra;
- decidir hierarquia de texto: descrição principal, primeiro parágrafo, bloco editorial, guia pós-grid, guia dedicado e FAQ;
- evitar texto genérico de SEO e keyword stuffing;
- criar blocos citáveis para LLM/GEO;
- garantir tom LK: premium, humano, curadoria e conversão;
- cruzar conteúdo da coleção com o guia dedicado e referências editoriais;
- gerar perguntas reais para FAQ e dúvidas de decisão.

Saídas obrigatórias da etapa CLAUDE-SEO:

1. mapa de intenção de busca;
2. entidades/termos principais;
3. ângulos editoriais;
4. estrutura recomendada da descrição;
5. estrutura recomendada do guia;
6. FAQ orientado a decisão;
7. riscos de copy genérica, excesso de SEO ou desalinhamento premium.

Essa etapa deve aparecer no brief/approval packet ou ficar registrada no artefato de copy.

## Fluxo obrigatório

### 0. Priorização

- Ordenar por visitas/sessões/receita quando Shopify/GA4 estiverem disponíveis.
- Usar GSC para impressões, cliques, CTR e posição.
- Se faltarem dados autenticados, marcar como **não decision-grade**.

### 1. Auditoria da coleção atual

Verificar:

- handle, title, descrição, SEO fields;
- produtos no grid;
- layout/template atual;
- existência de guia;
- imagens atuais;
- FAQ/schema;
- tags/metafields;
- performance e oportunidade.

### 2. Pesquisa editorial/SERP

Pesquisar:

- principais queries;
- SERP/PAA;
- concorrentes;
- publicações de moda/sneaker/cultura;
- imagens editoriais reais;
- novidades/collabs recentes.

Critério de imagem válida:

- pessoa usando;
- campanha com styling;
- editorial real;
- street style;
- ambiente/atelier/ativação;
- contexto cultural.

Proibido:

- packshot;
- PDP;
- produto isolado;
- release frio sem styling;
- imagem de portal de moda que ainda seja só produto isolado.

### 3. Brief

Criar brief com template `templates/brief-template.md`.

### 4. Copy

Criar:

- descrição principal em 3 `<p>` reais;
- primeiro parágrafo 350–450 chars;
- bloco editorial/visual 600–800 chars em coleções prioritárias;
- guia pós-grid;
- guia dedicado completo;
- FAQ;
- seção “Referências editoriais e contexto”.

### 5. Assets

- Baixar imagens aprovadas quando permitido/tecnicamente possível.
- Subir para Shopify/CDN própria antes de produção.
- Registrar URL original, veículo, contexto, crédito e data.

### 6. Implementação DEV

- Alterar sempre primeiro no Dev Theme.
- CTAs podem usar âncoras enquanto page pública não existir.
- Não criar/alterar produção sem aprovação.
- Não criar Shopify Pages públicas sem aprovação.

### 7. QA DEV

Usar `templates/qa-template.json` e `checklists/qa-checklist.md`.

### 8. Approval packet

Usar `templates/approval-packet-template.md`.

Approval único deve conter:

- coleção;
- guia dedicado;
- CTA;
- assets;
- tags/metafields;
- ledger;
- QA;
- rollback.

### 9. Produção aprovada

Com aprovação explícita no turno atual:

- publicar alterações de coleção;
- criar/atualizar guia público;
- trocar CTA para URL final;
- aplicar tag/metafields;
- atualizar ledger;
- gerar receipt;
- programar revisão de impacto.

## Atualização em lote

Quando Lucas pedir atualização de layout/padrão em coleção otimizada:

1. Consultar tag/metafields/ledger.
2. Identificar todas as coleções `LK Growth Optimized Collection`.
3. Aplicar atualização em todas no DEV.
4. QA comparativo em lote.
5. Approval para produção.
6. Produção apenas após aprovação.

## Refresh mensal de guias

Mensalmente, revisar guias otimizados por ordem de visitas/tráfego:

- novas collabs;
- novos colorways;
- novidades de marca/modelo;
- novas publicações relevantes;
- atualização da seção “Referências editoriais e contexto”.

## Guardrails

Nunca:

- publicar produção sem aprovação;
- alterar Shopify Page pública sem aprovação;
- aplicar tag/metafield externo sem aprovação;
- usar PDP/packshot como hero editorial;
- fazer guia sem layout Moon Shoe/Jacquemus;
- chamar de otimizada uma coleção sem guia dedicado;
- alterar só uma coleção quando a mudança for global do padrão;
- ignorar rollback.

## 2026-06-01 19:50:47 — Regra obrigatória LK Growth Optimized Collection

Toda coleção que for otimizada/melhorada para SEO, GEO/AI Search, CRO, layout, hero, guia ou texto deve obrigatoriamente passar pelo fluxo **LK Growth Optimized Collection**, usando a skill `lk-superpowers-collection-optimizer`, camada CLAUDE-SEO, guia dedicado, Guia Editorial LK pós-grid, imagens editoriais reais, tag/metafields e ledger. Regra canônica: `rules/REGRA-LK-GROWTH-OPTIMIZED-COLLECTION-OBRIGATORIA.md`.

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

