# Organograma Operacional — Hermes Brain

Última atualização: 2026-05-16

## Modelo mental canônico

Lucas corrigiu a hierarquia: o Hermes não deve organizar o Brain como várias empresas soltas. O modelo certo é uma **grande mente central** que cuida de tudo e roteia para camadas abaixo.

```text
Grande Mente — Hermes Brain / Hermes COO
├── Lucas pessoal
├── Empresas
│   ├── LK Sneakers
│   ├── Zipper Galeria
│   └── SPITI Auction
├── Operações Hermes
├── Tecnologia / Infraestrutura
└── Governança / Segurança / Aprovações
```

## Regra de navegação

1. Começar pela camada global: intenção de Lucas, segurança, decisão, memória e aprendizagem.
2. Só depois descer para a empresa ou área correta.
3. Não misturar dados, clientes, credenciais, tom ou decisões entre empresas.
4. Quando algo cruza empresas, registrar em `empresa/` antes de detalhar em `areas/`.
5. Quando algo é específico de uma empresa, registrar em `areas/<empresa>/` e referenciar no mapa global apenas como índice.

## Papel de cada camada

### Grande Mente — Hermes Brain / Hermes COO

A camada central guarda:

- princípios operacionais;
- aprendizados de Lucas;
- decisões permanentes;
- guardrails de aprovação;
- rotinas globais;
- roteamento entre empresas;
- consolidação de pendências;
- padrões de qualidade e segurança.

Caminhos principais:

- `START-HERE.md`
- `AGENTS.md`
- `PROTOCOLS.md`
- `empresa/`
- `memories/`
- `seguranca/`
- `skills/`

### Lucas pessoal

Camada para agenda, lembretes, intake pessoal e Mordomo. Pode receber sinais de qualquer empresa, mas deve classificar antes de agir.

Regra: eventos claros podem virar calendário conforme guardrails; contato externo continua exigindo aprovação explícita de Lucas com destinatário e texto.

### Empresas

Cada empresa tem operação, tom, fontes de verdade e riscos próprios.

#### LK Sneakers

- Caminho: `areas/lk/`
- Fonte viva: Shopify, Tiny, GA4/GSC, Klaviyo, Meta/Google, Supabase LK quando aplicável.
- Tom: premium, comercial, analítico.
- Risco: campanhas, preço, estoque, Shopify/Tiny/GMC e contato com cliente exigem controle forte.

#### Zipper Galeria

- Caminho: `areas/zipper/`
- Fonte viva: Supabase Zipper Vendas, Gmail/WhatsApp aprovados, calendário `lucas@zippergaleria.com.br`.
- Tom: cultural, sofisticado, sem hard-sell.
- Risco: colecionadores, artistas, propostas, obras, logística e comunicação externa.

#### SPITI Auction

- Caminho: `areas/spiti/`
- Fonte viva: repo Spiti Hub, Supabase/CRM, fontes verificadas de leilão/lances.
- Tom: preciso, conservador, sem afirmar lance/lote sem evidência.
- Risco: dados de leilão, clientes, deploy e reports públicos.

### Operações Hermes

- Caminho: `areas/operacoes/`
- Escopo: crons, watchdogs, release tracking, Brain hygiene, learning loop, rotinas internas.
- Regra: read-only/local/documentação pode avançar; Docker/runtime/gateway/host exigem plano e aprovação.

### Tecnologia / Infraestrutura

- Caminho: `areas/tecnologia/`
- Escopo: arquitetura técnica, integrações, scripts, APIs, VPS, Doppler, GitHub.
- Regra: não tocar em Docker, rede, volumes, Traefik, root, SSH ou produção sem aprovação explícita e rollback.

### Governança / Segurança

- Caminho: `areas/governanca/` e `seguranca/`
- Escopo: permissões, ações sensíveis, aprovações, limites de autonomia.
- Regra: `/background`, `seguir` e aprovações amplas nunca autorizam envio externo ou ação destrutiva.

## Consequência para a consolidação atual

A limpeza do Brain deve seguir esta ordem:

1. Consolidar arquitetura global e mapas (`START-HERE`, `README`, `empresa/`, `areas/`).
2. Separar pendências por camada: global, Lucas pessoal, LK, Zipper, SPITI, Operações, Tecnologia, Governança.
3. Commitar por camada/tema, não por data solta.
4. Evitar que relatórios operacionais virem a fonte de verdade principal; eles devem apontar para rotinas, mapas ou decisões.
5. Manter `reports/` como evidência e `areas/`/`empresa/` como operação viva.

## Regra curta

**Uma mente em cima. Empresas e Lucas pessoal embaixo. Operações, tecnologia e governança sustentam a mente.**
