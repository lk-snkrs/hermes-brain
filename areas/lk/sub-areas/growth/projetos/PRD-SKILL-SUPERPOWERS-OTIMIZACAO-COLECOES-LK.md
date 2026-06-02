# PRD — Skill SUPERPOWERS para otimização de coleções LK

Versão: 0.1 — draft para validação de Lucas  
Criado em: 2026-06-01 17:39:35  
Área: LK Growth / Shopify SEO / GEO / CRO / Guias editoriais  
Status: **RASCUNHO — aguardando respostas de Lucas antes de virar skill operacional**

## 1. Problema

Os padrões de otimização de coleção da LK foram criados em várias frentes — 204L, Moon Shoe/Jacquemus, guias editoriais, bloco pós-grid, textos SEO/GEO, regras de produção e aprendizados de rollback. Hoje eles existem, mas ainda estão espalhados em documentos e receipts.

Isso gera risco de:

- criar apenas um texto quando a otimização exige coleção + guia + layout + links + tags;
- usar padrão visual antigo;
- esquecer guia pós-grid;
- esquecer página guia dedicada;
- alterar uma coleção otimizada e deixar outras fora de paridade;
- publicar sem tag/ledger que identifique quais coleções pertencem ao padrão otimizado;
- repetir erros de imagem, copy, modal, mobile e “Ler mais”.

## 2. Objetivo da Skill SUPERPOWERS

Criar uma skill operacional grande, chamada provisoriamente **SUPERPOWERS — Otimização de Coleções LK**, que execute um fluxo completo e obrigatório para cada coleção otimizada.

A skill deve transformar uma coleção comum em uma coleção otimizada LK, sempre com:

1. **Coleção Shopify otimizada**;
2. **Guia LK dedicado sobre a coleção/produto**;
3. **Bloco Guia Editorial LK pós-grid**;
4. **Layout/hero/collage no padrão aprovado**;
5. **Imagens reais/editoriais de portais de moda/sneakers/cultura**;
6. **Texto SEO/GEO/LLM completo**;
7. **Fontes externas linkadas**;
8. **Tag/metadado de identificação para futuras atualizações em lote**;
9. **Preview DEV, QA, approval packet e rollback**.

## 3. Fontes canônicas já estudadas

A skill deve carregar/seguir estes documentos antes de operar:

- `PADRAO-CANONICO-GUIA-E-COLECAO-LK.md`
- `PADRAO-GUIAS-EDITORIAIS-LK.md`
- `PADRAO-LK-COLLECTION-V2.md`
- `PADRAO-TEXTO-COLECAO-LK.md`
- `rules/PADRAO-CRIACAO-TEXTO-COLECOES-SEO-GEO-LK.md`
- `PADRAO-CANONICO-BLOCO-GUIA-POS-GRID-COLECOES-LK.md`
- `rules/REGRA-PRODUCTION-GUIAS-COLECOES-LK.md`
- `references/collection-204l-gold-source-final/`
- `references/moon-shoe-jacquemus-canonical-guide-pattern.html`

## 4. Escopo obrigatório de cada otimização de coleção

### 4.1 Dentro da página de coleção

Cada coleção otimizada deve incluir:

#### A) Texto de descrição reescrito

Usar obrigatoriamente o padrão:

- `rules/PADRAO-CRIACAO-TEXTO-COLECOES-SEO-GEO-LK.md`
- e o complemento `PADRAO-TEXTO-COLECAO-LK.md`.

Regras operacionais:

- descrição principal em 3 parágrafos reais (`<p>`);
- primeiro parágrafo maior/forte porque fica visível antes do “Ler mais”;
- texto pensado em SEO, GEO, LLM e conversão;
- sem keyword stuffing;
- sem termos operacionais proibidos.

#### B) Layout refeito no padrão LK atual

Usar o padrão `lk-collection-v2`, baseado na 204L gold source:

- hero/header produto-first;
- collage/editorial à direita no desktop;
- mobile com reveal/“Ler mais” funcional;
- grid de produto preservado antes do guia;
- espaçamento pós-grid antes do guia;
- CSS + JS + modal de imagem + comportamento mobile, não só HTML.

#### C) Fotos reais/editoriais

As imagens do hero/collage e guia devem vir de:

- portais de moda;
- portais de sneakers;
- campanhas reais;
- street style;
- editoriais;
- ativações/eventos;
- contexto cultural com pessoa usando, styling ou ambiente real.

Proibido:

- packshot/PDP;
- imagem de produto isolado;
- release sem contexto real;
- imagem em portal de moda que ainda seja só produto isolado.

#### D) Hero atualizado

