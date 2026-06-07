# PRD / Contract Lock — LKGOC Puma Speedcat

Timestamp: 20260606T233512Z
Status: **DEV_BUILD_ALLOWED / PRODUCTION_BLOCKED**

## Coleção
- Handle: `puma-speedcat`
- Preview DEV: `https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718`
- Tema DEV: `155065450718` / `lk-new-theme/dev` / `role: unpublished`
- Production: proibido sem aprovação explícita do Lucas.

## Objetivo
Criar experiência LKGOC premium para Puma Speedcat copiando/adaptando o shell visual aprovado da New Balance 204L, sem inventar arquitetura nova.

## Gold source
- New Balance 204L production.
- Estrutura a copiar: hero editorial preto antes do grid + grid de todos os produtos + guia/FAQ pós-grid.
- Namespace novo preferencial: `lk-goc-*`, mantendo aliases quando necessário.

## Decisões Lucas aplicadas
- LKGOC não inventa layout novo.
- DEV/unpublished pode receber write para preview/QA.
- Production/main bloqueado.
- Pós-grid significa **depois de todos os produtos**.

## Direção editorial
- Motorsport/F1 heritage: silhueta nascida da cultura de pista.
- Fashion/street style: sneaker baixo, alongado, fácil com jeans, alfaiataria relaxada e saias/peças minimalistas.
- Curadoria LK: seleção, autenticidade e atendimento humano.

## Conteúdo obrigatório
- Hero pré-grid com imagem/contexto editorial/lifestyle.
- Texto curto e premium; sem tom enciclopédico.
- Grid de produtos intacto.
- Guia LK pós-grid com:
  - como escolher entre OG, suede/faded/archive;
  - ajuste/forma;
  - como usar;
  - autenticidade LK;
  - FAQ único.
- Schema FAQ se compatível, sem duplicar FAQ existente.

## Regras negativas
- Não usar packshot/PDP como hero principal.
- Não mencionar desconto como ângulo público.
- Não falar pronta entrega/encomenda/estoque como taxonomia.
- Não colocar guia antes do último produto.
- Não escrever em Production.

## Acceptance tests
1. Tema confirmado `role: unpublished` antes do write.
2. Collection carrega sem Liquid error.
3. Hero aparece antes do grid e segue shell 204L.
4. Todos os 13 produtos continuam no grid antes do guia.
5. Primeiro marcador editorial/guia pós-grid aparece após o último card no DOM e no scroll.
6. FAQ não duplica.
7. Visual QA mobile/desktop sem overflow.
8. Approval packet enviado antes de Production.

## Worker verdicts iniciais
- Intake: PASS — pedido é LKGOC Full para Puma Speedcat.
- Evidence: PASS com SERP/editorial suficiente; asset final ainda requer validação visual no preview.
- Experience Architect: PASS condicionado a copiar shell 204L e pós-grid correto.
- Editorial: PASS condicionado a tom premium e FAQ único.
- Shopify DEV Builder: ALLOWED apenas em `155065450718` se `unpublished`.
- Visual QA: PENDING.
- SEO/GEO: PENDING.
- Rollback/Receipt: PENDING.
