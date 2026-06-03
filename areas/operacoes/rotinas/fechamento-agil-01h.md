# Rotina — Hermes Brain Fechamento Ágil 01h + Pacote de Handoff

Status: **ativa como cron recorrente aprovado por Lucas**
Atualizada em: 2026-06-02 UTC
Área: Operações / Hermes Brain / Grande Mente

## Objetivo

Consolidar diariamente os fatos operacionais relevantes do dia anterior e entregar um **pacote de handoff completo** para o Daily Intelligence Loop das 02h. O objetivo não é só arquivar contexto: é capturar padrões de aprovação/correção de Lucas para que Hermes aprenda, reduza repetição de erro e ganhe autonomia A0/A1 com segurança.

## Cadência

- Horário operacional: **01h BRT**.
- Cron UTC: `0 4 * * *`.
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Delivery: `local`.
- Telegram: somente exceção, falha crítica, risco, decisão urgente ou quando Lucas pedir.

## Artefatos obrigatórios

1. Relatório diário Markdown:

```text
reports/daily-consolidation/YYYY-MM-DD.md
```

2. Pacote estruturado para o 02h:

```text
reports/daily-consolidation/latest-handoff.json
reports/daily-consolidation/YYYY-MM-DD-handoff.json
```

O JSON deve ser sanitizado e não conter segredos, transcrições integrais, HTML bruto, tokens, connection strings ou dados vivos não verificados.

## Template do relatório Markdown

```md
# Fechamento Ágil — YYYY-MM-DD

## 1. Resumo executivo
## 2. Hoje foi feito
## 3. Decisões do dia
## 4. Pendências e bloqueios
## 5. Crons e automações
## 6. Handoffs de especialistas
## 7. Riscos / guardrails
## 8. Amanhã
## 9. Promover para memória/skills/rotinas
## 10. Pacote de aprendizado para 02h
## 11. Fontes
```

## Contrato do `latest-handoff.json`

Campos recomendados:

```json
{
  "operational_date": "YYYY-MM-DD",
  "generated_at_utc": "...",
  "status": "ok|attention|action_required",
  "executive_summary": "...",
  "material_changes": [],
  "incidents": [],
  "decisions_made_by_lucas": [],
  "approvals_and_corrections": [],
  "learning_ledger_candidates": [],
  "autonomy_pattern_candidates": [],
  "pending_decisions_for_lucas": [],
  "safe_next_actions": [],
  "blocked_actions_requiring_approval": [],
  "cron_and_delivery_truth": [],
  "sources": [],
  "sanitization": {
    "secrets_redacted": true,
    "raw_chat_transcripts_excluded": true,
    "live_facts_verified": true
  }
}
```

## O que capturar como aprendizado

Capturar especialmente:

- aprovações explícitas de Lucas e qual escopo elas autorizaram;
- correções de Lucas sobre comportamento, linguagem, autonomia ou ruído;
- diferença entre relatório gerado e entregue;
- padrões de decisão que podem virar A0/A1 amanhã;
- ações que ainda exigem A3/A4 por risco, segredo, produção, dinheiro, cliente ou fonte de verdade;
- pontos em que Hermes pediu aprovação demais, de menos ou parou cedo;
- watchdogs ou crons que geraram ruído e deveriam virar silent-OK;
- gaps documentais que podem ser corrigidos localmente.

## Critério de inclusão

Incluir apenas fatos com sinal operacional: decisão, aprovação, pendência, bloqueio, risco, receipt, write externo aprovado, falha, aprendizado durável, mudança de rotina ou correção feita por Lucas.

Não incluir: transcrição integral de chat, status sem ação, HTML bruto, segredos, tokens, senhas, keys, connection strings ou dado vivo não verificado.

## Cobertura mínima

Verificar todos, mesmo que o resultado seja “sem evidência operacional nova”:

- Hermes Geral / Grande Mente;
- Lucas pessoal / Mordomo;
- LK OS;
- LK Growth OS;
- Zipper OS;
- SPITI OS;
- ZIZ OS, se houver evidência;
- Mission Control;
- watchdogs e crons script-only.

## Segurança

- Sem WhatsApp, e-mail, campanha, proposta, cliente, fornecedor ou envio externo.
- Sem write em Shopify, Tiny, GMC, Ads, Klaviyo, Supabase, banco, Docker, VPS ou gateway.
- Sem expor credenciais. Usar `[REDACTED]` se algum nome sensível aparecer.
- Se houver dúvida entre silêncio e dado errado, marcar como `a validar`.

## Validação esperada

Após escrever os artefatos:

1. Ler de volta o Markdown e o JSON.
2. Validar JSON parseável.
3. Rodar secret scan direcionado nos artefatos gerados.
4. Registrar fontes usadas.
5. Rodar Brain Sync seguro pós-fechamento, respeitando allowlist e secret scan:

```bash
/opt/data/scripts/brain_sync_safe.py --push
```

## Relação com 02h e 02h30

- 01h = consolidação + pacote de aprendizado.
- 02h = supervisor de inteligência, promoção de aprendizado e auto-melhoria segura.
- 02h15 = higiene de memória e receipt local.
- 02h30 = digest executivo para Lucas: o que aconteceu, o que Hermes fez, como Hermes se auto-melhorou e o que precisa de Lucas.
