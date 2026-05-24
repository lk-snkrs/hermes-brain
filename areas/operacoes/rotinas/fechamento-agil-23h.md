# Rotina — Hermes Brain Fechamento Ágil 23h

Status: **ativa como cron recorrente aprovado por Lucas após Fase 1A**
Criada em: 2026-05-20 UTC
Área: Operações / Hermes Brain / Grande Mente

## 1. Objetivo

Consolidar diariamente, no Brain, os fatos operacionais relevantes do dia de Lucas e das empresas/OS conectadas, reduzindo perda de contexto por:

- compactação de chat;
- execução em profiles/bots especialistas;
- crons script-only;
- outputs que ficam só em Telegram/WhatsApp/e-mail;
- projetos sem receipt documental.

A rotina não é mais um relatório para Lucas. É a camada Brain-first que alimenta memória operacional e a Mesa COO da manhã.

## 2. Cadência

- Horário operacional: **23h BRT**.
- Cron UTC: `0 2 * * *`.
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Delivery: `local`.
- Telegram: somente exceção, falha crítica, risco, decisão pendente urgente ou quando Lucas pedir.

## 3. Artefato de saída

Arquivo diário:

```text
reports/daily-consolidation/YYYY-MM-DD.md
```

Template obrigatório:

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
## 10. Fontes
```

## 4. Fontes obrigatórias

Antes de escrever o fechamento, consultar quando disponíveis:

- `areas/operacoes/inventarios/crons-agentes-profiles.md`;
- `areas/operacoes/brds/hermes-brain-fechamento-agil-23h-brd-2026-05-19.md`;
- `empresa/contexto/organograma-agentes-hermes.md`;
- `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`;
- `reports/` e subpastas relevantes com arquivos do dia;
- `areas/*/` para LK, Zipper, SPITI, Operações e projetos recentes;
- `cronjob list` para estado vivo dos jobs;
- `session_search` para conversas recentes relevantes, sem tentar transcrever tudo.

## 5. Critério de inclusão

Incluir apenas fatos que tenham sinal operacional:

- decisão;
- aprovação;
- pendência/follow-up;
- bloqueio;
- risco;
- entrega/receipt;
- write externo aprovado;
- falha/exceção;
- aprendizado durável;
- mudança de projeto/rotina;
- correção feita por Lucas.

Não incluir:

- transcrição integral de chat;
- status sem ação;
- HTML/artefato bruto;
- segredos, tokens, senhas, keys ou connection strings;
- dado vivo não verificado.

## 6. Cobertura mínima por domínio

Verificar todos, mesmo que o resultado seja “sem evidência relevante hoje”:

- Hermes Geral / Grande Mente;
- Lucas pessoal / Mordomo;
- LK OS;
- LK Growth OS;
- Zipper OS;
- SPITI OS;
- ZIZ OS, se houver evidência;
- Mission Control;
- watchdogs e crons script-only.

## 7. Regras de baixo ruído

- Sucesso normal fica no arquivo local/Brain.
- Telegram principal não recebe status/HTML de sucesso.
- Se o fechamento falhar, ou detectar risco/decisão urgente para amanhã, o job pode reportar exceção de forma curta.
- Relatórios LK seguem a regra: Telegram só decisões/exceções/falhas; não status/HTML de sucesso.

## 8. Segurança

- Sem WhatsApp, e-mail, campanha, proposta, cliente, fornecedor ou qualquer envio externo.
- Sem write em Shopify, Tiny, GMC, Ads, Klaviyo, Supabase, banco, Docker, VPS ou gateway.
- Sem expor credenciais. Usar `[REDACTED]` se algum nome sensível aparecer.
- Se houver dúvida entre silêncio e dado errado, marcar como `a validar`.

## 9. Validação esperada

Após escrever o relatório diário:

1. Confirmar que o arquivo existe.
2. Rodar secret scan simples no arquivo gerado.
3. Se possível, rodar health check do Brain periodicamente ou quando houver alteração estrutural.
4. Registrar fontes usadas na seção 10.
5. Rodar Brain Sync seguro pós-fechamento para versionar o relatório e os documentos Brain permitidos:

```bash
/opt/data/scripts/brain_sync_safe.py --push
```

O sync deve respeitar a rotina `areas/operacoes/rotinas/brain-sync.md`: allowlist documental, sem `config/`, sem `scripts/`, sem HTML/artefatos grandes, com secret scan antes de qualquer commit/push.

## 10. Relação com Mesa COO

A Mesa COO da manhã deve usar o arquivo mais recente de `reports/daily-consolidation/` como fonte prioritária quando existir, transformando o fechamento em decisões e desbloqueios curtos para Lucas.

Fechamento 23h = consolidação documental.
Mesa COO = superfície executiva de decisão.

## 11. Histórico de aprovação

- BRD aprovado para Fase 1A por Lucas: inventário vivo + teste manual.
- Fase 1A executada com FAIL=0 em health/secret scan dos novos artefatos.
- Após o teste, Lucas disse “Seguir”, autorizando o próximo bloco seguro: rotina canônica + integração Mesa + cron recorrente local.
