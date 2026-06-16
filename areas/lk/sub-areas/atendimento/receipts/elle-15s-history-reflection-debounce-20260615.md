# Receipt — Elle 15s debounce + histórico antes de responder

- Data/hora UTC: 2026-06-15T15:14Z
- Área: LK / Atendimento / Elle / Chatwoot
- Pedido humano: corrigir Elle para não responder imediatamente por mensagem isolada; esperar 15 segundos após a última mensagem do cliente, usar histórico da conversa, refletir via Gemini/modelo configurado e só então responder ou transbordar.
- Classificação: produção aprovada pelo responsável; alteração no bot Elle; sem envio de teste para cliente real.

## Diagnóstico

- Raiz encontrada em `/opt/elle-chatwoot/app.py`: o webhook `message_created` processava cada inbound imediatamente, chamando `classify(flat)` e depois `apply_actions(...)` no mesmo request.
- Embora a Elle já buscasse histórico em alguns pontos, não havia uma janela de fala/debounce por conversa. Isso fazia a decisão depender demais da última mensagem individual, sem aguardar sequência curta do cliente.

## O que foi alterado

- Adicionado debounce por conversa:
  - `ELLE_DEBOUNCE_ENABLED=true` por padrão;
  - `ELLE_DEBOUNCE_SECONDS=15` por padrão.
- Fluxo novo:
  1. Webhook recebe mensagem inbound elegível.
  2. Cancela timer anterior da mesma conversa, se existir.
  3. Agenda processamento para 15s depois da última mensagem.
  4. No disparo do timer, busca histórico vivo no Chatwoot.
  5. Monta `customer_burst` com as últimas mensagens consecutivas do cliente desde a última saída pública.
  6. Envia ao classificador/Gemini o histórico recente + bloco agrupado do cliente.
  7. Se puder responder com segurança, responde; se não puder, faz transbordo conforme guardrails.
- Prompt atualizado para instruir explicitamente a reflexão sobre conversa inteira, histórico recente e bloco agrupado do cliente, sem interpretar linha isolada.
- Preservados os guards existentes:
  - human takeover lock;
  - duplicate public reply guard;
  - estoque/pronta-entrega/loja física para Larissa/lk-stock;
  - sensíveis/pedido problemático para Larissa;
  - sem prometer estoque, reserva, prazo, preço negociado ou desconto.

## Verificação

- `python3 -m py_compile app.py`: OK.
- Teste sintético sem cliente real:
  - duas chamadas rápidas na mesma conversa geraram somente 1 processamento final;
  - conteúdo final agrupado incluiu 3 linhas de mensagens do cliente;
  - `debounced=true`;
  - `history_message_count=4`;
  - `values_printed=false`.
- Teste sintético de transbordo:
  - bloco recente com “loja física” + produto/tamanho gerou `handoff=true`;
  - categoria `stock_handoff`;
  - resposta menciona Larissa;
  - não prometeu disponibilidade/estoque/reserva.
- Rebuild/recreate:
  - `docker compose up -d --no-deps --build --force-recreate elle-chatwoot` concluído;
  - container `elle-chatwoot` ativo.
- Health público via Traefik:
  - `ok=true`;
  - `dry_run=false`;
  - `write_enabled=true`;
  - `kill_switch=false`;
  - `public_reply_enabled=true`;
  - `ai_enabled=true`;
  - `ai_model=google/gemini-2.5-flash`;
  - `ai_secret_present=true`;
  - `debounce_enabled=true`;
  - `debounce_seconds=15.0`.

## Rollback

- Backup antes da alteração salvo em `/opt/elle-chatwoot/backups/lucas-debounce-history-20260615T151009Z/app.py`.

## Segurança

- Nenhum telefone, e-mail, URL de conversa, token, secret ou conteúdo sensível de cliente foi registrado neste receipt.
- Testes foram sintéticos/no-send; não houve mensagem de teste enviada a cliente real.
