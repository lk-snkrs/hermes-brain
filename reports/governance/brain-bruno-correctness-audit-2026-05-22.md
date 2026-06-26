# Auditoria Bruno/OpenClaw do Hermes Brain — 2026-05-22

Status: **direcionalmente correto, estruturalmente saudável, operacionalmente quase correto — não 10/10**.

## Pergunta

Lucas pediu: “Faça um audit no brain e como o Bruno ensina, está tudo correto?”

## Veredito executivo

O Brain está **correto no desenho principal** do método Bruno/OpenClaw adaptado para Hermes:

- Brain como fonte de verdade versionada, não chat solto.
- Camada `hot/current` para contexto vivo.
- Rotinas, MAPAs, agentes documentais, skills e governança separados por área.
- Crons e watchdogs reconciliados com evidência runtime, não só documentação.
- Fechamento 23h + Brain Sync em modo local/silencioso.
- Guardrails fortes para Docker/VPS, externos, Shopify/GMC/WhatsApp/e-mail/campanhas e secrets.

Mas **não estava tudo perfeito**. A auditoria encontrou e corrigiu localmente alguns resíduos Bruno/OpenClaw/`cerebro-cimino` em agentes legados e pequenos drifts documentais de runtime.

Nota honesta pós-correção: **8,2/10**.

## Evidência viva coletada

Data/hora da auditoria: `2026-05-22T11:55:34+00:00`.

### Checks técnicos

- `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-22-bruno-audit.json`
  - Resultado: `FAIL=0`, `WARN=0`, `issues=0`.
- `python3 /opt/data/scripts/brain_operating_layer_audit.py`
  - Resultado: exit `0`, stdout vazio; contrato silent-OK respeitado.
- `git diff --check`
  - Resultado: sem erros de whitespace/conflito.
- `python3 /opt/data/scripts/brain_sync_safe.py --dry-run`
  - Resultado: dry-run executado; `allowed_files=21`, `skipped_files=275` por allowlist/guardrails.
  - Isso é esperado: reports brutos/snapshots/artefatos não allowlisted continuam bloqueados.

### Runtime/crons

Fonte viva: `cronjob list` da sessão.

- Jobs totais: `29`.
- Jobs ativos: `23`.
- Jobs pausados: `6`.
- Últimos status não-ok na evidência viva: `0`.
- Delivery error explícito: `0`.
- Jobs centrais Bruno/Hermes Brain ativos:
  - `Lucas Brain daily intelligence loop` — `f5a23dd6a1bd`, ativo, `local`, último run `ok` em 2026-05-22.
  - `Hermes Brain Fechamento Ágil 23h + Brain Sync` — `3fc45b0830c6`, ativo, `local`, último run `ok` em 2026-05-22.
  - `Hermes Brain Operating Layer structural watchdog` — `d03fa04e1188`, ativo, `no_agent`, último run `ok`.
  - `Hermes Brain Runtime Truth Reconciler` — `2404c0766d33`, ativo, `local`, último run `ok`.
  - `Lucas Brain weekly Learning Loop report` — `f4c499e85eac`, ativo, aguardando primeira segunda-feira útil.

## O que foi corrigido nesta auditoria

Correções locais/documentais, sem writes externos:

1. `agentes/lk/AGENTS.md`
   - Removidas instruções operacionais antigas que apontavam para `cerebro-cimino/...`.
   - Removida instrução perigosa/obsoleta de `cd /root/cerebro-cimino && git add ... && git push`.
   - Substituída por handoff/receipt no Hermes Brain Central e commit apenas quando o fluxo pedir checkpoint versionado com secret scan.

2. `agentes/zipper/AGENTS.md`
   - Mesmas correções de paths, visibilidade e fonte de verdade.

3. `agentes/lk/SOUL.md` e `agentes/zipper/SOUL.md`
   - Escopos atualizados de `cerebro-cimino/...` para caminhos atuais do Hermes Brain.

