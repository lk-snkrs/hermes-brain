# REGRA — Production de guias e coleções LK

Atualizado em: 2026-06-01T13:32:01+00:00

## Regra absoluta

Nenhum guia editorial, bloco de collection, FAQ visual, CTA de guia ou alteração visual em coleção da LK pode ir para production sem respeitar o padrão visual/editorial aprovado pela LK.

## Origem do aprendizado

Em 2026-06-01 houve publicação de guias/collections com conteúdo tecnicamente válido, mas layout fora do padrão definido. Lucas reprovou e pediu rollback. Este arquivo existe para impedir repetição.

## Padrão obrigatório

- Usar padrão canônico LK de collection product-first.
- Usar bloco guia pós-grid canônico quando for dentro da collection.
- Usar shell editorial correto quando for página standalone.
- Referenciar visualmente padrões já aprovados, como Moon Shoe/Jacquemus e documentos canônicos locais.
- Não usar corpo cru/markdown como página final.
- Não expor FAQ legado cru ou blocos sem formatação no topo da collection.
- Não inserir CTAs soltos fora do padrão visual.

## Fluxo obrigatório antes de production

1. Criar/alterar apenas em dev theme/preview quando houver mudança visual.
2. Comparar contra referência aprovada.
3. Validar desktop e mobile visualmente.
4. Validar técnico: HTTP, title/meta, schema, links, sem duplicação de FAQ/schema.
5. Enviar preview/screenshot para Lucas.
6. Só publicar em production com aprovação explícita atual.
7. Registrar receipt, rollback e revisão D+7.

## Definição de QA suficiente

QA suficiente = técnico + visual + comercial.

Não basta:

- HTTP 200;
- title/meta certo;
- FAQPage JSON-LD presente;
- tabela presente;
- imagens presentes;
- link funcionando.

Também é obrigatório conferir:

- layout igual ao padrão LK;
- hierarquia produto-first;
- bloco pós-grid no padrão;
- shell editorial premium;
- mobile/desktop sem quebra;
- copy e CTA com tom LK;
- Lucas aprovou visualmente antes de production.

## Rollback

Se production ficar fora do padrão, executar rollback primeiro. Só depois refazer em dev/preview.

## Aprendizado crítico adicional — 2026-06-01, preview P0 coleções/guias

Erro confirmado por Lucas após preview DEV das coleções/guias Nike Vomero Premium, Adidas x Bad Bunny e Adidas SL 72:

1. **Imagens de hero/collage de coleção não podem ser fotos de produto/PDP**. Devem ser fotos editoriais/reais extraídas de portais de moda/sneaker/cultura, com fonte registrada no brief. Produto pode aparecer no grid Shopify, não como imagem editorial do hero/guia.
2. **Texto de coleção nunca pode ser copy genérica**. Sempre usar `PADRAO-TEXTO-COLECAO-LK.md` + lógica Curadoria LK + camada Claude SEO/GEO antes de gerar H2/body/meta. Texto precisa definir a coleção, intenção de busca, contexto cultural/estético e curadoria humana da LK.
3. **Bloco/Guia LK não pode usar versão antiga**. Antes de montar preview, comparar contra o snapshot/padrão mais atual aprovado. Se houver dúvida entre versões, parar, abrir fonte canônica e não publicar preview errado.
4. Quando um preview visual é criticado, o agente deve automaticamente: conter/remover preview ruim, registrar aprendizado, refazer com o padrão correto e só então reapresentar. Não esperar Lucas lembrar.
- 2026-06-01: Bloco `Guia editorial LK` pós-grid deve ter respiro visual obrigatório após o último produto; no mobile, mínimo de ~48px antes do painel para não parecer colado no grid.
- 2026-06-01: Para guias/coleções LK, “imagem de portal de moda” não é suficiente se for packshot/release/isolada. A imagem editorial válida deve mostrar pessoa usando, campanha com styling, ambiente/atelier/ativação ou contexto cultural real; produto isolado continua proibido mesmo quando hospedado em Hypebeast/Highsnobiety/Nike/Marie Claire.
- 2026-06-01: Ao replicar padrão aprovado de coleção/guia (ex. 204L), copiar o contrato funcional completo: layout, CSS, JS, modal de imagem, comportamento de “ler mais”, QA de clique e mobile. Não basta clonar aparência/HTML; se imagens não abrem, o preview é reprovado.

## 2026-06-01 19:50:47 — Regra obrigatória LK Growth Optimized Collection

Toda coleção que for otimizada/melhorada para SEO, GEO/AI Search, CRO, layout, hero, guia ou texto deve obrigatoriamente passar pelo fluxo **LK Growth Optimized Collection**, usando a skill `lk-superpowers-collection-optimizer`, camada CLAUDE-SEO, guia dedicado, Guia Editorial LK pós-grid, imagens editoriais reais, tag/metafields e ledger. Regra canônica: `rules/REGRA-LK-GROWTH-OPTIMIZED-COLLECTION-OBRIGATORIA.md`.

## Aprendizado crítico adicional — 2026-06-02, Guia Adidas Samba Jane aprovado

Lucas aprovou o refinamento visual do Guia Adidas Samba Jane em DEV como padrão LKGOC para guias dedicados:

- Guia dedicado deve usar shell Moon Shoe com hero preto/full-bleed; não publicar hero branco ou artigo estreito.
- Imagem editorial precisa mostrar o tênis de verdade. Pessoa usando não basta se calça/ângulo/corte esconderem o calçado. Bloquear e trocar imagem.
- Fonte aspiracional continua importante, mas visibilidade do produto é gate visual. Se Vogue/Glamour não mostrarem o tênis, usar outra fonte editorial de styling com justificativa.
- Texto abaixo do hero deve manter a mesma régua/largura útil do hero preto. Não permitir regressão para coluna estreita do `main-page`.
- FAQ desktop deve ser visualmente equilibrado: até 4 perguntas = 1 coluna; mais de 4 = 6 ou 8 perguntas em 2 colunas; mobile = 1 coluna.
- Approval de Lucas em preview DEV não autoriza production automaticamente fora do escopo pedido; production continua exigindo aprovação explícita atual.

## Referência LKGOC

O padrão completo de LKGOC vive em um único documento canônico:

- `LKGOC-PADRAO-CANONICO.md`

Não duplicar regras longas aqui. Este arquivo deve apenas complementar seu escopo específico e apontar para o canônico.
