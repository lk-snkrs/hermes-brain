# Revisão Semanal Multiempresa — Hermes Chief of Staff

> Rotina Hermes-native inspirada nos cases OpenClaw Amora/Filippe, adaptada para Lucas Cimino. Esta rotina é documental; rotina documentada não prova cron ativo.

## Objetivo

Produzir uma revisão executiva semanal para Lucas, consolidando **LK OS**, **Zipper OS**, **SPITI OS** e infraestrutura Hermes, sem misturar contextos ou executar ações externas.

## Quando usar

- Manualmente, quando Lucas pedir “revisão semanal”, “status geral”, “o que temos pendente?” ou “seguir” após uma rodada de organização multiempresa.
- Futuramente como cron Hermes, se Lucas aprovar agenda e formato.

## Skills relacionadas

- `lucas-chief-of-staff`
- `multiempresa-routing-lucas`
- `bruno-openclaw-hermes-brain-adaptation`
- Skills específicas por negócio quando aplicável.

## Escopo

### LK OS — LK Sneakers

- Pendências de CRM/campanhas.
- Oportunidades de cross-sell/leads esfriando.
- Alertas de dados/integrações se houver evidência.
- Nenhum envio externo sem preview + aprovação Lucas.

### Zipper OS — Zipper Galeria

- Pendências de obras, colecionadores, feiras e comunicação.
- Rascunhos ou oportunidades comerciais apenas como proposta interna.
- Nenhum contato/publicação/proposta sem aprovação Lucas/Osmar/responsável.

### SPITI OS — SPITI Auction

- Pendências de leilão, Spiti Hub, lances, SEO/conteúdo e analytics.
- Dados de lances só com fonte verificada; se não houver fonte, registrar como desconhecido.
- Nenhum deploy/merge/migração/email/post sem aprovação Lucas.

### Hermes/Infra

- Estado geral do Hermes Brain, skills, rotinas e crons.
- VPS/Docker/Telegram apenas read-only, salvo aprovação explícita com plano de backup/rollback.

## Entrada esperada

- Pedido do Lucas ou cron futuro.
- Contexto recente da conversa via `session_search` quando relevante.
- Hermes Brain: `memories/`, `areas/`, `empresa/rotinas/_index.md`, `CHANGELOG.md`, `ROADMAP-30-DIAS-HERMES.md`.
- Dados vivos somente quando a rotina exigir e houver autorização/credenciais seguras.

## Procedimento

1. Carregar `lucas-chief-of-staff` e `multiempresa-routing-lucas`.
2. Verificar se existe contexto recente relevante com `session_search`.
3. Ler os resumos/arquivos necessários do Hermes Brain.
4. Separar a revisão em quatro blocos: LK OS, Zipper OS, SPITI OS, Hermes/Infra.
5. Para cada bloco, listar:
   - status conhecido;
   - pendências;
   - riscos;
   - decisões necessárias;
   - próximas ações recomendadas.
6. Marcar explicitamente o que é fato verificado vs. hipótese/recomendação.
7. Não executar ações externas; apenas gerar plano/preview.
8. Se alguma próxima ação for sensível, pedir aprovação antes de executar.

## Formato de saída para Lucas

```markdown
## Revisão semanal — [data]

### LK OS — LK Sneakers
- Status:
- Pendências:
- Riscos:
- Próximas ações:

### Zipper OS — Zipper Galeria
- Status:
- Pendências:
- Riscos:
- Próximas ações:

### SPITI OS — SPITI Auction
- Status:
- Pendências:
- Riscos:
- Próximas ações:

### Hermes / Infra
- Status:
- Pendências:
- Riscos:
- Próximas ações:

### Decisões que preciso de você
1. ...

### Posso executar sem risco agora
1. ...
```

## Guardrails

- Não inventar métricas.
- Não misturar LK/Zipper/SPITI.
- Não imprimir segredos.
- Não enviar contato externo.
- Não alterar produção/infra sem aprovação.
- SPITI: silêncio é melhor do que dado errado.

## Verificação

Antes de dizer que a revisão está pronta:

- conferir que cada bloco cita fonte ou deixa claro que é recomendação;
- conferir que nenhuma ação externa foi executada;
- conferir que decisões sensíveis estão separadas como “precisa de aprovação”.

## Status de automação

- Estado atual: documentada, não necessariamente agendada.
- Próximo passo possível: criar cron Hermes semanal, se Lucas aprovar dia/horário e canal de entrega.
