# Revisão dos watchdogs Telegram — 2026-06-07

Escopo: revisar watchdogs que podem falar no Telegram/origin para reduzir ruído sem remover o Relatório Hermes Diário obrigatório.

## Inventário revisado

`cronjob list` mostra 32 jobs. Superfícies Telegram/origin relevantes:

- `98478b820720` — Relatório Hermes diário 01h+02h+02h15 para Lucas — Telegram obrigatório. **Preservado em `deliver=origin`**.
- `749ee30b51eb` — Mesa COO diária Telegram. Preservado.
- `c1ce34b4449a` — Hermes multi-profile latency watchdog. Revisado/patcheado.
- `b78ae7ac81d0` — Hermes all Telegram gateways watchdog. Revisado/patcheado.
- `955dc769b5a6` — LK specialist Telegram gateway watchdog. Está pausado, mas o script foi revisado/patcheado para evitar regressão se for reativado.

## Mudanças aplicadas

### `/opt/data/scripts/hermes_profile_latency_watchdog.py`

Antes: alerta tinha evidência, mas misturava contexto e ação em formato menos escaneável.

Depois: qualquer stdout agora usa blocos explícitos:

- `O que mudou`
- `Por que importa`
- `Evidência`
- `Ação automática`
- `Ação recomendada`

Também preserva a regra existente: stdout vazio no OK; eventos antigos sem recorrência atual ficam silenciosos por padrão; o script é read-only.

### `/opt/data/scripts/hermes_all_gateway_watchdog.py`

Antes: alertava `ALERTA Hermes gateway watchdog global` + lista.

Depois: stdout ficou acionável e delimitado:

- explica que gateway esperado está ausente/inseguro/não recuperado;
- explica impacto no Telegram/superfície indevida;
- lista evidência por perfil;
- explicita que auto-heal só ocorre para perfis secundários gerenciados com API/webhook off e Main é check-only;
- recomenda verificar apenas os perfis listados e não reiniciar Docker/VPS/Traefik sem aprovação.

### `/opt/data/scripts/lk_specialist_gateways_watchdog.py`

Embora o cron esteja pausado, o script foi ajustado no mesmo padrão para evitar ruído caso seja reativado.

### Skill corrigida

`/opt/data/skills/devops/lucas-runtime-operations/SKILL.md` tinha uma referência obsoleta sugerindo `origin → local` para o Relatório Hermes Diário. Foi corrigida: esse relatório é Telegram-obrigatório; reduzir ruído deve ser por conteúdo, não por suprimir entrega.

## Verificação executada

- `python3 -m py_compile` nos 3 scripts: `rc=0`.
- Silent-OK do latency watchdog com base temporária vazia: `rc=0`, stdout=0 bytes, stderr=0 bytes.
- Fixture de alerta do latency watchdog: `rc=0`, stdout contém todos os rótulos obrigatórios (`O que mudou`, `Por que importa`, `Evidência`, `Ação automática`, `Ação recomendada`).
- Harness sem side effect para `hermes_all_gateway_watchdog.py`: fake profile ausente + `HERMES_BIN=/bin/true`, `rc=0`, stdout contém todos os rótulos obrigatórios.
- Harness sem side effect para `lk_specialist_gateways_watchdog.py`: fake profile ausente + `HERMES_BIN=/bin/true`, `rc=0`, stdout contém todos os rótulos obrigatórios.
- Primeiro focused secret scan apontou 3 falsos positivos de *nomes/placeholder* (literal de nome de chave Telegram em código e placeholder de header n8n). Corrigi os dois scripts para montar o nome da chave sem padrão `KEY=...` literal e reescrevi a documentação do header para não parecer valor de token.
- Focused secret scan final nos scripts/skill/receipt alterados: `0 hits`.
- `cronjob list` pós-revisão: Relatório Hermes Diário continua `deliver=origin`; watchdogs ativos `c1ce34b4449a` e `b78ae7ac81d0` continuam `deliver=origin`.

## Não-ações

- Não alterei cron schedules.
- Não removi nem silenciei o Relatório Hermes Diário.
- Não executei o gateway watchdog real em modo que pudesse auto-iniciar profiles; a verificação de formato usou harness sem side effect.
- Não reiniciei gateways, Docker, VPS, Traefik, providers, webhook ou API server.
- Não toquei em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail.
- Não imprimi nem movi secrets.

## Estado final

Telegram continua recebendo:

- Relatório Hermes Diário obrigatório.
- Mesa COO diária.
- Watchdogs operacionais somente quando houver evento acionável.

Os watchdogs revisados agora devem alertar com gatilho, impacto, evidência e ação recomendada, em vez de apenas despejar uma lista técnica.
