# Manual simples — Hermes/LK em produção

Gerado em: 2026-05-30T21:41:19+00:00  
Status: **fonte canônica operacional v0.1**  
Escopo: documentação e governança local. **Não autoriza mudança de runtime, Docker, VPS, Traefik, secrets, webhooks, crons ou writes externos.**

## Para que isto existe

Este diretório reduz a documentação espalhada do Hermes/LK a um conjunto pequeno de arquivos que devem guiar operação diária.

A regra é simples:

- **Este diretório é a fonte da verdade operacional curta.**
- Relatórios antigos continuam úteis como histórico/evidência, mas não devem ser usados como manual principal.
- Se houver conflito entre um relatório antigo e este manual, usar este manual e reabrir evidência read-only antes de agir.

## Arquivos canônicos

1. `OPERATING_MANUAL.md`
   - Visão geral simples: quem é quem, como pensar os perfis, o que significa online/offline e quais são os princípios de operação.

2. `PROFILE_STATUS_MATRIX.md`
   - Matriz dos principais perfis vivos/relevantes: missão, Telegram, API/webhook, modelo, toolsets e observações.

3. `RUNTIME_REPAIR_RUNBOOK.md`
   - Playbook de diagnóstico e reparo seguro para casos como “LK Shopify offline”, bot lento, cron não entregou, provider travou e gateway duplicado.

4. `DECISION_POLICY.md`
   - O que o Hermes pode fazer sozinho, o que exige aprovação escopada e o que é bloqueado sem aprovação explícita.

5. `CAPABILITIES_ADOPTION_MATRIX.md`
   - Matriz de features oficiais do Hermes vs uso atual: Skills, Memory, Profiles, Toolsets, Cron, Delegation, Kanban, MCP, Plugins, Hooks, Dashboard/API, Goals, Batch, Deliverable Mode e prioridades de piloto.

6. `PHASE_2_CONTROLLED_ADOPTION.md`
   - Charter da Fase 2: frentes abertas, escopo permitido, guardrails e critérios para transformar capabilities em pilotos seguros.

7. `HERMES_FEATURE_BACKLOG.md`
   - Backlog canônico da Fase 2 com cards documentais/unassigned para Kanban, MCP, plugin local/read-only, dashboard/API e deliverables.

8. `F2_004_DASHBOARD_API_EXPOSURE_CLASSIFICATION.md`
   - Resultado do card F2-004: classificação read-only da exposição API/webhook/dashboard do default; revalidação 2026-06-03 registrou API default host-local, webhook público e dashboard público separado exigindo revisão de autenticação/exposição.

9. `F2_001_KANBAN_BOARD_DESIGN.md`
   - Resultado do card F2-001: design documental do board Kanban `hermes-lk-improvements`, estados, labels de risco, template de card e política de assignees.

10. `F2_002_MCP_INVENTORY_AND_CANDIDATES.md`
   - Resultado do card F2-002: inventário MCP/DataForSEO existente e candidatos MCP para integrações Lucas/LK/Zipper/SPITI/Hermes.

11. `F2_006_BUSINESS_MCP_POLICY.md`
   - Política MCP de negócio v0.1: classes de risco, whitelist, sampling, approval e regras para Meta Ads, Klaviyo, Tiny, Metricool, Supabase e DataForSEO.

12. `F2_007_DATAFORSEO_MCP_PILOT_RECEIPT.md`
   - Receipt do piloto MCP DataForSEO pequeno para LK SEO/GEO com keyword única e duas tools read-only.

13. `APPROVAL_PACKET_SUPABASE_MCP_READONLY.md`
   - Approval packet para eventual Supabase MCP read-only por empresa/projeto.

14. `MCP_ROADMAP_META_KLAVIYO_TINY_METRICOOL.md`
   - Roadmap técnico seguro para conectar Meta Ads, Klaviyo, Tiny e Metricool por MCP sem ativação runtime ainda.

15. `RECEIPT_MCP_READONLY_LK_GROWTH_AND_LK_SHOPIFY_HEALTH_20260530.md`
   - Receipt da ativação dos MCPs read-only `metricool_readonly` e `meta_ads_readonly` no profile `lk-growth`, mais probe de saúde do LK Shopify.

## Documentos rebaixados para histórico/evidência

Não apagar. Apenas não usar como manual diário.

### Relatórios recentes úteis

- `/opt/data/reports/hermes-operational-surface-matrix.md`
- `/opt/data/reports/hermes-profile-surface-governance-policy.md`
- `/opt/data/reports/hermes-runtime-change-approval-template.md`
- `/opt/data/reports/hermes-operational-inventory-20260530.json`
- `/opt/data/reports/hermes-fase0-fase1-verification-20260530.json`

### Estratégia/PRD

- `/opt/data/reports/hermes-agent-improvement-prd.md`
- `/opt/data/reports/hermes-agent-improvement-implementation-plan.md`
- `/opt/data/reports/hermes-agent-prd-reread-gap-analysis-20260530.md`

### Receipts/governance históricos

- `/opt/data/reports/governance/`

Use esses arquivos apenas para reconstruir decisões, evidências e histórico de correções.

## Regra de manutenção

Quando um novo incidente ou melhoria operacional virar padrão reutilizável:

1. Atualizar o arquivo canônico adequado neste diretório.
2. Manter o relatório/receipt detalhado separado como histórico.
3. Não transformar este manual em dump técnico.
4. Preferir bullets curtos, ações verificáveis e limites claros.
