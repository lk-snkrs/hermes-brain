# QVNtnC Checkout Concierge — model splits + Hash flow exit learning

Data: 2026-06-11
Contexto: Lucas perguntou se devemos criar mais splits por modelos e pediu para aprender com o flow Hash sobre o que acontece quando a pessoa compra.

## Fonte read-only usada

- Flow original: `QVNtnC` — `Hash - Abandonment Checkout`
- Status: `live`
- Readback sanitizado: `receipts/2026-06-10T183607Z-klaviyo-flow-QVNtnC-definition-readonly.json`
- Writes externos: `0`

## Aprendizado do Hash flow

O Hash usa controle global de saída/entrada via `profile_filter`, não apenas copy nos emails.

Pontos observados:

1. Trigger do flow: métrica de checkout (`UXafgs` no readback; tratado operacionalmente como Started Checkout / abandono de checkout).
2. Filtro de perfil para compra:
   - condição `profile-metric` sobre métrica `VAbhT5`;
   - `measurement=count`;
   - `operator=equals`;
   - `value=0`;
   - `timeframe_filter.operator=flow-start`.
3. Interpretação operacional: a pessoa só deve continuar no flow se tiver `0` eventos da métrica de compra desde que entrou no flow. Se comprar depois de entrar, não deve seguir recebendo os próximos emails de abandono.
4. Reentrada atual observada no Hash: `7 day`.

## Regra obrigatória para o novo Checkout Concierge

Antes de ativar qualquer versão nova, replicar/validar a lógica do Hash:

- Flow/profile filter: `Placed Order` desde o início do flow = `0`.
- Reentrada: definir conscientemente; recomendação LK Content: 14–30 dias se quisermos reduzir excesso, ou manter 7 dias se quisermos paridade com Hash.
- Consent/suppression: validar dentro do Klaviyo antes de ativação.
- Não usar estoque/pronta entrega/disponibilidade como condição sem lk-stock.

## Resposta estratégica sobre mais splits

Sim, faz sentido criar mais splits por modelo, mas com limite operacional.

Recomendação para v1:

1. New Balance 9060 — já planejado.
2. New Balance 530 — já planejado.
3. Onitsuka Tiger Mexico 66.
4. Onitsuka Tiger Mexico 66 Sabot.
5. Nike Vomero / Vomero Premium.
6. Nike Mind 001 / Mind 002.
7. Adidas terrace / low-profile se o volume justificar: Samba, Gazelle, Campus, Taekwondo, SL 72.
8. Fallback curadoria LK.

## Como ordenar os splits

A ordem ideal deve vir de ranking por família/modelo em 90 dias, retornado por `[LK] Estoque Loja Física` / `lk-stock`, porque envolve vendas/modelos. LK Content não deve assumir ranking final sem esse retorno.

Enquanto o ranking não vem, usar ordem estratégica provisória:

1. 9060
2. 530
3. Mexico 66
4. Mexico 66 Sabot
5. Vomero / Vomero Premium
6. Nike Mind 001/002
7. Adidas terrace / outros
8. fallback

## Estrutura mantida

A arquitetura continua com 3 emails:

1. Email 1 universal.
2. Email 2 branchado por modelo/família, com produto + CTA cedo.
3. Email 3 comercial/10% compartilhado ou adaptado por branch.

Não reintroduzir quarto email.

## Gate de Klaviyo

Não ativar nem migrar sem dupla confirmação. Montagem no Klaviyo UI deve permanecer em draft/manual até readback final.
