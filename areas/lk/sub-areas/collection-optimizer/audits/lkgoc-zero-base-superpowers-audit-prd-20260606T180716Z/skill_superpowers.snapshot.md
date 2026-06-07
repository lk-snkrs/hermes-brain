# Skill — LK SUPERPOWERS Collection Optimizer

Versão: v1.2  
Atualizado em: 20260606T164407Z  
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
9. Guia dedicado `/pages/guia-[handle]` no shell editorial Moon Shoe/Jacquemus, nunca texto corrido ou artigo cru.
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

Antes de executar, consultar **nesta ordem**:

1. `LKGOC-PADRAO-CANONICO.md` — fonte única de verdade; se houver divergência, este arquivo vence.
2. `PADRAO-CANONICO-GUIA-E-COLECAO-LK.md`
3. `PADRAO-GUIAS-EDITORIAIS-LK.md`
4. `PADRAO-LK-COLLECTION-V2.md`
5. `PADRAO-TEXTO-COLECAO-LK.md`
6. `rules/PADRAO-CRIACAO-TEXTO-COLECOES-SEO-GEO-LK.md`
7. `PADRAO-CANONICO-BLOCO-GUIA-POS-GRID-COLECOES-LK.md`
8. `rules/REGRA-PRODUCTION-GUIAS-COLECOES-LK.md`
9. `references/collection-204l-gold-source-final/`
10. `references/moon-shoe-jacquemus-canonical-guide-pattern.html`

Regra de conflito: normas antigas/auxiliares que falem em hero branco/off-white, primeiro parágrafo de 350–450 caracteres, FAQ duplicado ou draft local como output final estão obsoletas para LKGOC se conflitarem com `LKGOC-PADRAO-CANONICO.md`.


## Gates visuais obrigatórios — padrão aprovado Lucas

O LKGOC tem dois padrões visuais canônicos e não deve inventar variação:

1. **Coleção produto-first:** New Balance 204L (`lk-collection-v2`).
   - Produto aparece antes de conteúdo longo.
   - Hero/header, collage, grid, guia pós-grid e FAQ seguem a gold source 204L.

2. **Guia LK dedicado `/pages/guia-*`:** Nike x Jacquemus Moon Shoe.
   - Shell editorial premium obrigatório.
   - Hero visual preto/full-bleed (`#101010` ou equivalente), texto claro e CTAs discretos.
   - Tipografia/spacing editorial, imagem contextual com pessoa usando o modelo, tabela comparativa quando aplicável, fontes/cards, blocos citáveis, FAQ e CTA discreto.
   - A régua horizontal do conteúdo abaixo do hero deve seguir a mesma lógica do hero: mesmo rail/margem esquerda e mesma largura útil visual. Não deixar H2/parágrafos/quote voltarem para coluna estreita dentro do `main-page`.
   - FAQ visual: até 4 perguntas = 1 coluna no desktop; acima de 4 usar número par e equilibrado, preferencialmente 6 ou 8 perguntas em 2 colunas no desktop; mobile continua 1 coluna.

Regra de bloqueio: guia dedicado publicado ou pronto como `<article>` simples, texto corrido, Markdown/HTML cru, FAQ básico, hero branco fora do padrão, imagem em que o tênis não aparece claramente, ou shell sem a régua/largura Moon Shoe **não é Guia LK aprovado**. Reprovar QA e refazer em DEV/local antes de qualquer production.

Não esperar Lucas pedir para salvar padrão: quando Lucas aprovar visualmente uma referência ou corrigir um padrão, registrar imediatamente na regra LKGOC, checklist e template aplicável.



## v1.2 — Contract Lock bloqueante antes de qualquer write LKGOC

Atualizado em: 20260606T164407Z. Esta seção existe por causa da falha Puma Speedcat/Nike Dunk em que o agente validou código/DOM, mas não validou o contrato visual LKGOC.

