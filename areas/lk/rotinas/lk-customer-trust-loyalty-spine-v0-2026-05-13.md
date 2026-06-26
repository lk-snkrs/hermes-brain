# LK OS — Customer Trust & Loyalty Spine v0

Status: `prd_extension_ready_no_platform_write`
Data: 2026-05-13
Fontes: PRD LK OS, correções Lucas via Telegram, docs `rivo.md` e `judgeme.md`.
Modo: documentação/read-only/local. Nenhuma consulta/API/write em Rivo, Judge.me, Shopify, Klaviyo, Notion, Supabase ou tema.

## Veredito

O próximo bloco seguro do PRD LK OS é formalizar **Customer Trust & Loyalty** como camada do sistema antes de qualquer configuração de Rivo/Judge.me/Klaviyo/Shopify.

A camada entra para resolver quatro pontos:

1. fidelidade premium por gasto acumulado/status;
2. prova social/reviews como input de CRO e CRM;
3. benefícios automáticos sem depender de troca manual de pontos;
4. página LK Rewards como superfície clara para cliente.

## Fonte e rótulos

- `fact_shopify`: gasto acumulado, pedidos elegíveis, cancelamentos/devoluções quando puxados da Shopify.
- `fact_supabase`: espelho operacional LK/RFM, quando usado para segmentação.
- `fact_rivo_loyalty`: membros/pontos/tiers/benefícios confirmados pela Rivo.
- `fact_judgeme_review`: reviews/rating/status confirmados pelo Judge.me.
- `derived_loyalty_crm`: cálculo de elegibilidade, cliente próximo de marco, benefício pendente.
- `derived_review_cro`: produto com venda/tráfego e pouca review, review forte para PDP/CRM.
- `manual_approval`: tier, benefício, cupom, resposta pública ou envio aprovado por Lucas.
- `unknown`: qualquer regra não confirmada.

## LK Rewards — modelo canônico v0

Nome: **LK Rewards**.

Modelo correto:

```text
gasto acumulado / status
→ marco atingido
→ benefício automático ou fila humana de cumprimento
→ comunicação premium simples
```

Modelo incorreto:

```text
cliente entra em área de pontos
→ troca manualmente por cupom
```

Regras confirmadas:

- 1 ponto = R$1.
- Tiers por gasto acumulado.
- Objetivo: recompras/margem + experiência VIP.
- Exemplos iniciais:
  - R$5.000 → kit de limpeza Jason Markk.
  - R$15.000 → 15% off + kit viagem.

Pendências de regra:

- lifetime spend ou janela móvel, ex. 12 meses;
- se cancelamentos/devoluções subtraem elegibilidade;
- expiração de pontos/status;
- cumprimento do benefício: automático, cupom, envio físico, atendimento humano ou combinação;
- tabela final de nomes dos tiers e benefícios;
- captura de aniversário.

## Reviews / Judge.me — modelo canônico v0

Regras confirmadas:

- reviews publicam automaticamente;
- Lucas deleta ruins manualmente;
- Lucas responde pessoalmente negativas;
- review request deveria sair por Klaviyo, mas precisa auditoria;
- uso por fase: PDP/CRO → CRM/Klaviyo → atendimento/reputação → ranking de produtos.

Primeiras métricas propostas:

- rating médio total;
- reviews por produto;
- produtos campeões com poucas reviews;
- reviews 1–3 estrelas recentes;
- produtos com rating alto e oportunidade de destaque;
- risco de duplicidade Judge.me/Klaviyo em review request.

## Página LK Rewards — estrutura v0

Objetivo da página: explicar o programa como **reconhecimento de relacionamento**, não promoção barata.

Estrutura recomendada:

1. Hero: “LK Rewards” + promessa premium.
2. Como funciona: compre, acumule status, receba benefícios.
3. Marcos de gasto: tabela/steps com benefícios.
4. Benefícios VIP: kits, acesso, atendimento, cupons pontuais, aniversário futuro.
5. FAQ simples: pontos, elegibilidade, devoluções, quando recebe, validade.
6. Termos: sujeito a disponibilidade, regras podem mudar, benefício não cumulativo quando aplicável.
7. CTA: entrar/logar/acompanhar status, dependendo da viabilidade técnica Rivo/Shopify.

Tom:

- premium;
- relacionamento;
- curadoria;
- cuidado;
- acesso;
- reconhecimento.

Evitar:

- “troque pontos por desconto”;
- linguagem de cashback popular;
- promessa automática que ainda depende de humano;
- benefício sem regra aprovada.

## Captura de aniversário — opções de arquitetura

Status atual: LK não capta aniversário no checkout.

Opções read-only a mapear antes de implementação:

1. Shopify customer metafield via área de conta/perfil.
2. Formulário Klaviyo pós-compra ou pop-up segmentado.
3. Campo/atributo no Rivo, se suportado.
4. Formulário pós-compra com incentivo leve.
5. Checkout extensibility/customer fields, apenas se o plano Shopify permitir e com cuidado de atrito.

Recomendação inicial: começar por **Klaviyo/Rivo/account page**, não mexer no checkout/tema antes de entender viabilidade e atrito.

## Guardrails

Sem aprovação explícita de Lucas, não executar:

- alteração de regra Rivo;
- criação de tier/cupom/benefício;
- envio Klaviyo/WhatsApp/SMS;
- resposta/moderação Judge.me;
- alteração de widget/tema Shopify;
- criação/publicação da página Shopify;
- write em Shopify/Rivo/Judge.me/Klaviyo/Notion/Supabase;
- exposição de PII em Telegram/Brain.

## Próximo bloco seguro

1. Atualizar PRD LK OS com o módulo Customer Trust & Loyalty.
2. Indexar subdocs Rivo/Judge.me nas integrações.
3. Criar wireframe/copy v0 da página LK Rewards em arquivo local.
4. Depois, quando Lucas quiser, fazer inventário read-only real de Judge.me/Rivo/Klaviyo sem writes.

## Não executado

- Nenhuma consulta à Rivo.
- Nenhuma consulta à Judge.me.
- Nenhum write em plataforma.
- Nenhuma campanha/cupom/review/página/tema alterados.
- Nenhum envio ou contato externo.
