# LKGOC — Padrão Canônico de Guia + Coleção LK

Atualizado em: 2026-06-02 — reforço Lucas: coleção gold source é `/collections/new-balance-204l?_pos=1&_psq=204l&_ss=e&_v=1.0`

Este é o **documento único de verdade** para LKGOC — LK Growth Optimized Collection.

Qualquer regra sobre criação, correção, publicação, QA ou manutenção de Guia + Coleção LKGOC deve morar aqui. Outros documentos podem apontar para este arquivo, mas não devem duplicar o conteúdo completo.

## 0.0 Sistema operacional LKGOC

Este canônico é a lei. Os arquivos abaixo são o playbook executável e devem ser usados conforme o caso:

- `LKGOC-PRD.md` — objetivo estratégico, níveis Full/Lite/Correção/Não-LKGOC e critérios de sucesso.
- `LKGOC-INPUT-CONTRACT.md` — dados mínimos antes de começar.
- `LKGOC-EVIDENCE-PACKET.md` — formato obrigatório para registrar pesquisa, GSC, DataForSEO, Ahrefs e Shopify/read-only.
- `LKGOC-EXECUTION-WORKFLOW.md` — fluxo DEV → approval → production → impact review.
- `LKGOC-SCORECARD-100.md` — rubrica 0–100; meta de approval >=85.
- `LKGOC-IMPACT-REVIEW.md` — medição D+7/D+14/D+30.
- `templates/lkgoc-copy-template.md` — contratos de copy para coleção, guia pós-grid e guia dedicado.
- `templates/lkgoc-liquid-contract.md` — contrato visual/Liquid/Shopify.
- `references/lkgoc-good-bad-examples.md` — exemplos bons/ruins para evitar drift.

## 0.1 Objetivo estratégico

LKGOC existe para transformar uma intenção/modelo prioritário em uma experiência LK completa: coleção produto-first que vende, guia editorial citável, SEO/GEO orientado por dados, visual premium, preview Shopify DEV, QA visual e aprendizado pós-lançamento.

Não é apenas texto, FAQ, blog, landing page ou ajuste de SEO. É um sistema auditável de entrada → evidência → escrita Claude SEO → visual 204L/Moon Shoe → preview → score → approval → produção → impacto.

## 0.2 Níveis de execução

- **Full:** obrigatório para coleções estratégicas; exige todos os artefatos, dados disponíveis, guia dedicado, DEV preview, QA e score.
- **Lite:** permitido para coleção menor; mantém pesquisa web, produto-first e Claude SEO, mas pode dispensar Ahrefs/guia longo com justificativa.
- **Correção:** usado para alinhar coleção/guia existente ao canônico, com antes/depois e QA visual.
- **Não-LKGOC:** coleção simples; não chamar de LKGOC.

## 0.3 Camada rewrite-from-zero — regra Lucas

Quando Lucas pedir para **otimizar uma coleção usando LKGOC**, o agente deve tratar qualquer material existente como **insumo/evidência**, não como base a ser remendada.

Regra operacional:

1. Auditar o que existe hoje apenas para mapear produtos, handles, gaps, riscos, SEO atual e screenshots antes/depois.
2. Reescrever do zero a experiência LKGOC: copy da coleção, guia pós-grid, FAQ/schema, guia dedicado e contrato visual, usando pesquisa/evidence packet + Claude SEO + templates LKGOC.
3. Reaplicar todo o sistema LKGOC completo, mesmo que já exista uma versão parcial, antiga ou “quase boa”.
4. Só preservar trechos/blocos existentes quando forem explicitamente compatíveis com o canônico **e** passarem no scorecard; caso contrário, substituir.
5. Se a coleção existente estiver fora do padrão 204L/Moon Shoe, classificar como **drift LKGOC** e refazer em vez de fazer patch incremental.

Frase-gatilho equivalente: “otimizar coleção com LKGOC” = **refactor/rewrite completo LKGOC**, não polish.


## 0.4 Gate DEV-first / merge para production — regra obrigatória Lucas

Toda alteração LKGOC que envolva Shopify theme, collection layout, guia visual, snippet, section, CSS, schema renderizado ou página visual deve seguir obrigatoriamente a sequência:

