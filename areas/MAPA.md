# Áreas — Mapa Executivo

Cada área segue o padrão Hermes adaptado de Bruno/OpenClaw:

```text
area/
├── MAPA.md          # visão e regras da área
├── contexto/        # contexto consolidado
├── skills/          # navegação ou skills da área
├── rotinas/         # rotinas business-readable
├── projetos/        # projetos e registros
└── sub-areas/       # opcional, quando a área é complexa
```

## Áreas principais

As áreas ficam **abaixo da Grande Mente**. Elas são unidades operacionais com fontes e regras próprias; a camada global decide roteamento, segurança e aprendizado antes de descer para uma área específica.

Referência de organograma: `empresa/contexto/organograma-operacional-hermes-brain.md`.

| Área | Caminho | Função | Fonte principal |
|------|---------|--------|-----------------|
| LK Sneakers | `areas/lk/` | ecommerce, CRM, tráfego, atendimento e syncs LK | Supabase LK `cnjimxglpktznenpbail`, Shopify |
| Zipper Galeria | `areas/zipper/` | vendas de obras, colecionadores, feiras e comunicação | Supabase Zipper Vendas `pcstqxpdzibheuopjkas` |
| SPITI Auction | `areas/spiti/` | leilão, lances, lotes, alertas e relatórios | Supabase/SPITI CRM `rmdugdkantdydivgnimb`, email |
| Operações | `areas/operacoes/` | brain sync, heartbeat e rotinas operacionais | GitHub, scripts, cronjobs |
| Governança | `areas/governanca/` | regras, compliance operacional e aprovações | `seguranca/`, decisões |
| Tecnologia | `areas/tecnologia/` | arquitetura, scripts, integrações e infra | Doppler, GitHub, VPS, APIs |

## Sub-áreas já mapeadas

### LK

- `areas/lk/sub-areas/crm/` — cross-sell, leads esfriando, RFM, outcomes e relacionamento.
- `areas/lk/sub-areas/trafego-pago/` — hipótese, criativo, teste, dado e learning.
- `areas/lk/sub-areas/ecommerce/` — Shopify, catálogo, pedidos e estoque.
- `areas/lk/sub-areas/atendimento/` — FAQ, dúvidas e consolidação para bot.

### Zipper

- `areas/zipper/sub-areas/vendas-obras/` — análise comercial de obras vendidas.
- `areas/zipper/sub-areas/colecionadores/` — relacionamento e abordagem aprovada.
- `areas/zipper/sub-areas/feiras/` — planejamento e execução de feiras.
- `areas/zipper/sub-areas/comunicacao/` — tom, textos, vídeos e publicações.

### SPITI

SPITI ainda é área compacta, com rotinas operacionais em `areas/spiti/rotinas/`.

## Regras globais

- `memories/` continua como memória executiva compacta.
- `areas/` detalha a operação por negócio.
- `empresa/` guarda contexto cross-área.
- Doppler guarda secrets; o Brain guarda apenas nomes de secrets.
- Ações externas exigem aprovação Lucas.
