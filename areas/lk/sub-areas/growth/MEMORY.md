# MEMORY — LK Growth OS

## Decisões ativas

- O agente especialista deve se chamar/operar como **LK Growth OS** ou **LK Search & Conversion OS**, não apenas SEO/GMC/CRO.
- GA4/Google Analytics é componente obrigatório do escopo.
- O agente deve cobrir Search Console, Merchant Center, GA4, Shopify SEO, Shopify CRO/theme, GEO/AI Search, PageSpeed/CrUX, schema, reviews, paid/influencer signals, concorrência/SERP e Google Business/local quando aplicável.
- Credenciais/tokens do bot ficam fora do Brain; consultar fonte segura autorizada quando necessário e nunca registrar valores.

## Guardrails lembrados

- Nada de write externo sem aprovação explícita atual.
- Theme/CRO sempre primeiro em dev theme.
- Relatórios decision-grade exigem dados comerciais/analytics/search, não apenas HTML.
- Não usar estoque como critério decisivo de SEO/CRO para LK.
- Não criar copy pública diferenciando pronta entrega/encomenda/estoque.

## Aprendizado crítico — padrão visual antes de production

Regra durável obrigatória: nenhum guia editorial, bloco de coleção, CTA, FAQ ou alteração visual de collection vai para production apenas com validação técnica. O padrão visual/editorial LK e aprovação explícita atual de Lucas são obrigatórios.

Fonte completa da regra, origem do incidente, QA suficiente e rollback:

- `rules/REGRA-PRODUCTION-GUIAS-COLECOES-LK.md`
- receipt: `receipts/2026-06-01-production-guide-layout-rollback-learning.md`

## Aprendizado crítico adicional — 2026-06-01, preview P0 coleções/guias

Erro confirmado por Lucas após preview DEV das coleções/guias Nike Vomero Premium, Adidas x Bad Bunny e Adidas SL 72:

1. **Imagens de hero/collage de coleção não podem ser fotos de produto/PDP**. Devem ser fotos editoriais/reais extraídas de portais de moda/sneaker/cultura, com fonte registrada no brief. Produto pode aparecer no grid Shopify, não como imagem editorial do hero/guia.
2. **Texto de coleção nunca pode ser copy genérica**. Sempre usar `PADRAO-TEXTO-COLECAO-LK.md` + lógica Curadoria LK + camada Claude SEO/GEO antes de gerar H2/body/meta. Texto precisa definir a coleção, intenção de busca, contexto cultural/estético e curadoria humana da LK.
3. **Bloco/Guia LK não pode usar versão antiga**. Antes de montar preview, comparar contra o snapshot/padrão mais atual aprovado. Se houver dúvida entre versões, parar, abrir fonte canônica e não publicar preview errado.
4. Quando um preview visual é criticado, o agente deve automaticamente: conter/remover preview ruim, registrar aprendizado, refazer com o padrão correto e só então reapresentar. Não esperar Lucas lembrar.

## 2026-06-01 17:08:05 — Padrão de texto para coleções SEO/GEO

Lucas aprovou padrão de criação de texto para otimizações de coleções: descrição principal robusta em 3 parágrafos reais; primeiro parágrafo maior/forte porque fica visível antes do Ler Mais; bloco editorial/visual também deve ser expandido em coleções prioritárias (600–800 chars), com termos naturais de modelo, LK, originalidade, styling, contexto e intenção comercial. Referência canônica: `rules/PADRAO-CRIACAO-TEXTO-COLECOES-SEO-GEO-LK.md`.

## 2026-06-01 19:20:28 — Skill SUPERPOWERS Collection Optimizer