1. **Descoberta e verificação do tema alvo:** antes de qualquer write, listar/ler o tema Shopify por API e registrar `theme_id`, `name` e principalmente `role`.
2. **DEV real obrigatório:** publicar/aplicar primeiro em tema **DEV/unpublished**. Nome do tema não basta. Se o `role` for `main`, abortar imediatamente.
3. **QA no DEV:** executar readback API, storefront preview com cookie/`preview_theme_id`, QA desktop e mobile, screenshot/render quando disponível, validação de Liquid errors, placeholders, FAQ/schema, links, CTA e scorecard LKGOC.
4. **Approval de Lucas:** entregar link DEV e pacote de aprovação. Sem aprovação explícita no turno atual, parar no DEV.
5. **Merge/promoção para production:** production só recebe o diff aprovado do DEV, preservando linhagem **DEV → Production**. Não fazer patch independente em production.
6. **Receipt e rollback:** registrar before/after, diff/sha, readback, storefront público, rollback e revisão de impacto.

Bloqueadores automáticos:

- Tema com nome “dev”, “preview” ou similar mas `role: main` = **produção**; abortar write.
- Link enviado para Lucas sem QA visual mínimo no DEV = falha de governança.
- Placeholder editorial, comentário técnico, bloco “pendente”, `Liquid error`, FAQ/schema duplicado ou guia fora do padrão 204L/Moon Shoe = não pode ir para approval.
- Production write direto só é permitido se Lucas disser explicitamente “hotfix direto em production”, nomeando a exceção e o escopo.

Esta regra complementa e reforça `rules/shopify-theme-dev-to-production-promotion-rule-20260531.md`; se houver divergência, a regra mais restritiva vence.

## 0. Gates executivos obrigatórios — não negociar

Se o agente LK Growth não cumprir qualquer item abaixo, a entrega deve ser tratada como **drift LKGOC** e não pode ser apresentada como coleção otimizada:

1. **Fonte única:** abrir este arquivo (`LKGOC-PADRAO-CANONICO.md`) antes dos documentos auxiliares. Se outro documento divergir, este vence.
2. **Nome correto:** LKGOC = **LK Growth Optimized Collection**; nunca “Organic”.
3. **Padrão visual da coleção:** copiar o contrato da New Balance 204L, incluindo hero/topo escuro/preto quando o padrão LKGOC visual for aplicado, produto-first, grid antes do guia longo e Guia Editorial LK pós-grid.
4. **Padrão visual do guia dedicado:** copiar o shell editorial Nike x Jacquemus Moon Shoe; texto corrido, artigo cru, hero branco ou `main-page` estreito reprovam automaticamente.
5. **Coleção + guia juntos:** não considerar a coleção pronta se o guia dedicado correspondente não estiver planejado, escrito e pronto para preview/approval.
6. **Pesquisa na internet antes de escrever:** SERP + fontes oficiais + fontes editoriais internacionais/reconhecíveis devem alimentar narrativa, SEO/GEO, fontes externas e FAQ. A pesquisa precisa cobrir todas as informações úteis do produto/coleção: nome/modelo, marca, colorway/collab, história, lançamento, materiais/silhueta, styling, tendência, intenção de busca, concorrência e dúvidas reais do comprador.
7. **Stack de dados SEO obrigatório quando disponível:** usar Google Search Console como fonte de verdade para demanda real da LK (queries, impressões, CTR, posição e páginas similares); usar DataForSEO para SERP/keyword/volume/intenção/concorrentes/People Also Ask/AI visibility; usar Ahrefs como camada complementar para concorrência, backlinks, autoridade e gap de conteúdo. Se algum conector não estiver disponível, declarar a limitação no approval packet e não inventar dado.
8. **Claude SEO obrigatório para texto:** depois da pesquisa factual, rodar camada Claude SEO/GEO usando as skills instaladas da família Claude SEO (`seo-content`, `seo-ecommerce`, `seo-page`, `seo-geo` e `seo-dataforseo` quando houver SERP/dados), mapeadas do upstream `AgriciDaniel/claude-seo`, para refinar entidade, E-E-A-T, SEO de coleção/ecommerce, AI readability/GEO, title/meta, FAQ e evitar copy genérica.
9. **Texto hero robusto:** primeiro bloco/parágrafo principal deve ter **500–700 caracteres**, salvo exceção registrada; regras antigas de 350–450 caracteres estão obsoletas para LKGOC.
   - Métrica operacional: contar o **texto editorial principal do hero/bloco de abertura que alimenta o read-more**, não snippets de botão, breadcrumbs, FAQ ou schema. Se o gold source 204L ou uma coleção aprovada tiver texto expandido acima da faixa por decisão visual/comercial, registrar como exceção no scorecard/approval. Textos abaixo de 500 chars em LKGOC Full reprovam salvo exceção explícita.
