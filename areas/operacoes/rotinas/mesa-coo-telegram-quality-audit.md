# Rotina — Auditoria de qualidade da Mesa COO no Telegram

Status: ativa como rotina local/read-only  
Owner: Hermes Geral / COO  
Cadência: após cada entrega real relevante da Mesa COO ou sob demanda de Lucas  
Writes externos: não  
Runtime mutation: não

## Objetivo

Validar se a Mesa COO chegou para Lucas como decisão executiva limpa, sem ruído técnico, e se o conteúdo merece atenção.

Esta rotina não cria cron, não reinicia gateway, não altera scheduler e não muda delivery. Ela só audita a próxima entrega real e registra evidência.

## Critérios de aprovação

A entrega é considerada limpa quando:

1. Não aparece `Cronjob Response`, job id, JSON, HTML comment, marker técnico ou boilerplate de gerenciamento.
2. Há uma decisão clara por mensagem.
3. A decisão tem contexto curto, risco/limite e próxima ação.
4. Se houver botões, eles são nativos e não aparecem como payload textual.
5. A pergunta para Lucas é útil: muda prioridade, risco, dinheiro, cliente, produção ou desbloqueio relevante.

## Classificação

- `validada`: passou em UX e utilidade.
- `limpa_mas_fraca`: não vazou metadata, mas a decisão não era executiva o bastante.
- `suja`: vazou wrapper, JSON, job id, HTML marker ou config boilerplate.
- `não_observada`: entrega ainda não ocorreu ou não há evidência visual/textual suficiente.

## Procedimento

1. Verificar a entrega real recebida por Lucas.
2. Registrar evidência textual mínima sem expor payload técnico desnecessário.
3. Classificar usando os critérios acima.
4. Se `validada`, registrar em `empresa/contexto/handoffs/YYYY-MM-DD.md` e atualizar o status da Fase 8.
5. Se `limpa_mas_fraca`, registrar melhoria de conteúdo da Mesa COO.
6. Se `suja`, preparar packet de correção scheduler/gateway com teste e rollback; não reiniciar gateway/Docker sem aprovação.

## Template de receipt

```md
# Receipt — Mesa COO Telegram quality audit

Data/hora:
Entrega auditada:
Classificação: validada | limpa_mas_fraca | suja | não_observada

Checklist:
- Sem wrapper/job_id/JSON/marker: sim/não
- Uma decisão por mensagem: sim/não
- Botões nativos quando aplicável: sim/não/n/a
- Conteúdo executivo: sim/não
- Próxima ação clara: sim/não

Evidência:

Risco:

Próximo passo:
```

## Guardrails

- Não criar cron novo para esta auditoria sem aprovação explícita.
- Não alterar gateway/scheduler em produção sem packet aprovado.
- Não mandar Telegram de sucesso normal; registrar no Brain.