Antes de escrever em Shopify, criar e registrar um **LKGOC Contract Lock**. Sem ele, a tarefa deve parar com status `BLOQUEADO / NÃO LKGOC`.

Campos obrigatórios do Contract Lock:

1. `gold_source_collection`: URL/snapshot/asset exato da coleção aprovada que será clonada.
2. `gold_source_guide`: URL/snapshot/asset exato do guia aprovado que será clonado.
3. `immutable_visual_contract`: hierarquia, densidade, grid antes do guia, guia pós-grid, FAQ/schema, mobile/desktop.
4. `media_manifest`: cada imagem com fonte, licença/status, screenshot e aprovação visual.
5. `hero_has_person_using_product`: deve ser verdadeiro; packshot/PDP/produto isolado reprova.
6. `guide_pattern_manifest`: prova de que o guia segue o padrão aprovado, não bloco simplificado.
7. `acceptance_tests`: testes visuais e técnicos que serão usados antes de enviar preview ao Lucas.

Regras duras:

- Componente único correto **não é suficiente** para chamar de LKGOC.
- DOM/HTTP/readback sem QA visual **não é suficiente**.
- Se faltar imagem de pessoa usando/contexto editorial seguro, parar e pedir asset ao Lucas.
- Se o guia não estiver clonado do gold source, parar.
- Workers Visual QA e LKGOC Experience Architect têm poder de veto antes do write.
- Nunca executar lote de 5 sem aprovar primeiro uma coleção piloto.

Arquivo complementar: `areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-CONTRACT-LOCK-ANTES-DE-WRITE.md`.

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

- pessoa usando o modelo ou uma silhueta equivalente com leitura clara;
- tênis visível: não pode estar tapado por calça, cortado, escuro demais ou pequeno a ponto de não dar para reconhecer;
- campanha com styling;
- editorial real;
- street style;
- ambiente/atelier/ativação;
- contexto cultural;
- fonte registrada e legenda fiel ao que a imagem realmente mostra.

Proibido:

- packshot;
- PDP;
- produto isolado;
- release frio sem styling;
- imagem de portal de moda que ainda seja só produto isolado;
- pessoa usando em que o produto fica escondido pela roupa;
- legenda/alt afirmando que o tênis aparece quando ele não aparece claramente.

### 3. Brief

Criar brief com template `templates/brief-template.md`.

### 4. Copy

Criar:

- descrição principal em 3 `<p>` reais;
- primeiro parágrafo/bloco hero 500–700 chars, salvo exceção registrada;
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

Gate obrigatório: comparar render desktop/mobile contra 204L quando for coleção e contra Moon Shoe quando for guia dedicado. QA técnico/readback textual não basta.

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


## Gate hard — DEV-first e merge para Production

Esta regra é obrigatória para o agente LK Otimização de Coleção / LKGOC.

### Sequência única permitida

1. **DEV primeiro:** toda alteração LKGOC de Shopify theme, section, snippet, CSS, schema renderizado, collection layout, guia visual ou página visual deve ser publicada primeiro em tema DEV real.
2. **Verificação por API:** antes do write, registrar `theme_id`, `name` e `role`. Nome do tema não é evidência. O tema alvo precisa estar com `role: unpublished`.
3. **Abortar se production:** se o tema tiver `role: main`, abortar imediatamente. Não corrigir “rapidinho” em production.
4. **QA no DEV:** readback API + storefront preview com cookie/`preview_theme_id` + desktop/mobile + ausência de `Liquid error` + ausência de placeholder/comentário técnico + FAQ/schema correto + padrão visual 204L/Moon Shoe.
5. **Approval do Lucas:** enviar apenas link DEV, scorecard, riscos e rollback. Sem approval explícito atual, parar no DEV.
6. **Merge/promoção:** production recebe somente o diff aprovado do DEV, preservando linhagem **DEV → Production**. Não fazer patch solto independente em production.
7. **Exceção:** hotfix direto em production só se Lucas disser explicitamente “hotfix direto em production”, com escopo e rollback.