10. **FAQ único:** apenas um FAQ visível/canônico por experiência LKGOC, dentro do Guia LK/bloco guia; schema `FAQPage` deve refletir somente esse FAQ.
11. **CTA do guia:** card/faixa “Para aprofundar...” em fundo claro igual aos cards internos do Guia LK; botão `ABRIR GUIA COMPLETO` em fundo escuro com texto branco, também no mobile.
12. **Preview Shopify DEV obrigatório:** draft local/Brain não é output final para Lucas validar. Todo draft visual deve ir para Shopify DEV/preview e a resposta deve trazer link direto com `preview_theme_id` quando aplicável.
13. **QA visual desktop + mobile:** readback de código, HTTP 200, title/meta ou HTML não bastam; precisa screenshot/render comparado à 204L e Moon Shoe.
14. **Production só com aprovação explícita atual:** com rollback, diff/readback, receipt e pendência de cache documentada quando houver.

## 1. Definição

LKGOC é o pacote otimizado completo de uma intenção/modelo prioritário:

- **Coleção produto-first** no padrão comercial/visual aprovado da LK.
- **Guia LK dedicado** no padrão editorial aprovado da LK.
- SEO, GEO/AI Search, CRO, pesquisa SERP e QA visual fechados juntos.

Nunca tratar como apenas texto de coleção, FAQ solto ou guia genérico.

## 2. Entrega obrigatória em par

Toda entrega LKGOC deve nascer ou ser corrigida como par:

- **Coleção:** referência visual/comercial principal = **New Balance 204L**.
- **Guia dedicado:** referência editorial principal = **Nike Moon Shoe**.

Se houver exceção, ela precisa estar justificada no approval packet.

## 3. Padrão da coleção — referência 204L

**Gold source correto e obrigatório indicado por Lucas:**

- URL pública: `https://lksneakers.com.br/collections/new-balance-204l?_pos=1&_psq=204l&_ss=e&_v=1.0`
- Handle: `/collections/new-balance-204l`
- Toda coleção LKGOC nova ou refeita deve copiar este padrão como contrato, não como inspiração.
- Se uma coleção sair com layout/copy/FAQ fora dessa estrutura, considerar drift e refazer do zero.

Estrutura pública observada no gold source 204L:

- topo com `Curadoria LK`;
- H2 curto, comercial e fashion: exemplo `Perfil baixo, leitura fashion.`;
- parágrafo único de orientação premium antes do grid, sem virar blog;
- grid/contagem/ordenação como centro da página;
- guia editorial LK **depois** do grid, com H2, introdução, H3 de escolha, bullets fortes e FAQ com pergunta + resposta;
- CTA final discreto para guia completo quando aplicável;
- tom de curadoria, autenticidade e atendimento humano, sem expor pronta entrega/encomenda/estoque como taxonomia pública.

A coleção deve ser produto-first, premium e comercial:

- manter grid de produtos e caminho de compra como centro;
- ter topo/hero premium quando o modelo exigir LKGOC visual;
- usar contexto editorial visual sem transformar coleção em blog;
- evitar layout default branco quando já existir padrão LKGOC aprovado para aquele modelo;
- trust strip, filtros ou sidebar não podem dominar o primeiro impacto visual se o padrão aprovado for hero editorial/produto-first;
- blocos específicos devem ser condicionados por `collection.handle`.

Exemplo de classe/bloco por modelo:

- `lk-samba-jane-coll-preview` para Adidas Samba Jane;
- equivalentes próprios para outros modelos.

## 4. Padrão do guia — referência Moon Shoe

O guia é editorial, educacional e citável:

- hero forte, visual premium e régua consistente;
- quando aplicável, fundo escuro `#101010` e texto branco no padrão aprovado;
- imagem editorial com pessoa usando o tênis e o calçado visível;
- seções abaixo do hero alinhadas à mesma régua visual, sem coluna estreita;
- blocos citáveis, FAQ e schema quando aplicável;
- tom LK: curadoria exclusiva, autenticidade, atendimento humano e confirmação via chat quando necessário.

## 5. Pesquisa obrigatória antes de escrever/publicar

Antes de escrever, corrigir ou publicar:

