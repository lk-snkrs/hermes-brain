# Regra LKGOC — Contract Lock antes de qualquer write

Registrado em: 20260606T164407Z

## Problema que esta regra resolve
O agente errou repetidamente porque validou partes isoladas do LKGOC — código, DOM, snippets ou ordem de blocos — sem travar o contrato visual/editorial completo antes de escrever. Isso permitiu hero com packshot/PDP e guia editorial simplificado, ambos incompatíveis com LKGOC.

## Regra bloqueante
Antes de qualquer write Shopify, preview ou entrega chamada de LKGOC, criar um **LKGOC Contract Lock** para a coleção alvo. Sem Contract Lock aprovado internamente, status obrigatório = `BLOQUEADO / NÃO LKGOC`.

O Contract Lock deve conter:

1. **Gold source exato da coleção**
   - URL e snapshot do padrão aprovado, normalmente New Balance 204L.
   - Quais trechos/classes/estrutura serão copiados.
   - O que pode mudar: copy, imagens, links, produtos e dados.
   - O que não pode mudar: hierarquia visual, densidade editorial, padrão do guia, FAQ/schema e comportamento mobile/desktop.

2. **Gold source exato do guia dedicado**
   - URL/snapshot Moon Shoe/Jacquemus ou fonte canônica aprovada.
   - Comprovação de que não é `<article>` simples, texto corrido ou bloco curto.

3. **Media manifest obrigatório**
   - Hero image 1/2/3: fonte, URL, licença/status de uso, screenshot e motivo de aprovação.
   - Cada imagem deve mostrar pessoa usando o produto ou contexto editorial/lifestyle real.
   - Packshot, PDP, produto isolado ou imagem onde o tênis fica escondido = reprovar.
   - Se não houver asset seguro/aprovado: parar e pedir asset ao Lucas; não improvisar.

4. **Guide pattern manifest**
   - Estrutura do guia pós-grid e/ou guia dedicado a ser clonada.
   - FAQ: layout correto, desktop/mobile, schema único.
   - Referências editoriais: veículos globais relevantes ou status de bloqueio se não houver evidência.

5. **Acceptance tests antes de mostrar ao Lucas**
   - Readback API do asset alterado.
   - Storefront preview no DEV/unpublished.
   - Screenshot desktop/mobile comparado ao gold source.
   - Verificação visual explícita: `hero_has_person_using_product`, `hero_not_packshot`, `guide_matches_gold_source`, `faq_not_duplicated`, `grid_before_guide`, `no_liquid_error`.

## Frases proibidas sem Contract Lock + QA
- “feito”
- “pronto”
- “seguindo LKGOC”
- “full rebuild”
- “gold source aplicado”

## Status permitido se faltar qualquer gate
- `BLOQUEADO — falta asset lifestyle/on-foot aprovado`.
- `BLOQUEADO — guia gold source não localizado`.
- `NÃO LKGOC — preview técnico sem validação visual`.
- `DRAFT DEV — aguardando QA visual`.

## Execução em lote
Nunca executar lote de 5. Fazer 1 coleção, passar Contract Lock + QA visual + feedback Lucas, só então replicar.

## Re-audit hardening — write proibido sem contrato aprovado

É **proibido qualquer write** em tema Shopify, snippet, section, template, metafield ou asset LKGOC antes de existir Contract Lock aprovado para a coleção específica.

Condição mínima para sair de `BLOCKED`:
- hero lifestyle com pessoa usando/contexto editorial aprovado;
- guia editorial premium com gold source definido;
- media manifest com fonte/licença/status;
- status explícito `APPROVED_FOR_DEV_WRITE`.

Sem isso, a única ação permitida é audit/read-only/contract prep.

## Correção Lucas — DEV write liberado; Contract Lock trava Production

Registrado em: 20260606T165719Z

Correção operacional definida por Lucas:

- **Write em tema DEV/unpublished é sempre liberado** para construir, testar, gerar preview, QA visual/readback e preparar approval packet.
- **Contract Lock não deve bloquear write em DEV**.
- **Contract Lock é gate para write direto em tema Production/main e qualquer mudança customer-facing.**
- Se o asset lifestyle ainda estiver pendente, o DEV pode receber placeholder/estrutura de teste, desde que esteja claramente marcado e nunca promovido para Production sem aprovação.
- Fluxo correto: DEV/unpublished write permitido → QA visual/readback → Contract/Approval para Production → merge/promoção após aprovação Lucas.

Interpretação canônica:
- `APPROVED_FOR_DEV_WRITE` não é necessário; DEV write é permitido por padrão.
- Status recomendado: `DEV_BUILD_ALLOWED`, `PRODUCTION_BLOCKED`, `PRODUCTION_APPROVED`.
- Qualquer referência anterior que bloqueie DEV por falta de Contract deve ser lida como bloqueio de Production, não de DEV.

## CORREÇÃO CANÔNICA LUCAS — mídia editorial, DEV write e Production proibido

Registrado em: 20260606T165914Z

- LKGOC deve sempre buscar/retirar as imagens principais dos principais veículos de moda/editoriais relevantes, como Vogue, Vogue Brasil, Highsnobiety, Hypebeast e campanhas oficiais.
- Para hero, priorizar pessoa usando/contexto editorial/lifestyle; packshot/PDP/produto isolado não é hero LKGOC.
- Todo write Shopify do LKGOC deve acontecer sempre em tema DEV/unpublished e não precisa de autorização prévia de Lucas.
- Antes de qualquer write, verificar por API que o tema tem `role: unpublished`.
- Write direto em Production/main é extremamente proibido.
- A autorização de Lucas é necessária apenas para merge/promoção para Production/main ou qualquer mudança customer-facing.
- Qualquer regra anterior que bloqueie DEV por Contract/asset/licença está obsoleta; o bloqueio é para Production, não para DEV.
