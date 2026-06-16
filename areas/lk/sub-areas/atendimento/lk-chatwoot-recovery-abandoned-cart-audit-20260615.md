# LK Chatwoot Recovery — auditoria carrinho abandonado 2026-06-15

Data da auditoria: 2026-06-15 07:09 BRT.
Janela: últimas 24h desde 2026-06-14 07:09 BRT.
Fonte: Chatwoot Rails read-only no container `chatwoot-rails-1`.
PII/segredos: não impressos (`values_printed=false`).

## Resultado

Carrinho abandonado rodou parcialmente, mas não 100% com sucesso.

- Conversas recovery/carrinho abandonado tocadas: 12.
- Mensagens públicas outbound na janela: 17.
- Status:
  - `delivered`: 10.
  - `read`: 2.
  - `failed`: 5.
- Notas simuladas: 0.
- Checkouts com `touches_sent > 0` atualizados na janela: 8.
- Último outbound público recovery identificado na janela: 2026-06-14 21:52 BRT.

## Templates / status

- `lk_checkout_abandonado_30min_v2`: 4 delivered, 2 failed, 2 read.
- `lk_checkout_abandonado_24h_v2`: 1 delivered, 1 failed.
- `lk_checkout_abandonado_72h_v2`: 1 failed.
- `lk_carrinho_abandonado_30min_v1`: 1 failed.
- Sem metadata de template: 5 delivered.

## Falhas observadas

As falhas sanitizadas retornaram Meta:

> 131049: This message was not delivered to maintain healthy ecosystem engagement.

Interpretação: a automação tentou enviar, o payload/template chegou ao fluxo, mas parte dos envios foi bloqueada pela Meta por limite/saúde de ecossistema. Não é erro de parâmetro `132000` nesta janela.

## Conclusão operacional

Não dizer “rodou com sucesso total”. Dizer: rodou e teve entregas/leitura, mas houve 5 falhas Meta `131049`; precisa monitorar/diagnosticar antes de considerar 100% saudável.
