# Meta WhatsApp erro 131049 — pesquisa e ação recomendada

Data: 2026-06-15.
Escopo: LK Chatwoot Recovery / carrinho abandonado.

## Fonte oficial Meta

Página consultada: `https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes/`

Erro `131049`:

> This message was not delivered to maintain healthy ecosystem engagement.

Ação oficial Meta: se suspeitar que é limite, esperar pelo menos 24h antes de reenviar mensagem de template; reenviar durante o limite tende a retornar o mesmo erro.

Página consultada via requests: `https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits/`

Resumo oficial extraído: WhatsApp aplica limites por usuário para mensagens de template de marketing; se uma WABA tenta reenviar várias vezes em 24h para usuários que já atingiram o limite, entregas para esses usuários podem ficar indisponíveis por até 24h e o webhook retorna `failed` com código `131049`. Isso não afeta envios a outros usuários.

## Fontes complementares

- Dualhook: descreve `131049` como retenção/bloqueio de mensagem de marketing por cap adaptativo por usuário; não é necessariamente falha do número/conta; recomenda esperar, segmentar usuários engajados, espaçar envios e verificar categoria do template.
- Fyno: associa `131049`/healthy ecosystem a limites de marketing e necessidade de observabilidade por usuário/canal.

## Diagnóstico LK provável

Na auditoria do carrinho abandonado, houve 17 outbound públicos: 10 delivered, 2 read, 5 failed. Falhas foram `131049`, não `132000`/parâmetro de template.

Causa mais provável: limite/qualidade de entrega Meta para templates de marketing/abandoned-cart em alguns destinatários, por saturação/recent marketing exposure/baixo engajamento. Como parte entregou/leu, o motor e templates não parecem globalmente quebrados.

## Correção recomendada

1. Não fazer retry imediato dos 5 failed.
2. Marcar `131049` como `cooldown/suppressed` por pelo menos 24h por destinatário/template.
3. Reduzir cadência por usuário: evitar múltiplos templates de recovery no mesmo dia para quem já recebeu marketing/recovery.
4. Segmentar para maior intenção: priorizar carrinhos recentes/alto valor/usuários engajados e suprimir frios.
5. Revisar categorias dos templates: usar Utility só se o conteúdo for genuinamente transacional/utility; abandoned-cart promocional normalmente segue Marketing.
6. Monitorar taxa de failed por template e destinatário, separando `delivered/read` de `failed`.

## Observação

Não imprimir PII, checkout URLs ou tokens. Qualquer alteração de cadência/logic production exige aprovação explícita de Lucas.
