# LK Rewards — modelo de benefícios automáticos por marco de gasto

Data: 2026-05-13
Status: `lucas_correction_registered_pending_details`
Fonte: correção direta de Lucas via Telegram.

## Correção importante

LK Rewards **não deve ser modelado como programa clássico de pontos para troca por desconto**.

Lucas explicou que o modelo desejado é mais parecido com companhia aérea / status por relacionamento:

- o cliente acumula progresso conforme compra/gasta;
- ao atingir determinados marcos de gasto, ganha benefícios automaticamente;
- o cliente da LK é mais velho/premium e provavelmente não vai entrar em uma área de Rewards para trocar pontos manualmente;
- o sistema deve reconhecer o marco e preparar/acionar benefício de forma guiada, com comunicação simples e premium.

## Exemplos iniciais informados

Ainda pendente de tabela final, mas exemplos citados:

- Gastou R$ 5.000 → ganha kit de limpeza Jason Markk.
- Gastou R$ 15.000 → ganha cupom de 15% + kit viagem.

## Implicação para o LK OS

Trocar o framing de:

- `points_redemption_program`

para:

- `automatic_spend_milestone_benefits`
- `relationship_status_progression`
- `premium_client_benefit_entitlement`

## Como o LK OS deve tratar

### Fonte primária

- Shopify/Supabase: gasto acumulado, pedidos elegíveis, devoluções/cancelamentos, janela temporal.
- Rivo: se usado como engine de loyalty/status/benefícios, confirmar como representa marcos, pontos e automações.
- Klaviyo/WhatsApp: somente previews de comunicação, sem envio automático.
- Notion/CRM interno: possível fila de benefício a cumprir, se Lucas aprovar.

### Métricas futuras

- clientes próximos do próximo marco;
- clientes que bateram marco e ainda não receberam benefício;
- benefício devido por cliente;
- custo estimado dos benefícios;
- impacto em recompra/VIP;
- elegibilidade considerando devoluções/cancelamentos;
- próximos marcos por faixa de gasto.

### Guardrails

Sem aprovação explícita, Hermes não deve:

- criar cupom;
- disparar comunicação;
- conceder benefício;
- alterar regra na Rivo;
- escrever no Shopify/Rivo/Klaviyo/Notion;
- prometer benefício a cliente;
- modificar tema ou criar página publicada.

## Página LK Rewards

Lucas também pediu ajuda futura para criar uma página do LK Rewards.

Primeiro bloco seguro deve ser:

1. briefing de posicionamento e regras;
2. wireframe/copy premium da página;
3. seção de benefícios por marco;
4. FAQ;
5. termos simples;
6. visual aprovado antes de qualquer implementação no Shopify.

A página deve evitar linguagem de “troque pontos por desconto” se esse não for o modelo. O tom correto é:

- relacionamento;
- status;
- benefícios automáticos;
- cuidado premium;
- reconhecimento por histórico com a LK.

## Respostas iniciais de Lucas — 2026-05-13

1. Nome: **LK Rewards**.
2. Modelo: tiers de acordo com gasto acumulado.
3. Pontuação-base: **1 ponto = R$ 1**.
4. Recomendações por reviews são desejadas.
5. Aniversário seria ótimo, mas a LK ainda não capta data de aniversário no checkout; adicionar captura de aniversário no Shopify virou pendência futura.
6. Expiração de pontos ainda não configurada/definida.
7. Objetivo do LK Rewards: **ambos** — recompra/margem e experiência premium/VIP.
8. Judge.me: reviews publicam automaticamente; Lucas deleta reviews ruins manualmente.
9. Reviews negativas: Lucas responde pessoalmente.
10. Review request deveria sair pelo Klaviyo, mas Lucas suspeita que não está bem configurado.
11. Prioridade de uso de reviews: todas as frentes, por fase — PDP/CRO, CRM/Klaviyo, atendimento/reputação e ranking de produtos.

## Pendências novas derivadas

- Definir tabela final de tiers/marcos e benefícios.
- Definir se gasto acumulado considera lifetime, últimos 12 meses ou outro período.
- Definir se devoluções/cancelamentos subtraem do gasto elegível.
- Definir como cumprir benefício: envio físico, cupom, atendimento humano ou combinação.
- Confirmar se Rivo consegue representar tiers/marcos automáticos por gasto acumulado ou se precisaremos de automação externa.
- Criar plano para capturar aniversário no Shopify checkout/customer profile sem atrito excessivo.
- Auditar configuração atual de review request no Klaviyo/Judge.me antes de qualquer disparo.
- Desenhar página LK Rewards: institucional primeiro; logada/saldo/status depois, se tecnicamente viável e aprovado.