### Bloqueadores antes de mandar link para Lucas

Não enviar link de approval se houver:

- placeholder editorial ou texto “pendente/substituir”;
- `Liquid error`;
- comentário técnico visível;
- FAQ/schema duplicado ou desatualizado;
- guia dedicado fora do shell Moon Shoe/Jacquemus;
- coleção fora do contrato 204L/LKGOC;
- QA apenas técnico sem visual desktop/mobile;
- preview não validado no tema DEV/unpublished.

Essa seção complementa `LKGOC-PADRAO-CANONICO.md` e `rules/shopify-theme-dev-to-production-promotion-rule-20260531.md`. Se houver divergência, vence a regra mais restritiva.

## Aprendizado obrigatório — paridade 204L sem seletores frágeis

Fonte canônica complementar: `areas/lk/sub-areas/growth/rules/REGRA-LKGOC-PARIDADE-204L-SEM-SELETORES-FRAGEIS.md`.

Ao executar Full LKGOC baseado no gold source New Balance 204L, não basta clonar HTML/classes principais. Validar e preservar os overrides finais de acabamento, especialmente mobile. Evitar seletor frágil preso ao texto do `aria-label` da 204L; usar/duplicar hooks por classe estável para a coleção alvo. Antes de enviar preview, medir no mobile `.coll-banner__title` e `.lk-collection-v2__headline` contra 204L: padding, x, font-size, line-height, letter-spacing e font-family.

## Aprendizado obrigatório — guia LK canônico `lk-goc-*`

Para Guia Editorial LK dentro de collections Full LKGOC, usar contrato class-based e namespace `lk-goc-*`: `lk-goc-guide-panel`, `lk-goc-guide-grid`, `lk-goc-guide-card`, `lk-goc-guide-faq`, `lk-goc-guide-media`, `lk-goc-guide-panel__cta`. Manter aliases `lk-guide-standard-*`/`lk-lkgoc-*` apenas como compatibilidade temporária. Não criar patches por handle (`#lk-guia-[handle]`) quando a intenção for padrão reutilizável. QA obrigatório contra 204L em mobile e desktop.

## CORREÇÃO CANÔNICA LUCAS — mídia editorial, DEV write e Production proibido

Registrado em: 20260606T165914Z

- LKGOC deve sempre buscar/retirar as imagens principais dos principais veículos de moda/editoriais relevantes, como Vogue, Vogue Brasil, Highsnobiety, Hypebeast e campanhas oficiais.
- Para hero, priorizar pessoa usando/contexto editorial/lifestyle; packshot/PDP/produto isolado não é hero LKGOC.
- Todo write Shopify do LKGOC deve acontecer sempre em tema DEV/unpublished e não precisa de autorização prévia de Lucas.
- Antes de qualquer write, verificar por API que o tema tem `role: unpublished`.
- Write direto em Production/main é extremamente proibido.
- A autorização de Lucas é necessária apenas para merge/promoção para Production/main ou qualquer mudança customer-facing.
- Qualquer regra anterior que bloqueie DEV por Contract/asset/licença está obsoleta; o bloqueio é para Production, não para DEV.

## HARD LOCK — 204L Gold Source Visual Contract

Toda execução LKGOC deve tratar a coleção New Balance 204L como **Gold Source visual bloqueante**, não como referência genérica.

Antes de qualquer `PASS`:

- screenshot 204L obrigatório;
- screenshot DEV da coleção alvo obrigatório;
- comparativo lado a lado obrigatório;
- equivalência visual obrigatória em hierarquia, densidade editorial, hero, guia pós-grid, FAQ e ordem hero → grid → guia;
- QA técnico sem side-by-side 204L é automaticamente `FAIL`.

Regra fonte: `rules/REGRA-LKGOC-204L-GOLD-SOURCE-VISUAL-CONTRACT.md`.

