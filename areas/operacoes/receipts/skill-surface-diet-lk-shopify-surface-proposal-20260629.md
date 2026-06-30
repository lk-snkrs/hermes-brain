# Receipt — Skill Surface Diet LK Shopify surface proposal

- Data/hora: 2026-06-29T11:44:15.331558+00:00
- Agente/profile/cron: Hermes default
- Empresa/área: Operações Hermes / LK Shopify
- Responsável humano: Operações Hermes
- Pedido original: Lucas disse 'Vamos continuar' após LKGOC e LK Trends; continuar otimizações Hermes com próximo P0 seguro da Skill Surface Diet.
- Classificação: read-only
- Fontes usadas:
- AGENTS/config/skills/usage do profile lk-shopify; Brain MAPA LK Shopify; skills lk-shopify-readonly/product-upload/theme-cro; relatório geral Skill Surface Diet; QA independente; Brain health; credential scan.
- O que foi feito:
- Criada proposta documental/read-only para LK Shopify com core mínimo, lentes sob demanda, handoffs, dry-run preliminar e correções pós-QA independente; nenhuma alteração em profile/config/runtime.
- Output/artefato:
- reports/governance/skill-surface-diet-lk-shopify-surface-proposal-2026-06-29.md e .json; dry-run: 40 enabled/154 disabled em Telegram se aplicado futuramente; config v23 caveat documentado.
- Aprovação: Continuação autorizada por Lucas como otimização; aplicação real ainda não aprovada.
- Envio/publicação: Telegram summary
- Writes externos: nenhum
- Riscos/bloqueios: QA inicial apontou skills inexistentes/arquivadas e risco GitHub/rollback; artefato corrigido para proteger doppler-github-pr-safe, rollback/dev workflow e declarar Playwright como ferramenta não skill.
- Rollback/mitigação: Não há rollback de runtime/config porque não houve patch; para desfazer, arquivar/remover os dois reports documentais e este receipt.
- Próximos passos: Se Lucas aprovar aplicar: gerar dry-run recalculado, backup de AGENTS/skill principal/config, patch platform_disabled.telegram, readback, restart apenas lk-shopify, receipt; depois migrar config v23->v30 em etapa separada se aprovado.
- Onde foi documentado no Brain: Este receipt e reports governance Skill Surface Diet LK Shopify.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
