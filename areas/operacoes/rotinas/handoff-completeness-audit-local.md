# Rotina — Auditoria local de handoff completeness

Status: ativa como rotina local/read-only  
Owner: Hermes Geral / COO  
Cadência recomendada: semanal ou após rodadas intensas de especialistas  
Writes externos: não

## Objetivo

Encontrar outputs materiais sem handoff/receipt central antes que contexto se perca por compactação, troca de profile ou passagem de tempo.

## O que conta como output material

Exige handoff ou receipt linkado quando houver:

- approval packet;
- receipt de dev/produção/theme/feed/API;
- write externo aprovado;
- relatório que muda prioridade;
- bloqueio que exige Lucas;
- aprendizado/correção durável;
- publicação, rollback ou verificação pós-write;
- PR/issue/deploy packet;
- decisão customer-facing.

## Fontes a varrer

- `empresa/contexto/handoffs/`
- `reports/governance/`
- `areas/**/reports/`
- `areas/**/receipts/`
- `areas/**/decisions/`
- `areas/**/approval*`
- MAPAs das áreas afetadas

## Saída

Salvar em:

`reports/governance/handoff-completeness-check-YYYY-MM-DD.md`

## Procedimento

1. Listar outputs materiais recentes.
2. Verificar se cada output tem:
   - owner;
   - data/hora;
   - fonte/evidência;
   - status;
   - bloqueios/aprovação quando aplicável;
   - rollback/readback quando aplicável;
   - link no handoff central ou MAPA.
3. Classificar:
   - `ok`;
   - `gap_corrigivel_documentalmente`;
   - `gap_precisa_contexto_Lucas`;
   - `gap_runtime/infra`.
4. Corrigir automaticamente apenas gaps documentais com fatos suficientes nos próprios artefatos.
5. Para gaps de runtime/infra, preparar packet; não executar mutação.

## Não fazer

- Não inventar aprovação retroativa.
- Não registrar checks saudáveis sem consequência.
- Não alterar produção para “verificar”.
- Não criar cron novo sem aprovação.

## Critério de done

A auditoria só está fechada quando:

- gaps corrigíveis foram corrigidos localmente;
- gaps não corrigíveis foram classificados;
- relatório foi salvo;
- handoff central foi atualizado se houve correção material;
- secret scan e brain health passaram quando houve edição documental.
