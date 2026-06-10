# Playbook — Full LKGOC Rebuild

## Quando usar

Lucas pede otimização real de coleção, LKGOC Full, reconstrução, nova experiência premium ou correção profunda de coleção.

## Workers mínimos comuns

Collection Intake Classifier, Evidence & SERP Researcher, LKGOC Experience Architect, Guia LK Editorial Writer, Visual QA, SEO/GEO Validator, Rollback & Receipt.


## Gate -1 — Contract Lock obrigatório

Antes do passo 1 e antes de qualquer write Shopify:

1. Criar `LKGOC Contract Lock` para a coleção alvo usando `templates/lkgoc-contract-lock-template.md`.
2. Travar gold source da coleção e do guia.
3. Aprovar media manifest: hero deve ter pessoa usando/contexto editorial; packshot/PDP/produto isolado bloqueia.
4. Travar guide pattern manifest: guia deve copiar o padrão aprovado, não ser texto/bloco simplificado.
5. Definir acceptance tests antes do build.
6. Se qualquer item falhar: parar com `BLOQUEADO / NÃO LKGOC`.

## Fluxo

1. Abrir padrão canônico LKGOC.
2. Classificar input contract e lacunas.
3. Tratar o existente como inventário/evidência; não remendar.
4. Fazer evidence packet: fonte oficial, SERP, concorrentes, intenção, PAA, tendências e dúvidas reais.
4.1. Criar text packet e media manifest conforme `rules/REGRA-LKGOC-TEXTOS-E-SELECAO-DE-IMAGENS.md`; sem isso, Production fica bloqueada.
5. Projetar experiência: hero, produto-first, grid antes do guia, guia pós-grid, FAQ único.
6. Escrever Guia LK e metadados.
7. Materializar em DEV/unpublished ou preparar handoff para LK Shopify.
8. QA visual desktop/mobile + readback.
9. Scorecard >=85 para approval.
10. Enviar approval packet.
11. Produção só após aprovação escopada, com rollback/readback/receipt.


## Gate 0 — seleção de coleção piloto

Depois do Gate -1, executar apenas uma coleção piloto por vez. Lote só é permitido após QA visual/readback da piloto e aprovação explícita de Lucas.

## Correção de fluxo — DEV-first sempre liberado

Fluxo canônico atualizado:

1. Confirmar tema DEV por API: `role: unpublished`.
2. Write em DEV é permitido para construir/preview/QA.
3. Se assets estiverem pendentes, usar placeholder explícito no DEV e marcar `PRODUCTION_BLOCKED`.
4. Rodar QA visual/readback.
5. Preparar Contract/Approval Packet para Production.
6. Só promover/publicar em `role: main` após aprovação explícita de Lucas.

O Contract Lock não é bloqueio de DEV; é bloqueio de Production/customer-facing.

## CORREÇÃO CANÔNICA LUCAS — mídia editorial, DEV write e Production proibido

Registrado em: 20260606T165914Z

- LKGOC deve sempre buscar/retirar as imagens principais dos principais veículos de moda/editoriais relevantes, como Vogue, Vogue Brasil, Highsnobiety, Hypebeast e campanhas oficiais.
- Para hero, priorizar pessoa usando/contexto editorial/lifestyle; packshot/PDP/produto isolado não é hero LKGOC.
- Todo write Shopify do LKGOC deve acontecer sempre em tema DEV/unpublished e não precisa de autorização prévia de Lucas.
- Antes de qualquer write, verificar por API que o tema tem `role: unpublished`.
- Write direto em Production/main é extremamente proibido.
- A autorização de Lucas é necessária apenas para merge/promoção para Production/main ou qualquer mudança customer-facing.
- Qualquer regra anterior que bloqueie DEV por Contract/asset/licença está obsoleta; o bloqueio é para Production, não para DEV.

## Gate obrigatório — 204L Gold Source Visual Contract

Depois do build DEV e antes de qualquer PASS:

1. Capturar Gold Source New Balance 204L.
2. Capturar coleção alvo no DEV/unpublished.
3. Gerar side-by-side 204L vs alvo.
4. Reprovar se a coleção alvo parecer layout próprio ou interpretação livre.
5. Só aceitar se for uma adaptação mínima do shell 204L.

Este gate é bloqueante para approval packet e Production.

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


## Camada Claude SEO

Depois do evidence packet e antes do text packet final, aplicar Claude SEO como camada de apoio para intenção, SERP, FAQ, title/meta, GEO/AI Search e validação de genericidade. Não permitir que Claude SEO altere shell visual, padrão 204L ou escolha de mídia sem media manifest.

Regra fonte: `rules/REGRA-LKGOC-CLAUDE-SEO-COMO-CAMADA-DE-APOIO.md`.
