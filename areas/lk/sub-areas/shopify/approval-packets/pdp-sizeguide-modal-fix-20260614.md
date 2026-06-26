# Approval packet — PDP guia de tamanhos modal fix — 2026-06-14

## Pedido
Lucas reportou que o guia de tamanho dentro da PDP está quebrado/não funciona e pediu implementação.

## Evidência read-only
- URL pública amostrada: `https://lksneakers.com.br/products/new-balance-530-white-natural-indigo-1`
- HTML live contém o botão `Guia de tamanhos` e o modal `lk-sizeguide-modal`.
- Root cause live/local: o handler ainda chama `sgFocusTrap.triggerEl`, mas `sgFocusTrap` foi removido (`/* sgFocusTrap removed */`). Resultado esperado: clique no botão gera `ReferenceError` e a classe `is-open` não é aplicada ao modal.

## Correção preparada localmente
- Worktree local: `/opt/data/worktrees/lk-new-theme-pdp-sizeguide-fix-20260614`
- Branch local: `fix/pdp-sizeguide-modal-20260614`
- Commit local: `327ccb1 fix: restore PDP size guide modal`
- Arquivo alterado: `sections/lk-pdp.liquid`

## Escopo da mudança
- Remove dependência quebrada de `sgFocusTrap`.
- Abre modal adicionando `.is-open`, `aria-hidden=false` e bloqueando scroll do body.
- Fecha por backdrop, botão fechar e Escape; retorna foco ao botão que abriu.
- Mantém tabs Sneakers/Roupas, agora escopadas ao modal.
- Adiciona `aria-hidden=true`, `tabindex=-1` no painel e `type=button` nos botões internos.

## Verificações locais
- `git diff --check`: passou.
- Secret scan no diff: `pass`.
- Busca por `sgFocusTrap` no arquivo corrigido: 0 ocorrências.
- Teste Node com DOM stub do bloco do guia: `sizeguide_block_test=pass`.
- `shopify theme check --path .`: tentou rodar, mas timeout após 300s; não foi usado como evidência de aprovação.

## Risco
- Baixo: alteração limitada ao modal de guia de tamanhos da PDP.
- Ainda precisa QA visual real em DEV/unpublished theme antes de produção.

## Rollback
- Reverter commit local `327ccb1` ou restaurar `sections/lk-pdp.liquid` do backup/branch anterior.
- Se for aplicado no Dev theme, salvar backup do asset antes do upload e re-upar backup se houver regressão.

## Próxima decisão necessária
Aprovação explícita de Lucas para:
1. subir esta correção para o tema DEV/unpublished e gerar preview da PDP; ou
2. apenas abrir PR/branch para revisão sem upload Shopify.

## Não feito
- Nenhum upload Shopify.
- Nenhuma alteração em production/live.
- Nenhum produto, preço, estoque, app, campanha, Klaviyo, WhatsApp ou checkout alterado.
