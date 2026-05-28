# Receipt — Normalização documental dos agentes/subáreas LK

Data: 2026-05-27
Escopo: Brain local/documental apenas.

## Objetivo

Corrigir lacunas de documentação dos agentes e subáreas operacionais detectadas na auditoria de pacotes Amora/Hermes.

## O que foi feito

Foram criados 26 arquivos documentais faltantes para que os pacotes verificados tenham o conjunto mínimo:

- `AGENTS.md`
- `IDENTITY.md`
- `MAPA.md`
- `HEARTBEAT.md`
- `SOUL.md`
- `USER.md`
- `TOOLS.md`
- `MEMORY.md`

## Diretórios normalizados

- `areas/lk/sub-areas/shopify/`
  - criado `IDENTITY.md`
  - criado `USER.md`
- `areas/lk/sub-areas/trends/`
  - criado `USER.md`
- `areas/lk/sub-areas/growth/lk-shopify/`
  - criado `IDENTITY.md`
  - criado `USER.md`
  - marcado como ponte documental Growth → Shopify; a fonte canônica Shopify permanece `areas/lk/sub-areas/shopify/`
- `areas/lk/sub-areas/crm/`
  - criado pacote completo complementar ao `MAPA.md`
- `areas/lk/sub-areas/ecommerce/`
  - criado pacote completo complementar ao `MAPA.md`
- `areas/lk/sub-areas/trafego-pago/`
  - criado pacote completo complementar ao `MAPA.md`

## Resultado da auditoria pós-correção

Pacotes verificados: 13.

Resultado: todos os pacotes verificados possuem `AGENTS`, `IDENTITY`, `MAPA`, `HEARTBEAT`, `SOUL`, `USER`, `TOOLS` e `MEMORY`.

## Escopo não tocado

Não houve alteração em:

- runtime/gateway/bots;
- Telegram polling/webhook/API server;
- crons;
- Docker/VPS/SSH/Traefik/volumes/networks;
- Shopify, Tiny, Klaviyo, Meta, Google Ads, GMC, CRM ou qualquer sistema externo;
- secrets ou credenciais.

## Guardrails preservados

- Shopify continua como superfície, Tiny como fonte de verdade de estoque.
- Writes externos continuam bloqueados sem aprovação explícita e escopada.
- LK Growth, LK Shopify, LK Ops, LK Trends, LK CRM, LK E-commerce e LK Tráfego Pago ficam separados por dono lógico e handoff.
- Sucesso rotineiro continua silent-OK; Telegram deve receber decisões, exceções e aprovações, não ruído.
