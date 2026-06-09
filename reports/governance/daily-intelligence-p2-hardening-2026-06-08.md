# Daily Intelligence Loop — P2 hardening local/read-only — 2026-06-08

## Escopo aprovado
Lucas pediu continuidade P2 para tornar Hermes menos propenso a erro, mais inteligente e mais proativo.

Executado apenas em escopo local/read-only/documental/script:
- sem Docker/VPS/Hostinger/Traefik/gateway restart;
- sem mudança de secrets ou persistência de valores;
- sem writes externos/source-of-truth;
- sem criação/remoção/reagendamento de cron.

## Melhorias implementadas

1. `host_docker_observability_snapshot`
   - O preflight v3 passa a ler o artefato sanitizado mais recente de Host/Docker.
   - Uso: evitar conclusões erradas quando a visão local divergir da verdade do host.
   - Regra: se stale/alerta, classificar como observability gap ou rerodar helper read-only; nunca mutar Docker/gateway.

2. `p2_release_adoption_planner`
   - Se não houver tag nova, o 02h deve pular revisão repetida de release.
   - Se houver tag nova, criar matriz local de adoção; upgrade/runtime continua approval-gated.

3. `skill_quality_audit`
   - O preflight passa a auditar skills grandes, stale ou com referências mencionadas ausentes.
   - Uso: reduzir erro por instrução obsoleta/oversized; preferir lookup em referências/Brain antes de agir.

4. `mistake_ledger`
   - Novo artefato `reports/hermes-mistake-ledger/latest.json`.
   - Transforma alertas recorrentes em padrão → causa de erro → próxima ação segura → limite de aprovação.

5. Cron 02h atualizado
   - O prompt do job 02h foi atualizado para consumir os sinais P2.
   - Mantidos: agenda 02h BRT, `deliver=local`, mesmo script, sem novo cron.

## Evidência inicial
- Host/Docker helper read-only gerou artefato sanitizado com `alerts_count=0`, `containers_count=2`, versões e cron status sanitizados presentes.
- Release planner: sem tag nova; ação correta é não repetir revisão de release.
- Skill audit: 225 skills escaneadas; flags viram sinal de confiança/curadoria, não falha automática.
- Mistake ledger: padrões gerados a partir de alertas recorrentes e riscos de skill/release/observabilidade.
- `values_printed=false`.

## Próximo comportamento esperado no 02h
O Daily Intelligence Loop deve:
- parar de repetir release igual;
- distinguir alerta recorrente de problema novo;
- não confundir gap de observabilidade com falha de runtime;
- consultar fonte/Brain quando skill estiver grande/stale;
- reportar causa-raiz e próxima ação, não só sintomas.

## Sync policy
Brain Sync safe dry-run listou `CHANGELOG.md`, mas ainda não listou os novos artefatos P2 em `reports/governance/`, `reports/hermes-mistake-ledger/` e o recibo host-observability P2. Isso é uma lacuna estreita de allowlist/política de sync, não falha do hardening local. Não usar `git add .`; tratar em pacote separado se esses artefatos precisarem sincronizar remotamente.
