# SPITI Auction — Memória

## Contexto
- **Dono:** Lucas Cimino
- **Leilão de arte**
- **SPITI 9:** pregão 31/03 e 01/04/2026

## Canais
| Canal | Contato/ID |
|-------|------------|
| WhatsApp | +551****0369 (instância SPITI — só recebe) |
| Grupo | SPITI.M (120363420032270213@g.us) |
| Painel | leiloesbr.com.br / leilão 60396 |
| Instagram | @spiti.auction |

## Lotes Top Confirmados
- Sandra Gamarra: R$ 120k (base confirmada pelo Fábio Cimino)
- Os Gêmeos: R$ 75k
- A.H. Amaral: R$ 95k

## Banco de Dados
- **Supabase:** `rmdugdkantdydivgnimb`
- **Tabela principal:** `spiti_lotes`
- **Instância Evolution:** `Clo` para envios (NÃO usar SPITI para enviar)

## Monitor de Lances
- systemd: `spiti-lances`, porta 19123
- n8n workflow: ID `OHC9FfEsK0JRVMBK`

## Regras de Ouro
- **Total de lances = fonte é o email** — site mostra só 12 destaques
- **Meta tag ≠ lance atual** — `product:price:amount` = preço base, não lance
- **Tipo de lance:** A = automático, O = normal
- **Tom no grupo:** leve e descontraído, mas pensar antes de responder
- **Silêncio é melhor que dado errado**

## Lições Aprendidas
- Scraper leu meta tag como lance → dado errado no Rodrigo Andrade (R$ 40k falso)
- n8n timeout curto (~10s) matava workflow de 7s/lote → Playwright rodava mas n8n abortava
- **Solução:** webhook async — responde 2xx imediato, processa em thread separada
- Deduplicação: TTL 24h, chave `{lote_id}:{lance_atual}`
