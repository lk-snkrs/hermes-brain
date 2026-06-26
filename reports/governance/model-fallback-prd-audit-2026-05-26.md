# Audit — PRD de fallback/model router Hermes

Data: 2026-05-26
Escopo: Hermes Geral, Mordomo, LK Growth, LK Ops, LK Shopify, LK Trends, SPITI
Tipo: read-only/local; sem restart, sem cron mutation, sem writes externos

## Artefato auditado

- `/opt/data/areas/hermes/performance/prd-resposta-rapida-trabalho-profundo-toolsets-watchdog-2026-05-26.md`

## Veredito executivo

O PRD está conceitualmente correto e a maior parte já evoluiu de "proposta" para "configurado/ativo" nos perfis principais. A separação entre fast lane e trabalho profundo está correta.

A principal lacuna não é o roteamento simples: esse está configurado e há evidência em logs. A lacuna é semântica de fallback/cooldown: o runtime possui fallback por cadeia, mas não exatamente a política prometida no PRD de "timeout 300s + 2–3 falhas + cooldown por modelo/provedor" para todo tipo de falha.

## Estado observado

### Configs

Todos os configs auditados têm:

- `model.provider: openai-codex`
- `model.default: gpt-5.5`
- `smart_model_routing.enabled: true`
- `smart_model_routing.cheap_model: openai-codex/gpt-5.4-mini`
- `max_simple_chars: 220`
- `max_simple_words: 36`
- `fallback_providers` com 1 entrada para `openai-codex/gpt-5.4-mini`

Perfis auditados:

- Hermes Geral
- Mordomo
- LK Growth
- LK Ops
- LK Shopify
- LK Trends
- SPITI

### Runtime vivo

Processos vivos confirmados por `HERMES_HOME` + `hermes gateway run`:

- Hermes Geral: vivo
- LK Growth: vivo
- Mordomo: vivo
- SPITI: vivo

Configurados, mas não vivos no momento do audit:

- LK Ops
- LK Shopify
- LK Trends

### Evidência de router nos logs

Logs recentes mostram linhas de seleção do modelo leve em perfis vivos:

- Hermes Geral: sim
- Mordomo: sim
- LK Growth: sim
- SPITI: sim
- LK Shopify: havia evidência anterior, mas profile não estava vivo no momento

LK Ops/LK Trends não tinham evidência recente de cheap-route porque não estavam vivos.

## Avaliação do PRD

### Correto

1. Separação fast lane vs deep work está correta.
2. `gpt-5.5` permanece como forte/default.
3. `gpt-5.4-mini` está aplicado como caminho leve para turns simples.
4. Heurística é conservadora: URLs, código, auditoria, pesquisa, deploy, cron, watchdog, PRD, config etc. ficam no caminho forte.
5. Toolsets por especialista estão coerentes com o PRD.
6. Watchdog é read-only e silent-OK por design.
7. O filtro recém-adicionado que ignora fallback de IP do Telegram está correto.

### Parcial / precisa ajuste de texto

1. O PRD ainda descreve `smart_model_routing.enabled=false` e `fallback_providers` vazio como estado observado inicial. Isso ficou desatualizado: agora estão `true` e preenchidos.
2. O PRD fala em "fallback automático se não responder até 300s". O runtime tem stale-call/timeout e fallback chain, mas a ativação de fallback ocorre claramente para rate-limit/billing/NouS guard e falhas classificadas; não está provado como garantia universal de timeout 300s em todos os caminhos.
3. O PRD fala em cooldown após 2–3 falhas. O runtime tem cooldown curto para rate-limit/billing ao deixar o primary, mas não há política genérica de 2–3 falhas por modelo/provedor com métrica persistida.
4. `fallback_providers` usa o mesmo provider (`openai-codex`) com outro modelo. Isso ajuda latência/capacidade do modelo, mas não é fallback real de provedor se o problema for auth/provider inteiro.
5. LK Ops/LK Shopify/LK Trends devem ser reportados como "configurados" e não "ativos" até gateway vivo + log pós-start.
6. O watchdog quando executado com `python3` do sistema não tem PyYAML e por isso imprime `modelo=unknown/unknown`; precisa rodar na venv do Hermes ou ter fallback parser sem PyYAML.

## Achados técnicos

### Router

Implementação relevante: `/opt/hermes/gateway/run.py`

- `_resolve_turn_agent_config()` carrega `smart_model_routing` por turno.
- `_is_simple_model_routing_turn()` aplica heurística conservadora.
- A seleção é registrada como `Smart model routing selected cheap model: ...`.

Conclusão: router simples está implementado de forma coerente com o PRD.

### Fallback

Implementação relevante: `/opt/hermes/run_agent.py`

- `fallback_providers` vira `_fallback_chain`.
- `_try_activate_fallback()` troca provider/model/client in-place.
- `_restore_primary_runtime()` restaura primary por turno, exceto enquanto houver cooldown de rate-limit.
- Há cooldown de 60s para rate-limit/billing ao sair do primary.

Conclusão: fallback existe, mas a política do PRD deve ser reescrita para refletir o que existe hoje e separar o que ainda é backlog.

### Watchdog

Implementação relevante: `/opt/data/scripts/hermes_profile_latency_watchdog.py`

Pontos bons:

- silent-OK;
- read-only;
- lê logs por perfil;
- separa fallback de modelo/provedor de fallback de IP do Telegram.

Ponto a corrigir:

- rodando com `/usr/bin/python3`, `yaml` não está instalado; o watchdog não consegue ler modelo/fallback do config e mostra `unknown/unknown`.

Correção recomendada sem risco:

- executar o cron com a venv do Hermes: `/opt/hermes/.venv/bin/python /opt/data/scripts/hermes_profile_latency_watchdog.py`; ou
- adicionar parser YAML mínimo/fallback para `model.provider`, `model.default` e `fallback_providers` sem depender de PyYAML.

## Recomendações

### P0 — documentação/status

Atualizar o PRD para separar três estados:

1. planejado originalmente;
2. configurado agora;
3. comprovado em runtime.

Não dizer "ativo em todos" enquanto LK Ops/LK Shopify/LK Trends não estiverem vivos e verificados.

### P1 — watchdog

Corrigir a execução do watchdog para usar Python da venv ou remover dependência de PyYAML. Isso evita alertas com `modelo=unknown/unknown`.

### P1 — fallback semantics

Criar uma pequena especificação técnica para o fallback real:

- quais classes de erro disparam fallback imediatamente;
- quais classes só fazem retry;
- timeout/stale-call dispara fallback em qual caminho;
- cooldown por provider/model persistido ou em memória;
- métrica por perfil/modelo/provedor.

### P2 — fallback de provedor real

Considerar uma segunda entrada de fallback em provider diferente, somente depois de validar credenciais e custo/qualidade. Hoje o fallback é modelo leve no mesmo provider, útil para latência, mas não cobre queda/entitlement/auth do provider inteiro.

### P2 — ativação dos perfis dormentes

LK Ops, LK Shopify e LK Trends estão preparados, mas precisam de ativação/verificação separada se Lucas quiser runtime vivo.

## Status final

- PRD conceitualmente correto: sim.
- Router simples configurado: sim.
- Router simples comprovado em runtime: sim para perfis vivos; pendente para dormentes.
- Fallback configurado: sim.
- Fallback/cooldown conforme PRD: parcialmente; precisa especificar/implementar as lacunas.
- Watchdog: funcional, mas precisa corrigir ambiente Python/YAML para exibir modelo/fallback corretamente.
