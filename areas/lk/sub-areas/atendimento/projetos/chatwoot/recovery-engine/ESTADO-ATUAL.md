# Estado Atual — Motor de Recuperação

Snapshot: `2026-06-10` (fim da sessão "audit + corrigir tudo")

## Produção
- Imagem: **`lk-chatwoot:v2-recovery17`** (rollback: v2-recovery16/15). Fonte com git: 4 commits (checkpoint → audit fixes → interpolação → fix interpolação).
- Migração `recovery_event_logs` aplicada.

## Interruptores (decisão Lucas 10/jun: TUDO DESLIGADO, pronto pra ligar)
| Chave | Valor | Para ligar |
|---|---|---|
| SHOPIFY_RECOVERY_ENABLED | **false** | `true` + trocar delays |
| SHOPIFY_RECOVERY_DELAYS | **1,2,3 (demo!)** | `60,1440,2880` |
| SHOPIFY_NOTIFY_ENABLED | **false** | `true` |
| SHOPIFY_FOLLOWUP_DELAY_MINUTES | **2 (demo!)** | sugerido `4320` (3d) |

## Templates (preenchidos e TESTADOS 10/jun — teste real no número do Lucas, conv #557, perfeito)
Biblioteca `nome :: texto` com 8 entradas: `carrinho_1h`, `carrinho_24h`, `carrinho_48h`, `pedido_criado`, `pedido_aprovado`, `pedido_enviado`, `pedido_entregue`, `pos_venda`. Tom LK ("Less Noise, More Identity": sem exclamação, sem urgência agressiva). Chaves das jornadas apontadas. Placeholders interpolados em runtime.

## WhatsApp
- Evolution "LK Flagship" (551123671467) `open`, bridge inbox #3. **Resposta de agente FUNCIONANDO** (consertada 10/jun — antes 100% perdida por webhook localhost/instância antiga "Pessoal").
- Cloud API oficial 5511949565000: no Crisp, travado em 2-step PIN (migração futura).
- Número +5511992055803 no WATI; marketing legado no BiteSpeed.

## Klaviyo
- Token rotacionado (forte, só header). 2 flows com webhook configurados pelo Lucas (10/jun): Checkout Started e Added to Cart → `https://chat.lkskrs.online/webhooks/klaviyo/1`. Sintaxe Django p/ campos $: `{{ event|lookup:'$value' }}`. Recomendado no Added to Cart: Wait 30-60min + filtro de saída.

## Números (audit 10/jun)
- 515 carrinhos em 7 dias · R$ 1,56M · ticket médio R$ 3.036 · 76 recuperados orgânicos (R$ 204,5 mil · 14,8%).
- **Gargalo nº1: 78,6% dos carrinhos sem telefone/email** (405/515).
- Contatos: 6.409 (99,9% E.164 ok, 0 duplicados) · 91,7% sync Shopify · RFM: champions 79 / vip 3.320 / loyal 246 / repeat 824 / one_timer 3.836 / winback 3.877 (sobrepostos).

## Incidente 10/jun (resolvido, lição registrada)
6 clientes receberam mensagens "(vazio)"/vazias: (a) templates com placeholder literal "(vazio)" + régua ligada com delays demo → 3 toques pra 1 cliente; (b) SERVER_URL localhost → 5 contatos com msgs vazias de mídia. Lucas optou por NÃO enviar follow-up de desculpas. Causas raiz corrigidas (sanitização + guard + webhook + SERVER_URL).
