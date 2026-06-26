# Handoff — LC Hermes ensinar uso do browser CDP a todos os agentes

Status: pronto / broadcast documental aplicado

## Pedido de Lucas

“Ensine o LC Hermes e peça para ensinar todos os agentes como usar.”

## O que foi ensinado

- Skill canônica: `skills/hermes-browser-cdp/SKILL.md`
- Protocolo canônico: `governance/protocols/browser-cdp-hermes-playwright.md`
- Bloco operacional adicionado em:
  - `AGENTS.md`
  - `agentes/hermes-geral/AGENTS.md`
  - `agentes/lc-claude-cli/AGENTS.md`
  - `agentes/lk/AGENTS.md`
  - `agentes/lk-otimizacao-colecao/AGENTS.md`
  - `agentes/mordomo/AGENTS.md`
  - `agentes/spiti/AGENTS.md`
  - `agentes/zipper/AGENTS.md`

## Instrução para LC Hermes / Hermes Geral

Ao iniciar sessão ou rotear tarefas que possam exigir browser:

1. Carregar `hermes-browser-cdp`.
2. Ensinar/relembrar o agente executor que:
   - acesso humano é `https://web.lucascimino.com`;
   - endpoint CDP privado é `http://lk-browser-web:9223`;
   - CDP é privado, nunca público;
   - login/captcha é feito por Lucas;
   - writes externos exigem aprovação explícita, rollback e receipt.
3. Se um agente novo for criado, copiar o bloco `HERMES_BROWSER_CDP_PROTOCOL` para o `AGENTS.md` dele ou referenciar a skill no boot.
4. Não registrar senha, cookies, localStorage, tokens ou headers sensíveis.

## Validação técnica disponível

Receipt de implantação CDP:

`areas/lk/sub-areas/growth/receipts/browser-docker/web-lucascimino-cdp-linked-20260606T133536Z/`

Receipt desta disseminação:

`areas/lk/sub-areas/growth/receipts/browser-docker/hermes-browser-cdp-teach-all-agents-20260606T134203Z/`
