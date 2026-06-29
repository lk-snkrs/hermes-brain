# Approval packet — Honcho provider snapshot + historical cleanup readiness

## Pedido

Preparar limpeza histórica de contaminação semântica do Honcho, começando por snapshot/rollback e confirmação de granularidade de delete. Não executar deletion sem nova aprovação após prova de rollback.

## Por que importa

Auditoria pós-best-practice detectou contaminação semântica histórica alta em resultados de busca Honcho, apesar de o filtro de ingestão novo estar ativo.

## Evidência sanitizada

- Utility status: `attention`.
- Utility score: `80`.
- Semantic contamination ratio: `0.75`.
- Cleanup candidates: `173` hashes sanitizados.
- Safe to delete now: `False`.
- `raw_content_printed=false`; `values_printed=false`.

## Escopo aprovado nesta etapa se Lucas disser Fazer

1. Criar snapshot/backup verificável do provider Honcho local.
2. Confirmar granularidade de exclusão suportada: mensagem, sessão, peer/conclusion, ou somente DB-level.
3. Produzir dry-run de limpeza com hashes/contagens, sem raw content.
4. Gerar rollback/readback plan.

## Fora de escopo nesta etapa

- Não deletar mensagens/conclusões/sessões ainda.
- Não resetar workspace.
- Não alterar Brain/memórias canônicas.
- Não expor raw content, PII, pedidos, clientes, tokens ou secrets.

## Requisitos de segurança

- Backup/snapshot antes de qualquer delete.
- Readback depois de qualquer delete futuro.
- Novo approval específico para a etapa destrutiva.
- `values_printed=false`.

## Rollback esperado

Restaurar snapshot Honcho local e validar `/health`, `hermes memory status`, search probe e watchdogs.
