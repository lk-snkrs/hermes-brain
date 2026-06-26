# LK OS — Etapa futura: Rivo / LK Rewards + Judge.me Reviews

Data: 2026-05-13
Status: `future_stage_planned`
Modo: planejamento/read-only; nenhum acesso, sync, write, campanha, cupom, mensagem, automação ou alteração de plataforma executado.

## Correção de escopo registrada

Lucas informou que faltava no LK OS uma camada de fidelidade e prova social:

- **LK Rewards** — programa de membros/fidelidade da LK, operado na plataforma **Rivo**.
- **Avaliações/reviews** — operadas na plataforma **Judge.me**.

Esta etapa deve entrar no LK OS como camada futura de **Customer Trust & Loyalty**, conectando recompra, CRM, experiência pós-compra, prova social de produto e benefícios de membros.

## Por que isso entra no LK OS

O LK OS hoje já separa fontes de verdade e sinais operacionais para vendas, estoque, marketing, sourcing e GMC. Rivo e Judge.me adicionam duas dimensões que ainda estavam sub-representadas:

1. **Fidelidade / membros**
   - pontos acumulados;
   - pontos resgatados;
   - membros ativos/inativos;
   - tiers/VIP, se existirem;
   - indicações/referrals, se estiverem ativos;
   - benefícios usados vs. benefícios esquecidos.

2. **Confiança / prova social**
   - rating por produto;
   - volume de reviews;
   - reviews recentes;
   - reviews negativas ou sem resposta;
   - produtos campeões de venda com pouca prova social;
   - produtos com boa avaliação que merecem destaque em PDP, CRM, e-mail e WhatsApp.

## Fonte e rótulos de dados

Adicionar ao vocabulário do LK OS:

- `fact_rivo_loyalty`: dados confirmados pela Rivo/LK Rewards, como pontos, membros, tiers, resgates, referrals e benefícios.
- `fact_judgeme_review`: dados confirmados pelo Judge.me, como avaliação, texto de review, status publicado, rating, produto associado e data.
- `derived_loyalty_crm`: cruzamentos calculados entre Shopify/Supabase/Klaviyo/Rivo, por exemplo cliente VIP com pontos parados.
- `derived_review_cro`: cruzamentos entre Shopify/Judge.me/GA4, por exemplo PDP com tráfego alto e poucas reviews.

PII continua privada. Telegram/Brain só devem receber agregados, hashes ou exemplos sanitizados, salvo aprovação explícita.

## Fase futura proposta

### Fase 10 — Customer Trust & Loyalty Spine

Objetivo: adicionar Rivo e Judge.me ao Data Spine do LK OS em modo read-only primeiro.

Entregas seguras:

1. **Subdocs de integração**
   - `empresa/integracoes/rivo.md`
   - `empresa/integracoes/judgeme.md`

2. **Inventário read-only**
   - confirmar se existe API/token Rivo em Doppler ou qual método de acesso;
   - confirmar token Judge.me já mapeado como `JUDGEME_API_TOKEN`;
   - listar endpoints disponíveis sem puxar PII desnecessária;
   - identificar IDs necessários: shop domain, app IDs, campaign/review IDs, webhook config, se houver.

3. **Snapshot inicial sem writes**
   - Rivo: membros, pontos, resgates, tiers, referrals, saldo parado, clientes com benefício não usado;
   - Judge.me: review count, average rating, reviews pendentes/negativas, produtos sem reviews, produtos com rating forte.

4. **Cruzamentos operacionais**
   - Shopify/Supabase + Rivo: cliente comprou mas não usa benefício; cliente VIP com pontos parados; cliente recorrente sem entrar no Rewards.
   - Shopify + Judge.me: produto vendido com pouca review; produto com rating alto para destacar; produto com review negativa para atendimento.
   - Klaviyo/WhatsApp previews: campanhas de benefício e review request sem envio automático.

