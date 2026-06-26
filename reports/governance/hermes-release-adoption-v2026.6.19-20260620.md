# Hermes release adoption — v2026.6.19

Data: 2026-06-20
Fonte: GitHub Releases (`NousResearch/hermes-agent`), via preflight/release probe e leitura da release.
Runtime atual observado: Hermes Agent v0.16.0 (2026.6.5).
Valores impressos: `values_printed=false`.

## Classificação

Status: **P2 approval-needed para runtime upgrade; P1 para adoção documental/read-only**.

A release nova (`v2026.6.19`, Hermes v0.17.0) é oportunidade, não incidente. Nenhuma troca de runtime, Docker, gateway ou deploy foi executada por este cron.

## Matriz de adoção

| Tema | Classificação | Próxima ação segura |
| --- | --- | --- |
| Background/async subagents | P1 workflow/Brain improvement | Mapear para rotinas de trabalho longo e reduzir pedidos repetidos de “seguir”, sem ativar runtime novo. |
| Automation Blueprints | P1 workflow/Brain improvement | Comparar com crons/no_agent existentes e transformar em checklist local se houver ganho. |
| Desktop/app/superfícies | P2 approval-needed | Manter Dashboard/Telegram como padrão até Lucas aprovar avaliação de superfície. |
| iMessage/Photon e novos canais | P2 approval-needed | Não ativar canais novos sem pacote de risco, rollback e destino. |
| Image editing/tooling | P1/P2 conforme demanda | Documentar como capacidade opcional; uso em cliente/publicação exige aprovação de artefato. |
| Runtime upgrade v0.17 | A3 approval-gated | Preparar pacote paralelo com backup, testes e rollback antes de qualquer troca. |

## Guardrails

- Sem upgrade automático.
- Sem restart de gateway.
- Sem Docker/VPS/Traefik/runtime mutation.
- Sem secrets impressos ou copiados.
- Sem criação/alteração de cron.

## Decisão recomendada

Preparar, em momento separado, um pacote de upgrade v0.17 com validação de regressões Lucas-facing: Telegram clean delivery, inline buttons, context compression, model fallback, Memory OS, Reminder OS, profile watchdogs e Brain Health.