4. `areas/operacoes/inventarios/crons-agentes-profiles.md`
   - Corrigido drift documental:
     - `LK GMC Review read-only mandatory delivery` agora documentado como ativo/read-only na evidência viva de 2026-05-22.
     - `Zipper OS vendas 09h WhatsApp/email` agora documentado como `local` na evidência viva, com Telegram só para exceções quando aplicável.

5. `memories/hot.md`
   - Atualizado timestamp da camada quente.
   - Adicionada prioridade current: LK/GMC permanece read-only até confirmação visual das Data Sources e aprovação explícita para qualquer write externo.

## Scorecard Bruno/OpenClaw → Hermes-native

- Arquitetura / fonte de verdade: **9/10**
  - Forte: Brain versionado, MAPA, START-HERE, AGENTS, governança e hierarquia Grande Mente.
  - Gap: alguns agentes legados ainda carregavam linguagem/path do sistema antigo; corrigido nesta rodada para LK/Zipper.

- Segurança / secrets / aprovações: **9/10**
  - Forte: health check limpo; secret guardrails; writes externos bloqueados por padrão.
  - Gap: continuar mantendo scans antes de commit/sync porque o repo recebe muitos artefatos operacionais.

- Memória quente / current context: **8/10**
  - Forte: `memories/hot.md` existe e foi atualizado.
  - Gap: precisa continuar sendo mantido no fechamento diário; stale hot memory é risco real.

- Agentes / identidade / handoff: **8/10**
  - Forte: Hermes Geral, LK, Zipper, SPITI e perfis estão documentados.
  - Gap: Mordomo ainda está espalhado em `areas/operacoes/`; inventário já marca a dúvida se deve virar `agentes/mordomo/` ou `areas/lucas-pessoal/`.

- Skills ownership/status/risk: **7/10**
  - Forte: índice existe e skills canônicas críticas estão apontadas.
  - Gap: ainda falta uma auditoria formal de skills com owner/status/risco/última revisão/última execução para todas as skills relevantes.

- Crons / runtime truth: **8,5/10**
  - Forte: runtime reconciler ativo e atualizado; crons críticos ok.
  - Gap: alguns watchdogs ainda usam `origin`; se estiverem silent-OK de verdade, não é incidente, mas ainda é pendência de revisão de ruído.

- Integrations/canais: **8/10**
  - Forte: Telegram, LK, Zipper, SPITI, Mordomo e rotinas principais aparecem no inventário.
  - Gap: confirmar/limpar one-shots pausados antigos e documentar melhor o destino de alguns canais especialistas.

- Mission/legacy alignment: **8/10**
  - Forte: Brain já explicita que OpenClaw/Amora são referência, não cópia.
  - Gap: resíduos textuais em documentos legados precisam continuar sendo varridos com busca direcionada; LK/Zipper foram tratados agora.

## Pendências reais, sem dramatizar

1. Criar ou consolidar uma pasta canônica para Mordomo/Lucas pessoal se o volume continuar crescendo.
2. Fazer auditoria formal de skills com campos: owner, status, risco, trigger, last review, last verification.
3. Revisar watchdogs `origin` que deveriam ser local/silent-OK para reduzir ruído.
4. Limpar ou arquivar one-shots pausados antigos depois de confirmar que não têm valor operacional.
5. Continuar varredura de resíduos OpenClaw/`cerebro-cimino` fora de `agentes/lk` e `agentes/zipper`, preservando avisos históricos quando forem úteis.

## Limites desta auditoria

Não foi feito nenhum write externo:

- Sem Shopify/GMC/API write.
- Sem WhatsApp/e-mail/campanha/envio externo.
- Sem Docker/VPS/gateway/Traefik/container/network.
- Sem alteração de cron/schedule/delivery.
- Sem secrets impressos ou movidos.

## Conclusão

Resposta curta: **sim, está correto no método Bruno, mas não estava 100% limpo**.

Agora, após as correções locais desta auditoria, o Brain está em estado bom para continuar: **health limpo, runtime crítico ok, fonte de verdade respeitada, e os principais resíduos perigosos nos agentes LK/Zipper removidos**.
