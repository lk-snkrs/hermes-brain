# Approval packet — Honcho historical cleanup migrator dry-run/readback

## Pedido

Autorizar a próxima etapa segura: criar e executar um migrator **somente em dry-run/readback**, sem commit/delete, para provar exatamente o blast radius de uma limpeza message-level no banco Honcho.

## Contexto

A etapa aprovada em 2026-06-28 foi concluída:

- snapshot lógico PostgreSQL criado;
- checksum e smoke gzip OK;
- granularidade de delete confirmada;
- dry-run hash-only criado;
- 173 candidatos sanitizados;
- private ID map restrito criado (`0600`);
- nenhum delete/mutation executado.

## Problema técnico

O SDK público do Honcho suporta `Session.delete()` e `ConclusionScope.delete()`, mas **não suporta message-level delete**. Apagar sessões inteiras pode remover contexto útil junto com ruído.

## Escopo se Lucas aprovar esta próxima etapa

1. Criar migrator DB-level local com flags obrigatórias:
   - default `--dry-run`;
   - `--commit` bloqueado sem approval reference;
   - reads a partir do private ID map restrito;
   - output hash-only.
2. Rodar somente `--dry-run --readback`.
3. Reportar contagens por tabela afetada (`messages`, `message_embeddings`, `queue` e derivados), sem raw IDs/conteúdo.
4. Gerar plano de rollback/readback para eventual etapa destrutiva futura.

## Fora de escopo

- Não deletar mensagens ainda.
- Não rodar `--commit`.
- Não apagar sessões inteiras.
- Não resetar workspace.
- Não expor raw content, PII, IDs crus, tokens ou secrets.

## Requisitos

- Usar snapshot já criado como rollback base.
- SQL transacional obrigatório em eventual execução futura.
- Readback antes/depois obrigatório em eventual execução futura.
- Novo approval específico para qualquer `--commit`.
- `values_printed=false`.

## Recomendação

Aprovar esta etapa de migrator dry-run/readback. Ainda não aprovar delete real.
