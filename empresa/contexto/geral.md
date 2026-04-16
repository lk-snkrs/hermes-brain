# Lucas Cimino — Contexto da Empresa

> Fonte de verdade sobre os negócios. Claw lê este arquivo antes de qualquer análise.

## Negócios

| Empresa | Descrição | Meta 2026 |
|---------|-----------|-----------|
| LK Sneakers | Sneaker boutique premium, Jardins/SP | R$ 1.000.000 |
| Zipper Galeria | Galeria de arte contemporânea | R$ 1.400.000 |
| SPITI | Leilão de arte (SPITI 9 — pregão 31/03 e 01/04/2026) | — |

## Equipe

### LK Sneakers
| Nome | Função |
|------|--------|
| Renan | Comunicação |
| Júlio | Financeiro e fiscal |
| Danilo | Vendas e curadoria |

### Zipper Galeria
| Nome | Função |
|------|--------|
| Osmar | Diretor comercial + sócio |
| Helo | Comunicação (vídeos) |
| Biz | Comunicação (texto) |
| Mie | Comunicação (fotos/design) |
| Cibele | Financeiro e RH |
| Panda | Produção |

## Ferramentas
- **E-commerce:** Shopify (lksneakers.com.br)
- **Dados:** Supabase (LK + Zipper + SPITI)
- **Deploy:** Railway
- **Secrets:** Doppler
- **Automações:** n8n, GitHub Actions
- **WhatsApp:** Evolution API (instâncias: Clo, SPITI, Pessoal, ZipperGaleria)

## Ferramentas e Integrações

> Documentação completa em [`empresa/integracoes/`](../integracoes/MAPA.md).

### Analytics
| Ferramenta | Propriedades | Secret Ref |
|------------|-------------|------------|
| Google Analytics 4 | lksneakers.com.br + zippergaleria.com | `GOOGLE_ANALYTICS_KEY` |
| Microsoft Clarity | lksneakers.com.br + zippergaleria.com | `CLARITY_API_KEY` |

### Marketing
| Ferramenta | Detalhes | Secret Ref |
|------------|---------|------------|
| Meta Ads | LK Sneakers (⚠️ Account ID pendente) | `META_ACCESS_TOKEN` |
| Klaviyo | LK News — 5.020 assinantes | `KLAVIYO_API_KEY` |
| Google Trends | Sem auth | — |

### SEO e Dados de Mercado
| Ferramenta | Detalhes | Secret Ref |
|------------|---------|------------|
| Google Search Console | lksneakers.com.br | via GOG |
| KicksDB | StockX/GOAT data | `KICKSDB_API_KEY` |
| lk-geo | Reddit scanner, 13 subreddits | — |
| lk-price | Monitor Palmtree48, Hype Concept, Juicy | — |
| Brave Search | Pesquisa de mercado | `BRAVE_API_KEY` |
| Tavily | Deep research | `TAVILY_API_KEY` |

### Infraestrutura
| Ferramenta | Detalhes | Secret Ref |
|------------|---------|------------|
| Railway | lc-whatsapp, zpr-cockpit, lk-cockpit, zpr-auto-like | `RAILWAY_TOKEN` |
| n8n | https://n8n.lucascimino.com/api/v1 | `N8N_API_KEY` |
| Doppler | lc-keys / prd — 104 secrets | — (self) |
| GitHub | lk-snkrs/lk-new-theme + cerebro-cimino | SSH /root/.ssh/id_rsa |

### Por Área
- **LK Sneakers:** Shopify, Supabase LK (24k clientes), Klaviyo, GA4, GSC, Meta Ads, KicksDB, lk-price, lk-geo → [`areas/lk/contexto/ferramentas.md`](../../areas/lk/contexto/ferramentas.md)
- **Zipper Galeria:** Supabase Zipper Vendas (2.058 vendas), Supabase SPITI, Evolution WhatsApp, GA4, zpr-cockpit, zpr-auto-like → [`areas/zipper/contexto/ferramentas.md`](../../areas/zipper/contexto/ferramentas.md)

*Atualizado: 2026-03-30*
