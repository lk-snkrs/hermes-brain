# Follow-through — Organograma Hermes vs Amora: correções 1/2/3/4

Data: 2026-05-27
Escopo: local/documental/read-only.

## Pedido

Executar os quatro ajustes definidos após a comparação com a estrutura da Amora:

1. fechar contratos por especialista;
2. padronizar handoff/receipt;
3. limpar o que ainda está no Main/Mordomo por histórico;
4. manter runtime, dono lógico e cron explicitamente separados.

## Princípio preservado

A correção foi feita sem reduzir autonomia dos agentes. A documentação passou a definir fronteira, contexto e governança — não microgestão de execução.

## O que foi alterado

### 1) Contrato por especialista

Atualizei o organograma para reforçar que cada pacote documental define a fronteira do especialista, sem centralizar execução desnecessariamente.

### 2) Handoff/receipt padronizado

Atualizei o protocolo de handoff para incluir:

- um formato canônico de receipt;
- a regra de que handoff não é reaprovação;
- a regra de que a autonomia do especialista é preservada pelo próprio registro.

### 3) Histórico no Main/Mordomo

O organograma passou a tratar as rotinas históricas no Main/Mordomo como temporárias e explicitamente rotuladas por dono lógico, até eventual migração aprovada.

### 4) Separação owner/runtime/cron

A documentação reforça que:

- dono lógico não é automaticamente runtime;
- runtime não é automaticamente cron owner;
- aprovação escopada destrava execução dentro do escopo aprovado;
- `seguir` continua significando continuidade documental/local, não write externo.

## Verificações

- `brain_health_check.py`:
  - `FAIL=0`
  - `WARN=0`
- `operational_docs_guard.py`:
  - `fail_count=0`
- Secret scan focado nas mudanças:
  - `0 findings`

## Escopo não tocado

- runtime/gateway/bots;
- crons;
- Docker/VPS/SSH/Traefik;
- Shopify/Tiny/Klaviyo/Meta/Google Ads/GMC/CRM;
- secrets.

## Resultado

O organograma ficou mais próximo da maturidade da Amora em uniformidade operacional, mas sem copiar o modelo de forma literal e sem sacrificar a autonomia dos especialistas.
