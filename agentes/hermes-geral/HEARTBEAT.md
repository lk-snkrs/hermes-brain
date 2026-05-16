# HEARTBEAT — Hermes Geral

> Configuração documental de proatividade. Este arquivo não prova cron ativo. Antes de afirmar execução recorrente, verificar `cronjob list`/runtime real.

## Política atual

Não ativar cron automático novo apenas porque a rotina existe.

Sequência aprovada:

1. Documentar rotina.
2. Rodar sob demanda.
3. Medir utilidade e ruído.
4. Propor agenda/destino/kill criteria.
5. Ativar cron só com aprovação de cadência ou autorização já documentada.

## Frequência sugerida se virar cron

- Inicial: 1 vez por dia útil ou sob demanda, não 30 minutos.
- Janela ativa: 08:00–19:00 BRT.
- Quiet hours: 19:00–08:00 BRT, salvo risco real.
- Alertar Lucas apenas se houver ação necessária, decisão pendente, risco real ou oportunidade clara.

## Checks candidatos

Começar com poucos checks. Não ativar tudo junto.

### P0 — Hermes runtime / Telegram / cron

- Gateway Telegram saudável.
- Cronjobs críticos sem falha recente.
- Runtime Hermes consistente com versão esperada.
- Logs sem erro repetitivo novo.

Ação permitida: read-only, diagnóstico e relatório. Restart/deploy/Docker/VPS exige aprovação.

### P1 — Brain e Mission Control

- Git status limpo ou divergência documentada.
- Worktrees/orfãos/relatórios pendentes classificados.
- Rotinas documentadas vs crons reais reconciliados.
- Pendências em `empresa/gestao/pendencias.md` sem envelhecimento crítico.

Ação permitida: organizar docs, relatórios, índices e pendências locais.

### P1 — LK OS

- Reports obrigatórios entregues conforme cadência aprovada.
- Blockers `needs_data` resolvíveis por lookup read-only/local.
- GMC/stock/sourcing/CRM pendentes separados entre preview, approval-gated e read-only.

Ação permitida: read-only/local/previews. Campanha, contato, Shopify/Tiny/Merchant/Klaviyo/Meta ou compra continuam bloqueados.

### P2 — Zipper / SPITI

- Pendências claras em Brain/Mission Control.
- Oportunidades de rascunho interno.
- Sinais de risco, prazo, feira, logística ou leilão.

Ação permitida: rascunho e documentação. Contato externo/deploy/lance/dado de leilão sem fonte continuam bloqueados.

## Regras de silêncio

Ficar silencioso quando:

- nada mudou desde a última checagem;
- só há informação “tudo certo”;
- a pendência não requer decisão/action de Lucas;
- a checagem exigiria fonte viva não autorizada;
- está em quiet hours e não é urgência real.

## Regras de reach out

Interromper Lucas apenas quando:

- há falha real em Hermes/Telegram/cron que afeta operação;
- existe decisão de Lucas necessária para destravar receita, prazo ou risco;
- uma pendência crítica envelheceu;
- um relatório obrigatório aprovado falhou ou atrasou;
- surgiu oportunidade forte e verificável.

## Anti-spam

- Não mandar “HEARTBEAT_OK” para Lucas; silêncio é OK.
- Não repetir alertas iguais.
- Não criar vários crons para checks que podem ser uma revisão única.
- Não confundir P0/P1/P2 com permissão de agir externamente.
