# Integração — Rivo / LK Rewards

Status: `mapped_pending_readonly_inventory`
Área: LK Sneakers / Customer Trust & Loyalty
Última atualização: 2026-05-13

## Papel no LK OS

Rivo deve ser tratada como possível engine operacional do **LK Rewards**: fidelidade, pontos/status, benefícios, referrals e comunicação de relacionamento.

Correção Lucas: LK Rewards não deve ser modelado como troca manual de pontos por desconto. O modelo desejado é **benefício automático por marco de gasto/status**, com tom premium/VIP.

## Fonte de dados

- `fact_rivo_loyalty`: dados confirmados pela Rivo/LK Rewards.
- `derived_loyalty_crm`: cruzamentos Shopify/Supabase/Klaviyo/Rivo para recompra, VIP e benefícios pendentes.
- `manual_approval`: qualquer configuração comercial aprovada por Lucas.
- `unknown`: regra não confirmada por API/admin/documento.

## Regras confirmadas por Lucas

- Nome do programa: **LK Rewards**.
- Pontuação-base: **1 ponto = R$1**.
- Modelo: tiers/marcos por gasto acumulado.
- Objetivo: recompras/margem + experiência premium/VIP.
- Exemplos iniciais:
  - R$5.000 de gasto acumulado → kit de limpeza Jason Markk.
  - R$15.000 de gasto acumulado → cupom de 15% + kit viagem.
- Expiração de pontos: ainda não definida.
- Aniversário: desejado, mas a LK ainda não capta data de aniversário no checkout.

## Credenciais / nomes seguros

Verificação Doppler `lc-keys/prd` em 2026-05-13, sem imprimir valores:

- Rivo dedicado: **não encontrado** (`RIVO_*` = 0).

Nomes candidatos a criar/verificar antes de API real:

- `RIVO_API_KEY`
- `RIVO_API_TOKEN`
- `RIVO_SHOP_ID`
- `RIVO_WEBHOOK_SECRET`

Não registrar valores neste arquivo.

## Inventário read-only necessário

Quando houver acesso/API/admin:

1. Confirmar se Rivo suporta tiers/marcos por lifetime spend ou pontos acumulados.
2. Confirmar se consegue disparar benefício automático sem exigir resgate manual pelo cliente.
3. Mapear entidades: member/customer, points, tier/status, reward/benefit, coupon, referral, activity/event.
4. Confirmar se Rivo lê lifetime spend do Shopify ou calcula saldo próprio.
5. Verificar se devoluções/cancelamentos subtraem pontos/gasto elegível.
6. Confirmar possibilidade de integração com Klaviyo para comunicação premium.
7. Confirmar suporte a birthday reward e onde a data precisa morar.

## Guardrails

Sem aprovação explícita de Lucas, Hermes não deve:

- criar/editar tier;
- alterar regra de pontos;
- criar cupom;
- conceder benefício;
- disparar e-mail/SMS/WhatsApp;
- escrever em Shopify/Rivo/Klaviyo/Notion/Supabase;
- prometer benefício a cliente;
- publicar página/alterar tema.

## Primeiros artefatos seguros

- Diagnóstico read-only de capacidade Rivo.
- Tabela de marcos/benefícios para aprovação.
- Preview da página LK Rewards.
- Fila sanitizada de clientes próximos de marco / benefício pendente, sem PII em Telegram.