- pesquisar internet/SERP;
- cruzar fontes editoriais, história do modelo, relevância atual, styling e curadoria LK;
- checar concorrência/SERP e intenção de busca;
- consultar **Google Search Console** quando houver URL, coleção similar ou consulta relacionada: usar queries, impressões, CTR, posição média e páginas similares como fonte de verdade da demanda real da LK;
- consultar **DataForSEO** para SERP live, volume, intenção, concorrentes, perguntas, páginas citáveis e AI visibility/LLM mentions quando a coleção for LKGOC prioritária;
- consultar **Ahrefs** quando disponível para backlinks, autoridade, concorrentes fortes e gap de conteúdo/off-page;
- se GSC/DataForSEO/Ahrefs não estiverem disponíveis, registrar a limitação e não inventar dado;
- separar fato, interpretação e recomendação.

Fontes editoriais preferenciais quando aplicável:

- Vogue;
- GQ;
- ELLE;
- Glamour;
- The Mom Edit;
- outras fontes fortes e atuais, se fizerem sentido.

## 6. SEO/GEO/AI Search

Toda entrega LKGOC deve considerar:

- title/meta/H1 coerentes;
- copy citável e não genérica;
- FAQ estruturado;
- `FAQPage`/schema quando aplicável;
- legibilidade para ChatGPT, Perplexity, Gemini e AI Overviews;
- higiene de source: sem markers/comentários DEV em production.

FAQ visual:

- até 4 perguntas: 1 coluna;
- mais de 4 perguntas: 2 colunas equilibradas.

## 7. Guardrails de linguagem LK

Evitar no texto editorial público:

- pronta entrega;
- encomenda;
- estoque como taxonomia/comunicação principal;
- prazo/envio como promessa editorial.

Preferir:

- curadoria exclusiva;
- autenticidade;
- atendimento humano;
- confirmação via chat quando necessário.

## 8. Implementação Shopify segura

- Writes em production exigem aprovação explícita atual de Lucas.
- Alterações visuais devem ir primeiro para DEV/preview quando possível.
- Sempre salvar rollback, diff, readback e receipt.
- Se `sections/*.liquid` estiver perto do limite Shopify de 256 KB, **não inflar a section global**.
- Nesses casos, usar snippet dedicado + `render` condicionado por handle.
- Não mexer em produto, preço, estoque, checkout, GMC, Klaviyo, campanhas ou PDP global sem aprovação específica.

## 9. Audit final obrigatório — screenshot

Toda alteração visual/layout precisa de screenshot final.

Não considerar concluído apenas com:

- readback de código;
- readback Admin;
- HTML público sem verificação visual.

Obrigatório:

- tirar print da página renderizada;
- comparar visualmente contra a referência aprovada;
- salvar screenshot no receipt;
- enviar/registrar evidência final.

Se a URL limpa pública estiver presa em `page_cache` da Shopify:

- tirar screenshot do render/preview/section atualizado;
- registrar evidência da URL limpa ainda em cache;
- marcar explicitamente: **código/readback OK, URL limpa pendente de cache**.

## 10. Definition of Done LKGOC

Uma entrega LKGOC só fecha quando houver:

- nível declarado: Full / Lite / Correção / Não-LKGOC;
- input contract preenchido ou lacunas declaradas;
- evidence packet preenchido, com dados reais ou limitações explícitas;
- pesquisa feita e registrada;
- coleção no padrão 204L ou justificativa aprovada;
- Guia LK no padrão Moon Shoe ou justificativa aprovada;
- SEO/GEO/schema/FAQ revisados via Claude SEO;
- score LKGOC 0–100 calculado; meta de approval >=85;
- preview ou section render validado;
- screenshot/audit visual desktop + mobile salvo;
- rollback e receipt salvos;
- cache público verificado ou pendência documentada;
- plano de impact review D+7/D+14/D+30 quando houver produção.

## 11. Ponteiros permitidos

Outros documentos do Brain podem conter apenas um resumo curto e link para este arquivo. Não duplicar este padrão completo fora daqui.

## Regra operacional — LKGOC como contexto obrigatório para tema Shopify

Registrado em: 20260603T152400Z

Sempre que Lucas falar sobre **LKGOC** e/ou sobre **tema Shopify** dentro deste profile, o agente deve tratar o assunto como execução pelo **LKGOC / LK Growth Optimized Collections**, não como edição genérica de tema.

