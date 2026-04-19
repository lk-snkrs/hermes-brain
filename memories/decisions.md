# Decisões Permanentes — Grupo Cimino

## Infraestrutura
| Decisão | Motivo | Data |
|---------|--------|------|
| Doppler = fonte de verdade de credenciais | Centralizado, rotacionável, nunca hardcode | 2026-03-17 |
| Git sempre push após commit | Cerebro só vale se estiver no GitHub | 2026-03-17 |
| Evolution instância `Clo` para envios LK | Separar envio (Clo) de recebimento (SPITI) | 2026-03-24 |
| Supabase: SERVICE_KEY para writes | Segurança — ANON_KEY só para reads públicos | 2026-03-17 |

## Bancos de Dados (definitivo)
| Banco | Project ID | Uso |
|-------|-----------|-----|
| LK Sneakers | `cnjimxglpktznenpbail` | pedidos, clientes, produtos |
| Zipper Vendas | `pcstqxpdzibheuopjkas` | vendas_tango (2.058 registros) |
| SPITI / Zipper CRM | `rmdugdkantdydivgnimb` | spiti_lotes, spiti_contacts, crm_spiti |

## Shopify
| Item | Valor |
|------|-------|
| Store handle | lk-sneakerss.myshopify.com |
| Token Doppler | `SHOPIFY_ACCESS_TOKEN` (não `SHOPIFY_API_TOKEN`) |
| API version | 2024-01 |

## Comunicação
| Decisão | Regra |
|---------|-------|
| Notificação Lucas | → Telegram (171397651) |
| Cross-sell / CRM LK | → Klaviyo (email) + Evolution Clo (WhatsApp) |
| Monitor SPITI | → Evolution Clo → Grupo SPITI.M |
| Comunicação Zipper | → Evolution ZipperGaleria |
| Preview antes de envio em massa | Aprovação obrigatória do Lucas |
| Claw não é a voz do Lucas em grupos | Risco de representação incorreta da marca |

## Autonomia
| Nível | O que faz | O que precisa aprovação |
|-------|-----------|------------------------|
| L2 (Executor) | Executa rotinas, analisa, consulta dados | External actions (emails, posts, WA em massa) |
| External actions | — | SEMPRE aprovação do Lucas |

## Processo de Projetos
| Fase | Regra |
|------|-------|
| Ideia | SUPERPOWER obrigatório antes de qualquer código |
| PRD | Sem PRD aprovado = não começa |
| Fluxo | Ideia → SUPERPOWER → PRD → Implementar → Skill documentada |

## Prioridade de Ferramentas
1. **CLI oficial** — Vercel, Supabase, Shopify, GitHub, Doppler (se instalada)
2. **MCP** — se não tem CLI mas tem MCP configurado
3. **API REST manual** — último recurso (curl/python/fetch)

## Regras de Ouro
- **Dúvida → consulta. Sem consulta → sem resposta sobre dados.**
- Nunca dizer "zerado" ou "sem lance" sem consultar banco primeiro
- Nunca inventar informação sobre estoque, preço ou prazo
- Credenciais: SEMPRE no Doppler, nunca hardcode
- Após deploy: confirmar PID/porta do processo que está rodando

## Fonte
Sincronizado do cerebro-cimino (VPS: /root/cerebro-cimino) para hermes-brain (/root/hermes-brain)
