# Rotina — SPITI Pós-leilão e Lessons

## Objetivo

Fechar cada pregão/leilão SPITI com registro verificável de resultado, divergências, decisões e lições aprendidas, sem transformar memória temporária em verdade permanente sem fonte.

## Quando usar

- Após encerramento do pregão.
- Após reconciliação de lances/lotes/consignantes.
- Após incidente de monitor, n8n, email, site ou banco.
- Antes de atualizar memória executiva SPITI.

## Entradas obrigatórias

1. Relatório interno usando `areas/spiti/templates/relatorio-interno-matriz-evidencia.md`.
2. Fontes consultadas e horário de coleta.
3. Divergências abertas e status de resolução.
4. Decisões tomadas por Lucas/equipe.
5. Ações externas realizadas com aprovação.

## Procedimento

1. Consolidar fontes em relatório interno.
2. Separar fatos confirmados, hipóteses e lacunas.
3. Registrar incidentes/falhas conhecidas.
4. Atualizar `areas/spiti/contexto/lessons.md` com lições duráveis.
5. Atualizar `areas/spiti/contexto/decisions.md` se houve decisão operacional permanente.
6. Atualizar `memories/spiti.md` apenas com memória executiva compacta e estável.
7. Se houver procedimento repetível novo, transformar em rotina ou skill.
8. Rodar health check do Brain e scan de secrets antes de commit.

## O que registrar em lessons

- Fonte que se mostrou mais confiável.
- Falhas de scraper/monitor/n8n/email/site.
- Ambiguidade que gerou risco de dado errado.
- Correção preventiva adotada.
- Sinal de alerta para próxima edição.

## O que registrar em decisions

- Mudança de fonte de verdade.
- Aprovação de novo fluxo de envio/alerta.
- Decisão de desativar/ativar monitor.
- Regra de comunicação com grupo/cliente.
- Alteração de responsabilidade operacional.

## O que não registrar como memória permanente

- Status transitório de um lote sem fechamento.
- Hipótese ainda sem fonte.
- Dado vivo que deve ser consultado no Supabase/email/site.
- Token, senha, webhook secret ou qualquer credencial.

## Checklist final

- [ ] Relatório interno tem matriz de evidência.
- [ ] Divergências estão marcadas como resolvidas/pendentes.
- [ ] Nenhuma mensagem externa foi enviada sem aprovação.
- [ ] Lessons/decisions atualizadas somente com fatos duráveis.
- [ ] `scripts/brain_health_check.py` passou.
- [ ] Secret scan retornou `possible_secrets 0`.
