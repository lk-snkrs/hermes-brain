# MAPA — Hermes

Área documental para receipts e evidências internas do próprio Hermes runtime/orquestração quando o artefato não pertence claramente a LK, Zipper, SPITI, Mordomo ou Operações.

## Escopo

- Receipts de UX do Hermes, crons e Telegram quando forem específicos do runtime Hermes.
- Evidências locais/read-only de correções de entrega, formatação ou roteamento.
- Ponte para governança central em `areas/operacoes/` e `empresa/contexto/`.

## Guardrails

- Esta área não autoriza Docker, VPS, gateway, cron, segredo, banco, produção ou external write.
- Correções runtime continuam sujeitas a aprovação escopada, backup/rollback e receipts.
- Sucesso normal de watchdogs deve permanecer `local`/silencioso.

## Navegação

- Receipts: `operacoes/receipts/`
- Rotinas canônicas relacionadas: `areas/operacoes/rotinas/`
- Organograma e roteamento: `empresa/contexto/`
