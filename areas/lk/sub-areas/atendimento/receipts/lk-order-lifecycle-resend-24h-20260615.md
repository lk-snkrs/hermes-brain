# Receipt — LK Chatwoot — reenvio pedido feito/pagamento aprovado últimas 24h

- Data/hora UTC: 2026-06-15T14:45:00Z
- Perfil: lk-ops
- Área: LK / Atendimento / Chatwoot / WhatsApp
- Pedido Lucas: reenviar mensagens de pedido feito e pagamento aprovado para quem falhou nas últimas 24h.
- Classificação: produção/write externo aprovado pelo pedido explícito do Lucas.
- PII/secrets: não persistidos neste receipt; IDs internos e finais de pedido sanitizados.

## Auditoria inicial

- Janela: últimas 24h a partir de 2026-06-14T14:23Z.
- Falhas públicas encontradas: 17.
- Templates originais com falha:
  - `lk_online_pedido_realizado_v1`: 9
  - `lk_online_pagamento_aprovado_v1`: 8
- Motivo inicial: botão URL obrigatório com parâmetro vazio / inválido.
- Shopify lookup: `order_status_url` encontrado para todos os 17 itens; valores não impressos.

## Tentativa com templates originais

- Foi aplicado hotfix no Chatwoot para transformar URL de pedido em parâmetro dinâmico de botão, evitando URL completa.
- Nova imagem: `lk-chatwoot:v2-recovery25-url-button-root-param-20260615`.
- Serviços recriados: `chatwoot-rails-1`, `chatwoot-sidekiq-1`.
- Health local depois do deploy: HTTP 200.
- Dry-run: parâmetro do botão presente e `param_starts_full_url=false`.
- Mesmo assim, a Meta retornou `132012` para os templates com botão, indicando incompatibilidade de formato do template aprovado na Meta.
- Ação segura tomada: parar reenvios com botão e usar templates aprovados sem botão.

## Reenvio final usando templates sem botão

Templates usados:
- Pedido feito: `lk_pedido_criado`
- Pagamento aprovado: `lk_pagamento_aprovado`

Resultado do readback após processamento:
- Total reenviado com templates sem botão: 17
- Sucesso Meta/WhatsApp: 16
  - Delivered: 14
  - Read: 2
- Falha restante: 1
  - Template: `lk_pedido_criado`
  - Erro Meta: `131026`
  - Interpretação operacional: conta/número indisponível para entrega; retry imediato não indicado.

## Observações de segurança

- Não foram impressos/persistidos telefones, e-mails, URLs completas de pedido/status, tokens ou secrets.
- Houve tentativas anteriores com templates originais que falharam antes de entrega (`source_id` ausente em falhas antigas; nas falhas com Meta, erro registrado). O reenvio efetivo entregue/lido foi via templates sem botão.
- O hotfix de botão permanece deployado para evitar URL completa; porém os templates originais com botão ainda precisam revisão/correção/aprovação na Meta antes de voltarem a ser usados para pedido/pagamento.

## Rollback / referências

- Compose backup: `/opt/chatwoot/docker-compose.yaml.bak-recovery25-url-button-root-param-20260615`
- Rollback do arquivo: `/root/chatwoot-rollbacks/url-button-root-param-*`
- Imagem anterior: `lk-chatwoot:v2-recovery24-template-button-guard-20260615`
- Imagem atual: `lk-chatwoot:v2-recovery25-url-button-root-param-20260615`

## Próximos passos recomendados

1. Manter templates sem botão para `pedido_criado` e `pagamento_aprovado` até corrigir/aprovar os templates online com botão na Meta.
2. Revisar `lk_online_pedido_realizado_v1` e `lk_online_pagamento_aprovado_v1` no Meta Template Manager: formato do botão dinâmico e exemplo aprovado.
3. Não tentar retry no item com `131026` sem nova evidência, pois tende a falhar por indisponibilidade do destino.
