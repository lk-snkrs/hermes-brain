# LKGOC Contract Lock — [coleção]

Status: `DRAFT / BLOQUEADO / APROVADO PARA DEV BUILD / REPROVADO`
Data:
Responsável:
Handle:

## 1. Gold source coleção

- URL/snapshot aprovado:
- Asset/template/snippet fonte:
- Screenshot desktop:
- Screenshot mobile:
- Elementos imutáveis:
  - [ ] hero/header escuro no padrão
  - [ ] produto-first
  - [ ] grid antes do guia
  - [ ] guia pós-grid no padrão
  - [ ] FAQ/schema único
  - [ ] comportamento mobile preservado

## 2. Gold source guia dedicado

- URL/snapshot aprovado:
- Asset/template/snippet fonte:
- Screenshot desktop:
- Screenshot mobile:
- Shell editorial copiado de:
- O guia NÃO é:
  - [ ] article simples
  - [ ] texto corrido
  - [ ] markdown/html cru
  - [ ] bloco curto genérico

## 3. Media manifest

### Hero image 1
- URL/fonte:
- Licença/status de uso:
- Mostra pessoa usando/contexto editorial? `sim/não`
- Produto visível? `sim/não`
- Não é packshot/PDP/produto isolado? `sim/não`
- Screenshot/evidência:
- Decisão: `aprovada/bloqueada`

### Hero image 2
- URL/fonte:
- Licença/status de uso:
- Mostra pessoa usando/contexto editorial? `sim/não`
- Produto visível? `sim/não`
- Não é packshot/PDP/produto isolado? `sim/não`
- Screenshot/evidência:
- Decisão: `aprovada/bloqueada`

### Hero image 3
- URL/fonte:
- Licença/status de uso:
- Mostra pessoa usando/contexto editorial? `sim/não`
- Produto visível? `sim/não`
- Não é packshot/PDP/produto isolado? `sim/não`
- Screenshot/evidência:
- Decisão: `aprovada/bloqueada`

## 4. Guide pattern manifest

- Estrutura visual do guia pós-grid:
- Estrutura visual do guia dedicado:
- FAQ desktop:
- FAQ mobile:
- Schema único:
- Referências editoriais previstas:

## 5. Acceptance tests pré-build

- [ ] `contract_lock_exists`
- [ ] `gold_source_collection_locked`
- [ ] `gold_source_guide_locked`
- [ ] `hero_has_person_using_product`
- [ ] `hero_not_packshot`
- [ ] `guide_matches_gold_source`
- [ ] `grid_before_guide`
- [ ] `faq_unique_schema`
- [ ] `desktop_mobile_screenshots_exist`
- [ ] `visual_qa_passed`
- [ ] `rollback_ready`

## 6. Decisão

- Se qualquer item crítico for `não`: `BLOQUEADO / NÃO LKGOC`.
- Se todos forem `sim`: `APROVADO PARA DEV BUILD`, ainda sem production.

## 7. Assinatura dos workers

- Collection Intake Classifier:
- Evidence & SERP Researcher:
- LKGOC Experience Architect:
- Guia LK Editorial Writer:
- Shopify DEV Preview Builder:
- Visual QA Mobile/Desktop Worker:
- SEO/GEO Validator:
- Rollback & Receipt Verifier:


## Resultado do Gate

Status permitido: `APPROVED_FOR_DEV_WRITE` ou `BLOCKED`.

- `APPROVED_FOR_DEV_WRITE` exige todos os campos críticos preenchidos e assets aprovados.
- `BLOCKED` é obrigatório quando faltar asset lifestyle, fonte/licença, gold source ou shell de guia premium.

## Correção de status — DEV sempre permitido

Status permitido atualizado:

- `DEV_BUILD_ALLOWED`: permitido escrever em tema DEV/unpublished para construção, preview e QA.
- `PRODUCTION_BLOCKED`: não pode promover/publicar em Production/main.
- `PRODUCTION_APPROVED`: Lucas aprovou promoção/write customer-facing.

Observação: Contract Lock não bloqueia DEV. Ele documenta risco, assets pendentes e critérios para Production.

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

## HARD LOCK — Gate -2 PRD / Questions / Superpowers

Antes de qualquer rebuild LKGOC:

- PRD obrigatório;
- perguntas bloqueantes respondidas por Lucas ou marcadas como default aprovado;
- Gold Source 204L confirmado;
- critérios de aceite visual congelados;
- worker verdicts Superpowers obrigatórios;
- sem PRD ou sem perguntas: `FAIL_NO_PRD` / `FAIL_NO_QUESTIONS`.

Regra fonte: `rules/REGRA-LKGOC-PRD-ANTES-DE-REBUILD.md`.
Templates:

- `templates/lkgoc-prd-template.md`
- `templates/lkgoc-questions-template.md`
- `templates/lkgoc-worker-verdicts-template.md`
- `templates/lkgoc-side-by-side-qa-template.md`

## HARD LOCK — Shared Shell / Só Texto e Imagem Mudam

Lucas definiu que as coleções LKGOC devem ser praticamente idênticas ao Gold Source 204L. Entre coleções, só devem mudar texto, fotos/imagens, links e conteúdo específico necessário.

O padrão deve ser compartilhado para que mudanças futuras no tema/padrão propaguem de forma consistente. É proibido cada coleção virar um layout próprio.

Regra fonte: `rules/REGRA-LKGOC-SHARED-SHELL-SO-TEXTO-E-IMAGEM-MUDAM.md`.



## LKGOC pós-grid — todos os produtos
- Regra Lucas: pós-grid significa depois de todos os produtos renderizados da coleção.
- Guia/FAQ/bloco editorial antes do último produto = `FAIL_POS_GRID_NOT_AFTER_ALL_PRODUCTS`.
- QA deve provar DOM + screenshot da sequência último produto → guia.
