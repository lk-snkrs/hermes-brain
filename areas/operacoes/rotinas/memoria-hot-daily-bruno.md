# Rotina — Memória hot/daily no padrão Bruno/OpenClaw

Status: ativo como governança documental  
Criada: 2026-05-20  
Escopo: Hermes Brain / Memória / Compactação

## Objetivo

Garantir que o Hermes não dependa de chat, compactação ou memória implícita para continuar operando. O que importa precisa existir em arquivo versionável, navegável e atualizado.

## Camadas obrigatórias

1. `memories/hot.md`
   - contexto quente/current;
   - prioridades da semana/dia;
   - decisões recentes que ainda afetam execução;
   - bloqueios e guardrails ativos;
   - links para arquivos vivos.

2. `memories/daily/YYYY-MM-DD.md`
   - daily note curada;
   - decisões, entregas, pendências, aprendizados e não-ações;
   - não é transcrição de chat.

3. Arquivo vivo na área certa
   - decisões customer-facing em `areas/**/decisions/`;
   - receipts em `areas/**/receipts/` quando houver execução;
   - rotinas/templates/PRDs quando virar processo repetível.

4. `MAPA.md` local
   - toda decisão/rotina/pasta nova precisa ser encontrável pelo próximo agente.

## Quando atualizar

Atualizar imediatamente quando houver:

- correção de Lucas;
- aprovação de copy/tom/fluxo;
- decisão de autonomia ou guardrail;
- pendência com prazo;
- risco/bloqueio que não pode sumir;
- mudança de cron, canal ou rotina;
- aprendizado repetível.

Atualizar no fechamento 23h mesmo quando não houver ação imediata, desde que exista contexto do dia que precise sobreviver.

## Formato mínimo da daily note

```md
# Daily memory — YYYY-MM-DD

## Decisões
- ...

## Entregas
- ...

## Pendências
- ...

## Aprendizados
- ...

## Não-ações / guardrails respeitados
- ...

## Próxima ação
- ...
```

## Guardrails

- Não registrar segredo, payload bruto, PII desnecessária ou logs completos.
- Não transformar daily note em histórico de chat.
- Se a decisão afeta cliente, usar também o template `areas/operacoes/templates/decisao-customer-facing.md`.
- Se a informação for de uma empresa específica, preferir arquivo na área correspondente e só resumir/linkar em `hot.md`/daily.

## Verificação

Antes de dizer que o padrão Bruno está coberto:

- existe `memories/MAPA.md`;
- existe `memories/hot.md`;
- existe daily note do dia quando houve decisão/execução relevante;
- links quentes apontam para arquivos reais;
- health check e secret scan passam.
