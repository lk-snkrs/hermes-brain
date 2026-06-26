# Handoff — Auditoria organograma Hermes/Cimino vs Amora

Data: 2026-05-26  
Owner: Hermes Geral / COO  
Escopo: auditoria local/read-only de governança, organograma, Brain, profiles, crons, segurança e performance.  
Produção/runtime: nenhuma alteração; sem restart, sem migração de cron, sem writes externos.

## Resultado

Relatório gerado em:

- `reports/governance/auditoria-completa-governanca-organograma-hermes-vs-amora-2026-05-26.md`

Nota geral: **7,9/10**.

Veredito: organograma conceitualmente correto, mais seguro que uma cópia direta da Amora para ambiente multiempresa, mas ainda abaixo da maturidade ritual/identitária da Amora.

## Tese operacional

Não adicionar agentes ou prompts por padrão. Fechar primeiro o ciclo:

`pedido → router → executor certo → preview/ação segura → receipt → handoff → Brain → skill/rotina`.

## Principais gaps

- Organograma canônico precisa refletir todos os profiles ativos: LK Ops, LK Shopify, LK Trends e SPITI runtime.
- Main e Mordomo ainda carregam rotinas LK Ops/Zipper por histórico.
- LK Shopify e LK Trends precisam pacote documental mais claro.
- SPITI precisa declarar se não terá crons próprios ou quais rituais futuros quer.
- Handoffs/receipts precisam regra mais uniforme.
- Migração de cron, restart, launcher/env, bot/profile novo e qualquer write externo exigem aprovação explícita.

## Próximo passo recomendado

Fazer pacote local/read-only:

1. Atualizar organograma canônico com status documental/runtime.
2. Criar matriz `agente → dono → profile → bot → área Brain → cron registry → status`.
3. Completar docs de LK Shopify e LK Trends.
4. Classificar D+7 Growth e rotinas Main/Mordomo por dono lógico.

## Verificação

- Brain health check executado: 0 FAIL; warnings existentes de MAPA/rotinas não indexadas.
- Secret scan focado do relatório: nenhum padrão sensível encontrado.