Cada coleção otimizada precisa ter hero atualizado, com:

- título/H1 correto;
- subtítulo/kicker curto;
- descrição principal rica;
- bloco visual/editorial coerente;
- imagens fontes registradas no brief.

#### E) Guia Editorial LK pós-grid

Após o grid, inserir/atualizar:

- bloco `GUIA EDITORIAL LK`;
- card padrão atual;
- FAQ à direita no desktop;
- CTA para guia completo quando o guia dedicado existir;
- `FAQPage` único quando aplicável;
- espaçamento mínimo antes do painel.

### 4.2 Guia dedicado sobre a coleção/produto

Toda coleção otimizada estratégica deve ter guia dedicado, salvo exceção registrada.

O guia deve conter:

- layout correto no padrão Moon Shoe/Jacquemus;
- hero editorial;
- fotos reais/editoriais;
- texto completo para SEO/GEO/LLM;
- blocos citáveis para IA;
- tabela/estrutura de escolha quando fizer sentido;
- FAQ;
- CTA para coleção;
- links para principais publicações dos principais veículos de moda/sneaker/cultura;
- schema compatível quando aplicável.

### 4.3 Links para publicações externas

O guia dedicado deve listar/usar fontes como:

- Hypebeast;
- Highsnobiety;
- Hypebae;
- Vogue/GQ/Elle/Marie Claire quando relevante;
- Sneaker News/Complex/Sole Retriever/Footwear News quando relevante;
- página oficial da marca/campanha quando útil;
- fontes culturais ou de moda específicas da collab.

Regra: a fonte precisa agregar contexto, imagem, campanha, história, release cultural ou validação editorial. Não basta linkar qualquer notícia fraca.

## 5. Tag/metadado obrigatório para governança

Toda coleção otimizada deve receber um marcador para futuras atualizações em lote.

### Proposta de marcador

Usar uma combinação de:

1. **Tag Shopify visível apenas internamente**:
   - `lk_growth_optimized_collection`
   - `lk_collection_v2`
   - `lk_superpowers_collection`

2. **Metafields recomendados**:
   - namespace: `lk_growth`
   - key: `optimized_collection`
   - value: `true`
   - key: `optimization_version`
   - value: `superpowers_v1`
   - key: `guide_page_handle`
   - value: `guia-[handle]`
   - key: `optimized_at`
   - value: ISO date

3. **Ledger local no Brain**:
   - arquivo: `ledgers/lk-optimized-collections-ledger.json`
   - campos: handle, collection_id, guide_page_id, theme_blocks, status, version, last_qa, rollback_files, external_sources.

### Regra obrigatória para updates futuros

Quando Lucas pedir:

> “atualizar o layout de uma coleção otimizada”

A skill deve:

1. consultar tags/metafields/ledger;
2. identificar todas as coleções otimizadas;
3. aplicar a atualização em todas, ou apresentar lista de afetadas para aprovação;
4. nunca atualizar uma única se a mudança pertence ao contrato global do padrão;
5. gerar QA comparativo em lote.

## 5.1 Camada CLAUDE-SEO obrigatória

Antes da copy final, a skill deve executar uma camada pensante chamada **CLAUDE-SEO**.

Essa camada não é apenas escrever texto. Ela organiza:

- intenção de busca;
- entidades principais e secundárias;
- oportunidades de GEO/LLM;
- estrutura semântica da coleção;
- ângulos editoriais;
- perguntas reais de FAQ;
- relação entre coleção, guia dedicado e referências externas;
- equilíbrio entre SEO e tom premium LK.

A saída CLAUDE-SEO deve orientar a descrição principal, o primeiro parágrafo, o bloco editorial, o guia pós-grid, o guia dedicado, a seção de referências e o FAQ.

## 6. Fluxo operacional da skill

### Fase 0 — Descoberta

- Receber handle(s) da coleção.
- Ler coleção atual, produtos, descrição, imagens, SEO fields e tema.
- Ler GSC/GA4/GMC quando disponível para priorização; se indisponível, marcar como não decision-grade.
- Identificar se já é otimizada via tag/metafield/ledger.

### Fase 1 — Pesquisa editorial e SERP

- Pesquisar fontes externas.
- Selecionar imagens editoriais válidas.
- Registrar URLs, créditos/contexto e motivo de uso.
- Mapear queries, PAA e concorrentes.

### Fase 2 — Brief

Criar brief com:

- intenção de busca;
- público/uso;
- termos principais e secundários;
- fontes externas;
- imagens candidatas;
- estrutura de coleção;
- estrutura do guia;
- riscos/limitações.

### Fase 3 — Copy

Gerar:

- descrição principal da coleção;
- primeiro parágrafo forte;
- parágrafos escondidos pelo “Ler mais”;
- bloco editorial/visual;
- bloco pós-grid;
- FAQ;
- guia dedicado completo;
- meta title/description se aprovado para alteração.

### Fase 4 — Layout DEV

- Aplicar no Dev Theme primeiro.
- Usar padrão 204L para coleção.
- Usar padrão Moon Shoe/Jacquemus para guia dedicado/local preview.
- CTAs em dev podem apontar para âncora se página pública ainda não existir.
- Não criar Shopify Pages públicas sem aprovação explícita.

### Fase 5 — QA

Obrigatório validar:

- HTML estrutural;
- render/link básico;
- descrição em `<p>` reais;
- “Ler mais”;
- modal de imagem;
- imagens não são PDP/packshot;
- guia pós-grid não colado no grid;
- `FAQPage` único;
- mobile/desktop quando ferramenta permitir;
- ausência de termos proibidos;
- rollback pronto.

### Fase 6 — Approval packet

Antes de produção, entregar:

- escopo;
- handles afetados;
- URLs DEV;
- imagens/fontes;
- textos alterados;
- tags/metafields propostos;
- riscos;
- rollback;
- checklist QA;
- aprovação necessária.

### Fase 7 — Publicação aprovada

Com aprovação explícita:

- criar/atualizar collection em produção;
- criar/atualizar guia público;
- trocar CTA de âncora para `/pages/guia-...`;
- aplicar tags/metafields;
- atualizar ledger local;
- gerar receipt;
- agendar revisão de impacto ~7 dias.

## 7. Guardrails

A skill nunca deve:

- publicar em produção sem aprovação explícita;
- criar Shopify Pages públicas sem aprovação;
- alterar price, stock, campanha, Klaviyo, WhatsApp ou GMC sem aprovação;
- usar packshot/PDP como imagem editorial;
- criar guia textual genérico sem layout Moon Shoe;
- criar coleção sem guia pós-grid quando classificada como otimizada;
- atualizar só uma coleção se a mudança for do padrão global;
- ignorar rollback/receipt.

## 8. Artefatos que a skill deve criar

Para cada otimização:

- `brief.md`
- `sources.json`
- `copy.md`
- `collection-dev-patch.md` ou payload/asset candidate
- `guide-standalone.html`
- `qa.json`
- `approval-packet.md`
- `rollback-plan.md`
- `receipt.md`
- update no `ledgers/lk-optimized-collections-ledger.json`

## 9. Nome e localização sugeridos

### Nome interno

`lk-superpowers-collection-optimizer`

### Nome humano

**SUPERPOWERS — Otimização completa de coleções LK**

### Local sugerido

Como skill do perfil LK Growth, mantendo docs canônicas no Brain:

- Skill operacional: perfil Hermes LK Growth.
- Documentação/base: `areas/lk/sub-areas/growth/skills/lk-superpowers-collection-optimizer/`
- Ledger: `areas/lk/sub-areas/growth/ledgers/lk-optimized-collections-ledger.json`

## 10. Perguntas abertas para Lucas

### A. Tag/metafield

1. Você prefere que o marcador principal seja **tag Shopify**, **metafield**, ou os dois?
2. O nome `lk_superpowers_collection` está aprovado ou prefere algo mais discreto como `lk_growth_optimized_collection`?
3. Essa tag pode ficar visível internamente na Shopify sem problema?

### B. Escopo obrigatório de guia

4. Toda coleção otimizada deve obrigatoriamente ter guia dedicado `/pages/guia-...`, ou só coleções estratégicas?
5. Se a coleção tiver baixa demanda, fazemos apenas coleção + guia pós-grid, ou ainda assim criamos guia dedicado?

### C. Imagens

6. Podemos usar imagens externas hotlinkadas de portais quando tecnicamente funcionarem, ou prefere sempre baixar/subir para assets/CDN própria da Shopify com registro de fonte?
7. Quando houver campanha oficial da marca com modelo usando, ela vale como fonte prioritária mesmo não sendo portal de moda?

### D. Atualização em lote

8. Quando você pedir uma alteração de layout em coleção otimizada, eu devo aplicar automaticamente em todas as coleções tagueadas no DEV, e só pedir aprovação para produção?
9. Quer que a resposta sempre liste “coleções afetadas” antes de eu mexer no DEV, ou posso preparar o DEV direto quando for read-only/dev?

### E. Guia dedicado

10. Os guias devem sempre ter seção “Principais publicações e fontes” visível para o cliente, ou os links podem ficar integrados no texto/cards?
11. Você quer que todo guia tenha tabela comparativa quando houver variações/modelos próximos?

