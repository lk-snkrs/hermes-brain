# Brain Consolidation by Organogram — 2026-05-16

## Premissa

Lucas confirmou o organograma: uma Grande Mente central no topo; abaixo ficam Lucas pessoal, empresas e as camadas de Operações/Tecnologia/Governança. A consolidação do Brain deve obedecer essa hierarquia, não apenas juntar arquivos por data.

## Contagem atual por camada

- `00-grande-mente-global`: 3 entradas (M:3)
- `01-empresa-cross-area`: 8 entradas (??:3, M:5)
- `10-lk-sneakers`: 674 entradas (??:648, M:26)
- `20-zipper-galeria`: 6 entradas (??:5, M:1)
- `40-operacoes-hermes`: 39 entradas (??:33, M:6)
- `60-governanca-seguranca`: 1 entradas (??:1)
- `80-scripts-a-classificar`: 4 entradas (??:4)
- `90-reports-evidencias`: 13 entradas (??:13)
- `99-revisar-manualmente`: 3 entradas (??:1, M:2)

## Ordem recomendada de commits locais

1. `00-grande-mente-global` + `01-empresa-cross-area`: mapas, organograma, decisões e guardrails globais.
2. `40-operacoes-hermes` + `50-tecnologia-infra` + `60-governanca-seguranca`: rotinas Hermes, watchdogs, runtime docs e segurança.
3. `10-lk-sneakers`: LK OS, GMC, Shopify/Tiny, relatórios e scripts LK.
4. `20-zipper-galeria`: Zipper OS/inbox/follow-ups/logística.
5. `30-spiti-auction`: Spiti Hub docs/diffs após revisão focada.
6. `90-reports-evidencias` e `80-scripts-a-classificar`: somente depois de ligar evidência à rotina/mapa correspondente.

## Guardrails

- Não pushar ainda.
- Não commitar tudo em massa.
- Não apagar worktree/repo que contenha commit único sem diff focado.
- Não tocar Docker/VPS/produção.
- Não executar envio externo, campanha, Shopify/Tiny/GMC/database write ou cliente.
- `reports/` é evidência; fonte operacional viva deve ficar em `empresa/` ou `areas/`.
