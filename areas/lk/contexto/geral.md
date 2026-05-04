# LK Sneakers — Memória

## Contexto
- **Dono:** Lucas Cimino
- **Meta 2026:** R$ 1.000.000
- **Resultado março 2026:** R$ 1.238.292 (META SUPERADA +23.8%)
- **E-commerce premium de sneakers, Jardins/SP**

## Equipe
| Nome | Função | Contato |
|------|--------|---------|
| Renan | Comunicação | @fortinifilm (TG: 1305071627) |
| Júlio | Financeiro e fiscal | TG: 5924913605 |
| Danilo | Vendas e curadoria | — |

## KPIs Atuais
- Pedidos/mês: ~408
- Ticket médio: R$ 3.035
- Clientes base: 24.000
- Produtos ativos: 2.100+
- Retenção 90d: 9.1% (meta 25%)

## Produtos Top (hub central)
- **Onitsuka Tiger** — 91.6% lealdade, 1.290 pedidos, hub central de cross-sell
- New Balance 9060, 204L
- Adidas Samba, Yeezy
- Nike Dunk, Jordan, Travis Scott
- **Jason Markk** — upsell universal (funciona com qualquer tênis)

## Cross-Sell Confirmado (dados reais de 5.7k pedidos)
- Jason Markk + qualquer tênis: 8x (upsell obrigatório)
- NB 9060 → Onitsuka Tiger: 25 clientes fizeram esse caminho
- Onitsuka repeat rate: 91.6%
- **378 clientes NB 9060 sem recompra** = segmento mais quente para campanha

## Canais
| Canal | Uso |
|-------|-----|
| Shopify | lksneakers.com.br |
| WhatsApp Business | +551****5245 (instância Clo) — atendimento |
| Klaviyo | LK News — 5.020 assinantes, open rate ~30% (VIP 55.6%) |
| Instagram | @lk.sneakers |

## Stack de Ferramentas
| Ferramenta | Status | Secret |
|-----------|--------|--------|
| Shopify | Ativo | `SHOPIFY_ACCESS_TOKEN` |
| Supabase LK | Ativo | `SUPABASE_LK_SERVICE_KEY` (proj: cnjimxglpktznenpbail) |
| Klaviyo | Ativo | `KLAVIYO_API_KEY` |
| GA4 | Ativo | `GOOGLE_ANALYTICS_KEY` |
| GSC | Ativo | via GOG |
| Meta Ads | Parcial | `META_ACCESS_TOKEN` |
| KicksDB | Ativo | `KICKSDB_API_KEY` |
| lk-price | Ativo | Monitora Palmtree48, Hype Concept, Juicy |
| lk-geo | Ativo | Reddit scanner, 13 subreddits |
| Tiny ERP | Ativo | `TINY_API_TOKEN` (Júlio) |
| Judge.me | Ativo | `JUDGEME_API_TOKEN` |
| Metricool | Ativo | `METRICOOL_API_TOKEN` (Renan) |
| Cloudflare | Ativo | DNS/CDN lksneakers.com.br |

## Como Falo (TOM LK)
- **Tom:** Analítico e premium. Dados primeiro, emoção depois.
- **Estratégias:** Hormozi (oferta), Eugene Schwartz (segmentação), Virgil Abloh (identidade)
- **Jamais:** "compre agora", travessão (—), "premium", "melhor do Brasil"
- **Sempre:** "encontre o que te representa", "curadoria intencional"
- **Numbers:** R$ com 2 decimais, nunca arredondar除非 for explicitly asked
- **Copy:** Sem travessão, sem emoji excessivo, direto ao ponto

## Decisões Permanentes
- **Cross-sell via Klaviyo + Evolution Clo** (não WhatsApp Business direto)
- **Nunca usar travessão (—) em copy LK** — tom premium
- **Preview no Telegram antes de qualquer envio de campanha** — aprovação obrigatória
- **Regra 90 dias: 1 cross-sell por cliente** — evitar spam
- **Recomendação só de produtos em estoque**
- **gender=unisex, age_group=adult** para todos produtos GMC

## Lições Aprendidas
- GraphQL metafieldsSet com JSON embutido dá erro 500 → usar REST API
- Heredoc Python dentro de exec trava output → escrever arquivo .py e rodar
- Shopify REST API: 0.12s entre calls = seguro (não dá rate limit)
- Googlebot ignora crawl-delay em robots.txt
- GMC pode levar horas para re-sincronizar após correção

## Pendências Ativas
- [ ] Lançar sistema cross-sell via Klaviyo (fluxo pós-compra + upsell Jason Markk)
- [ ] Campanha reativação 378 clientes NB 9060 dormentes
- [ ] Campanhas segmentadas por marca (Klaviyo)
- [ ] Taxa segunda compra: 17% → meta 25%

## Scripts Principais
- `/root/lk-price/` — monitor concorrentes
- `/root/lk-geo/` — Reddit scanner
- `lk_frenet_api` skill — Frenet shipping

## Fonte
Sincronizado do cerebro-cimino (VPS: /root/cerebro-cimino) para hermes-brain (/root/hermes-brain)
