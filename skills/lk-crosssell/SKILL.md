---
name: lk-crosssell
description: Monitor de cross-sell LK — detecta pedidos fulfilled e gera sugestões de produtos complementares para clientes recentes. Baseado nos padrões de cross-sell do cerebro-cimino (Onitsuka hub central, Jason Markk upsell universal).
area: lk
version: 1.0.0
---

# Skill: Cross-Sell Monitor LK

## Fontes
- Scripts: `/root/lk-price/` (monitor concorrentes)
- Docs: `/root/hermes-brain/memories/lk.md`
- Database: Supabase LK (`cnjimxglpktznenpbail`)

## Input
- Pedidos fulfilled nas últimas 24h (Supabase LK)
- Histórico de compras por cliente

## Processo
1. Busca pedidos com status `fulfilled` nas últimas 24h
2. Para cada cliente, analisa histórico de compras anteriores
3. Identifica padrões: quem comprou X também comprou Y
4. Aplica regras de cross-sell confirmadas:
   - Jason Markk + qualquer tênis = upsell obrigatório
   - NB 9060 → Onitsuka Tiger = fluxo mais forte (25 clientes)
   - Onitsuka Tiger = hub central (91.6% lealdade)
5. Gera sugestão de produto complementar por perfil
6. Envia preview para Lucas aprovar antes de disparar

## Regras de Cross-Sell Confirmadas
- **Jason Markk** — funciona como upsell com qualquer tênis
- **NB 9060** → Onitsuka Tiger = caminho mais forte de cross-sell
- **Onitsuka Tiger** — maior lealdade (91.6%), funciona como hub
- **Regra 90 dias:** 1 cross-sell por cliente (evitar spam)
- **Só produtos em estoque**

## Output
Preview no Telegram com:
- Lista de clientes para cross-sell
- Produto sugerido por cliente
- Contexto (última compra, perfil)
- Botão de aprovação

## Credenciais (Doppler)
- `SUPABASE_LK_URL`
- `SUPABASE_LK_SERVICE_KEY`

## Cron
`LK Cross-Sell Monitor` — 9h10, 15h10 e 21h10 diariamente
