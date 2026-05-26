# MAPA — SPITI OS

Status: mapa documental e operacional do SPITI OS.

## Ler primeiro

1. `agentes/spiti/IDENTITY.md`.
2. `agentes/spiti/AGENTS.md`.
3. `agentes/spiti/HEARTBEAT.md`.
4. `areas/spiti/MAPA.md` quando existir/for aplicável.
5. Referências de Hub/Financial/Supabase antes de qualquer claim operacional.

## Onde salvar

- Relatórios SPITI: `areas/spiti/reports/` ou subárea equivalente.
- PRDs/projetos: `areas/spiti/projetos/` quando a estrutura existir.
- Baseline de crons locais: `areas/spiti/projetos/spiti-cron-registry-baseline-2026-05-25.md`.
- Handoffs: seguir `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`.
- Código: usar repositórios SPITI com branch/PR seguro, nunca direto em produção.

## Roteamento rápido

- Hub/CRM/lotes/leilões/Financial/Growth SPITI → SPITI profile.
- Lances/lotes/status sensível → fonte oficial obrigatória.
- Banco/deploy/publicação/cliente/bidder → approval packet; write bloqueado.
- IA de obras/matching → interno assistivo, nunca contato automático.

## Regra de qualidade

Se a fonte não fecha, responder “não verificado” e registrar o gap em vez de inferir.
