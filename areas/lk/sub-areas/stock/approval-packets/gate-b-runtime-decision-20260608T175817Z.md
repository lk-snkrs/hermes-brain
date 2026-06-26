# Gate B — Decision Packet para Runtime Real

Criado em: 2026-06-08T17:58:17Z
Status: **aprovado e ativado em produção read-only em 2026-06-08T19:29:25Z**

## Decisão necessária

O Gate B local/offline/dry-run está validado e pode avançar apenas se Lucas aprovar explicitamente a ativação do runtime real.

Sem essa aprovação, o estado correto é manter:

- webhook público: **não ativado**;
- cron real: **não ativado**;
- gateway/bot: **não ativado**;
- writes Tiny/Shopify/fornecedor/cliente/campanha: **0**.

## Evidência local disponível

Comando executado em 2026-06-08T17:58:17Z:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 3.162s

OK
```

Cobertura local verificada anteriormente no runbook:

- schema SQLite sobe em banco temporário;
- ledger/eventos têm idempotência;
- webhook fixture duplicado vira `ignored`;
- cron dry-run sucesso marca `cron_diario`;
- cron dry-run falha marca `stale`;
- query A1 com `stale` declara `NÃO CONFIRMADO`;
- Telegram OK permanece silencioso;
- writes externos permanecem `0`.

## Escopo se aprovado

Ativar somente:

1. webhook read-only via `hermes-webhooks` no Vercel;
2. validação HMAC do provedor;
3. resign interno se necessário para Hermes;
4. cron diário read-only;
5. base local SQLite/cache operacional;
6. receipts de falha, divergência, P0 ou aprovação necessária;
7. Telegram silent-OK: só P0/falha/aprovação.

## Fora do escopo mesmo se aprovado

- compra automática;
- contato com fornecedor;
- contato com cliente;
- reserva/promessa de disponibilidade;
- Tiny write;
- Shopify inventory/product write;
- campanha/CRM/WhatsApp/Klaviyo;
- alertas de OK no Telegram.

## Secrets necessários — nomes, sem valores

- `SHOPIFY_WEBHOOK_SECRET_LK`
- `TINY_API_TOKEN_LK_READONLY` ou equivalente autorizado
- `HERMES_WEBHOOK_RESIGN_SECRET_LK_STOCK`
- `LK_STOCK_LOCAL_DB_PATH`

Os valores devem vir de Doppler/ambiente autorizado e nunca ser impressos no Brain, logs ou Telegram.

## Kill criteria

Pausar/desativar se ocorrer qualquer item:

1. HMAC falhando repetidamente.
2. Evento duplicado furando idempotência.
3. Algum caminho tentando escrever em Tiny/Shopify.
4. Base `stale` gerando afirmação de disponibilidade/ruptura sem fonte viva.
5. Telegram gerando ruído de OK/fallback benigno.

## Rollback

1. Pausar webhook/cron.
2. Manter banco local como evidência read-only.
3. Marcar snapshots como `stale`.
4. Voltar para Gate A/manual read-only com Tiny/fonte viva sob demanda.

## Frase exata para aprovação

> Aprovo ativar o runtime real do Gate B do `lk-stock`, usando `hermes-webhooks` no Vercel para os eventos listados e cron diário read-only, com HMAC, idempotência, kill criteria, rollback acima, Telegram silent-OK e zero writes Tiny/Shopify/fornecedor/cliente/campanha.

## Se não aprovar agora

Próximo passo seguro: manter Gate B local validado e desenhar o plano do Gate C em modo documental/offline, sem cron real e sem Telegram real.
