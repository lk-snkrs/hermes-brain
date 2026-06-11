# MCP / Tooling Activation Governance — Decisions and Guardrails

## Decisão Brain OS

Criar um hub canônico para reduzir ambiguidade entre documentação histórica, configuração, runtime vivo e ação externa.

## Guardrails

1. MCP/tool activation só está completo quando configurado, descoberto, exposto em toolsets e documentado com guardrails.
2. Não instalar, autenticar ou habilitar MCP server como parte deste hub documental.
3. Ferramenta com capacidade de write externo herda approval gate do domínio de negócio.
4. Registrar falhas como ausência de secret, server indisponível, toolset não exposto ou wrapper read-only, sem inventar disponibilidade.
