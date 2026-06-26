# Skill Quality Critical Wave — 2026-06-14

## Pedido

Lucas disse: "Seguir" após a recomendação de uma wave curta de skill-quality focada em governança/runtime/memória.

## Escopo

Classificação: A1 local/documental/skill-quality.

Guardrails:

- Sem runtime, Docker, VPS, Traefik, gateway, restart ou container.
- Sem alteração de cron schedule/delivery/enabled/state.
- Sem integração externa, banco, Shopify, Tiny, GMC, Klaviyo, Meta, WhatsApp ou e-mail.
- Sem secrets impressos; `values_printed=false`.

## Alvos escolhidos

Skills críticas de alto impacto para futuras respostas/autoheals:

1. `hermes-agent`
2. `hermes-brain-governance`
3. `lucas-hermes-continuous-improvement`

## Problemas objetivos corrigidos

- Descrições de skill que não começavam com `Use when...`, reduzindo precisão de trigger.
- `hermes-brain-governance` tinha cabeçalho duplicado `Session references added:`.
- `hermes-brain-governance` tinha duplicação literal da referência `Memory hot/daily audit + refresh`.
- A melhoria de daily-learning JSON hardening estava registrada em referência, mas ainda sem ponte explícita no `SKILL.md` principal de governança.
- `lucas-hermes-continuous-improvement` tinha frontmatter mínimo sem `author`, `license`, `metadata.tags` e `related_skills`.
- Faltava uma referência curta ligando o protocolo de melhoria contínua ao padrão de transformar falhas recorrentes em validator + regressão + receipt.

## Mudanças aplicadas

- `hermes-agent/SKILL.md`
  - descrição alterada para trigger padrão: `Use when configuring, extending, troubleshooting, or contributing to Hermes Agent itself.`

- `hermes-brain-governance/SKILL.md`
  - descrição alterada para trigger padrão `Use when...`;
  - removido cabeçalho duplicado;
  - removida referência duplicada de `Memory hot/daily audit + refresh`;
  - adicionado ponteiro para `references/daily-learning-json-hardening-20260614.md`.

- `lucas-hermes-continuous-improvement/SKILL.md`
  - descrição alterada para trigger padrão `Use when...`;
  - frontmatter enriquecido com `author`, `license`, `metadata.tags` e `related_skills`;
  - princípio 7 agora aponta para `references/daily-learning-hardening-continuation-20260614.md`.

- Nova referência:
  - `/opt/data/skills/devops/lucas-hermes-continuous-improvement/references/daily-learning-hardening-continuation-20260614.md`

## Auditoria pós-mudança

Checados 5 artefatos de skill/referência:

- `frontmatter=true` nos 3 `SKILL.md` alterados.
- `description_starts_use_when=true` nos 3 `SKILL.md` alterados.
- `hermes-brain-governance`:
  - `Session references added:` = 1
  - `Memory hot/daily audit + refresh` = 1
  - ponteiro daily-learning = presente
- `lucas-hermes-continuous-improvement`:
  - ponteiro daily-learning = presente

## Verificações

Verificações finais registradas no receipt desta wave.

## Resultado

A wave reduziu ruído/duplicação e melhorou a capacidade de descoberta correta das skills críticas sem tocar runtime nem produção. A próxima wave natural é escolher outro lote pequeno de skills críticas ou atacar testes determinísticos de approval-packet/Telegram-noise.
