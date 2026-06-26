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
