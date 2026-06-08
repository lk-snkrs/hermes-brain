# Memória quente — contexto current

Atualizado: 2026-06-07
Status: camada current compacta para orientar execução. Histórico/evidência fica em reports/receipts/daily, não aqui.

## Política de memória em vigor

- Fonte canônica: `memories/politica-memoria-hermes.md`.
- `MEMORY.md`/`USER.md` = boot mínimo injetado: preferências, guardrails globais e ponteiros.
- Brain/daily/hot/reports/receipts/skills/session_search = memória rica e continuidade.
- Provider externo/Mem0 = rejeitado/off até novo PRD/spike explícito de Lucas.
- Watchdog 02h15 faz higiene local/silent-OK de boot memories com backup e cobertura por roster.

## Prioridades current

1. Manter Brain como fonte rica canônica; não transformar prompt memory em repositório.
2. Telegram para Lucas deve conter só decisão, exceção, falha ou resumo desejado; sucesso normal fica local/Brain.
3. Fechamento 01h + supervisor 02h + higiene 02h15 + relatório 02h30 devem fechar a cadeia: report/handoff → daily curado → hot atualizado quando houver prioridade/bloqueio atual.
4. Corrigir qualquer alerta de `hot.md stale` atualizando esta camada, não repetindo histórico antigo.
5. Para dado vivo — gateway, cron, estoque, pedido, métrica, deploy, campanha — consultar fonte real no momento antes de afirmar.

## Bloqueios e guardrails current

- Sem Docker/VPS/Traefik/SSH/containers/volumes sem aprovação escopada, backup/rollback e verificação.
- Sem writes externos em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco/campanhas sem fonte e aprovação adequada.
- Sem tokens, secrets, payloads sensíveis ou localizadores de credencial em Telegram/docs versionáveis.
- Documentação de rotina não prova execução ativa; runtime precisa de evidência viva.

## Estado operacional quente

- Runtime Hermes esperado atual: v0.16.0. Alertas antigos para v0.15.1 são históricos/superseded.
- Boot-memory watchdog 02h15: último estado conhecido OK, provider externo off, sem saturação/over-limit, cobertura completa dos profiles com arquivos de memória.
- Structural watchdog detectou que este `hot.md` estava stale; refresh aplicado em 2026-06-07 com backup em `reports/governance/memory-backups/`.
- Daily 2026-06-07 existe e foi curada a partir do fechamento/relatórios do dia.

## Links quentes

- Política: `memories/politica-memoria-hermes.md`
- Daily atual: `memories/daily/2026-06-07.md`
- Fechamento atual: `reports/daily-consolidation/2026-06-07.md`
- Audit desta correção: `reports/governance/memory-hot-daily-audit-2026-06-07.md`
- Cobertura de boot memory: `areas/operacoes/runtime/hermes-profile-memory-coverage.md`
- Watchdog latest: `reports/memory-hygiene/latest.json`

## Próxima revisão

Atualizar no fechamento diário ou sempre que Lucas corrigir uma prioridade/decisão que afete execução contínua.