Lucas corrigiu: o padrão não é só texto; deve virar skill grande. Decisões: usar tag + metafields + ledger local; tag verbal `LK Growth Optimized Collection` (tag confirmada como LK Growth Optimized Collection); toda coleção otimizada obrigatoriamente tem guia dedicado `/pages/guia-...`; imagens devem ser baixadas/subidas para Shopify/CDN própria quando possível; atualizações de layout/padrão em coleção otimizada devem aplicar em todas as coleções tagueadas no DEV antes de approval de produção; seção visível no guia: “Referências editoriais e contexto”; meta estratégica: otimizar principais coleções por ordem de visitas/tráfego. Skill doc: `skills/lk-superpowers-collection-optimizer/SKILL.md`; PRD: `projetos/PRD-SKILL-SUPERPOWERS-OTIMIZACAO-COLECOES-LK.md`; ledger: `ledgers/lk-optimized-collections-ledger.json`.

## 2026-06-01 19:49:18 — CLAUDE-SEO obrigatório na SUPERPOWERS

Lucas perguntou se a skill CLAUDE-SEO estava incluída como parte pensante da otimização de coleção. Não estava explícita; foi adicionada como camada obrigatória antes da copy final na skill `lk-superpowers-collection-optimizer`, no PRD, no brief-template e no QA checklist. A camada deve registrar intenção de busca, entidades, ângulos editoriais, estrutura semântica, FAQ decisório, riscos de keyword stuffing e alinhamento SEO/GEO/LLM + tom premium LK.

## 2026-06-01 19:50:47 — Regra obrigatória LK Growth Optimized Collection

Toda coleção que for otimizada/melhorada para SEO, GEO/AI Search, CRO, layout, hero, guia ou texto deve obrigatoriamente passar pelo fluxo **LK Growth Optimized Collection**, usando a skill `lk-superpowers-collection-optimizer`, camada CLAUDE-SEO, guia dedicado, Guia Editorial LK pós-grid, imagens editoriais reais, tag/metafields e ledger. Regra canônica: `rules/REGRA-LK-GROWTH-OPTIMIZED-COLLECTION-OBRIGATORIA.md`.

## 2026-06-01 19:51:55 — Regra replicada para LK Shopify

A regra **LK Growth Optimized Collection** foi replicada também para o agente/área `lk-shopify`: `lk-shopify/AGENTS.md`, `lk-shopify/MEMORY.md`, `lk-shopify/IDENTITY.md` e `lk-shopify/rules/REGRA-LK-GROWTH-OPTIMIZED-COLLECTION-OBRIGATORIA.md`.

## Aprendizado crítico — LKGOC salva padrão visual aprovado automaticamente — 2026-06-02T11:06:41Z

Feedback Lucas após Guia Adidas Samba Jane fora do padrão: o agente deve registrar no LKGOC imediatamente todo padrão visual aprovado/corrigido por Lucas. Não esperar Lucas dizer “salva como padrão”.

Padrão obrigatório atual:
- coleção product-first: New Balance 204L;
- Guia LK dedicado `/pages/guia-*`: Nike x Jacquemus Moon Shoe.

Guia dedicado em texto corrido/HTML cru/`article` simples reprova automaticamente, mesmo com conteúdo SEO correto. QA visual desktop/mobile contra Moon Shoe é gate de produção.

## Regra Telegram/preview — draft visível em Shopify DEV — 2026-06-02T12:14:03Z

Feedback Lucas: draft local sozinho não serve em fluxo por Telegram, porque Lucas não consegue ver/validar visualmente.

Regra obrigatória LKGOC:

- Todo draft visual de coleção, Guia LK, source page, CTA, FAQ ou bloco editorial deve ser materializado em **Shopify DEV theme/preview** antes de pedir opinião/aprovação.
- A resposta no Telegram deve trazer o **link direto de preview Shopify** (`preview_theme_id=155065450718` ou tema DEV ativo equivalente).
- Arquivo local/Brain é apenas backup/rollback/evidência; não é output final para Lucas validar.
- Se ainda não for possível criar preview no Shopify DEV, declarar bloqueio técnico e não apresentar como “pronto”.
- Para guia dedicado, o padrão é: rascunho → snippet/template/section no DEV theme → URL preview clicável → QA visual desktop/mobile → só então approval de produção.

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
