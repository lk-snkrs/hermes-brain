---
name: lk-leads-esfriando
description: Monitor de leads esfriando LK — detecta clientes que compraram há 30-60 dias e podem estar desinteressando. Identifica padrões de churn e gera alertas proativos.
area: lk
version: 1.0.0
---

# Skill: LK Leads Esfriando Monitor

## Contexto
- 378 clientes NB 9060 sem recompra = segmento mais quente
- Taxa segunda compra atual: 17% (meta: 25%)
- Clientes em risco: compraram há 30-60 dias, sem interação

## Processo
1. Busca clientes que compraram entre 30-60 dias atrás
2. Verifica se tiveram interação desde então (Klaviyo opens, site visits)
3. Classifica em:
   - **Quente:** teve interação mas não comprou — kampagin candidate
   - **Frio:** sem interação — reativação necessária
   - **Risco:** comprou marca com baixa lealdade — cross-sell urgente
4. Gera lista segmentada por estratégia:
   - Reativação (campanha Klaviyo)
   - Cross-sell (direto via Evolution Clo)
   - VIP (mais de 2 compras, alto ticket)

## Segmentação de Risco
| Risco | Critério | Ação |
|-------|---------|------|
| Alto | >60 dias sem compra + marca baixa lealdade | Cross-sell urgente |
| Médio | 45-60 dias sem interação | Reativação Klaviyo |
| Baixo | 30-45 dias | Monitorar |

## Output
- Lista segmentada no Telegram para Lucas
- Recommendações de ação por segmento
- Dados: nome, última compra, marca, dias desde última compra

## Credenciais (Doppler)
- `SUPABASE_LK_SERVICE_KEY`
- `KLAVIYO_API_KEY`
