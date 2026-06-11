# Telegram Delivery / UX Governance — Decisions and Guardrails

## Decisão Brain OS

Criar um hub canônico para reduzir ambiguidade entre documentação histórica, configuração, runtime vivo e ação externa.

## Guardrails

1. Telegram deve receber alertas acionáveis: atual diferente do histórico, exceção/falha/decisão, gatilho e ação clara.
2. Sucesso normal de rotina Brain/Mordomo/COO deve ser silent-OK salvo pedido explícito.
3. Não enviar mensagem externa, campanha, follow-up, customer-facing ou supplier-facing sem fonte/aprovação do domínio.
4. UX não deve expor job_id, JSON bruto, wrappers internos ou ruído de fallback benigno recuperado.