5. **Mission Control**
   - adicionar bloco de status: `Loyalty & Reviews`.
   - métricas propostas:
     - membros LK Rewards ativos;
     - pontos emitidos/resgatados/expirando;
     - clientes com benefício parado;
     - produtos P1 sem reviews suficientes;
     - reviews negativas/pendentes;
     - produtos com alta nota + oportunidade comercial.

## Guardrails

Sem aprovação explícita de Lucas, esta etapa **não autoriza**:

- criar/editar cupom;
- alterar regra de pontos ou tiers;
- disparar e-mail, WhatsApp ou SMS;
- responder review publicamente;
- publicar/despublicar review;
- criar campanha Klaviyo/Rivo/Judge.me;
- mexer em tema Shopify ou widgets;
- escrever em Shopify, Rivo, Judge.me, Klaviyo, Notion ou Supabase.

Primeiro bloco permitido quando Lucas pedir: documentação + leitura read-only + preview sanitizado.

## Casos de uso futuros

### 1. Recompra por benefício esquecido

Exemplo de insight:

- Cliente comprou nos últimos 180 dias.
- Tem pontos/recompensa disponível.
- Não comprou nos últimos X dias.
- Próximo seguro: preview de mensagem/campanha, sem envio.

### 2. Review request inteligente

Exemplo:

- Produto vendido.
- Pedido entregue.
- Cliente ainda não avaliou.
- Próximo seguro: preview de régua Judge.me/Klaviyo, sem envio.

### 3. PDP/CRO com prova social

Exemplo:

- Produto tem tráfego alto e venda baixa.
- Tem reviews fortes que não aparecem bem na dobra inicial.
- Próximo seguro: preview de recomendação visual/UX, sem alteração de tema.

### 4. Produtos campeões sem review suficiente

Exemplo:

- SKU/produto vende bem, mas tem poucas avaliações.
- Próximo seguro: fila de review request ou incentivo via LK Rewards, sem disparo.

### 5. Atendimento/reputação

Exemplo:

- Review 1–3 estrelas recente.
- Próximo seguro: fila interna para atendimento humano, sem resposta pública automática.

## Perguntas pendentes para Lucas

1. O nome correto é **LK Rewards** ou há grafia/branding específico diferente?
2. A Rivo está conectada ao Shopify com qual escopo: pontos, tiers, referrals, VIP, cupons, indicação, pós-compra?
3. Existe API/token da Rivo já em Doppler? Se não, quem tem acesso ao admin da Rivo?
4. Quais são as regras atuais de pontos? Ex.: R$1 = X pontos, bônus por cadastro, aniversário, review, indicação etc.
5. Existem tiers de membro? Se sim, quais nomes e benefícios?
6. Pontos expiram? Se sim, em quanto tempo?
7. O LK Rewards deve ser tratado como ferramenta de margem/recorrência ou mais como experiência premium de marca?
8. Judge.me: reviews são publicadas automaticamente ou passam por moderação?
9. Quem responde reviews negativas hoje?
10. Review request hoje sai por Judge.me, Klaviyo, Shopify, e-mail nativo ou outro fluxo?
11. Queremos usar reviews como input de CRO/PDP, CRM/Klaviyo, atendimento, ou todos?
12. Há algum benefício que nunca deve ser comunicado automaticamente?

## Próximo passo seguro

Quando Lucas aprovar esta etapa, o primeiro bloco deve ser:

1. criar subdocs `rivo.md` e `judgeme.md`;
2. mapear credenciais por nome, sem valores;
3. fazer inventário read-only da API/admin disponível;
4. gerar um snapshot sanitizado `Loyalty & Reviews v0`;
5. incluir o bloco no Mission Control como futuro, sem cron e sem envio.

## Não executado

- Nenhuma consulta à Rivo.
- Nenhuma consulta nova ao Judge.me.
- Nenhum write em plataforma.
- Nenhum cupom, regra, review, campanha, e-mail, WhatsApp, Shopify theme, Klaviyo ou Notion alterado.
