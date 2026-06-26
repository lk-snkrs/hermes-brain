# Regra LKGOC — hero com pessoas + guia editorial padrão é gate bloqueante

Registrado em: 20260606T163400Z

## Motivo
Lucas rejeitou Puma Speedcat porque:
1. Guia editorial estava errado.
2. Hero usou fotos de produto/packshot em vez de pessoas usando o produto.

## Regra bloqueante
Antes de apresentar qualquer preview LKGOC:

1. **Hero LKGOC não pode usar packshot/foto de produto isolado** como mídia principal.
   - Deve usar pessoas usando o produto ou contexto editorial/lifestyle real.
   - Se não houver asset licenciado/aprovado, marcar como bloqueado e não criar substituto com produto.
2. **Guia editorial pós-grid não pode ser reescrito como bloco simplificado.**
   - Deve copiar a estrutura visual/editorial do padrão aprovado.
   - Adaptar texto/dados, não inventar layout, densidade ou hierarquia.
3. Passar no QA visual humano/side-by-side antes de chamar de LKGOC.
4. Se Lucas apontar esses erros, rollback imediato antes de nova tentativa.

## Anti-padrões proibidos
- Usar fotos de PDP/produto no hero para “preencher” mídia.
- Criar guia curto/genérico só porque o componente técnico está correto.
- Declarar correto por readback técnico quando o contrato visual está errado.

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

