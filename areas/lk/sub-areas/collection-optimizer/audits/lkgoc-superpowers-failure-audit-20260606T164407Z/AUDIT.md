# AUDIT — Falha LKGOC/Superpowers e reconstrução da lógica

Data: 2026-06-06T16:44:07.106893+00:00

## Pergunta do Lucas
“Por que você errou? Você não deveria reconstruir toda a lógica do LKGOC para não termos mais esse problema? Vamos fazer um audit usando o Skill Superpowers?”

## Resposta curta
Sim. O erro foi sistêmico: a lógica operacional permitia executar por validações parciais. Eu usei gates técnicos como se fossem gates LKGOC. O Superpowers tinha regras certas espalhadas, mas não tinha um **gate atômico bloqueante antes do write** que impedisse qualquer implementação sem asset lifestyle/on-foot e guia clonado do padrão.

## Causa raiz
1. **Validação técnica substituiu validação visual.**  
   Readback, DOM, ausência de Liquid error e componente único foram tratados como suficientes.
2. **Contrato visual não foi travado antes do write.**  
   Eu não congelei, em artefato, qual gold source seria clonado e quais partes eram imutáveis.
3. **Media gate era checklist, não trava.**  
   A skill dizia que packshot era proibido, mas o fluxo não abortava automaticamente se faltasse imagem de pessoa usando.
4. **Guide gate era genérico demais.**  
   O playbook dizia “Guia LK”, mas não exigia prova de clonagem do padrão visual antes da escrita.
5. **Lote/pressa contaminou execução.**  
   A tentativa de resolver as 5 coleções criou pressão para preencher lacunas com aproximação.
6. **Workers foram usados como registro conceitual, não como veto real.**  
   Visual QA e Experience Architect não tinham poder explícito de bloquear antes do write.

## Falhas observadas nas entregas rejeitadas
- Hero com fotos de produto/PDP, violando LKGOC.
- Guia editorial simplificado, sem copiar a estrutura aprovada.
- Uso de “componente único” como falsa prova de conformidade.
- Preview apresentado como avanço quando deveria ser classificado como `NÃO LKGOC`.

## Correção feita neste audit
1. Criada regra nova: `rules/REGRA-LKGOC-CONTRACT-LOCK-ANTES-DE-WRITE.md`.
2. Skill Superpowers será promovida para v1.2 com Contract Lock obrigatório.
3. Checklist QA será reforçado com campos binários bloqueantes.
4. Playbook Full Rebuild será alterado para abortar antes do write se faltar Contract Lock.
5. AGENTS do Collection Optimizer será reforçado para dar veto real aos workers Visual QA e Experience Architect.

## Nova lógica operacional
Antes de qualquer Shopify write:

- Contract Lock preenchido.
- Gold source coleção identificado.
- Gold source guia identificado.
- Media manifest com pessoa usando/contexto editorial.
- Guide pattern manifest.
- Acceptance tests definidos antes do build.

Depois do write DEV:

- Readback API.
- Preview DEV.
- Screenshot mobile/desktop.
- QA contra gold source.
- Só então enviar para Lucas — e ainda como approval, não production.

## Critério de aceite para próximos LKGOC
Uma entrega só pode ser chamada de LKGOC se todos forem `true`:

- `contract_lock_exists`
- `gold_source_collection_locked`
- `gold_source_guide_locked`
- `hero_has_person_using_product`
- `hero_not_packshot`
- `guide_matches_gold_source`
- `grid_before_guide`
- `faq_unique_schema`
- `desktop_mobile_screenshots_exist`
- `visual_qa_passed`
- `rollback_ready`

## Recomendação executiva
Congelar implementação de Nike/Puma/Adidas/Yeezy/Labubu até fazer um piloto correto em **uma única coleção** com Contract Lock. Se faltar asset de pessoa usando, a saída correta é pedir asset ou marcar bloqueado, não improvisar.