### F. Publicação

12. Ao aprovar uma coleção otimizada, a aprovação inclui automaticamente criar a página guia pública e aplicar tag/metafield, ou quer aprovações separadas?
13. Devemos agendar sempre uma revisão de impacto em 7 dias para cada coleção otimizada?

## 11. Próximo passo após respostas

Depois das respostas, criar:

1. especificação final da skill;
2. checklist executável;
3. template de brief;
4. template de approval packet;
5. ledger inicial;
6. primeira versão da skill `lk-superpowers-collection-optimizer`.

## 12. Decisão pendente

Este PRD ainda não é a skill final. Ele é a base para Lucas aprovar o comportamento antes de eu transformar em skill operacional.

---

# Decisões de Lucas — 2026-06-01 19:20:28

## A. Tag/metafield/ledger

Decisão: usar **os três**.

- Tag Shopify;
- Metafields Shopify;
- Ledger local no Brain.

## B. Nome da tag

Lucas aprovou a tag verbalmente como: **LK Growth Optimized Collection**.

Normalização técnica proposta para Shopify tag:

- `LK Growth Optimized Collection`

Confirmação posterior de Lucas: usar **LK Growth Optimized Collection**.

## C. Guia dedicado obrigatório

Decisão: **toda coleção otimizada deve ter guia dedicado**.

Justificativa de Lucas:

- LK costuma ranquear bem no Google;
- guias completos geram tráfego orgânico;
- otimização de coleção sem guia dedicado fica incompleta.

Regra: nenhuma coleção pode ser considerada `SUPERPOWERS optimized` sem página guia dedicada `/pages/guia-...` ou sem um plano aprovado para publicá-la.

## D. Atualização recorrente dos guias

Nova regra adicionada:

- guias dedicados devem poder ser atualizados mensalmente quando houver novidades do modelo/categoria;
- exemplo: se adidas lança nova collab ou nova versão do Samba, o guia do Adidas Samba deve ser atualizado para manter frescor, relevância e potencial de ranking;
- criar rotina de revisão mensal dos guias das coleções otimizadas, priorizando páginas com maior tráfego orgânico/visitas.

## E. Imagens externas

Decisão: **baixar e subir para Shopify/CDN própria**, mantendo a fonte registrada.

Regra:

- não depender de hotlink em produção quando possível;
- registrar URL original, veículo, contexto, crédito quando disponível e data de captura;
- asset final deve ficar sob controle da LK/Shopify sempre que tecnicamente possível.

## F. Atualização em lote

Decisão: quando Lucas pedir alteração de layout/padrão em coleção otimizada:

1. identificar todas as coleções tagueadas/registradas;
2. aplicar direto em todas no DEV;
3. gerar QA em lote;
4. pedir aprovação para merge/publicação em produção;
5. só então publicar em produção.

## G. Referências editoriais e contexto

Decisão: a seção de fontes deve ser **visível ao cliente**.

Nome aprovado:

- **Referências editoriais e contexto**

Uso:

- dentro do guia dedicado;
- com curadoria premium;
- sem parecer bibliografia acadêmica;
- links para veículos relevantes de moda, sneaker e cultura.

## H. Approval packet único

Decisão: approval packet único está correto, desde que tudo esteja casado:

- coleção;
- guia dedicado;
- CTA entre coleção e guia;
- tag/metafield;
- imagens/assets;
- QA;
- rollback.

## I. Meta estratégica

Meta de médio prazo:

- otimizar as principais coleções por ordem de visita;
- começar pelas coleções mais visitadas;
- seguir da mais visitada para a menos visitada;
- objetivo: ter praticamente todas as principais coleções no novo padrão SUPERPOWERS.

Fonte de priorização:

- Shopify/GA4/GSC quando disponíveis;
- relatório deve marcar quando não tiver dados autenticados suficientes.

---

# Status v1 — 2026-06-01 19:34:26

Lucas respondeu as perguntas de governança e confirmou:

- tag oficial: `LK Growth Optimized Collection`;
- usar tag + metafields + ledger local;
- toda coleção otimizada exige guia dedicado;
- imagens devem ser baixadas/subidas para Shopify/CDN própria quando possível;
- atualização de layout/padrão deve rodar em lote no DEV para todas as coleções tagueadas;
- seção visível do guia: “Referências editoriais e contexto”;
- estratégia macro: otimizar coleções por ordem de visitas/tráfego.

Este PRD agora é a base aprovada para a skill v1 local `lk-superpowers-collection-optimizer`.

## Atualização de padrão — 2026-06-01T20:43:14Z

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

