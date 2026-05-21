# Memória quente — contexto current

Atualizado: 2026-05-20 17:25 UTC  
Status: camada Bruno/OpenClaw criada para evitar perda por compactação.

## Prioridades current

1. Manter o Hermes Brain como fonte de verdade, não o chat.
2. Garantir que decisões customer-facing aprovadas por Lucas virem arquivo vivo, MAPA/índice e evidência de verificação.
3. Manter o Fechamento Ágil 23h + Brain Sync seguro como rotina de consolidação silenciosa/local.
4. Evitar ruído no Telegram: sucesso normal fica local/Brain; Lucas recebe decisão, exceção, falha ou pedido de aprovação.

## Decisões recentes que não podem sumir

- Decisões de copy/tom/fluxo customer-facing precisam ser registradas imediatamente usando `areas/operacoes/templates/decisao-customer-facing.md`.
- Decisão viva prevalece sobre playbook antigo quando houver conflito.
- Reports brutos continuam bloqueados; apenas evidência curada entra em `reports/governance/`.
- Especialista pode executar dentro do escopo, mas precisa deixar handoff/receipt para o Hermes Central.

## Links quentes

- `areas/operacoes/rotinas/protocolo-registro-decisoes-aprovadas-contexto-compactado.md`
- `areas/operacoes/templates/decisao-customer-facing.md`
- `areas/operacoes/rotinas/brain-sync.md`
- `areas/operacoes/rotinas/fechamento-agil-23h.md`
- `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`
- `reports/governance/`

## Bloqueios/guardrails current

- Não alterar Docker/VPS/Traefik/volumes/redes/containers sem aprovação explícita e plano de rollback.
- Não executar writes externos em Shopify/GMC/WhatsApp/e-mail/banco/campanhas sem fonte e aprovação adequada ao escopo.
- Não expor tokens, secrets ou payloads sensíveis em Telegram ou docs versionáveis.
- Documentação de rotina não prova execução ativa; crons/canais precisam de evidência runtime quando afirmados como ativos.

## Próxima revisão

Atualizar no fechamento diário ou sempre que Lucas corrigir prioridade/decisão que afete execução contínua.