Implicações obrigatórias:
- carregar e aplicar o padrão canônico do LKGOC antes de diagnosticar ou propor mudança;
- usar o fluxo DEV-first: tema Shopify com `role: unpublished` verificado por API;
- nunca tratar tema production como área de teste;
- qualquer preview, QA, approval packet, rollback ou merge deve ser descrito e executado no vocabulário/processo LKGOC;
- se a conversa envolver coleção, guia, collection template, metafields, FAQ/schema, blocos editoriais ou Liquid de coleção, assumir LKGOC por padrão;
- se houver ambiguidade, perguntar apenas o mínimo necessário, mas manter o LKGOC como default operacional.

## Regra operacional — LKGOC não inventa tema novo

Registrado em: 20260603T152525Z

O LKGOC **não deve inventar um tema, layout ou padrão visual novo**. Toda execução deve **copiar e adaptar o padrão definido/aprovado** para otimização de collections da LK.

Implicações obrigatórias:
- usar o padrão canônico LKGOC como fonte de verdade;
- replicar estrutura, hierarquia, blocos, densidade editorial, tom premium e comportamento visual já definidos;
- adaptar apenas conteúdo, links, produtos, FAQ e nuances comerciais da coleção alvo;
- não criar novo design system, nova arquitetura de seção, novo bloco visual ou novo comportamento sem aprovação explícita de Lucas;
- se faltar referência do padrão aprovado, parar e localizar a referência antes de propor execução;
- qualquer variação deve ser marcada como exceção e ir para approval antes de implementação.

## Regra operacional — namespace CSS LKGOC

Registrado em: 20260603T153717Z

O namespace preferencial novo para o LK Growth Optimized Collections é `lk-goc-*`.

Implicações:
- novas classes estruturais do LKGOC devem usar `lk-goc-*`;
- durante transição, manter compatibilidade quando necessário com aliases antigos `lk-lkgoc-*` e `lk-204l-*`;
- 204L continua sendo padrão-base/gold source visual, mas não deve obrigar novos blocos a dependerem somente de `lk-204l-*`;
- em tema Shopify, qualquer mudança segue DEV/unpublished → QA → approval Lucas → merge para Production.

## Standard v1 — `lk-goc-*`

Registrado em: 20260603T162846Z

O padrão canônico reutilizável do LKGOC está documentado em:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-STANDARD-V1-LK-GOC.md`

A coleção New Balance 204L e o guia New Balance 204L são a gold source inicial.

Mudanças futuras aprovadas em uma implementação LKGOC devem ser avaliadas como evolução do Standard LK-GOC, para propagação controlada em outros temas/collections otimizados.

## Regra operacional — LK-GOC sem legado `lk-204l-*`

Registrado em: 20260603T163131Z

Para o padrão novo LKGOC, usar apenas `lk-goc-*` nas áreas/componentes migrados.

- `lk-204l-*` não é mais alias padrão.
- `lk-lkgoc-*` permanece obsoleto/transitório.
- 204L continua sendo gold source visual/editorial, mas não como namespace CSS.
- Migração deve ocorrer em DEV/unpublished, com readback, preview QA e aprovação antes de Production.

## Regra operacional — tema alvo oficial LKGOC

Registrado em: 20260603T164243Z

Tema correto/alvo informado por Lucas: `155065450718` (`lk-new-theme/dev`).

- Tratar este tema como fonte correta do LKGOC.
- Esquecer/desconsiderar outros temas como alvo oficial, salvo nova instrução explícita.
- Como o role verificado é `main`, não escrever direto sem aprovação explícita de produção.
- Para execução segura, criar/usar cópia `unpublished` derivada deste tema antes de aplicar mudanças.

## Regra operacional — destino DEV obrigatório

Registrado em: 20260603T170929Z

Lucas reforçou que o LKGOC deve **sempre alterar o tema DEV**.

- Não usar tema sandbox/alternativo como destino oficial sem instrução explícita.
- Se o tema indicado como DEV aparecer com `role: main` na Shopify API, registrar conflito e pedir/obter confirmação explícita antes de qualquer write.
- O objetivo operacional permanece: DEV correto → QA → approval → Production.



## Guardrail obrigatório — remover FAQ/descrição legado `coll-rich-content`

Registrado em: 2026-06-05T17:42:57

Para qualquer coleção otimizada com LKGOC, o bloco legado `.coll-rich-content` — especialmente a seção antiga de **Perguntas frequentes** — deve ser removido/ocultado no escopo da coleção otimizada. QA obrigatório: não pode haver `.coll-rich-content` visível nem FAQ antigo duplicado depois do LKGOC.

Fonte: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/rules/REGRA-LKGOC-REMOVER-COLL-RICH-CONTENT-LEGADO.md`
