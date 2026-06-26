# HEARTBEAT — Hermes Brain

Configuração documental de proatividade do Brain. Este arquivo não prova cron ativo.

A configuração operacional detalhada do Hermes Geral está em:

- `agentes/hermes-geral/HEARTBEAT.md`

## Decisão atual

Não ativar cron novo automaticamente.

Fluxo correto:

1. Documentar rotina.
2. Rodar sob demanda.
3. Validar valor e ruído.
4. Propor agenda, destino, critérios de silêncio, erro e kill criteria.
5. Ativar cron só com aprovação de cadência/escopo ou autorização já documentada.

## Checks candidatos

- Hermes runtime / Telegram / cron: read-only; restart/deploy/Docker/VPS exigem aprovação.
- Brain / Mission Control: git status, pendências, rotinas documentadas vs crons reais.
- LK OS: reports obrigatórios, blockers `needs_data`, GMC/stock/sourcing/CRM em modo read-only/preview.
- Zipper / SPITI: pendências, prazos, rascunhos internos e riscos; sem contato externo.

## Regra de silêncio

Silêncio é o padrão quando não há ação necessária. Não enviar “tudo certo” gratuito.
