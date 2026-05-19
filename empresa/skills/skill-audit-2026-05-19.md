# Auditoria de skills — Hermes Brain

Data: 2026-05-19  
Motivo: gap P0 da auditoria BRUNO-ATUAL.  
Escopo: skills canônicas versionadas em `skills/*/SKILL.md`.  
Ação executada: documentação/auditoria. Nenhuma skill runtime foi instalada, carregada, removida ou executada por este arquivo.

## Regra canônica

Skill resolve workflow repetível. Para ser considerada canônica no Hermes Brain, precisa ter:

- gatilho claro;
- passos executáveis;
- saída esperada;
- verificação;
- guardrails de aprovação quando houver ação externa, produção, dados vivos, secrets ou writes;
- índice em `empresa/skills/_index.md`.

## Matriz atual

| Skill | Caminho | Owner | Status documental | Risco | Gatilho | Última revisão documental | Última execução runtime | Decisão |
|---|---|---|---|---|---|---|---|---|
| Mesa COO | runtime skill `/opt/data/skills/productivity/mesa/SKILL.md`; Brain doc `areas/operacoes/rotinas/mesa-coo-diaria-telegram-2026-05-19.md` | Hermes Geral | canônica runtime + documentada | baixo/médio | `/mesa`, `Mesa COO`, cron diário Telegram | 2026-05-19 criada | cron `749ee30b51eb` ativo; primeira execução agendada 2026-05-20 08h30 BRT | manter; depende de `/reload-skills`/gateway para slash imediato |
| Hermes Brain | `skills/hermes-brain/SKILL.md` | Operações Hermes | canônica | baixo | uso do Brain como fonte de verdade | 2026-05-19 auditada | não verificada nesta rodada | manter |
| Session Start Protocol | `skills/session-start-protocol/SKILL.md` | Operações Hermes | canônica, mas deve ser reconciliada com o novo `memories/current.md` | médio | boot/checklist de sessão | 2026-05-19 auditada | não verificada nesta rodada | manter e atualizar em rodada futura se necessário |
| Brain Sync | `skills/brain-sync/SKILL.md` | Operações Hermes | canônica | médio | sync/versionamento do Brain | 2026-05-19 auditada | não verificada nesta rodada | manter; sempre checar diff/segredos |
| LK Cross-sell | `skills/lk-crosssell/SKILL.md` | LK CRM | canônica | médio | oportunidade pós-pedido/cross-sell | 2026-05-19 auditada | não verificada nesta rodada | manter; externo exige aprovação |
| LK Leads Esfriando | `skills/lk-leads-esfriando/SKILL.md` | LK CRM | canônica | médio | leads esfriando/reativação | 2026-05-19 auditada | não verificada nesta rodada | manter; externo exige aprovação |
| LK Shopify Read-only | `skills/lk-shopify-readonly/SKILL.md` | LK Ecommerce | canônica | médio | consulta/análise Shopify sem write | 2026-05-19 auditada | não verificada nesta rodada | manter; dados vivos exigem fonte/API |
| LK Shopify Product Upload | `skills/lk-shopify-product-upload/SKILL.md` | LK Ecommerce | canônica | alto | cadastro/subida de produto Shopify | 2026-05-19 auditada | não verificada nesta rodada | manter com approval gate; write só aprovado |
| LK SEO Weekly Improvement | `skills/lk-seo-weekly-improvement/SKILL.md` | LK Growth/SEO | canônica | médio | melhoria semanal SEO/CRO | 2026-05-19 auditada | não verificada nesta rodada | manter; alterações visíveis exigem aprovação |

## Gaps encontrados

- Falta campo estruturado de `owner/status/risco/última revisão/última execução` dentro de cada skill. Esta auditoria cria a primeira matriz central sem editar o conteúdo das skills.
- `Session Start Protocol` ainda referencia boot operacional amplo; em uma próxima rodada pode apontar explicitamente para `memories/current.md` como camada quente.
- Rotinas maduras de LK Growth, GMC, Daily/Weekly e Mission Control podem futuramente virar skills específicas, mas isso exige auditoria de uso e não foi feito nesta rodada.
- Mordomo foi documentado como agente/profile, não como skill. Só deve virar skill se houver workflow repetível aprovado.

## Checklist para próxima auditoria

1. Verificar se cada skill ainda existe no runtime ativo, sem instalar/remover nada sem aprovação.
2. Registrar última execução real quando houver evidência segura.
3. Promover rotinas repetidas a skill apenas quando houver 2+ usos ou padrão aprovado.
4. Depreciar skill obsoleta com ponte/redirect antes de remover.
5. Rodar health check e secret scan em qualquer mudança de skill.

## Guardrails

- Skill não autoriza envio externo.
- Skill não autoriza cron novo.
- Skill não autoriza write em Shopify, Supabase, Tiny, Klaviyo, Meta, Merchant Center, tema, VPS ou runtime.
- Qualquer credencial deve aparecer só por nome de secret/cofre, nunca valor.
