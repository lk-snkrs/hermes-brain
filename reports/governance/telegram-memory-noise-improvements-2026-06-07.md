# Telegram + Memory hygiene improvements — 2026-06-07

Escopo: continuidade aprovada por Lucas após priorização de melhoria em Telegram limpo, memória/Brain confiável e rotinas silenciosas. Operação local/governança; sem Docker, VPS, Traefik, gateway, provider, secrets ou integrações externas.

## Mudanças aplicadas

### 1. Boot memory default compactada

A memória global injetada do perfil default estava visivelmente perto do limite na sessão atual (`MEMORY` ~98%). Foram compactadas entradas estáveis para manter só boot mínimo, guardrails e ponteiros canônicos.

Resultado informado pelo memory tool após a última substituição:

- `MEMORY`: 1.584 / 2.200 chars = 72%.
- `entry_count`: 10.
- Padrão preservado: Brain como memória rica; boot memory como índice/guardrails.

Observação: a memória injetada nesta conversa continua mostrando o snapshot antigo até nova sessão, pois Hermes congela memory no início da sessão.

### 2. Correção: Relatório Hermes Diário é Telegram obrigatório

Eu havia movido temporariamente o cron `98478b820720` para `deliver=local`, mas Lucas corrigiu explicitamente por voz: esse relatório diário é importante para entender o que aconteceu e deve sempre ir para o Telegram.

Correção aplicada imediatamente:

- Cron: `98478b820720`.
- Nome atual: `Relatório Hermes diário 01h+02h+02h15 para Lucas — Telegram obrigatório`.
- `deliver=origin` restaurado.
- Próxima execução preservada: `2026-06-08T05:30:00+00:00`.

Regra durável registrada em memória de usuário: o Relatório Hermes Diário 01h+02h+02h15 é exceção obrigatória à política de Telegram limpo e deve sempre ser enviado no Telegram.

### 3. Superfícies Telegram preservadas

Após a correção, as superfícies `origin` relevantes incluem:

- `Relatório Hermes diário 01h+02h+02h15 para Lucas — Telegram obrigatório`.
- `Mesa COO diária Telegram`.
- `Hermes multi-profile latency watchdog`.
- `Hermes all Telegram gateways watchdog`.

## Verificação executada

- `cronjob update`: confirmou `deliver=origin` no cron `98478b820720`.
- `memory replace`: registrou a preferência durável do Lucas.

## Não-ações

- Não alterei Docker/VPS/Traefik/SSH/containers.
- Não reiniciei gateways, providers, webhooks ou API server.
- Não toquei em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail.
- Não copiei nem imprimi secrets.

## Próxima melhoria recomendada

Para reduzir ruído sem quebrar a regra do relatório obrigatório, o caminho correto agora é melhorar o conteúdo do Relatório Hermes Diário — mais curto, atual e acionável — e não removê-lo do Telegram.
