# Brain worktrees — fila de integração

Data: 2026-05-16
Branch base: `consolidation/brain-filesystem-git-hygiene-20260516`

## Resultado da auditoria

Foram encontrados 43 worktrees além do Brain canônico.

- 43 limpos (`git status --short` sem pendências).
- 0 sujos.
- 0 totalmente contidos no HEAD atual por ancestralidade.
- 0 com árvore idêntica ao HEAD atual.

Conclusão: **não remover automaticamente**. Todos ainda representam alguma diferença de conteúdo ou linha histórica que precisa ser integrada, exportada ou descartada conscientemente.

## Grupos de integração

### 1. LK / marketing, attribution e creative — 23 worktrees

Prioridade alta para consolidar porque cruza com Pareto/GA4/Meta/FHITS/Maicon, que são áreas já operacionalmente relevantes para LK.

Inclui temas como:

- paid attribution;
- campaign attribution map;
- campaign dictionary;
- creative assets/audits/sales view;
- GA4 docs;
- influencer audits;
- Meta attribution label fix;
- ROAS/campaign title;
- Pareto monthly reconciliation;
- weekly influencer creative reports.

Ação recomendada: integrar primeiro em um commit temático `docs: integrate lk marketing attribution worktrees`, preservando relatórios úteis e descartando duplicatas geradas.

### 2. LK / email e reporting — 4 worktrees

Inclui:

- Gmail safe HTML;
- inline creative email;
- weekly influencer email;
- Gmail fix for influencer email.

Ação recomendada: integrar depois do grupo de attribution, com atenção à regra de segurança: **não criar drafts/enviar e-mail externo sem aprovação explícita de destinatário + conteúdo**.

### 3. Brain/global/Bruno/multiempresa — 16 worktrees

Inclui:

- brain score script;
- Bruno P0/P1 operational instruments;
- retomada planos/PRDs;
- healthchecks;
- memory hygiene;
- multiempresa operational review;
- material ingest test;
- alguns worktrees LK antigos que são mais estruturais do que relatórios de marketing.

Ação recomendada: integrar por subgrupo, mantendo o organograma correto: Grande Mente primeiro, depois empresas/áreas abaixo.

## Regra de remoção

Só remover worktree quando uma destas condições for verdadeira:

1. `git merge-base --is-ancestor <worktree-head> <current-head>` retornar sucesso; ou
2. `git diff --quiet <current-head> <worktree-head>` retornar sucesso e o branch/commit estiver preservado; ou
3. houver decisão explícita documentada de descartar o conteúdo, com resumo do que foi descartado.

Nenhuma dessas condições foi satisfeita agora.

## Próximo passo recomendado

Começar pelo grupo **LK / marketing, attribution e creative**, porque é o maior, mais próximo do uso real da LK e menos arriscado que mexer em infra/runtime.


## Execução parcial — LK marketing/attribution

Atualização: 2026-05-16.

O grupo **LK / marketing, attribution e creative** foi exportado e teve 23 worktrees removidos com segurança operacional:

- worktrees estavam limpos;
- branches/commits foram preservados;
- o worktree detached recebeu branch de arquivo antes da remoção;
- nenhum push, PR, produção, Docker ou sistema externo foi alterado;
- relatório de preservação em `lk-marketing-attribution-export/`.

Restam 20 worktrees além do Brain canônico.


## Execução parcial — LK email/reporting

Atualização: 2026-05-16.

O grupo **LK / email e reporting** foi exportado e teve 4 worktrees removidos com segurança operacional:

- worktrees estavam limpos;
- branches/commits foram preservados;
- nenhum e-mail/Gmail draft/envio externo foi criado;
- nenhum push, PR, produção, Docker ou sistema externo foi alterado;
- relatório de preservação em `lk-email-reporting-export/`.

Restam 16 worktrees além do Brain canônico.


## Execução final — worktrees estruturais restantes

Atualização: 2026-05-16.

Os 16 worktrees restantes foram exportados e removidos como diretórios de worktree, preservando branches/commits.

- todos estavam limpos;
- nenhum branch foi deletado;
- nenhum push/PR foi executado;
- nenhum sistema externo/produção foi alterado;
- relatório de preservação em `global-structural-export/`.

Resultado final: resta apenas o Brain canônico como worktree registrado.
