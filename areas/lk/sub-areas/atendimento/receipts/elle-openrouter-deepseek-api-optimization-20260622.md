# Elle — OpenRouter/DeepSeek API optimization

Data: 2026-06-22 UTC
Perfil: lk-ops
Escopo aprovado por Lucas: aplicar as adaptações recomendadas para aproveitar melhor `deepseek/deepseek-v4-pro` via OpenRouter.

## Alterações aplicadas

- Separação de mensagens OpenRouter em `system` + `user`.
  - `system`: identidade/guardrails duros da Elle/LK, JSON-only, proibição de prometer estoque/disponibilidade/reserva/desconto/prazo/decisão financeira.
  - `user`: prompt operacional existente com dados sanitizados da conversa.
- Troca de `max_tokens` para `max_completion_tokens` no payload OpenRouter.
- Inclusão de `session_id` por conversa/purpose: `elle-chatwoot-<purpose>-<conversation_id>`.
- Inclusão de `reasoning_effort='low'` para OpenRouter/DeepSeek.
- Timeout OpenRouter ajustado para mínimo efetivo de 15s via `OPENROUTER_TIMEOUT_SECONDS`, sem alterar fallback Anthropic/Gemini.
- Log sanitizado de erro de provider com `provider`, `model`, `conversation_id`, `purpose`, `error_type`; sem secrets.
- Log/metadata sanitizados de modelo real e latência quando OpenRouter retorna JSON válido.
- Healthz agora expõe `openrouter_timeout_seconds` e `openrouter_reasoning_effort`.

## Deploy/persistência

- Backup runtime antes do patch: `/opt/data/backups/elle-chatwoot/20260622T011233Z-deepseek-openrouter-params/app.py.before`
- App pós-patch salvo em: `/opt/data/backups/elle-chatwoot/20260622T011233Z-deepseek-openrouter-params/app.py.after`
- SHA256 before: `5afa520bfa0d34003b5756674c755f4ed61ae6427cb8a22a759d5ea6d310a025`
- SHA256 after: `afb8cc839a2f5463875c9b3379d51f73cbcb6d8e1b471c3a19f9651f83f867d3`
- Runtime atualizado via `docker cp` para `/app/app.py` no container `elle-chatwoot`.
- Container reiniciado.
- Imagem commitada para reduzir risco de perda do hotpatch: `elle-chatwoot-elle-chatwoot:latest` = `sha256:c4335f80f9f1f851abaeddbd6ba81ddc5f22e352041cdd003b1e6a509e999567`.

Observação: o label Docker ainda aponta compose source `/opt/elle-chatwoot/docker-compose.yml`, mas esse diretório não estava presente no filesystem local no momento da aplicação. Por isso, não foi feito `docker compose up --build`; a persistência possível nesta janela foi runtime + commit da imagem local. Recomenda-se reconstruir/normalizar o diretório fonte da Elle em uma manutenção separada antes do próximo rebuild via compose.

## Verificação executada

1. `python3 -m py_compile /app/app.py` dentro do container: OK.
2. Smoke real OpenRouter com `system/user`, `max_completion_tokens`, `reasoning_effort=low`, `session_id`: OK.
   - provider: `openrouter`
   - modelo retornado: `deepseek/deepseek-v4-pro-20260423`
   - JSON parseado: OK
   - latência capturada: OK
3. Healthz dentro do container:
   - `ok=true`
   - `ai_provider=openrouter`
   - `ai_model=deepseek/deepseek-v4-pro`
   - `openrouter_timeout_seconds=15.0`
   - `openrouter_reasoning_effort=low`
   - `ai_secret_present=true`
   - `public_reply_enabled=true`
   - `write_enabled=true`
   - `kill_switch=false`
4. Smokes determinísticos de classificação com IA desabilitada no módulo importado:
   - pós-venda/entrega atrasada → `human_handoff`: OK
   - loja física/tamanho/estoque → `stock_handoff`: OK
   - home/site genérico → `product_clear`: OK
5. Logs recentes:
   - Docker stdout recente sem erro.
   - Eventos recentes `ai_provider_error`: 0.

## Guardrails preservados

- Aviso de IA em aprendizado preservado.
- Estoque/pronta entrega continua transbordando para Larissa/lk-stock; sem promessa de disponibilidade.
- Fallback Anthropic/Gemini preservado.
- Nenhum secret impresso neste receipt.
